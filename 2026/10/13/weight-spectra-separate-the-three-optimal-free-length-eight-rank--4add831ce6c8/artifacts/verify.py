from collections import Counter

MATS = [
    [[1,0,0,1,1,0,1,0],[0,1,1,1,1,0,0,0]],
    [[1,0,0,1,1,1,1,1],[0,1,1,1,1,0,0,0]],
    [[1,0,0,0,0,1,1,1],[0,1,1,1,1,0,0,0]],
]
EXPECTED = [Counter({0:1,4:9,6:6}), Counter({0:1,4:3,6:6,8:6}), Counter({0:1,4:6,8:9})]

def add(a,b): return (a[0]^b[0], a[1]^b[1])

def scale_kappa_pair(coeff, bit):
    # Elements are u*kappa+v*zeta with (u,v) in F2^2. Since x*kappa=x, multiplying bit*kappa by coeff gives bit*coeff.
    return coeff if bit else (0,0)

def enumerate_E_code(G):
    words=[]
    for a in [(0,0),(1,0),(0,1),(1,1)]:
      for b in [(0,0),(1,0),(0,1),(1,1)]:
        w=[]
        for j in range(8):
          w.append(add(scale_kappa_pair(a,G[0][j]), scale_kappa_pair(b,G[1][j])))
        words.append(w)
    assert len({tuple(w) for w in words})==16
    return words

def wt(w): return sum(x!=(0,0) for x in w)

def binary_nonzero_weights(G):
    out=[]
    for a,b in [(1,0),(0,1),(1,1)]:
        v=[(a&G[0][j])^(b&G[1][j]) for j in range(8)]
        out.append(sum(v))
    support=sum(any(G[i][j] for i in range(2)) for j in range(8))
    return sorted(out),support

for idx,G in enumerate(MATS,1):
    dist=Counter(wt(w) for w in enumerate_E_code(G))
    assert dist==EXPECTED[idx-1], (idx,dist)
    bws,s=binary_nonzero_weights(G)
    # independent support-pair formula: 3 ordered coefficient pairs span each nonzero 1-space; 6 span all of F2^2.
    formula=Counter({0:1})
    for d in bws: formula[d]+=3
    formula[s]+=6
    assert formula==dist
    assert min(k for k,v in dist.items() if k>0) == 4
    print(idx, dict(sorted(dist.items())), 'binary', bws, 'full_support', s)
assert len({tuple(sorted(c.items())) for c in EXPECTED})==3
print('VERIFY_OK')
