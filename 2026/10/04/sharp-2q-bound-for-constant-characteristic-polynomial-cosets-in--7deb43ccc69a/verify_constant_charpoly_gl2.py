from itertools import product
from collections import deque, Counter

def mm(A,B,q):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
def det(A,q):
    a,b,c,d=A; return (a*d-b*c)%q
def tr(A,q): return (A[0]+A[3])%q
def inv(A,q):
    a,b,c,d=A; z=pow(det(A,q),-1,q)
    return ((d*z)%q,(-b*z)%q,(-c*z)%q,(a*z)%q)
def gen_subgroup(gens,q):
    I=(1,0,0,1); gs=list(gens)+[inv(g,q) for g in gens]
    S={I}; Q=deque([I])
    while Q:
        a=Q.popleft()
        for g in gs:
            b=mm(a,g,q)
            if b not in S: S.add(b); Q.append(b)
    return frozenset(S)
def all_subgroups(G,q):
    I=(1,0,0,1); root=frozenset([I]); seen={root}; Q=[root]
    while Q:
        H=Q.pop()
        for g in G:
            if g not in H:
                K=gen_subgroup(list(H)+[g],q)
                if K not in seen: seen.add(K); Q.append(K)
    return seen
def comm(A,B,q): return mm(A,B,q)==mm(B,A,q)
def valid_x(H,q,GL):
    return [x for x in GL if all(det(h,q)==1 and tr(mm(x,h,q),q)==tr(x,q) for h in H)]

def check(q):
    GL=[A for A in product(range(q),repeat=4) if det(A,q)]
    SL=[A for A in GL if det(A,q)==1]
    subs=all_subgroups(SL,q)
    valid=[]
    for H in subs:
        xs=valid_x(H,q,GL)
        if xs:
            assert all(comm(a,b,q) for a in H for b in H)
            assert len(H)<=2*q
            valid.append((len(H),len(xs)))
    mx=max(n for n,_ in valid)
    eq=[p for p in valid if p[0]==2*q]
    print(f'q={q}: |SL2|={len(SL)}, subgroups={len(subs)}, valid_subgroups={len(valid)}, max_order={mx}, equality_subgroups={len(eq)}')
    print('  (order,number_of_valid_x)->count:', sorted(Counter(valid).items()))
    assert mx==2*q
for q in (3,5): check(q)
print('VERIFY_OK')
