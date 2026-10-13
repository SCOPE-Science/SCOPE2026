"""Independent checks for the fixing polynomial of two-set Kneser graphs.

No third-party modules are required. Every graph uses a fixed labeled ground set.
"""
import itertools
import math
from collections import Counter


def is_base_signatures(n, selected):
    words = [0] * n
    for i, (a, b) in enumerate(selected):
        words[a] |= 1 << i
        words[b] |= 1 << i
    return len(set(words)) == n


def is_base_components(n, selected):
    adj = [set() for _ in range(n)]
    for a, b in selected:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    isolated = 0
    for start in range(n):
        if start in seen: continue
        todo = [start]
        seen.add(start)
        comp = []
        while todo:
            v = todo.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        if len(comp) == 1: isolated += 1
        if len(comp) == 2: return False
    return isolated <= 1


def minimum_coefficient(n):
    q, r = divmod(n, 3)
    f = math.factorial
    if r == 1:
        return f(n)//(2**q * f(q))
    if r == 2:
        return f(n)*2//(3*2**(q-1)*f(q-1))
    no_single = f(n)//(2**q*f(q))
    with_five = f(n)*125//(120*2**(q-2)*f(q-2)) if q >= 2 else 0
    with_two_fours = f(n)*256//(2 * 24**2 * 2**(q-3)*f(q-3)) if q >= 3 else 0
    return no_single + with_five + with_two_fours


def poly_add(a,b,coef=1):
    c=a[:]
    if len(c)<len(b):c +=[0]*(len(b)-len(c))
    for i,v in enumerate(b):c[i]+=coef*v
    return c


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def all_graph_polynomial(n):
    N=n*(n-1)//2
    return [math.comb(N,k) for k in range(N+1)]


def fixing_polynomial_formula(n):
    # Mark components 1 or 2 as forbidden, then allow zero or one singleton.
    # H_n counts graphs with every component of size >=3.
    H=[[1]]
    for k in range(1,n+1):
        G=all_graph_polynomial(k)
        # Decomposing at vertex 0 into a singleton, an isolated edge,
        # or a component of >=3 is equivalent to the EGF recurrence.
        # H= exp(-t-y*t*t/2)G, using an explicit signed binomial sum.
        S=[0]
        for j in range(k+1):
            for e in range((k-j)//2+1):
                rem=k-j-2*e
                a=(-1)**(j+e)*math.factorial(k)//(math.factorial(j)*2**e*math.factorial(e)*math.factorial(rem))
                term=[0]*e + [a*t for t in all_graph_polynomial(rem)]
                S=poly_add(S,term)
        H.append(S)
    F=poly_add(H[n],H[n-1],n)
    assert all(x >=0 for x in F)
    return F


def check():
    records = []
    for n in range(5,8):
        edges=list(itertools.combinations(range(n),2))
        counts=Counter()
        for mask in range(1<<len(edges)):
            selected=[edges[j] for j in range(len(edges)) if mask & (1<<j)]
            a=is_base_signatures(n,selected)
            b=is_base_components(n,selected)
            assert a==b, (n, mask)
            if a:counts[len(selected)] +=1
        f=fixing_polynomial_formula(n)
        assert all(f[k]==counts[k] for k in range(len(f)))
        z=2*n//3
        assert counts[z]==minimum_coefficient(n)
        records.append((n, sum(counts.values()), z, counts[z], len(edges), 'full'))
    for n in (8,9):
        edges=list(itertools.combinations(range(n),2))
        z=2*n//3
        c=0
        for selected in itertools.combinations(edges,z):
            a=is_base_signatures(n,selected)
            b=is_base_components(n,selected)
            assert a==b
            c += a
        f=fixing_polynomial_formula(n)
        assert f[z]==c==minimum_coefficient(n)
        records.append((n, math.comb(len(edges),z),z,c,len(edges),'minimum'))
    for n in range(5,22):
        f=fixing_polynomial_formula(n)
        assert next(i for i,v in enumerate(f) if v)==2*n//3
        assert f[2*n//3]==minimum_coefficient(n)
        N=n*(n-1)//2
        assert f[-1]==1 and f[-2]==N
    print('PASS',records)

if __name__ == '__main__':
    check()
