"""Independent oriented-chain quotient computation in numerically sorted vertex bases."""
import itertools,collections,json
from sympy import zeros,ZZ
from sympy.matrices.normalforms import smith_normal_form
p=11;Q={1,3,4,5,9}
def cyclic(a,b,c):
    e=lambda x,y:(y-x)%p in Q
    return (e(a,b) and e(b,c) and e(c,a)) or (e(a,c) and e(c,b) and e(b,a))
def legal(c):return all(not cyclic(*t) for t in itertools.combinations(c,3))
F={d:[tuple(c) for c in itertools.combinations(range(p),d+1) if legal(c)] for d in range(4)}
assert list(map(len,F.values()))==[11,55,110,55]
def permutation_sign(t):return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def check(H, cell_counts, snf_expected):
    J={}; representatives={d:[] for d in range(4)}
    for d in range(4):
        for simplex in F[d]:
            if simplex in J:continue
            ident=len(representatives[d]);representatives[d].append(simplex)
            for a,b in H:
                image=tuple((a*v+b)%p for v in simplex)
                sorted_image=tuple(sorted(image));sig=permutation_sign(image)
                assert J.get(sorted_image,(ident,sig))==(ident,sig)
                J[sorted_image]=(ident,sig)
    assert [len(representatives[d]) for d in range(4)]==cell_counts
    ranks={}; invariants={};B={}
    for d in range(1,4):
        D=zeros(len(representatives[d-1]),len(representatives[d]))
        for col,c in enumerate(representatives[d]):
            for i in range(d+1):
                row,orientation=J[c[:i]+c[i+1:]]
                D[row,col]+=(-1)**i*orientation
        B[d]=D
        S=smith_normal_form(D,domain=ZZ)
        diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
        ranks[d]=len(diag);invariants[d]=dict(sorted(collections.Counter(diag).items()))
    assert B[1]*B[2]==zeros(B[1].rows,B[2].cols)
    assert B[2]*B[3]==zeros(B[2].rows,B[3].cols)
    assert invariants==snf_expected
    return {'cells':cell_counts,'snf':invariants,'ranks':ranks}
r={
 'G':check([(a,b) for a in Q for b in range(p)],[1,1,2,1],{1:{},2:{1:1},3:{2:1}}),
 'C11':check([(1,b) for b in range(p)],[1,5,10,5],{1:{},2:{1:4,11:1},3:{1:4,2:1}}),
 'C5':check([(a,0) for a in Q],[3,11,22,11],{1:{1:2},2:{1:9},3:{1:10,2:1}})
}
print(json.dumps({'status':'verified','by_group':r},sort_keys=True))
