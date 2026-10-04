#!/usr/bin/env python3
"""Finite checks for the n=2 nilpotent-free matrix-space construction.

For odd prime q choose a nonsquare d and use
  U = {[[x,-d*y],[y,-x]] : x,y in F_q}.
For q=2 use d=1 in the characteristic-2 formula
  U = {[[x,x+d*y],[y,x]] : x,y in F_2}.
Then W=U+F_q E_11.  We exhaust all W and check that trace=det=0
occurs only at the zero matrix.  For 2x2 matrices this is equivalent to
nilpotence.
"""

def det(M,q):
    return (M[0]*M[3]-M[1]*M[2])%q

def tr(M,q):
    return (M[0]+M[3])%q

def nonsquare(q):
    squares={x*x%q for x in range(1,q)}
    for d in range(1,q):
        if d not in squares: return d
    raise ValueError

def check_prime(q):
    if q==2:
        d=1
        mats=[]
        for x in range(q):
          for y in range(q):
            for c in range(q):
              M=((x+c)%q,(x+d*y)%q,y%q,x%q)
              mats.append(M)
    else:
        d=nonsquare(q)
        mats=[]
        for x in range(q):
          for y in range(q):
            for c in range(q):
              M=((x+c)%q,(-d*y)%q,y%q,(-x)%q)
              mats.append(M)
    assert len(set(mats))==q**3
    bad=[M for M in mats if M!=(0,0,0,0) and tr(M,q)==0 and det(M,q)==0]
    assert not bad,(q,d,bad[:3])
    return q,d,len(mats)

if __name__=='__main__':
    out=[check_prime(q) for q in (2,3,5,7,11,13)]
    print('VERIFY_OK',out)

# GF(4)=F_2[w]/(w^2+w+1), elements encoded a+b*w as a|(b<<1).
def f4_add(a,b): return a^b
def f4_mul(a,b):
    a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
    c0=(a0*b0) ^ (a1*b1)          # w^2=w+1 contributes 1
    c1=(a0*b1) ^ (a1*b0) ^ (a1*b1) # and w
    return c0 | (c1<<1)
def f4_det(M): return f4_add(f4_mul(M[0],M[3]),f4_mul(M[1],M[2]))
def f4_tr(M): return f4_add(M[0],M[3])
def check_f4():
    d=2 # w, absolute trace w+w^2 = 1
    mats=[]
    for x in range(4):
      for y in range(4):
        for c in range(4):
          M=(f4_add(x,c), f4_add(x,f4_mul(d,y)), y, x)
          mats.append(M)
    assert len(set(mats))==64
    bad=[M for M in mats if M!=(0,0,0,0) and f4_tr(M)==0 and f4_det(M)==0]
    assert not bad,bad[:3]
    return 4,d,len(mats)

print('VERIFY_GF4_OK',check_f4())
