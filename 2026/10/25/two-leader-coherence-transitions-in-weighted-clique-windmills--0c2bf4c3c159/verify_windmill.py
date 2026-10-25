"""Exact reproducibility checks for weighted clique-windmill two-leader coherence.

Requires SymPy (see requirements.txt). This finite verification supplements,
but cannot replace, the symbolic universal proof in RESULT.md.
"""
from itertools import combinations
from sympy import Matrix, Rational, S, symbols, simplify, factor

r, s, b = symbols('r s b', positive=True)
alpha = (1+b)/(1+s*b)
beta = 2/(1+s*b)

def phi(x,y,z):
    return (x+y)/2-z/4-(x-y)**2/(4*z)

A = factor((s-1)*phi(alpha,beta,alpha)+(r-1)*s*phi(alpha,2*alpha,alpha))
B = factor((s-2)*phi(beta,beta,beta)+phi(alpha,alpha,beta)
           +(r-1)*s*phi(2*alpha,2*alpha,beta))
C = factor(phi(alpha,alpha,2*alpha)
           +2*(s-1)*phi(beta,2*alpha,2*alpha)
           +(r-2)*s*phi(2*alpha,2*alpha,2*alpha))
A0 = ((r*s-1)*(1+2*b)+s*(r-1)*b*b)/((1+b)*(1+s*b))
Dca = (r*s-3+b*(s*(r-4)+1))/(2*(1+s*b))
Dbc = b*(b*r*s+2*b*s+b+r*s+3)/(2*(1+b)*(1+s*b))
for expr in [A-A0,C-A-Dca,B-C-Dbc]:
    assert simplify(expr)==0
assert simplify(Dca.subs(r,3)-(s-1)*(3-b)/(2*(1+s*b)))==0
assert simplify(Dca.subs(r,2)-(2*s-3-(2*s-1)*b)/(2*(1+s*b)))==0


def laplacian(n_petals,petal_size,weight):
    n=1+n_petals*petal_size
    L=Matrix.zeros(n)
    edges=[]
    for j in range(n_petals):
        block=list(range(1+j*petal_size,1+(j+1)*petal_size))
        edges.extend((0,x,S.One) for x in block)
        edges.extend((u,v,weight) for u,v in combinations(block,2))
    for u,v,w in edges:
        L[u,u]+=w;L[v,v]+=w
        L[u,v]-=w;L[v,u]-=w
    return L


def cost(L, pair):
    F=[i for i in range(L.rows) if i not in pair]
    Q=L.extract(F,F)
    inv=Q.inv()
    return sum(inv[i,i] for i in range(len(F)))

representatives=0
all_pairs=0
for R in range(2,5):
    for S_ in range(2,4):
        for B_ in [Rational(1,5),Rational(1,3),S.One,Rational(3),Rational(5)]:
            L=laplacian(R,S_,B_)
            vals=[cost(L, pair) for pair in [(0,1),(1,2),(1,S_+1)]]
            expected=[A,B,C]
            for v,e in zip(vals, expected):
                assert simplify(v-e.subs({r:R,s:S_,b:B_}))==0,(R,S_,B_,v,e)
                representatives+=1

for R in range(2,4):
    for S_ in range(2,4):
        for B_ in [Rational(1,5),Rational(1,3),S.One,Rational(3),Rational(5)]:
            L=laplacian(R,S_,B_)
            aa=A.subs({r:R,s:S_,b:B_})
            cc=C.subs({r:R,s:S_,b:B_})
            predicted=min(aa,cc)
            correct=[]
            for pair in combinations(range(L.rows),2):
                value=cost(L,pair)
                if value==predicted:correct.append(pair)
                assert value>=predicted,(R,S_,B_,pair,value,predicted)
                all_pairs+=1
            permitted=[]
            if aa==predicted:
                permitted.extend((0,v) for v in range(1,L.rows))
            if cc==predicted:
                permitted.extend((u,v) for u,v in combinations(range(1,L.rows),2)
                                 if (u-1)//S_ != (v-1)//S_)
            assert set(correct)==set(permitted),(R,S_,B_,correct,permitted)
print(f'PASS: 3 universal symbolic identities, {representatives} exact representative tests, {all_pairs} exhaustive small-graph pairs')
