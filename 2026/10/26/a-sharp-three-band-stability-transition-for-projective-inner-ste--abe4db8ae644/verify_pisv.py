"""Standalone exact-arithmetic algebra checks for the three-band PISV stability theorem.
Python 3 standard library only. This is supplementary verification, not a substitute for the proof.
"""
from fractions import Fraction as F
from math import sqrt

# Bivariate Q[lambda,t] polynomials, dictionary (lambda_power,t_power): rational.
def poly(*terms):
    d = {}
    for coeff,i,j in terms:
        d[(i,j)] = d.get((i,j), F(0)) + F(coeff)
    return {k:v for k,v in d.items() if v}

def add(*args):
    out={}
    for p in args:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def neg(p):return {k:-v for k,v in p.items()}
def sub(p,q):return add(p,neg(q))
def mul(*args):
    out={(0,0):F(1)}
    for p in args:
        r={}
        for (i,j),a in out.items():
            for (k,l),b in p.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+a*b
        out={k:v for k,v in r.items() if v}
    return out

def val(p,L,T):return sum(a*L**i*T**j for (i,j),a in p.items())

one=poly((1,0,0)); L=poly((1,1,0)); T=poly((1,0,1)); half=poly((F(1,2),0,0))
R=add(one,neg(T),mul(poly((F(3,2),0,0)),L,sub(one,L),T,T),neg(mul(half,L,L,sub(one,L),T,T,T)))
R_factor=mul(sub(one,mul(L,T)),add(one,neg(mul(sub(one,L),T)),mul(half,L,sub(one,L),T,T)))
assert R==R_factor
# Recover the scalar stability function independently from the published tableau.
U2=sub(one,mul(L,T))
U3=sub(one,add(mul(L,T),mul(half,L,T,U2)))
assert U3==add(one,neg(mul(poly((F(3,2),0,0)),L,T)),mul(half,L,L,T,T))
R_stages=sub(sub(one,mul(L,T)),mul(sub(one,L),T,U3))
assert R_stages==R
left_plus=add(R,one)
right_plus=mul(sub(poly((2,0,0)),mul(L,T)),add(one,neg(mul(half,sub(one,L),T)),mul(half,L,sub(one,L),T,T)))
assert left_plus==right_plus
left_minus=sub(R,one)
right_minus=neg(mul(T,add(one,neg(mul(poly((F(3,2),0,0)),L,sub(one,L),T)),mul(half,L,L,sub(one,L),T,T))))
assert left_minus==right_minus
assert val(R,F(1,9),F(9,2))==-1
assert val(R,F(1,9),F(27,2))==1
assert val(R,F(1,9),F(18))==-1

# At lambda=1/10 all five nonzero boundary roots are rational.
L0=F(1,10)
endpoints=[F(0),F(10,3),F(20,3),F(40,3),F(50,3),F(20)]
assert [val(R,L0,t) for t in endpoints]==[1,-1,-1,1,1,-1]
for t,should_stable in [(F(1),True),(F(5),False),(F(10),True),(F(15),False),(F(19),True),(F(21),False)]:
    a=val(R,L0,t)
    assert (abs(a)<=1)==should_stable,(t,a)

# Exact rational samples across and on both sides of the sharp transition.
count=0
for lam_num in range(1,51):
    lam=F(lam_num,100)
    if lam<F(1,9):
        s=sqrt(float((1-9*lam)/(1-lam)))
        cuts=[0,(1-s)/(2*float(lam)),(1+s)/(2*float(lam)),
              (3-s)/(2*float(lam)),(3+s)/(2*float(lam)),2/float(lam)]
    for i in range(1,1001):
        t=F(2*i,1001)/lam
        amp=val(R,lam,t)
        if lam>F(1,9):assert -1<amp<1,(lam,t,amp)
        else:
            x=float(t)
            band=(cuts[0]<=x<cuts[1] or cuts[2]<x<cuts[3] or cuts[4]<x<cuts[5])
            assert (abs(amp)<1)==band,(lam,t,amp,cuts)
        count+=1
print('PISV_EXACT_CHECKS_OK',count+15)
