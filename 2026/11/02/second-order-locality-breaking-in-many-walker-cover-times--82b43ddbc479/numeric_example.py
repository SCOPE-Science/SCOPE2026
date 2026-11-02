"""Numerical finite-N example, using only Python's standard library.

Independent of the proof and the exact coefficient checker. The mathematical
limit is proved in RESULT.md; these calculations provide finite-N diagnostics.
"""
from math import exp, factorial, pi, sqrt


def survival_killed(edges, forbidden, t, start=0, terms=65):
    n=1+max(max(e) for e in edges)
    E=[i for i in range(n) if i not in forbidden]
    Q=[[0.0 for _ in E] for __ in E]
    for a,b in edges:
        if a in E and b in E:
            Q[E.index(a)][E.index(b)]+=1.0
            Q[E.index(b)][E.index(a)]+=1.0
    for i in E:
        Q[E.index(i)][E.index(i)]=-sum((i==a or i==b) for a,b in edges)
    rate=max(-Q[i][i] for i in range(len(E)))
    if rate==0:return 1.0
    P=[[float(i==j)+Q[i][j]/rate for j in range(len(E))] for i in range(len(E))]
    vec=[1.0]*len(E)
    mu=rate*t
    coeff=exp(-mu)
    ans=coeff*vec[E.index(start)]
    for k in range(1,terms):
        vec=[sum(P[i][j]*vec[j] for j in range(len(E))) for i in range(len(E))]
        coeff*=mu/k
        ans+=coeff*vec[E.index(start)]
    return min(1.0,max(0.0,ans))


def cover_mean(N,edges,steps=2400):
    upper=15.0; h=upper/steps
    s=0.0
    for k in range(steps+1):
        x=k*h; t=x/sqrt(N)
        pb=survival_killed(edges,{2},t)**N
        pz=survival_killed(edges,{3},t)**N
        pbz=survival_killed(edges,{2,3},t)**N
        weight=1 if k==0 or k==steps else (4 if k%2 else 2)
        s+=weight*(pb+pz-pbz)
    return s*h/(3*sqrt(N))


def run():
    baseline=[(0,1),(0,2),(1,3)]
    pendant=baseline+[(1,4)]
    c0=sqrt(pi/2)
    for N in (100,1000,10000):
        base=N*(cover_mean(N,baseline)-c0/sqrt(N))
        leaf=N*(cover_mean(N,pendant)-c0/sqrt(N))
        print(f'N={N:5d} second coefficients: baseline={base:.8f}, pendant={leaf:.8f}')
        if N==10000:
            assert abs(base-4/3)<0.04
            assert abs(leaf-5/3)<0.04
            assert leaf>base
    print('PASS finite-N numerical checks (not a proof of the limit)')

if __name__=='__main__':run()
