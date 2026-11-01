#!/usr/bin/env python3
"""Exhaustive face construction and acyclic Morse certificate for CF3 of the icosahedron.
Only the Python standard library is required.
"""
from itertools import combinations
from collections import Counter, deque
from functools import lru_cache

# Twelve vertices: north=0, upper pentagon 1..5, lower pentagon 6..10, south=11.
# U_i~U_{i+1}, L_i~L_{i+1}, U_i~L_i, U_i~L_{i-1} (indices cyclic).
EDGES=set()
def edge(a,b): EDGES.add(tuple(sorted((a,b))))
for i in range(5):
    u=1+i; un=1+(i+1)%5
    l=6+i; ln=6+(i+1)%5
    edge(0,u); edge(11,l); edge(u,un); edge(l,ln)
    edge(u,l); edge(u,6+(i-1)%5)
assert len(EDGES)==30
TRIANGLES=[]
for t in combinations(range(12),3):
    if all(tuple(sorted(ab)) in EDGES for ab in combinations(t,2)):
        TRIANGLES.append(sum(1<<v for v in t))
assert len(TRIANGLES)==20

def admissible(m):
    return all(m&t !=t for t in TRIANGLES)

# Check two equivalent exhaustive models: (i) triangular circuits of the given
# edge list; (ii) the explicit 20 triangles by 5-fold cyclic construction.
manual=set()
for i in range(5):
    j=(i+1)%5
    u_i,u_j=1+i,1+j
    l_i,l_j=6+i,6+j
    for tri in [(0,u_i,u_j),(11,l_i,l_j),(u_i,u_j,l_i),(u_j,l_i,l_j)]:
        manual.add(sum(1<<v for v in tri))
assert set(TRIANGLES)==manual
F={m for m in range(1,1<<12) if admissible(m)}
F_by_dim={k:[m for m in sorted(F) if m.bit_count()==k+1] for k in range(6)}
assert tuple(len(F_by_dim[k]) for k in range(6))==(12,66,200,345,312,112)
assert len(F)==1047
FACETS={m for m in F if all(m|(1<<v) not in F for v in range(12) if not m&(1<<v))}
assert len(FACETS)==112 and all(m.bit_count()==6 for m in FACETS)

# Order-independent acyclic matching obtained by successive complete toggle
# matchings: all faces sigma and sigma+v still present are paired.
PIVOTS=(6,0,4,3,2,5,9,8,10,11,1,7)
remaining=F.copy()
pairs=[]
for v in PIVOTS:
    bit=1<<v
    for a in sorted(remaining):
        b=a|bit
        if a&bit==0 and b in remaining:
            remaining.remove(a)
            remaining.remove(b)
            pairs.append((a,b))
assert len(pairs)==522
assert len(remaining)==3
assert Counter(m.bit_count()-1 for m in remaining)=={0:1,4:1,5:1}
crit_4=next(m for m in remaining if m.bit_count()==5)
crit_5=next(m for m in remaining if m.bit_count()==6)

# Exhaustively verify acyclicity independently via directed Hasse diagram:
# every codimension-one edge goes downward except reversed matched pairs.
matched=set(pairs)
succ={m:[] for m in F}
indeg={m:0 for m in F}
incidences=0
for b in F:
    for v in range(12):
        if not b&(1<<v) or b.bit_count()==1:continue
        a=b^(1<<v)
        assert a in F
        if (a,b) in matched:
            x,y=a,b
        else:
            x,y=b,a
        succ[x].append(y)
        indeg[y]+=1
        incidences+=1
que=deque([m for m in F if indeg[m]==0]); seen=0
while que:
    u=que.popleft();seen+=1
    for v in succ[u]:
        indeg[v]-=1
        if indeg[v]==0:que.append(v)
assert seen==len(F), f'Not acyclic: {seen}/{len(F)}'

# An independent integer gradient-path computation for the unique Morse
# boundary C_5 -> C_4.  A matched (4,5) incidence has unit coefficient.
# Cancellation rewrites the matched lower 4-face into the other faces of its
# paired 5-simplex.  Four-faces paired downward with three-faces are zero in
# the Morse C_4 projection.
up={a:b for a,b in pairs}
def incidence(a,b):
    """Signed incidence <d(b),a> in ordered-vertex bases."""
    assert b.bit_count()==a.bit_count()+1 and a&b==a
    difference=b^a
    v=difference.bit_length()-1
    return -1 if (b&((1<<v)-1)).bit_count()%2 else 1

