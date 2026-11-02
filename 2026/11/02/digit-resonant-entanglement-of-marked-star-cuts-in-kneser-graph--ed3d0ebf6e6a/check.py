"""Exact checks for prime-dimensional Kneser graph-state marked-star cuts."""
from math import comb
from itertools import combinations,product
import numpy as np


def rank_mod_p(matrix,p):
    if not matrix: return 0
    if p==2:
        basis={};rank=0
        for row in matrix:
            x=sum(1<<i for i,b in enumerate(row) if b)
            while x:
                j=x.bit_length()-1
                if j in basis: x^=basis[j]
                else: basis[j]=x;rank+=1;break
        return rank
    M=np.array(matrix,dtype=np.int64)%p
    rank=0
    for j in range(M.shape[1]):
        candidates=np.flatnonzero(M[rank:,j])
        if len(candidates)==0:continue
        pivot=rank+int(candidates[0]);M[[rank,pivot]]=M[[pivot,rank]]
        M[rank,j:]=(M[rank,j:]*pow(int(M[rank,j]),-1,p))%p
        for i in range(rank+1,M.shape[0]):
            if M[i,j]: M[i,j:]=(M[i,j:]-M[i,j]*M[rank,j:])%p
        rank+=1
        if rank==M.shape[0]:break
    return rank


def predicted(n,k,s,p):
    assert 1<=s<n and k>=2 and n>=2*k+s-1
    m=n-s;L=m-k
    total=0
    for i in range(k):
        weights=comb(m,i)-(comb(m,i-1) if i else 0)
        if any(comb(L-i,k-j-i)%p for j in range(1,min(s,k-i)+1)):
            total+=weights
    return total


def cut(n,k,s):
    vert=list(combinations(range(n),k));marked=set(range(s))
    left=[set(v) for v in vert if set(v)&marked]
    right=[set(v) for v in vert if not set(v)&marked]
    return [[int(v.isdisjoint(w)) for w in right] for v in left]


def direct_quantum(n,k,s,p):
    # Direct, small quantum amplitudes for a concrete Kneser graph.
    assert n==5 and k==2 and p in (2,3)
    vertices=list(combinations(range(n),k));marked=set(range(s))
    left=[i for i,v in enumerate(vertices) if set(v)&marked]
    right=[i for i,v in enumerate(vertices) if not set(v)&marked]
    permutation=left+right
    edges=[(a,b) for a in range(len(permutation)) for b in range(a+1,len(permutation))
           if set(vertices[permutation[a]]).isdisjoint(vertices[permutation[b]])]
    N=len(vertices)
    digits=np.array(list(product(range(p),repeat=N)),dtype=np.int16)
    phase=np.zeros(len(digits),dtype=np.int16)
    for a,b in edges:phase=(phase+digits[:,a]*digits[:,b])%p
    amp=np.exp(2j*np.pi*phase/p)/np.sqrt(p**N)
    wave=amp.reshape(p**len(left),p**len(right))
    rho=wave.conj().T@wave if len(left)>len(right) else wave@wave.conj().T
    eigen=np.linalg.eigvalsh(rho)
    r=predicted(n,k,s,p)
    positives=eigen[eigen>1e-8]
    assert len(positives)==p**r,(n,k,s,p,len(positives),p**r)
    assert np.max(abs(positives-p**(-r)))<1e-10
    return float(np.max(abs(positives-p**(-r))))


def main():
    cases=0
    for n in range(5,13):
        for k in range(2,min(4,(n-1)//2)+1):
            for s in range(1,min(4,n-2*k+1)):
                if n<2*k+s-1:continue
                M=cut(n,k,s)
                for p in (2,3,5):
                    predicted_rank=predicted(n,k,s,p)
                    actual_rank=rank_mod_p(M,p)
                    assert actual_rank==predicted_rank,(n,k,s,p,actual_rank,predicted_rank)
                    cases+=1
    errors=[]
    for s in (1,2):
        for p in (2,3):errors.append(direct_quantum(5,2,s,p))
    bounds=0
    for k in range(2,9):
        for s in range(1,k):
            for p in (2,3,5):
                q=p
                while q<=s:q*=p
                for n in range(2*k+s-1,2*k+s+50):
                    m=n-s;imax=k-s-1
                    bound=comb(m,imax-1) if imax else 0
                    mu=comb(m,imax)-bound
                    deficit=comb(m,k-1)-predicted(n,k,s,p)
                    if (n-2*k+1)%q==0:
                        assert mu<=deficit<=mu+bound
                    else:
                        assert 0<=deficit<=bound
                    bounds+=1
    for k in range(2,15):
        n=2*k+1
        for p in (2,3,5,7):
            assert predicted(n,k,2,p)==comb(n-2,k), (n,k,p)
    print('VERIFY_OK',f'exact_cross_matrix_checks={cases}',f'direct_spectra={len(errors)}',f'sharp_resonance_checks={bounds}',f'largest_eigenvalue_error={max(errors):.3g}', 'universal_odd_graph_checks=52')
    for n,k,s in [(7,3,1),(7,3,2),(8,3,1),(8,3,2),(9,4,1),(9,4,2),(10,4,3)]:
        print(f'KG({n},{k}) marked={s} parts=({comb(n,k)-comb(n-s,k)},{comb(n-s,k)}) ranks='+str([(p,predicted(n,k,s,p)) for p in (2,3,5,7)]))

if __name__=='__main__':main()
