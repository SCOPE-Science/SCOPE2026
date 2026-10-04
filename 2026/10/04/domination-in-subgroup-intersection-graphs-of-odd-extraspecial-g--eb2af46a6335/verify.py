from itertools import combinations
from collections import Counter


def subgroup_generated(G, mul, inv, gens, e):
    H={e}
    frontier=list(gens)
    while frontier:
        g=frontier.pop()
        if g in H: continue
        old=list(H)
        # close by g and g^-1 against current H
        candidates=[g, inv(g)]
        for h in old:
            candidates += [mul(h,g),mul(g,h),mul(h,inv(g)),mul(inv(g),h)]
        H.add(g)
        for x in candidates:
            if x not in H:
                frontier.append(x)
    # final closure safety
    changed=True
    while changed:
        changed=False
        L=list(H)
        for a in L:
            ia=inv(a)
            if ia not in H:
                H.add(ia); changed=True
            for b in L:
                c=mul(a,b)
                if c not in H:
                    H.add(c); changed=True
    return frozenset(H)


def all_subgroups(G,mul,inv,e):
    triv=frozenset([e])
    seen={triv}
    frontier=[triv]
    while frontier:
        H=frontier.pop()
        for g in G:
            if g not in H:
                K=subgroup_generated(G,mul,inv,list(H)+[g],e)
                if K not in seen:
                    seen.add(K); frontier.append(K)
    return sorted(seen,key=lambda H:(len(H),sorted(map(str,H))))


def graph_of_intersection(G,subs,e):
    whole=frozenset(G); triv=frozenset([e])
    V=[H for H in subs if H not in (triv,whole)]
    adj=[set() for _ in V]
    for i,H in enumerate(V):
        for j in range(i+1,len(V)):
            K=V[j]
            if len(H & K)>1:
                adj[i].add(j); adj[j].add(i)
    return V,adj


def dominates(S,adj,total=False):
    S=set(S)
    for v in range(len(adj)):
        if total:
            if not (adj[v] & S): return False
        else:
            if v not in S and not (adj[v] & S): return False
    return True


def perfect_matching(S,adj):
    S=set(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in list(adj[v]&S):
        if perfect_matching(S-{v,u},adj): return True
    return False


def minima(adj):
    n=len(adj)
    ans=[None,None,None]
    for k in range(1,n+1):
        for S in combinations(range(n),k):
            if ans[0] is None and dominates(S,adj,False): ans[0]=(k,S)
            if ans[1] is None and dominates(S,adj,True): ans[1]=(k,S)
            if ans[2] is None and k%2==0 and dominates(S,adj,False) and perfect_matching(S,adj): ans[2]=(k,S)
            if all(x is not None for x in ans): return ans
    return ans

# Heisenberg group H_3, exponent 3: triples (a,b,c) mod 3,
# (a,b,c)(A,B,C)=(a+A,b+B,c+C+aB).
p=3
H3=[(a,b,c) for a in range(p) for b in range(p) for c in range(p)]
e3=(0,0,0)
def hmul(x,y):
    a,b,c=x; A,B,C=y
    return ((a+A)%3,(b+B)%3,(c+C+a*B)%3)
def hinv(x):
    a,b,c=x
    # (-a,-b,-c+ab)
    return ((-a)%3,(-b)%3,(-c+a*b)%3)

# Modular group M_27 = C9 semidirect C3 with b a b^-1 = a^4.
# Elements (i,j)=a^i b^j and multiplication (i,j)(k,l)=(i+4^j k,j+l).
M27=[(i,j) for i in range(9) for j in range(3)]
eM=(0,0)
def mmul(x,y):
    i,j=x; k,l=y
    return ((i + pow(4,j,9)*k)%9,(j+l)%3)
def minv(x):
    i,j=x
    # inverse exponent k solves i+4^j k=0 mod9
    mult=pow(4,j,9)
    invmult=pow(mult,-1,9)
    return ((-i*invmult)%9,(-j)%3)

rows=[]
for name,G,mul,inv,e,expected in [
    ('Heisenberg27_exp3',H3,hmul,hinv,e3,(4,4,4)),
    ('Modular27_exp9',M27,mmul,minv,eM,(1,2,2)),
]:
    subs=all_subgroups(G,mul,inv,e)
    V,adj=graph_of_intersection(G,subs,e)
    mins=minima(adj)
    got=tuple(x[0] for x in mins)
    assert got==expected,(name,got,expected)
    orders=Counter(map(len,V))
    rows.append((name,len(V),dict(sorted(orders.items())),got))

# Structural checks of the two proof mechanisms.
# Every nonidentity H3 element has order 3.
def power(x,n,mul,e):
    y=e
    for _ in range(n): y=mul(y,x)
    return y
assert all(power(x,3,hmul,e3)==e3 for x in H3)

# In M27 the p-th power kernel is an index-p subgroup and contains every order-p element.
K=frozenset(x for x in M27 if power(x,3,mmul,eM)==eM)
assert len(K)==9
assert K != frozenset([eM]) and K != frozenset(M27)
order3=[x for x in M27 if x!=eM and power(x,3,mmul,eM)==eM]
assert all(x in K for x in order3)

# Hyperplane-cover check for F_3^2: exactly p+1=4 one-dimensional hyperplanes are necessary and sufficient.
vec=[(a,b) for a in range(3) for b in range(3)]
lines=[]
for v in vec[1:]:
    L=frozenset(((t*v[0])%3,(t*v[1])%3) for t in range(3))
    if L not in lines: lines.append(L)
assert len(lines)==4
assert set().union(*lines)==set(vec)
for S in combinations(lines,3):
    assert set().union(*S)!=set(vec)

print('VERIFY_OK')
for name,nv,orders,got in rows:
    print(f'{name}: vertices={nv} subgroup_orders={orders} gamma={got[0]} gamma_t={got[1]} gamma_pr={got[2]}')
print('M27_pth_power_kernel_size=9_contains_all_order3_elements')
print('F3^2_hyperplane_cover_minimum=4')
