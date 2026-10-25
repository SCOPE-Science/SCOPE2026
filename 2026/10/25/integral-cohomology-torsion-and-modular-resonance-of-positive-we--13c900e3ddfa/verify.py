"""Independent exterior Chevalley-Eilenberg differential checks for integral weighted Lie rings."""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def ce_matrix(weights,k):
    # basis indices 0=h, 1..n=v_i, [h,v_i]=weights[i-1]*v_i
    n=len(weights)+1
    src=list(combinations(range(n),k)); dst=list(combinations(range(n),k+1))
    lookup={s:i for i,s in enumerate(dst)}
    m=Matrix.zeros(len(dst),len(src))
    # CE on a k-form f evaluated on sorted tuple x_0,..,x_k:
    # sum_{i<j} (-1)^(i+j) f([x_i,x_j],rest) with zero-based positions
    for r,tup in enumerate(dst):
        for i in range(k+1):
            for j in range(i+1,k+1):
                a,b=tup[i],tup[j]
                if a!=0 or b==0: continue
                bracket_coeff=weights[b-1]
                seq=(b,)+tuple(tup[z] for z in range(k+1) if z!=i and z!=j)
                if len(set(seq))<len(seq):continue
                sgn=(-1)**(i+j)
                inv=sum(seq[a]>seq[b] for a in range(k) for b in range(a+1,k))
                seq=tuple(sorted(seq))
                m[r,src.index(seq)]+=sgn*(-1)**inv*bracket_coeff
    return m

def rank_mod(mat,p):
    a=[[int(mat[i,j])%p for j in range(mat.cols)] for i in range(mat.rows)]
    rank=0
    for col in range(mat.cols):
        piv=next((r for r in range(rank,mat.rows) if a[r][col]),None)
        if piv is None:continue
        a[rank],a[piv]=a[piv],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[v*inv%p for v in a[rank]]
        for r in range(rank+1,mat.rows):
            c=a[r][col]
            if c:a[r]=[(a[r][j]-c*a[rank][j])%p for j in range(mat.cols)]
        rank+=1
        if rank==mat.rows:break
    return rank

def check(weights):
    n=len(weights); mats=[ce_matrix(weights,k) for k in range(n+2)]
    assert all(mats[k+1]*mats[k]==Matrix.zeros(mats[k+1].rows,mats[k].cols) for k in range(n+1))
    for k in range(1,n+2):
        d=mats[k-1]
        raw=[sum(weights[j] for j in s) for s in combinations(range(n),k-1)]
        expected=smith_normal_form(Matrix.diag(*raw),domain=ZZ) if raw else Matrix.zeros(0,0)
        got=smith_normal_form(d,domain=ZZ)
        invariants=sorted(abs(int(got[i,i])) for i in range(min(got.rows,got.cols)) if got[i,i]!=0)
        exp=sorted(abs(int(expected[i,i])) for i in range(min(expected.rows,expected.cols)) if expected[i,i]!=0)
        assert invariants==exp,(weights,k,invariants,exp)
    for p in [2,3,5,7,11]:
        ranks=[rank_mod(m,p) for m in mats]
        for k in range(n+2):
            c_k=sum(sum(weights[i] for i in s)%p==0 for s in combinations(range(n),k)) if k<=n else 0
            c_prev=sum(sum(weights[i] for i in s)%p==0 for s in combinations(range(n),k-1)) if 0<=k-1<=n else 0
            actual=comb(n+1,k)-(ranks[k] if k<len(ranks) else 0)-(ranks[k-1] if k>=1 else 0)
            assert actual==c_k+c_prev,(weights,k,p,actual,c_k+c_prev)
    print('PASS',weights)

for weights in [[1],[1,2],[1,7],[2,3,4],[1,1,2,5],[1,2,3,5,8],[2,2,2,3]]:check(weights)
print('VERIFY_OK')
