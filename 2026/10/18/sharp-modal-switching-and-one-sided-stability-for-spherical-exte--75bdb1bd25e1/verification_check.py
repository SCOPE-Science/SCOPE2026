import mpmath as mp
mp.mp.dps=50
checks=0
for d in (2,3,4,5,8,13):
 nu=mp.mpf(d)/2-1
 for R in (mp.mpf('.5'),mp.mpf('2'),mp.mpf('3.8'),mp.mpf('5.7'),mp.mpf('11.3'),mp.mpf('24.1')):
  T=lambda k: mp.quad(lambda r:r*mp.besselj(nu+k,r)**2,[0,R])
  vals=[T(k) for k in range(13)]
  expected=max(vals[0],vals[1]); observed=max(vals)
  assert abs(expected-observed)<mp.mpf('1e-40')
  for k in range(10):
   assert abs(vals[k]-vals[k+1]-R*mp.besselj(nu+k,R)*mp.besselj(nu+k+1,R))<mp.mpf('1e-40')
   assert abs(vals[k]-vals[k+2]-2*(nu+k+1)*mp.besselj(nu+k+1,R)**2)<mp.mpf('1e-40')
   checks+=2
  checks+=1
print('VERIFY_OK',checks,'integral identities/top modal comparisons')
for d in (2,3,4,7):
 nu=mp.mpf(d)/2-1
 r0=mp.besseljzero(nu,1)
 r1=mp.besseljzero(nu+1,1)
 T=lambda k,r: mp.quad(lambda x:x*mp.besselj(nu+k,x)**2,[0,r])
 for r,name in [(r0,'Jnu'),(r1,'Jnu+1')]:
  vals=[T(k,r) for k in range(5)]
  assert abs(vals[0]-vals[1])<mp.mpf('1e-40')
  if name=='Jnu+1':assert abs(vals[0]-vals[2])<mp.mpf('1e-40')
  else:assert vals[0]>vals[2]
  print('d',d,name,'R',mp.nstr(r,13),'T0-T1',mp.nstr(vals[0]-vals[1],4),'T0-T2',mp.nstr(vals[0]-vals[2],4))
