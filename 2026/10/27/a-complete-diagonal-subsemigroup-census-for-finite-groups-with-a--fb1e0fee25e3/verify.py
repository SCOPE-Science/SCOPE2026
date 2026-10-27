"""Finite checks for reflexive compatible relations on monoids G with a new identity.
Usage: python verify.py. Standard Python 3 only.
"""
from itertools import permutations

def cyclic(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]

def klein():
    return [[i^j for j in range(4)] for i in range(4)]

def symmetric_three():
    ps=list(permutations(range(3)))
    identity=(0,1,2)
    ps.remove(identity); ps.insert(0,identity)
    ind={p:i for i,p in enumerate(ps)}
    return [[ind[tuple(p[q[x]] for x in range(3))] for q in ps] for p in ps]

def add_identity(M):
    n=len(M); t=n
    return [row+[i] for i,row in enumerate(M)]+[list(range(n+1))]

def inverse(M,i):
    for j in range(len(M)):
        if M[i][j]==0 and M[j][i]==0:return j
    raise ValueError('non-group')

def subgroups(M):
    n=len(M); answer=[]
    for mask in range(1,1<<n,2):
        A={i for i in range(n) if mask>>i&1}
        if all(M[i][j] in A for i in A for j in A):answer.append(frozenset(A))
    return answer

def normals(M, subs):
    n=len(M)
    return [N for N in subs if all(M[M[g][x]][inverse(M,g)] in N for g in range(n) for x in N)]

def predicted(M):
    subs=subgroups(M); normals_=normals(M,subs)
    counts=[1+sum(H<=N for H in subs) for N in normals_]
    d=sum(v*v for v in counts)
    t=sum(counts)
    c=2*len(normals_)
    return d,t,c,normals_,subs

def brute(M):
    S=add_identity(M); n=len(S)
    pairs=[(i,j) for i in range(n) for j in range(n)]
    diagmask=sum(1<<(i*n+i) for i in range(n))
    others=[i for i,(a,b) in enumerate(pairs) if a!=b]
    required=[]
    for idx in others:
        a,b=pairs[idx]
        forced=1<<idx
        for g in range(n):
            forced|=1<<(S[a][g]*n+S[b][g])
            forced|=1<<(S[g][a]*n+S[g][b])
        required.append(forced)
    D=T=C=0
    for num in range(1<<len(others)):
        mask=diagmask
        for k,idx in enumerate(others):
            if num>>k&1:mask|=1<<idx
        if any(num>>k&1 and (mask&req)!=req for k,req in enumerate(required)):continue
        present=[(a,b) for i,(a,b) in enumerate(pairs) if mask>>i&1]
        if any(not (mask>>(S[a][c]*n+S[b][d])&1) for a,b in present for c,d in present):continue
        D+=1
        symmetric=all((mask>>(b*n+a))&1 for a,b in present)
        if symmetric:T+=1
        transitive=symmetric and all((mask>>(a*n+c))&1 for a,b in present for b2,c in present if b==b2)
        if transitive:C+=1
    return D,T,C

def all_normal_forms_closed(M):
    S=add_identity(M); n=len(M); D,T,C,Ns,subs=predicted(M)
    seen=set(); congruences=0; symmetries=0; triples=[]
    for N in Ns:
        fam=[None]+[H for H in subs if H<=N]
        for A in fam:
            for B in fam:
                R={(i,j) for i in range(n) for j in range(n) if M[i][inverse(M,j)] in N}
                R.add((n,n))
                if A is not None:R|={(n,a) for a in A}
                if B is not None:R|={(b,n) for b in B}
                assert all((S[a][c],S[b][d]) in R for a,b in R for c,d in R)
                frozen=frozenset(R);assert frozen not in seen
                seen.add(frozen)
                triples.append((N,A,B,frozen))
                sym=all((b,a) in R for a,b in R)
                if sym:symmetries+=1
                if sym and all((a,c) in R for a,b in R for b2,c in R if b==b2):congruences+=1
    assert len(seen)==D and symmetries==T and congruences==C
    for N,A,B,R in triples:
        for NN,AA,BB,RR in triples:
            poset=N<=NN and (A is None or (AA is not None and A<=AA)) and (B is None or (BB is not None and B<=BB))
            assert (R<=RR)==poset
    return D,T,C

if __name__=='__main__':
    for label,M in [('C1',cyclic(1)),('C2',cyclic(2)),('C3',cyclic(3)),('C4',cyclic(4)),('V4',klein()),('S3',symmetric_three())]:
        expected=predicted(M)[:3]
        forms=all_normal_forms_closed(M)
        assert forms==expected
        if len(M)<=4:
            actual=brute(M)
            assert actual==expected,(label,actual,expected)
            print(label,'direct_exhaustive',actual,'normal_forms',forms)
        else:
            print(label,'all_normal_forms_checked',forms)
    print('VERIFY_OK')
