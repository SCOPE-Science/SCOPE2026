#!/usr/bin/env python3
"""Reproducible finite certificate for order-five Latin partial-transversal complexes.
Only Python's standard library is required. Prints a reproducible report and VERIFY_OK.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

N = 5
CYCLIC = tuple(tuple((r+c)%N for c in range(N)) for r in range(N))
NONCYCLIC = ((0,1,2,3,4),(1,0,3,4,2),(2,3,4,0,1),(3,4,1,2,0),(4,2,0,1,3))

def latin_ok(L):
    target = set(range(N))
    return len(L)==N and all(set(row)==target for row in L) and all(set(L[r][c] for r in range(N))==target for c in range(N))

def all_reduced():
    first=tuple(range(N)); rows=[first]
    choices={i:[p for p in permutations(range(N)) if p[0]==i] for i in range(1,N)}
    colused=[{c} for c in range(N)]
    out=set()
    def extend(r):
        if r==N:
            out.add(tuple(y for row in rows for y in row));return
        for p in choices[r]:
            if any(p[c] in colused[c] for c in range(N)):continue
            rows.append(p)
            for c in range(N):colused[c].add(p[c])
            extend(r+1)
            for c in range(N):colused[c].remove(p[c])
            rows.pop()
    extend(1)
    return out

def orbit_reduced(A):
    P=list(permutations(range(N)));ans=set()
    for r in P:
        for c in P:
            z=[[A[r[i]][c[j]] for j in range(N)] for i in range(N)]
            smap={z[0][j]:j for j in range(N)}
            n=[[smap[z[i][j]] for j in range(N)] for i in range(N)]
            order=sorted(range(N),key=lambda i:n[i][0])
            ans.add(tuple(n[i][j] for i in order for j in range(N)))
    return ans

def simplices(L):
    """Enumerate all partial transversals; bit v=r*5+c."""
    F=[0]
    layer=[(0,0,0,0)]
    while layer:
        nxt=[]
        for f,R,C,S in layer:
            for v in range(f.bit_length(),N*N):
                r,c=divmod(v,N)
                rr,cc,ss=1<<r,1<<c,1<<L[r][c]
                if R&rr or C&cc or S&ss:continue
                nxt.append((f|(1<<v),R|rr,C|cc,S|ss))
        F.extend(t[0] for t in nxt)
        layer=nxt
    assert len(F)==len(set(F))
    return F

def face_incidence(f):
    vs=[i for i in range(f.bit_length()) if f>>i&1]
    return [(f^(1<<v),1 if j%2==0 else -1) for j,v in enumerate(vs)]

def lex_toggle(F):
    unmatched=set(F); matched={}
    for v in range(N*N):
        bit=1<<v
        candidates=sorted((a for a in unmatched if not a&bit),key=lambda a:(a.bit_count(),a))
        for a in candidates:
            b=a|bit
            if a in unmatched and b in unmatched:
                unmatched.remove(a);unmatched.remove(b);matched[a]=b
    return matched,unmatched

def gradient_check(F,matched):
    g=defaultdict(list);indeg={f:0 for f in F};count=0
    for hi in F:
        for lo,_ in face_incidence(hi):
            a,b=(lo,hi) if matched.get(lo)==hi else (hi,lo)
            g[a].append(b);indeg[b]+=1;count+=1
    queue=deque(f for f in F if indeg[f]==0);visit=0
    while queue:
        f=queue.popleft();visit+=1
        for t in g[f]:
            indeg[t]-=1
            if not indeg[t]:queue.append(t)
    assert visit==len(F), ('cyclic gradient',visit,len(F))
    return count

def critical_boundary(matched,unmatched):
    """Exact signed discrete-Morse boundary C_2^M -> C_1^M.
    f matched upward to b: eliminate f via ∂b=±f+other faces;
    f matched downward: its projection is zero. The DAG check makes recursion finite.
    """
    upper=set(matched.values())
    low=sorted(f for f in unmatched if f.bit_count()==2)
    high=sorted(f for f in unmatched if f.bit_count()==3)
    cache={}
    def flow(f):
        if f in cache:return cache[f]
        if f in upper:answer={}
        elif f in matched:
            b=matched[f];s=dict(face_incidence(b))[f]
            d=defaultdict(int)
            for a,t in face_incidence(b):
                if a==f:continue
                for y,v in flow(a).items():d[y]-=s*t*v
            answer={a:v for a,v in d.items() if v}
        else:answer={f:1}
        cache[f]=answer
        return answer
    M=[]
    for h in high:
        d=defaultdict(int)
        for f,s in face_incidence(h):
            for z,v in flow(f).items():d[z]+=s*v
        M.append(tuple(d[f] for f in low))
    return high,low,M

def determinant(A):
    """Fraction-free determinant, exact integers."""
    n=len(A);a=[list(row) for row in A]
    if not n:return 1
    sg=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            q=next((i for i in range(k+1,n) if a[i][k]),None)
            if q is None:return 0
            a[k],a[q]=a[q],a[k];sg=-sg
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                assert (a[i][j]*p-a[i][k]*a[k][j])%prev==0
                a[i][j]=(a[i][j]*p-a[i][k]*a[k][j])//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sg*a[-1][-1]

def inverse(w):return [-a for a in w[::-1]]

def freely_reduce(w):
    stack=[]
    for x in w:
        if stack and stack[-1]==-x:stack.pop()
        else:stack.append(x)
    while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    return stack

def fundamental_presentation(F):
    es=sorted(f for f in F if f.bit_count()==2)
    tris=sorted(f for f in F if f.bit_count()==3)
    adj=defaultdict(list)
    for e in es:
        u,v=[i for i in range(N*N) if e>>i&1]
        adj[u].append(v);adj[v].append(u)
    visited={0};todo=deque([0]);tree=set()
    while todo:
        u=todo.popleft()
        for v in sorted(adj[u]):
            if v not in visited:
                visited.add(v);todo.append(v);tree.add(tuple(sorted((u,v))))
    assert len(visited)==N*N and len(tree)==N*N-1
    labels={}
    for e in es:
        i,j=[v for v in range(N*N) if e>>v&1]
        if (i,j) not in tree:labels[i,j]=len(labels)+1
    def edge(u,v):
        if u>v:return inverse(edge(v,u))
        return [labels[u,v]] if (u,v) in labels else []
    rel=[]
    for t in tris:
        i,j,k=[v for v in range(N*N) if t>>v&1]
        rel.append(freely_reduce(edge(i,j)+edge(j,k)+edge(k,i)))
    return labels,rel

def tietze_triviality(F):
    """Each eliminated generator occurs exactly once in an explicit relator.
    Substitution and free reduction preserve the presented group. If all vanish,
    the group is trivial. Initial presentation is the standard triangular 2-skeleton.
    """
    labels, rel=fundamental_presentation(F)
    remain=set(labels.values());steps=0;maxlen=0
    while remain:
        occurs=Counter(abs(z) for w in rel for z in w)
        possible=[]
        for j,w in enumerate(rel):
            counts=Counter(abs(z) for z in w)
            for x in counts:
                if counts[x]==1 and x in remain:
                    possible.append((len(w),occurs[x],j,x))
        assert possible, ('cannot eliminate',len(remain),len(rel))
        _,_,j,x=min(possible)
        w=rel[j]
        k=next(i for i in range(len(w)) if abs(w[i])==x)
        a,b=w[:k],w[k+1:]
        replacement=inverse(b+a) if w[k]>0 else b+a
        assert all(abs(z)!=x for z in replacement)
        new=[]
        for word in rel:
            expr=[]
            for z in word:
                if z==x:expr.extend(replacement)
                elif z==-x:expr.extend(inverse(replacement))
                else:expr.append(z)
            reduced=freely_reduce(expr)
            if reduced:new.append(reduced)
            maxlen=max(maxlen,len(reduced))
        rel=new;remain.remove(x);steps+=1
    assert not rel
    assert steps==len(labels)
    return steps,maxlen

def run():
    assert latin_ok(CYCLIC) and latin_ok(NONCYCLIC)
    reduced=all_reduced()
    A,B=orbit_reduced(CYCLIC),orbit_reduced(NONCYCLIC)
    assert (len(reduced),len(A),len(B),len(A&B),len(A|B))==(56,6,50,0,56)
    assert A|B==reduced
    print('isotopy_census reduced=56 cyclic_reduced=6 noncyclic_reduced=50 intersection=0')
    for name,L,faces_expected,crit_expected,unit_columns,rank_expected,pi_max in [
       ('cyclic',CYCLIC,(1,25,150,250,75,15),(-1,0,1,65,0,0),(0,),64,3),
       ('noncyclic',NONCYCLIC,(1,25,150,250,79,3),(-1,0,4,52,0,0),(0,1,2,3),48,3)]:
        F=simplices(L)
        fvec=tuple(sum(f.bit_count()==k for f in F) for k in range(N+1))
        assert fvec==faces_expected,(name,fvec)
        matched,unmatched=lex_toggle(F)
        incidences=gradient_check(F,matched)
        dims=Counter(f.bit_count()-1 for f in unmatched)
        assert dims=={1:crit_expected[2],2:crit_expected[3]},(name,dims)
        high,low,M=critical_boundary(matched,unmatched)
        assert (len(high),len(low))==(crit_expected[3],crit_expected[2])
        assert all(all(abs(v)<=1 for v in row) for row in M)
        square=[[M[j][i] for j in unit_columns] for i in range(len(low))]
        det=determinant(square)
        assert abs(det)==1,(name,square,det)
        pivots,tietze_max=tietze_triviality(F)
        assert pivots==126 and tietze_max<=pi_max
        assert len(high)-len(low)==rank_expected
        chi=sum((-1)**(k-1)*fvec[k] for k in range(len(fvec)))
        assert chi==rank_expected
        print(name,'fvector',fvec[1:],'nonempty',len(F)-1,'incidences',incidences,
              'morse_pairs',len(matched),'critical',dict(dims),'unimodular_minor',unit_columns,
              'det',det,'pi1_generators_eliminated',pivots,'max_relator_length',tietze_max,
              'homotopy_wedge_S2',rank_expected)
    print('VERIFY_OK')

if __name__=='__main__':run()
