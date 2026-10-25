"""Exact checks for symmetric negative-doubling survivor zeta identities.

Requires Python 3.10+ and SymPy. Finite tests supplement the analytic proof.
"""
from fractions import Fraction as Q
from math import gcd
import sympy as sp


def markov(k):
    m = 2*k+1
    states = [j for j in range(m) if j != k]
    A = sp.zeros(2*k)
    for row,j in enumerate(states):
        base = m-2*j-2 if j < k else 2*m-2*j-2
        for dest in [base,base+1]:
            if dest in states:
                A[row,states.index(dest)] = 1
    return states,A


def periodic_count(k,n):
    """Enumerate fixed points of (-2)^n on the circle by exact integers."""
    q = abs((-2)**n-1)
    count=0
    for j in range(q):
        s=j
        good=True
        for t in range(n):
            if (2*k+1)*s > k*q and (2*k+1)*s < (k+1)*q:
                good=False
                break
            s=(-2*s)%q
        count += good
    return count


def iterate_fraction(x,n):
    for _ in range(n):
        x=(-2*x)%1
    return x


def refined_graph():
    D=[Q(0),Q(1,9),Q(1,7),Q(2,9),Q(2,7),Q(3,7),Q(4,9),
       Q(5,9),Q(4,7),Q(5,7),Q(7,9),Q(6,7),Q(8,9),Q(1)]
    nodes=[i for i in range(13) if i!=6]
    edges={}
    for j in nodes:
        edges[j]=[]
        for i in nodes:
            mid=(D[i]+D[i+1])/2
            preimages=[(1-mid)/2,(2-mid)/2]
            if any(D[j]<p<D[j+1] for p in preimages):
                edges[j].append(i)
    # Reachability-based SCCs on these twelve states.
    reach={u:{u} for u in nodes}
    for u in nodes:
        stack=[u]
        while stack:
            v=stack.pop()
            for w in edges[v]:
                if w not in reach[u]:
                    reach[u].add(w);stack.append(w)
    components=[]
    unseen=set(nodes)
    while unseen:
        u=min(unseen)
        component={v for v in nodes if v in reach[u] and u in reach[v]}
        components.append(component)
        unseen-=component
    return D,edges,components


def main():
    x=sp.Symbol('x')
    polys={
      3:(x-1)*(x+1)*(x*x-x-1)*(x*x-x+1),
      4:(x-1)*(x+1)**3*(x*x-x-1)*(x*x-x+1),
    }
    for k in [3,4]:
        states,A=markov(k)
        assert sp.factor(A.charpoly(x).as_expr()-polys[k])==0
        for n in range(1,15):
            p=periodic_count(k,n)
            tr=int(sp.trace(A**n))
            expected_correction=(-1)**n if k==3 else 3*(-1)**n-6*(n%3==0)
            assert tr-p==expected_correction,(k,n,tr,p)
            if k==3:
                assert p==periodic_count(3,n)
            else:
                assert p-periodic_count(3,n)==6*(n%3==0)
    print('MARKOV_CHARACTERISTIC_AND_PERIODIC_TRACE_FORMULAS_PASS 28')

    D,edges,components=refined_graph()
    assert {frozenset(s) for s in components}=={
      frozenset([0,12]),frozenset([2,4,8,10]),
      frozenset([1,3,5,7,9,11])}
    assert all(edges[i] for i in edges)
    assert all(v in edges[u] for u,v in zip([5,1,9,7,11,3],[1,9,7,11,3,5]))
    # The only closed six-step paths through the new annuli yield these
    # affine branches. The corresponding fixed points are their old endpoints.
    a=Q(3,7)+Q(1,10000)
    b=Q(4,7)-Q(1,10000)
    for start,branch,offset,root in [
       (a,[5,1,9,7,11,3],27,Q(3,7)),
       (b,[7,11,3,5,1,9],36,Q(4,7))]:
        orbit=[];cur=start
        for _ in range(6):
            orbit.append(next(j for j in edges if D[j]<cur<D[j+1]))
            cur=(-2*cur)%1
        assert orbit==branch,(orbit,branch)
        assert cur==64*start-offset
        # Compose exact affine branches from the six cells; the same
        # expression holds on every orbit following this six-cell word.
        coefficient,intercept=1,0
        for cell in branch:
            shift=1 if D[cell+1]<=Q(1,2) else 2
            coefficient,intercept=-2*coefficient,shift-2*intercept
        assert coefficient==64 and intercept==-offset
        assert Q(offset,63)==root
    print('REFINED_GRAPH_AND_SIX_CYCLE_BOUNDARY_RIGIDITY_PASS 12')

    for x0 in [Q(4,9),Q(5,9)]:
        assert iterate_fraction(x0,3)==x0
        assert [iterate_fraction(x0,j) for j in range(3)] == (
          [Q(4,9),Q(1,9),Q(7,9)] if x0==Q(4,9) else
          [Q(5,9),Q(8,9),Q(2,9)])
    for a in [Q(3,7),Q(13,30),Q(7,16)]:
      for n in range(1,13):
        q=abs((-2)**n-1)
        count=0
        for j in range(q):
          t=j; good=True
          for _ in range(n):
            if a.denominator*t > a.numerator*q and a.denominator*t < (a.denominator-a.numerator)*q:
              good=False;break
            t=(-2*t)%q
          count+=good
        assert count==periodic_count(3,n),(a,n,count)
    print('INTERIOR_PLATEAU_AND_ENDPOINT_ORBITS_PASS 38')
    print('INFINITE_PERIODIC_RIGIDITY_AND_DIMENSION_REQUIRE_ANALYTIC_PROOF')

if __name__=='__main__': main()
