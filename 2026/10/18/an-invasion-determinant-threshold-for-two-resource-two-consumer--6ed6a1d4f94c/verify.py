"""Exact-rational checks accompanying the 2+2 antagonistic ecological census.

Uses only the Python standard library. Finite checks supplement the written proof.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(A, b):
    A = [[F(v) for v in row] + [F(rhs)] for row, rhs in zip(A, b)]
    n = len(A)
    if n == 0:
        return []
    for k in range(n):
        p = next((j for j in range(k, n) if A[j][k] != 0), None)
        if p is None:
            return None
        A[k], A[p] = A[p], A[k]
        div = A[k][k]
        A[k] = [z/div for z in A[k]]
        for j in range(n):
            if j != k:
                div = A[j][k]
                A[j] = [u - div*v for u, v in zip(A[j], A[k])]
    return [row[-1] for row in A]


def all_isolated_equilibria(d):
    # The active-coordinate equations are f_i=R_i+sum_j B_ij z_j=0.
    B = [[F(-1), F(0), F(-3), F(-1)],
         [F(0), F(-1), F(-1), F(-3)],
         [F(1), d, F(-1), F(0)],
         [d, F(1), F(0), F(-1)]]
    R = [F(3), F(3), F(-3), F(-3)]
    found = []
    for size in range(5):
        for support in combinations(range(4), size):
            solution = solve([[B[i][j] for j in support] for i in support],
                             [-R[i] for i in support])
            if solution is None or any(z <= 0 for z in solution):
                continue
            full = [F(0)]*4
            for i,z in zip(support,solution):
                full[i]=z
            assert all(full[i] * (R[i] + sum(B[i][j]*full[j] for j in range(4))) == 0 for i in range(4))
            found.append(tuple(full))
    return set(found)


def general_sample_checks():
    n=0
    for a in [F(2),F(3),F(4)]:
      for b in [F(1),F(3,2)]:
       if a<=b: continue
       for d in [F(3,2),F(2),F(3)]:
        for c in [F(1,2),F(1)]:
         if d<=c: continue
         for r in [F(1),F(3)]:
          upper=(c+d)*r
          lower=max(F(0),r*((a-b)*d-F(1))/a)
          if lower>=upper: continue
          m=(upper+lower)/2
          Q=1+(a-b)*(c-d)
          S=1+(a+b)*(c+d)
          T=1+a*c+b*d
          x=(r+(a+b)*m)/S
          y=((c+d)*r-m)/S
          yy=((c+d)*r-m)/T
          u=(r*(1-(a-b)*d)+a*m)/T
          v=(r*(1+(a-b)*c)+b*m)/T
          assert min(x,y,yy,u,v)>0
          assert r-x-(a+b)*y==0
          assert -m-y+(c+d)*x==0
          assert r-u-a*yy==0 and r-v-b*yy==0
          assert -m-yy+c*u+d*v==0
          assert (-m+d*u+c*v)==Q*yy
          assert (1+(a+b)*(c+d))*x*y>0
          assert (1+(a-b)*(c-d))*x*y == Q*x*y
          # J_resident is dissipative in this rational diagonal metric.
          P=[c/(a*u),d/(b*v),1/yy]
          J=[[-u,F(0),-a*u], [F(0),-v,-b*v], [c*yy,d*yy,-yy]]
          metric=[[P[i]*J[i][j]+P[j]*J[j][i] for j in range(3)] for i in range(3)]
          assert metric==[[-2*c/a,F(0),F(0)], [F(0),-2*d/b,F(0)], [F(0),F(0),F(-2)]]
          n+=1
    return n


def main():
    n=general_sample_checks()
    assert n >= 60
    for d in (F(5,4),F(7,4)):
        found=all_isolated_equilibria(d)
        assert len(found)==9, (d,len(found),found)
        star=(F(15)/(5+4*d),)*2+(F(3)*d/(5+4*d),)*2
        edge1=(F(6)*(2-d)/(4+d),F(12)/(4+d),F(3)*d/(4+d),F(0))
        edge2=(edge1[1],edge1[0],F(0),edge1[2])
        assert {star,edge1,edge2}.issubset(found)
        Q=F(3)-2*d
        assert (Q>0)==(d<F(3,2))
        assert (Q<0)==(d>F(3,2))
    # At criticality: six isolated equilibria and two continuum endpoints on proper supports; the continuum interior comes from the singular full support.
    assert len(all_isolated_equilibria(F(3,2)))==8  # includes both continuum endpoints
    for t in [F(0),F(1,9),F(9,22),F(2,3),F(9,11)]:
        assert F(0)<=t<=F(9,11)
        x1=F(24,11)-2*t
        x2=F(6,11)+2*t
        y1=t; y2=F(9,11)-t
        assert x1*(3-x1-3*y1-y2)==0
        assert x2*(3-x2-y1-3*y2)==0
        assert y1*(-3-y1+x1+F(3,2)*x2)==0
        assert y2*(-3-y2+F(3,2)*x1+x2)==0
    print('PASS:',n,'general rational cases; 9+9 support equilibria; 8 critical proper-support equilibria (including the 2 continuum endpoints); critical continuum samples; exact metric identities')

if __name__=='__main__':
    main()
