#!/usr/bin/env python3
"""Check finite Fourier sampling identities for a one-point-punctured two-layer set.

Run with Python 3 and NumPy. All finite tests are confirmations, not infinite proofs.
"""
import itertools
import math
import numpy as np


def trial(factors, m, exhaustive=False):
    H = list(itertools.product(*(range(k) for k in factors)))
    n = len(H)
    dual = H
    chars = np.asarray([[np.exp(2j*np.pi*sum(a*b/q for a,b,q in zip(x,xi,factors)))
                         for xi in dual] for x in H])
    missing = H[0]
    E = [(x,y) for x in H for y in (0,1) if not (x==missing and y==1)]
    z = np.exp(2j*np.pi*np.arange(m)/m)
    freq = [(a,b) for a in range(n) for b in range(m)]
    M = np.array([ [chars[H.index(x),a]*z[b]**y for a,b in freq] for x,y in E ],complex)
    gap = m//2
    B = []
    for a in range(n):
        if a==0: B.append(a*m)
        else: B.extend((a*m+0,a*m+gap))
    T=M[:,B]; G=T.conj().T@T
    assert np.linalg.slogdet(G)[0]>0
    c=1.0 if m%2==0 else math.cos(math.pi/(2*m))
    expected_det=(2*n*c)**(2*(n-1))
    det=float(np.linalg.det(G).real)
    assert abs(det-expected_det)/expected_det<1e-8,(factors,m,det,expected_det)
    vals=np.linalg.eigvalsh(G)
    if m%2==0:
        expected=np.array([1.0]+[2*n]*(2*n-2))
        assert np.allclose(vals,expected,atol=1e-8)
    else:
        s=math.sin(math.pi/(2*m))
        yroots=np.roots([2*n,-(2*n-1),-2*s*s,s*s])
        assert max(abs(yroots.imag))<1e-10
        predicted=[2*n*(1-float(y.real)) for y in yroots]
        predicted += [2*n*(1-s)]*(n-2)+[2*n*(1+s)]*(n-2)
        assert np.allclose(vals, sorted(predicted),atol=1e-8)

    tested=0
    if exhaustive:
        optimal_count=0
        bases_count=0
        global_ratio=float('inf')
        for S in itertools.combinations(range(n*m),2*n-1):
            cnt=[0]*n
            for j in S:cnt[j//m]+=1
            is_basis=(sorted(cnt)==[1]+[2]*(n-1))
            A=M[:,S]
            vals0=np.linalg.eigvalsh(A.conj().T@A)
            if is_basis:
                bases_count+=1
                assert vals0[0]>1e-8
                dd=float(np.prod(vals0))
                assert dd<=expected_det*(1+1e-8)
                if abs(dd/expected_det-1)<1e-7:optimal_count+=1
                global_ratio=min(global_ratio,vals0[-1]/vals0[0])
            else:
                assert vals0[0]<1e-7
            tested+=1
        K=(m//2 if m%2==0 else m)
        expected_opt=n*m*K**(n-1)
        assert optimal_count==expected_opt,(factors,m,optimal_count,expected_opt)
        if m%2==0:
            assert abs(global_ratio-2*n)<1e-7,(global_ratio,2*n)
        else:
            assert global_ratio>2*n-1e-7
        print('exhaustive',factors,'m',m,'sets',tested,'bases',bases_count,
              'D-max partners',optimal_count,'optimal ratio',format(global_ratio,'.10g'))
    print('spectrum',factors,'m',m,'max determinant squared',f'{det:.10g}',
          'min eigen',f'{vals[0]:.10g}','max eigen',f'{vals[-1]:.10g}')


def main():
    for factors,m in [((2,),2),((2,),3),((2,),4),((3,),3),((3,),5),((4,),3),
                       ((4,),4),((2,2),3),((2,2),5),((2,2),6),((5,),7)]:
        trial(factors,m,exhaustive=(factors,m) in {
            ((2,),2),((2,),3),((2,),4),((3,),3),((3,),5),((4,),3),((2,2),3)})
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
