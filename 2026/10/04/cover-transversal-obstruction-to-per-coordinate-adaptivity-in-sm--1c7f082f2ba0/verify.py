from itertools import product

def sm3_i_step(mu, cover, g, eta=1):
    mu = list(mu)
    for r,S in enumerate(cover):
        mu[r] += max(g[j]*g[j] for j in S)
    nu = []
    for i in range(len(g)):
        nu_i = min(mu[r] for r,S in enumerate(cover) if i in S)
        nu.append(nu_i)
    upd = [0 if nu[i] == 0 else eta*g[i]/(nu[i]**0.5) for i in range(len(g))]
    return mu, nu, upd

def sm3_ii_step(mu, cover, g, eta=1):
    nu = []
    for i in range(len(g)):
        past = min(mu[r] for r,S in enumerate(cover) if i in S)
        nu.append(past + g[i]*g[i])
    new_mu = []
    for S in cover:
        new_mu.append(max(nu[j] for j in S))
    upd = [0 if nu[i] == 0 else eta*g[i]/(nu[i]**0.5) for i in range(len(g))]
    return new_mu, nu, upd

def matrix_cover(m,n):
    def idx(a,b): return a*n+b
    rows = [{idx(a,b) for b in range(n)} for a in range(m)]
    cols = [{idx(a,b) for a in range(m)} for b in range(n)]
    return rows+cols, idx

m=n=3
cover, idx = matrix_cover(m,n)
target = idx(1,1)
H = {idx(1,0), idx(0,1)}
M = 7
delta = 2
g1 = [0]*(m*n)
for j in H:
    g1[j]=M
g2 = [0]*(m*n)
g2[target]=delta

for step in (sm3_i_step, sm3_ii_step):
    mu = [0]*len(cover)
    mu, nu, upd = step(mu, cover, g1)
    assert nu[target] == (M*M if step is sm3_i_step else 0)
    mu, nu, upd = step(mu, cover, g2)
    assert nu[target] == M*M+delta*delta
    expected = delta/((M*M+delta*delta)**0.5)
    assert abs(upd[target]-expected) < 1e-14

# Singleton AdaGrad takes unit-magnitude update on the target's first nonzero gradient.
singleton_cover = [{i} for i in range(m*n)]
mu = [0]*(m*n)
mu,nu,upd = sm3_i_step(mu,singleton_cover,g1)
mu,nu,upd = sm3_i_step(mu,singleton_cover,g2)
assert abs(upd[target]-1.0) < 1e-14

# No single off-target matrix coordinate hits both target row and target column.
target_sets = [S for S in cover if target in S]
for j in range(m*n):
    if j == target:
        continue
    assert not all(j in S for S in target_sets)
assert all(any(j in S for j in H) for S in target_sets)

# Tensor codimension-one slice covers have transversal number exactly two.
def tensor_cover(shape):
    coords = list(product(*[range(q) for q in shape]))
    pos = {c:k for k,c in enumerate(coords)}
    cover = []
    for axis,q in enumerate(shape):
        for value in range(q):
            cover.append({pos[c] for c in coords if c[axis] == value})
    return coords,pos,cover

for rank in range(2,6):
    shape = tuple([2]*rank)
    coords,pos,cov = tensor_cover(shape)
    tcoord = tuple([0]*rank)
    ti = pos[tcoord]
    tsets = [S for S in cov if ti in S]

    # one point differing only in axis 0, another only in axis 1
    a = list(tcoord); a[0] = 1
    b = list(tcoord); b[1] = 1
    H2 = {pos[tuple(a)], pos[tuple(b)]}
    assert all(any(j in S for j in H2) for S in tsets)

    # no single off-target coordinate hits every target slice
    for j,c in enumerate(coords):
        if j == ti:
            continue
        assert not all(j in S for S in tsets)

# Arbitrarily strong exact attenuation.
for ratio in (10,100,1000):
    M = ratio
    delta = 1
    attenuation = delta/((M*M+delta*delta)**0.5)
    assert attenuation < 1/ratio

print("verification passed")
