"""Exact checks for two-site vaccination on a cycle in the seeded bond model.
Run with: python3 verify.py
Requires only the Python standard library. This is finite verification,
not a replacement for the all-size proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations


def constants(p, q):
    r = p*(1-q)
    A = (1-p)/(1-r)
    B = p*q/(1-r)
    K = 2*(1-q)*A*B/(1-r)
    c = 1-(1-q)*A*A
    theta = (1-q)*(p*q+2*(1-p))/(q*(1-p+p*q))
    return r, A, B, K, c, theta


def f(s, p, q):
    r,A,B,K,c,theta = constants(p,q)
    if s==0: return K
    return K*r**s-(1-q)*B*B*s*r**(s-1)


def H(s, p, q):
    r,A,B,K,c,theta = constants(p,q)
    if s==0: return Q(0)
    return c*s-K+f(s,p,q)


def exact_percolation(n, V, p, q):
    live=[v for v in range(n) if v not in V]
    edge=[(u,(u+1)%n) for u in range(n) if u not in V and (u+1)%n not in V]
    total=Q(0)
    for mask in range(1<<len(edge)):
        parent={u:u for u in live}
        def root(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        for j,(u,v) in enumerate(edge):
            if (mask>>j)&1:
                a,b=root(u),root(v)
                parent[a]=b
        comps={}
        for u in live:
            rt=root(u);comps[rt]=comps.get(rt,0)+1
        infected=sum(sz*(1-(1-q)**sz) for sz in comps.values())
        open_count=mask.bit_count()
        total+=p**open_count*(1-p)**(len(edge)-open_count)*infected
    return total


def arc_lengths(n, V):
    u,v=sorted(V)
    return v-u-1,n-(v-u)-1


def verify():
    count=0
    for p,q,maxn in [(Q(1,2),Q(1,2),11),
                       (Q(1,4),Q(2,3),8),
                       (Q(3,4),Q(1,3),8)]:
        r,A,B,K,c,theta=constants(p,q)
        for s in range(1,75):
            left=H(s+1,p,q)-2*H(s,p,q)+H(s-1,p,q)
            right=p**s*q*(1-q)**(s-1)*(2-(s+1)*q)
            assert left==right,(s,p,q,left,right)
            if s>=1:
                assert f(s+1,p,q)-f(s,p,q)==(1-q)*B**2*(1-r)*r**(s-1)*(s-theta)
        for n in range(3,maxn+1):
            for V in combinations(range(n),2):
                a,b=arc_lengths(n,V)
                target=H(a,p,q)+H(b,p,q)
                brute=exact_percolation(n,set(V),p,q)
                assert brute==target,(n,V,p,q,target,brute)
                count+=1
    for n in range(4,72):
        N=n-2
        values=[H(a,Q(1,2),Q(1,2))+H(N-a,Q(1,2),Q(1,2))
                for a in range(N//2+1)]
        mi=min(values)
        best=[a for a,x in enumerate(values) if x==mi]
        expect=([1] if n==4 or n==5 else [2,3] if n==8 else [2])
        assert best==expect,(n,best,expect)
    # Stabilization towards the explicitly predicted finite short-gap length.
    for p,q in [(Q(1,4),Q(1,5)),(Q(3,4),Q(1,5)),
                (Q(1,2),Q(1,2)),(Q(3,4),Q(4,5))]:
        r,A,B,K,c,theta=constants(p,q)
        m=max(1,theta.numerator//theta.denominator+1)
        for N in [300,350]:
            vals=[H(s,p,q)+H(N-s,p,q) for s in range(1,N//2+1)]
            best=[s+1 for s,val in enumerate(vals) if val==min(vals)]
            assert best==[m],(p,q,N,m,best)
    print('PASS: independent edge-configuration enumeration',count,'cycle-vaccine cases')
    print('PASS: curvature and finite-difference identities for 3 rational parameter pairs, s=1..74')
    print('PASS: p=q=1/2 optimal gaps on every cycle n=4..71')
    print('PASS: four asymptotic short-gap instances at n=302,352')


if __name__=='__main__':
    verify()
