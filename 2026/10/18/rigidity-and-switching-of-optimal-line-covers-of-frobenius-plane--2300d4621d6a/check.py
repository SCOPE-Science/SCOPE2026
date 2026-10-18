"""Reproducible finite-field checks for covers of Frobenius plane curves."""
from itertools import combinations
from collections import Counter

def field(t,h,mod):
    q=t**h
    def coeff(a): return [(a//(t**i))%t for i in range(h)]
    def add(a,b):
        A,B=coeff(a),coeff(b)
        return sum(((A[i]+B[i])%t)*t**i for i in range(h))
    def neg(a): return sum(((-c)%t)*t**i for i,c in enumerate(coeff(a)))
    def mul(a,b):
        A,B=coeff(a),coeff(b); C=[0]*(2*h-1)
        for i in range(h):
            for j in range(h): C[i+j]=(C[i+j]+A[i]*B[j])%t
        for k in range(2*h-2,h-1,-1):
            c=C[k]
            for j in range(h): C[k-h+j]=(C[k-h+j]-c*mod[j])%t
        return sum(C[i]*t**i for i in range(h))
    def power(a,e):
        b=1
        while e:
            if e&1: b=mul(b,a)
            a=mul(a,a);e//=2
        return b
    for a in range(1,q):
        assert mul(a,power(a,q-2))==1
    return q,add,neg,mul,power

def classify(t,h,mod):
    q,add,neg,mul,power=field(t,h,mod)
    ys=[power(x,t) for x in range(q)]; allmask=(1<<q)-1
    lines=[]
    for m in range(q):
        for c in range(q):
            mask=sum(1<<x for x in range(q) if ys[x]==add(mul(m,x),c))
            lines.append((('nonvertical',m,c),mask,False))
            assert mask.bit_count() in (0,1,t)
    for x in range(q): lines.append((('vertical',x),1<<x,True))
    lines.append((('infinity',),0,True))
    return q,add,neg,mul,power,ys,lines,allmask

# F_9 = F_3[a]/(a^2+1).
t=3; q,add,neg,mul,power,ys,lines,allmask=classify(t,2,[1,0])
assert q==9
minimum=[]
for I in combinations(range(len(lines)),q//t+1):
    cov=0; at_inf=False
    for i in I:
        cov |= lines[i][1]; at_inf |= lines[i][2]
    if cov==allmask and at_inf: minimum.append(I)
assert len(minimum)==(t+1)*(q+1)==40, len(minimum)
for I in minimum:
    assert sum(lines[i][2] for i in I)==1
    assert sum(lines[i][1].bit_count()==3 for i in I)==3
    masks=[lines[i][1] for i in I if not lines[i][2]]
    assert len(set(masks))==3 and (masks[0]&masks[1])==0 and (masks[1]&masks[2])==0 and (masks[2]&masks[0])==0
print('GF(9): 40 exhaustive minimum covers (all 4-subsets of the 91 lines tested).')

# F_27 = F_3[a]/(a^3-a-1).
q,add,neg,mul,power,ys,lines,allmask=classify(3,3,[2,2,0]);assert q==27
A={add(a,mul(3,b)) for a in range(3) for b in range(3)};assert len(A)==9
u=1;v=3
# F_3-lines in the affine source vector space.
def coset(s,u): return frozenset(add(s,mul(c,u)) for c in range(3))
def partition(u): return set(coset(s,u) for s in range(q))
base=partition(u); assert len(base)==9
inside={L for L in base if L<=A}; assert len(inside)==3
replacement={L for L in partition(v) if L<=A};assert len(replacement)==3
switched=(base-inside)|replacement
assert len(switched)==9 and set().union(*(set(L) for L in switched))==set(range(q))
assert sum(bool(L & set(A)) for L in switched)==3
line_sets={frozenset(i for i in range(q) if (mask>>i)&1) for typ,mask,inf in lines if not inf and mask.bit_count()==3}
assert switched<=line_sets
assert switched!=base and replacement!=inside
print('GF(27): switched nonparallel partition by nine maximal secants verified.')
print('VERIFY_OK')
