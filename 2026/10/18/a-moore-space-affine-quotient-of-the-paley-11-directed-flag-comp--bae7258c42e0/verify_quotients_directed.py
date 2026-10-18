"""Integral homology of the topological quotients, using ordered tournament simplices."""
import collections,itertools,json
from sympy import zeros,ZZ
from sympy.matrices.normalforms import smith_normal_form
p=11;Q={1,3,4,5,9}
def arc(a,b):return (b-a)%p in Q
def ordering(s):
    # Each source in a transitive tournament is its unique maximal outdegree vertex.
    s=list(s);seq=[]
    while s:
        sources=[x for x in s if all(x==y or arc(x,y) for y in s)]
        if len(sources)!=1:return None
        z=sources[0];s.remove(z);seq.append(z)
    return tuple(seq)
K={d:[] for d in range(4)}
for j in range(1,12):
    for s in itertools.combinations(range(p),j):
        v=ordering(s)
        if v is not None:
            assert j<=4,(j,v)
            K[j-1].append(v)
assert [len(K[d]) for d in range(4)]==[11,55,110,55]

def quotient(name,H,expected_cells,expected_smith,expected_betti):
    orb_index={};reps={d:[] for d in range(4)}
    for d in range(4):
        for s in K[d]:
            if s in orb_index:continue
            idx=len(reps[d]);reps[d].append(s)
            for a,b in H:
                t=tuple((a*x+b)%p for x in s)
                assert t in K[d]
                assert orb_index.get(t,idx)==idx
                orb_index[t]=idx
    sizes=[len(reps[d]) for d in range(4)]
    assert sizes==expected_cells,(name,sizes)
    mat={}; smith={};ranks={}
    for d in (1,2,3):
        B=zeros(sizes[d-1],sizes[d])
        for j,s in enumerate(reps[d]):
            for i in range(d+1):
                B[orb_index[s[:i]+s[i+1:]],j]+=(-1)**i
        mat[d]=B
        S=smith_normal_form(B,domain=ZZ)
        nonzero=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
        smith[d]=dict(sorted(collections.Counter(nonzero).items()))
        ranks[d]=len(nonzero)
    assert mat[1]*mat[2]==zeros(sizes[0],sizes[2])
    assert mat[2]*mat[3]==zeros(sizes[1],sizes[3])
    betti=[sizes[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(4)]
    assert smith==expected_smith,(name,smith)
    assert betti==expected_betti,(name,betti)
    return {'cells':sizes,'boundary_ranks':ranks,'smith_invariants':smith,'betti':betti,'full_quotient_d2':list(map(int,mat[2])) if name=='G' else None,'full_quotient_d3':list(map(int,mat[3])) if name=='G' else None}

R={}
R['G']=quotient('G',[(a,b) for a in sorted(Q) for b in range(p)],[1,1,2,1],{1:{},2:{1:1},3:{2:1}},[1,0,0,0])
R['C11']=quotient('C11',[(1,b) for b in range(p)],[1,5,10,5],{1:{},2:{1:4,11:1},3:{1:4,2:1}},[1,0,0,0])
R['C5']=quotient('C5',[(a,0) for a in sorted(Q)],[3,11,22,11],{1:{1:2},2:{1:9},3:{1:10,2:1}},[1,0,2,0])
print(json.dumps({'quotients':R,'interpretation':{'G':'M(Z/2,2)','C11':'H1=Z/11,H2=Z/2','C5':'H2=Z^2+Z/2'}},sort_keys=True))
