#!/usr/bin/env python3
"""Standalone finite arithmetic/numerical consistency examples; not a universal proof."""
import cmath

def b(z,a): return z*(z-a)/(1-a*z)
def db(z,a): return (2*z-a-a*z*z)/(1-a*z)**2

def roots(a,w):
    delta=(a*(w-1))**2+4*w
    sq=cmath.sqrt(delta)
    return ((-a*(w-1)+sq)/2,(-a*(w-1)-sq)/2)

def spectral(a,z):
    bvals=[b(t,a) for t in z]; bp=[db(t,a) for t in z]
    G=[[1/(1-z[i]*z[j].conjugate())**2 for j in range(2)] for i in range(2)]
    H=[[bp[i]*bp[j].conjugate()/(1-bvals[i]*bvals[j].conjugate())**2 for j in range(2)] for i in range(2)]
    det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
    inv=[[G[1][1]/det,-G[0][1]/det],[-G[1][0]/det,G[0][0]/det]]
    tr=sum(inv[i][j]*H[j][i] for i in range(2) for j in range(2))
    detH=H[0][0]*H[1][1]-H[0][1]*H[1][0]
    eig1=(tr+cmath.sqrt(tr*tr-4*detH/det))/2
    eig2=(tr-cmath.sqrt(tr*tr-4*detH/det))/2
    return eig1,eig2

positive=0; off=0
for a in (0.2,0.4,0.7):
    for w in (0.1,0.3+0.2j,-0.5):
        z=roots(a,w)
        es=sorted(spectral(a,z),key=lambda q:q.real)
        assert abs(es[0])<1e-8 and abs(es[1]-2)<1e-8,(a,w,es)
        positive+=1
        pert=(z[0]+0.037,z[1])
        assert all(abs(q)<1 for q in pert)
        em=max(x.real for x in spectral(a,pert))
        assert em<2-1e-6,(a,w,em)
        off+=1
print('VERIFY_OK degree_two_full_fibers=%d degree_two_off_fibers=%d' % (positive,off))
