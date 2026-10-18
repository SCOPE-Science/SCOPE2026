"""Self-contained combinatorial equivariant audit of the Paley-11 directed flag complex."""
import itertools, json, collections
p=11
qr={x*x % p for x in range(1,p)}
assert qr=={1,3,4,5,9}

def arc(x,y): return (y-x)%p in qr

def transitive(S):
    # Every nonempty sub-tournament of a transitive tournament has a unique source.
    V=list(S)
    while V:
        sources=[v for v in V if all(v==w or arc(v,w) for w in V)]
        if len(sources)!=1:return False
        V.remove(sources[0])
    return True
faces=[c for k in range(1,p+1) for c in itertools.combinations(range(p),k) if transitive(c)]
fvector=dict(sorted(collections.Counter(len(S)-1 for S in faces).items()))
assert fvector=={0:11,1:55,2:110,3:55},fvector
assert sum((-1)**d*n for d,n in fvector.items())==11
assert all(sum(arc(v,w) and arc(u,w) for w in range(p) if w!=u and w!=v)==2 for u in range(p) for v in range(p) if u!=v)

class_counts=collections.Counter(); trace_counts=collections.defaultdict(set)
for a in sorted(qr):
    for b in range(p):
        permutation=tuple((a*x+b)%p for x in range(p))
        assert all(arc(x,y)==arc(permutation[x],permutation[y]) for x in range(p) for y in range(p) if x!=y)
        fixed=[x for x in range(p) if permutation[x]==x]
        # Face stabilizers act pointwise on transitive tournaments: count the fixed faces.
        fixed_faces=[s for s in faces if all(permutation[x]==x for x in s)]
        euler=sum((-1)**(len(s)-1) for s in fixed_faces)
        character_h2=euler-1
        key='identity' if a==1 and b==0 else 'translation' if a==1 else 'nontranslation'
        class_counts[key]+=1
        trace_counts[key].add(character_h2)
        assert character_h2==len(fixed)-1
        assert len([s for s in faces if tuple(sorted(permutation[x] for x in s))==s])==len(fixed_faces)
assert dict(class_counts)=={'identity':1,'translation':10,'nontranslation':44}
assert {k:sorted(v) for k,v in trace_counts.items()}=={'identity':[10],'translation':[-1],'nontranslation':[0]}
assert (10+10*(-1)+44*0)==0
assert (10+10*(-1))==0
assert (10+4*0)==10
print(json.dumps({'qr':sorted(qr),'face_vector':fvector,'group_order':sum(class_counts.values()),'classes':dict(class_counts),'H2_character':{k:next(iter(v)) for k,v in trace_counts.items()},'invariant_H2_full_G':0,'invariant_H2_C11':0,'invariant_H2_C5':2},sort_keys=True))
