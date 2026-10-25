"""Self-contained enumeration checks for Hamming-product geodesic distance profiles."""
from itertools import product, permutations, combinations
from math import comb, factorial, prod
from collections import Counter


def ballot_poly(length):
    out = [0] * (length // 2 + 1)
    for j in range(len(out)):
        out[j] = (length - 2*j + 1) * (comb(length,j) - (comb(length,j-1) if j else 0))
    return out


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def expected(q,changed):
    changed=set(changed)
    base=[1]
    for i,v in enumerate(q):
        if i not in changed:
            base=mul(base,[1,v-1])
    c=list(changed)
    active=[0]*(len(c)+1)
    for mask in range(1<<len(c)):
        ways=1
        k=0
        for j,i in enumerate(c):
            if (mask>>j)&1:
                ways*=q[i]-2
                k+=1
        if not ways:continue
        f=ballot_poly(len(c)-k)
        for j,val in enumerate(f):
            active[j+k]+=ways*val
    v=mul(base,active)
    while len(v)>1 and v[-1]==0: v.pop()
    return v


def direct(q,path):
    counts=Counter()
    for x in product(*[range(t) for t in q]):
        d=min(sum(a!=b for a,b in zip(x,y)) for y in path)
        counts[d]+=1
    return [counts[i] for i in range(max(counts)+1)]


def canonical_path(q, changed, order=None):
    p=[0]*len(q)
    result=[tuple(p)]
    for i in (order if order is not None else changed):
        p[i]=1
        result.append(tuple(p))
    return result


def target_ecc(q, changed):
    b=sum(q[i]==2 for i in changed)
    return len(q)-(b+1)//2


def check(q, changed, order=None):
    path=canonical_path(q,changed,order)
    e=expected(q,changed)
    a=direct(q,path)
    assert a==e, (q,changed,order,a,e)
    assert len(a)-1==target_ecc(q,changed), (q,changed,a)
    assert sum(a)==prod(q)


def count_optimal(q):
    vertices=list(product(*[range(t) for t in q]))
    b=sum(t==2 for t in q)
    best=len(q)-(b+1)//2
    total=0
    counted=0
    for v in vertices:
        for l in range(len(q)+1):
            for changes in combinations(range(len(q)),l):
                for vals in product(*[range(1,q[i]) for i in changes]):
                    for order in permutations(changes):
                        p=list(v)
                        path=[tuple(p)]
                        change_value=dict(zip(changes,vals))
                        for i in order:
                            p[i]=(v[i]+change_value[i])%q[i]
                            path.append(tuple(p))
                        # endpoint involution gives /2 for non-singleton
                        if l>0 and path[0]>path[-1]:continue
                        total+=1
                        r=max(min(sum(a!=b for a,b in zip(x,y)) for y in path) for x in vertices)
                        if r==best: counted+=1
    expected_count=0
    if b==0:
        expected_count+=prod(q)
    bs=({b} if b%2 else ({b,b-1} if b>0 else {0}))
    nonbinary=[qi-1 for qi in q if qi>2]
    for s in bs:
        for t in range(len(nonbinary)+1):
            if s+t==0:continue
            weighted=sum(prod(c) for c in combinations(nonbinary,t))
            expected_count+=prod(q)*comb(b,s)*weighted*factorial(s+t)//2
    assert counted==expected_count,(q,counted,expected_count)
    return total,counted


def run():
    cases=0
    for d in range(1,11):
        q=(2,)*d
        for s in range(d+1):
            check(q,tuple(range(s)))
            cases+=1
    mixed=0
    for d in range(1,5):
        for q in product([2,3,4],repeat=d):
            if prod(q)>150:continue
            for mask in range(1<<d):
                changed=tuple(i for i in range(d) if mask>>i&1)
                check(q,changed)
                if len(changed)>=2:
                    check(q,changed,tuple(reversed(changed)))
                mixed+=1
    optimal=0
    for q in [(2,), (3,), (2,2), (2,3), (3,3), (2,2,2), (2,2,3), (2,3,3), (3,3,3), (2,2,2,2), (2,2,2,3), (2,2,3,3)]:
        count_optimal(q)
        optimal+=1
    print('VERIFY_OK binary_profiles=%d mixed_profiles=%d exhaustive_optimal_geodesic_cases=%d' %(cases,mixed,optimal))


if __name__=='__main__': run()
