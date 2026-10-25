"""Independent small-field checks for the radical centralizer and commuting-pair formulas.
Usage: python verify.py
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def nullity_linear(m, r, p, aa):
    # Assemble commutator equations in each two-arrow basis path.
    rows=[]
    for i in range(m-1):
        for j in range(r):
            for k in range(r):
                row=[0]*(m*r)
                row[(i+1)*r+k] = (row[(i+1)*r+k] + aa[i][j])%p
                row[i*r+j] = (row[i*r+j] - aa[i+1][k])%p
                rows.append(row)
    rank=0
    for col in range(m*r):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][col]%p),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        rows[rank]=[(v*inv)%p for v in rows[rank]]
        for j in range(rank+1,len(rows)):
            if rows[j][col]:
                factor=rows[j][col]
                rows[j]=[(u-factor*v)%p for u,v in zip(rows[j],rows[rank])]
        rank+=1
    return m*r-rank


def combinatorial_dim(mask, r):
    m=len(mask)
    free_zero=sum(not b and (i==0 or not mask[i-1]) and (i==m-1 or not mask[i+1]) for i,b in enumerate(mask))
    one_runs=[]
    i=0
    while i<m:
        if not mask[i]:
            i+=1
            continue
        j=i
        while j<m and mask[j]:j+=1
        one_runs.append(j-i)
        i=j
    return r*(free_zero+sum(k==1 for k in one_runs))+sum(k>=2 for k in one_runs)


def is_commuting(aa,bb,r,p):
    for i in range(len(aa)-1):
        for j in range(r):
            for k in range(r):
                if (aa[i][j]*bb[i+1][k]-bb[i][j]*aa[i+1][k])%p:
                    return False
    return True


def word_counts(m,q,r):
    A=q**r-1
    out=Counter()
    for mask in product([False,True],repeat=m):
        out[combinatorial_dim(mask,r)]+=A**sum(mask)
    return out


def rational_coeffs(m_max,q,r):
    A=q**r-1;B=A*(q**r-q)
    a=[1]
    # (1-(A+1)z-(qA+B)z^2+ABz^3) F(z) = 1+(qA+B)z-ABz^2
    for m in range(1,m_max+1):
        val=(A+1)*a[m-1]
        if m>=2: val+=(q*A+B)*a[m-2]
        if m>=3: val-=A*B*a[m-3]
        if m==1: val+=(q*A+B)
        if m==2: val-=A*B
        a.append(val)
    return a


def all_vectors(m,r,p):
    arr=list(product(range(p),repeat=r))
    return product(arr,repeat=m)


def main():
    checks=0
    for q,r,mmax in [(2,1,5),(2,2,4),(2,3,3),(3,1,5),(3,2,3),(5,1,4)]:
        expected=rational_coeffs(mmax,q,r)
        for m in range(1,mmax+1):
            pred=word_counts(m,q,r)
            assert sum(v*q**d for d,v in pred.items())==expected[m],(q,r,m,expected[m],pred)
            brute_spectrum=Counter()
            for aa in all_vectors(m,r,q):
                dim=nullity_linear(m,r,q,aa)
                mask=tuple(any(v!=0 for v in a) for a in aa)
                assert dim==combinatorial_dim(mask,r),(q,r,m,aa,dim,mask)
                brute_spectrum[dim]+=1
                checks+=1
            assert brute_spectrum==pred,(q,r,m,brute_spectrum,pred)
            if q**(2*r*m)<=5000:
                brute=0
                vv=list(all_vectors(m,r,q))
                for aa in vv:
                    for bb in vv:
                        if is_commuting(aa,bb,r,q):brute+=1
                assert brute==expected[m], (q,r,m,brute,expected[m])
                checks+=1
    for q,r in [(2,1),(2,2),(3,1),(3,2),(5,2)]:
        for m in range(1,13):
            assert sum(c*q**d for d,c in word_counts(m,q,r).items())==rational_coeffs(m,q,r)[m]
            checks+=1
    print('VERIFY_OK_PARALLEL_ARROW_COMMUTANT_CENSUS', checks)
    print('Selected coefficients q=2 r=2 m=1..8:',rational_coeffs(8,2,2)[1:])
    print('Spectrum q=2 r=2 m=4:', dict(sorted(word_counts(4,2,2).items())))

if __name__=='__main__':main()
