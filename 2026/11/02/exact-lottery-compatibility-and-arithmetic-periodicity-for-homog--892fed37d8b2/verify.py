"""Exact finite checks for WEFX lotteries in homogeneous chore allocation.

Only Python's standard library is needed. All comparisons use Fraction.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, gcd


def compositions(total, n, minimum=0):
    if n == 1:
        if total >= minimum:
            yield (total,)
        return
    for k in range(minimum, total - minimum*(n-1) + 1):
        for rest in compositions(total - k, n-1, minimum):
            yield (k,) + rest


def wefx(x, w):
    # Unit-cost chores: WEF1 and WEFX coincide.
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] and Q(x[i]-1, 1)/w[i] > Q(x[j], 1)/w[j]:
                return False
    return True


def priority_feasible(m, w):
    n = len(w)
    if m < n:
        return set(compositions(m,n,0)).intersection(
            {x for x in compositions(m,n,0) if max(x) <= 1})
    if m == n:
        return {(1,)*n}
    L = m - n
    scores = sorted((Q(k,1)/w[i], i, k)
                    for i in range(n) for k in range(1,L+1))
    alpha = scores[L-1][0]
    below = [sum(sc < alpha and j == i for sc,j,k in scores)
             for i in range(n)]
    ties = [i for i in range(n) if any(sc==alpha and j==i for sc,j,k in scores)]
    need = L - sum(below)
    result = set()
    for chosen in combinations(ties, need):
        result.add(tuple(1+below[i]+int(i in chosen) for i in range(n)))
    return result


def polytope_test(m,w):
    """Priority-score hypersimplex criterion (no solver)."""
    n=len(w)
    if m<n:
        return all(m*z <= 1 for z in w)
    if m==n:
        return all(n*z == 1 for z in w)
    L=m-n
    scores=sorted((Q(k,1)/w[i],i) for i in range(n) for k in range(1,L+1))
    alpha=scores[L-1][0]
    below=[sum(sc<alpha and j==i for sc,j in scores) for i in range(n)]
    tied={i for sc,i in scores if sc==alpha}
    return all((1+below[i] <= m*w[i] <= 2+below[i])
               if i in tied else m*w[i]==1+below[i] for i in range(n))


def solve_linear_overdetermined(a,b):
    """Solve n equations in k variables exactly if independent, else None."""
    mat=[list(row)+[val] for row,val in zip(a,b)]
    nr=len(a); nc=len(a[0]); piv=[]; r=0
    for c in range(nc):
        pivot=next((j for j in range(r,nr) if mat[j][c]),None)
        if pivot is None:
            continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        fac=mat[r][c]
        mat[r]=[val/fac for val in mat[r]]
        for j in range(nr):
            if j!=r and mat[j][c]:
                scale=mat[j][c]
                mat[j]=[v-scale*u for v,u in zip(mat[j],mat[r])]
        piv.append(c); r+=1
    if any(not any(row[:nc]) and row[nc] for row in mat):
        return None
    if len(piv)<nc:
        return None
    x=[Q(0)]*nc
    for j,c in enumerate(piv):
        x[c]=mat[j][nc]
    return x if all(z>=0 for z in x) else None


def exhaustive_lottery(m,w,options):
    """Independent barycentric feasibility over all WEFX count vectors."""
    n=len(w); target=[m*wi for wi in w]
    for k in range(1,min(n,len(options))+1):
        for chosen in combinations(sorted(options),k):
            a=[[Q(x[i]) for x in chosen] for i in range(n)]
            if solve_linear_overdetermined(a,target) is not None:
                return True
    return False


def run():
    nprofile=0; mprofile=0; vecs=0; poly=0; periods=0; modular=0
    for n in (2,3,4):
        for b in range(n,9):
            for aa in compositions(b,n,1):
                w=tuple(Q(a,b) for a in aa)
                nprofile+=1
                for m in range(1,n+5):
                    mprofile+=1
                    brute={x for x in compositions(m,n,0) if wefx(x,w)}
                    vecs+=comb(m+n-1,n-1)
                    pred=priority_feasible(m,w)
                    assert brute==pred,('priority',n,b,aa,m,brute,pred)
                    if n<=3:
                        btruth=exhaustive_lottery(m,w,brute)
                        formula=polytope_test(m,w)
                        assert btruth==formula,('lottery',n,b,aa,m,btruth,formula)
                        poly+=1
                    if m>=n:
                        later=priority_feasible(m+b,w)
                        translated={tuple(x[i]+aa[i] for i in range(n)) for x in brute}
                        assert later==translated,('period',n,b,aa,m,brute,later)
                        assert polytope_test(m,w)==polytope_test(m+b,w)
                        periods+=1
    for b in range(2,15):
        for a in range(1,b):
            if gcd(a,b)!=1: continue
            w=(Q(a,b),Q(b-a,b))
            for m in range(1,30):
                target=polytope_test(m,w)
                assert target == (m%b in (0,1)),('modular',a,b,m)
                modular+=1
    print('VERIFY_OK rational_weight_profiles=',nprofile,
          'population_size_profiles=',mprofile,
          'integer_occupancy_vectors=',vecs,
          'independent_exact_lottery_tests=',poly,
          'periodicity_tests=',periods,
          'two_agent_modular_tests=',modular,sep='')


if __name__=='__main__':
    run()
