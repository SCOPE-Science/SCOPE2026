#!/usr/bin/env python3
"""Direct finite checks of cyclic homology-character formulas for cycle-complete categorical products."""
from math import gcd
from collections import defaultdict

def predicted(m,n,j):
    d = gcd(m,j)
    q=n-1
    return q*((-1)**d)+(3*q**(d//3) if d%3==0 else 0)

def representation(m,n,j):
    r=m//3;q=n-1
    if r%2==0:
        return q*((-1)**j)+(3*q**gcd(r,j//3) if j%3==0 else 0)
    return q*(2 if j%3==0 else -1)+(3*(q**gcd(r,j//3)-q) if j%3==0 else 0)

def independent_masks(m,n):
    L=m*n
    adj=[0]*L
    for i in range(m):
      for a in range(n):
        idx=i*n+a
        for e in ((i-1)%m,(i+1)%m):
          for b in range(n):
            if b!=a: adj[idx] |= 1<<(e*n+b)
    def rec(available,selected):
      if not available:
        yield selected
      else:
        low=available&(-available);v=low.bit_length()-1
        yield from rec(available^low,selected)
        yield from rec((available^low)&~adj[v],selected|low)
    return rec((1<<L)-1,0)

def permutation_image(mask,m,n,j):
    shifted=0
    while mask:
        b=mask&-mask;v=b.bit_length()-1;mask-=b
        i,a=divmod(v,n)
        shifted|=1<<(((i+j)%m)*n+a)
    return shifted

def cycles_on_face(mask,m,n,j):
    unseen=mask;cycles=0
    while unseen:
      cycles+=1
      b=unseen&-unseen;v=b.bit_length()-1
      i,a=divmod(v,n)
      while unseen&(1<<(i*n+a)):
        unseen^=1<<(i*n+a)
        i=(i+j)%m
    return cycles

def exhaustive(m,n):
    signed=[-1]*m
    fixed=[-1]*m
    total=0
    for face in independent_masks(m,n):
        if face==0:continue
        total+=1
        k=face.bit_count()
        for j in range(m):
          if permutation_image(face,m,n,j)==face:
            cycles=cycles_on_face(face,m,n,j)
            signed[j] += (-1)**(k-1 +k-cycles)
            fixed[j] += (-1)**(cycles-1)
    for j in range(m):
        expect=predicted(m,n,j)
        assert signed[j]==fixed[j]==-expect, (m,n,j,signed[j],fixed[j],expect)
        assert representation(m,n,j)==expect
    assert -signed[0]==3*(n-1)**(m//3)+(n-1)*(-1)**m
    return total

def cycle_transfer(d,n):
    # States: empty, each singleton color, multi-color (collective signed weight n-1).
    N=n+2;weight=[1]+[-1]*n+[n-1]
    def compatible(a,b):
        if a==0 or b==0:return True
        if a==n+1 or b==n+1:return False
        return a==b
    T=[[int(compatible(a,b))*weight[b] for b in range(N)] for a in range(N)]
    P=[[int(a==b) for b in range(N)] for a in range(N)]
    for _ in range(d):
      P=[[sum(P[i][k]*T[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    return sum(P[i][i] for i in range(N))

def char_ortho(m,n):
    # Multiplicity of each complex C_m character by exact cyclotomic real sums
    import cmath
    chars=[predicted(m,n,j) for j in range(m)]
    for k in range(m):
      val=sum(chars[j]*cmath.exp(-2j*cmath.pi*k*j/m) for j in range(m))/m
      assert abs(val.imag)<1e-7 and abs(val.real-round(val.real))<1e-7 and val.real>-1e-7
    return round(sum(chars)/m)

def phi(n):
    return sum(gcd(n,k)==1 for k in range(1,n+1))

def necklace(r,q):
    return sum(phi(r//d)*q**d for d in range(1,r+1) if r%d==0)//r

if __name__=='__main__':
    outcomes=[]
    for m,n in [(3,2),(3,3),(3,4),(6,2),(6,3),(9,2),(12,2)]:
      total=exhaustive(m,n) if m*n<=18 else -1
      inv=char_ortho(m,n)
      assert inv==necklace(m//3,n-1)-(n-1 if (m//3)%2 else 0)
      assert all(cycle_transfer(d,n)==((n-1)*((-1)**d)+(3*(n-1)**(d//3) if d%3==0 else 0)) for d in range(1,m+1))
      outcomes.append((m,n,total,inv))
    print('CYCLIC_PRODUCT_CHARACTERS_VERIFIED',outcomes)