@lru_cache(maxsize=None)
def coefficient(a):
    assert a.bit_count()==5
    if a in remaining:return 1 if a==crit_4 else 0
    b=up.get(a)
    if b is None:
        # This 4-cell is matched as an upper cell against a 3-cell.
        assert any(x==a for _,x in pairs)
        return 0
    assert b.bit_count()==6
    s=incidence(a,b)
    return -s*sum(incidence(c,b)*coefficient(c)
                  for v in range(12) if b&(1<<v)
                  for c in [b^(1<<v)] if c!=a)

MORSE_D_5_4=sum(incidence(crit_5^(1<<v),crit_5)*coefficient(crit_5^(1<<v))
                for v in range(12) if crit_5&(1<<v))
assert abs(MORSE_D_5_4)==2, MORSE_D_5_4

# Independent column-side elimination: find the integral chain consisting of
# the critical 5-simplex plus matched 5-simplices whose boundary vanishes on
# every matched-lower 4-face. This is a triangular integral system because
# the matching is acyclic; all diagonal coefficients are +1 or -1.
five_pairs={a:b for a,b in pairs if a.bit_count()==5}
assert len(five_pairs)==111
pivrows=set(five_pairs)
@lru_cache(maxsize=None)
def multiplier(a):
    b=five_pairs[a]
    other=0
    for c,d in five_pairs.items():
        if c!=a and a&d==a:
            other+=incidence(a,d)*multiplier(c)
    direct=incidence(a,crit_5) if a&crit_5==a else 0
    return -(direct+other)*incidence(a,b)
coeff_critical_4=(incidence(crit_4,crit_5) if crit_4&crit_5==crit_4 else 0)
coeff_critical_4+=sum((incidence(crit_4,b)*multiplier(a) if crit_4&b==crit_4 else 0)
                      for a,b in five_pairs.items())
assert coeff_critical_4==MORSE_D_5_4,(coeff_critical_4,MORSE_D_5_4)


# Independent mod-p simplicial chain reduction checks correct dimensions.
def rank_mod_p(k,p):
    if k==0:return 0
    target=F_by_dim[k-1]
    idx={x:i for i,x in enumerate(target)}
    piv={}
    for b in F_by_dim[k]:
        col={idx[b^(1<<v)]:incidence(b^(1<<v),b)%p
             for v in range(12) if b&(1<<v)}
        col={i:a for i,a in col.items() if a}
        while col:
            j=max(col)
            if j not in piv:
                inv=pow(col[j],-1,p)
                piv[j]={i:(v*inv)%p for i,v in col.items() if (v*inv)%p}
                break
            factor=col[j]
            for i,v in piv[j].items():
                nv=(col.get(i,0)-factor*v)%p
                if nv:col[i]=nv
                else:col.pop(i,None)
    return len(piv)
for p in (2,3,5,7):
    ranks={k:rank_mod_p(k,p) for k in range(1,6)}
    betti={k:len(F_by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)-int(k==0)
           for k in range(6)}
    expected={0:0,1:0,2:0,3:0,4:int(p==2),5:int(p==2)}
    assert betti==expected,(p,betti)

print('VERIFY_OK edges=30 triangles=20 faces=1047 facets=112')
print('VERIFY_OK f_vector=(12,66,200,345,312,112)')
print(f'VERIFY_OK pairs={len(pairs)} incidences={incidences} dag={seen} critical=(1_0,1_4,1_5)')
print(f'VERIFY_OK integer_morse_boundary_5_4={MORSE_D_5_4} homotopy=Moore_Z2_4')
print('VERIFY_OK mod2_reduced_betti=(0,0,0,0,1,1) odd_prime_reduced_betti=all_zero')
print('CERTIFICATE pivots=',','.join(map(str,PIVOTS)))
print('CERTIFICATE critical_masks=',','.join(map(str,sorted(remaining))))
