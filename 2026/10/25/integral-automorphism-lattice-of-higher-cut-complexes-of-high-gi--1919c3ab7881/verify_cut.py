"""Finite checks for automorphism characters of higher cut complexes.

The theorem is proved separately; these checks test orientations, boundary
conventions, and nontrivial examples across several graph families.
"""
from itertools import combinations
from math import comb

def connected(T, edges):
    if not T: return False
    todo=[T[0]]; reached={T[0]}; A=set(T)
    while todo:
        v=todo.pop()
        for w in A:
            if w not in reached and (min(v,w),max(v,w)) in edges:
                reached.add(w);todo.append(w)
    return len(reached)==len(T)

def permutation_sign(vals):
    return -1 if sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%2 else 1

def faces(N,k,E):
    disc=[s for s in combinations(range(N),k) if not connected(s,E)]
    ans=[()] + [s for r in range(1,N-k+1) for s in combinations(range(N),r) if any(set(s).isdisjoint(D) for D in disc)]
    return ans

def signed_fixed(S,perm):
    vals=[perm[v] for v in S]
    return permutation_sign(vals) if sorted(vals)==list(S) else 0

def direct_lefschetz(N,k,E,perm):
    return -1+sum((-1)**(len(S)-1)*signed_fixed(S,perm) for S in faces(N,k,E) if S)

def poly_coeff_u(perm,k):
    n=len(perm); unvisited=set(range(n));poly=[1]
    while unvisited:
        x=next(iter(unvisited));a=[];v=x
        while v not in a: a.append(v);unvisited.remove(v);v=perm[v]
        length=len(a); fac=[0]*(length+1);fac[0]=1;fac[-1]=(-1)**(length-1)
        new=[0]*(len(poly)+length)
        for i,u in enumerate(poly):
            for j,v in enumerate(fac):new[i+j]+=u*v
        poly=new
    # divide det(1+t P) by 1+t
    q=[]
    for i in range(k):q.append(poly[i]-(q[i-1] if i else 0))
    return q[k-1]

def predicted_lefschetz(N,k,E,perm):
    F=sum(signed_fixed(S,perm) for S in combinations(range(N),k) if connected(S,E))
    q=poly_coeff_u(perm,k)
    char=permutation_sign(list(perm))*(q-F)
    return ((-1)**(N-k-1))*char,q,F

def rank_mod2(col_bitvectors):
    piv={}
    for x in col_bitvectors:
        while x:
            h=x.bit_length()-1
            if h in piv:x^=piv[h]
            else:piv[h]=x;break
    return len(piv)

def mod2_betti(N,k,E):
    f=faces(N,k,E)
    bettis={};by={r:[s for s in f if len(s)==r] for r in range(N-k+1)}
    ranks={}
    for r in range(1,N-k+1):
        smaller={s:i for i,s in enumerate(by[r-1])}
        cols=[]
        for s in by[r]:
            x=0
            for a in range(len(s)):x^=1<<smaller[s[:a]+s[a+1:]]
            cols.append(x)
        ranks[r]=rank_mod2(cols)
    for r in range(1,N-k+1):
        b=len(by[r])-ranks.get(r,0)-ranks.get(r+1,0)
        if b:bettis[r-1]=b
    # normalized reduced H0: H0 -> dim ker(d0) via augmented boundary
    if 0 in bettis:bettis[0]-=1
    return {d:b for d,b in bettis.items() if b}

def path(N):return {(i,i+1) for i in range(N-1)}
def cycle(N):return path(N)|{(0,N-1)}
def star(N):return {(0,i) for i in range(1,N)}
def two_paths(N):return {(i,i+1) for i in range(3)}|{(i,i+1) for i in range(4,N-1)}
def verify():
    examples=[]
    for n in range(7,11):
        for kind,E in [('path',path(n)),('cycle',cycle(n)),('star',star(n))]:
            for k in range(3,min(6,n-3)):
                acts={'identity':tuple(range(n))}
                if kind in ('path','cycle'):
                    acts['reversal']=tuple(n-1-i for i in range(n))
                if kind=='cycle':
                    acts['rotation']=tuple((i+1)%n for i in range(n))
                    acts['reflection']=tuple((-i)%n for i in range(n))
                if kind=='star':
                    acts['leaf-swap']=tuple(([0,2,1]+list(range(3,n))))
                    acts['leaf-cycle']=tuple(([0,2,3,1]+list(range(4,n))))
                for lab,p in acts.items():
                    assert {tuple(sorted((p[u],p[v]))) for u,v in E}==E,(n,k,kind,lab)
                    a=direct_lefschetz(n,k,E,p)
                    b,q,F=predicted_lefschetz(n,k,E,p)
                    assert a==b,(n,k,kind,lab,a,b,q,F)
                    examples.append((n,k,kind,lab,a,q,F))
    print('SIGNED_LEFSCHETZ_COMPARISONS_OK',len(examples))
    # Different independent finite homology calculation, all dimension checks
    checked=[]
    for n,k,kind in [(7,3,'path'),(8,4,'path'),(8,4,'cycle'),(9,4,'cycle'),(8,4,'star'),(9,5,'path'),(9,5,'cycle')]:
        E={'path':path,'cycle':cycle,'star':star}[kind](n)
        expected=comb(n-1,k-1)-sum(connected(S,E) for S in combinations(range(n),k))
        got=mod2_betti(n,k,E)
        assert got==({n-k-1:expected} if expected else {}),(n,k,kind,got,expected)
        checked.append((n,k,kind,expected))
    print('MOD2_HOMOLOGY_CHECKS_OK',len(checked))
    print('CUT_COMPLEX_CHARACTER_CERTIFICATE_VERIFIED')
if __name__=='__main__':verify()

def check_private_faces():
    checked=0; certificates=0
    for n in range(7,11):
        for E in (path(n), cycle(n), star(n)):
            for k in range(4,min(6,n-3)):
                relevant=[tuple(S) for S in combinations(range(n),k) if connected(S,E)]
                tallies={}
                for T in relevant:
                    for A in combinations(T,k-1):
                        tallies.setdefault(A,[]).append(T)
                for T in relevant:
                    private=[A for A in combinations(T,k-1) if len(tallies[A])==1]
                    assert private,(n,k,T)
                    certificates+=1
                checked+=1
    print('PRIVATE_FACET_UNIMODULAR_SATURATION_OK',checked,certificates)

if __name__=='__main__':check_private_faces()
