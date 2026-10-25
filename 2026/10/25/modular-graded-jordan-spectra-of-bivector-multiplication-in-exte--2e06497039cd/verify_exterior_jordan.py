#!/usr/bin/env python3
"""Recompute modular Jordan spectra of bivector multiplication in exterior algebras.

No external dependencies. Exact arithmetic in prime fields. This verifies finite
cases; the arbitrary-size theorem uses the cited integral inclusion-matrix form.
"""
from math import comb
from itertools import combinations, product


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=1;den=1
    for j in range(k):
        num*=q**(n-j)-1
        den*=q**(j+1)-1
    return num//den


def alt_count(n,r,q):
    a=q**(r*(r-1))
    for j in range(1,r+1):a*=q**(2*j-1)-1
    return gaussian(n,2*r,q)*a


def incl_rank(m,j,k,p):
    if k>=p or j+k>m:return 0
    r=min(j,m-j-k)
    return sum((comb(m,i)-(comb(m,i-1) if i else 0))
               for i in range(r+1) if comb(r+k-i,r-i)%p)


def predicted_ranks(n,r,p):
    ans=[]
    for k in range(p+1):
        a=0
        for m in range(r+1):
            a+=comb(r,m)*2**(r-m)*sum(incl_rank(m,j,k,p) for j in range(m-k+1))
        ans.append(a*2**(n-2*r))
    return ans


def jordan(ranks):
    return {i:ranks[i-1]-2*ranks[i]+(ranks[i+1] if i+1<len(ranks) else 0)
            for i in range(1,len(ranks))
            if ranks[i-1]-2*ranks[i]+(ranks[i+1] if i+1<len(ranks) else 0)}


def rank_vectors(vectors,p):
    piv={}
    for vec in vectors:
        a=dict((j,x%p) for j,x in vec.items() if x%p)
        while a:
            j=min(a)
            if j not in piv:
                z=pow(a[j],-1,p)
                piv[j]={e:v*z%p for e,v in a.items()}
                break
            mul=a[j]
            for e,v in piv[j].items():
                nv=(a.get(e,0)-mul*v)%p
                if nv:a[e]=nv
                elif e in a:del a[e]
    return len(piv)


def direct_ranks(n,r,p):
    Qpairs=[3<<(2*i) for i in range(r)]
    vectors={a:{a:1} for a in range(1<<n)}
    ranks=[2**n]
    for k in range(1,p+1):
        new={}
        for a,old in vectors.items():
            w={}
            for b,v in old.items():
                for e in Qpairs:
                    if not b&e:
                        c=b|e
                        w[c]=(w.get(c,0)+v)%p
            new[a]={c:v for c,v in w.items() if v}
        vectors=new
        ranks.append(rank_vectors(vectors.values(),p))
    return ranks



def graded_prediction(n,r,p):
    # R[k][d] = rank(Q^k: Lambda^d -> Lambda^(d+2k)).
    R=[[0]*(n+1) for _ in range(p+2)]
    for k in range(p):
        for m in range(r+1):
            for outside in range(n-2*r+1):
                mult=comb(r,m)*2**(r-m)*comb(n-2*r,outside)
                for j in range(m-k+1):
                    d=r-m+outside+2*j
                    R[k][d]+=mult*incl_rank(m,j,k,p)
    B={}
    for ell in range(1,p+1):
        for d in range(n+1):
            b=R[ell-1][d]-R[ell][d]
            if d>=2:b-=R[ell][d-2]
            if d>=2:b+=R[ell+1][d-2]
            assert b>=0,(n,r,p,ell,d,b)
            if b:B[(d,ell)]=b
    return R,B


def graded_direct(n,r,p):
    basis={d:[a for a in range(1<<n) if a.bit_count()==d] for d in range(n+1)}
    pairs=[3<<(2*i) for i in range(r)]
    powers={a:{a:1} for a in range(1<<n)}
    R=[[0]*(n+1) for _ in range(p+1)]
    for k in range(p+1):
        for d in range(n+1):
            R[k][d]=rank_vectors([powers[a] for a in basis[d]],p)
        nxt={}
        for a,vec in powers.items():
            out={}
            for b,c in vec.items():
                for pair in pairs:
                    if not b&pair:
                        target=b|pair
                        out[target]=(out.get(target,0)+c)%p
            nxt[a]={b:c for b,c in out.items() if c}
        powers=nxt
    return R

def rank_mat(a,p):
    z=[row[:] for row in a];m=len(z);n=len(z[0]) if m else 0;j=0
    for c in range(n):
        h=next((i for i in range(j,m) if z[i][c]%p),None)
        if h is None:continue
        z[h],z[j]=z[j],z[h]
        inv=pow(z[j][c]%p,-1,p)
        for t in range(c,n):z[j][t]=z[j][t]*inv%p
        for i in range(j+1,m):
            if z[i][c]:
                t=z[i][c]
                for b in range(c,n):z[i][b]=(z[i][b]-t*z[j][b])%p
        j+=1
        if j==m:break
    return j


def distribution_4(p):
    got=[0,0,0]
    for coeff in product(range(p),repeat=6):
        a=[[0]*4 for _ in range(4)]
        for v,(i,j) in zip(coeff,combinations(range(4),2)):
            a[i][j]=v;a[j][i]=-v%p
        got[rank_mat(a,p)//2]+=1
    want=[alt_count(4,r,p) for r in range(3)]
    assert got==want,(p,got,want)
    assert sum(got)==p**6
    return got


def run():
    count=0
    for p in (3,5,7):
        for n in range(2,9):
            for r in range(0,n//2+1):
                prediction=predicted_ranks(n,r,p)
                actual=direct_ranks(n,r,p)
                assert prediction==actual,(p,n,r,prediction,actual)
                j=jordan(prediction)
                assert sum(length*num for length,num in j.items())==2**n
                assert all(num>=0 for num in j.values())
                assert all(length<=p for length in j)
                predicted_grades,strings=graded_prediction(n,r,p)
                actual_grades=graded_direct(n,r,p)
                assert predicted_grades[:p+1]==actual_grades[:p+1],(n,r,p,predicted_grades,actual_grades)
                assert [sum(row) for row in predicted_grades[:p+1]]==prediction
                assert sum(ell*number for (d,ell),number in strings.items())==2**n
                count+=1
    for p in (3,5):
        print('alternating rank frequencies n=4, p=%d:'%p,distribution_4(p))
    for p in (3,5,7):
        print('n=8, r=4, characteristic %s ranks '%p,predicted_ranks(8,4,p),'Jordan',jordan(predicted_ranks(8,4,p)))
    print('VERIFY_OK_EXTERIOR_QUADRATIC_JORDAN',count,'matrix-power cases')

if __name__=='__main__':run()
