"""Triple-vertex motif certificates for non-isomorphic C2 pairs."""
import itertools,collections,json
from verify_triple_equivalences import get_objs,wl

def pair_color(v,u,partitions):
    return sum((1<<j) for j,p in enumerate(partitions) if p[v]==p[u])

def triangle_motif(p,vs):
    keys=[]
    for a,b,c in itertools.permutations(vs):
        keys.append((pair_color(a,b,p),pair_color(a,c,p),pair_color(b,c,p)))
    return min(keys)

def census(p):
    return collections.Counter(triangle_motif(p,v) for v in itertools.combinations(range(6),3))

if __name__=='__main__':
    pp,objs,_=get_objs(6)
    b=wl(pp,objs,6)
    groups=[g for g in b.values() if len(g)>1]
    all_pairs=[]
    for ix,g in enumerate(groups,1):
        a,b=(tuple(pp[t] for t in objs[i]) for i in g)
        ca,cb=census(a),census(b)
        assert ca[(0,0,0)]==0 and cb[(0,0,0)]==2
        diffs=[{'motif':list(m),'left_count':ca[m],'right_count':cb[m]} for m in sorted(set(ca)|set(cb)) if ca[m]!=cb[m]]
        print(ix,len(diffs),diffs[:3])
        all_pairs.append({'pair_index':ix,'left':[list(p) for p in a],'right':[list(p) for p in b], 'triple_motif_differences':diffs})
    with open('COLLISIONS.json','w',encoding='utf-8') as f: json.dump({'domain':'Three named equivalence relations on six elements; partition labels normalized by first appearance.','unlabelled_isomorphism_types':len(objs),'C2_equivalence_classes':len(b),'ambiguous_doubletons':all_pairs,'relation_label_symmetry_orbits_1indexed':[[1],[2,3,5],[4,6,7],[8]]},f,indent=2,ensure_ascii=False)
    print('certificate written')
