#!/usr/bin/env python3
"""Exact finite-field checks of two-point complete-bipartite configuration homology.

The mathematical result applies to all m,n >= 3 by a characteristic-zero
representation-ring argument; these computations test cells, boundaries,
finite cases, and actual (not virtual) actions on degree-two cycles.
"""
from itertools import combinations, permutations
from math import comb

P=1009

def rank_and_kernel(columns, rows, p=P):
    piv={};kernel=[]
    for j,col in enumerate(columns):
        y={i:a%p for i,a in col.items() if a%p}
        z={j:1}
        while y:
            i=max(y)
            if i not in piv:
                t=pow(y[i],-1,p)
                piv[i]=({k:(v*t)%p for k,v in y.items()},
                        {k:(v*t)%p for k,v in z.items()})
                break
            coef=y[i]
            b,u=piv[i]
            for k,v in b.items():
                nv=(y.get(k,0)-coef*v)%p
                if nv:y[k]=nv
                else:y.pop(k,None)
            for k,v in u.items():
                nv=(z.get(k,0)-coef*v)%p
                if nv:z[k]=nv
                else:z.pop(k,None)
        else:
            assert z.get(j)==1
            kernel.append((j,z))
    return len(piv),kernel

def setup(m,n):
    V=range(m+n)
    E=list((a,m+b) for a in range(m) for b in range(n))
    C0=list(combinations(V,2)); D0={c:i for i,c in enumerate(C0)}
    C1=[(e,v) for e in E for v in V if v not in e]
    D1={c:i for i,c in enumerate(C1)}
    C2=[(e,f) for e,f in combinations(E,2) if len(set(e+f))==4]
    D2={c:i for i,c in enumerate(C2)}
    B1=[]
    for (a,b),v in C1:
        B1.append({D0[tuple(sorted((b,v)))]:1,D0[tuple(sorted((a,v)))]:-1})
    B2=[]
    for (a,b),(c,d) in C2:
        B2.append({D1[((c,d),b)]:1,D1[((c,d),a)]:-1,
                   D1[((a,b),d)]:-1,D1[((a,b),c)]:1})
    # boundary square check (mod p) for every two-cell
    for column in B2:
        chk={}
        for i,a in column.items():
            for j,b in B1[i].items():chk[j]=chk.get(j,0)+a*b
        assert all(a==0 for a in chk.values())
    return C0,C1,C2,B1,B2,D2

def wchi(perm):
    f=sum(i==v for i,v in enumerate(perm))
    t=sum(i<j and perm[i]==j and perm[j]==i for i in range(len(perm)) for j in range(i+1,len(perm)))
    return comb(f,2)+t-f

def xchi(perm):
    f=sum(i==v for i,v in enumerate(perm))
    t=sum(i<j and perm[i]==j and perm[j]==i for i in range(len(perm)) for j in range(i+1,len(perm)))
    return comb(f,2)-t-f+1

def vertex_action(m,n,p,q,swap):
    if not swap:return {**{i:p[i] for i in range(m)},**{m+j:m+q[j] for j in range(n)}}
    assert m==n
    return {**{i:m+q[i] for i in range(m)},**{m+j:p[j] for j in range(n)}}

def char_direct(m,n,C2,D2,kernel,p,q,swap):
    perm=vertex_action(m,n,p,q,swap)
    tr=0
    for j,z in kernel:
        for i,a in z.items():
            e,f=C2[i]
            e1=tuple(sorted((perm[e[0]],perm[e[1]])))
            e2=tuple(sorted((perm[f[0]],perm[f[1]])))
            if e1<e2: dest=D2[(e1,e2)];sgn=1
            else:dest=D2[(e2,e1)];sgn=-1
            if dest==j:tr=(tr+sgn*a)%P
    return tr

def test(m,n,full=False):
    C0,C1,C2,B1,B2,D2=setup(m,n)
    r0,z0=rank_and_kernel(B1,len(C0));r1,z1=rank_and_kernel(B2,len(C1))
    assert r0==len(C0)-1
    assert len(z0)==len(C1)-r0
    assert len(z1)==len(C2)-r1
    W=lambda z:z*(z-3)//2 if z>=4 else 0
    X=lambda z:(z-1)*(z-2)//2
    expect=W(m)*X(n)+X(m)*W(n)
    assert len(z0)-r1==(m-1)*(n-1)
    assert len(z1)==expect
    checks=0
    if full:
        for p in permutations(range(m)):
            for q in permutations(range(n)):
                expected=wchi(p)*xchi(q)+xchi(p)*wchi(q)
                got=char_direct(m,n,C2,D2,z1,p,q,False)
                assert got==expected%P,(m,n,p,q,False,got,expected)
                checks+=1
                if m==n:
                    got=char_direct(m,n,C2,D2,z1,p,q,True)
                    assert got==0,(m,n,p,q,True,got)
                    checks+=1
    print(f'K_{m},{n}: cells=({len(C0)},{len(C1)},{len(C2)}), '
          f'boundary ranks=({r0},{r1}), rational-expected betti=(1,{(m-1)*(n-1)},{expect}), '
          f'full signed kernel-character tests={checks}',flush=True)
    return checks

if __name__=='__main__':
    total=0
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)]:
        total+=test(m,n,full=(m,n) in {(3,3),(3,4),(4,4),(4,5)})
    print('PASS; direct signed cellular actions and finite-field kernel traces:',total,flush=True)
