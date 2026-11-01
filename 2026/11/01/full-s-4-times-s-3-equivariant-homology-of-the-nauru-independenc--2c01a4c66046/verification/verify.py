#!/usr/bin/env python3
"""Finite integral Morse and exact equivariant Lefschetz calculation for the Nauru independence complex.
Uses only Python's standard library. Run: python3 nauru_symmetry_verify.py
All assertions concern the graph, its matching, its homology, and the natural group action.
"""
from itertools import permutations
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from math import factorial, prod

# Independent construction 1: generalized Petersen graph GP(12,5).
def gp_graph():
    pairs=set()
    for i in range(12):
        for a,b in ((i,(i+1)%12),(i,12+i),(12+i,12+(i+5)%12)):
            pairs.add(tuple(sorted((a,b))))
    assert len(pairs)==36
    nbs=[0]*24
    for a,b in pairs:
        nbs[a]|=1<<b; nbs[b]|=1<<a
    assert {x.bit_count() for x in nbs}=={3}
    return nbs

def morse_homology():
    nbr=gp_graph()
    faces=[0]
    for v in range(24):
        bit=1<<v
        faces += [s|bit for s in faces if s & nbr[v] == 0]
    assert len(faces)==35219 and len(set(faces))==len(faces)
    fv=Counter(s.bit_count() for s in faces)
    assert tuple(fv[k] for k in range(1,13))==(24,240,1304,4212,8328,10036,7176,2964,752,156,24,2)
    available=set(faces); match={}
    for v in range(24):
        bit=1<<v
        pairs=[(low,low|bit) for low in available if not (low&bit) and (low|bit) in available]
        for low,high in pairs:
            available.remove(low);available.remove(high);match[low]=high
    crit=sorted(available)
    assert len(match)==17605 and Counter(s.bit_count()-1 for s in crit)=={5:6,6:3}
    # Full augmented Hasse DAG acyclicity, including the matched empty face.
    indeg={s:0 for s in faces}
    inc_count=0
    for upper in faces:
        x=upper
        while x:
            bit=x&-x;x-=bit
            lower=upper^bit;inc_count+=1
            if match.get(lower)==upper:indeg[upper]+=1
            else:indeg[lower]+=1
    q=deque(s for s in faces if indeg[s]==0); done=0
    while q:
        s=q.popleft();done+=1
        x=s
        while x:
            bit=x&-x;x-=bit;lower=s^bit
            if match.get(lower)!=s:
                indeg[lower]-=1
                if indeg[lower]==0:q.append(lower)
        if s in match:
            upper=match[s];indeg[upper]-=1
            if indeg[upper]==0:q.append(upper)
    assert done==len(faces) and inc_count==205680
    lower=sorted(s for s in crit if s.bit_count()==6)
    upper=sorted(s for s in crit if s.bit_count()==7)
    low_index={s:i for i,s in enumerate(lower)}
    def boundary(s):
        x=s;i=0
        while x:
            bit=x&-x;x-=bit
            yield (s^bit, -1 if i%2 else 1)
            i+=1
    active=set()
    @lru_cache(None)
    def normal(s):
        if s in active:raise AssertionError('closed gradient path')
        active.add(s)
        if s in low_index:
            out={low_index[s]:1}
        elif s in match:
            partner=match[s]
            bound=dict(boundary(partner))
            assert bound[s] in (-1,1)
            acc=defaultdict(int)
            for face,coef in bound.items():
                if face==s:continue
                for i,c in normal(face).items():acc[i]-=bound[s]*coef*c
            out={i:c for i,c in acc.items() if c}
        else:out={}
        active.remove(s)
        return out
    mat=[[0]*3 for _ in range(6)]
    for j,cell in enumerate(upper):
        for face,coef in boundary(cell):
            for i,c in normal(face).items():mat[i][j]+=coef*c
    # Every column is determined by the latter two; the latter two span a primitive rank-two lattice.
    assert all(r[0]==r[1]-r[2] for r in mat)
    det=mat[0][1]*mat[3][2]-mat[0][2]*mat[3][1]
    assert det in [-1,1]
    assert len(lower)==6 and len(upper)==3
    return {'face_counts':tuple(fv[k] for k in range(1,13)),'morse_pairs':len(match),
            'critical_5':len(lower),'critical_6':len(upper),'morse_boundary':mat,
            'minor':det,'betti5':4,'betti6':1}

# Independent construction 2: 24-vertex Cayley star graph on permutations of 4 points.
Q=list(permutations(range(4)))
q_idx={q:i for i,q in enumerate(Q)}
def compose(a,b):return tuple(a[b[i]] for i in range(4))
def inverse(a):return tuple(a.index(i) for i in range(4))
SWAPS=[tuple(i if k==0 else (0 if k==i else k) for k in range(4)) for i in range(1,4)]
B=[b for b in Q if b[0]==0]
def star_graph():
    nbr=[0]*24
    for i,h in enumerate(Q):
        for s in SWAPS:nbr[i]|=1<<q_idx[compose(h,s)]
    return nbr

def graph_identification(star_nbr):
    # Explicit isomorphism certificate Cayley -> generalized Petersen indexing.
    relabel=(0,18,22,8,4,14,12,6,10,20,16,2,17,7,11,13,21,3,5,19,23,1,9,15)
    assert sorted(relabel)==list(range(24))
    gp=gp_graph()
    for i in range(24):
        assert {relabel[j] for j in range(24) if star_nbr[i]>>j&1}=={j for j in range(24) if gp[relabel[i]]>>j&1}

def cycles(p):
    visited=set(); out=[]
    for i in range(len(p)):
        if i in visited:continue
        orbit=[];cur=i
        while cur not in visited:
            visited.add(cur);orbit.append(cur);cur=p[cur]
        out.append(orbit)
    return out

