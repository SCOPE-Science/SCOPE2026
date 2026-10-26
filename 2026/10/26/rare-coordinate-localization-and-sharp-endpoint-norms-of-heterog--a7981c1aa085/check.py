"""Exact-rational independent tests for first-chaos projector endpoint norms.
Uses direct finite-matrix Gram inversion, without using the formula under test
for constructing the projection operator.
"""
from fractions import Fraction as F
from itertools import product
from math import prod
import random

COUNTS={'assertions':0,'matrix_instances':0,'bias_comparisons':0}

def test(condition,message='failure'):
    COUNTS['assertions']+=1
    if not condition:
        raise AssertionError(message)

def inverse(A):
    d=len(A)
    B=[list(row)+[F(int(i==j)) for j in range(d)] for i,row in enumerate(A)]
    for j in range(d):
        pivot=next(i for i in range(j,d) if B[i][j])
        B[j],B[pivot]=B[pivot],B[j]
        c=B[j][j]
        B[j]=[z/c for z in B[j]]
        for i in range(d):
            if i!=j:
                c=B[i][j]
                if c:B[i]=[u-c*v for u,v in zip(B[i],B[j])]
    return [row[d:] for row in B]

def matrix_norms(parameters):
    p=list(parameters);n=len(p)
    states=list(product((0,1),repeat=n));m=len(states)
    masses=[prod(pi if xi else 1-pi for pi,xi in zip(p,x)) for x in states]
    designs=[[F(1),*map(F,x)] for x in states]
    gram=[[sum((masses[k]*designs[k][i]*designs[k][j] for k in range(m)), F(0))
           for j in range(n+1)] for i in range(n+1)]
    gram_inv=inverse(gram)
    ker=[[sum((designs[i][a]*gram_inv[a][b]*designs[j][b]
                 for a in range(n+1) for b in range(n+1)),F(0))
          for j in range(m)] for i in range(m)]
    rows=[sum((masses[j]*abs(ker[i][j]) for j in range(m)),F(0)) for i in range(m)]
    columns=[sum((masses[i]*abs(ker[i][j]) for i in range(m)),F(0)) for j in range(m)]
    test(rows==columns, 'kernel symmetric endpoint duality')
    # Check projector and reproducing property independently.
    if n<=4:
        for i in range(m):
            for j in range(m):
                q=sum((masses[k]*ker[i][k]*ker[k][j] for k in range(m)),F(0))
                test(q==ker[i][j],'idempotence of exact Gram projector')
    return states, masses,ker,rows

def formula(parameters):
    r=[min(p,1-p) for p in parameters]
    z=F(0);n=len(r)
    for bits in product((0,1),repeat=n):
        mass=prod(si if bit else 1-si for si,bit in zip(r,bits))
        value=sum((F(bit)/si for bit,si in zip(bits,r)), F(1-n))
        z+=mass*abs(value)
    return z

def run():
    cases=[
      [F(1,2)]*n for n in range(1,6)
    ]+[
      [F(1,4)]*4,
      [F(1,8),F(1,8),F(3,8),F(3,8)],
      [F(1,6),F(1,6),F(1,3),F(1,3)],
      [F(2,5)]*4,
      [F(3,10),F(3,10),F(1,2),F(1,2)],
      [F(1,3),F(1,2),F(1,5)],
      [F(2,3),F(1,5),F(3,4),F(1,8)],
      [F(3,7),F(2,7),F(4,7),F(1,7),F(5,7)],
      [F(1,7),F(1,9),F(1,5),F(1,3),F(3,5)],
    ]
    random.seed(20261019)
    rationals=[F(k,12) for k in range(1,12)]
    cases+= [[random.choice(rationals) for _ in range(n)] for n in range(2,6) for _ in range(6)]
    for p in cases:
        states,masses,ker,rows=matrix_norms(p)
        norm=max(rows)
        direct=formula(p)
        test(norm==direct, ('not sharp',p,norm,direct))
        r=[min(x,1-x) for x in p]
        rare=tuple(1 if x<=F(1,2) else 0 for x in p)
        test(rows[states.index(rare)]==direct,'rare vertex not maximizing')
        # Sign-valued extremizer realizes the maximum at a maximizing row.
        idx=states.index(rare)
        signs=[F(1) if z>=0 else F(-1) for z in ker[idx]]
        output=sum((masses[j]*ker[idx][j]*signs[j] for j in range(len(states))),F(0))
        test(output==direct,'sign-extremizer unsuccessful')
        COUNTS['matrix_instances']+=1
    a=formula([F(1,4)]*4)
    b=formula([F(1,8),F(1,8),F(3,8),F(3,8)])
    test(a==F(371,128),'quarter exact')
    test(b==F(6213,2048),'heterogeneous exact')
    test(b-a==F(277,2048),'upper heterogeneity gap')
    c=formula([F(1,6),F(1,6),F(1,3),F(1,3)])
    test(c==F(77,27),'lower heterogeneity exact')
    test(a-c==F(161,3456),'lower heterogeneity gap')
    for n in range(2,7):
        fair=formula([F(1,2)]*n)
        for _ in range(25):
            r=[random.choice([F(k,16) for k in range(1,9)]) for _ in range(n)]
            val=formula(r)
            test(val>=fair,'fair global min violation')
            test(val<2*n-1,'sharp envelope violation')
            for i in range(n):
                r2=r[:]
                r2[i]=F(1,2)
                test(formula(r2)<=val,'coordinate convex order violation')
                COUNTS['bias_comparisons']+=1
    print('PASS',COUNTS)

if __name__=='__main__':run()
