"""Independent finite-set checks for uniform-subset interpolation formulas."""
from itertools import combinations

def formula(s,k,r):
    q,t=divmod(s,k)
    return r*q+max(0,t-(k-r))

def main():
    total=0
    for n in range(1,8):
        subsets=range(1<<n)
        pc=[x.bit_count() for x in subsets]
        for k in range(1,n+1):
            for r in range(1,k+1):
                initial=[r if pc[s]==k else 0 for s in subsets]
                v=initial[:]
                loops=0
                while True:
                    out=[]
                    for s in subsets:
                        out.append(max(v[u]-(u&~s).bit_count()+v[s&~u] for u in subsets))
                    loops+=1
                    if out==v: break
                    assert loops<=n+2
                    v=out
                feasible=[j for j in subsets if all(initial[s]<=(j&s).bit_count() for s in subsets)]
                for s in subsets:
                    assert v[s]==formula(pc[s],k,r),(n,k,r,s,v[s],formula(pc[s],k,r))
                    p=min((j&s).bit_count() for j in feasible)
                    assert p==max(0,pc[s]-(k-r)),(n,k,r,s,p)
                    total+=1
    print('PASS: %d individual subset comparisons, n=1..7, all k,r and subsets, direct closure and model minimization.'%total)

if __name__=='__main__': main()
