"""Independent state-transition checks for two sharp star best-response results."""
from itertools import product
from functools import lru_cache


def valid_best_step(mask, who, nleaves, center_value, leaf_value, explain=False):
    m=nleaves
    assert 0<=mask<(1<<m)
    if who[0]=='leaf':
        i=who[1]
        assert not (mask>>i)&1, 'leaf already with center'
        assert leaf_value(i,mask|(1<<i))>leaf_value(i,0),'leaf does not improve'
        assert center_value(mask|(1<<i))>=center_value(mask),'center vetoes leaf'
        # Other coalition members' payoff remains one (in our testing instances).
        return mask|(1<<i)
    assert who[0]=='center'
    i=who[1]
    assert not mask>>i&1, 'receiving leaf not free'
    current=center_value(mask)
    singles=[(center_value(1<<j),j) for j in range(m) if not mask>>j&1]
    assert singles, 'no receiving coalition'
    best=max(q for q,j in singles)
    assert center_value(1<<i)==best and best>current, (who,mask,best,current)
    return 1<<i


def verify_long_ir(k):
    # n = k+2: center, anchors a_0,...,a_k; each anchor strictly likes center.
    m=k+1
    def center_value(mask):
        ids=[i for i in range(m) if mask>>i&1]
        return min(ids) if ids else 0
    def leaf_value(i,mask):return int(bool(mask>>i&1))
    mask=(1<<0)|sum(1<<i for i in range(2,k+1))
    initial_mask=mask
    trace=[]
    def move(name, i):
        nonlocal mask
        old=mask
        mask=valid_best_step(mask,(name,i),m,center_value,leaf_value)
        trace.append((name,i,old,mask))
    move('center',1)
    for j in range(1,k):
        for i in range(j+2,k+1):
            move('leaf',i)
        move('center',j+1)
    target=k+(k-1)*(k-2)//2
    assert len(trace)==target,(k,len(trace),target)
    return initial_mask,trace


def enumerate_monotone_values(m,K=2):
    # Every integer monotone nonadditive center function with fixed u(empty)=0.
    masks=sorted(range(1<<m),key=lambda s:(s.bit_count(),s))
    val={0:0}
    def rec(t):
        if t==len(masks):
            yield tuple(val[i] for i in range(1<<m))
            return
        mask=masks[t]
        floor=max(val[mask^(1<<i)] for i in range(m) if mask>>i&1)
        for v in range(floor,K+1):
            val[mask]=v
            yield from rec(t+1)
    yield from rec(1)


def max_trajectory_from_center(center_values):
    m=(len(center_values)-1).bit_length()
    @lru_cache(None)
    def f(mask):
        neighbors=[mask|1<<i for i in range(m) if not mask>>i&1]
        free=[i for i in range(m) if not mask>>i&1]
        if free:
            best=max(center_values[1<<i] for i in free)
            if best>center_values[mask]:
                neighbors += [1<<i for i in free if center_values[1<<i]==best]
        return max((1+f(s) for s in neighbors),default=0)
    return max(f(mask) for mask in range(1<<m))

if __name__=='__main__':
    num=0
    for m in range(1,5):
        count=0
        for values in enumerate_monotone_values(m):
            d=max_trajectory_from_center(values)
            assert d<=2*m-1,(m,values,d)
            count+=1
        num+=count
        print('n',m+1,'monotone nonadditive center preference tables',count,'passed')
    print('Total',num,'monotone preference tables; all center-coalition masks and best response transitions explored')
    for k in range(1,15):
        initial,trace=verify_long_ir(k)
        print('n',k+2,'IR lower example length',len(trace),'formula',k+(k-1)*(k-2)//2)

# Additional separate exhaustive enumeration for nonsymmetric local-additive valuations.
def check_local_additive():
    from itertools import product
    from functools import lru_cache
    total=0
    for m in range(1,6):
        values=range(3 if m<=4 else 2)
        for setting in product(values, repeat=2*m):
            c=setting[:m]
            leaf=setting[m:]
            @lru_cache(None)
            def depth(mask):
                free=[i for i in range(m) if not mask>>i&1]
                value=sum(c[i] for i in range(m) if mask>>i&1)
                choices=[mask|(1<<i) for i in free if leaf[i]>0]
                if free:
                    best=max(c[i] for i in free)
                    if best>value:
                        choices += [1<<i for i in free if c[i]==best]
                return max((1+depth(new) for new in choices),default=0)
            assert max(depth(mask) for mask in range(1<<m))<=2*m-1
            total+=1
    assert total==8404,total
    print('TOTAL',total,'nonsymmetric local-additive valuations, all initial partitions and best-response branches')

if __name__=='__main__':
    check_local_additive()
