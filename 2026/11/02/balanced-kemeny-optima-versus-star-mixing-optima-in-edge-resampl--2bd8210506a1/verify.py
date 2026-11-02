#!/usr/bin/env python3
"""Exact finite-state checks for edge-resampled walks on complete bipartite graphs.

All checks use rational arithmetic or elementary exact integer comparisons.
"""
from fractions import Fraction as F


def matrix(a,b,p):
    n=a+b
    r=1-p
    qa=1-r**a
    qb=1-r**b
    M=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        if i<a:
            M[i][i]=1-qb
            for j in range(a,n): M[i][j]=qb/b
        else:
            M[i][i]=1-qa
            for j in range(a): M[i][j]=qa/a
    return M

def solve(A,v):
    N=len(v)
    M=[row[:] + [v[i]] for i,row in enumerate(A)]
    for j in range(N):
        z=next(k for k in range(j,N) if M[k][j])
        M[z],M[j]=M[j],M[z]
        pivot=M[j][j]
        M[j]=[x/pivot for x in M[j]]
        for i in range(N):
            if i==j: continue
            z=M[i][j]
            if z:
                M[i]=[M[i][k]-z*M[j][k] for k in range(N+1)]
    return [row[-1] for row in M]

def kemeny_from_hitting(M,pi):
    n=len(M)
    C=[]
    for target in range(n):
        keep=[i for i in range(n) if i!=target]
        H=solve([[int(i==j)-M[i][j] for j in keep] for i in keep],[F(1)]*(n-1))
        full=[F(0)]*n
        for i,val in zip(keep,H):full[i]=val
        C.append(full)
    return [sum(pi[j]*C[j][i] for j in range(n)) for i in range(n)]

def main():
    count=0
    for a in range(1,6):
        for b in range(1,6):
            if a+b<3: continue
            for p in [F(1,5),F(2,5),F(1,2),F(3,4),F(7,8)]:
                r=1-p;qa=1-r**a;qb=1-r**b
                M=matrix(a,b,p)
                q=qa+qb
                pi=[qa/(q*a)]*a+[qb/(q*b)]*b
                assert all(sum(x)==1 for x in M)
                assert all(sum(pi[i]*M[i][j] for i in range(a+b))==pi[j] for j in range(a+b))
                count+=a+b+1
                # Alternative exact trace-of-first-hit verification.
                K=kemeny_from_hitting(M,pi)
                expect=F(a-1)/qb+F(b-1)/qa+1/q
                assert all(z==expect for z in K),(a,b,p,K,expect)
                count+=a+b
                # Eigenvectors of class contrasts and aggregate mass.
                agg=r**a+r**b-1
                for i in range(a-1):
                    v=[0]*(a+b);v[i]=1;v[i+1]=-1
                    assert all(sum(M[j][k]*v[k] for k in range(a+b))==r**b*v[j] for j in range(a+b))
                    count+=1
                for i in range(a,a+b-1):
                    v=[0]*(a+b);v[i]=1;v[i+1]=-1
                    assert all(sum(M[j][k]*v[k] for k in range(a+b))==r**a*v[j] for j in range(a+b))
                    count+=1
                vec=[F(qb)]*a+[-F(qa)]*b
                assert all(sum(M[j][k]*vec[k] for k in range(a+b))==agg*vec[j] for j in range(a+b))
                count+=1
                # Exact two-step matrix powers against closed-class-contrast formula.
                for start in [0,a]:
                    dist=[F(int(i==start)) for i in range(a+b)]
                    for t in range(5):
                        A_mass=qa/q+ (qb/q if start<a else -qa/q)*agg**t
                        correction=((r**b if start<a else r**a)**t)
                        rhs=[]
                        for j in range(a+b):
                            baseline=(A_mass/a if j<a else (1-A_mass)/b)
                            within=(correction*(F(int(j==start))- (F(1,a) if start<a and j<a else F(1,b) if start>=a and j>=a else F(0))))
                            rhs.append(baseline+within)
                        assert dist==rhs,(a,b,p,start,t,dist,rhs)
                        count+=a+b
                        dist=[sum(dist[i]*M[i][j] for i in range(a+b)) for j in range(a+b)]
    # For each n and p verify balancing of K and exact integer rho minimizer against monotone branches.
    for n in range(4,31):
        for p in [F(1,17),F(1,5),F(1,2),F(9,10)]:
            r=1-p
            def K(a):
                b=n-a;qa=1-r**a;qb=1-r**b
                return F(a-1)/qb+F(b-1)/qa+1/(qa+qb)
            def rho(a):
                b=n-a
                return max(r**a,1-r**a-r**b)
            Ks=[K(a) for a in range(1,n//2+1)]
            assert Ks==sorted(Ks,reverse=True)
            assert all(Ks[i]>Ks[i+1] for i in range(len(Ks)-1))
            rs=[rho(a) for a in range(1,n//2+1)]
            Fs=[2*r**a+r**(n-a)-1 for a in range(1,n//2+1)]
            assert Fs==sorted(Fs,reverse=True)
            if Fs[-1]>=0: assert rs[-1]==min(rs)
            elif Fs[0]<=0: assert rs[0]==min(rs)
            else:
                cross=next(i for i,x in enumerate(Fs) if x<=0)
                assert min(rs)==min(rs[cross-1:cross+1])
            count+=len(Ks)*3
    # Explicit opposite behavior at half availability.
    for m in range(2,31):
        n=2*m
        r=F(1,2)
        assert max(r**m,1-2*r**m)==1-2*r**m if m>=3 else F(1,2)
        assert max(r,1-r-r**(n-1))==r
        count+=2
    print('PASS',count,'checked exact-rational comparison units')
if __name__=='__main__':main()
