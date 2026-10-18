#!/usr/bin/env python3
"""High-precision checks of finite Stieltjes-jet recovery for mean-zero periodic Dirichlet series."""
import math
import mpmath as mp
mp.mp.dps = 45
CASES = 0

def basis(q, x, s, i):
    if s == 1:
        return (mp.stieltjes(0,(x+i)/q)-mp.stieltjes(0,(x+i+1)/q))/q
    return (mp.zeta(s, (x+i)/q)-mp.zeta(s, (x+i+1)/q))*q**(-s)

def jet_matrix(q,x):
    # gamma_k of H_i(s), where H_i is the L-series for f=e_i-e_{i+1}
    logq=mp.log(q)
    return mp.matrix([[sum(mp.binomial(k,j)*logq**(k-j)*(mp.stieltjes(j,(x+i)/q)-mp.stieltjes(j,(x+i+1)/q)) for j in range(k+1))/q for i in range(q-1)] for k in range(q-1)])

for q in range(2,6):
    for xraw in ['0.7','2.3']:
        x=mp.mpf(xraw)
        m=q-1
        J=jet_matrix(q,x)
        determinant=mp.det(J)
        assert determinant>0, (q,x,determinant)
        v=mp.matrix([mp.mpf((i+1)*(-1)**i)/7 for i in range(m)])
        y=J*v
        recovered=mp.lu_solve(J,y)
        err=max(abs(recovered[i]-v[i]) for i in range(m))
        assert err<mp.mpf('1e-28'), (q,x,err)
        # The evaluation kernel has orientation (-1)^(m*(m-1)/2)
        svals=[mp.mpf('0.4')+mp.mpf(i)*mp.mpf('0.33') for i in range(m)]
        M=mp.matrix([[basis(q,x,s,i) for i in range(m)] for s in svals])
        assert mp.det(M)*(-1)**(m*(m-1)//2)>0, (q,x,'evaluation sign')
        CASES+=1
        print('q=%d x=%s: det(G)=%s, max recovery residual=%s'%(q,xraw,mp.nstr(determinant,12),mp.nstr(err,5)))

# Sharpness: prescribe q-2 zeros; the unique nonzero linear combination has exactly these zeros.
q=5; x=mp.mpf('0.75'); m=q-1
sites=[mp.mpf('0.5'),mp.mpf('0.9'),mp.mpf('1.45')]
A=mp.matrix([[basis(q,x,s,i) for i in range(m)] for s in sites])
last=mp.lu_solve(A[:,:m-1],-A[:,m-1])
weights=[last[i] for i in range(m-1)]+[mp.mpf(1)]
res=max(abs(sum(A[k,i]*weights[i] for i in range(m))) for k in range(m-1))
assert res<mp.mpf('1e-28')
print('sharp q=5 prescribed 3 zeros at',sites, 'residual',mp.nstr(res,5))
print('PASS: %d parameter cases, positive Stieltjes-jet determinants, sign-regular evaluations and exact-data recovery; one sharpness construction.'%CASES)
