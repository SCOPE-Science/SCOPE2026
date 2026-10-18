#!/usr/bin/env python3
"""Standalone verification of Mersenne-shift Thue--Morse state counts.

This checks finite instances independently in two ways: the residual
fingerprint criterion and direct minimization of a complete DFAO built
from consecutive Thue--Morse blocks. No finite check substitutes for
an all-parameter proof.
"""
from collections import deque


def tm(n):
    assert n >= 0
    return n.bit_count() & 1


def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def offsets(c):
    ans={c}
    for l in range(1,c.bit_length()+3):
        q,r=divmod(c,1<<l)
        ans.add(q)
        if r: ans.add(q+1)
    return tuple(sorted(ans))


def fingerprints(c, m_end):
    qs=offsets(c)
    return {tuple(tm(m+q) for q in qs) for m in range(m_end)}


def word_transition(mask,c,b):
    result=0
    for j in range(c+1):
        r=b+j
        bit=((mask>>(r//2))&1) ^ (r&1)
        result |= bit<<j
    return result


def dfa_states_and_minimization(c):
    start=sum(tm(j)<<j for j in range(c+1))
    states=[start]; index={start:0}; edges=[]
    for state in states:  # intentional BFS with appended states
        row=[]
        for b in (0,1):
            nxt=word_transition(state,c,b)
            if nxt not in index:
                index[nxt]=len(states);states.append(nxt)
            row.append(index[nxt])
        edges.append(tuple(row))
    output=[(x>>c)&1 for x in states]
    cls=output[:]
    while True:
        sig=[(output[i],cls[edges[i][0]],cls[edges[i][1]]) for i in range(len(states))]
        dictionary={key:z for z,key in enumerate(sorted(set(sig)))}
        new=[dictionary[s] for s in sig]
        # Old classes might have different labels, so compare equivalence
        # by both size and indexed pairs, not raw label equality.
        if len(set(new))==len(set(cls)):
            assert all((cls[i]==cls[j])==(new[i]==new[j]) for i in range(len(states)) for j in range(i))
            return len(states),len(set(new))
        assert len(set(new))>len(set(cls))
        cls=new


def main():
    assert offsets(1)==(0,1)
    for k in range(1,12):
        c=(1<<k)-1
        expected=2*fibonacci(k+4)-6
        cap=1<<(k+4)
        observed=len(fingerprints(c,cap))
        assert observed==expected, (k,c,observed,expected)
        print(f'FINGERPRINT k={k:2} shift={c:5} scanned_prefixes={cap:6} distinct={observed:5} formula={expected:5} PASS')
    for k in range(1,8):
        c=(1<<k)-1
        raw,minimal=dfa_states_and_minimization(c)
        expected=2*fibonacci(k+4)-6
        assert minimal==expected,(k,raw,minimal,expected)
        print(f'DFA_MINIMIZATION k={k:2} shift={c:5} raw={raw:5} minimal={minimal:5} formula={expected:5} PASS')
    print('VERIFY_OK')

if __name__=='__main__':main()
