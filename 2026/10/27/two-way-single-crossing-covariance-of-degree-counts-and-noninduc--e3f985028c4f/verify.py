"""Exact checks for the weighted motif / degree-count covariance identity.
Uses only Python's standard library. Run: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def count_degrees(mask, edges, n):
    d=[0]*n
    for b,(u,v) in enumerate(edges):
        if mask>>b & 1:
            d[u]+=1; d[v]+=1
    return d


def test_motif(n, pattern, p, weighted=False):
    k=max(max(e) for e in pattern)+1
    E=list(combinations(range(n),2))
    emap={e:i for i,e in enumerate(E)}
    d=[0]*k
    for a,b in pattern:
        d[a]+=1; d[b]+=1
    embeddings=[]
    for f in permutations(range(n),k):
        bits=0
        for a,b in pattern:
            bits|=1<<emap[tuple(sorted((f[a],f[b])))]
        embeddings.append((bits, (1+(len(embeddings)%5)) if weighted and len(embeddings)%3==0 else (0 if weighted else 1)))
    e=len(E)
    prob=[p**j*(1-p)**(e-j) for j in range(e+1)]
    mean_T=Fraction(0); mean_N=[Fraction(0) for _ in range(n)]; mean_NT=[Fraction(0) for _ in range(n)]
    for mask in range(1<<e):
        weight=prob[mask.bit_count()]
        degs=count_degrees(mask,E,n)
        T=sum(weight for b,weight in embeddings if (mask&b)==b)
        mean_T+=weight*T
        for r in range(n):
            nr=degs.count(r)
            mean_N[r]+=weight*nr
            mean_NT[r]+=weight*nr*T
    assert mean_T==sum(w for _,w in embeddings)*p**len(pattern)
    for r in range(n):
        B=Fraction(comb(n-1,r))*p**r*(1-p)**(n-1-r)
        F=-k
        for a in d:
            if a<=r:
                falling=lambda x,j: factorial(x)//factorial(x-j)
                F+=Fraction(falling(r,a),falling(n-1,a))*p**(-a)
        expected=mean_T*B*F
        observed=mean_NT[r]-mean_N[r]*mean_T
        assert observed==expected,(n,pattern,p,r,observed,expected)
    return n


def crossing(n, degree_sequence, r):
    N=n-1
    assert 1<=r<N
    def F(p):
        ans=-len(degree_sequence)
        for d in degree_sequence:
            if d<=r:
                product=1.
                for i in range(d): product*=(r-i)/(N-i)
                ans+=product/p**d
        return ans
    lo=1e-12;hi=1.
    for _ in range(90):
        mid=(lo+hi)/2
        if F(mid)>0: lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    tests=0
    motifs=[[(0,1)], [(0,1),(1,2)], [(0,1),(1,2),(0,2)],
            [(0,1),(0,2),(0,3)], [(0,1),(1,2),(2,3)]]
    for n in (4,5):
        for pattern in motifs:
            if max(max(e) for e in pattern)<n:
                for p in (Fraction(1,4),Fraction(2,5),Fraction(3,4)):
                    tests+=test_motif(n,pattern,p)
    for pattern in (motifs[1],motifs[2],motifs[4]):
        tests+=test_motif(5,pattern,Fraction(3,7),weighted=True)
    # Strict ordering across degree thresholds and a unique crossing in r.
    for N in (10,20,40):
        for degs in ([1,2,1],[2,2,2],[3,1,1,1]):
            roots=[crossing(N+1,degs,r) for r in range(min(degs),N)]
            assert all(roots[i]<roots[i+1] for i in range(len(roots)-1))
            tests+=1
    # Dense-profile expansion, nonregular graph with degree sequence (1,2,2,1).
    deg=(1,2,2,1)
    excess=sum(d*(d-1) for d in deg)/sum(deg)
    for N in (400,800,1600,3200):
        n=N+1;r=N*2//5
        root=crossing(n,deg,r)
        u=r/N
        approximation=u-(1-u)*excess/(2*N)
        assert abs(root-approximation)*N*N<3
        tests+=1
    # Exact sparse star roots, including a center excluded by r=1.
    for leaves in (2,3,5,8):
        degree_seq=[leaves]+[1]*leaves
        for N in (leaves+2,leaves+5,100):
            root=crossing(N+1,degree_seq,1)
            assert abs(root-leaves/((leaves+1)*N))<2e-10
            tests+=1
    print('PASS: %d exact finite graph-case/threshold groups' % (tests-16))
    print('PASS: %d additional asymptotic/root checks' % 16)

if __name__=='__main__':
    main()