def ptype(a):return tuple(sorted((len(c) for c in cycles(a)),reverse=True))
def btype(b):return tuple(sorted((len([x for x in c if x!=0]) for c in cycles(b) if 0 not in c),reverse=True))

def orbit_euler(a,b,nbr):
    binv=inverse(b)
    action=[q_idx[compose(compose(a,h),binv)] for h in Q]
    assert len(set(action))==24
    # Action by graph automorphisms is independently verified.
    assert all(sum(1<<action[j] for j in range(24) if nbr[i]>>j&1)==nbr[action[i]] for i in range(24))
    admissible=[]
    for orbit in cycles(action):
        mask=sum(1<<u for u in orbit)
        if all(nbr[u]&mask==0 for u in orbit):admissible.append(mask)
    # Reducible fixed simplices are unions of admissible vertex-orbits.
    # A selected union of r vertex-orbits contributes (-1)^(r+1)
    # to the reduced alternating signed chain trace, including empty union.
    def recurse(j,used,parity):
        if j==len(admissible):return parity
        ans=recurse(j+1,used,parity)
        block=admissible[j]
        if all((nbr[v]&used)==0 for v in range(24) if block>>v&1):
            ans+=recurse(j+1,used|block,-parity)
        return ans
    return -recurse(0,0,1)

def full_group_check(nbr):
    # Upper bound for Aut(G): pointwise stabilizer of vertex 0 and its neighbors is trivial.
    # Deterministic color refinement distinguishes all vertices from this marked neighborhood.
    roots=[j for j in range(24) if nbr[0]>>j&1]
    assert len(roots)==3
    colors=[0]*24;colors[0]=1
    for k,j in enumerate(roots):colors[j]=k+2
    for _ in range(20):
        descriptors=[(colors[i],tuple(sorted(colors[j] for j in range(24) if nbr[i]>>j&1))) for i in range(24)]
        classes={x:j for j,x in enumerate(sorted(set(descriptors)))}
        colors=[classes[x] for x in descriptors]
        if len(classes)==24:break
    assert len(set(colors))==24
    # |Aut(G)| <= 24 * 3! = 144; the left-by-right action has 144 distinct automorphisms.
    actions=set()
    for a in Q:
        for b in B:
            p=tuple(q_idx[compose(compose(a,h),inverse(b))] for h in Q)
            actions.add(p)
    assert len(actions)==144
    return len(actions)

S4={(1,1,1,1):(1,3,2,3,1),(2,1,1):(1,1,0,-1,-1),
    (2,2):(1,-1,2,-1,1),(3,1):(1,0,-1,0,1),(4,):(1,-1,0,1,-1)}
S3={(1,1,1):(1,2,1),(2,1):(1,0,-1),(3,):(1,-1,1)}
def zclass(t):
    return prod(k**v*factorial(v) for k,v in Counter(t).items())

def homology_representation():
    nbr=star_graph();graph_identification(nbr)
    size=full_group_check(nbr)
    values=defaultdict(set)
    for a in Q:
        for b in B:
            values[(ptype(a),btype(b))].add(orbit_euler(a,b,nbr))
    assert len(values)==15 and all(len(v)==1 for v in values.values())
    D={k:next(iter(v)) for k,v in values.items()}
    assert D[((1,1,1,1),(1,1,1))]==-3
    # Exact rational irreducible multiplicity via orthogonality of S4/S3 characters.
    coeff={}
    for i in range(5):
        for j in range(3):
            z=sum((Fraction(D[(a,b)]*c4[i]*c3[j],zclass(a)*zclass(b))
                for a,c4 in S4.items() for b,c3 in S3.items()),Fraction(0))
            assert z.denominator==1
            coeff[(i,j)]=int(z)
    assert {k:v for k,v in coeff.items() if v}=={(3,2):-1,(4,0):1,(4,2):-1}
    # H6 dimension one permits only the four 1-dimensional irreducible characters.
    # Of these, only sign(S4)⊗triv(S3) gives a nonnegative H5 representation.
    viable=[]
    for i in (0,4):
        for j in (0,2):
            h5={key:int(key==(i,j))-v for key,v in coeff.items()}
            if all(v>=0 for v in h5.values()): viable.append(((i,j),h5))
    assert len(viable)==1 and viable[0][0]==(4,0)
    assert {k:v for k,v in viable[0][1].items() if v}=={(3,2):1,(4,2):1}
    # Trace total for all characters determines both rational representations.
    print('CAYLEY_ISOMORPHIC_TO_GP_12_5: yes')
    print('FULL_AUTOMORPHISM_GROUP_ORDER:',size)
    print('LEFSCHETZ_TABLE rows S4: 1^4,2.1^2,2^2,3.1,4; columns S3: 1^3,2.1,3')
    for a in S4:
        print(' '.join(str(D[(a,b)]) for b in S3))
    print('VIRTUAL_CHARACTER:',{k:v for k,v in coeff.items() if v})
    print('H6: sign(S4) tensor trivial(S3)')
    print('H5: (Specht(2,1,1) plus sign(S4)) tensor sign(S3)')
    print('NO_FULL_GROUP_INVARIANTS: yes')
    return D

def main():
    data=morse_homology()
    print('MORSE_CRITICAL_5_6:',data['critical_5'],data['critical_6'])
    print('MORSE_INTEGRAL_MATRIX:')
    for row in data['morse_boundary']:print(' ',row)
    print('MORSE_PRIMITIVE_MINOR:',data['minor'])
    print('RATIONAL_REDUCED_BETTI_5_6:',data['betti5'],data['betti6'])
    homology_representation()
    print('VERIFY_OK')

if __name__=='__main__':main()
