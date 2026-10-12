#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

def direct_stats(n, mask, edges, eidx, triples):
    deg=[0]*n
    for j,(u,v) in enumerate(edges):
        if (mask>>j)&1:
            deg[u]+=1
        else:
            deg[v]+=1
    cyc=0
    for a,b,c in triples:
        wins=[0,0,0]
        vs=(a,b,c)
        for i,j in ((0,1),(0,2),(1,2)):
            u,v=vs[i],vs[j]
            idx=eidx[(u,v)] if u<v else eidx[(v,u)]
            bit=(mask>>idx)&1
            u_wins = bit==1 if u<v else bit==0
            if u_wins: wins[i]+=1
            else: wins[j]+=1
        if wins==[1,1,1]: cyc+=1
    return deg,cyc

def run():
    tournaments=0
    conditional_checks=0
    covariance_checks=0
    variance_checks=0
    sign_checks=0
    master_checks=0
    for n in range(3,7):
        q=n-1
        edges=list(combinations(range(n),2))
        eidx={e:i for i,e in enumerate(edges)}
        triples=list(combinations(range(n),3))
        M=1<<len(edges)
        sC=sC2=0
        sN=[0]*n; sN2=[0]*n; sNC=[0]*n
        cond=[[0,0] for _ in range(n)]
        phi_sums={name:[0,0] for name in ('linear','square','central')}
        for mask in range(M):
            deg,C=direct_stats(n,mask,edges,eidx,triples)
            tournaments+=1; sC+=C; sC2+=C*C
            cond[deg[0]][0]+=1; cond[deg[0]][1]+=C
            for k in range(n):
                Nk=sum(d==k for d in deg)
                sN[k]+=Nk; sN2[k]+=Nk*Nk; sNC[k]+=Nk*C
            funcs={
                'linear':sum(deg),
                'square':sum(d*d for d in deg),
                'central':sum(int((2*d-q)**2<=q) for d in deg),
            }
            for name,val in funcs.items():
                phi_sums[name][0]+=val; phi_sums[name][1]+=val*C
        EC=Fraction(sC,M); varC=Fraction(sC2,M)-EC*EC
        assert EC==Fraction(comb(n,3),4)
        assert varC==Fraction(n*q*(q-1),32)
        variance_checks+=1
        for k in range(n):
            p=Fraction(comb(q,k),2**q); delta=2*k-q
            EN=Fraction(sN[k],M)
            cov=Fraction(sNC[k],M)-EN*EC
            target=Fraction(n,8)*p*(q-delta*delta)
            assert EN==n*p and cov==target
            covariance_checks+=1
            ce=Fraction(cond[k][1],cond[k][0])
            assert ce==EC+Fraction(q-delta*delta,8)
            conditional_checks+=1
            varN=Fraction(sN2[k],M)-EN*EN
            targetv=n*p*(1-p*(1+Fraction(delta*delta,q)))
            assert varN==targetv
            variance_checks+=1
            assert (cov>0)==(delta*delta<q)
            assert (cov==0)==(delta*delta==q)
            assert (cov<0)==(delta*delta>q)
            sign_checks+=1
            # squared correlation identity without floating point
            if cov:
                lhs=cov*cov
                rhs=varN*varC*Fraction((q-delta*delta)**2*p, 2*q*(q-1)*(1-p*(1+Fraction(delta*delta,q))))
                assert lhs==rhs
        # master identity for explicit functions
        for name in ('linear','square','central'):
            ES=Fraction(phi_sums[name][0],M)
            ESC=Fraction(phi_sums[name][1],M)
            lhs=ESC-ES*EC
            def phi(k):
                if name=='linear': return k
                if name=='square': return k*k
                return int((2*k-q)**2<=q)
            Ephi=sum(Fraction(comb(q,k),2**q)*phi(k) for k in range(n))
            Ez2=sum(Fraction(comb(q,k),2**q)*(2*k-q)**2 for k in range(n))
            Ephiz2=sum(Fraction(comb(q,k),2**q)*phi(k)*(2*k-q)**2 for k in range(n))
            rhs=-Fraction(n,8)*(Ephiz2-Ephi*Ez2)
            assert lhs==rhs
            master_checks+=1
    print('VERIFY_OK '
          f'tournaments={tournaments} '
          f'conditional_checks={conditional_checks} '
          f'covariance_checks={covariance_checks} '
          f'variance_checks={variance_checks} '
          f'sign_checks={sign_checks} '
          f'master_checks={master_checks}')

if __name__=='__main__': run()
