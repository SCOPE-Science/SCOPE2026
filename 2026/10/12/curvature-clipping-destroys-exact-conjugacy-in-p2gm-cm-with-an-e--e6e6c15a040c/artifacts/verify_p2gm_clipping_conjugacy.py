from fractions import Fraction
import math, random

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(H,x): return [sum(H[i][j]*x[j] for j in range(len(x))) for i in range(len(H))]
def qclip(r,c1,c2): return max(c1,min(r,c2))

Hq=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1,2)]]
x0=[Fraction(1),Fraction(1)]
g0=mv(Hq,x0); v0=[-z for z in g0]; x1=[x0[i]+v0[i] for i in range(2)]
def fq(x):
    Hx=mv(Hq,x)
    return Fraction(1,2)*dot(x,Hx)
assert fq(x0)==Fraction(3,4)
assert fq(x1)==Fraction(1,16)
assert fq(x1)-fq(x0)==Fraction(-11,16)
assert Fraction(1,2)*dot(g0,v0)==Fraction(-5,8)
assert x1==[Fraction(0),Fraction(1,2)]

s1=v0; g1=mv(Hq,x1); v1=[-z for z in g1]; Hv1=mv(Hq,v1)
nv1=dot(v1,v1); vHv=dot(v1,Hv1); coupling=dot(s1,Hv1); r=vHv/nv1
assert v1==[Fraction(0),Fraction(-1,4)]
assert r==Fraction(1,2) and coupling==Fraction(1,16) and nv1==Fraction(1,16)
q=Fraction(1,4); coef=coupling/(q*nv1)
st=[s1[i]-coef*v1[i] for i in range(2)]
defect=dot(v1,mv(Hq,st))
assert coef==4 and st==[Fraction(-1),Fraction(1,2)]
assert defect==Fraction(-1,16)==coupling*(1-r/q)

coef_exact=coupling/vHv
st_exact=[s1[i]-coef_exact*v1[i] for i in range(2)]
assert coef_exact==2 and st_exact==[Fraction(-1),Fraction(0)]
assert dot(v1,mv(Hq,st_exact))==0

random.seed(34)
for _ in range(300):
    B=[[random.uniform(-2,2) for _ in range(3)] for _ in range(3)]
    H=[[sum(B[k][i]*B[k][j] for k in range(3))+(1.0 if i==j else 0.0)
        for j in range(3)] for i in range(3)]
    s=[random.uniform(-2,2) for _ in range(3)]
    v=[random.uniform(-2,2) for _ in range(3)]
    Hv=mv(H,v); nv=dot(v,v); rr=dot(v,Hv)/nv; qq=qclip(rr,0.4,1.3); cc=dot(s,Hv)
    st=[s[i]-cc/(qq*nv)*v[i] for i in range(3)]
    lhs=dot(v,mv(H,st)); rhs=cc*(1.0-rr/qq)
    assert abs(lhs-rhs)<=2e-10*max(1.0,abs(lhs),abs(rhs))

vals=[]
for tau in [1/4,1/8,1/16,1/32,1/64,1/128]:
    a=-0.5+1.0/(4.0*tau)
    vals.append(-a/math.sqrt(2.0+a*a))
assert all(vals[i+1]<vals[i] for i in range(len(vals)-1))
assert vals[-1]<-0.998
print("VERIFY_OK")
