"""Independent exact checks of opposite two-run shuffle identities.

Run with Python 3.9 or newer. No third-party dependencies.
The tests are finite consistency checks, not proofs of the all-parameter result.
"""

from functools import lru_cache
from itertools import product
from collections import deque
from math import comb


def direct_shuffle(u, v):
    """Enumerate distinct outputs by recursively choosing one next input."""
    @lru_cache(None)
    def rec(i, j):
        if i == len(u):
            return frozenset((v[j:],))
        if j == len(v):
            return frozenset((u[i:],))
        return frozenset({u[i] + x for x in rec(i + 1, j)} |
                         {v[j] + x for x in rec(i, j + 1)})
    return rec(0, 0)


def normal_form(a, b, c, d):
    p = frozenset(x for x in product('01', repeat=a+c) if x.count('0') == a)
    q = frozenset(x for x in product('01', repeat=b+d) if x.count('0') == d)
    return frozenset(''.join(x) + ''.join(y) for x in p for y in q)


def quotient_profile(words):
    """Distinct Myhill-Nerode residual languages after every non-dead prefix."""
    n = len(next(iter(words)))
    profile = []
    for i in range(n + 1):
        residuals = {}
        for word in words:
            residuals.setdefault(word[:i], set()).add(word[i:])
        profile.append(len({frozenset(s) for s in residuals.values()}))
    return profile


def predicted_profile(a, b, c, d):
    result = []
    for i in range(a+c+b+d + 1):
        if i <= a+c:
            result.append(min(a, i) - max(0, i-c) + 1)
        else:
            j = i-a-c
            result.append(min(d, j) - max(0, j-b) + 1)
    return result


def minimized_grid_shuffle(a, b, c, d):
    """Independent NFA-subset determinization and acyclic quotient minimization."""
    u='0'*a+'1'*b
    v='1'*c+'0'*d
    init=frozenset(((0,0),))
    queue=deque((init,))
    states={init}
    edges={}
    while queue:
        state=queue.popleft()
        for symbol in '01':
            out=set()
            for i,j in state:
                if i<len(u) and u[i]==symbol: out.add((i+1,j))
                if j<len(v) and v[j]==symbol: out.add((i,j+1))
            nxt=frozenset(out)
            edges[state,symbol]=nxt
            if nxt not in states:
                states.add(nxt)
                queue.append(nxt)
    n=len(u)+len(v)
    by_depth={k:[] for k in range(n+2)}
    for state in states:
        depth=sum(next(iter(state))) if state else n+1
        by_depth[depth].append(state)
    classes={}
    sig_to_class={}
    for depth in range(n+1,-1,-1):
        for state in by_depth[depth]:
            signature=((len(u),len(v)) in state,
                       classes.get(edges[state,'0'], -1),
                       classes.get(edges[state,'1'], -1))
            if signature not in sig_to_class:
                sig_to_class[signature]=len(sig_to_class)
            classes[state]=sig_to_class[signature]
    return len(sig_to_class)


def main():
    explicit=0
    for a,b,c,d in product(range(1,5), repeat=4):
        actual=direct_shuffle('0'*a+'1'*b, '1'*c+'0'*d)
        expected=normal_form(a,b,c,d)
        assert actual==expected, ('normal-form', a,b,c,d, actual ^ expected)
        assert len(actual)==comb(a+c,a)*comb(b+d,b)
        p=quotient_profile(actual)
        q=predicted_profile(a,b,c,d)
        assert p==q, ('quotient-profile', a,b,c,d,p,q)
        assert 1+sum(p)==(a+1)*(c+1)+(b+1)*(d+1)
        explicit+=1
    machine=0
    for a,b,c,d in product(range(1,9), repeat=4):
        expected=(a+1)*(c+1)+(b+1)*(d+1)
        actual=minimized_grid_shuffle(a,b,c,d)
        assert actual==expected, ('state-complexity', a,b,c,d,actual,expected)
        machine+=1
    print(f'VERIFY_OK explicit_languages_and_residuals={explicit} independent_grid_DFAs={machine}')

if __name__=='__main__':
    main()
