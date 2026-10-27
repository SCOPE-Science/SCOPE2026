"""Independent finite checks for centralizer generator-rank theorem.
Only Python standard library is needed.  Run python verify.py.
"""
from itertools import product, combinations
from collections import deque


def make_generators(b):
    # X consists of special fixed point 0 and two points (i,0),(i,1)
    # for each i=1,...,b.  Positions 0,2i-1,2i are these labels.
    m=b+1
    def lift(sigma, keep):
        ans=[0]*(2*b+1)
        ans[0]=0 if sigma[0]==0 else 2*sigma[0]-1
        for i in range(1,m):
            j=sigma[i]
            ans[2*i-1]=0 if j==0 else 2*j-1
            ans[2*i]=0 if j==0 else (2*j if keep[i-1] else 2*j-1)
        return tuple(ans)
    U=[]
    if b>=2:
        sigma=list(range(m));sigma[1],sigma[2]=sigma[2],sigma[1]
        U.append(lift(sigma,[1]*b))
    if b>=3:
        sigma=list(range(m));
        for i in range(1,b):sigma[i]=i+1
        sigma[b]=1
        U.append(lift(sigma,[1]*b))
    sigma=list(range(m));sigma[0],sigma[1]=sigma[1],sigma[0]
    t=lift(sigma,[0]+[1]*(b-1))
    sigma=list(range(m));sigma[0]=1
    z=lift(sigma,[1]*b)
    generators=U+[t,z]
    if b>=2:
        sigma=list(range(m));sigma[2]=1
        c=lift(sigma,[1]*b)
        generators.append(c)
    return generators


def multiply(a,b):
    return tuple(b[i] for i in a)


def generated(b):
    generators=make_generators(b)
    identity=tuple(range(2*b+1))
    seen={identity}
    queue=deque([identity])
    while queue:
        x=queue.popleft()
        for g in generators:
            for y in (multiply(x,g),multiply(g,x)):
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
    # independently enumerate the entire centralizer as actual value vectors
    all_eligible=set()
    for sigma in product(range(b+1),repeat=b+1):
        for keep in product((0,1),repeat=b):
            if any(keep[i-1] and sigma[i]==0 for i in range(1,b+1)):
                continue
            f=[0]*(2*b+1)
            f[0]=0 if sigma[0]==0 else 2*sigma[0]-1
            for i in range(1,b+1):
                j=sigma[i]
                f[2*i-1]=0 if j==0 else 2*j-1
                f[2*i]=0 if j==0 else (2*j if keep[i-1] else 2*j-1)
            all_eligible.add(tuple(f))
    assert seen==all_eligible, (b,len(seen),len(all_eligible),list(all_eligible-seen)[:1])
    assert len(seen)==(b+1)*(2*b+1)**b
    print('b=',b,'generators=',len(generators),'centralizer_size=',len(seen),'PASS')
    return seen,generators


for b in (1,2,3,4):
    generated(b)

# Exhaustive rank check b=2: no unit and two arbitrary nonunits suffice.
# Any generating family must contain a generating set of units.
monoid,generators=generated(2)
identity=tuple(range(5))
u=generators[0]
units={identity,u}
nonunits=sorted(monoid-units)
def quick_closure(gens):
    seen={identity}
    queue=deque([identity])
    while queue:
        x=queue.popleft()
        for g in gens:
            y=multiply(x,g)
            if y not in seen:
                seen.add(y); queue.append(y)
    return seen
assert len(monoid)==75
for x,y in combinations(nonunits,2):
    assert len(quick_closure((u,x,y)))<75, 'Three generators found unexpectedly'
print('b=2: all 2,628 unit-plus-two-nonunit sets are insufficient. PASS')
print('VERIFY_OK_MIXED_REGULAR_CENTRALIZER_RANK')
