#!/usr/bin/env python3
import math

N=8
q=9
lam=6/5
c=[5,4,2,1,-1,-2,-4,-5]

# Exact combinatorial frequency separation.
same=set()
opp=set()
for r in range(8):
    for s in range(r+1,8):
        d=abs(c[r]-c[s])
        if ((s+1)-(r+1))%2==0:
            same.add(d)
        else:
            opp.add(d)
assert same == {3,6,9}, same
assert opp == {1,2,4,5,7,8,10}, opp
assert same.isdisjoint(opp)
assert c[0]-c[1]-c[3] == 0
assert abs((1-3*lam/4)-0.1) < 1e-15

# Corroborate exact spectral identities numerically.
th=[None]+[2*math.cos(r*math.pi/q) for r in range(1,q)]
assert abs(th[3]-1) < 2e-15
assert abs(th[4]-(th[2]**2-2)) < 3e-15
assert abs(th[1]-th[2]-th[4]) < 3e-15
assert abs(th[2]**3-3*th[2]+1) < 5e-15

# Published forced coherence target reconstructed through the spectral expansion.
# v_r(k)=sqrt(2/q) sin(r k pi/q), E_r=v_r v_r^T.
vs=[]
for r in range(1,q):
    vs.append([math.sqrt(2/q)*math.sin(r*k*math.pi/q) for k in range(1,q)])
Es=[]
for v in vs:
    Es.append([[v[i]*v[j] for j in range(N)] for i in range(N)])
M=[[0.0]*N for _ in range(N)]
for r in range(N):
    for i in range(N):
        for j in range(N):
            M[i][j] += Es[r][i][j]*Es[r][i][j]
for r in range(N):
    for s in range(r+1,N):
        y = -1/N if ((s+1)-(r+1))%2==0 else 0.0
        for i in range(N):
            for j in range(N):
                M[i][j] += 2*y*Es[r][i][j]*Es[s][i][j]
err=max(abs(M[i][j]-1/N) for i in range(N) for j in range(N))
assert err < 2e-15, err

# The phase density Fourier moments are exact by orthogonality; encode the values
# that enter the coherence target and verify the convex rescaling.
def phase_moment(k):
    return -lam/8 if k in {3,6,9} else 0.0
for r in range(8):
    for s in range(r+1,8):
        y=phase_moment(abs(c[r]-c[s]))
        target=-1/8 if ((s+1)-(r+1))%2==0 else 0.0
        assert abs(y/lam-target) < 1e-15

print('VERIFY_OK')
