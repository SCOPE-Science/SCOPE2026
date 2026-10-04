#!/usr/bin/env python3
from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter

def matrix_and_outsets(n,bits):
    pairs=list(combinations(range(n),2))
    A=[[0]*n for _ in range(n)]
    out=[set() for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (bits>>k)&1:
            A[i][j]=1; A[j][i]=-1; out[i].add(j)
        else:
            A[i][j]=-1; A[j][i]=1; out[j].add(i)
    return A,out

def solve_unique(eqs, rhs, nvar):
    M=[list(map(Fraction,row))+[Fraction(b)] for row,b in zip(eqs,rhs)]
    r=0
    piv=[]
    for c in range(nvar):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None:
            continue
        M[r],M[p]=M[p],M[r]
        z=M[r][c]
        M[r]=[x/z for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                z=M[i][c]
                M[i]=[M[i][j]-z*M[r][j] for j in range(nvar+1)]
        piv.append(c)
        r+=1
    for row in M:
        if all(row[c]==0 for c in range(nvar)) and row[nvar]!=0:
            return None
    if len(piv)!=nvar:
        return None
    x=[Fraction(0)]*nvar
    for i,c in enumerate(piv):
        x[c]=M[i][nvar]
    return tuple(x)

def maximal_lottery_gauss(n,bits):
    A,_=matrix_and_outsets(n,bits)
    for r in range(1,n+1):
        for S in combinations(range(n),r):
            eqs=[]; rhs=[]
            for i in S:
                eqs.append([A[i][j] for j in S]); rhs.append(0)
            eqs.append([1]*r); rhs.append(1)
            x=solve_unique(eqs,rhs,r)
            if x is None or not all(z>0 for z in x):
                continue
            p=[Fraction(0)]*n
            for i,z in zip(S,x): p[i]=z
            vals=[sum(p[i]*A[i][j] for i in range(n)) for j in range(n)]
            if all(v>=0 for v in vals) and all(vals[j]==0 for j in S):
                return frozenset(S),tuple(p),tuple(vals)
    raise AssertionError("no maximal lottery")

def pfaffian(M):
    n=len(M)
    if n==0: return Fraction(1)
    assert n%2==0
    total=Fraction(0)
    for j in range(1,n):
        sub=[[M[a][b] for b in range(n) if b not in (0,j)]
             for a in range(n) if a not in (0,j)]
        total += ((-1)**(j+1))*M[0][j]*pfaffian(sub)
    return total

def maximal_lottery_pfaffian(n,bits):
    A,_=matrix_and_outsets(n,bits)
    for r in range(1,n+1,2):
        for S in combinations(range(n),r):
            if r==1:
                vals=[Fraction(1)]
            else:
                B=[[Fraction(A[i][j]) for j in S] for i in S]
                vals=[]
                for k in range(r):
                    minor=[[B[i][j] for j in range(r) if j!=k]
                           for i in range(r) if i!=k]
                    vals.append(((-1)**k)*pfaffian(minor))
                if all(z<0 for z in vals):
                    vals=[-z for z in vals]
                if not all(z>0 for z in vals):
                    continue
                s=sum(vals)
                vals=[z/s for z in vals]
            p=[Fraction(0)]*n
            for i,z in zip(S,vals): p[i]=z
            pay=[sum(p[i]*A[i][j] for i in range(n)) for j in range(n)]
            if all(v>=0 for v in pay) and all(pay[j]==0 for j in S):
                return frozenset(S),tuple(p),tuple(pay)
    raise AssertionError("no pfaffian maximal lottery")

def uncovered_cover(n,bits):
    _,out=matrix_and_outsets(n,bits)
    U=set()
    for x in range(n):
        if not any(y!=x and x in out[y] and out[x] <= out[y] for y in range(n)):
            U.add(x)
    return frozenset(U)

def uncovered_two_step(n,bits):
    _,out=matrix_and_outsets(n,bits)
    U=set()
    for x in range(n):
        reach={x}|out[x]
        for y in out[x]:
            reach |= out[y]
        if len(reach)==n:
            U.add(x)
    return frozenset(U)

def permute_bits(n,bits,p):
    pairs=list(combinations(range(n),2))
    idx={e:k for k,e in enumerate(pairs)}
    out=0
    for k,(i,j) in enumerate(pairs):
        w=i if (bits>>k)&1 else j
        l=j if w==i else i
        W,L=p[w],p[l]
        a,b=sorted((W,L))
        if W==a:
            out |= 1<<idx[(a,b)]
    return out

def canonical(n,bits):
    return min(permute_bits(n,bits,p) for p in permutations(range(n)))

hist={}
diff_counts={}
classes=Counter()

for n in range(1,6):
    H=Counter()
    total=1<<(n*(n-1)//2)
    diff=0
    for bits in range(total):
        B1,p1,v1=maximal_lottery_gauss(n,bits)
        B2,p2,v2=maximal_lottery_pfaffian(n,bits)
        assert (B1,p1,v1)==(B2,p2,v2)
        U1=uncovered_cover(n,bits)
        U2=uncovered_two_step(n,bits)
        assert U1==U2
        assert B1 <= U1
        H[(len(B1),len(U1),B1==U1)] += 1
        if B1!=U1:
            diff+=1
            if n==5:
                classes[canonical(n,bits)] += 1
    hist[n]=H
    diff_counts[n]=diff

assert diff_counts == {1:0,2:0,3:0,4:0,5:120}
assert hist[4] == Counter({(1,1,True):32,(3,3,True):32})
assert hist[5] == Counter({
    (3,3,True):520,
    (1,1,True):320,
    (3,4,False):120,
    (5,5,True):64,
})
assert classes == Counter({41:120})

B,p,pay=maximal_lottery_gauss(5,41)
U=uncovered_cover(5,41)
assert B==frozenset({0,3,4})
assert U==frozenset({0,2,3,4})
assert p==(Fraction(1,3),0,0,Fraction(1,3),Fraction(1,3))
assert pay==(0,Fraction(1,3),Fraction(1,3),0,0)

print("VERIFY_OK")
for n in range(1,6):
    print("n",n,"total",1<<(n*(n-1)//2),"diff",diff_counts[n],"hist",dict(hist[n]))
print("n5_probability","120/1024 = 15/128")
print("n5_classes",dict(classes))
print("canonical_bits",41)
print("canonical_BP",sorted(B))
print("canonical_UC",sorted(U))
print("canonical_lottery",p)
print("canonical_expected_payoffs",pay)
