#!/usr/bin/env python3
"""Exact arithmetic checks for sparse-polynomial critical-value trace identities."""
from fractions import Fraction as Q
from math import comb


def numerical_gaps(F):
    """Enumerate all gap sets whose Frobenius number is exactly F."""
    for mask in range(1 << (F-1)):
        gaps = {F} | {j for j in range(1, F) if mask & (1 << (j-1))}
        inside = [j for j in range(0, F) if j not in gaps]
        if all(a+b not in gaps for a in inside for b in inside if a+b <= F):
            yield gaps


def matrices_mult(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def trace_from_companion(F, gaps, coeff):
    """Trace of P over Q[z]/(P'), using only the companion matrix."""
    n = F-1
    if not n:
        return Q(0)
    C = [[Q(0) for _ in range(n)] for _ in range(n)]
    for j in range(n-1):
        C[j+1][j] = Q(1)
    for g in gaps:
        if g != F:
            C[g-1][n-1] -= Q(g*coeff.get(g, 0), F)
    M = [[Q(int(i==j)) for j in range(n)] for i in range(n)]
    total = Q(0)
    for k in range(1,F+1):
        M = matrices_mult(M,C)
        ck = Q(1) if k==F else Q(coeff.get(k,0))
        if ck:
            total += ck * sum(M[j][j] for j in range(n))
    return total


def truncated_product(A,B,maxdeg):
    C = [Q(0)]*(maxdeg+1)
    for i,v in enumerate(A):
        if v:
            for j,w in enumerate(B[:maxdeg+1-i]):
                if w: C[i+j] += v*w
    return C


def trace_from_log(F,gaps,coeff):
    """Separate coefficient-extraction evaluation of -F[t^F] A log A."""
    U = [Q(0)]*(F+1)
    for g in gaps:
        if g<F: U[F-g] = Q(g*coeff.get(g,0), F)
    power = [Q(1)]+[Q(0)]*F
    total=Q(0)
    for k in range(1,F+1):
        power=truncated_product(power,U,F)
        if k>=2:
            total += Q((-1)**k,k*(k-1))*power[F]
    return -F*total


def quadratic_coefficient_from_evaluations(F,gaps,direction):
    """Extract [e^2] T(e*v) from evaluations e=0,...,F."""
    vals = []
    for e in range(F+1):
        c={g:e*direction.get(g,0) for g in gaps if g<F}
        vals.append(trace_from_companion(F,gaps,c))
    total=Q(0)
    row=vals
    harmonic=Q(0)
    for k in range(F+1):
        if k>=2:
            harmonic += Q(1,k-1)
            total += row[0]*((-1)**k)*harmonic/k
        row=[row[j+1]-row[j] for j in range(len(row)-1)]
    return total


def verify():
    semigroups=trace_tests=quadratic_checks=0
    symmetric=pseudo=other=0
    for F in range(1,14):
      for G in numerical_gaps(F):
        semigroups += 1
        genus=len(G)
        delta=2*genus-F-1
        paired=sum(1 for g in G if g<F and (F-g) in G)
        assert paired==delta
        if delta==0: symmetric+=1
        elif delta==1: pseudo+=1
        else: other+=1
        for seed in range(3):
          c={g:(-1)**(g+seed)*(1+(3*g+seed)%5) for g in G if g<F}
          t=trace_from_companion(F,G,c)
          assert t==trace_from_log(F,G,c), (F,G,c,t,trace_from_log(F,G,c))
          if delta==0: assert t==0,(F,G,c,t)
          if delta==1:
            assert F%2==0
            assert t == -Q(F,8)*c[F//2]**2,(F,G,c,t)
          trace_tests+=1
        if F<=7:
          inds=sorted(G-{F})
          partial={}
          for g in inds:
            q=quadratic_coefficient_from_evaluations(F,G,{g:1})
            assert 2*q == (-Q(g*g,F) if 2*g==F else 0),(F,G,g,q)
            partial[g]=q
            quadratic_checks+=1
          for i,g in enumerate(inds):
            for h in inds[i+1:]:
              q=quadratic_coefficient_from_evaluations(F,G,{g:1,h:1})
              hh=q-partial[g]-partial[h]
              assert hh == (-Q(g*h,F) if g+h==F else 0),(F,G,g,h,hh)
              quadratic_checks+=1
    print(f'VERIFY_OK semigroups={semigroups} trace_companion_vs_log={trace_tests} '
          f'Hessian_entry_checks={quadratic_checks} symmetric={symmetric} '
          f'pseudosymmetric={pseudo} other={other} exact_rational=yes')
    for F,G in [(2,{1,2}),(5,{1,2,3,5}),(6,{1,2,3,6}),(11,{1,2,3,6,7,11})]:
      c={g:1 for g in G if g<F}
      print(f'CASE F={F} genus={len(G)} rank={2*len(G)-F-1} trace={trace_from_companion(F,G,c)}')

if __name__=='__main__':
    verify()
