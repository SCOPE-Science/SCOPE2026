#!/usr/bin/env python3
"""Finite checks for exact cut spectra of Katz-weighted star Ising states.
Run: python3 verify_rank.py (requires numpy). Not an infinite-dimensional proof.
"""
import cmath, math
import numpy as np


def prediction(m, a, beta):
    b = m - a
    entries = np.zeros((b + 1, b + 1), dtype=complex)
    for j in range(b + 1):
        for k in range(b + 1):
            r = j - k
            if r % 2 == 0:
                entries[j, k] = (math.sqrt(math.comb(b, j) * math.comb(b, k)) / 2**b
                                  * cmath.exp(0.5j * math.pi * beta * a * r)
                                  * math.cos(0.5 * math.pi * beta * r)**a)
    purity = sum(math.comb(2*b,b + 2*r) * math.cos(math.pi*beta*r)**(2*a)
                 for r in range(-b//2,b//2+1) if 0 <= b+2*r <= 2*b)/4**b
    return entries, purity

def expected_rank(m, a, kind, p=None, q=None):
    b = m-a
    if kind == 'irrational':
        s = 2*(a+1)
    else:
        assert math.gcd(p,q)==1
        s = 2*min(a+1,q)
    return min(b+1,s)

def direct(m, a, beta):
    b=m-a
    D=1-m*beta*beta
    t=math.pi*D/2
    matrix=np.zeros((2**(a+1),2**b),complex)
    norm=2**(-(m+1)/2)
    for x in range(2**(m+1)):
        zz=[1-2*((x>>i)&1) for i in range(m+1)]
        val=zz[0]*sum(zz[1:])
        leaves=zz[1:]
        val+=beta*(sum(leaves)**2-m)/2
        amplitude=norm*cmath.exp(0.5j*t*val/D)
        # layout: center and first a leaves -> row, remaining leaves -> col
        row=x&((1<<(a+1))-1)
        col=x>>(a+1)
        matrix[row,col]=amplitude
    return np.linalg.svd(matrix,compute_uv=False)**2

def check():
    total=0
    for m in range(1,9):
        cases=[]
        for q in range(2,10):
            for p in range(1,q):
                beta=p/q
                if math.gcd(p,q)==1 and 0<beta<1/math.sqrt(m):cases.append((beta,'rational',p,q))
        for beta in [math.sqrt(2)/8, math.pi/20]:
            if beta<1/math.sqrt(m):cases.append((beta,'irrational',None,None))
        for a in range(0,m):
            b=m-a
            for beta,kind,p,q in cases:
                G, pur=prediction(m,a,beta)
                eig=np.linalg.eigvalsh(G)
                if eig.min() < -1e-10:raise AssertionError(('PSD',m,a,beta,eig.min()))
                if abs(eig.sum()-1)>1e-10:raise AssertionError(('trace',m,a,beta,eig.sum()))
                if abs(np.sum(eig**2)-pur)>1e-10:raise AssertionError(('purity',m,a,beta,np.sum(eig**2),pur))
                expected=expected_rank(m,a,kind,p,q)
                numerical=int((eig>1e-9).sum())
                if numerical!=expected:raise AssertionError(('rank',m,a,beta,numerical,expected,eig))
                got=direct(m,a,beta)
                eig2=np.sort(eig)[::-1]
                got=np.sort(got)[::-1]
                if len(got)<len(eig2):got=np.pad(got,(0,len(eig2)-len(got)))
                if len(eig2)<len(got):eig2=np.pad(eig2,(0,len(got)-len(eig2)))
                if max(abs(eig2-got))>1e-10:raise AssertionError(('direct',m,a,beta,eig2,got))
                total+=1
    print(f'DIRECT_SPECTRUM_PURITY_RANK_OK {total} cases')
    # Exact residue-class tests (integer arithmetic, independently of SVD).
    residue_tests=0
    for q in range(2,24):
        for p in range(1,q):
            if math.gcd(p,q)!=1:continue
            for a in range(0,50):
                residues={(p*i+c*q)%(2*q) for c in (0,1) for i in range(a+1)}
                if len(residues)!=2*min(a+1,q):
                    raise AssertionError(('residue-count',p,q,a,len(residues)))
                residue_tests+=1
    print('EXACT_RESIDUE_COUNT_OK',residue_tests)
    # A fixed-cardinality Schmidt-rank resonance resolved numerically at stable size.
    for m,a,beta,kind,p,q in [(13,5,1/4,'rational',1,4),
                              (13,5,math.sqrt(2)/6,'irrational',None,None),
                              (80,30,1/10,'rational',1,10)]:
        b=m-a
        G,purity=prediction(m,a,beta)
        eig=np.linalg.eigvalsh(G)
        predicted=expected_rank(m,a,kind,p,q)
        count=int((eig>1e-10).sum())
        if count!=predicted:raise AssertionError(('resonance-rank',m,a,beta,count,predicted))
        print('RESONANCE_OK',m,a,b,repr(beta),predicted,'purity',purity)
    print('VERIFY_OK')
if __name__=='__main__':check()
