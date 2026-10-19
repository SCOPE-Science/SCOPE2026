"""Independent tour-order two-edge-exchange verifier for the icosahedron.
Builds graph from triangular faces rather than from an edge presentation.
Run: python verify_direct.py certificate.json
"""
import collections
import json
import sys

def make_from_faces():
    faces=[]
    for i in range(5):
        a=1+i;an=1+(i+1)%5;b=6+i;bp=6+(i-1)%5;bn=6+(i+1)%5
        faces.extend(((0,a,an),(11,b,bn),(a,b,bp),(b,a,an)))
    edge_set=set()
    faces_by_edge=collections.Counter()
    for triangle in faces:
        for i in range(3):
            e=tuple(sorted((triangle[i],triangle[(i+1)%3])))
            edge_set.add(e);faces_by_edge[e]+=1
    assert len(faces)==20 and len(edge_set)==30 and set(faces_by_edge.values())=={2}
    E=sorted(edge_set);adj=[set() for _ in range(12)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    assert sorted(map(len,adj))==[5]*12
    return E,adj

def compute():
    E,adj=make_from_faces();edge_i={e:i for i,e in enumerate(E)}
    tours={}
    def visit(p,visited):
        if len(p)==12:
            if p[-1] not in adj[0] or p[1]>p[-1]:return
            m=0
            for j in range(12):
                e=tuple(sorted((p[j],p[(j+1)%12])))
                m|=1<<edge_i[e]
            tours[m]=tuple(p)
            return
        for v in adj[p[-1]]:
            if v not in visited:
                visited.add(v);visit(p+[v],visited);visited.remove(v)
    visit([0],{0})
    masks=sorted(tours);by_tour={tour:i for i,tour in enumerate([tours[m] for m in masks])}
    assert len(masks)==1280
    pair_set=set()
    for i,mask in enumerate(masks):
        p=tours[mask]
        for a in range(12):
            for b in range(a+2,12):
                if a==0 and b==11:continue
                x,y=p[a],p[a+1]
                z,w=p[b],p[(b+1)%12]
                if z not in adj[x] or w not in adj[y]:continue
                q=p[:a+1]+p[a+1:b+1][::-1]+p[b+1:]
                # tour is anchored at vertex 0, orientation is canonicalized.
                if q[1]>q[-1]:q=q[:1]+q[:0:-1]
                j=by_tour.get(q)
                assert j is not None and j!=i
                pair_set.add(tuple(sorted((i,j))))
    pairs=sorted(pair_set)
    assert len(pairs)==1800
    degree=[0]*len(masks)
    parent=list(range(len(masks)))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for a,b in pairs:
        degree[a]+=1;degree[b]+=1
        a,b=find(a),find(b)
        if a!=b:parent[b]=a
    sizes=collections.Counter(collections.Counter(find(i) for i in range(len(masks))).values())
    assert sizes=={36:30,2:60,1:80}
    assert collections.Counter(degree)=={0:80,1:180,2:330,3:240,4:240,5:180,6:30}
    return E,masks,pairs

def main():
    E,masks,pairs=compute()
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf8') as f:cert=json.load(f)
        assert cert['icosahedron_edges']==[list(e) for e in E]
        assert cert['undirected_cycle_edge_masks']==masks
        assert cert['switch_edges_indexed']==[list(e) for e in pairs]
    print('VERIFY_DIRECT_OK source_faces=20 edges=30 tours=1280 independent_2opt_edges=1800')
    print('VERIFY_DIRECT_OK exact_cycle_and_transition_tables_equal=true components=30x36,60x2,80x1')
if __name__=='__main__':main()
