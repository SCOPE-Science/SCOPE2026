# Independent mathematical audit

## correctness

PASS

The binary de Bruijn graph on order-(d−1) vertices is Eulerian: a cyclic order-d block B of length p=2^d visits each d-word exactly once. Hence for any ℓ>=d, p cyclic phases are distinct. A length-n prefix of B-periodic word contains at least floor((n−ℓ+1)/p) of each phase. With ℓ<=L=floor((n−p+1)/(p+1)), this is >=ℓ+1, so all p phase factors for d<=ℓ<=L qualify. Choose d=floor(0.5log2(n/log2 n)); for n>=64 prove L>=d by a=log2 n<=n/8 and show n−p(L−d+1)<n/p+p(d+1)<3sqrt(n a). Combining lower bound with published Theorem1 M_2(n)<=n yields limit exactly1. Independently an Euler-cycle implementation (different from source FKM recursion) directly counted qualifying binary factors for eight n, verifying each lower bound; no finite experiment proves the limit.

## originality

PASS

Bals et al. ESA 2026 Theorem1 gives <=n for all strings; Proposition6 gives asymptotic tightness by repeating r different letters r times over alphabet size r, which increases with n. The fixed-binary de Bruijn phase-distinctness construction is not obtained by setting a constant alphabet in that witness.

## value

PASS

Whether the universal n upper bound remains sharp over a fixed two-letter alphabet is a natural extremal question in frequent-factor counting/data structures. A uniform explicit binary witness and quantitative deficit bound resolves this alphabet-dependence rather than merely reproving a known n bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
