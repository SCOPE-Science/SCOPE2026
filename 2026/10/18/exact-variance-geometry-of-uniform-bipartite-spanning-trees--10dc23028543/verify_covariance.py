"""Exact small-order checks for covariance geometry of random bipartite spanning trees.

Run: python verify_bipartite_tree_covariance.py
No external dependencies. Finite checks supplement, rather than replace, the proof.
"""
from fractions import Fraction as F
from itertools import combinations


def all_trees(a, b):
    E = [(i, j) for i in range(a) for j in range(b)]
    for chosen in combinations(range(a*b), a+b-1):
        parent = list(range(a+b))
        def root(k):
            while parent[k] != k:
                k = parent[k]
            return k
        for e in chosen:
            i, j = E[e]
            x, y = root(i), root(a+j)
            parent[x] = y
        if len({root(k) for k in range(a+b)}) == 1:
            yield chosen


def projectors(a, b):
    edges = [(i,j) for i in range(a) for j in range(b)]
    z = len(edges)
    I = lambda e,f: F(int(e==f))
    P0 = [[F(1,a*b) for _ in edges] for _ in edges]
    Pr = [[(F(int(i==k))-F(1,a))/b for k,l in edges] for i,j in edges]
    Pc = [[(F(int(j==l))-F(1,b))/a for k,l in edges] for i,j in edges]
    Ph = [[I(e,f)-P0[e][f]-Pr[e][f]-Pc[e][f] for f in range(z)] for e in range(z)]
    return edges,P0,Pr,Pc,Ph


def covariance_formula(a, b):
    edges,P0,Pr,Pc,Ph=projectors(a,b)
    lr,lc,lh=F(b-1,a*b),F(a-1,a*b),F(a+b-3,a*b)
    z=len(edges)
    return [[lr*Pr[e][f]+lc*Pc[e][f]+lh*Ph[e][f] for f in range(z)] for e in range(z)]


def exact_test(a,b):
    edges,P0,Pr,Pc,Ph=projectors(a,b)
    z=len(edges)
    trees=list(all_trees(a,b))
    assert len(trees)==a**(b-1)*b**(a-1), (a,b,len(trees))
    m=len(trees)
    S=[0]*z
    S2=[[0]*z for _ in range(z)]
    for t in trees:
        for e in t:
            S[e]+=1
            for f in t: S2[e][f]+=1
    actual=[[F(S2[e][f],m)-F(S[e]*S[f],m*m) for f in range(z)] for e in range(z)]
    predicted=covariance_formula(a,b)
    for e in range(z):
        assert F(S[e],m)==F(a+b-1,a*b)
        for f in range(z): assert actual[e][f]==predicted[e][f], (a,b,e,f,actual[e][f],predicted[e][f])
    # Independent orthogonal projectors and spectral decomposition
    P=[P0,Pr,Pc,Ph]
    for s in range(4):
        for t in range(4):
            for i in range(z):
                for j in range(z):
                    v=sum(P[s][i][k]*P[t][k][j] for k in range(z))
                    assert v==(P[s][i][j] if s==t else 0)
    eig=[F(0),F(b-1,a*b),F(a-1,a*b),F(a+b-3,a*b)]
    for idx in range(4):
        for i in range(z):
            for j in range(z):
                assert sum(actual[i][k]*P[idx][k][j] for k in range(z))==eig[idx]*P[idx][i][j]
    # Independently compute variance from all trees of a nonadditive edge cost.
    w=[F(4+3*i-j+2*i*j+(-1)**(i+j)*j*j,7) for i,j in edges]
    cost=[sum(w[e] for e in t) for t in trees]
    av=sum(cost,F(0))/m
    exact=sum((v-av)**2 for v in cost)/m
    spectral=sum(w[i]*actual[i][j]*w[j] for i in range(z) for j in range(z))
    assert exact==spectral
    return len(trees),z*z,4*z*z


def main():
    tested=[(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]
    trees=entries=operator_checks=0
    for a,b in tested:
        t,e,o=exact_test(a,b)
        trees+=t;entries+=e;operator_checks+=o
        print(f'K_{{{a},{b}}}: {t} trees; {e} exact covariance entries; 4 orthogonal projectors checked')
    print('PASS:',trees,'exact spanning trees;',entries,'covariance-entry comparisons; ',operator_checks,'projection/eigenvalue comparisons')

if __name__=='__main__': main()
