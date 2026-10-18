"""Exact finite-field Kalman-rank checks for a single exceptional bipartite edge.

Pure Python, no external dependencies. A full modular rank certifies full rational rank.
We also compare the full rank truth table at the chosen primes to the theorem.
"""
from itertools import product
from collections import Counter

PRIMES=(1000003,1000033)

def rank_mod(vectors,N,P):
    basis={}
    for vec in vectors:
        v=[x%P for x in vec]
        for i,base in sorted(basis.items()):
            if v[i]:
                factor=v[i]
                v=[(u-factor*w)%P for u,w in zip(v,base)]
        pos=next((i for i,a in enumerate(v) if a),None)
        if pos is None:continue
        inv=pow(v[pos],-1,P)
        basis[pos]=[(a*inv)%P for a in v]
        if len(basis)==N:return N
    return len(basis)

def check(p,q,c_num,c_den,P):
    N=p+q
    L=[[0]*N for i in range(N)]
    den_inv=pow(c_den,-1,P)
    weight=(c_num*den_inv)%P
    for i in range(p):
        for j in range(q):
            v=p+j
            w=weight if (i,j)==(0,0) else 1
            L[i][i]=(L[i][i]+w)%P
            L[v][v]=(L[v][v]+w)%P
            L[i][v]=(L[i][v]-w)%P
            L[v][i]=(L[v][i]-w)%P
    ncheck=0
    counts=Counter()
    for mask in range(1<<N):
        S=[i for i in range(N) if mask>>i&1]
        cols=[]
        for i in S:
            v=[int(j==i) for j in range(N)]
            for k in range(N):
                cols.append(v)
                v=[sum(L[r][t]*v[t] for t in range(N))%P for r in range(N)]
        actual=(rank_mod(cols,N,P)==N)
        aa=sum(i in S for i in range(1,p))
        bb=sum(p+j in S for j in range(1,q))
        if c_num==c_den:
            expected=(sum(i in S for i in range(p))>=p-1 and sum(p+j in S for j in range(q))>=q-1)
        elif p==q:
            expected=(aa>=p-2 and bb>=q-2 and len(S)>=N-3)
        else:
            expected=(aa>=p-2 and bb>=q-2)
        assert actual==expected,(p,q,c_num,c_den,P,mask,S,actual,expected)
        if actual:counts[len(S)]+=1
        ncheck+=1
    return ncheck,counts

if __name__=='__main__':
    checks=0
    for p,q in [(3,3),(3,4),(4,4),(4,5),(5,5)]:
        for num,den in [(0,1),(1,2),(1,1),(2,1),(5,2)]:
            x=check(p,q,num,den,PRIMES[0]);y=check(p,q,num,den,PRIMES[1]);assert x==y
            checks+=2*x[0]
            print('OK',p,q,num,den,'min:',min(x[1]),'placements:',x[1][min(x[1])])
    print('VERIFY_OK',checks,'individual truth-table entries over two primes')
