import mpmath as mp
mp.mp.dps=65
checks=0

def close(a,b,tol):
 global checks
 assert abs(a-b)<tol, (mp.nstr(a,35),mp.nstr(b,35),tol)
 checks+=1

def formulas(T,tau,d):
 A=tau; B=T-tau
 dv=mp.sqrt(B*B+d)-mp.sqrt(A*A+d)-(B-A)
 moment=(A*mp.sqrt(A*A+d)+B*mp.sqrt(B*B+d)-d*(mp.asinh(A/mp.sqrt(d))+mp.asinh(B/mp.sqrt(d)))-A*A-B*B)/2
 dx=B*dv-moment
 return dv,dx

def direct(T,tau,d):
 f=lambda t: (t-tau)/mp.sqrt((t-tau)**2+d)-mp.sign(t-tau)
 return mp.quad(f,[0,tau,T]),mp.quad(lambda t:(T-t)*f(t),[0,tau,T])

for T,tau in [(mp.mpf('2.3'),mp.mpf('.7')),(mp.mpf('2'),mp.mpf('1')),(mp.mpf('1.8'),mp.mpf('1.2'))]:
 for d in map(mp.mpf,['0.4','0.0003','1e-8','1e-14']):
  v,x=formulas(T,tau,d)
  vn,xn=direct(T,tau,d)
  close(v,vn,mp.mpf('1e-52'))
  close(x,xn,mp.mpf('1e-52'))
  if T==2*tau:close(v,0,mp.mpf('1e-53'))
for delta in map(mp.mpf,['1e-10','1e-20','1e-35']):
 dv,dx=formulas(mp.mpf('2.3'),mp.mpf('.7'),delta)
 predicted=delta*mp.log(1/delta)/2
 assert abs(dx/predicted-1)<mp.mpf('0.12'), mp.nstr(dx/predicted,20)
 checks+=1

def weak(S,w,a,b,d,c):
 g=lambda x: x/mp.sqrt(x*x+d)-mp.sign(x)
 return mp.quad(lambda t:w(t)*g(S(t)),[a,0,b])
for beta in [mp.mpf('.25'),mp.mpf('-.375')]:
 S=lambda t:t+beta*t*t
 w=lambda t:mp.mpf('1')
 for d in map(mp.mpf,['1e-8','1e-16','1e-28']):
  J=weak(S,w,mp.mpf('-.4'),mp.mpf('.4'),d,0)
  expected=beta*d*mp.log(1/d)
  assert abs(J/expected-1)<mp.mpf('.2'), (mp.nstr(J,20),mp.nstr(expected,20))
  checks+=1
print('VERIFY_OK',checks)
