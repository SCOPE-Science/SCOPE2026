"""Exact arithmetic checks for the finite-dimensional quadratic Fourier moment identity.
No numerical sampling is used as proof of the all-dimensional inequality.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from random import Random


def edges(n): return list(combinations(range(n), 2))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm(a): return a[0]*a[0]+a[1]*a[1]
def real_dot(a,b): return a[0]*b[0]+a[1]*b[1]


def fourth_via_convolution(n, a):
    ee = edges(n)
    mon = {}
    for j, (u, v) in enumerate(ee):
        for k, (s, t) in enumerate(ee):
            exp = tuple(int(w in (u, v)) + int(w in (s, t)) for w in range(n))
            mon[exp] = add(mon.get(exp, (0,0)), mul(a[j],a[k]))
    return sum(norm(c) for c in mon.values())


def fourth_via_cycles(n, a):
    ee = edges(n); ind = {e: j for j, e in enumerate(ee)}
    x = [norm(v) for v in a]; S = sum(x)
    q = 2*S*S - sum(t*t for t in x)
    for i,j,k,l in combinations(range(n), 4):
        X = mul(a[ind[i,j]],a[ind[k,l]])
        Y = mul(a[ind[i,k]],a[ind[j,l]])
        Z = mul(a[ind[i,l]],a[ind[j,k]])
        q += 8*( real_dot(X,Y) + real_dot(X,Z) + real_dot(Y,Z) )
    return q


def optimal_constant(n):
    N = comb(n,2)
    return F(2) - F(1,N) + F(24*comb(n,4),N*N)


def stability_coefficient(n):
    return min(F(3),F(1)+F((n-3)*(n-4),n-1))


def run():
    rng = Random(424242); assertions = 0
    for n in range(4,10):
        ee=edges(n); N=len(ee)
        all_one=[(1,0)]*N
        lhs=fourth_via_convolution(n,all_one)
        assert F(lhs,N*N)==optimal_constant(n)
        assertions+=1
        # Three eigenspaces of the line graph: 1, incidence row-space differences, incidence kernel.
        A=[[int(bool(set(e)&set(f))) if i!=j else 0 for j,f in enumerate(ee)] for i,e in enumerate(ee)]
        for i in range(N):
            assert sum(A[i])==2*(n-2)
            assertions+=1
        for s in range(n-1):
            v=[int(s in e)-int((n-1) in e) for e in ee]
            av=[sum(A[i][j]*v[j] for j in range(N)) for i in range(N)]
            assert av==[(n-4)*z for z in v]
            assertions+=1
        # Matrix polynomial (A-2(n-2)I)(A-(n-4)I)(A+2I)=0.
        for j in range(N):
            v=[int(i==j) for i in range(N)]
            for root in (-2,n-4,2*(n-2)):
                v=[sum(A[i][k]*v[k] for k in range(N))-root*v[i] for i in range(N)]
            assert v==[0]*N
            assertions+=1
        for trial in range(80):
            a=[(rng.randint(-4,4),rng.randint(-4,4)) for _ in ee]
            if not any(a): continue
            x=[norm(t) for t in a]; S=sum(x)
            raw=fourth_via_convolution(n,a)
            cyc=fourth_via_cycles(n,a)
            assert raw==cyc,(n,trial,raw,cyc)
            deficit=optimal_constant(n)*S*S-F(raw)
            dispersion=sum((F(t)-F(S,N))**2 for t in x)
            assert deficit>=stability_coefficient(n)*dispersion,(n,trial,deficit,dispersion)
            assertions+=2
        for trial in range(15):
            phases=[(rng.choice([-1,1]),rng.choice([-1,1])) for _ in range(n)]
            a=[mul(phases[i],phases[j]) for i,j in ee]
            assert F(fourth_via_convolution(n,a),sum(norm(t) for t in a)**2)==optimal_constant(n)
            assertions+=1
    print('all exact assertions:',assertions)
    for n in range(4,10):
        print(n, 'edges',comb(n,2),'fourth power constant',optimal_constant(n),'stability coefficient',stability_coefficient(n))

if __name__=='__main__': run()
