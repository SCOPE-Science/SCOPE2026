"""Reproducible finite checks for the integral homology module of Ind(C5 x Kn).

Run: python3 verify.py. Requires Python 3 standard library only.
All searches, collapses and face maps are exact integer combinatorics.
"""
from functools import lru_cache
from itertools import permutations, combinations


def graph_neighbors(n):
    z = 5*n
    adj = [0]*z
    for i in range(5):
        for c in range(n):
            v=i*n+c
            for h in ((i-1)%5,(i+1)%5):
                for d in range(n):
                    if c!=d:
                        adj[v] |= 1<<(h*n+d)
    return adj


def independent_faces(n):
    adj=graph_neighbors(n)
    result=[[] for _ in range(5*n+1)]
    def visit(available,face):
        if not available:
            result[len(face)].append(tuple(face))
            return
        b=available&-available
        v=b.bit_length()-1
        visit(available^b,face)
        visit((available^b)&~adj[v],face+[v])
    visit((1<<(5*n))-1,[])
    return {k:sorted(f) for k,f in enumerate(result) if f}


def collapse_base_case():
    # This cyclic labeling realizes C5 x K2 as the ten-cycle.
    # Simpler description: v_0=(0,0), v_1=(1,1), ..., v_9=(4,1).
    order=[(j%5,j%2) for j in range(10)]
    assert len(set(order))==10
    adj=graph_neighbors(2)
    for j in range(10):
        i,c=order[j]
        neighbors={order[(j+1)%10],order[(j-1)%10]}
        assert {divmod(x,2) for x in range(10) if adj[i*2+c]>>x&1}==neighbors
    faces=set()
    for sz in range(1,6):
        for f in combinations(range(10),sz):
            if all((abs(x-y)%10) not in (1,9) for x,y in combinations(f,2)):
                faces.add(frozenset(f))
    # Three separated graph edges form an induced matching.
    sphere_vertices=frozenset((0,1,3,4,6,7))
    target={f for f in faces if f<=sphere_vertices}
    assert len(faces)==122 and len(target)==26
    assert sum(len(f)==3 for f in target)==8
    remaining=set(faces)
    pairs=[]
    while True:
        candidate=None
        for f in sorted(remaining-target,key=lambda s:(-len(s),tuple(sorted(s)))):
            upper=[f|{v} for v in range(10) if v not in f and f|{v} in remaining]
            if len(upper)==1 and upper[0] not in target:
                candidate=(f,upper[0]);break
        if candidate is None:break
        low,high=candidate
        assert len(high)==len(low)+1
        assert not any(high < other for other in remaining), "upper member must be maximal"
        remaining.remove(low);remaining.remove(high)
        pairs.append(candidate)
    assert len(pairs)==48 and remaining==target
    return len(faces),len(pairs),len(target)


def orbit_trace(n,colors,positions):
    """Signed augmented Lefschetz trace, via vertex-orbit independence polynomial."""
    adj=graph_neighbors(n)
    N=5*n
    perm=[positions[v//n]*n+colors[v%n] for v in range(N)]
    assert sorted(perm)==list(range(N))
    vertex_orbits=[];seen=set()
    for v in range(N):
        if v in seen:continue
        orb=[];x=v
        while x not in seen:
            seen.add(x);orb.append(x);x=perm[x]
        vertex_orbits.append(orb)
    valid=[]
    for orb in vertex_orbits:
        mask=sum(1<<x for x in orb)
        if all((adj[x]&mask)==0 for x in orb):
            valid.append(mask)
    q=len(valid)
    conflict=[0]*q
    for i,a in enumerate(valid):
        for j in range(i+1,q):
            if any(adj[v]&valid[j] for v in range(N) if a>>v&1):
                conflict[i]|=1<<j
                conflict[j]|=1<<i
    @lru_cache(None)
    def independence_polynomial_minus_one(nodes):
        if not nodes:return 1
        bit=nodes&-nodes
        j=bit.bit_length()-1
        return independence_polynomial_minus_one(nodes^bit)-independence_polynomial_minus_one(nodes&~(bit|conflict[j]))
    return -independence_polynomial_minus_one((1<<q)-1)


def verify_color_mergers():
    tested=0
    # Check every face of all complexes with 2 to 5 colors.
    for n in range(2,6):
        adj2=graph_neighbors(2)
        for fs in independent_faces(n).values():
            for f in fs:
                for j in range(n):
                    image={2*(v//n)+(0 if v%n==j else 1) for v in f}
                    if any(adj2[a]>>b&1 for a,b in combinations(image,2)):
                        raise AssertionError((n,j,f,'image not independent'))
                    tested+=1
    return tested


def rank_gf2(columns):
    pivots={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i not in pivots:
                pivots[i]=col
                break
            col^=pivots[i]
    return len(pivots)


def mod2_betti(n):
    faces=independent_faces(n)
    ranks={}
    for size in range(1,max(faces)+1):
        if size==1:
            ranks[size]=1  # augmented differential to C_{-1}
            continue
        rows={f:i for i,f in enumerate(faces[size-1])}
        cols=[]
        for simplex in faces[size]:
            column=0
            for i in range(size):
                boundary=simplex[:i]+simplex[i+1:]
                column^=1<<rows[boundary]
            cols.append(column)
        ranks[size]=rank_gf2(cols)
    result={}
    for size,simplices in faces.items():
        if size==0:continue
        b=len(simplices)-ranks.get(size,0)-ranks.get(size+1,0)
        if b:result[size-1]=b
    return result,sum(len(v) for v in faces.values())


def main():
    assert collapse_base_case()==(122,48,26)
    assert orbit_trace(2,(1,0),list(range(5)))==-1
    assert orbit_trace(2,(0,1),[(-i)%5 for i in range(5)])==-1
    assert orbit_trace(2,(0,1),[(i+1)%5 for i in range(5)])==1
    maps=verify_color_mergers()
    char_tests=0
    for n in (2,3,4,5):
        for p in permutations(range(n)):
            fixed=sum(i==p[i] for i in range(n))
            for a in range(5):
                for b in (0,1):
                    site=[(a+(-i if b else i))%5 for i in range(5)]
                    assert orbit_trace(n,p,site)==(fixed-1)*(-1 if b else 1), (n,p,a,b)
                    char_tests+=1
    betti=[]
    for n in (2,3,4,5):
        h, faces=mod2_betti(n)
        assert h=={2:n-1}, (n,h)
        betti.append((n,faces,n-1))
    print('C5_PRODUCT_INTEGRAL_MODULE_CHECKS_OK',
          'base_collapse_pairs=48',
          'color_maps=',maps,
          'signed_lefschetz=',char_tests,
          'mod2_betti=',betti)

if __name__=='__main__':main()
