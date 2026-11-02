"""Independent finite-field checks for rank-one Rota--Baxter operators on a six-dimensional 2-step algebra.
Run: python checker.py. Requires numpy. Does not use theorem's operator-count formula to test identity.
"""
from itertools import product
import numpy as np

def forms(p, alpha=1, beta=0):
    h=pow(2,-1,p)
    B1=np.zeros((4,4),dtype=np.int64)
    B2=np.zeros((4,4),dtype=np.int64)
    B1[1,1]=1
    B1[0,3]=B1[3,0]=-h
    B2[2,2]=1
    B2[1,3]=B2[3,1]=-h
    B2[0,1]=B2[1,0]=-alpha*h
    B2[0,0]=-beta
    return B1%p,B2%p

def products(a,p,B1,B2):
    # P[j,k] is the kth coordinate of a * e_j; basis includes W in coordinates 4 and 5.
    P=np.zeros((6,6),dtype=np.int64)
    P[:4,4]=a[:4]@B1 % p
    P[:4,5]=a[:4]@B2 % p
    return P

def projective_points(p,alpha=1,beta=0):
    B1,B2=forms(p,alpha,beta)
    pts=[]
    for v0 in product(range(p),repeat=4):
        v=np.array(v0,dtype=np.int64)
        if not np.any(v):continue
        if int(v@B1@v)%p or int(v@B2@v)%p:continue
        if any(v):
            i=next(j for j,x in enumerate(v) if x)
            v=v*pow(int(v[i]),-1,p)%p
            t=tuple(map(int,v))
            if t not in pts:pts.append(t)
    for t in pts:
        v=np.array(t,dtype=np.int64)
        G=np.stack((2*B1@v,2*B2@v))%p
        assert any((G[0,i]*G[1,j]-G[0,j]*G[1,i])%p for i in range(4) for j in range(i+1,4))
    return len(pts)

def ellipse_count(p,alpha=1,beta=0):
    # y^2=x^3+alpha*x+beta and its point at infinity
    return 1+sum(1 for x in range(p) for y in range(p) if (y*y-x*x*x-alpha*x-beta)%p==0)

def formula(p, countC):
    return (p+1)*(p**6-1)+p*p*(p**4-1)*countC

def exhaustive(p=3):
    B1,B2=forms(p)
    F=np.asarray(list(product(range(p),repeat=6)),dtype=np.int64)
    F=F[np.any(F,axis=1)]
    total_repr=0; central_repr=0; noncentral_repr=0
    for a0 in product(range(p),repeat=6):
        a=np.asarray(a0,dtype=np.int64)
        if not np.any(a):continue
        P=products(a,p,B1,B2)
        aa=(a@P)%p
        t=(F@P.T)%p
        lhs=(F[:,:,None]*F[:,None,:])%p
        rhs=(F[:,:,None]*t[:,None,:]+t[:,:,None]*F[:,None,:])%p
        ok=np.ones(len(F),dtype=bool)
        for k in range(6):
            ok &= np.all((lhs*aa[k]-rhs*a[k])%p==0,axis=(1,2))
        c=int(ok.sum())
        total_repr+=c
        if np.any(a[:4]):noncentral_repr+=c
        else:central_repr+=c
    assert total_repr%(p-1)==0
    return total_repr//(p-1),central_repr//(p-1),noncentral_repr//(p-1)

def random_checks(p,alpha, beta=0,seed=826,tests=2000):
    rng=np.random.default_rng(seed+p+alpha)
    B1,B2=forms(p,alpha,beta)
    n=0
    while n<tests:
        a=rng.integers(0,p,size=6,dtype=np.int64)
        f=rng.integers(0,p,size=6,dtype=np.int64)
        if not np.any(a) or not np.any(f):continue
        P=products(a,p,B1,B2)
        aa=a@P%p
        t=f@P.T%p
        # Check the original Rota--Baxter identity on 36 ordered pairs of basis vectors.
        direct=all(np.array_equal((f[i]*f[j]*aa)%p,((f[i]*t[j]+f[j]*t[i])*a)%p) for i in range(6) for j in range(6))
        v=a[:4]
        predicted=(not np.any(v)) or (int(v@B1@v)%p==0 and int(v@B2@v)%p==0 and all(t%p==0))
        assert direct==predicted,(p,alpha,a,f,direct,predicted)
        n+=1
    return n


def extension9_check():
    # F_9=F_3[t]/(t^2+1); -1 is nonsquare in F_3.
    E=[(a,b) for a in range(3) for b in range(3)]
    def add(x,y):return ((x[0]+y[0])%3,(x[1]+y[1])%3)
    def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
    count=1+sum(1 for x in E for y in E if mul(y,y)==add(mul(mul(x,x),x),x))
    assert count==16,(count,'genus-one recurrence for trace 0 over F_3')
    print(f'EXTENSION F_9: curve={count} N_RB_rank1={formula(9,count)}')
    return count

def main():
    for p,alphas in [(3,[1,2]),(5,[1,2,4]),(7,[1,2]),(11,[1])]:
        for alpha in alphas:
            c=projective_points(p,alpha)
            E=ellipse_count(p,alpha)
            assert c==E,(p,alpha,c,E)
            nr=formula(p,c)
            print(f'POINTS p={p} alpha={alpha}: curve={c} N_RB_rank1={nr}')
            assert random_checks(p,alpha,tests=400)==400
    extension9_check()
    total,central,noncentral=exhaustive(3)
    c=ellipse_count(3)
    assert (total,central,noncentral)==(formula(3,c), (3+1)*(3**6-1), 3**2*(3**4-1)*c)
    print(f'EXHAUSTIVE q=3: total={total},central={central},noncentral={noncentral}, all (3^6-1)^2=529984 nonzero tensor representations checked')
    print('ELLIPTIC_ROTA_BAXTER_RANK_ONE_OK')
if __name__=='__main__':main()
