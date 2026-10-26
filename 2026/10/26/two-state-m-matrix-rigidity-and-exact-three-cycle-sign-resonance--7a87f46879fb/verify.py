"""Independent numerical checks for the three-state inverse averaged semigroup theorem.
No external scientific data or software services are used.
"""
from mpmath import mp

mp.dps = 90
P = mp.matrix([[0,1,0],[0,0,1],[1,0,0]])
I = mp.eye(3)

def phi1(X):
    Y = mp.eye(X.rows)
    term = mp.eye(X.rows)
    for k in range(1,700):
        term = term*X/(k+1)
        Y += term
        if mp.norm(term, 'inf') < mp.mpf('1e-75'):
            break
    else:
        raise RuntimeError('Taylor series did not converge')
    return Y

def predicted_b2(t):
    h=mp.sqrt(3)*t/2
    return mp.mpf(1)/3 - 2*h*mp.sin(h)/(3*(mp.cosh(mp.sqrt(3)*h)-mp.cos(h)))

count = 0
for t_text in ['0.01','0.1','0.25','0.5','1','2','3','4','5','7','9','11','14']:
    t=mp.mpf(t_text)
    F=phi1(t*(P-I))
    B=F**-1
    assert mp.norm(B*F-I,'inf') < mp.mpf('1e-60')
    for i in range(3):
        for j in range(3):
            assert abs(B[i,j]-B[0,(j-i)%3]) < mp.mpf('1e-60')
    b0,b1,b2=(B[0,j] for j in range(3))
    assert b0>0 and b1<0 and b2>0
    assert abs(b0+b1+b2-1)<mp.mpf('1e-60')
    assert abs(b2-predicted_b2(t))<mp.mpf('1e-60')
    count += 4

for k in range(1,6):
    t=2*k*mp.pi/mp.sqrt(3)
    assert abs(predicted_b2(t)-mp.mpf(1)/3)<mp.mpf('1e-80')
    count += 1
for j in range(1,21):
    c=3**j+(-1)**j*(4*j-1)
    assert (c==0 if j==1 else c>0)
    count += 1
for t in [mp.mpf('0.1'),mp.mpf('1'),mp.mpf('10')]:
    f=2*t/(1-mp.exp(-2*t))
    off=(1-f)/2
    assert off<0
    count+=1
for a,b in [(mp.mpf('0'),mp.mpf('0')),(mp.mpf('0'),mp.mpf('2')),(mp.mpf('2'),mp.mpf('0')),(mp.mpf('1.25'),mp.mpf('3.5'))]:
    G=mp.matrix([[-a,a],[b,-b]])
    X=phi1(mp.mpf('0.8')*G)**-1
    if a+b:
        v=mp.mpf('0.8')*(a+b)
        f=v/(1-mp.exp(-v))
        gamma=(f-1)/(a+b)
        Z=mp.eye(2)-gamma*G
    else:
        Z=mp.eye(2)
    assert mp.norm(X-Z,'inf')<mp.mpf('1e-60')
    assert X[0,1]<=0 and X[1,0]<=0
    count+=2
print('VERIFY_OK',count)
