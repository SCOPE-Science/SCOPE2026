"""Leading I-function coefficient for F1, beta = 3H-2E = 3F+E.
Cohomology basis idx 0:1,1:H,2:F,3:E,4:pt with F=H-E.
Relations: H^2=pt, H*E=0, E^2=-pt (hence F^2=0, F*H=pt, F*E=pt).
I_d/z = prod_{i} prod_{m=1}^{k_i} 1/(D_i+m*z), k=(1,1,3,2).
Expand in w=1/z using D^3=0 (surface): 1/(D+mz) = w/m - w^2 D/m^2 + w^3 D^2/m^3.
"""
from fractions import Fraction
def mul(a,b):
    res={}
    def toHE(k):
        if k==1: return (Fraction(1),Fraction(0))
        if k==2: return (Fraction(1),Fraction(-1))
        if k==3: return (Fraction(0),Fraction(1))
        return None
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            c=v1*v2
            if k1==0: res[k2]=res.get(k2,Fraction(0))+c
            elif k2==0: res[k1]=res.get(k1,Fraction(0))+c
            elif k1==4 or k2==4: pass
            else:
                a1,b1=toHE(k1); a2,b2=toHE(k2)
                res[4]=res.get(4,Fraction(0))+c*(a1*a2-b1*b2)
    return {k:v for k,v in res.items() if v!=0}
def add(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,Fraction(0))+v
        if r[k]==0: del r[k]
    return r
def scl(a,s): return {k:v*s for k,v in a.items() if v*s!=0}
one={0:Fraction(1)}; H={1:Fraction(1)}; F={2:Fraction(1)}; E={3:Fraction(1)}
maxk=9
def fac(D,m):
    s=[{} for _ in range(maxk+1)]
    s[1]=add(s[1],scl(one,Fraction(1,m)))
    s[2]=add(s[2],scl(D,Fraction(-1,m*m)))
    s[3]=add(s[3],scl(mul(D,D),Fraction(1,m**3)))
    return s
def conv(a,b):
    c=[{} for _ in range(maxk+1)]
    for i in range(maxk+1):
        for j in range(maxk+1-i):
            if a[i] and b[j]:
                c[i+j]=add(c[i+j],mul(a[i],b[j]))
    return c
C=[{} for _ in range(maxk+1)]; C[0]=one
for D,m in [(F,1),(F,1),(H,1),(H,2),(H,3),(E,1),(E,2)]:
    C=conv(C,fac(D,m))
names={0:'1',1:'H',2:'F',3:'E',4:'pt'}
for j in range(maxk+1):
    print("w^%d:" % j, {names[k]:str(v) for k,v in C[j].items()})
assert C[7]=={0:Fraction(1,12)}, C[7]
print("LEADING COEFF w^7 (z^-6): 1/12 * 1  ->  <tau_5(pt)> = 1/12")
