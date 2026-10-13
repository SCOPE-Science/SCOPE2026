import mpmath as mp
mp.mp.dps=60
def f(x,p): return p/(p+1)**p*(p+1-x)**(p-1)
def fp(x,p): return -p*(p-1)/(p+1)**p*(p+1-x)**(p-2)
def logcurv(x,p): return -(p-1)/(p+1-x)**2
def hprime(x,p): return p/(p+1-x)**2
for p in (mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.9')):
    a=(p+1)*mp.mpf('0.2'); b=(p+1)*mp.mpf('0.8')
    assert fp(a,p)>0 and fp(b,p)>0 and f(a,p)<f(b,p) and logcurv(a,p)>0
p=mp.mpf('1')
for x in (mp.mpf('0.1'),mp.mpf('1.0'),mp.mpf('1.9')):
    assert abs(f(x,p)-mp.mpf('0.5'))<mp.mpf('1e-50') and fp(x,p)==0
for p in (mp.mpf('1.2'),mp.mpf('2'),mp.mpf('5')):
    a=(p+1)*mp.mpf('0.2'); b=(p+1)*mp.mpf('0.8')
    assert fp(a,p)<0 and fp(b,p)<0 and f(a,p)>f(b,p) and logcurv(a,p)<0
for p in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5')):
    const=p/(p+1)**p
    for d in (mp.mpf('1e-2'),mp.mpf('1e-5')):
        lhs=f(p+1-d,p)*d**(1-p)
        assert abs(lhs/const-1)<mp.mpf('1e-45')
    for x in ((p+1)*mp.mpf('0.1'),(p+1)*mp.mpf('0.9')): assert hprime(x,p)>0
for p in (mp.mpf('0.4'),mp.mpf('1'),mp.mpf('2.5')):
    val=mp.quad(lambda x:f(x,p),[0,p+1])
    assert abs(val-1)<mp.mpf('1e-20')
print('VERIFY_OK')
