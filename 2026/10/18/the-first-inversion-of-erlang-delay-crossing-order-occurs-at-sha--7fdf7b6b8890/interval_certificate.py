#!/usr/bin/env python3
"""Exact rational interval proof for the first reversed adjacent Erlang crossing order."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

def atan_pair(inv, terms=14):
    x=F(1,inv)
    arr=[((-1)**j)*x**(2*j+1)/F(2*j+1) for j in range(2*terms+1)]
    return sum(arr[:-1],F(0)),sum(arr,F(0))

a5,b5=atan_pair(5,terms=10);a239,b239=atan_pair(239,terms=10)
pil,pih=16*a5-4*b239,16*b5-4*a239
S_PI=10**15
PI_LO,PI_HI=F((pil*S_PI).__floor__(),S_PI),F((pih*S_PI).__ceil__(),S_PI)
assert F(314159,100000)<PI_LO<PI_HI<F(314160,100000)

def taylor_pair(x,powshift,N=5):
    # N pairs, last negative yields low, next positive yields high
    terms=[((-1)**j)*x**(2*j+powshift)/F(factorial(2*j+powshift)) for j in range(2*N+1)]
    return sum(terms[:-1],F(0)),sum(terms,F(0))

@lru_cache(None)
def trig_interval(m,k):
    xlo=F(k,m)*PI_LO; xhi=F(k,m)*PI_HI
    sl,_=taylor_pair(xlo,1);_,sh=taylor_pair(xhi,1)
    cl,_=taylor_pair(xhi,0);_,ch=taylor_pair(xlo,0)
    assert 0<sl<sh and 0<cl<ch
    S=10**12
    return F((sl*S).__floor__(),S),F((sh*S).__ceil__(),S),F((cl*S).__floor__(),S),F((ch*S).__ceil__(),S)

def rho_interval(m,k):
    sl,sh,cl,ch=trig_interval(m,k)
    SL,SH,CL,CH=trig_interval(m,k+1)
    tl,th=sl/ch,sh/cl;TL,TH=SL/CH,SH/CL
    al=TL*TL-th*th;au=TH*TH-tl*tl
    dl=tl*tl*CL**m+TL*TL*cl**m
    du=th*th*CH**m+TH*TH*ch**m
    assert al>0 and dl>0
    return al/du,au/dl

if __name__=='__main__':
 import time
 s=time.monotonic()
 ntest=0
 smallest=(None,None,None)
 for m in range(3,28):
  for k in range(2,(m-1)//2,2):
   low,high=rho_interval(m,k)
   ntest+=1
   assert low>1,('earlier inversion',m,k,float(low))
   if smallest[0] is None or low<smallest[0]:smallest=(low,m,k)
 l,h=rho_interval(28,2)
 assert F(99,100)<l<h<F(999,1000)
 for k in range(4,13,2):
  lo,hi=rho_interval(28,k)
  assert lo>1,(28,k,float(lo))
 print('PASS all '+str(ntest)+' comparison intervals for shape m<28 strictly >1')
 print('minimum certified earlier lower-bound at m,k',smallest[1:], ' >',str(float(smallest[0])))
 print('at m=28,k=2: ',float(l),'< rho <',float(h),' < 0.999')
 print('PASS exact minimal Erlang stage threshold 28 for any b/a in (0,1)')
 # Rational enclosure of normalized squared critical delays at coupling ratio 999/1000.
 r=F(999,1000)
 def t2_interval(m,k):
  sl,sh,cl,ch=trig_interval(m,k)
  tl,th=sl/ch,sh/cl
  if k%2:
   dl,du=1+r*cl**m,1+r*ch**m
  else:
   dl,du=1-r*ch**m,1-r*cl**m
  assert dl>0
  return tl*tl/du,th*th/dl
 for k,j in [(1,3),(3,2),(2,4)]+[(k,k+1) for k in range(4,13)]:
  lo1,hi1=t2_interval(28,k);lo2,hi2=t2_interval(28,j)
  assert hi1<lo2,(k,j,float(hi1),float(lo2))
 print('PASS exact critical-delay order 1<3<2<4<5<...<13 for m=28,b/a=999/1000')
 print('seconds',time.monotonic()-s)
