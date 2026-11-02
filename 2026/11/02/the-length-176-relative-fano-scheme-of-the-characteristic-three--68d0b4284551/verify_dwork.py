"""Exact enumeration of lines on the characteristic-three Dwork quartic pencil.
Uses the field F_9=F_3[i]/(i^2+1), RREF charts of Gr(2,4), and
five independent tests on P^1(F_9) for each restricted quartic.
No external dependencies. The accompanying proof treats algebraic closures.
"""
from itertools import combinations, product

Q=9
add=[[((a%3+b%3)%3)+3*((a//3+b//3)%3) for b in range(Q)] for a in range(Q)]
mul=[[((a%3)*(b%3)+2*(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(Q)] for a in range(Q)]
p4=[mul[mul[mul[a][a]][a]][a] for a in range(Q)]

def lines():
    for i,j in combinations(range(4),2):
        free=[(r,c) for r,piv in enumerate((i,j)) for c in range(piv+1,4) if c not in (i,j)]
        for vals in product(range(Q),repeat=len(free)):
            R=[[0]*4,[0]*4]
            R[0][i]=R[1][j]=1
            for (r,c),v in zip(free,vals): R[r][c]=v
            yield R

def value(x,l):
    v=0
    for a in x:v=add[v][p4[a]]
    return add[v][mul[l][mul[x[0]][mul[x[1]][mul[x[2]][x[3]]]]]]

# Four different affine values and infinity give five roots of a quartic.
points=((1,0),(0,1),(1,1),(1,2),(1,3))
Ls=list(lines())
assert len(Ls)==(Q*Q+1)*(Q*Q+Q+1)==7462
counts={}
for lam in range(Q):
    count=0
    for (a,b) in Ls:
        if all(value([add[mul[s][a[k]]][mul[t][b[k]]] for k in range(4)],lam)==0 for s,t in points):
            count+=1
    counts[lam]=count
assert counts[0]==112, counts
assert all(counts[x]==0 for x in range(1,Q)),counts
print('GF9_DWORK_LINES_'+repr(counts)+'_OK')
