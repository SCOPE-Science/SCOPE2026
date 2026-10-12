import mpmath as mp
mp.mp.dps = 50
pi=mp.pi

def w(j):
    n=2*j
    A=n*n-1
    return 64*n*n/(pi*pi*A**3)

def Mseries(q, N=200000):
    q=mp.mpf(q)
    return mp.nsum(lambda jj: (64*(2*jj)**2)/(pi*pi*((2*jj)**2-1)**2*(((2*jj)**2-1)+q*q)), [1, mp.inf])

def Mclosed(q):
    q=mp.mpf(q)
    if q == 0: return mp.mpf(1)
    if abs(q-1) < mp.mpf('1e-30'):
        return 4-32/pi**2
    if q < 1:
        s=mp.sqrt(1-q*q)
        return 4/q**2 - 16*s/(pi*q**4)*mp.cot(pi*s/2)
    s=mp.sqrt(q*q-1)
    return 4/q**2 - 16*s/(pi*q**4)*mp.coth(pi*s/2)

def mat_elem(n,a=1):
    f=lambda u: (1/mp.sqrt(a))*mp.sin(pi*n*(u+a)/(2*a))*u*(1/mp.sqrt(a))*mp.sin(pi*(u+a)/(2*a))
    return mp.quad(f,[-a,a])

def exact_elem(n,a=1):
    return -8*a*n*((-1)**n+1)/(pi**2*(n*n-1)**2)

sumw=mp.nsum(lambda j:w(j),[1,mp.inf])
sumwA=mp.nsum(lambda j:w(j)*((2*j)**2-1),[1,mp.inf])
assert abs(sumw-1)<mp.mpf('1e-35')
assert abs(sumwA-4)<mp.mpf('1e-35')
for n in [2,3,4,5,8]:
    assert abs(mat_elem(n)-exact_elem(n))<mp.mpf('1e-40')
for q in ['0.1','0.5','1','2','10']:
    s=Mseries(q)
    c=Mclosed(q)
    assert abs(s-c)<mp.mpf('1e-35')
    lo=3/(3+mp.mpf(q)**2)
    hi=4/(4+mp.mpf(q)**2)
    assert lo-mp.mpf('1e-35') <= c <= hi+mp.mpf('1e-35')
vals=[Mclosed(q) for q in [0,mp.mpf('0.1'),mp.mpf('0.5'),1,2,10]]
assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
q=mp.mpf(200)
assert abs(q*q*Mclosed(q)-4)<mp.mpf('0.1')
# sample exact rationalization of the Dirac threshold gap from a Laplacian deficit d
m=mp.mpf('0.7'); c0=mp.mpf('1.3'); mu=(pi/2)**2; d=mp.mpf('1e-8')
Et=c0*mp.sqrt(m*m*c0*c0+mu)
E=c0*mp.sqrt(m*m*c0*c0+mu-d)
rat=c0*d/(mp.sqrt(m*m*c0*c0+mu)+mp.sqrt(m*m*c0*c0+mu-d))
assert abs((Et-E)-rat)<mp.mpf('1e-45')
print('VERIFY_OK sum_w=%s sum_wA=%s M1=%s M10=%s q2M200=%s' % tuple(mp.nstr(x,18) for x in [sumw,sumwA,Mclosed(1),Mclosed(10),q*q*Mclosed(q)]))
