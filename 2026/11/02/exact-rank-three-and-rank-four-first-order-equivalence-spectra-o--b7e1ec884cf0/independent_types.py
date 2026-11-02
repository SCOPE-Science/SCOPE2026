"""Independent enumeration of first-order type signatures for squares of finite paths.
The base relations and refinement are generated directly from adjacency on tuple vertices.
Usage: python ef_pathsquare_independent.py
"""
from itertools import product

def atom(vertices):
    return tuple((0 if vertices[i] == vertices[j] else 1 if abs(vertices[i]-vertices[j]) <=2 else 2)
                 for i in range(len(vertices)) for j in range(i+1,len(vertices)))

class Intern:
    def __init__(self): self.index={}
    def add(self,obj):
        key=self.index.get(obj)
        if key is None:
            key=len(self.index)+1
            self.index[obj]=key
        return key

T31=Intern();T22=Intern();T13=Intern();T04=Intern()
T21=Intern();T12=Intern();T03=Intern()

for n in list(range(1,13))+[25,26,27]:
    vv=range(n)
    r31={}
    for x,y,z in product(vv,repeat=3):
        s=frozenset(atom((x,y,z,w)) for w in vv)
        r31[(x,y,z)]=T31.add((atom((x,y,z)),s))
    r22={}
    for x,y in product(vv,repeat=2):
        r22[(x,y)]=T22.add((atom((x,y)),frozenset(r31[(x,y,z)] for z in vv)))
    r13={x:T13.add(((),frozenset(r22[(x,y)] for y in vv))) for x in vv}
    rank4=T04.add(((),frozenset(r13.values())))
    r21={(x,y):T21.add((atom((x,y)),frozenset(atom((x,y,z)) for z in vv))) for x,y in product(vv,repeat=2)}
    r12={x:T12.add(((),frozenset(r21[(x,y)] for y in vv))) for x in vv}
    rank3=T03.add(((),frozenset(r12.values())))
    print(f'RANKS_PY n={n} rank3_type={rank3} rank4_type={rank4}',flush=True)
    assert rank3 == min(n,11),(n,rank3)
    if n<=12: assert rank4 == n,(n,rank4)
    if n==25: p25=rank4
    if n==26: p26=rank4
    if n==27: assert rank4==p26 and p25!=p26, (p25,p26,rank4)
print('INDEPENDENT_PYTHON_TYPE_CLASSIFICATION_PASS',flush=True)
