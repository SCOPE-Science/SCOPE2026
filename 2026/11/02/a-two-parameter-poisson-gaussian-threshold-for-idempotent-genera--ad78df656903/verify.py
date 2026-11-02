"""Independent finite Rees-semigroup multiplication census and cycle-rank checks.
Run: python3 verify.py (Python standard library only)."""
from itertools import product
from collections import defaultdict, Counter, deque
from math import comb


def components_and_rank(a, b, edges, weights, dim):
    vertices = a+b
    adj = [[] for _ in range(vertices)]
    for e,(i,j) in enumerate(edges):
        u,v=i,a+j
        adj[u].append((v,weights[e])); adj[v].append((u,weights[e]))
    visited=set(); size=1; connected=(len(edges)>0)
    betas=[]; ranks=[]
    for root in range(vertices):
        if root in visited: continue
        vertices_comp=[]; potential={root:0}; visited.add(root)
        todo=deque([root]); cycle=[]
        while todo:
            u=todo.popleft(); vertices_comp.append(u)
            for v,w in adj[u]:
                if v not in visited:
                    visited.add(v); potential[v]=potential[u]^w; todo.append(v)
                elif u<v:
                    cycle.append(w^potential[u]^potential[v])
        li=sum(x<a for x in vertices_comp); ri=len(vertices_comp)-li
        if not li or not ri:
            connected=False; continue
        size += li*ri*2**gf2_rank(cycle)
        betas.append(sum(sum(v==vv for vv,_ in adj[u]) for u in vertices_comp for vv in vertices_comp)//2-len(vertices_comp)+1)
        ranks.append(gf2_rank(cycle))
    if len(ranks)!=1 or len(visited)!=vertices: connected=False
    return size, connected and (ranks[0]==dim),tuple(ranks),tuple(betas)


def gf2_rank(vectors):
    basis={}
    for v in vectors:
        while v:
            j=v.bit_length()-1
            if j in basis: v^=basis[j]
            else: basis[j]=v;break
    return len(basis)


def direct_closure(a,b,edges,weights,dim):
    values={(j,i):w for (i,j),w in zip(edges,weights)}
    zero=None
    seen={zero}
    pending=[]
    for (i,j),w in zip(edges,weights):
        g=(i,w,j) # inverse == itself for elementary binary groups
        if g not in seen: seen.add(g);pending.append(g)
    def mul(x,y):
        if x is None or y is None:return None
        i,g,lam=x; j,h,mu=y
        if (lam,j) not in values:return None
        return i,g^values[(lam,j)]^h,mu
    while pending:
        x=pending.pop()
        for y in tuple(seen):
            for z in (mul(x,y),mul(y,x)):
                if z not in seen:seen.add(z);pending.append(z)
    return len(seen),len(seen)==1+a*b*(2**dim)


def verify_case(a,b,dim):
    universe=list(product(range(a),range(b)))
    count=0; rankhist=Counter(); valid=0
    for state in product(range(1+(1<<dim)),repeat=len(universe)):
        edges=[e for e,w in zip(universe,state) if w]
        weights=[w-1 for w in state if w]
        actual,ag=direct_closure(a,b,edges,weights,dim)
        predicted,pg,rhos,betas=components_and_rank(a,b,edges,weights,dim)
        assert actual==predicted, (a,b,dim,edges,weights,actual,predicted,rhos,betas)
        assert ag==pg,(a,b,dim,edges,weights,ag,pg)
        count+=1; valid+=ag
        if len(edges)==len(universe):rankhist[rhos]+=1
    return count,valid,rankhist


def exact_full_support_rank_hist(a,b,dim):
    beta=(a-1)*(b-1)
    p=2
    # ranks of all dim x beta matrices, times factor for tree-edge gauges
    def count_rank(d,e,k):
        num=1
        for j in range(k):num*=((p**d-p**j)*(p**e-p**j))
        den=1
        for j in range(k):den*=p**k-p**j
        return num//den
    return { (k,):count_rank(dim,beta,k)*2**(dim*(a+b-1)) for k in range(min(dim,beta)+1)}

if __name__=='__main__':
    outcomes=[]
    for a,b,dim in [(2,2,1),(2,2,2),(2,3,1),(2,3,2)]:
        num,good,hist=verify_case(a,b,dim)
        assert hist==exact_full_support_rank_hist(a,b,dim),(a,b,dim,hist)
        outcomes.append((a,b,dim,num,good))
    print('VERIFY_OK exhaustive multiplication, all supports and edge labels:',outcomes)


def odd_prime_checks(a,b,p):
    universe=list(product(range(a),range(b)))
    full_hist=Counter()
    n_cases=0
    for state in product(range(p+1),repeat=a*b):
        edges=[e for e,w in zip(universe,state) if w]
        weights={e:(w-1) for e,w in zip(universe,state) if w}
        seen={None};stack=[]
        for (i,j),w in weights.items():
            x=(i,(-w)%p,j)
            if x not in seen:seen.add(x);stack.append(x)
        def mul(x,y):
            if x is None or y is None:return None
            i,g,lam=x;j,h,mu=y
            if (j,lam) not in weights:return None
            return i,(g+weights[(j,lam)]+h)%p,mu
        while stack:
            x=stack.pop()
            for y in tuple(seen):
                for z in (mul(x,y),mul(y,x)):
                    if z not in seen:seen.add(z);stack.append(z)
        # Determine image group dimension with spanning forest potentials.
        adj=[[] for _ in range(a+b)]
        for (i,j),w in weights.items():
            adj[i].append((a+j,w,+1))
            adj[a+j].append((i,w,-1))
        pot={};predicted=1;component_count=0;covered=0; rank_full=False
        for root in range(a+b):
            if root in pot:continue
            pot[root]=0;todo=deque([root]); verts=[]
            while todo:
                u=todo.popleft();verts.append(u)
                for v,w,sgn in adj[u]:
                    if v not in pot:
                        pot[v]=(pot[u]+sgn*w)%p
                        todo.append(v)
            il=sum(v<a for v in verts);jl=len(verts)-il
            if il and jl:
                cycle_values=[(w+pot[i]-pot[a+j])%p for (i,j),w in weights.items() if i in verts]
                rank=int(any(cycle_values))
                predicted+=il*jl*(p**rank)
                component_count+=1
                rank_full=rank==1
                covered+=len(verts)
        assert len(seen)==predicted,(a,b,p,state,len(seen),predicted)
        assert (len(seen)==1+a*b*p)==(component_count==1 and covered==a+b and rank_full)
        if len(weights)==a*b:full_hist[int(rank_full)]+=1
        n_cases+=1
    return n_cases,full_hist

if __name__=='__main__':
    odd=[]
    for a,b,p in [(2,2,3),(2,3,3),(2,2,5)]:
        n,h=odd_prime_checks(a,b,p)
        beta=(a-1)*(b-1);tree=a+b-1
        assert h[0]==p**tree and h[1]==(p**beta-1)*p**tree
        odd.append((a,b,p,n,dict(h)))
    print('VERIFY_OK odd-prime direct group multiplication and cycle spans:',odd)
