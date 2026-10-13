"""Reproduce heterogeneous amplitude-damping GHZ phase-sensing identities."""
import itertools
import math
import random
import numpy as np

def kron_all(seq):
    acc = np.array([[1.0]], dtype=complex)
    for a in seq:
        acc = np.kron(acc, a)
    return acc

def direct_qfi(ps):
    n = len(ps)
    dim = 2**n
    vec = np.zeros(dim, dtype=complex)
    vec[0] = vec[-1] = 1/math.sqrt(2)
    rho = np.outer(vec, vec.conj())
    for i,p in enumerate(ps):
        k0=np.array([[1,0],[0,math.sqrt(1-p)]],dtype=complex)
        k1=np.array([[0,math.sqrt(p)],[0,0]],dtype=complex)
        a0 = kron_all([k0 if j==i else np.eye(2) for j in range(n)])
        a1 = kron_all([k1 if j==i else np.eye(2) for j in range(n)])
        rho = a0 @ rho @ a0.conj().T + a1 @ rho @ a1.conj().T
    eigs, vecs=np.linalg.eigh(rho)
    eigs=np.maximum(eigs,0)
    z=np.array([0.5*(n-2*k.bit_count()) for k in range(dim)],dtype=float)
    J = (vecs.conj().T * z) @ vecs
    qfi=0.0
    for i,j in itertools.product(range(dim), repeat=2):
        if eigs[i]+eigs[j]>1e-11:
            qfi+=2*(eigs[i]-eigs[j])**2/(eigs[i]+eigs[j])*abs(J[i,j])**2
    return float(qfi)

def theorem_qfi(ps):
    n=len(ps)
    Q=math.prod(1-p for p in ps)
    R=math.prod(ps)
    return 2*n*n*Q/(1+Q+R)

def main():
    count=0
    rng=random.Random(713203)
    for n in range(2,6):
        for _ in range(12):
            ps=[rng.random()*.92 for j in range(n)]
            a,b=direct_qfi(ps),theorem_qfi(ps)
            assert abs(a-b)<4e-10,(n,ps,a,b)
            count+=1
    for n in range(2,14):
        for _ in range(100):
            ps=[rng.random() for i in range(n)]
            i,j=rng.sample(range(n),2)
            old=theorem_qfi(ps)
            mid=(ps[i]+ps[j])/2
            ps[i]=ps[j]=mid
            new=theorem_qfi(ps)
            assert new+1e-10>=old,(n,new,old)
            count+=1
    for n in range(2,13):
        for _ in range(250):
            ps=[rng.random() for i in range(n)]
            s=sum(ps)
            uniform=theorem_qfi([s/n]*n)
            minimum=(2*n*n*(1-s)/(2-s)) if s<1 else 0.0
            q=theorem_qfi(ps)
            assert minimum-1e-10<=q<=uniform+1e-10,(n,ps,q,minimum,uniform)
            count+=1
    for n in range(2,40):
        lo,hi=0,n
        for _ in range(80):
            s=(lo+hi)/2
            u=s/n
            if (2*n-1)*(1-u)**n>1+u**n:lo=s
            else:hi=s
        star=(lo+hi)/2
        low=2*(n-1)/(2*n-1)
        assert low<star<n
        count+=1
    for n in [10,20,50,100,200,500]:
        lo,hi=0,n
        for _ in range(100):
            s=(lo+hi)/2
            if (2*n-1)*(1-s/n)**n>1+(s/n)**n: lo=s
            else:hi=s
        x=math.log(2*n-1)
        approx=x-x*x/(2*n)
        assert abs((lo-approx)/(x**3/n**2))<0.5,(n,lo,approx)
        count+=1
    print('VERIFY_OK',count,'direct_density_QFI',48,'majorization',1200,'extrema',2750,'threshold',38,'asymptotics',6)
if __name__ == '__main__':main()
