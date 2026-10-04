from itertools import product, permutations

ALPH=(0,1,2)
PERMS=tuple(permutations(ALPH))
NUM={
    '0000':10,
    '0001':8,
    '0010':5,
    '0011':7,
    '0012':6,
    '0101':3,
    '0102':4,
    '0110':7,
    '0112':6,
    '0120':4,
}
BASE=('00121','00200','01010','01022','01112','02120','02221')

def delete_desc(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def canonical(w):
    cands=[]
    for p in PERMS:
        trans=''.join(str(p[int(ch)]) for ch in w)
        cands.append(trans)
        cands.append(trans[::-1])
    return min(cands)

def translate(w,k):
    return ''.join(str((int(ch)+k)%3) for ch in w)

U={''.join(map(str,t)) for t in product(ALPH, repeat=4)}
W={''.join(map(str,t)) for t in product(ALPH, repeat=5)}
assert len(U)==81 and len(W)==243

orbits={}
for y in U:
    can=canonical(y)
    assert can in NUM, (y,can)
    orbits.setdefault(can,[]).append(y)
assert {k:len(v) for k,v in orbits.items()} == {
    '0000':3,'0001':12,'0010':12,'0011':6,'0012':12,
    '0101':6,'0102':12,'0110':6,'0112':6,'0120':6,
}

total_num=sum(NUM[canonical(y)] for y in U)
assert total_num==468,total_num
mx=-1; sat=[]
for c in sorted(W):
    s=sum(NUM[canonical(y)] for y in delete_desc(c))
    assert s<=23,(c,s,delete_desc(c))
    if s>mx: mx=s; sat=[c]
    elif s==mx: sat.append(c)
assert mx==23

C={translate(b,k) for b in BASE for k in ALPH}
assert len(C)==21
covered=set().union(*(delete_desc(c) for c in C))
assert covered==U,(len(covered),sorted(U-covered)[:10])

# Check listed generators are from distinct translation orbits.
for i,b in enumerate(BASE):
    orb={translate(b,k) for k in ALPH}
    for j,b2 in enumerate(BASE):
        if i!=j:
            assert b2 not in orb

print('targets=81 candidates=243 codewords=21')
print('dual_total=468/23 max_ball_numerator=23 saturated_candidates=%d' % len(sat))
print('covered=81')
print('VERIFY_OK')
