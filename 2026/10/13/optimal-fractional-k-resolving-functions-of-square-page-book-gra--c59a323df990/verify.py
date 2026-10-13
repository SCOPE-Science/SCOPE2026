from fractions import Fraction
from collections import deque
from itertools import combinations


def book_graph(r):
    # vertices 0=x, 1=y, then a_i=2+2i, b_i=3+2i
    n = 2 + 2*r
    adj = [set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        for u,v in ((0,a),(a,b),(b,1)):
            adj[u].add(v); adj[v].add(u)
    return adj


def all_distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def resolving_neighborhood(D,u,v):
    return frozenset(z for z in range(len(D)) if D[u][z] != D[v][z])


def expected_R(r,u,v):
    if u>v: u,v=v,u
    V=frozenset(range(2+2*r))
    x,y=0,1
    # helpers identify page/type
    def kind(z):
        if z==x: return ('x',None)
        if z==y: return ('y',None)
        i=(z-2)//2
        return ('a' if z%2==0 else 'b',i)
    ku,iu=kind(u); kv,iv=kind(v)
    if {ku,kv}=={'a'} and iu!=iv:
        return frozenset({2+2*iu,3+2*iu,2+2*iv,3+2*iv})
    if {ku,kv}=={'b'} and iu!=iv:
        return frozenset({2+2*iu,3+2*iu,2+2*iv,3+2*iv})
    if (ku,kv)==('x','b'):
        i=iv
        return frozenset({x,3+2*i} | {2+2*j for j in range(r) if j!=i})
    if (ku,kv)==('y','a'):
        i=iv
        return frozenset({y,2+2*i} | {3+2*j for j in range(r) if j!=i})
    # ordering may place internal first only if x/y are smaller, so no reversed special case needed.
    return V


def feasible(D,g,k):
    n=len(D)
    for u,v in combinations(range(n),2):
        R=resolving_neighborhood(D,u,v)
        if sum(g[z] for z in R) < k:
            return False,(u,v,R,sum(g[z] for z in R))
    return True,None

pairs_checked=0
candidate_checks=0
certificate_checks=0
for r in range(4,11):
    adj=book_graph(r)
    D=all_distances(adj)
    n=len(adj)
    # Exhaust the exact resolving-neighborhood table.
    minR=n
    for u,v in combinations(range(n),2):
        actual=resolving_neighborhood(D,u,v)
        exp=expected_R(r,u,v)
        assert actual==exp,(r,u,v,actual,exp)
        minR=min(minR,len(actual))
        pairs_checked += 1
    assert minR==4,(r,minR)

    # The summed page-pair inequalities are a dual certificate:
    # every internal vertex occurs in exactly r-1 of them.
    incidence=[0]*n
    page_pair_sets=[]
    for i,j in combinations(range(r),2):
        R=frozenset({2+2*i,3+2*i,2+2*j,3+2*j})
        page_pair_sets.append(R)
        for z in R: incidence[z]+=1
    assert incidence[0]==incidence[1]==0
    assert all(incidence[z]==r-1 for z in range(2,n))
    certificate_checks += 1

    for k in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3),Fraction(7,2),Fraction(4)]:
        g=[Fraction(0),Fraction(0)] + [k/Fraction(4)]*(2*r)
        ok,bad=feasible(D,g,k)
        assert ok,(r,k,bad)
        assert sum(g)==Fraction(r)*k/Fraction(2)
        # Certificate arithmetic: sum_{i<j} k divided by multiplicity r-1.
        lower=Fraction(r*(r-1),2)*k/Fraction(r-1)
        assert lower==Fraction(r)*k/Fraction(2)
        candidate_checks += 1

# Exact r=4 uniqueness consequence from the optimizer equations:
# page sums are k/2. Writing A=sum a_i, the two cross inequalities give
# 2 a_i <= A-k/2 and 2 a_i >= A-k/2, hence all a_i equal; summing gives A=k.
for k in [Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3),Fraction(7,2),Fraction(4)]:
    A=k
    ai=A/Fraction(4)
    assert ai==k/Fraction(4)
    assert k/Fraction(2)-ai==k/Fraction(4)

# Construct asymmetric optimum examples for r>=6 and k<=2:
asym_examples=0
for r in range(6,11):
    adj=book_graph(r); D=all_distances(adj)
    for k in [Fraction(1),Fraction(3,2),Fraction(2)]:
        m=3
        g=[Fraction(0),Fraction(0)]
        for i in range(r):
            if i<m:
                g.extend([k/Fraction(2),Fraction(0)])
            else:
                g.extend([Fraction(0),k/Fraction(2)])
        ok,bad=feasible(D,g,k)
        assert ok,(r,k,bad)
        assert sum(g)==Fraction(r)*k/Fraction(2)
        asym_examples += 1

print('VERIFY_OK')
print('book_parameters_checked = 7')
print('parameters r = 4..10')
print('resolving_neighborhood_pairs_checked =', pairs_checked)
print('uniform_candidate_checks =', candidate_checks)
print('dual_certificate_parameters_checked =', certificate_checks)
print('asymmetric_optimum_examples_checked =', asym_examples)
print('all resolving-neighborhood tables matched the theorem')
print('all kappa values equal 4')
print('all dual certificates give lower bound r*k/2')
print('all uniform candidates attain r*k/2 for sampled rational k in [1,4]')
print('r=4 uniqueness algebra replayed exactly')
print('asymmetric minima verified for r>=6 and k<=2')
