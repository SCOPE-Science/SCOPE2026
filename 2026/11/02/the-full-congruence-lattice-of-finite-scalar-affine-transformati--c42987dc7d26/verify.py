"""Exact check of congruence classification for scalar-affine monoids.
All arithmetic is over prime fields; enumeration is exhaustive for sizes <=9.
"""
import itertools, math

def elements(p,r):
    return [(v,a) for v in itertools.product(range(p),repeat=r) for a in range(p)]

def product(x,y,p):
    v,a=x; w,b=y
    return (tuple((v[i]+a*w[i])%p for i in range(len(v))), a*b%p)

def lin_span(vectors,p,r):
    span={tuple(0 for _ in range(r))}
    for v in vectors:
        span={tuple((x[i]+c*v[i])%p for i in range(r)) for x in span for c in range(p)}
    return frozenset(span)

def subspaces(p,r):
    vecs=list(itertools.product(range(p),repeat=r))
    ss={frozenset({tuple(0 for _ in range(r))})}
    for v in vecs:
        ss.update({lin_span(list(a)+[v],p,r) for a in list(ss)})
    return sorted(ss,key=lambda x:(len(x),sorted(x)))

def predicted_relations(p,r):
    E=elements(p,r)
    U=[i for i,(v,a) in enumerate(E) if a!=0]
    I=[i for i,(v,a) in enumerate(E) if a==0]
    V=frozenset(itertools.product(range(p),repeat=r))
    zero=(0,)*r
    subs=subspaces(p,r)
    out={}
    for W in subs:
        for T in subs:
            if not T.issubset(W): continue
            def equiv(i,j):
                (v,a),(w,b)=E[i],E[j]
                if a==0 and b==0: return tuple((x-y)%p for x,y in zip(v,w)) in W
                if a==0 or b==0: return False
                if a != b: return False
                return tuple((x-y)%p for x,y in zip(v,w)) in T
            blocks=canon(E,equiv)
            out[blocks]=('flag',len(W),len(T))
    # Quotients by N=V semidirect H, H nontrivial subgroups of F_p^*.
    for h_size in range(2,p):
        if (p-1)%h_size: continue
        H=frozenset(pow(a,(p-1)//h_size,p) for a in range(1,p))
        if len(H)!=h_size: raise AssertionError(('group generation',p,h_size,H))
        def equiv(i,j):
            (v,a),(w,b)=E[i],E[j]
            if a==0 and b==0:return True
            if a==0 or b==0:return False
            return (a*pow(b,-1,p))%p in H
        out[canon(E,equiv)]=('scalar',h_size)
    out[(tuple(range(len(E))),)]=('universal',)
    return out

def canon(E,equiv):
    unseen=set(range(len(E))); B=[]
    while unseen:
        i=min(unseen)
        block=tuple(sorted(j for j in unseen if equiv(i,j)))
        for j in block:unseen.remove(j)
        B.append(block)
    return tuple(B)

def check_cong(p,r,blocks):
    E=elements(p,r); idx={a:i for i,a in enumerate(E)}
    cls={i:k for k,b in enumerate(blocks) for i in b}
    M=[[idx[product(x,y,p)] for y in E] for x in E]
    n=len(E)
    for b in blocks:
        for i in b:
            for j in b:
                for z in range(n):
                    if cls[M[i][z]]!=cls[M[j][z]] or cls[M[z][i]]!=cls[M[z][j]]:
                        return False
    return True

def all_partitions(n):
    # restricted-growth codes enumerate Bell(n) partitions
    code=[0]*n
    def rec(k,m):
        if k==n:
            groups=[[] for _ in range(m+1)]
            for i,j in enumerate(code):groups[j].append(i)
            yield tuple(tuple(g) for g in groups)
            return
        for v in range(m+2):
            code[k]=v
            yield from rec(k+1,max(m,v))
    if n: yield from rec(1,0)

def exhaustive(p,r):
    E=elements(p,r); ans=set()
    for blocks in all_partitions(len(E)):
        if check_cong(p,r,blocks):ans.add(blocks)
    return ans

if __name__=='__main__':
    for p,r in ((2,1),(2,2),(3,1),(3,2),(5,1)):
        pred=predicted_relations(p,r)
        assert all(check_cong(p,r,b) for b in pred),(p,r)
        print(f'p={p} r={r} monoid_size={p**(r+1)} predicted_congruences={len(pred)} constructed_verified')
        if p**(r+1)<=9:
            allc=exhaustive(p,r)
            assert set(pred)==allc,(p,r,'exhaustive',len(allc),'predicted',len(pred))
            print(f'p={p} r={r} exhaustive_Bell_congruences={len(allc)} EXACT_MATCH')
    print('VERIFY_OK')

# Extension-field check: F_4 = F_2[u]/(u^2+u+1), with u encoded as 2.
def gf4_mul(a,b):
    z = 0
    for i in range(2):
        if (b >> i)&1: z ^= a << i
    if z&8: z ^= 0b1110   # u^3 = u^2+u; not needed for degree<=2 inputs
    if z&4: z ^= 0b111
    return z

def gf4_check(r):
    vecs = list(itertools.product(range(4),repeat=r))
    subs = {frozenset({(0,)*r})}
    for v in vecs:
        for T in tuple(subs):
            subs.add(frozenset(tuple(t[i]^gf4_mul(s,v[i]) for i in range(r)) for t in T for s in range(4)))
    for v in vecs:
        for T in tuple(subs):
            subs.add(frozenset(tuple(t[i]^gf4_mul(s,v[i]) for i in range(r)) for t in T for s in range(4)))
    assert len(subs)==(2 if r==1 else 7),(r,len(subs))
    E=[(v,a) for v in vecs for a in range(4)]
    index={x:i for i,x in enumerate(E)}
    M=[[index[(tuple(v[i]^gf4_mul(a,w[i]) for i in range(r)),gf4_mul(a,b))] for w,b in E] for v,a in E]
    out=set()
    for W in subs:
        for T in subs:
            if not T.issubset(W):continue
            def eq(i,j):
                (v,a),(w,b)=E[i],E[j]
                if a==0 and b==0:return tuple(v[k]^w[k] for k in range(r)) in W
                if a==0 or b==0 or a!=b:return False
                return tuple(v[k]^w[k] for k in range(r)) in T
            out.add(canon(E,eq))
    # Nontrivial scalar subgroup F4^* of order 3.
    out.add(canon(E,lambda i,j: (E[i][1]!=0 and E[j][1]!=0) or (E[i][1]==0 and E[j][1]==0)))
    out.add((tuple(range(len(E))),))
    for blocks in out:
        cid={i:k for k,B in enumerate(blocks) for i in B}
        for B in blocks:
            for i in B:
                for j in B:
                    for k in range(len(E)):
                        assert cid[M[i][k]]==cid[M[j][k]] and cid[M[k][i]]==cid[M[k][j]]
    expected=(5 if r==1 else 20)
    assert len(out)==expected,(r,len(out),expected)
    print(f'q=4 r={r} monoid_size={len(E)} predicted_congruences={len(out)} constructed_verified')

if __name__=='__main__':
    for r in (1,2):gf4_check(r)
    print('EXTENSION_FIELD_VERIFY_OK')
