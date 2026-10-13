from itertools import permutations, combinations
from collections import Counter

# F4 = F2[w]/(w^2+w+1), encoded as 0,1,w,w^2 = 0,1,2,3.
G = [
    (1,0,2,3,0,3,1),
    (2,0,0,1,3,2,1),
    (0,1,2,1,3,3,2),
    (0,2,2,3,1,0,3),
    (0,0,1,3,2,1,2),
]

def add(u,v):
    return tuple(a ^ b for a,b in zip(u,v))

C={(0,)*7}
for r in G:
    C |= {add(c,r) for c in tuple(C)}
assert len(C)==32
wd=Counter(sum(x!=0 for x in c) for c in C)
assert wd==Counter({0:1,5:21,6:7,7:3})

W5=[c for c in C if sum(x!=0 for x in c)==5]
byzero={tuple(i for i,x in enumerate(c) if x==0):c for c in W5}
assert len(byzero)==21
assert set(byzero)==set(combinations(range(7),2))
for i in range(7):
    assert {c[i] for c in W5 if c[i] != 0} == {1,2,3}

def permute_word(c,p):
    # p maps old coordinate i to new coordinate p[i].
    out=[0]*7
    for i,x in enumerate(c):
        out[p[i]]=x
    return tuple(out)

pure=[]
full=[]
for p in permutations(range(7)):
    if {permute_word(c,p) for c in C}==C:
        pure.append(p)

    # A weight-5 word is uniquely indexed by its two zero coordinates. Hence p
    # determines its target. These targets determine each local nonzero-symbol map.
    local=[{0:0} for _ in range(7)]
    ok=True
    for z,c in byzero.items():
        target=byzero[tuple(sorted((p[z[0]],p[z[1]])))]
        for i,x in enumerate(c):
            if x:
                y=target[p[i]]
                old=local[i].get(x)
                if old is not None and old != y:
                    ok=False
                    break
                local[i][x]=y
        if not ok:
            break
    if not ok:
        continue
    # Maps x -> a*x or a*x^2 are exactly the six permutations of F4^* fixing 0.
    if any(set(m.keys())!={0,1,2,3} or set(m.values())!={0,1,2,3} for m in local):
        continue

    transformed=set()
    for c in C:
        out=[0]*7
        for i,x in enumerate(c):
            out[p[i]]=local[i][x]
        transformed.add(tuple(out))
    if transformed==C:
        full.append((p,local))

assert len(pure)==7
assert len(full)==21
P={p for p,_ in full}
assert len(P)==21

def compose(p,q):
    return tuple(p[q[i]] for i in range(7))

def order(p):
    e=tuple(range(7)); a=e
    for k in range(1,100):
        a=compose(p,a)
        if a==e:
            return k
    raise AssertionError('order bound')

assert all(compose(p,q) in P for p in P for q in P)
orders=Counter(order(p) for p in P)
assert orders==Counter({1:1,3:14,7:6})
assert set(pure)=={p for p in P if order(p) in (1,7)}

print('VERIFY_OK')
print('CODE_SIZE',len(C),'WEIGHTS',dict(sorted(wd.items())))
print('WEIGHT5_ZERO_PAIRS',len(byzero))
print('PURE_COORDINATE_AUTOMORPHISMS',len(pure))
print('FULL_EQUIVALENCE_AUTOMORPHISMS',len(full))
print('PROJECTED_PERMUTATION_ORDERS',dict(sorted(orders.items())))
