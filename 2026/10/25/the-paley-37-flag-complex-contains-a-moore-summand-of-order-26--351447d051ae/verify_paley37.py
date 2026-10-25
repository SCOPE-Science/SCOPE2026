"""Standalone exact finite verification for the Paley graph of order 37.
Requires Python 3.10+ and SymPy. Run: python3 verify_paley37.py.
"""
from collections import Counter, deque
from functools import lru_cache
import hashlib, json
from sympy import zeros
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form

N=37
Q={a*a%N for a in range(1,N)}
assert len(Q)==18 and all((-x)%N in Q for x in Q)
adj=[sum(1<<j for j in range(N) if ((j-i)%N in Q)) for i in range(N)]
faces=[]
def enumerate_cliques(f, possibilities):
    while possibilities:
        bit=possibilities&-possibilities
        possibilities-=bit
        j=bit.bit_length()-1
        g=f|bit
        faces.append(g)
        enumerate_cliques(g, possibilities&adj[j])
enumerate_cliques(0,(1<<N)-1)
S=set(faces)
assert len(S)==len(faces)==1813
assert Counter(f.bit_count() for f in faces)=={1:37,2:333,3:888,4:555}
assert all(f.bit_count()<=4 for f in faces)

def boundary(f):
    return [(f^(1<<v),(-1)**i) for i,v in enumerate(j for j in range(N) if f>>j&1)]

unmatched=S.copy();pairs=[]
for vertex in range(N):
    bit=1<<vertex
    for a in sorted(tuple(unmatched),key=lambda f:(f.bit_count(),f)):
        if a not in unmatched or a&bit:continue
        b=a|bit
        if b in unmatched:
            unmatched.remove(a);unmatched.remove(b);pairs.append((a,b))
assert len(pairs)==841
assert Counter(f.bit_count() for f in unmatched)=={1:1,3:83,4:47}

# Verify *every* face--coface incidence, not only matched pairs.
matched=set(pairs)
next_nodes={f:[] for f in S};indegree={f:0 for f in S};incidence_count=0
for f in faces:
    if f.bit_count()<2:continue
    for lower,_ in boundary(f):
        assert lower in S
        a,b=(lower,f) if (lower,f) in matched else (f,lower)
        next_nodes[a].append(b);indegree[b]+=1;incidence_count+=1
queue=deque(f for f in S if indegree[f]==0)
visited=0
while queue:
    f=queue.popleft();visited+=1
    for g in next_nodes[f]:
        indegree[g]-=1
        if not indegree[g]:queue.append(g)
assert visited==len(S) and incidence_count==5550

critical2=sorted(f for f in unmatched if f.bit_count()==3)
critical3=sorted(f for f in unmatched if f.bit_count()==4)
c2_index={f:i for i,f in enumerate(critical2)}
paired_up={a:b for a,b in pairs};paired_down={b for _,b in pairs}
@lru_cache(None)
def projection(f):
    if f in c2_index:return {c2_index[f]:1}
    if f in paired_down:return {}
    assert f in paired_up
    larger=paired_up[f]
    faces_of_larger=dict(boundary(larger))
    sign=faces_of_larger[f]
    res={}
    for g,coeff in faces_of_larger.items():
        if g==f:continue
        for i,n in projection(g).items():
            res[i]=res.get(i,0)-sign*coeff*n
    return {i:n for i,n in res.items() if n}

B=zeros(len(critical2),len(critical3))
for j,f in enumerate(critical3):
    for lower,coeff in boundary(f):
        for i,n in projection(lower).items():B[i,j]+=coeff*n
D=smith_normal_form(B,domain=ZZ)
factors=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert factors==[1]*46+[26],factors
assert max(abs(int(x)) for x in B)==1
# Independent determinantal witnesses, zero-indexed critical-cell coordinates.
rows47=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,37,38,39,41,42,44,45,50,51,56,57,63]
rows46=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,37,38,39,41,42,44,45,50,51,56,57]
assert int(B.extract(rows47,list(range(47))).det(method='domain-ge'))==-26
assert int(B.extract(rows46,list(range(1,47))).det(method='domain-ge'))==1

# A second chain calculation works on original simplices, not Morse cells.
by_size={k:sorted(x for x in faces if x.bit_count()==k) for k in (1,2,3,4)}
def rank_boundary(k,p):
    targets={f:i for i,f in enumerate(by_size[k-1])}
    pivots={};rank=0
    for f in by_size[k]:
        col={targets[g]:c%p for g,c in boundary(f)}
        while col:
            r=max(col)
            if r not in pivots:
                inv=pow(col[r],-1,p)
                pivots[r]={j:(v*inv)%p for j,v in col.items()}
                rank+=1;break
            a=col[r];pivot=pivots[r]
            for j,v in pivot.items():
                nv=(col.get(j,0)-a*v)%p
                if nv:col[j]=nv
                else:col.pop(j,None)
    return rank
ranks={str(p):[rank_boundary(2,p),rank_boundary(3,p),rank_boundary(4,p)] for p in (2,3,5,13)}
assert ranks=={'2':[36,297,554],'3':[36,297,555],'5':[36,297,555],'13':[36,297,554]},ranks

# Independent Euler check and data digest: stable, row-major signed matrix.
matrix=[[int(B[i,j]) for j in range(B.cols)] for i in range(B.rows)]
encoded=json.dumps(matrix,separators=(',',':')).encode()
assert sum((-1)**(k-1)*len(by_size[k]) for k in by_size)==37
summary={
    'graph':'Paley 37 with quadratic-residue difference adjacency',
    'vertices':37,'faces':len(S),'face_vector':[37,333,888,555],
    'Morse_pairs':len(pairs),'Morse_critical_counts':{'0':1,'2':83,'3':47},
    'Hasse_incidence_count':incidence_count,'acyclic':True,
    'Morse_boundary_shape':[83,47],'Morse_boundary_smith':[1]*46+[26],
    'Morse_boundary_sha256':hashlib.sha256(encoded).hexdigest(),
    'independent_simplicial_boundary_ranks_mod_p':ranks,
    'reduced_integral_homology':{'H2':'Z^36 plus Z/26','others':'zero'},
}
print(json.dumps(summary,indent=2))
print('VERIFY_OK')
