# Scientific review: two-unequal-spike random section radii

## Correctness — PASS

The exact radius identity follows from the equality of nonzero spectra of \(BB^{\mathsf T}\) and \(B^{\mathsf T}B\), with \(B\) the weighted projection of the two exceptional coordinate vectors into the random hyperplane. The \(2\times2\) determinant inequality is sufficient and necessary for the exact CDF because the lower-right diagonal entry of \(D-sI\) is positive for \(s\in(d_1,d_2)\). The first two squared coordinates of a Haar normal have the specified Dirichlet law. The coupled Gaussian strong law proves the critical and supercritical weak limits. The limiting supercritical matrix is positive definite almost surely because its determinant is \(c_2^{-2}G_1^2\). A conditional normal integral proves the precise tail constant by dominated convergence, and the layer-cake formula yields the sharp moment threshold. Bounded truncation plus weak convergence proves divergence of the normalized finite-dimensional expectations. No finite simulation is used to infer an infinite statement.

The separate standard-library checker independently restricts the full ellipsoid gauge to 420 sampled hyperplanes, diagonalizes the resulting matrix, and compares with the two-coordinate reduction (largest observed error below \(1.1\times10^{-13}\)). It also checks exact boundary normals and determinant events, and independently quadratures the tail constant. The analytical proof—not the checker—establishes the quantifiers and asymptotics.

## Originality — PASS, with residual risk

The motivating September 21, 2026 article by Guedon, Litvak, Tatarko, and Vritsiou studies random sections of general convex bodies and \(p\)-ellipsoids. Its relevant Section 6.3 treats semiaxes taking only two values, with high-probability order bounds; this does not imply a full CDF for two **distinct enlarged** semiaxes, the rank-two Gaussian limit, or its exact tail. The earlier full-text works by Hinrichs and collaborators establish general high-probability random-radius estimates, not the claimed explicit two-unequal-spike distribution. The closest public research-index record gives an exact beta law for **one** exceptional semiaxis; an affine change of coordinates cannot turn that law into the present one while preserving both the Euclidean radius and Haar hyperplanes. Searches using exact objects, aliases, Gaussian matrices, Dirichlet distributions, and the asymptotic moment transition found no result implying the full claim. Unindexed literature on low-rank secular eigenvalues or special Wishart laws is the principal priority risk; no absolute first-discovery guarantee is asserted.

## Mathematical value — PASS

For codimension one, optimal information eliminates the longest axis and has exact radius \(b\). The theorem determines the **entire** stochastic performance of Haar/Gaussian information for the first nontrivial unequal two-spike spectrum, through an exact finite-dimensional CDF and a critical \(\sqrt N\) limit. The transition from bounded, nondegenerate fluctuations to an unbounded limit with sharp \(t^{-1}\) tail and loss of every moment of order at least one is a structural quantitative benchmark for random-section geometry. This is not a numerical refinement, a single finite example, or a restatement of general order-of-magnitude bounds.

## Closest sources and limitations

- Guedon–Litvak–Tatarko–Vritsiou, arXiv:2609.24131 (2026), introduction and Section 6.3: general random radius bounds and two-valued axes.
- Hinrichs–Krieg–Novak–Prochno–Ullrich, arXiv:1901.06639 (2019), Sections 2 and 3: random information bounds for arbitrary ellipsoid spectra.
- Hinrichs–Prochno–Sonnleitner, arXiv:2109.14504 (2021), Sections 1–2: upper bounds for generalized ellipsoids.
- Public record titled *Exact random-radius law for one-spike ellipsoids in every codimension*, indexed with identifier `2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae`: a distinct one-spike exact law, examined through its accessible public summary.

The result does not treat two or more hyperplane measurements, additional exceptional axes, or noncentral affine sections. The heavy-tail claim concerns the weak limit and should not be transferred to finite-dimensional expectations without a separate uniform-integrability argument. The generic random-matrix literature may contain an equivalent statement under different terminology.

Self-review: passed. Independent audit: not yet performed.
