"""Exact arithmetic verification of the three-primary four-particle formula.

Run: python3 verify.py
No third-party dependencies.
"""
from fractions import Fraction

class Poly:
    def __init__(self, val=0):
        if isinstance(val, Poly): self.c = dict(val.c)
        elif isinstance(val, dict): self.c = {k: Fraction(v) for k,v in val.items() if v}
        else: self.c = {(0,0): Fraction(val)} if val else {}
    def __add__(self, other):
        other=Poly(other); z=dict(self.c)
        for k,v in other.c.items(): z[k]=z.get(k,0)+v
        return Poly(z)
    __radd__=__add__
    def __neg__(self): return Poly({k:-v for k,v in self.c.items()})
    def __sub__(self,other): return self+-Poly(other)
    def __rsub__(self,other): return Poly(other)+-self
    def __mul__(self,other):
        other=Poly(other); z={}
        for (i,j),v in self.c.items():
            for (p,q),w in other.c.items():
                k=(i+p,j+q);z[k]=z.get(k,0)+v*w
        return Poly(z)
    __rmul__=__mul__
    def __truediv__(self,z): return self*Fraction(1,z)
    def __eq__(self,other): return self.c==Poly(other).c
    def at(self,a,b): return sum(v*a**i*b**j for (i,j),v in self.c.items())

a=Poly({(1,0):1});b=Poly({(0,1):1})
def data(t):
    dim=t*(t-1)*(t-2)*(t-3)-4*t*(t-1)*(t-2)+6*t*(t-1)-4*t+1
    trace=-t*t+3*t-1
    k=t-1
    P=t*(t-7)*(t-2)*(t-1)/24
    Q=(t-4)*(t-3)*(t-2)*(t-1)/24
    U=t*(t-6)*(t-3)*(t-1)/8
    V=t*(t-5)*(t-3)*(t-2)/8
    return dim,trace,k,P,Q,U,V
D,T,k,P,Q,U,V=data(a)
E,S,l,R,Z,X,Y=data(b)
# V4-trivial S3 block, ordered U2-, U3+, U3-.
module_a=[k,P,Q];module_b=[l,R,Z]

def rank3(rows,n):
    rank=0; piv={}
    for row in rows:
        v={j:x%3 for j,x in row.items() if x%3}
        while v:
            j=min(v);x=v[j]
            if j not in piv:
                if x==2:v={i:(2*y)%3 for i,y in v.items()}
                piv[j]=v;rank+=1;break
            for i,y in piv[j].items():
                z=(v.get(i,0)-x*y)%3
                if z:v[i]=z
                else:v.pop(i,None)
    return rank

def maps_dimension(na,sa,nb,sb):
    # F: (U_na^sa)^* --> U_nb^sb tensor sign.
    sdom=sa*((-1)**(na-1));star=-sb
    eqs=[]
    for i in range(nb):
      for j in range(na):
        eqs.append({i*na+j:sdom*((-1)**j)-star*((-1)**i)})
        row={}
        if i>0:row[(i-1)*na+j]=row.get((i-1)*na+j,0)+1
        if j<na-1:row[i*na+j+1]=row.get(i*na+j+1,0)-1
        eqs.append(row)
    return na*nb-rank3(eqs,na*nb)

labels=[(2,-1),(3,1),(3,-1)]
H=[[maps_dimension(n,s,m,t) for m,t in labels] for n,s in labels]
assert H==[[1,1,1],[1,1,2],[1,2,1]],H
trivial=sum(module_a[i]*module_b[j]*H[i][j] for i in range(3) for j in range(3))
nontrivial=U*Y+V*X
mod3=trivial+nontrivial
rational=(D*E-6*T*S+8*k*l-3)/24
assert mod3==rational, 'Bivariate rational-polynomial identity does not hold'
for left,right,expected in [(7,7,1911),(7,8,5726),(8,8,16716)]:
    assert mod3.at(left,right)==expected
for i in range(7,40):
    di,ti,ki,pi,qi,ui,vi=[x.at(i,i) for x in data(a)]
    assert all(v.denominator==1 and v>=0 for v in (di,ki,pi,qi,ui,vi))
    for j in range(7,40):
        assert mod3.at(i,j)==rational.at(i,j)
print('VERIFY_OK: exact bivariate identity, 9 modular Hom spaces, 1089 integer cases; 1911/5726/16716')
