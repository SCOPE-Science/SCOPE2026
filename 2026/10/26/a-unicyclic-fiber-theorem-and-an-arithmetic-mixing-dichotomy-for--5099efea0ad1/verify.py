"""Finite checks for the rational-angle Feres transition-graph theorem.

Only the integer graph statements are checked exactly. Trigonometric
probability and detailed-balance checks are numerical tests, not proofs.
Run with Python 3, no third-party packages.
"""
from math import pi, cos, sin, tan, gcd
from collections import deque


def predicted_edges(n, m):
    edges = set()
    def add(a, b):
        assert 0 <= a < n and 0 <= b < n and a != b
        edges.add((min(a,b), max(a,b)))
    for j in range(n-2*m):
        add(j, j+2*m)
    for j in range(m, 2*m):
        add(j, 4*m-1-j)
    for j in range(n-3*m, n-2*m):
        add(j, 2*n-4*m-1-j)
    return edges


def u(a, x):
    return (1 + tan(a)*cos(x)/sin(x))/2


def probabilities(x, a):
    # Samples here avoid all branch-boundary positions.
    z = 2*cos(2*a)
    if x < a: p1 = 1.
    elif x < pi-3*a: p1 = u(a,x)
    elif x < pi-2*a: p1 = z*u(2*a,x)
    else: p1 = 0.
    if x < pi-3*a: p2 = 0.
    elif x < pi-2*a: p2 = u(a,x)-z*u(2*a,x)
    elif x < pi-a: p2 = u(a,x)
    else: p2 = 0.
    if x < 2*a: p3 = 0.
    elif x < 3*a: p3 = z*u(2*a,-x)
    elif x < pi-a: p3 = u(a,-x)
    else: p3 = 1.
    if x < a: p4 = 0.
    elif x < 2*a: p4 = u(a,-x)
    elif x < 3*a: p4 = u(a,-x)-z*u(2*a,-x)
    else: p4 = 0.
    return [p1,p2,p3,p4]


def check(n, m, frac):
    assert n>6*m and gcd(n,m)==1
    h=pi/n; a=m*h; t=frac*h
    x=[(j+(j%2))*h+((-1)**j)*t for j in range(n)]
    transitions=(lambda z:z+2*a,lambda z:2*pi-4*a-z,
                 lambda z:z-2*a,lambda z:4*a-z)
    e=predicted_edges(n,m)
    assert len(e)==n
    adj=[set() for _ in range(n)]
    for i,j in e: adj[i].add(j);adj[j].add(i)
    leaves=[j for j in range(n) if len(adj[j])==1]
    assert len(leaves)==2*m
    assert all(len(adj[j]) in (1,2,3) for j in range(n))
    assert sum(len(adj[j])==3 for j in range(n))==2*m
    seen={0}; todo=deque([0])
    while todo:
        i=todo.popleft()
        for j in adj[i]-seen: seen.add(j);todo.append(j)
    assert len(seen)==n
    core=set(range(n))-set(leaves)
    assert len(core)==n-2*m
    assert all(len(adj[i]&core)==2 for i in core)
    weights=[sin(z) for z in x]
    if n%2: Z=cos(h/2-t)/sin(h/2)
    else: Z=2*cos(h-t)/sin(h)
    assert abs(sum(weights)-Z)<2e-11
    P=[[0.]*n for _ in range(n)]
    for i,xi in enumerate(x):
        p=probabilities(xi,a)
        assert all(q>=-5e-12 for q in p),(n,m,i,p)
        assert abs(sum(p)-1)<5e-12,(n,m,i,p)
        for k,q in enumerate(p):
            if q<1e-11: continue
            y=transitions[k](xi)
            match=[j for j,z in enumerate(x) if abs(y-z)<1e-10]
            assert len(match)==1,(n,m,i,k,y)
            P[i][match[0]]+=q
    edges_actual={ (i,j) for i in range(n) for j in range(i+1,n) if P[i][j]>1e-11 or P[j][i]>1e-11}
    assert edges_actual==e,(n,m,edges_actual^e)
    assert all(P[i][i]<1e-10 for i in range(n))
    assert all(abs(weights[i]*P[i][j]-weights[j]*P[j][i])<5e-12
               for i,j in e)
    assert all(abs(sum(weights[i]*P[i][j] for i in range(n))-weights[j])<1e-11
               for j in range(n))
    if n%2==0:
        colors=[None]*n;colors[0]=0;todo=deque([0])
        while todo:
            i=todo.popleft()
            for j in adj[i]:
                if colors[j] is None: colors[j]=1-colors[i];todo.append(j)
                else: assert colors[j]!=colors[i]
        assert abs(sum(w for w,c in zip(weights,colors) if c==0)/Z-0.5)<1e-11
    else:
        # The unique core cycle has odd length: nonbipartiteness is exact.
        assert len(core)%2==1
    return len(e)

if __name__=='__main__':
    cases=0
    for n in range(7,101):
        for m in range(1,(n-1)//6+1):
            if n<=6*m or gcd(n,m)!=1: continue
            for frac in (0.137,0.381,0.5,0.769):
                check(n,m,frac)
                cases+=1
    print('PASS:',cases,'exact integer graph and numerical detailed-balance cases')
