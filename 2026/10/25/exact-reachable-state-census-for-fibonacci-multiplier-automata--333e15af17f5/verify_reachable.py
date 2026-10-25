#!/usr/bin/env python3
"""Reproduce reachable-state counts for the bounded Zeckendorf multiplier automaton.
Run: python verify_reachable.py
Only reachable non-sink states are counted; no minimality is asserted.
"""
from collections import deque
from decimal import Decimal, localcontext
import json


def reachable(m):
    """Breadth-first search on the exact integer transition graph."""
    start = (0, 0, 0, 0)  # previous input bits, current difference, preceding difference
    states = {start}
    q = deque([start])
    while q:
        a0, b0, d, e = q.popleft()
        for a in (0, 1):
            if a0 and a:
                continue
            for b in (0, 1):
                if b0 and b:
                    continue
                new_d = d + e + b0 - m*a0 + b - m*a
                if not -m <= new_d <= 2*m-1:
                    continue
                v = (a, b, new_d, d)
                if v not in states:
                    states.add(v)
                    q.append(v)
    return states


def symbolic_partition(m):
    """Independently count circle cells from the exact boundary coincidences.

    Irrationality of 1/phi means c*(1/phi) belongs to the integers
    (respectively integers+1/phi) precisely for c=0 (respectively c=1).
    """
    total = 0
    profile = []
    for d in range(-m, 2*m):
        borders = 2*m
        if d == 2*m-2:
            borders -= 1
        if d == 2*m-1:
            borders -= 1
        borders += 1
        if d == m-2:
            borders -= 1
        if d == m-1:
            borders -= 1
        nstates = borders + 1
        profile.append(nstates)
        total += nstates
    return total, profile


def independent_numeric_states(m, limit=3000):
    """Sample actual padded valid numeral pairs via integer Zeckendorf evaluation.

    For each d and source X, use Y=m*X+d; g(X) is obtained by
    deleting the last digit of the canonical Zeckendorf representation.
    This does not use the recurrence defining the automaton.
    """
    fs=[1,2]
    while fs[-1] < m*limit + 3*m + 100:
        fs.append(fs[-1]+fs[-2])
    def rep(z):
        assert z>=0
        bits=[]
        for weight in reversed(fs):
            if z>=weight:
                bits.append(1)
                z-=weight
            else:
                bits.append(0)
        first=next((k for k,v in enumerate(bits) if v),len(bits)-1)
        return bits[first:]
    def num(w):
        return sum(b*fs[len(w)-i-1] for i,b in enumerate(w))
    seen=set()
    for x in range(limit):
        xr=rep(x)
        gx=num(xr[:-1])
        for d in range(-m,2*m):
            y=m*x+d
            if y<0:
                continue
            yr=rep(y)
            gy=num(yr[:-1])
            seen.add((xr[-1],yr[-1],d,gy-m*gx))
    return seen


def main():
    data=[]
    for m in range(1,61):
        states=reachable(m)
        analytic,prof=symbolic_partition(m)
        expected=6*m*m+6*m-4
        assert len(states)==analytic==expected, (m,len(states),analytic,expected)
        assert all(-m<=d<=2*m-1 and -m<=e<=2*m-1 for _,_,d,e in states)
        counts={d:0 for d in range(-m,2*m)}
        for a,b,d,e in states:
            counts[d]+=1
        assert [counts[d] for d in range(-m,2*m)]==prof
        if m<=12:
            samples=independent_numeric_states(m)
            assert samples==states, (m,len(samples),len(states),len(states-samples))
        if m in (1,2,3,5,10,20,40,60):
            data.append({'m':m,'reachable_non_sink':len(states),'formula':expected})
    print(json.dumps({'status':'PASS','graph_parameters_checked':'all m from 1 through 60',
       'independent_numeral_checks':'all m from 1 through 12; X=0,...,2999',
       'definition':'non-sink reachable states, not minimized states',
       'selected_counts':data},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
