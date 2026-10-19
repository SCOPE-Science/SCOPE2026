"""Exhaustive finite-field checks for the multiplicative coordinate Fourier Gram spectra.

The claimed all-field theorem rests on character orthogonality and explicit
counting, not on these small-field checks. Requires Python 3 and NumPy.
"""
import itertools,cmath,math
import numpy as np

def field(q):
    if q == 4:
        add = lambda a,b:a^b
        def mul(a,b):
            z=0
            while b:
                if b&1: z^=a
                b>>=1
                a<<=1
                if a&4:a^=7
            return z
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    els=list(range(1,q))
    for g in els:
        p=1; order=[]
        for t in range(q-1):
            order.append(p);p=mul(p,g)
        if p==1 and len(set(order))==q-1:break
    else:raise ValueError('No generator')
    log={v:i for i,v in enumerate(order)}
    return add,els,log


def theoretical(q,d):
    n=((q-1)**d+(q-1)*(-1)**d)//q
    c=(q-1)*(-1)**d/n
    result=[1.0]
    if q%2:
        for parity,mult in ((1,(q-3)//2),(-1,(q-1)//2)):
            result += [1+c*(d-1)*parity]*mult
            result += [1-c*parity]*((d-1)*mult)
    else:
        result += [1+c*(d-1)]*(q-2)
        result += [1-c]*((d-1)*(q-2))
    return sorted(result),n,c


def check(q,d):
    add,els,log=field(q)
    xs=[]
    for x in itertools.product(els,repeat=d):
        s=0
        for a in x:s=add(s,a)
        if s==0:xs.append(x)
    cols=[np.ones(len(xs),dtype=complex)]
    w=cmath.exp(2j*math.pi/(q-1))
    for i in range(d):
        for k in range(1,q-1):
            cols.append(np.array([w**(k*log[x[i]]) for x in xs]))
    M=np.column_stack(cols)
    calc=np.linalg.eigvalsh(M.conj().T @ M / len(xs))
    theo,n,c=theoretical(q,d)
    assert n==len(xs), (q,d,n,len(xs))
    err=max(abs(calc-np.array(theo)))
    assert err<3e-11,(q,d,err)
    return q,d,n,len(cols),float(err),sum(v<1e-8 for v in theo)

def predicted_affine(q,d):
    m=q-1;e=(-1)**d
    N=(m**d-e)//q
    C=(m**(d-1)+e)//q
    assert N==m*C-e
    eig=[]
    eps=[(1,(q-3)//2),(-1,(q-3)//2)] if q%2 else [(1,(q-4)//2),(-1,(q-2)//2)]
    for sigma,r in eps:
        eig += [m*(C+(d-1)*e*sigma)/N]*r
        eig += [m*(C-e*sigma)/N]*((d-1)*r)
    eig += [m*(C-e)/N]*(d-1)
    B=np.array([[1.,-e*math.sqrt(d*(m-1))/N],[-e*math.sqrt(d*(m-1))/N,(m*C+e*(d-m))/N]])
    eig += np.linalg.eigvalsh(B).tolist()
    assert len(eig)==1+d*(q-2)
    return sorted(eig),N

def check_affine(q,d):
    add,els,log=field(q)
    xs=[]
    for x in itertools.product(els,repeat=d):
        s=0
        for v in x:s=add(s,v)
        if s==1:xs.append(x)
    w=cmath.exp(2j*math.pi/(q-1))
    cols=[np.ones(len(xs),dtype=complex)]
    for i in range(d):
        for k in range(1,q-1):
            cols.append(np.array([w**(k*log[x[i]]) for x in xs]))
    M=np.column_stack(cols)
    actual=np.linalg.eigvalsh(M.conj().T @ M / len(xs))
    theor,N=predicted_affine(q,d)
    assert len(xs)==N,(q,d,len(xs),N)
    err=max(abs(actual-np.array(theor)))
    assert err<5e-11,(q,d,err,actual,theor)
    return q,d,N,len(cols),float(err),sum(v<1e-8 for v in theor)


if __name__=='__main__':
    tests=[(3,d) for d in range(3,11)]+[(4,d) for d in range(3,8)]+[(5,d) for d in range(3,7)]+[(7,d) for d in range(3,6)]+[(11,d) for d in range(3,5)]
    for q,d in tests:
        r0=check(q,d)
        r1=check_affine(q,d)
        print('q=%d d=%d b=0:%d/%d rank=%d; b=1:%d/%d rank=%d; maxerr=%.3g'%(q,d,r0[2],r0[3],r0[3]-r0[5],r1[2],r1[3],r1[3]-r1[5],max(r0[4],r1[4])))
    print('PASS %d cardinality checks, %d independently assembled Fourier Gram spectra'%(2*len(tests),2*len(tests)))
