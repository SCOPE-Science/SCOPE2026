"""Direct exact checks of graph-incidence pseudocomplement and implication theorem.
Standalone, Python 3 stdlib only; no external files are required.
"""
from itertools import product
from fractions import Fraction
from math import factorial, comb


def iter_graphs(n, only_admissible=False):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for cs in product(range(3),repeat=len(pairs)):
        deg=[0]*n
        for (i,j),c in zip(pairs,cs):
            deg[i]+=c;deg[j]+=c
        if only_admissible and max(deg,default=0)>2:continue
        yield pairs,cs,deg


def evaluate(n,pairs,cs):
    # Graph-incidence elements 0..n-1 vertices, n..n+m-1 edge occurrences, top last.
    endpoint=[]
    for (u,v),c in zip(pairs,cs):
        endpoint.extend([(u,v)]*c)
    m=len(endpoint); top=n+m; N=top+1
    less=[[False]*N for _ in range(N)]
    for x in range(N):less[x][x]=True;less[x][top]=True
    for e,(u,v) in enumerate(endpoint,n):
        less[u][e]=less[v][e]=True
    def members_low(a,b):return [z for z in range(N) if less[z][a] and less[z][b]]
    def complement(a,y):
        # candidates c in [y,1] with section-common lower cone exactly {y}.
        cand=[c for c in range(N) if less[y][c] and [z for z in members_low(a,c) if less[y][z]]==[y]]
        greatest=[c for c in cand if all(less[d][c] for d in cand)]
        return greatest[0] if len(greatest)==1 else None
    comp={}
    good=True
    for y in range(N):
        for a in range(N):
            if less[y][a]:
                c=complement(a,y)
                if c is None:good=False
                else:comp[a,y]=c
    if not good:return False,None,len(endpoint)
    amb=0
    for x in range(N):
        for y in range(N):
            upp=[z for z in range(N) if less[x][z] and less[y][z]]
            mn=[z for z in upp if all(not(less[u][z] and u!=z) for u in upp)]
            val={comp[a,y] for a in mn}
            if len(val)>1:
                assert len(val)==2 and x<n and y<n and x!=y
                amb+=1
    return True,amb,m




def evaluate_incidence(n, m, cols):
    # n labelled points, m distinct labelled nonempty blocks.
    # cols: m integers, bit i reports incidence of point i.
    N=n+m+1; top=N-1
    less=[[False]*N for _ in range(N)]
    for x in range(N):less[x][x]=True;less[x][top]=True
    for j,mask in enumerate(cols):
        for i in range(n):
            if (mask>>i)&1:less[i][n+j]=True
    def low(a,b):return [z for z in range(N) if less[z][a] and less[z][b]]
    comp={}; good=True
    for y in range(N):
        for a in range(N):
            if not less[y][a]:continue
            cand=[c for c in range(N) if less[y][c] and [z for z in low(a,c) if less[y][z]]==[y]]
            tops=[c for c in cand if all(less[d][c] for d in cand)]
            if len(tops)!=1:good=False
            else:comp[a,y]=tops[0]
    if not good:return False,None
    ambiguous=[]
    for x in range(N):
        for y in range(N):
            upp=[z for z in range(N) if less[x][z] and less[y][z]]
            mn=[z for z in upp if all(not(less[u][z] and u!=z) for u in upp)]
            val={comp[a,y] for a in mn}
            if len(val)>1:ambiguous.append((x,y,tuple(sorted(val))))
    return True,ambiguous


def power_add(a,b,N):return [(a[i] if i<len(a) else Fraction(0))+(b[i] if i<len(b) else Fraction(0)) for i in range(N+1)]

def exp_series(logcoeff,N):
    out=[Fraction(1)]
    for k in range(1,N+1):
        out.append(sum(Fraction(j)*logcoeff[j]*out[k-j] for j in range(1,k+1))/k)
    return out

def check():
    incidence_tested=incidence_good=incidence_amb=0
    for n in range(1,4):
        for m in range(1,4):
            for cols in product(range(1,1<<n), repeat=m):
                incidence_tested+=1
                deg=[sum(bool(mask & (1<<i)) for mask in cols) for i in range(n)]
                good,amb=evaluate_incidence(n,m,cols)
                assert good==(max(deg)<=2),(n,m,cols,deg,good)
                if not good:continue
                incidence_good+=1
                counts={}
                for i in range(n):
                    support=tuple(j for j,mask in enumerate(cols) if (mask>>i)&1)
                    if len(support)==2:counts[support]=counts.get(support,0)+1
                expected=sum(t*(t-1) for t in counts.values())
                assert len(amb)==expected,(n,m,cols,amb,expected)
                assert all(x<n and y<n and x!=y and len(value)==2 for x,y,value in amb)
                incidence_amb+=len(amb)
    tested=valid=total_amb=0
    dist={}
    for n in range(1,5):
        by_m={};at_n=0
        for pairs,cs,deg in iter_graphs(n):
            tested+=1
            g,amb,m=evaluate(n,pairs,cs)
            assert g==(max(deg,default=0)<=2),(n,cs,'admissibility')
            if not g:continue
            doubles=sum(c==2 for c in cs)
            assert amb==2*doubles,(n,cs,amb,doubles)
            valid+=1;total_amb+=amb;at_n+=1
            by_m[doubles]=by_m.get(doubles,0)+1
        dist[n]=by_m
    # 5-vertex valid graphs: full implication tests (cheap for small admissible subfamily).
    n=5;by_m={}
    for pairs,cs,deg in iter_graphs(n,only_admissible=True):
        g,amb,m=evaluate(n,pairs,cs)
        assert g and amb==2*sum(c==2 for c in cs)
        valid+=1;total_amb+=amb
        by_m[amb//2]=by_m.get(amb//2,0)+1
    dist[n]=by_m
    # EGF coefficients log(F(x,t)) = -1/2 log(1-x)+x/[2(1-x)]+(2t-1)x^2/4
    N=5
    for t in (0,1,2,3):
        log=[Fraction(0)]+[Fraction(1,2*k)+Fraction(1,2)+(Fraction(2*t-1,4) if k==2 else 0) for k in range(1,N+1)]
        vals=exp_series(log,N)
        for n in range(1,N+1):
            expected=sum(mult*t**d for d,mult in dist[n].items())
            assert vals[n]*factorial(n)==expected,(n,t,vals[n],dist[n],expected)
    # check exact coefficient probabilities into 2-cycle multiplicities n<=35 via rational series
    N=35
    log=[Fraction(0)]+[Fraction(1,2*k)+Fraction(1,2)+(Fraction(1,4) if k==2 else 0) for k in range(1,N+1)]
    total=exp_series(log,N)
    sharp_log=log[:];sharp_log[2]-=Fraction(1,2)
    sharp=exp_series(sharp_log,N)
    assert sharp[2]*factorial(2)==2 and total[2]*factorial(2)==3
    print('VERIFY_OK', 'incidence_tested',incidence_tested, 'incidence_good',incidence_good, 'incidence_ambiguous_pairs',incidence_amb, 'graphs_all_n_le_4',tested, 'admissible_implications_tested',valid, 'ambiguous_inputs',total_amb)
    print('EXACT_SHARPNESS_COUNTS', {n:(int(sharp[n]*factorial(n)),int(total[n]*factorial(n))) for n in range(1,9)})
    print('COUNT_DISTRIBUTIONS',dist)
    print('SHARP_RATIO_N35',float(sharp[35]/total[35]),'POISSON_LIMIT',0.6065306597126334)

if __name__=='__main__':check()
