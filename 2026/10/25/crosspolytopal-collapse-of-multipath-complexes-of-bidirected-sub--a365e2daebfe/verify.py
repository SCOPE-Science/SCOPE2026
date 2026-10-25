"""Finite regression tests for the bidirected once-subdivided-forest collapse.
Only the Python standard library is required.  The theorem's proof is inductive;
finite checks here are independent tests of each local domination claim.
"""
from itertools import combinations
from collections import Counter
from random import Random

def forest(n, E):
    par = list(range(n))
    def root(u):
        while par[u] != u: u = par[u]
        return u
    for u, v in E:
        a,b=root(u),root(v)
        if a == b:return False
        par[a]=b
    return True

def build(n, E):
    arcs=[]; triples=[]
    for i,(u,v) in enumerate(E):
        w=n+i
        start=len(arcs)
        arcs += [(u,w),(w,u),(w,v),(v,w)]
        triples.append((u,v,w,start))
    return arcs,triples

def allowed(mask,arcs):
    incoming={};outgoing={}; selected=set()
    for i,(u,v) in enumerate(arcs):
        if not (mask>>i)&1:continue
        if u in outgoing or v in incoming or (v,u) in selected:return False
        outgoing[u]=v;incoming[v]=u;selected.add((u,v))
    # Directed cycles longer than 2 cannot occur on a subdivided forest.
    return True

def faces_for(arcs):
    return {s for s in range(1<<len(arcs)) if allowed(s,arcs)}

def check(n,E):
    arcs,details=build(n,E)
    faces=faces_for(arcs)
    originals=set(faces); preserved=[]; checks=0
    pending=list(range(len(E)))
    while pending:
        deg=Counter()
        for i in pending:
            u,v,w,j=details[i];deg[u]+=1;deg[v]+=1
        for i in pending:
            u,v,w,j=details[i]
            if deg[u]==1: leaf=i; direction=0;break
            if deg[v]==1: leaf=i; direction=1;break
        u,v,w,j=details[leaf]
        if direction==0:
            # a=leaf->subdivider, b=subdivider->leaf,
            # c=subdivider->core, d=core->subdivider.
            a,b,c,d=(j,j+1,j+2,j+3)
        else:
            a,b,c,d=(j+3,j+2,j+1,j)
        assert arcs[a]==(u if direction==0 else v,w)
        # Every face containing c admits a, so c is dominated by a.
        for face in faces:
            if (face>>c)&1:
                assert (face>>a)&1 or (face|(1<<a)) in faces
                checks+=1
        faces={mask for mask in faces if not (mask>>c)&1}
        # Every surviving face containing d admits b.
        for face in faces:
            if (face>>d)&1:
                assert (face>>b)&1 or (face|(1<<b)) in faces
                checks+=1
        faces={mask for mask in faces if not (mask>>d)&1}
        preserved.append((a,b))
        pending.remove(leaf)
    expected={0}
    for a,b in preserved:
        expected={f|choice for f in expected for choice in (0,1<<a,1<<b)}
    assert faces==expected
    assert len(faces)==3**len(E)
    # Reduced Euler characteristic of the original complex equals that
    # of the crosspolytope boundary, and is (-1)^(m-1).
    f=Counter(x.bit_count() for x in originals)
    reduced=-sum((-1)**k*v for k,v in f.items())
    assert reduced==(-1)**(len(E)-1)
    return len(originals),checks,len(expected)

def main():
    tests=0; faces=0; dom=0; maximum=0; edges_total=0
    for n in range(2,6):
        pair=list(combinations(range(n),2))
        for mask in range(1,1<<len(pair)):
            E=[pair[i] for i in range(len(pair)) if (mask>>i)&1]
            if not forest(n,E):continue
            f,c,e=check(n,E)
            tests+=1;faces+=f;dom+=c;maximum=max(maximum,f);edges_total+=len(E)
    # Additional seeded nonisomorphic-ish larger-branching examples, including
    # six-vertex paths, stars, double-stars, and two brooms.
    large=[[(0,1),(1,2),(2,3),(3,4),(4,5)],
           [(0,i) for i in range(1,6)],
           [(0,1),(0,2),(0,3),(3,4),(3,5)],
           [(0,1),(0,2),(0,3),(1,4),(4,5)],
           [(0,1),(0,2),(1,3),(1,4),(4,5)]]
    for E in large:
        f,c,e=check(6,E)
        tests+=1;faces+=f;dom+=c;maximum=max(maximum,f);edges_total+=len(E)
    print('PASS', 'forests',tests,'total_original_faces',faces,
          'domination_face_checks',dom,'largest_complex_faces',maximum,
          'total_graph_edges_across_tests',edges_total)

if __name__=='__main__':main()
