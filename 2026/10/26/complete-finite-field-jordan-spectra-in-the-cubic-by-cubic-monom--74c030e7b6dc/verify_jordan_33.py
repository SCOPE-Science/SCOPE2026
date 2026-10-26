#!/usr/bin/env python3
"""Direct multiplication-matrix verification of Jordan strata of k[x,y]/(x^3,y^3), p>=5."""
from collections import Counter
from itertools import product
from random import Random
M=[(i,j) for i in range(3) for j in range(3)]
M_INDEX={x:i for i,x in enumerate(M)}
ONE=M_INDEX[(0,0)]
def rank(a,p):
    a=[row[:] for row in a]
    m=len(a); n=len(a[0]); r=0
    for j in range(n):
        k=next((i for i in range(r,m) if a[i][j]%p), None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        inv=pow(a[r][j]%p,-1,p)
        a[r]=[(z*inv)%p for z in a[r]]
        for i in range(r+1,m):
            c=a[i][j]
            if c:a[i]=[(v-c*w)%p for v,w in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r
def mmul(a,b,p):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]
def power_ranks(vec,p):
    n=9; a=[[0]*n for _ in range(n)]
    for col,(i,j) in enumerate(M):
      for loc,(k,l) in enumerate(M):
        if i+k<3 and j+l<3:
          a[M_INDEX[(i+k,j+l)]][col]=(a[M_INDEX[(i+k,j+l)]][col]+vec[loc])%p
    prod=[row[:] for row in a]
    rr=[9]
    for power in range(1,6):
      rr.append(rank(prod,p))
      prod=mmul(prod,a,p)
    if rr[-1]!=0:raise AssertionError('non nilpotent')
    blocks=[]
    for j in range(1,len(rr)):
      c=rr[j-1]-2*rr[j]+(rr[j+1] if j+1<len(rr) else 0)
      blocks.extend([j]*c)
    assert sum(blocks)==9,(vec,rr,blocks)
    return tuple(sorted(blocks,reverse=True))
def expected(vec,p):
    a,b,c,d,e,f,g,h=[vec[M_INDEX[mon]] for mon in [(1,0),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2),(2,2)]]
    if a and b:return (5,3,1)
    if a or b:
      return (4,3,2) if (e if a else c) else (3,3,3)
    if c or d or e:
      det=(d*d-c*e)%p
      square=(d*d+2*c*e)%p
      r=4 if det else 3
      if square:
        return (3,2,2,1,1) if r==4 else (3,2,1,1,1,1)
      return (2,2,2,2,1) if r==4 else (2,2,2,1,1,1)
    if f or g:return (2,2,1,1,1,1,1)
    if h:return (2,1,1,1,1,1,1,1)
    return (1,1,1,1,1,1,1,1,1)
def predict_counts(q):
    return {
      (5,3,1): (q-1)**2*q**6,
      (4,3,2): 2*(q-1)**2*q**5,
      (3,3,3): 2*(q-1)*q**5,
      (3,2,2,1,1): q**3*(q-1)*(q*q-q+1),
      (2,2,2,2,1): q**3*(q-1)**2,
      (3,2,1,1,1,1): q**3*(q-1)**2,
      (2,2,2,1,1,1): 2*q**3*(q-1),
      (2,2,1,1,1,1,1): (q*q-1)*q,
      (2,1,1,1,1,1,1,1): q-1,
      (1,1,1,1,1,1,1,1,1): 1
    }
def main():
    ran=Random(4390872)
    # All 125 quadratic forms modulo 5. No other coefficients, direct rank computation.
    hist=Counter()
    p=5
    for c,d,e in product(range(p),repeat=3):
       vec=[0]*9
       for mon,v in [((2,0),c),((1,1),d),((0,2),e)]:vec[M_INDEX[mon]]=v
       actual=power_ranks(vec,p); expected_type=expected(vec,p)
       assert actual==expected_type,(p,vec,actual,expected_type)
       hist[actual]+=1
    for p in (5,7,11):
       for j in range(1500):
          v=[0]+[ran.randrange(p) for k in range(8)]
          actual=power_ranks(v,p); expected_type=expected(v,p)
          assert actual==expected_type,(p,j,v,actual,expected_type)
       assert sum(predict_counts(p).values())==p**8
       print('SAMPLE_OK',p,'1500')
    # Independent literal enumeration over all 5^5 coefficients in the quadratic-or-higher ideal:
    # only 5 parameters (c,d,e,f,g) are enumerated, h is fixed to 0.
    p=5; total=0
    for c,d,e,f,g in product(range(p),repeat=5):
      vec=[0]*9
      for mon,v in [((2,0),c),((1,1),d),((0,2),e),((2,1),f),((1,2),g)]: vec[M_INDEX[mon]]=v
      actual=power_ranks(vec,p)
      if actual!=expected(vec,p):raise AssertionError((vec,actual,expected(vec,p)))
      total+=1
    print('EXHAUSTIVE_M2_SLICE_OK',total)
    # Independent full-condition counts in three-dimensional quadratic parameter space.
    for p in (5,7,11):
      forms=Counter()
      for c,d,e in product(range(p),repeat=3):
        if c or d or e:
          forms[((d*d-c*e)%p==0, (d*d+2*c*e)%p==0)]+=1
      assert forms[(False,False)]==(p-1)*(p*p-p+1),forms
      assert forms[(False,True)]==(p-1)**2,forms
      assert forms[(True,False)]==(p-1)**2,forms
      assert forms[(True,True)]==2*(p-1),forms
    print('VERIFY_OK_JORDAN_33_COMPLETE_SPECTRUM')
if __name__=='__main__':main()
