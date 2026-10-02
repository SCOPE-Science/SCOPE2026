# Independent audit — 2026-10-01

## Record

**Sharp C(K) dichotomy for metric-functional weak convergence**

Final claim: For real \(C(K)\) with \(K\) compact Hausdorff, the metric-functional weak topology equals the classical weak topology exactly when \(K\) is finite; if \(K\) is infinite, every prescribed positive norm profile is realized by a pairwise-disjoint nonnegative metric-functionally weak-null sequence.

Disposition: **REPAIRED**

## Correctness — PASS

The repaired proof is self-contained: every infinite compact Hausdorff space has countably many pairwise-disjoint nonempty open sets; normality supplies supported bumps. For any internal metric functional \(h_w\), a norm-attainment point lies in at most one support, so \(h_w(f_n)\ge0\) except possibly once. Pointwise limits inherit this property, giving d-weak convergence for arbitrary amplitudes. The finite case follows from the already-known finite-dimensional topology equality.

## Originality — PASS

An earlier 2026-09-18 published result already proves the general weak-topology sandwich, extreme-dual span criterion, finite-dimensional equality and strictly-convex-dual equality, so those claims are removed from the repaired novelty claim. Gutiérrez–Nevanlinna's 2026 topology preprint states an unbounded d-weak-null sequence only in \(C[0,1]\). No inspected source or published-record search supplied the all-compact-Hausdorff \(C(K)\) dichotomy or arbitrary positive norm profiles.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Primary-source inspections and residual access risks are also recorded there.

## Scientific value — PASS

The repaired theorem gives a natural exact classification for the standard Banach-space family \(C(K)\) and strengthens a single-space counterexample to all infinite compact Hausdorff spaces with arbitrary prescribed growth, while explicitly excluding the already-covered general topology comparison.

## Checked scientific sources

- Gutiérrez–Nevanlinna, A Weak Topology on Metric Spaces, arXiv:2609.19368.
- Gutiérrez–Nevanlinna, Metric functionals and weak convergence, Z. Anal. Anwend. (2026), arXiv:2506.04154.
- Walsh, Hilbert and Thompson geometries isometric to infinite-dimensional Banach spaces, Ann. Inst. Fourier 68 (2018).
- Earlier published record: Extreme-dual recovery of the classical weak topology from metric functionals (2026-09-18).
- Published-record semantic search for metric-functional topology on C(K).

## Residual risks

- The repaired construction is conceptually close to the recent \(C[0,1]\) disjoint-support counterexample, so parallel or subsequent generalization is a material residual risk.

## Verification boundary

The audit reconstructed the argument and performed fresh algebraic or logical checks where needed. Existing package logs were treated as supporting evidence only. No formal proof-assistant or expert attestation is asserted.
