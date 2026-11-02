"""Independent exact Smith-normal-form computation (requires sympy)."""
from itertools import combinations
from sympy import Matrix,eye,ZZ
from sympy.matrices.normalforms import smith_normal_form
lines={frozenset((i,(i+1)%7,(i+3)%7)) for i in range(7)}
V=[frozenset(x) for x in combinations(range(7),3) if frozenset(x) not in lines]
A=Matrix(28,28,lambda i,j:int(i!=j and V[i].isdisjoint(V[j])))
L=3*eye(28)-A
D=smith_normal_form(L[:27,:27],domain=ZZ)
assert list(D.diagonal()) == [1]*21+[8]+[56]*5
assert L[:27,:27].det(method='domain-ge')==4405854208
assert A*Matrix.ones(28,1)==3*Matrix.ones(28,1)
print('COXETER_INDEPENDENT_SMITH_PASS')
