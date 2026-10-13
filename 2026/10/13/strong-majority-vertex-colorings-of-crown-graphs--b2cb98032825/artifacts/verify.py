from itertools import product
from math import factorial, ceil


def crown(n):
    # A={0,...,n-1}, B={n,...,2n-1}, missing i--(n+i)
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def direct(n,col):
    adj=crown(n)
    h=(n-1)//2
    for v in range(2*n):
        counts={}
        for u in adj[v]:
            counts[col[u]]=counts.get(col[u],0)+1
        if counts and max(counts.values())>h:
            return False
    return True


def structural(n,col,q):
    h=(n-1)//2
    for c in range(q):
        if sum(1 for i in range(n) if col[i]==c)>h:
            return False
        if sum(1 for i in range(n,2*n) if col[i]==c)>h:
            return False
    return True


def compositions(n,q,h):
    out=[]
    def rec(rem,k,cur):
        if k==1:
            if rem<=h:
                out.append(tuple(cur+[rem]))
            return
        for x in range(min(h,rem)+1):
            rec(rem-x,k-1,cur+[x])
    if q==0:
        return [()] if n==0 else []
    rec(n,q,[])
    return out


def E(n,q):
    if q==0:
        return 0
    h=(n-1)//2
    ans=0
    for xs in compositions(n,q,h):
        ways=factorial(n)
        for x in xs:
            ways//=factorial(x)
        ans+=ways
    return ans


def onto_formula(n,q):
    ans=0
    from math import comb
    for j in range(q+1):
        e=E(n,q-j)
        ans += (-1)**j * comb(q,j) * e*e
    return ans

assignments=0
cases=[]
for n,qs in [(3,range(1,5)),(4,range(1,5)),(5,range(1,4)),(6,range(1,4))]:
    minq=None
    for q in qs:
        total=0
        onto=0
        for col in product(range(q), repeat=2*n):
            assignments += 1
            d=direct(n,col)
            s=structural(n,col,q)
            if d!=s:
                raise AssertionError(("criterion",n,q,col,d,s))
            if d:
                total+=1
                if len(set(col))==q:
                    onto+=1
        if total != E(n,q)**2:
            raise AssertionError(("palette count",n,q,total,E(n,q)**2))
        if onto != onto_formula(n,q):
            raise AssertionError(("onto count",n,q,onto,onto_formula(n,q)))
        if total>0 and minq is None:
            minq=q
    expected=ceil(n/((n-1)//2))
    if minq!=expected:
        raise AssertionError(("minimum",n,minq,expected))
    cases.append((n,minq,E(n,minq)**2))

# Formula-only structural checks for a wider range.
for n in range(3,51):
    h=(n-1)//2
    q=ceil(n/h)
    # balanced side composition with every part at most h exists by definition.
    if E(n,q)==0:
        raise AssertionError(("no optimal side coloring",n,q))
    if q>1 and E(n,q-1)!=0:
        raise AssertionError(("unexpected fewer colors",n,q))

print(
    "ALL CHECKS PASSED; "
    f"color_assignments_checked={assignments}; "
    f"exhaustive_cases={cases}; "
    "structural_formula_n=3..50"
)
