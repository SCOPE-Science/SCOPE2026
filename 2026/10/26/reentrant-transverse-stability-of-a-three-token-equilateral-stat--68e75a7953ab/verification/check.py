#!/usr/bin/env python3
"""Independent finite checks for three-token repulsive full-softmax dynamics."""
from math import cos, sin, exp, pi, hypot
from fractions import Fraction

def bisect(f,lo,hi,iterations=95):
    flo=f(lo)
    assert flo*f(hi)<0
    for _ in range(iterations):
        mid=(lo+hi)/2
        if flo*f(mid)<=0: hi=mid
        else: lo=mid;flo=f(lo)
    return (lo+hi)/2

def vals(beta):
    q=1/(exp(1.5*beta)+2)
    k=1-3*q
    ell=1+3*q*(3*beta-2)/4
    return k,ell,k+ell

def forward(theta,h,beta):
    uv=[(cos(t),sin(t)) for t in theta]
    outs=[]
    for i in range(3):
        z=[exp(beta*(uv[i][0]*uv[j][0]+uv[i][1]*uv[j][1])) for j in range(3)]
        zsum=sum(z)
        mx=sum(z[j]*uv[j][0] for j in range(3))/zsum
        my=sum(z[j]*uv[j][1] for j in range(3))/zsum
        wx=uv[i][0]-h*mx; wy=uv[i][1]-h*my
        norm=hypot(wx,wy)
        assert norm>=1-h-1e-13
        outs.append((wx/norm,wy/norm))
    return outs

def angle_derivative(beta,h,d):
    t=[2*pi*i/3 for i in range(3)]
    e=1e-6
    xp=forward([t[i]+e*d[i] for i in range(3)],h,beta)
    xm=forward([t[i]-e*d[i] for i in range(3)],h,beta)
    return [((xp[i][0]-xm[i][0])*(-sin(t[i])) +
             (xp[i][1]-xm[i][1])*cos(t[i]))/(2*e) for i in range(3)]

for aa,bb,hh in [(Fraction(7,4),Fraction(3,5),Fraction(2,7)),(Fraction(-3,8),Fraction(11,6),Fraction(9,10))]:
    assert (1-hh*bb)**2-(1-hh*aa)**2 == hh*(aa-bb)*(2-hh*(aa+bb))

def rootfun(beta): return 2+(4-1.5*beta)*exp(1.5*beta)
star=bisect(rootfun,2.5,3.1)
smax=vals(star)[2]
hcrit=2/smax
assert 2.69<star<2.70 and 0.986<hcrit<0.987
counter=0
for h in [0.2,0.8,0.98,0.99,0.995,0.999]:
  for beta in [0.1,0.5,1,1.8,2,2.2,2.5,3,4,5,7,11]:
    k,l,S=vals(beta)
    lam=(1-h*l)/(1-h*k)
    assert (abs(lam)<1)==(h*S<2)
    for direction,target in [((1,1,1),1.0),((1,-1,0),lam),((1,1,-2),lam)]:
      got=angle_derivative(beta,h,direction)
      assert max(abs(got[i]-target*direction[i]) for i in range(3))<8e-6,(beta,h,direction,got,lam)
      counter+=1
h=.995
threshold1=bisect(lambda b: vals(b)[2]-2/h,2.0,star)
threshold2=bisect(lambda b: vals(b)[2]-2/h,star,10)
assert 2.115< threshold1 <2.116 and 4.098<threshold2<4.100
for b in [0.1,1,2.0,3.0,5,10]:
  lam=(1-h*vals(b)[1])/(1-h*vals(b)[0])
  assert (abs(lam)>1)==(threshold1<b<threshold2)
print('VERIFY_OK numerical_angular_directions=',counter,'beta_star=',format(star,'.13f'),'h_critical=',format(hcrit,'.13f'),'flip_thresholds=',format(threshold1,'.12f'),format(threshold2,'.12f'))
