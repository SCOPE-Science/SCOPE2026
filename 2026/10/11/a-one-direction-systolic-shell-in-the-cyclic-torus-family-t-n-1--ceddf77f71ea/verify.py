from itertools import product
from math import ceil

STEPS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))

def norm(v):
    a,b=v
    return max(abs(a),abs(b),abs(a-b))

def end(seq):
    return (sum(x for x,y in seq),sum(y for x,y in seq))

# Exact universal-cover short-word classification.
by_len={}
for ell in range(1,5):
    rel=set()
    for seq in product(STEPS, repeat=ell):
        v=end(seq)
        if v[0]+3*v[1]==0:
            rel.add(v)
    by_len[ell]=rel
assert by_len[1]==set()
assert by_len[2]=={(0,0)}
assert by_len[3]=={(0,0)}
assert by_len[4]=={(0,0),(-3,1),(3,-1)}
assert norm((-3,1))==4

# Every step changes the cyclic label a+3b by one of +-1,+-3,+-4.
assert {a+3*b for a,b in STEPS}=={-4,-3,-1,1,3,4}

# Explicit witnesses for the second independent homology minimum.
def second_witness(n):
    r,s=divmod(n,4)
    if s==0: v=(r,r)
    elif s==1: v=(r+1,r)
    elif s==2: v=(r-1,r+1)
    else: v=(r,r+1)
    assert v[0]+3*v[1]==n
    assert norm(v)==ceil(n/4)
    return v

# Finite replay of the actual cyclic complexes for a broad parameter window.
def graph(n):
    adj=[set() for _ in range(n)]
    for i in range(n):
        for s in (1,3,4):
            j=(i+s)%n
            adj[i].add(j); adj[j].add(i)
    return adj

def edge_vec(n,a,b):
    d=(b-a)%n
    table={1:(1,0),n-1:(-1,0),3:(0,1),n-3:(0,-1),4:(1,1),n-4:(-1,-1)}
    return table[d]

def canonical_cycle(c):
    c=tuple(c)
    reps=[]
    for q in (c,tuple(reversed(c))):
        for j in range(len(q)): reps.append(q[j:]+q[:j])
    return min(reps)

def simple_cycles_len(adj,L):
    n=len(adj); out=set()
    for s in range(n):
        stack=[(s,[s])]
        while stack:
            v,path=stack.pop()
            if len(path)==L:
                if s in adj[v]: out.add(canonical_cycle(path))
                continue
            for w in adj[v]:
                if w not in path: stack.append((w,path+[w]))
    return out

def homology_vector(n,cyc):
    a=b=0
    for i in range(len(cyc)):
        x,y=edge_vec(n,cyc[i],cyc[(i+1)%len(cyc)])
        a+=x; b+=y
    return (a,b)

for n in range(17,41):
    A=graph(n)
    c3=simple_cycles_len(A,3)
    c4=simple_cycles_len(A,4)
    nz3=[c for c in c3 if homology_vector(n,c)!=(0,0)]
    nz4=[c for c in c4 if homology_vector(n,c)!=(0,0)]
    assert not nz3
    assert len(nz4)==n
    want={canonical_cycle((i,(i+1)%n,(i+2)%n,(i+3)%n)) for i in range(n)}
    assert set(nz4)==want
    assert {tuple(map(abs,homology_vector(n,c))) for c in nz4} <= {(3,1)}
    v=second_witness(n)
    # universal lower bound outside the rank-one systolic subgroup
    m=ceil(n/4)
    for b in range(-m,m+1):
        for a in range(-m,m+1):
            if norm((a,b))<m and (a+3*b)%n==0 and a+3*b!=0:
                raise AssertionError((n,a,b))

print('VERIFY_OK short_relation_vectors=none_through3;length4=plusminus(-3,1)')
print('family=T_{n,1,3} range=n>=17 H1=Z^2')
print('simple_integral_1_systole=4 minimizers=n consecutive_4_cycles one_primitive_direction=yes')
print('second_independent_homology_minimum=ceil(n/4)')
print('finite_replay=n17..40 passed')
