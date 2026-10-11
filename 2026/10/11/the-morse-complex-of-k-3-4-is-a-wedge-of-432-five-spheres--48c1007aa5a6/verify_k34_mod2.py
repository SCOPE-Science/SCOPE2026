"""Independent exhaustive mod-2 simplicial boundary calculation for M(K_3,4)."""
from itertools import product
from collections import defaultdict


def all_faces():
    vertices=range(7)
    outgoing={u:([3,4,5,6] if u<3 else [0,1,2]) for u in vertices}
    choices=[[-1]+outgoing[u] for u in vertices]
    dart_positions={(u,v):i for i,(u,v) in enumerate((u,v) for u in vertices for v in outgoing[u])}
    faces=[]
    for nxt in product(*choices):
        cyclic=False
        for root in vertices:
            reached=set()
            v=root
            while v!=-1:
                if v in reached:
                    cyclic=True
                    break
                reached.add(v)
                v=nxt[v]
            if cyclic:
                break
        if not cyclic:
            face=0
            for u,v in enumerate(nxt):
                if v!=-1:
                    face |= 1<<dart_positions[u,v]
            faces.append(face)
    return faces


def mod2_ranks(faces):
    bydim=defaultdict(list)
    for s in faces:
        bydim[s.bit_count()-1].append(s)
    fvector={k:len(v) for k,v in bydim.items()}
    assert fvector=={-1:1,0:24,1:234,2:1192,3:3357,4:4968,5:3024}
    ranks=[]
    for k in range(6):
        positions={s:i for i,s in enumerate(bydim[k-1])}
        pivots={}
        for s in bydim[k]:
            column=0
            rest=s
            while rest:
                b=rest&-rest
                rest-=b
                column ^=1<<positions[s^b]
            while column:
                leading=column.bit_length()-1
                if leading in pivots:
                    column ^=pivots[leading]
                else:
                    pivots[leading]=column
                    break
        ranks.append(len(pivots))
    assert ranks==[1,23,211,981,2376,2592],ranks
    # Reduced H5 = ker d5 = 3024-2592; H4 vanishes.
    assert 3024-ranks[5]==432
    assert 4968-ranks[4]-ranks[5]==0
    for k in range(1,4):
        assert len(bydim[k])-ranks[k]-ranks[k+1]==0
    # Characteristic polynomial / matrix-tree independent check:
    # spectrum of Laplacian K_3,4: 0,3 (mult. 3),4 (mult. 2),7.
    # det(I-L) = (1-3)^3 (1-4)^2 (1-7) = 432.
    assert ((1-3)**3)*((1-4)**2)*(1-7)==432
    print('MOD2_OK faces=12799_nonempty ranks=1,23,211,981,2376,2592 beta5=432 det_I_minus_L=432')


if __name__=='__main__':
    mod2_ranks(all_faces())
