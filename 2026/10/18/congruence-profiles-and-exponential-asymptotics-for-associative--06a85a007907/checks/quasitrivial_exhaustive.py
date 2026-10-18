"""Enumerate quasitrivial operations independently of the weak-order parametrization."""
import itertools
from quasitrivial_checker import congruence_profile

def exhaustive(n):
    points=[(i,j) for i in range(n) for j in range(n) if i!=j]
    full=[0]*(n+1)
    associative=0
    for selections in itertools.product((0,1),repeat=len(points)):
        mat=[[i if i==j else -1 for j in range(n)] for i in range(n)]
        for (i,j),b in zip(points,selections):mat[i][j]=i if b==0 else j
        if any(mat[mat[a][b]][c]!=mat[a][mat[b][c]] for a in range(n) for b in range(n) for c in range(n)):
            continue
        associative+=1
        actual=congruence_profile(mat)
        for k,val in enumerate(actual):full[k]+=val
    return associative,full

if __name__=='__main__':
    for n in range(1,5):
        s,c=exhaustive(n)
        print('EXHAUSTIVE',n,s,c,sum(c))
    assert exhaustive(4)==(138,[0,138,270,300,138])
    print('EXHAUSTIVE_OK')
