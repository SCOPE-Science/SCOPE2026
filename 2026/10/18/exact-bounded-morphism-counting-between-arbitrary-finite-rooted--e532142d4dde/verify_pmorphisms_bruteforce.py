"""Independent direct exhaustive bounded-morphism verifier, with no DP recurrence."""
from itertools import product
from count_pmorphisms_dp import trees_up_to,parent_from_shape,count_bounded_surjections

def is_bounded(parentS,parentT,mapping):
    # Evaluate exact relational forward/back property independently.
    n,m=len(parentS),len(parentT)
    def descendant(p,x,y):
        while y>=0:
            if x==y:return True
            y=p[y]
        return False
    for s in range(n):
        left={mapping[x] for x in range(n) if descendant(parentS,s,x)}
        right={t for t in range(m) if descendant(parentT,mapping[s],t)}
        if left!=right:return False
    return True

def brute(parentS,parentT):
    n,m=len(parentS),len(parentT)
    total=0
    # Every map is examined, not merely order-preserving ones.
    for t in product(range(m),repeat=n):
        if t[0]==0 and len(set(t))==m and is_bounded(parentS,parentT,t):total+=1
    return total

if __name__=='__main__':
    bysize=trees_up_to(6)
    pairs=0;evals=0;positive=0
    for n in range(1,7):
        for source in bysize[n]:
            sp=parent_from_shape(source)
            for m in range(1,n+1):
                for target in bysize[m]:
                    tp=parent_from_shape(target)
                    expect=count_bounded_surjections(sp,tp)
                    got=brute(sp,tp)
                    if expect != got:raise AssertionError((sp,tp,expect,got))
                    pairs+=1;evals+=m**n;positive+=got>0
    print('BRUTE_ALL_MAPS_MATCH',pairs,'PAIRS',evals,'TOTAL_FUNCTIONS','POSITIVE_PAIRS',positive)
