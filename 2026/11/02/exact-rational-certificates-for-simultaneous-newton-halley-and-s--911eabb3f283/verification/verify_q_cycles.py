#!/usr/bin/env python3
"""Exact rational interval certificate for three quartic root-finding iterations.

Requires Python 3 standard library only; all assertions are exact fractions.
"""
from fractions import Fraction as F

Q = [395,-576,0,-33,33]
Q1 = [1580,-1728,0,-33]
Q2 = [4740,-3456,0]
UH = [780125,-1137600,497664,13035,-4752]
DH = [1560250,-3412800,1990656,-26070,-21186,57024,1089]
US = [2184350,-3185280,1244160,13035,-4752]
DS = [1580,-1728,0,-33]

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    t=[x*y for x in a for y in b];return (min(t),max(t))
def div(a,b):
    assert b[0]>0 or b[1]<0, 'division interval contains 0'
    return mul(a,(1/b[1],1/b[0]))
def scalar(x):return (F(x),F(x))
def poly(coeffs,x):
    v=scalar(coeffs[0]);
    for a in coeffs[1:]:v=add(mul(v,x),scalar(a))
    return v
def powi(a,k):
    v=scalar(1)
    for _ in range(k):v=mul(v,a)
    return v

def qmap(method,x):
    p=poly(Q,x);p1=poly(Q1,x);p2=poly(Q2,x)
    if method=='H':return sub(x,div(mul(scalar(2),mul(p,p1)),sub(mul(scalar(2),mul(p1,p1)),mul(p,p2))))
    if method=='S':return sub(sub(x,div(p,p1)),div(mul(mul(p,p),p2),mul(scalar(2),powi(p1,3))))
    if method=='N':return sub(x,div(p,p1))
    raise ValueError(method)

def derivative(method,x):
    p=poly(Q,x)
    if method=='H':return div(mul(scalar(12),mul(powi(p,2),poly(UH,x))),powi(poly(DH,x),2))
    if method=='S':return div(mul(scalar(12),mul(powi(p,2),poly(US,x))),powi(poly(DS,x),4))
    raise ValueError(method)

def maxabs(interval):return max(abs(interval[0]),abs(interval[1]))

def proof(method,centers,radii,ceilings):
    k=len(centers);assert k in (2,3)
    I=[(c-r,c+r) for c,r in zip(centers,radii)]
    assert all(I[i][1]<I[j][0] or I[j][1]<I[i][0] for i in range(k) for j in range(i+1,k))
    L=[]
    for i,(center,r) in enumerate(zip(centers,radii)):
        j=(i+1)%k
        d=derivative(method,I[i]);lb=maxabs(d)
        assert lb < ceilings[i], (method,i,"derivative ceiling")
        # Need actual derivative bound, rational exact and nonzero denominators in derivative.
        pc=poly(Q,I[i]);assert pc[0]>0 or pc[1]<0, 'root in interval'
        if method=='S':
            qprime=poly(Q1,I[i]); assert qprime[0]>0 or qprime[1]<0
        else:
            p=poly(Q,I[i]);p1=poly(Q1,I[i]);p2=poly(Q2,I[i]);v=sub(mul(scalar(2),mul(p1,p1)),mul(p,p2));assert v[0]>0 or v[1]<0
        val=qmap(method,scalar(center));err=max(abs(val[0]-centers[j]),abs(val[1]-centers[j]))
        assert err < F(1,10**12), (method,i,"center error ceiling")
        assert err + ceilings[i]*r < radii[j], (method,i,"coarse rational inclusion")
        assert err + lb*r < radii[j], (method,i,'not invariant',float(err),float(lb),float(r),float(radii[j]))
        L.append(lb)
        print(method,i,'center',str(center),'radius',str(r),'max derivative bound',float(lb),'center residual',float(err),'next slack',float(radii[j]-err-lb*r))
    mult=F(1)
    for l in L:mult*=l
    assert mult<1,(method,'no contraction',float(mult))
    print(method,'CERTIFIED maximal multiplier',float(mult))
    return mult

def dec(s):return F(s)

# Exact Newton cycle: nonzero polynomial values and denominators, and N(0)=1, N(1)=0.
assert poly(Q,scalar(0))==scalar(33)
assert poly(Q,scalar(1))==scalar(-181)
assert qmap('N',scalar(0))==scalar(1)
assert qmap('N',scalar(1))==scalar(0)
assert poly(Q2,scalar(0))==scalar(0)
print('N: exact extraneous superattracting two-cycle 0 <-> 1')
proof('H', [dec('-0.099563100530747'),dec('-0.519387031162540')],[F(1,10000),F(1,50000)],[F(19,250),F(7,5)])
proof('S',[dec('0.061148311552933'),dec('-0.691524324611230'),dec('-0.347921163893610')],[F(1,100000),F(1,5000000),F(1,4000000)],[F(11,1000),F(4,5),F(23,10)])
print('VERIFIED: rational intervals, strict inclusions, no roots or poles, strict attraction')

# Independent polynomial-identity checks for the derivative formulas above.
# Coefficients below are stored in ascending powers; no computer-algebra package is required.
def low(high): return list(reversed(high))
def padd(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def pneg(a):return [-v for v in a]
def psub(a,b):return padd(a,pneg(b))
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def pder(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def pscale(a,s):return [s*x for x in a]
def same(a,b):
    while a and a[-1]==0:a=a[:-1]
    while b and b[-1]==0:b=b[:-1]
    return a==b
q=low(Q);qp=low(Q1);qpp=low(Q2);z=[0,1]
assert same(pder(q),qp) and same(pder(qp),qpp)
dH=psub(pscale(pmul(qp,qp),2),pmul(q,qpp))
nH=psub(pmul(z,dH),pscale(pmul(q,qp),2))
assert same(psub(pmul(pder(nH),dH),pmul(nH,pder(dH))),pscale(pmul(pmul(q,q),low(UH)),48))
dS=pscale(pmul(pmul(qp,qp),qp),2)
nS=psub(psub(pmul(z,dS),pscale(pmul(q,pmul(qp,qp)),2)),pmul(pmul(q,q),qpp))
assert same(psub(pmul(pder(nS),dS),pmul(nS,pder(dS))), pscale(pmul(pmul(pmul(q,q),low(US)),pmul(qp,qp)),48))
# Verify the Halley denominator polynomial used by the interval derivative enclosure.
assert same(dH,pscale(low(DH),2))
print('VERIFIED: derivative rational identities by integer polynomial algebra')

# Independent squarefreeness certificate: quartic discriminant by Sylvester determinant.
def determinant_bareiss(A):
    A=[list(row) for row in A]
    n=len(A);sgn=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            for j in range(k+1,n):
                if A[j][k]:
                    A[k],A[j]=A[j],A[k];sgn=-sgn;break
            else:return 0
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*p-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        for i in range(k+1,n):A[i][k]=0
        prev=p
    return sgn*A[n-1][n-1]

def sylvester(a,b):
    n=len(a)-1;m=len(b)-1
    rows=[]
    for i in range(m):rows.append([0]*i+a+[0]*(m-i-1))
    for i in range(n):rows.append([0]*i+b+[0]*(n-i-1))
    return rows
assert determinant_bareiss(sylvester(Q,Q1))==395*(-3350378794970691)
print('VERIFIED: nonzero quartic discriminant via 7x7 exact integer determinant')
