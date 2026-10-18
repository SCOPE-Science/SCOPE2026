# Independent direct point-substitution check of negative singularity witnesses.
from pathlib import Path
from functools import lru_cache
IRR={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def rem(p,q):
    while p and p.bit_length()>=q.bit_length():p^=q<<(p.bit_length()-q.bit_length())
    return p
for m,p in IRR.items():
    assert p.bit_length()==m+1
    for d in range(1,m//2+1):
        for q in range(1<<d,1<<(d+1)):
            assert rem(p,q)!=0,(m,q)

def multiply(a,b,m):
    mod=IRR[m];r=0
    while b:
        if b&1:r^=a
        b//=2;a*=2
        if a&(1<<m):a^=mod
    return r

@lru_cache(None)
def evaluations(m,ax,by):
    n=1<<m;inf_x=ax==n;inf_y=by==n
    X=0 if inf_x else ax;Y=0 if inf_y else by
    px=[1];py=[1]
    for j in range(3):px.append(multiply(px[-1],X,m));py.append(multiply(py[-1],Y,m))
    vals=[]
    for i in range(4):
        for j in range(4):
            ei=3-i if inf_x else i;ej=3-j if inf_y else j
            v=multiply(px[ei],py[ej],m)
            vx=multiply(px[ei-1],py[ej],m) if ei%2 else 0
            vy=multiply(px[ei],py[ej-1],m) if ej%2 else 0
            vals.append((v,vx,vy))
    return vals

D=Path(__file__).parent
cand=set(map(int,(D/'candidates.txt').read_text().splitlines()))
maskset=set()
for line in (D/'singular_witnesses.tsv').read_text().splitlines():
    mask,m,ax,by=map(int,line.split());assert mask not in maskset
    maskset.add(mask)
    vals=evaluations(m,ax,by)
    cur=mask;acc=[0,0,0]
    while cur:
        bit=cur&(-cur);idx=bit.bit_length()-1
        for j in range(3):acc[j]^=vals[idx][j]
        cur^=bit
    assert acc==[0,0,0],(mask,m,ax,by,acc)
assert len(maskset)==49515 and len(cand)==16020
assert not (maskset&cand) and maskset|cand==set(range(1,65536))
print('VALIDATED_IRREDUCIBLE_POLYNOMIALS',sorted(IRR))
print('VALIDATED_SINGULAR_POINT_WITNESSES',len(maskset))
print('UNLABELLED_EQUATIONS',len(cand))
print('TOTAL_NONZERO_EQUATIONS',len(maskset|cand))
