"""Exact Rayleigh cross-check for the explicit SL(2,7) witness.

This script deliberately does NOT use one test vector as an upper bound on the
second eigenvalue.  For a vector perpendicular to constants its Rayleigh
quotient is a lower bound on the maximum Rayleigh quotient on that subspace.
The Ramanujan upper certificate is supplied by the exact positive-definiteness
certificate in bareiss_cert.py (and can also be checked by exact characteristic
polynomial factorization).
"""
import json, os
q=7
M=[(a,b,c,d) for a in range(q) for b in range(q) for c in range(q) for d in range(q) if (a*d-b*c)%q==1]
idx={m:i for i,m in enumerate(M)}
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
SR=[(6,0,0,6),(4,2,6,5),(2,4,5,0),(1,4,0,1),(5,5,1,4),(0,3,2,2),(1,3,0,1)]
nbr=[[idx[mul(x,g)] for g in SR] for x in M]
d=json.load(open(os.path.join(os.path.dirname(__file__),'rayleigh_vec.json')))
w=d['w']
assert len(w)==336 and sum(w)==0 and any(w)
qq=sum(a*a for a in w)
p=sum(w[i]*w[j] for i in range(336) for j in nbr[i])
assert p==55177273021248 and qq==11289966448320
assert p*p < 24*qq*qq
assert 100*p <= 489*qq
print('Rayleigh numerator =',p)
print('Rayleigh denominator =',qq)
print('quotient < 4.89 < 2*sqrt(6): exact')
print('Interpretation: lower-bound/eigenvector cross-check only; not an upper certificate.')
print('EXACT_RAYLEIGH_CROSSCHECK_OK')
