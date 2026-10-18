import math
import numpy as np

def build(b,h):
    vertices=[()]
    for d in range(1,h+1):
        vertices += [v+(j,) for v in list(x for x in vertices if len(x)==d-1) for j in range(b)]
    d={v:i for i,v in enumerate(vertices)}
    N=len(vertices)
    A=np.zeros((N,N), dtype=float)
    for v in vertices:
        for k in range(len(v)+1):
            u=v[:k]
            A[d[v],d[u]]=b**(-(len(v)-k)/2)
    return A,vertices

def expected(b,h):
    out=[]
    for d in range(h+1):
        L=h-d+1
        mult=1 if d==0 else (b-1)*b**(d-1)
        for j in range(1,L+1):
            out.extend([1/(2*math.sin((2*j-1)*math.pi/(4*L+2)))]*mult)
    return np.sort(np.array(out))

for b in [2,3,4]:
 for h in range(5 if b==2 else 4):
    A,V=build(b,h)
    sv=np.linalg.svd(A,compute_uv=False)
    ex=expected(b,h)
    assert len(ex)==len(sv), (b,h,len(ex),len(sv))
    assert np.max(np.abs(np.sort(sv)-ex))<2e-10,(b,h)
    HS=np.linalg.norm(A,'fro')**2
    N=len(V)
    want=b/(b-1)*N-(h+1)/(b-1)
    assert abs(HS-want)<1e-8,(b,h,HS,want)
    print('PASS',b,h,N,'norm',max(sv),'HS^2',HS)

for b in (2,3,4):
 w=(b-1)**2
 qsum=0
 for L in range(1,110):
    s=[1/(2*math.sin((2*j-1)*math.pi/(4*L+2))) for j in range(1,L+1)]
    qsum+=w/b**(L+1)*sum(x*x for x in s)
 assert abs(qsum - b/(b-1))<1e-11,(b,qsum)
 print('LIMIT HS PASSED',b,qsum)
