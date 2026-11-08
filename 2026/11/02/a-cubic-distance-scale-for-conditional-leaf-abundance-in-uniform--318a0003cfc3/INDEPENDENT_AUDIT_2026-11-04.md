# Independent mathematical audit

## correctness

PASS

Conditioning a uniform n-label Cayley tree on its u–v path of ℓ edges gives an equally weighted rooted forest with r=ℓ+1 roots and m=n−r off-path vertices. The directed matrix-tree determinant equals (Σ_roots x_i)(Σ_all x_i)^(m−1), yielding one uniformly selected root child and m−1 independent uniform parent draws. The ℓ−1 internal path vertices cannot be leaves; eligible vertices are m off-path plus 2 endpoints; hence the exact mixture of empty-box counts X_{m+2} and X_{m+1} with weights (ℓ−1)/(ℓ+1) and 2/(ℓ+1). The mean h_n(ℓ)=(1−1/n)^(n−ℓ−2)[n−ℓ−1+2ℓ/(ℓ+1)] extends to the path boundary L=2. Difference h_n(ℓ+1)−h_n(ℓ) has sign of 2(n−1)−ℓ(ℓ+1)²; strict increasing ℓ(ℓ+1)² gives unique peak/ties, maximizing ℓ~(2n)^(1/3), ties only n=1+k(k+1)²/2. For n≥11, E[L|D3]>E[L|D2], yet P(L≥n−1|D2)=1/[3 n^(n−4)]>0, while P(L≥n−1|D3)=0: neither stochastic law dominates. This is all n≥2 with path boundary treated separately.

## originality

PASS

Pitman 1998 Theorem 1 already contains the rooted-forest child-count enumerator, and conditional occupancy mixture is its specialization. The new scope is not a novel forest count; it is the globally nonmonotone conditional total-leaf response, the exact cubic cutoff and infinitely recurring tie cases, and explicit stochastic-order incomparability. A published Resultary result covers conditional ENDPOINT DEGREE, not total leaf count; full source RESULT was compared directly. Best-of-knowledge priority qualified by older labeled-tree sources.

## value

PASS

Leaf abundance and marked-vertex distance are natural joint Cayley-tree observables. Contrary to an anticipated monotone response, the conditional total-leaf count has an exact cubic rather than ordinary square-root distance scale, a full arithmetic tie classification, and a systematic stochastic incomparability witness. These provide useful structural information beyond the known rooted-forest polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
