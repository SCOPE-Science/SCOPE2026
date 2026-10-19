#!/usr/bin/env python3
"""Independent tests for binary two-string pooled 2-gram profiles.
Only Python standard library. Does not rely on external data."""
from itertools import product, combinations_with_replacement

def vect(word):
    z=[0]*4
    for u,v in zip(word,word[1:]):
        z[u*2+v]+=1
    return tuple(z)

def direct(n):
    words=list(product(range(2),repeat=n))
    profiles=[]
    for word in words:profiles.append(vect(word))
    out=set()
    for i in range(len(words)):
        for j in range(i,len(words)):
            out.add(tuple(profiles[i][v]+profiles[j][v] for v in range(4)))
    return out

def vector_sum(n):
    S={vect(w) for w in product(range(2),repeat=n)}
    return {tuple(x[i]+y[i] for i in range(4)) for x in S for y in S}

def predicted(n):
    L=n-1; T=2*L; profiles=set()
    for b in range(T+1):
        for c in range(T+1-b):
            s=b+c; t=b-c; remainder=T-s
            if t==0 and s==0:
                As={0,L,T}
            elif t==0 and s>=2 and s%2==0:
                As=range(remainder+1)
            elif abs(t)==1 and s>=1 and s%2==1:
                As=range(remainder+1)
            elif abs(t)==2 and s>=2 and s%2==0 and (L%2 or s<=2*L-2):
                As=range(remainder+1)
            else:
                continue
            for a in As:
                profiles.add((a,b,c,remainder-a))
    return profiles

def count_formula(n):
    return 5*n*n-8*n+(6 if n%2==0 else 4)

def main():
    for n in range(2,11):
        A=direct(n)
        B=predicted(n)
        assert A==B,(n,'direct',sorted(A-B)[:4],sorted(B-A)[:4])
        assert len(A)==count_formula(n),(n,len(A),count_formula(n))
        print('direct n=',n,'profile_count=',len(A),'OK')
    for n in range(11,18):
        A=vector_sum(n)
        B=predicted(n)
        assert A==B,(n,'vector',sorted(A-B)[:4],sorted(B-A)[:4])
        assert len(A)==count_formula(n)
        print('vector n=',n,'profile_count=',len(A),'OK')
    for n in range(18,128):
        P=predicted(n)
        assert len(P)==count_formula(n)
    print('THEOREM_BOUNDARY_CHECKS_OK')
if __name__=='__main__':main()
