"""Independent small-dimensional checks for binary invertible-matrix symmetry law."""
import itertools
from math import factorial

def permute_mask_rows(rows, p):
    n=len(rows)
    out=[]
    for i in range(n):
        old=rows[p[i]]
        out.append(sum(((old >> p[j]) & 1)<<j for j in range(n)))
    return tuple(out)

def invertible(rows):
    n=len(rows)
    a=list(rows)
    rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,n) if a[i] >> j & 1), None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        for i in range(n):
            if i!=rank and (a[i]>>j & 1):a[i]^=a[rank]
        rank+=1
    return rank==n

def gl_formula(n):
    x=1
    for i in range(n):x*=2**n-2**i
    return x

def run():
    for n in range(2,5):
        perms=list(itertools.permutations(range(n)))
        ident=tuple(range(n))
        tau=list(range(n)); tau[0],tau[1]=tau[1],tau[0];tau=tuple(tau)
        count=0; nontriv=0; tau_hits=0; aut_sum=0
        for rows in itertools.product(range(1<<n), repeat=n):
            if not invertible(rows):continue
            count+=1
            fixed=[p for p in perms if permute_mask_rows(rows,p)==rows]
            aut_sum+=len(fixed)
            nontriv+=len(fixed)>1
            tau_hits+=tau in fixed
        assert count==gl_formula(n),(n,count,gl_formula(n))
        predicted=(1<<(2*n-3))*gl_formula(n-2)
        assert tau_hits==predicted,(n,tau_hits,predicted)
        assert aut_sum%factorial(n)==0
        print(f'n={n} |GL|={count} nontrivial={nontriv} tau_centralizer={tau_hits} orbits={aut_sum//factorial(n)}')
    print('VERIFY_OK')
if __name__=='__main__':run()
