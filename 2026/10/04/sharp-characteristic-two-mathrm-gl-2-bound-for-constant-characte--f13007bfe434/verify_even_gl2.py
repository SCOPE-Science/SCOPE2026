from collections import deque

def gf_mul(a,b,m,poly):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a&(1<<m): a^=poly
    return r & ((1<<m)-1)

def gf_pow(a,n,m,poly):
    r=1
    while n:
        if n&1:r=gf_mul(r,a,m,poly)
        a=gf_mul(a,a,m,poly);n>>=1
    return r

def gf_inv(a,m,poly):
    assert a
    return gf_pow(a,(1<<m)-2,m,poly)

def add(a,b):return a^b

def mm(A,B,m,p):
    a,b,c,d=A; e,f,g,h=B
    return (add(gf_mul(a,e,m,p),gf_mul(b,g,m,p)),
            add(gf_mul(a,f,m,p),gf_mul(b,h,m,p)),
            add(gf_mul(c,e,m,p),gf_mul(d,g,m,p)),
            add(gf_mul(c,f,m,p),gf_mul(d,h,m,p)))

def det(A,m,p):
    a,b,c,d=A
    return add(gf_mul(a,d,m,p),gf_mul(b,c,m,p)) # minus=plus char2

def tr(A): return A[0]^A[3]

def inv(A,m,p):
    z=det(A,m,p); iz=gf_inv(z,m,p); a,b,c,d=A
    return tuple(gf_mul(x,iz,m,p) for x in (d,b,c,a))

def closure(gens, elems, m,p):
    I=(1,0,0,1)
    H={I}; q=deque([I])
    gs=list(gens)
    while q:
        a=q.popleft()
        for g in gs:
            for b in (mm(a,g,m,p),mm(g,a,m,p)):
                if b not in H:
                    H.add(b); q.append(b)
    return frozenset(H)

def all_subgroups(G,m,p):
    I=(1,0,0,1); start=frozenset([I]); subs={start}; q=deque([start])
    GL=list(G)
    while q:
        H=q.popleft()
        # representatives outside H; simple
        for g in GL:
            if g in H: continue
            K=closure(list(H)+[g],G,m,p)
            if K not in subs:
                subs.add(K);q.append(K)
    return subs

def is_abelian(H,m,p):
    L=list(H)
    for i,a in enumerate(L):
        for b in L[i+1:]:
            if mm(a,b,m,p)!=mm(b,a,m,p):return False
    return True

def check(m,p):
    q=1<<m
    mats=[(a,b,c,d) for a in range(q) for b in range(q) for c in range(q) for d in range(q)]
    GL=[A for A in mats if det(A,m,p)!=0]
    SL=[A for A in GL if det(A,m,p)==1]
    subs=all_subgroups(SL,m,p)
    print('q',q,'GL',len(GL),'SL',len(SL),'subgroups',len(subs))
    maxord=0; witnesses=[]; bad=[]
    for x in GL:
        tx=tr(x); dx=det(x,m,p)
        valid=[]
        for H in subs:
            ok=True
            for h in H:
                y=mm(x,h,m,p)
                if tr(y)!=tx or det(y,m,p)!=dx:
                    ok=False;break
            if ok:
                valid.append(H)
                if not is_abelian(H,m,p): bad.append(('nonabelian',x,H))
                if len(H)>q+1: bad.append(('large',x,H))
                if tx!=0 and len(H)>q: bad.append(('large_nonzero_trace',x,H))
        mo=max(map(len,valid))
        if mo>maxord:
            maxord=mo;witnesses=[(x,tx,mo)]
        elif mo==maxord:witnesses.append((x,tx,mo))
    print('max order',maxord,'num x attaining',len(witnesses),'bad',len(bad))
    print('sample witness',witnesses[:3])
    assert not bad and maxord==q+1

if __name__=='__main__':
    check(1,0b11)
    check(2,0b111)
