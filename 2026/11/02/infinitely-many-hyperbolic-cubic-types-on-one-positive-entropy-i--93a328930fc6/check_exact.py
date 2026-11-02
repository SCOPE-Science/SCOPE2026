from fractions import Fraction as Q

def f(s,x):
 d=1/(s*s*(s+1)); A=1-d; B=s+d
 return 1-A*x**3-B*x*x

def critical(s):
 d=1/(s*s*(s+1)); A=1-d; B=s+d
 return -2*B/(3*A),1-4*B**3/(27*A*A)
lo=Q(109,100); hi=Q(11,10)
for s in [lo,hi]:
 c,v=critical(s); R=f(s,f(s,v))-v
 print('s',s,'A',float(1-1/(s*s*(s+1))),'B',float(s+1/(s*s*(s+1))))
 print('critical c, v, residual',float(c),float(v),float(R),'sign', 'positive' if R>0 else 'negative')
 assert Q(-1,2) < v < Q(-3,10)
assert f(lo,f(lo,critical(lo)[1]))-critical(lo)[1]>Q(1,20)
assert f(hi,f(hi,critical(hi)[1]))-critical(hi)[1]<-Q(1,10)
Amin=Q(59,100);Amax=Q(61,100);Bmin=Q(149,100);Bmax=Q(3,2)
print('F(-1/2) between',float(1+Amin/Q(8)-Bmax/Q(4)),float(1+Amax/Q(8)-Bmin/Q(4)))
print('F(-3/10) between',float(1+Amin*Q(27,1000)-Bmax*Q(9,100)),float(1+Amax*Q(27,1000)-Bmin*Q(9,100)))
assert 1+Amin/Q(8)-Bmax/Q(4)>Q(69,100)
assert 1+Amax/Q(8)-Bmin/Q(4)<Q(71,100)
assert 1+Amin*Q(27,1000)-Bmax*Q(9,100)>Q(88,100)
assert 1+Amax*Q(27,1000)-Bmin*Q(9,100)<Q(89,100)
Gleftbound=1-Amax*Q(71,100)**3-Bmax*Q(71,100)**2
Grightbound=1-Amin*Q(88,100)**3-Bmin*Q(88,100)**2
print('Gleft bound >',float(Gleftbound),'Gright bound <',float(Grightbound))
assert Gleftbound>0 and Grightbound<Q(-1,2)
d1=2*Bmin*Q(3,10)-3*Amax*Q(3,10)**2
d2=3*Amin*Q(69,100)**2+2*Bmin*Q(69,100)
print('derivative lower product',float(d1),float(d2),float(d1*d2));assert d1*d2>2
for s in [lo,hi]:
 d=1/(s*s*(s+1)); A=1-d; B=s+d
 assert f(s,0)==1 and f(s,1)==-s and f(s,-s)==0
 assert A>=Amin and A<=Amax and B>=Bmin and B<=Bmax
print('ALL EXACT RATIONAL CERTIFICATES PASS')
