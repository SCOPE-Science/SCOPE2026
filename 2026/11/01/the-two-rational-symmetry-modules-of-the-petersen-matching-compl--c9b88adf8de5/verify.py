"""Exact rational, full S5 representation check for Petersen matching complex.
Run with Python 3 and SymPy."""
from itertools import combinations, permutations
from collections import defaultdict
from functools import lru_cache
import sympy as sp

V=list(combinations(range(5),2))
E=[(i,j) for i,j in combinations(range(10),2) if set(V[i]).isdisjoint(V[j])]
assert len(E)==15
faces=[[] for _ in range(5)]
for k in range(1,6):
    for ids in combinations(range(15),k):
        if len({x for i in ids for x in E[i]})==2*k:faces[k-1].append(ids)
assert list(map(len,faces))==[15,75,145,90,6]
ix=[{f:i for i,f in enumerate(F)} for F in faces]
def bd(k):
    d=sp.zeros(len(faces[k-1]),len(faces[k]))
    for j,face in enumerate(faces[k]):
        for i in range(k+1):d[ix[k-1][face[:i]+face[i+1:]],j]=(-1)**i
    return d
D=[None,sp.zeros(15,75)]+[bd(k) for k in range(2,5)]
D[1]=bd(1)
assert D[1].rank()==14
assert [D[k].rank() for k in (2,3,4)]==[61,79,6]
for k in (2,3,4):assert D[k-1]*D[k]==sp.zeros(D[k-1].rows,D[k].cols)
assert len(faces[2])-61-79==5 and len(faces[3])-79-6==5
kernel=D[3].nullspace()
cols=list(D[4].columnspace()); assert len(cols)==6
for z in kernel:
    if sp.Matrix.hstack(*cols,z).rank()>len(cols):cols.append(z)
assert len(cols)==11
B=sp.Matrix.hstack(*cols)
rows=list(B.T.rref()[1]); inv=B.extract(rows,range(11)).inv()
H=cols[6:]
expected2={(1,1,1,1,1):5,(2,1,1,1):-3,(2,2,1):1,(3,1,1):2,(3,2):0,(4,1):-1,(5,):0}
expected3={(1,1,1,1,1):5,(2,1,1,1):1,(2,2,1):1,(3,1,1):-1,(3,2):1,(4,1):-1,(5,):0}

def cyc(p):
    visited=set();parts=[]
    for i in range(5):
        if i not in visited:
            j=i;c=0
            while j not in visited:
                visited.add(j);c+=1;j=p[j]
            parts.append(c)
    return tuple(sorted(parts,reverse=True))

@lru_cache(None)
def induced(p):
    vmap={i:V.index(tuple(sorted((p[a],p[b])))) for i,(a,b) in enumerate(V)}
    return {i:E.index(tuple(sorted((vmap[a],vmap[b])))) for i,(a,b) in enumerate(E)}

def action(k,p):
    em=induced(p)
    res=[]
    for f in faces[k]:
        mapped=[em[j] for j in f]
        sign=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        res.append((ix[k][tuple(sorted(mapped))],sign))
    return res

def h3trace(p):
    op=action(3,p)
    trace=0
    for j,z in enumerate(H):
        az=sp.zeros(90,1)
        for i,(dest,sgn) in enumerate(op):
            if z[i]:az[dest]+=sgn*z[i]
        c=inv*az.extract(rows,[0]);assert B*c==az
        trace+=c[6+j]
    return int(trace)

cnt=defaultdict(int)
for p in permutations(range(5)):
    tp=cyc(p)
    t3=h3trace(p)
    L=sum((-1)**k*sum(s for i,(j,s) in enumerate(action(k,p)) if i==j) for k in range(5))
    t2=L-1+t3
    assert t3==expected3[tp],(p,tp,t3,expected3[tp])
    assert t2==expected2[tp],(p,tp,t2,expected2[tp])
    cnt[tp]+=1
assert sum(cnt.values())==120 and len(cnt)==7
for tp in sorted(cnt,reverse=True):
    print('cycle_type',tp,'size',cnt[tp],'trace_H2',expected2[tp],'trace_H3',expected3[tp])
print('f_vector',list(map(len,faces)),'boundary_ranks',[14,61,79,6])
print('reduced_rational_betti',{'H2':5,'H3':5})
print('all_120_S5_actions_exactly_verified','VERIFY_OK')
