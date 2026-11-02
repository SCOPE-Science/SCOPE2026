from fractions import Fraction as F
from math import factorial
values=(0,8,8,0,-8,-8)
N=40

def apply(z, sign):
    out=[]
    for j,v in enumerate(values):
        a,b=z[j]; an,bn=z[(j+1)%6]
        c=F(3*v,8)*sign
        out.append((F(9,4)*(-a+an)-c*b,F(9,4)*(-b+bn)+c*a))
    return out

def series(z,sign):
    term=z
    acc=z[:]
    for k in range(1,N+1):
        term=[(a/k,b/k) for a,b in apply(term,sign)]
        acc=[(a+c,b+d) for (a,b),(c,d) in zip(acc,term)]
    return acc
ones=[(F(1),F(0))]*6
right=series(ones,-1)
left=series(right,1)
wre=sum((a for a,b in left),F(0))/6
wim=sum((b for a,b in left),F(0))/6
R=F(3**8*8**(N+1),factorial(N+1))
eps=2*3**8*R+R*R
print('Wre',float(wre),'Wim',float(wim),'exact_im_zero',wim==0)
print('bound checks',wre< -F(1,10),eps<F(1,10000),float(eps))
assert wim==0 and wre<-F(1,10) and eps<F(1,10000)
