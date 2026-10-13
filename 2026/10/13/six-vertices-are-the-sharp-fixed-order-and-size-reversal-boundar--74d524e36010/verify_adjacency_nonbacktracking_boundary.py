from itertools import combinations, permutations
from fractions import Fraction

# polynomial low -> high, Fraction/int

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def padd(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def pneg(a): return [-x for x in a]
def psub(a,b): return padd(a,pneg(b))
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return trim(c)

def pdivmod(a,b):
    a=[Fraction(x) for x in trim(a)]; b=[Fraction(x) for x in trim(b)]
    if b==[0]: raise ZeroDivisionError
    q=[Fraction(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); coef=a[-1]/b[-1]; q[k]+=coef
        for j in range(len(b)): a[j+k]-=coef*b[j]
        a=trim(a)
    return trim(q), trim(a)

def deriv(p): return [i*p[i] for i in range(1,len(p))] or [0]
def peval(p,x):
    y=Fraction(0)
    for c in reversed(p): y=y*x+c
    return y

def pgcd(a,b):
    a=[Fraction(x) for x in trim(a)]; b=[Fraction(x) for x in trim(b)]
    while b != [0]:
        _,r=pdivmod(a,b); a,b=b,r
    if a==[0]: return [0]
    lead=a[-1]
    return [x/lead for x in a]

def squarefree(p):
    p=[Fraction(x) for x in trim(p)]
    g=pgcd(p,deriv(p))
    q,r=pdivmod(p,g)
    assert r==[0]
    return q

def sturm(p):
    p=squarefree(p)
    seq=[p,deriv(p)]
    while seq[-1] != [0]:
        _,r=pdivmod(seq[-2],seq[-1])
        if r==[0]: break
        seq.append([-x for x in r])
    return seq

def variations(seq,x):
    signs=[]
    for p in seq:
        v=peval(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def roots_between(seq,a,b): return variations(seq,a)-variations(seq,b)

def largest_root_interval(p,lo,hi,bits=60):
    seq=sturm(p); lo=Fraction(lo); hi=Fraction(hi)
    assert roots_between(seq,lo,hi)>=1,(p,lo,hi,roots_between(seq,lo,hi))
    # isolate largest root
    for _ in range(bits):
        mid=(lo+hi)/2
        if roots_between(seq,mid,hi)>=1: lo=mid
        else: hi=mid
    return lo,hi

def perm_sign(p):
    inv=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            inv += p[i]>p[j]
    return -1 if inv%2 else 1

def det_poly(mat):
    n=len(mat); total=[0]
    for perm in permutations(range(n)):
        term=[1]
        zero=False
        for i,j in enumerate(perm):
            e=mat[i][j]
            if e==[0]: zero=True; break
            term=pmul(term,e)
        if not zero:
            if perm_sign(perm)<0: term=pneg(term)
            total=padd(total,term)
    return trim(total)

def adj_poly(n,edges):
    E={tuple(sorted(e)) for e in edges}
    M=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j: row.append([0,1])
            elif tuple(sorted((i,j))) in E: row.append([-1])
            else: row.append([0])
        M.append(row)
    return det_poly(M)

def nb_aux_poly(n,edges):
    E={tuple(sorted(e)) for e in edges}; deg=[0]*n
    for u,v in E:deg[u]+=1;deg[v]+=1
    M=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:row.append([deg[i]-1,0,1])
            elif tuple(sorted((i,j))) in E:row.append([0,-1])
            else:row.append([0])
        M.append(row)
    return det_poly(M)

def connected(n,edges):
    if n==0:return True
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    seen={0};st=[0]
    while st:
        u=st.pop()
        for v in adj[u]:
            if v not in seen:seen.add(v);st.append(v)
    return len(seen)==n

def canon(n,edges):
    E={tuple(sorted(e)) for e in edges};best=None
    pairs=list(combinations(range(n),2))
    for p in permutations(range(n)):
        code=0
        for k,(i,j) in enumerate(pairs):
            if tuple(sorted((p[i],p[j]))) in E:code|=1<<k
        if best is None or code<best:best=code
    return best

def reps(n):
    poss=list(combinations(range(n),2)); d={}
    for mask in range(1<<len(poss)):
        if mask.bit_count()<n-1:continue
        E=[poss[i] for i in range(len(poss)) if mask>>i&1]
        if not connected(n,E):continue
        c=canon(n,E)
        d.setdefault(c,E)
    return list(d.values())

def common_root_in_overlap(pa,ia,pb,ib):
    lo=max(ia[0],ib[0]); hi=min(ia[1],ib[1])
    if lo>hi:return False
    g=pgcd(pa,pb)
    if len(trim(g))<=1:return False
    return roots_between(sturm(g),lo,hi)>=1

def compare_largest_positive_roots(pa,pb,lo,hi):
    ia=largest_root_interval(pa,lo,hi,bits=70)
    ib=largest_root_interval(pb,lo,hi,bits=70)
    if ia[1] < ib[0]: return -1,ia,ib
    if ib[1] < ia[0]: return 1,ia,ib
    if common_root_in_overlap(pa,ia,pb,ib): return 0,ia,ib
    ia=largest_root_interval(pa,lo,hi,bits=140)
    ib=largest_root_interval(pb,lo,hi,bits=140)
    if ia[1] < ib[0]: return -1,ia,ib
    if ib[1] < ia[0]: return 1,ia,ib
    raise AssertionError(('unresolved distinct roots',pa,pb,ia,ib))

def rhoA_data(n,E):
    p=adj_poly(n,E); return p,largest_root_interval(p,0,n,bits=70)

def rhoB_data(n,E):
    m=len(E)
    if m==n-1:return None,(Fraction(0),Fraction(0))
    if m==n:return None,(Fraction(1),Fraction(1))
    p=nb_aux_poly(n,E); return p,largest_root_interval(p,1,n,bits=70)

def cmp_intervals(a,b):
    if a[1] < b[0]: return -1
    if b[1] < a[0]: return 1
    return 0

def compare_metric(data1,data2,lo,hi):
    p1,i1=data1; p2,i2=data2
    c=cmp_intervals(i1,i2)
    if c:return c
    if p1 is None and p2 is None:return 0
    assert p1 is not None and p2 is not None
    c,_,_=compare_largest_positive_roots(p1,p2,lo,hi)
    return c

expected_counts={2:1,3:2,4:6,5:21}
for n in range(2,6):
    R=reps(n); print('n',n,'reps',len(R)); assert len(R)==expected_counts[n]
    by={}
    for E in R:
        m=len(E);by.setdefault(m,[]).append((E,rhoA_data(n,E),rhoB_data(n,E)))
    for m,L in by.items():
        for x,y in combinations(L,2):
            ca=compare_metric(x[1],y[1],0,n)
            cb=compare_metric(x[2],y[2],1,n)
            if ca*cb<0:
                raise AssertionError(('reversal',n,m,x,y))
print('NO_REVERSAL_THROUGH_5')
E1=[(0,1),(0,2),(0,3),(0,4),(0,5),(2,3),(4,5)]
E2=[(0,4),(0,5),(1,3),(1,4),(2,3),(2,4),(3,4)]
A1=rhoA_data(6,E1); B1=rhoB_data(6,E1); A2=rhoA_data(6,E2); B2=rhoB_data(6,E2)
print('witness G',adj_poly(6,E1),nb_aux_poly(6,E1),A1[1],B1[1])
print('witness H',adj_poly(6,E2),nb_aux_poly(6,E2),A2[1],B2[1])
assert compare_metric(A1,A2,0,6)==1
assert compare_metric(B1,B2,1,6)==-1
print('VERIFY_OK')
