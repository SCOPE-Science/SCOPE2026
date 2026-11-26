# Independent mathematical audit

## correctness

PASS

Using a=2^p and b=3^p, the compressed powered-distance form on the real mean-zero space has n(t−1) internal leaf directions with eigenvalue −a, n−1 identical two-by-two blocks with first entry −1 and determinant t[b+a−a²−1+a/t], and the contrast (−t on cores, +1 on leaves) with form nt²H. Concavity gives H<0 and positive block determinants for 0≤p≤1, including the specified diagonal convention at p=0. H is increasing from −2/t to 2n−4/t on [1,2] and strictly increasing thereafter. For 1<p≤α, H≤0 gives det/t≥nF−(a−2)²>0: F≥(a−2)²/2 follows from strict concavity of a^(log_2 3)−a²/2−1 on [2,4]. Thus only the global contrast is null at α, giving centered Gram rank N−2, versus N−1 below. A distinct-point Euclidean realization gives strictly positive Gaussian kernels even at α; above α the first-order expansion on the global contrast produces a negative direction at small positive scales, and the unit diagonal gives a positive direction. H increases in either integer size at fixed p>1, and Taylor expansion at 1 with slope (n−1)c+2(1−1/t)log 2 and α−1≤2/[t(n−1)c] gives both asymptotic orders. Independent bisection gives the two stated numerical anchors (1.70951129135145 and 1.38018235538565); these are illustrative, not a proof. The original checker and its recorded replay were inspected, not re-executed.

## originality

PASS

Credit the full one-leaf unit-edge special case, including the endpoint and its large-core limit, to demonstrated coverage in a distinct same-day indexed result; no date-based priority inference is made. The supported distinct contribution is the multiplicity-dependent classification for t≥2, including the exact obstruction, absence of other vanishing modes, and the large-multiplicity regime. The strongest inspected sources do not derive that classification, and the weighted one-leaf tangent calculation does not control the new multiplicity term.

## value

PASS

For t≥2 the exact exponent directly decides all-scale Gaussian-kernel validity for a natural family of graph metrics and specifies the minimum embedding dimension at the critical parameter. The proof identifies the global contrast as the only obstruction despite extra leaf modes, and the two size limits distinguish adding core vertices from adding leaves. The value rests on that full multiplicity-dependent threshold and endpoint structure, not on the already covered t=1 case or two numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
