"""Finite checks for local-surjectivity on straight and twisted cubic ladders.

The infinite assertions also have the hand proof in RESULT.md; these
checks test its finite-state lemma and the explicit residue-class witnesses.
"""
from collections import deque


def columns(n, twisted):
    if n % 3 == 0 and not twisted:
        return [(i % 3, (i + 1) % 3) for i in range(n)]
    k = 2 if n % 3 == 1 else 1
    v = [(i % 3, (i + 1) % 3) for i in range(n - k)]
    if n % 3 == 0:
        v.append((0, 3))
    elif n % 3 == 1:
        v.extend(((0, 3), (3, 2)))
    else:
        v.append((2, 3))
    return v


def neighbours(n, twisted):
    d = [set() for _ in range(2 * n)]
    def link(a, b):
        d[a].add(b); d[b].add(a)
    for i in range(n):
        link(2*i, 2*i+1)
    for i in range(n - 1):
        for row in range(2):
            link(2*i+row, 2*(i+1)+row)
    for row in range(2):
        link(2*(n-1)+row, 1-row if twisted else row)
    assert all(len(x) == 3 for x in d)
    return d


def valid(v, d, k):
    f = [a for p in v for a in p]
    if max(f) >= k or min(f) < 0:
        return False
    return all(f[i] not in {f[j] for j in nb} and len({f[j] for j in nb}) >= 2
               for i, nb in enumerate(d))


def state_automaton():
    ss = [(a, b) for a in range(3) for b in range(3) if a != b]
    compatible = lambda s, t: s[0] != t[0] and s[1] != t[1]
    pairs = [(s,t) for s in ss for t in ss if compatible(s,t)]
    assert len(pairs) == 18
    next_states = {}
    for s,t in pairs:
        cand = [(t,u) for u in ss if compatible(t,u)
                and not(s[0] == u[0] == t[1])
                and not(s[1] == u[1] == t[0])]
        assert len(cand) in (0,1)
        next_states[s,t] = cand
    assert sum(map(len,next_states.values())) == 12
    for q in pairs:
        seen = {q}
        todo = deque([q])
        while todo:
            x = todo.popleft()
            for y in next_states[x]:
                if y not in seen:
                    seen.add(y); todo.append(y)
        s,t = q
        flip = ((s[1],s[0]),(t[1],t[0]))
        assert flip not in seen, (q, flip)
        if next_states[q]:
            x=q
            for _ in range(3):x=next_states[x][0]
            assert x==q
        else:assert len(seen)==1
    return len(pairs),sum(map(len,next_states.values()))


def exact_three_coloring_count(n, twisted):
    d = neighbours(n,twisted)
    ss = [(a,b) for a in range(3) for b in range(3) if a!=b]
    comp=lambda s,t:s[0]!=t[0] and s[1]!=t[1]
    def dv(s,t,u):
        return not(s[0] == u[0] == t[1] or s[1] == u[1] == t[0])
    # Enumerate all proper 3-coloring column sequences, pruning 2-dynamic
    # conditions as soon as their three neighboring columns are assigned.
    def search(cols):
        if len(cols)==n:
            first, second = cols[0],cols[1]
            prev = tuple(reversed(cols[-1])) if twisted else cols[-1]
            next_ = tuple(reversed(first)) if twisted else first
            return int(comp(cols[-1],next_) and dv(prev,first,second) and dv(cols[-2],cols[-1],next_))
        out = 0
        for s in ss:
            if not comp(cols[-1],s):continue
            if len(cols)>1 and not dv(cols[-2],cols[-1],s):continue
            cols.append(s)
            out += search(cols)
            cols.pop()
        return out
    return sum(search([s]) for s in ss)


def main():
    states, arcs=state_automaton()
    examples=0
    for n in range(3,601):
        for twisted in (False,True):
            d=neighbours(n,twisted)
            v=columns(n,twisted)
            k=4 if (twisted or n % 3 != 0) else 3
            assert valid(v,d,k),(n,twisted,v)
            examples+=1
    exhaustive=0
    for n in range(3,16):
        for twisted in (False,True):
            got=exact_three_coloring_count(n,twisted)
            expected=(12 if not twisted and n%3==0 else 0)
            assert got == expected,(n,twisted,got,expected)
            exhaustive+=1
    print('PASS: 3-color state-pair automaton:',states,'states,',arcs,'arcs')
    print('PASS: explicit witnesses:',examples,'graphs (n=3..600)')
    print('PASS: exact named 3-color counts:',exhaustive,'graphs (n=3..15)')

if __name__ == '__main__':main()
