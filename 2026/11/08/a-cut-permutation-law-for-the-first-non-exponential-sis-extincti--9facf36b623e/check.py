"""Exact-arithmetic tests of finite-network SIS extinction-time asymptotics."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def cut(edges, surviving):
    return sum((u in surviving) != (v in surviving) for u, v in edges)


def coefficient(n, edges):
    # All deletion sequences, counted once each.
    total = F(0)
    hazard = F(0)
    for perm in permutations(range(n)):
        surviving = set(range(n))
        cuts = []
        for removed in perm[:-1]:
            surviving.remove(removed)
            c = cut(edges, surviving)
            assert c > 0
            cuts.append(c)
        weight = F(1)
        for c in cuts: weight /= c
        hazard += weight
        total += 2*weight*sum((F(1,c) for c in cuts), F(0))
    return total, hazard


def solve(A, b):
    n=len(b)
    a=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        mul=a[j][j]; a[j]=[x/mul for x in a[j]]
        for i in range(n):
            if i==j: continue
            mul=a[i][j]
            if mul: a[i]=[x-mul*y for x,y in zip(a[i],a[j])]
    return [a[i][-1] for i in range(n)]


def moments(n, edges, lam):
    states=list(range(1,1<<n))
    where={s:i for i,s in enumerate(states)}
    A=[[F(0) for _ in states] for _ in states]
    for idx,s in enumerate(states):
        infected=[i for i in range(n) if s & (1<<i)]
        healthy=set(range(n))-set(infected)
        for v in infected:
            A[idx][idx] += 1
            to=s^(1<<v)
            if to: A[idx][where[to]] -= 1
        for v in healthy:
            rate=lam*sum((u,v) in edges or (v,u) in edges for u in infected)
            if rate:
                A[idx][idx] += rate
                A[idx][where[s|(1<<v)]] -= rate
    m=solve(A,[F(1)]*len(states))
    m2=solve(A,[2*x for x in m])
    mean=m[-1]; cv2=(m2[-1]-mean**2)/mean**2
    return cv2


def test():
    examples=[
      (2, [(0,1)],'edge'),
      (3, [(0,1),(1,2)],'P3'),
      (3, [(0,1),(1,2),(0,2)],'K3'),
      (4, [(0,1),(1,2),(2,3)],'P4'),
      (4, [(0,1),(1,2),(2,3),(3,0)],'C4'),
      (4, [(0,1),(0,2),(0,3)],'K1,3'),
      (4, [(i,j) for i in range(4) for j in range(i+1,4)],'K4')]
    for n,edges,label in examples:
        C,H=coefficient(n,edges)
        print(label,'n=',n,'R=',H,'C=',C)
        gaps=[]
        for rate in [10,20,40]:
            cv2=moments(n,edges,F(rate))
            gap=(1-cv2)*rate**n
            gaps.append(gap)
            assert gap>0
        # convergence of scaled coefficient from below in tested cases
        assert all(gaps[i]<gaps[i+1]<C for i in range(2)), (label,gaps,C)
        print(' scaled deficits at 10,20,40:',*[float(x) for x in gaps])
    for n in range(2,7):
        E=[(i,j) for i in range(n) for j in range(i+1,n)]
        C,_=coefficient(n,E)
        H=sum((F(1,i) for i in range(1,n)),F(0))
        assert C==4*H/factorial(n-1)
    print('PASS: all seven graphs and all five complete-graph constants')

if __name__=='__main__': test()
