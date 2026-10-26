# Scientific review

## Correctness — PASS

The claim has explicit assumptions (square unit-capacity strict preferences with two or three agents) and a deterministic rule for selecting a symmetric priority lottery. Its invariance under reversal proves Dec-EF without any numerical inference. Exact rational enumeration compares two independently implemented algorithms—the continuous-eating PS rule and priority-by-priority serial dictatorship—for all four two-agent and all \(216\) three-agent labeled profiles. The 10 disjoint isomorphism classes and matrix table exhaust the domain; the source's four-agent obstruction is also independently reconstructed. The checker is part of this package and reports `ALL EXACT CHECKS PASSED`. Exhaustiveness is finite and no claim above three agents is extrapolated.

## Originality — PASS, subject to precedence limits

Kawase et al., arXiv:2604.16973 (full HTML, especially Section 3 and Example 5), prove the broader but different property that every three-agent SD-envy-free assignment matrix has some Dec-EF decomposition. Their proof uses generic permutation-matrix decomposition and does not implement PS by reversal-symmetric serial dictatorship. They identify a four-agent obstruction for exactly that strategy, so the four-agent negative is explicitly credited. The prior small-market PS-vs-uniform-RSD census gives the 144/72 split but not a profile-dependent distribution to repair the 72 exceptions. The two-preference-type random-priority theorem only certifies marginal envy-freeness, not exact PS implementation. Searches for weighted/reversal-symmetric priority implementation and equivalent mechanisms identified no stronger covering result. Remaining risk: unpublished or unindexed equivalences or priority-mixture classifications.

## Value — PASS

The original source explicitly raises reversal-symmetric serial dictatorship as a natural method for fair implementation and proves it fails at four agents, leaving its exact small-market positive reach unspecified. The new theorem supplies the complete, implementable positive frontier for that same natural method: an explicit four-order repair on precisely identified profiles, six-order baseline elsewhere, exact lotteries, and direct Dec-EF plus Pareto-efficiency of realized assignments. The classification has structural content beyond a routine restatement of EF-decomposability or of the known 144/72 comparison. It is a finite small-market theorem, not a new general decomposition theorem.

## Closest literature and limits

References: Kawase et al., arXiv:2604.16973 (Theorem 1 and Example 5); Hosseini, Larson and Cohen, arXiv:1503.01488; Bogomolnaia and Moulin (2001); the full public 3-agent PS-vs-RSD census and two-preference-type RSD-envy study listed in RESULT.md. Incentive compatibility, non-strict preferences, larger markets, and priority-support minimality are open beyond the stated result. Historical priority cannot be certified by a finite search.

Self-review: passed. Independent audit: not yet performed.
