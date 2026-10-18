#!/usr/bin/env python3
"""Independent checks for large-numerator continued-fraction digit correlations.
Requires mpmath (arbitrary-precision arithmetic). This verifies finite identities and
numerical scaling; it does not replace the uniform operator proof.
"""
import mpmath as mp
mp.mp.dps = 65
checks = 0
for N in (1, 2, 3, 8, 20):
    for m in (N + 1, N + 3, 2*N + 5):
        for x in (mp.mpf('0.13'), mp.mpf('0.47'), mp.mpf('0.83')):
            target=(N+x)/(m+x)
            # Exact telescoping of the branch weights whose digit is >=m.
            total=mp.nsum(lambda a:(N+x)/((a+x)*(a+x+1)),[m,mp.inf])
            assert abs(total-target)<mp.mpf('1e-55')
            checks+=1
for N in (1,2,4,12,50):
    z=mp.mpf(N)+mp.mpf('0.37')
    exact=N*(z*mp.polygamma(1,z)-1)
    direct=mp.nsum(lambda a:(N+mp.mpf('0.37'))/((a+mp.mpf('0.37'))*(a+mp.mpf('1.37')))*N/(a+mp.mpf('0.37')),[N,mp.inf])
    assert abs(exact-direct)<mp.mpf('1e-52')
    checks+=1
values=[]
for N in (10,40,160):
    m,n=2*N,3*N
    L=mp.log1p(mp.mpf(1)/N)
    q=mp.log1p(mp.mpf(1)/m)/L
    r=mp.log1p(mp.mpf(1)/n)/L
    c1=mp.log1p(mp.mpf(N)/(m*n))/L-q*r
    p2=lambda x:(N+x)*(mp.digamma(N+x+mp.mpf(N)/m)-mp.digamma(N+x))
    c2=mp.quad(lambda x:p2(x)/(N+x),[0,mp.mpf(N)/n])/L-q*r
    target1=-mp.mpf(1)/36 # u(1-u)v(1-v)/2 with u=1/2,v=1/3
    target2=mp.mpf(1)/72
    assert c1<0 and c2>0
    assert abs(N*c1-target1)<mp.mpf('0.012')/N
    assert abs(N*N*c2-target2)<mp.mpf('0.011')/N
    values.append((N,float(N*c1),float(N*N*c2)))
    checks+=2
print('VERIFY_OK:',checks,'exact/numerical comparisons; finite-lag scaled values=',values)
