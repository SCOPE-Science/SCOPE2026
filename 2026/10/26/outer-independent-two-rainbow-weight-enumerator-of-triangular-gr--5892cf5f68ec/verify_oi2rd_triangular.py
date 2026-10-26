"""Definition-level checks of outer-independent 2-rainbow labellings of triangular graphs."""
from itertools import combinations,product
from collections import Counter
from math import factorial, comb


def polynomial_formula(n):
    N=comb(n,2)
    pol=Counter()
    for t in range(n//2+1):
        ways=factorial(n)//(2**t*factorial(t)*factorial(n-2*t))
        L=N-t
        for k in range(t+1):
            multiplier=ways*(1 if k==0 else 2)*(-1)**k*comb(t,k)
            U=2*k*(n-k-1)
            # z^L * (z+2)^(L-U)
            for h in range(L-U+1):
                pol[L+h]+= multiplier*comb(L-U,h)*2**(L-U-h)
    return Counter({a:b for a,b in pol.items() if b})


def definition_polynomial(n):
    edges=list(combinations(range(n),2))
    ecount=len(edges)
    adjacent=[tuple(j for j,(a,b) in enumerate(edges) if j!=i and (a in (u,v) or b in (u,v)))
              for i,(u,v) in enumerate(edges)]
    # label 0 empty, 1 {1}, 2 {2}, 3 {1,2}; bitmask union tests
    count=Counter()
    for assignment in product(range(4),repeat=ecount):
        empties=[i for i,x in enumerate(assignment) if not x]
        if any(j in adjacent[i] for i,j in combinations(empties,2)):
            continue
        if any(not (3 == __import__('functools').reduce(lambda a,j: a|assignment[j], adjacent[i], 0)) for i in empties):
            continue
        wt=sum((x==1 or x==2)+2*(x==3) for x in assignment)
        count[wt]+=1
    return count


def min_colorings_by_matching(n):
    edges=list(combinations(range(n),2))
    t=n//2
    match=[]
    def rec(vertices, chosen):
        if len(chosen)==t:
            match.append(tuple(chosen)); return
        if not vertices:
            return
        v=vertices[0]
        if len(vertices)>2*(t-len(chosen)):
            rec(vertices[1:],chosen)
        for j in range(1,len(vertices)):
            w=vertices[j]
            rec(vertices[1:j]+vertices[j+1:],chosen+[(v,w)])
    rec(tuple(range(n)),[])
    count=0
    for m in match:
        mset=set(m)
        active=[e for e in edges if e not in mset]
        adj=[[j for j,e in enumerate(active) if e[0] in uv or e[1] in uv] for uv in m]
        for colors in product((1,2),repeat=len(active)):
            if all(set(colors[j] for j in a)=={1,2} for a in adj):
                count+=1
    return len(match),count


if __name__=='__main__':
    for n in range(3,6):
        a=definition_polynomial(n)
        b=polynomial_formula(n)
        assert a==b,(n,a,b)
        print(f'n={n}, all 4-label assignments checked: {4**comb(n,2)}, polynomial={dict(sorted(a.items()))}')
    for n in range(3,7):
        t=n//2
        L=comb(n,2)-t
        m=factorial(n)//(2**t*factorial(t)*factorial(n-2*t))
        T=2**L+2*sum((-1)**k*comb(t,k)*2**(L-2*k*(n-k-1)) for k in range(1,t+1))
        assert polynomial_formula(n)[L]==m*T
        if n<=6:
            q,v=min_colorings_by_matching(n)
            assert (q,v)==(m,m*T),(n,q,v,m,m*T)
        print(f'n={n}: min_weight={L}, matchings={m}, valid minimum labellings={m*T}')
    print('ALL CHECKS PASSED')
