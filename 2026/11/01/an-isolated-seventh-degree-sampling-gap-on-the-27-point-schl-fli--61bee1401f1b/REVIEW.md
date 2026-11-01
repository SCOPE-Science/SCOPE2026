# Scientific review: Schläfli all-degree harmonic sampling

## Correctness — PASS

The statement fixes all 27 points by explicit unit coordinates on the real six-dimensional sphere ambient space. There are just two distinct inner products, \(1/4\) and \(-1/2\). Exact enumeration proves the associated adjacency matrix satisfies \(A\mathbf1=16\mathbf1\) and \(A^2=8I+2A+8J\), hence its eigenspace dimensions are \(1,6,20\) at eigenvalues \(16,4,-2\). The Gegenbauer addition theorem gives the displayed three-sector Gram spectrum without a numerical eigensolver. The exact recurrence yields all entries at degrees zero through eight, including the rank-26 cancellation at degree seven. The Chebyshev-derivative bound proves every Gram sector is strictly positive for all integers \(k\ge9\), closing the infinite range. The separately evaluated exact rational row reductions on all nine low-degree Gram matrices agree with the spectral ranks. The harmonic-index statement follows from the positive-semidefinite sum-of-squares expression for the constant sector.

The standalone checker runs with the Python standard library and was replayed from its actual package path, ending in `SCHLAEFLI_ALL_DEGREE_CERTIFICATE_OK 27 points, 9 exact ranks`. Finite checks do not substitute for the analytic large-degree proof; both components are necessary. All critical hypotheses, quantifiers, Gram normalizations and boundary degrees are explicit.

## Originality — PASS under bounded source review

The historical starting point is *not* claimed new: the 27-point Schläfli orbit is a unique tight spherical four-design, its two inner products and multiplicities were already determined, and the Gegenbauer addition formula is classical. Boyvalenkov's 1995 full article was compared at its distance-distribution theorem and uniqueness proof. Bannai–Okuda–Tagami's 2013 harmonic-index preprint and Zhu et al.'s 2015 extension were inspected at their definitions, addition-kernel identities, constructions and principal conclusions, with whole-text checks for 27-point Schläfli or interpolation claims. These sources cover the framework and early cancellations but do not assert the complete exact-degree evaluation ranks, the isolated seventh-degree failure after surjectivity, or the all-high-degree theorem.

Additional searches of published mathematical records for Schläfli, 27 lines, E6, harmonic-index seven, exact-degree interpolation, Gegenbauer sampling and numerical rank sequences found closest records on the 27-line incidence graph and other exceptional configurations, neither of which implies this statement. The classical Weyl-invariant degrees may explain the absence of an invariant seventh harmonic but do not by themselves determine the entire rank-26 image at degree seven or all later ranks. The older E7/Gosset harmonic sampling statement concerns 56 antipodal points in a different ambient sphere and is not a specialization of the present statement.

The inference from established two-distance parameters to a full all-degree rank classification does require exact evaluation of the three Gegenbauer spectral branches and a separate uniform positivity argument. Nonetheless older exceptional association-scheme, spherical cubature or Weyl-harmonic literature might contain an equivalent computation or a stronger theorem; this is a residual originality risk, not a claim of exhaustive uniqueness.

## Mathematical value — PASS

The problem asks when a single exact spherical-harmonic degree interpolates all values on the canonical 27-point tight four-design. The result determines all ranks and complete Gram spectra, gives the first full-rank degree \(5\), proves an isolated loss of surjectivity at degree \(7\), and identifies the eventual full-rank threshold \(8\). It also classifies precisely all harmonic-index cancellation degrees, yielding a natural property beyond the classical four-design strength. These are motivated exact interpolation and harmonic-index invariants of a unique exceptional configuration, not arbitrary numerical slices or routine restatements of known graph parameters.

## Closest literature and limitations

- Peter Boyvalenkov, *Computing distance distributions of spherical designs*, Linear Algebra and its Applications 226–228 (1995), 277–286, DOI `10.1016/0024-3795(95)00153-I`: establishes two-distance data and uniqueness for the tight four-design, not the all-degree evaluation rank table.
- Eiichi Bannai, Takayuki Okuda and Makoto Tagami, *Spherical designs of harmonic index t*, arXiv `1308.5101v1` (2013-08-23): definitions, constructions and lower bounds, without the specific Schläfli interpolation calculation.
- Yan Zhu et al., *More on spherical designs of harmonic index t*, arXiv `1507.05373` (2015-07-20): addition-kernel formula and harmonic-index classification theory, not the exact 27-point all-degree ranks.
- Classical Schläfli graph eigenparameters and Weyl-invariant degrees imply part of the spectral reduction or the degree-seven cancellation, respectively; neither alone gives the full theorem. Future expert comparison to older association-scheme tables is desirable.

The proof does not provide optimal numerical interpolation conditioning, generalize to arbitrary weights, or claim an independent audit. Inaccessible or unindexed historical work remains possible.

Self-review: passed. Independent audit: not yet performed.
