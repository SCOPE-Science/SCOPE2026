# Self-review

## Correctness
PASS. A generic diagonal row-column \(\mathbb C^*\)-action has pairwise distinct weights on all matrix coordinates, and matrix Schubert varieties are invariant under it. The projective fixed points are therefore coordinate matrices.

For \(E_{ij}\), every northwest rank is \(0\) until the submatrix includes \((i,j)\), then \(1\). Monotonicity reduces membership to
\[
r_w(i,j)\ge1,
\]
equivalent to
\[
i\ge m_j.
\]
Euler localization gives the formula. The bounds and equality cases follow symbolically from the prefix minima, and the bundled checker replays all coordinate rank conditions for every permutation through \(n=7\).

## Originality
PASS. The archival source studies the same varieties through determinantal ideals, multidegrees, Hilbert series, Gröbner bases, and pipe dreams but contains no Euler occurrence. A later same-object paper on diagonal degenerations has no located Euler or fixed-point occurrence.

Targeted literature and semantic-database searches did not locate the prefix-minimum formula or an equivalent coordinate-rank positivity count. Residual risk remains because the localization proof is short.

## Value
PASS. The result computes a natural topological invariant for every matrix Schubert variety and shows that it collapses the full permutation to its left-to-right minima. The exact extremal classification also identifies when a proper nonlinear variety is Euler-indistinguishable from ambient projective space.

Self-review: passed. Independent audit: not yet performed.
