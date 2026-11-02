"""Reproduce powered-distance spectral decomposition for one-vertex bouquets of 5-cycles.
Run: python3 c5_bouquet_checker.py. Uses NumPy/SciPy for supplementary finite checks.
Analytic arguments in RESULT.md establish assertions for all k and p.
"""
import math
from collections import deque
import numpy as np
from scipy.optimize import brentq

PC = math.log2((3+math.sqrt(5))/2)
L2,L3=math.log(2),math.log(3)
B=68*L2-36*L3
C=16*L2**2+48*L2*L3-36*L3**2
THETA=10/(B+math.sqrt(B*B-20*C))

def blocks(p,k):
    a,b=2**p,3**p
    base=np.array([[a-4,-(a+1)],[-(a+1),1-4*a]])
    cross=2*np.array([[a-2,b-a-1],[b-a-1,a*a-2*a]])
    anti=np.array([[-a,1-a],[1-a,-1]])
    return base+(k-1)*cross,base-cross,anti,cross

def epsilon(p,k):
    return np.linalg.eigvalsh(blocks(p,k)[0])[-1]

def critical(k):
    assert k>=2
    return brentq(lambda p:epsilon(p,k),1+1e-10,PC,xtol=1e-13)

def distances(k):
    n=1+4*k
    adj=[set() for _ in range(n)]
    for t in range(k):
        vs=[0]+[1+4*t+i for i in range(4)]
        for i in range(5):
            x,y=vs[i],vs[(i+1)%5]
            adj[x].add(y);adj[y].add(x)
    D=np.zeros((n,n),int)
    for s in range(n):
        dist={s:0}; todo=deque([s])
        while todo:
            x=todo.popleft()
            for y in adj[x]:
                if y not in dist:
                    dist[y]=dist[x]+1;todo.append(y)
        assert len(dist)==n
        for j,d in dist.items(): D[s,j]=d
    return D

def fullT(p,k):
    d=distances(k).astype(float)**p
    return d[1:,1:]-d[0,1:][None,:]-d[0,1:][:,None]

def predicted_spectrum(p,k):
    uniform,contr,anti,_=blocks(p,k)
    return np.sort(np.concatenate((np.linalg.eigvalsh(uniform),
       np.tile(np.linalg.eigvalsh(contr),k-1),
       np.tile(np.linalg.eigvalsh(anti),k))))

def run():
    tests=0
    for k in range(2,12):
        pc=critical(k)
        assert 1<pc<PC
        assert epsilon(1,k)<0 and abs(epsilon(pc,k))<2e-11
        tests+=3
        for p in (0.3,0.9,1,1.02,(1+pc)/2,pc,min(1.5,pc+0.05)):
            observed=np.linalg.eigvalsh(fullT(p,k))
            predicted=predicted_spectrum(p,k)
            assert np.allclose(observed,predicted,atol=3e-12,rtol=3e-12),(k,p)
            tests+=len(observed)
        obs=np.linalg.eigvalsh(fullT(pc,k))
        assert abs(obs[-1])<1e-10 and obs[-2]<-1e-7,(k,obs[-2:])
        tests+=2
        assert np.linalg.eigvalsh(fullT(max(0.001,pc-0.01),k))[-1]<0
        assert np.linalg.eigvalsh(fullT(pc+0.01,k))[-1]>0
        tests+=2
    ps=[critical(k) for k in range(2,102)]
    assert all(ps[i]>ps[i+1] for i in range(len(ps)-1))
    tests+=len(ps)-1
    for k in (100,300,1000,3000):
        p=critical(k)
        assert abs((k-1)*(p-1)-THETA) < 1.5/(k-1)
        tests+=1
    print('PASS:', tests, 'supplementary finite spectral and asymptotic assertions')
    print('theta =',THETA)
    for k in (2,3,4,5,10,20,100):print(k,critical(k))

if __name__=='__main__': run()
