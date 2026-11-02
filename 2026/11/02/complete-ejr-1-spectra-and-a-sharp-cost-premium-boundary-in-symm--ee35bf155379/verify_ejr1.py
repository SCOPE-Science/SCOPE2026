"""Direct exhaustive EJR-1 checks for symmetric shared/private budgeting instances."""
from itertools import combinations
from math import comb

def instance(n, h):
    m=n*(h+1)
    cost=tuple([h]*n+[1]*(n*h))
    approve=tuple((1<<n)-1 | sum(1<<(n+i*h+j) for j in range(h)) for i in range(n))
    allmask=(1<<m)-1
    tests=[]
    for group in range(1,1<<n):
        voters=tuple(i for i in range(n) if group & 1<<i)
        shared=allmask
        for i in voters: shared &= approve[i]
        budget=len(voters)*h
        for t in range(1<<m):
            if t & ~shared: continue
            tc=sum(cost[j] for j in range(m) if t>>j&1)
            if tc>budget:continue
            tests.append((voters,t,t.bit_count(),tc))
    return m,cost,approve,allmask,tests

def evaluations(n,h):
    m,cost,approve,allmask,tests=instance(n,h)
    budget=n*h
    vals=[(sum(cost[j] for j in range(m) if mask>>j&1),
           tuple((mask&approve[i]).bit_count() for i in range(n)),
           tuple(sum(cost[j] for j in range(m) if mask>>j&1 and approve[i]>>j&1) for i in range(n)))
          for mask in range(1<<m)]
    total=cost_yes=count_yes=both=0
    least_deficit=None
    for W,(used,card,weighted) in enumerate(vals):
        if used>budget:continue
        common=(W&((1<<n)-1)).bit_count()
        priv=[(W >> (n+i*h) & ((1<<h)-1)).bit_count() for i in range(n)]
        cost_fair = common==n or (common==n-1 and sum(priv)>0)
        card_fair = all(z>=max(h,j) for j,z in enumerate(sorted(common+x for x in priv),1))
        # Evaluate independently: for each cohesive group+project set T, try all additions.
        valid=[True,True]
        for voters,T,tcard,tcost in tests:
            if T&~W==0:continue
            for which,utils,target in ((0,card,tcard),(1,weighted,tcost)):
                if not valid[which]: continue
                success=False
                for p in range(m):
                    if W>>p&1: continue
                    for i in voters:
                        add=(1 if which==0 else cost[p]) if approve[i]>>p&1 else 0
                        if utils[i]+add>target:
                            success=True
                            break
                    if success:break
                if not success:valid[which]=False
            if not valid[0] and not valid[1]:break
        if valid[1]!=cost_fair or (card_fair is not None and valid[0]!=card_fair):
            raise AssertionError((n,h,W,common,priv,valid,cost_fair,card_fair))
        total+=1
        cost_yes+=valid[1]
        if valid[1]:
            deficit=max(0,max(h-(common+x) for x in priv))
            least_deficit=deficit if least_deficit is None else min(least_deficit,deficit)
        count_yes+=valid[0]
        both+=(valid[0] and valid[1])
    expected_cost_count=1+n*sum(comb(n*h,j) for j in range(1,h+1))
    if cost_yes!=expected_cost_count:raise AssertionError(("cost_count",n,h,cost_yes,expected_cost_count))
    predicted_deficit=0 if h<=n else h-n+1-h//n
    if least_deficit!=predicted_deficit:raise AssertionError(("deficit",n,h,least_deficit,predicted_deficit))
    predicted=h<=n
    if (both>0)!=predicted:raise AssertionError(('joint',n,h,both,predicted))
    return n,h,total,cost_yes,count_yes,both,least_deficit

def main():
    checks=[(2,h) for h in range(1,6)]+[(3,h) for h in range(1,5)]+[(4,h) for h in range(1,4)]+[(5,1)]
    for n,h in checks:
        print('verified', evaluations(n,h))
    print('ALL_EJR1_CHECKS_PASS')

if __name__=='__main__':main()
