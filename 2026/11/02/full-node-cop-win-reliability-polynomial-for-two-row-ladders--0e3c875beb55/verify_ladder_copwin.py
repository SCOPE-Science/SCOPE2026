#!/usr/bin/env python3
"""Independent finite checks of the cop-win ladder subset enumerator."""
from collections import Counter
from math import comb

def bracket_add(a,b):
    out=[0]*max(len(a),len(b))
    for i in range(len(out)):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return out

def shift(a,k): return [0]*k+a

def transfer(n):
    # weighted state transitions, each vector uses powers of z as indices
    U=[0,2]; V=[0,0,1]; total=[0]*(2*n+1)
    for ell in range(1,n+1):
        a=bracket_add(U,V)
        for k,c in enumerate(a): total[k]+=(n-ell+1)*c
        U,V=shift(bracket_add(U, [2*x for x in V]),1),shift(U,2)
    return total

def graph_edges(n):
    es=[]
    for r in range(2):
        for c in range(n-1): es.append((r*n+c,r*n+c+1))
    for c in range(n):es.append((c,n+c))
    return es

def connected_tree(n,mask,edges):
    if not mask:return False
    vertices=mask.bit_count()
    parent=list(range(2*n))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    components=vertices
    for a,b in edges:
        if (mask>>a)&1 and (mask>>b)&1:
            ra,rb=root(a),root(b)
            if ra==rb:return False
            parent[ra]=rb; components-=1
    return components==1

def word_condition(n,mask):
    col=[((mask>>c)&1)+2*((mask>>(c+n))&1) for c in range(n)]
    if not any(col):return False
    first=next(i for i,x in enumerate(col) if x)
    last=n-1-next(i for i,x in enumerate(reversed(col)) if x)
    if 0 in col[first:last+1]:return False
    for a,b in zip(col[first:last],col[first+1:last+1]):
        if (a,b) in ((3,3),(1,2),(2,1)):return False
    return True

def coefficient_formula(n,k):
    # Enumerate possible numbers of complete columns with a gap formula.
    def C(a,b):return comb(a,b) if 0 <= b <= a else 0
    total=2*(n-k+1) if 1 <= k <= n else 0
    for r in range(1,(k+1)//3+1):
        ell=k-r
        if ell>n:continue
        total+=(n-ell+1)*2**(r-1)*(C(ell-r+1,r)+2*C(ell-r,r)+C(ell-r-1,r))
    return total

def copwin_by_dismantling(n,mask,edges):
    # Test connectivity separately, then greedily remove dominated vertices.
    if mask==0:return False
    verts={i for i in range(2*n) if mask>>i&1}
    adj={i:set() for i in verts}
    for a,b in edges:
        if a in verts and b in verts: adj[a].add(b);adj[b].add(a)
    found={next(iter(verts))}; todo=list(found)
    while todo:
        v=todo.pop()
        for w in adj[v]:
            if w not in found:found.add(w);todo.append(w)
    if len(found)!=len(verts):return False
    while len(verts)>1:
        removable=None
        for v in verts:
            Nv={v}|(adj[v]&verts)
            for u in verts-{v}:
                if Nv <= ({u}|(adj[u]&verts)):
                    removable=v;break
            if removable is not None:break
        if removable is None:return False
        verts.remove(removable)
    return True

def minimum_remainder(n):
    q,r=divmod(n,2)
    return (n+(n+1)//2, (2**q if r else (q+3)*2**(q-1)))

def main():
    for n in range(1,10):
        ed=graph_edges(n)
        measured=Counter()
        for mask in range(1,1<<(2*n)):
            a=connected_tree(n,mask,ed)
            b=word_condition(n,mask)
            assert a==b,(n,mask,a,b)
            if a:measured[mask.bit_count()]+=1
        if n<=7:
            for mask in range(1,1<<(2*n)):
                assert connected_tree(n,mask,ed)==copwin_by_dismantling(n,mask,ed),(n,mask)
        tab=transfer(n)
        assert all(tab[k]==coefficient_formula(n,k) for k in range(2*n+1))
        assert all(tab[k]==measured[k] for k in range(2*n+1)),(n,tab,measured)
        count=sum(tab)
        weight_sum=sum(k*tab[k] for k in range(len(tab)))
        assert count==3*(2**(n+1)-n-2),(n,count)
        assert weight_sum==8*(n-2)*2**n+4*n+16,(n,weight_sum)
        top_n,top_count=minimum_remainder(n)
        assert max(measured)==top_n and measured[top_n]==top_count,(n,measured[top_n],top_count)
        print('n',n,'subsets',2**(2*n)-1,'count',count,'size-sum',weight_sum,'max',top_n,'max-count',top_count)
    # Independent arithmetic generation of 100 exact polynomials and 50 max-counts.
    for n in range(1,101):
        c=transfer(n)
        assert all(c[k]==coefficient_formula(n,k) for k in range(2*n+1))
        assert sum(c)==3*(2**(n+1)-n-2)
        assert sum(k*v for k,v in enumerate(c))==8*(n-2)*2**n+4*n+16
        mx,multip=minimum_remainder(n)
        assert len(c)-1>=mx and c[mx]==multip and not any(c[mx+1:])
    print('VERIFY_OK: 9 exhaustive graph/word/poly comparisons (349,515 nonempty subsets), 7 independent dismantling checks, 100 exact coefficient and transfer checks')

if __name__=='__main__':main()
