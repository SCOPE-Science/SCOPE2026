from itertools import combinations

# GF(3^4) = F_3[x]/(x^4-x-1). Elements are tuples c0+c1*x+c2*x^2+c3*x^3.
P = 3

def add(a,b): return tuple((x+y)%P for x,y in zip(a,b))
def neg(a): return tuple((-x)%P for x in a)
def sub(a,b): return add(a,neg(b))
ZERO=(0,0,0,0)
ONE=(1,0,0,0)
G=(0,1,0,0)

def mul(a,b):
    t=[0]*7
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            t[i+j]=(t[i+j]+ai*bj)%P
    # x^4 = x+1; reduce high terms from degree 6 down to 4.
    for d in range(6,3,-1):
        c=t[d]%P
        if c:
            t[d]=0
            t[d-4]=(t[d-4]+c)%P
            t[d-3]=(t[d-3]+c)%P
    return tuple(t[:4])

def powe(a,n):
    r=ONE
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a); n//=2
    return r

def elems():
    for n in range(81):
        x=n; c=[]
        for _ in range(4): c.append(x%3); x//=3
        yield tuple(c)

E=list(elems())
assert len(set(E))==81
assert powe(G,80)==ONE
assert all(powe(G,d)!=ONE for d in [1,2,4,5,8,10,16,20,40])

A=[powe(G,4*k) for k in range(20)]
assert len(set(A))==20

bad=[]
for a in A:
    for b in A:
        for c in A:
            if add(add(a,b),c)==ZERO and not (a==b==c):
                bad.append((a,b,c))
assert not bad

# Columns (h, h+a, h-a), h in GF(81), a in A.
cols=[]
for h in E:
    for a in A:
        cols.append((h, add(h,a), sub(h,a)))
assert len(cols)==1620
assert all(len({col[r] for col in cols})==81 for r in range(3))

# Every pair of columns may collide in at most one row. Record edge color = colliding row.
edge_color={}
for r in range(3):
    classes={}
    for idx,col in enumerate(cols):
        classes.setdefault(col[r],[]).append(idx)
    assert sorted(map(len,classes.values()))==[20]*81
    for cls in classes.values():
        for u,v in combinations(cls,2):
            key=(u,v) if u<v else (v,u)
            assert key not in edge_color, (key,edge_color.get(key),r)
            edge_color[key]=r

# A bad triple in a 3-row PHF with pairwise-at-most-one collision must form a rainbow
# collision triangle: one pair collides in each row. Search all such triangles.
adj=[ [set() for _ in cols] for __ in range(3)]
for (u,v),r in edge_color.items():
    adj[r][u].add(v); adj[r][v].add(u)

bad_triangles=[]
# Orient: row0 edge (u,v), row1 edge (v,w), test row2 edge (w,u).
for (u,v),r in edge_color.items():
    if r != 0: continue
    for a,b in ((u,v),(v,u)):
        for w in adj[1][b]:
            if w!=a and a in adj[2][w]:
                bad_triangles.append(tuple(sorted((a,b,w))))
assert not bad_triangles

print('field_size=81')
print('primitive_generator_order=80')
print('cap_size=20')
print('nontrivial_zero_sum_triples=0')
print('phf_rows=3')
print('phf_columns=1620')
print('alphabet_size_each_row=81')
print('class_size_each_symbol_each_row=20')
print('pair_collisions_in_multiple_rows=0')
print('bad_column_triples=0')
print('verified=PHF(3;1620,81,3)')
