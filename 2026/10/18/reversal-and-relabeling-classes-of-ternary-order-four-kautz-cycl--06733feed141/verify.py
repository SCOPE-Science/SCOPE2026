"""Finite exact enumeration of ternary Kautz cycles of order four.
All counting uses integer and exhaustive finite steps; no dependencies.
"""
from itertools import permutations, product

Q=3
K=4
words=[''.join(z) for z in product('012', repeat=K)
       if all(z[i]!=z[i+1] for i in range(K-1))]
words.sort()
assert len(words)==24 and words[0]=='0101'
vertices=sorted(set(w[:K-1] for w in words))
assert len(vertices)==12
ins={v:[i for i,w in enumerate(words) if w[1:]==v] for v in vertices}
outs={v:[i for i,w in enumerate(words) if w[:-1]==v] for v in vertices}
assert all(len(ins[v])==len(outs[v])==2 for v in vertices)

def anchored(w):
    p=w.find('0101')
    assert p>=0 and (w+w).count('0101')==1
    return w[p:]+w[:p]

def canon(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def mirror(w):
    return canon(w)==canon(w[::-1])

# Enumeration A: every permutation of the two possible local through-connections.
# Each selection partitions the 24 edges into disjoint directed cycles.
def via_transition_systems():
    result=set()
    for bits in range(1<<len(vertices)):
        successor=[-1]*len(words)
        for iv,v in enumerate(vertices):
            for j,i in enumerate(ins[v]):
                successor[i]=outs[v][j^((bits>>iv)&1)]
        walk=[]; at=0
        while at not in walk:
            walk.append(at)
            at=successor[at]
        if at==0 and len(walk)==len(words):
            w=''.join(words[i][0] for i in walk)
            assert w.startswith('0101')
            result.add(w)
    return result

# Enumeration B: edge-use DFS with the single distinguished edge fixed first.
def via_depth_first():
    result=set()
    used=[False]*len(words); used[0]=True
    edge_walk=[0]
    def explore(v):
        if len(edge_walk)==len(words):
            if v==words[0][:-1]:
                result.add(''.join(words[i][0] for i in edge_walk))
            return
        for i in outs[v]:
            if not used[i]:
                used[i]=True;edge_walk.append(i)
                explore(words[i][1:])
                edge_walk.pop();used[i]=False
    explore(words[0][1:])
    return result

cycles_A=via_transition_systems()
cycles_B=via_depth_first()
assert cycles_A==cycles_B and len(cycles_A)==384
for w in cycles_A:
    assert len(w)==24 and w[:4]=='0101'
    windows={(w+w[:K-1])[i:i+K] for i in range(len(w))}
    assert windows==set(words)
reflect={w for w in cycles_A if mirror(w)}
assert len(reflect)==24
bracelets={min(canon(w),canon(w[::-1])) for w in cycles_A}
assert len(bracelets)==204

perms=list(permutations('012'))
def relabel(w,perm):
    return ''.join(perm[ord(x)-48] for x in w)
def orbit_rep(w,allow_mirror=False):
    reps=[]
    for perm in perms:
        x=relabel(w,perm)
        reps.append(canon(x))
        if allow_mirror: reps.append(canon(x[::-1]))
    return min(reps)
classes={orbit_rep(w) for w in cycles_A}
reversal_classes={orbit_rep(w,True) for w in cycles_A}
reflect_classes={r for w in reflect for r in [orbit_rep(w)]}
assert len(classes)==64 and len(reversal_classes)==34
assert len(reflect_classes)==4
representatives=sorted(reflect_classes)
expected=['010102021021210121201202',
          '010102021210210120121202',
          '010102102021210121202012',
          '010102121020210120201212']
assert representatives==expected
assert all(sum(orbit_rep(w)==r for w in reflect)==6 for r in representatives)
assert len({orbit_rep(w) for w in cycles_A if not mirror(w)})==60
assert len(reversal_classes)==4+(64-4)//2
print('VERIFY_OK q3_order4 cycles_384 reflection_fixed_24 bracelets_204 symbol_orbits_64 unoriented_symbol_orbits_34 achiral_symbol_orbits_4')
