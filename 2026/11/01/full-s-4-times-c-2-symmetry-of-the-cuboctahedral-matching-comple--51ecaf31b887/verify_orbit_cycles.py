"""Independent orbit-cycle check of the top rational homology character.
The character sum uses only disjoint unions of edge orbits, not simplicial traces.
"""
from itertools import permutations
from collections import defaultdict

Q=[(u,v) for u in range(8) for v in range(u+1,8) if (u^v) in (1,2,4)]
Q.sort()
E=[(a,b) for a in range(12) for b in range(a+1,12) if set(Q[a]).intersection(Q[b])]
assert len(Q)==12 and len(E)==24
qi={frozenset(e):i for i,e in enumerate(Q)}
ei={frozenset(e):i for i,e in enumerate(E)}
D=(frozenset((0,7)),frozenset((1,6)),frozenset((2,5)),frozenset((3,4)))

def perm_parity(xs):
    return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))

def cyc_type(g):
    todo=set(range(len(g)));lengths=[]
    while todo:
        x=next(iter(todo));z=x;n=0
        while z in todo:
            todo.remove(z);n+=1;z=g[z]
        lengths.append(n)
    return tuple(sorted(lengths,reverse=True))

def orbit_character(g):
    todo=set(range(24));masks=[]
    while todo:
        x=min(todo);y=x;members=[]
        while y in todo:
            todo.remove(y);members.append(y);y=g[y]
        bitmask=0
        for edge_idx in members:
            a,b=E[edge_idx];m=(1<<a)|(1<<b)
            if bitmask&m:break
            bitmask |= m
        else:masks.append(bitmask)
    def rec(i,used):
        if i==len(masks):return 1
        r=rec(i+1,used)
        if not used&masks[i]:r-=rec(i+1,used|masks[i])
        return r
    return rec(0,0)

class_char=defaultdict(set)
for ax in permutations(range(3)):
    for b in range(8):
        gv=[sum(((u>>i)&1)<<ax[i] for i in range(3)) ^ b for u in range(8)]
        det=perm_parity(ax)*(-1)**b.bit_count()
        r=[x^7 for x in gv] if det<0 else gv
        dperm=[D.index(frozenset(r[x] for x in d)) for d in D]
        qp=[qi[frozenset((gv[u],gv[v]))] for u,v in Q]
        ep=[ei[frozenset((qp[u],qp[v]))] for u,v in E]
        class_char[(cyc_type(dperm),int(det<0))].add(orbit_character(ep))
assert len(class_char)==10 and all(len(s)==1 for s in class_char.values())
expected={((1,1,1,1),0):57,((1,1,1,1),1):11,((2,1,1),0):3,((2,1,1),1):1,((2,2),0):13,((2,2),1):-1,((3,1),0):-3,((3,1),1):-1,((4,),0):-3,((4,),1):-5}
assert {key:next(iter(vals)) for key,vals in class_char.items()}==expected
for k in sorted(class_char):print(k,next(iter(class_char[k])))
print('ORBIT_VERIFY_OK')
