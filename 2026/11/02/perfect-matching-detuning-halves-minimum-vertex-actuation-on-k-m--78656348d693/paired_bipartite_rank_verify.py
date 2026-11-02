"""Exact modular tests for paired-bipartite controllability ranks.
Finite checks corroborate but do not establish the all-size proof.
"""
from fractions import Fraction
from itertools import combinations
import random
P=1000003

def rank(columns,n):
    piv={}
    for src in columns:
        v=src[:]
        while True:
            k=next((j for j,x in enumerate(v) if x%P),None)
            if k is None:break
            if k in piv:
                a=v[k]; w=piv[k]
                v=[(x-a*y)%P for x,y in zip(v,w)]
            else:
                inv=pow(v[k],-1,P)
                piv[k]=[x*inv%P for x in v]
                break
    return len(piv)

def kalman(m,t,S):
    n=2*m; a=t.numerator*pow(t.denominator,-1,P)%P
    L=[[0]*n for _ in range(n)]
    for i in range(n):
        L[i][i]=(m-1+a)%P
    for i in range(m):
        for j in range(m):
            b=a if i==j else 1
            L[i][m+j]=L[m+j][i]=-b%P
    cur=[[int(i==j) for i in range(n)] for j in S]; cols=[]
    for _ in range(n):
        cols.extend(cur)
        cur=[[sum(L[i][j]*v[j] for j in range(n))%P for i in range(n)] for v in cur]
    return rank(cols,n)

def formula(m,t,S):
    if not S:return 0
    a={i for i in S if i<m}; b={i-m for i in S if i>=m}
    return (2+min(len(a),m-1)+min(len(b),m-1)) if t==1 else (2+2*min(len(a|b),m-1))

def main():
    rng=random.Random(20261029); count=0
    for m in range(2,5):
        for t in map(Fraction,['1','1/2','3/2','4/3','2']):
            for k in range(1,2*m+1):
                for S in combinations(range(2*m),k):
                    got=kalman(m,t,S);want=formula(m,t,S)
                    assert got==want,(m,t,S,got,want)
                    count+=1
    for m in range(5,9):
        for t in map(Fraction,['1','1/2','3/2','4/3','2']):
            cases={tuple(range(m-1)),tuple(range(m,2*m-1)),tuple(range(2*m)),(0,)}
            for j in range(40):cases.add(tuple(sorted(rng.sample(range(2*m),rng.randint(1,2*m)))))
            for S in cases:
                got=kalman(m,t,S);want=formula(m,t,S)
                assert got==want,(m,t,S,got,want)
                count+=1
    print('PASS',count,'exact finite-field Kalman rank comparisons; modulus',P)
if __name__=='__main__':main()
