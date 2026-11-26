# Independent mathematical audit

## correctness

PASS

For fixed complex ℓ_p^d, normalize the first coordinate s≥0 and put t=||y||_p for the tail. The circled states e^{iθ}j_p(x)⊗x norm the operator space; by finite-dimensional polarity their convex hull is the full dual ball. For a pure state its deficit is δ=t^p+s^p(1−cosθ), so zero deficit forces the unique state F₀. Fourier averaging of conjugation by diag(e^{iϕ},1,…,1) extracts the off-diagonal first row or column with norm at most one. On each extracted rank-one subspace Hölder's equality and the scalar maximization of s^{p−1}(1−s^p)^{1/p} (or its transposed expression) give the exact dual norms ||y||_p/c_p and ||h||_q/c_p, with c_p=(p−1)^{(p−1)/p}/p. Expand the state about F₀: the phase/diagonal term is O(√δ), the tail block O(δ), and the row/column terms have sizes s^{p−1}t/c_p and st^{p−1}/c_p. Away from p=2 exactly the larger term survives at power 1/max(p,q); setting θ=0, t=ε^{1/p} and testing the corresponding single matrix unit realizes its coefficient. At p=2 the combined off-diagonal term has norm 2t by subtracting the two states at (e₁±y/t)/√2 and testing the swap. The leading bound |θ|+2t divided by √(t²+θ²/2) is ≤√6; with θ=t the block [[−i,1],[1,i]] has numerical radius 1 since (|z₂|²−|z₁|²)²+4Re(conj(z₁)z₂)²≤1 on its unit Hilbert sphere. It adds the phase and off-diagonal terms in phase to yield 3t+O(t²). Its deficit is 3t²/2+O(t⁴), and it can be chosen at any sufficiently small prescribed deficit by local monotonicity. Finally average the small-state estimates by concavity; the weight of states with deficit above fixed r>0 is at most ε/r, and their total norm error at most 2ε/r=o(ε^α). This establishes the sharp bound on the entire slice rather than merely on pure states. Fixed d and p are essential for the stated limiting argument; the leading coefficient has the asserted jump.

## originality

PASS

Credit the quantitative full-ball local asymptotic at the coordinate-exposed state, including the competing phase/spatial effects and the exceptional √6 coefficient at p=2. The accessible closest original statements identify extreme states, one-norming families and qualitative exposure, but do not evaluate the sharp slice distance as a function of deficit. The two-link scalar norm computation and the convex-hull representation are ingredients, not independently credited here. The strongest inspected indexed matches address radii/ranges of specific operators, not quantitative operator-dual exposure. This is a scoped best-of-knowledge decision.

## value

PASS

A coordinate projection is a natural exposure probe. The result gives a sharp quantitative guarantee on how far an approximately norming functional can be from the unique coordinate normer, including for mixtures. Dimension-independent leading constants and the noncontinuous sharp Hilbert coefficient show why qualitative exposure or off-Hilbert estimates do not capture this geometry. The result needs no claim about all exposed points or a dimension-uniform finite-depth error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
