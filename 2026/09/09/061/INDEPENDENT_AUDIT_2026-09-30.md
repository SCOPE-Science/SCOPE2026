# Independent audit — SCOPE-20260909-061

Date: 2026-09-30 UTC

## Final claim

The normalized product of the three balanced-cut determinants has modulus one on the golden AME(4,6) tensor and vanishes on every pure four-quhex stabilizer state; the prime-power rank obstruction yields trace distance at least \(1-1/\sqrt{2}\) from the golden state to every pure stabilizer state, and the same overlap bound extends to their convex hull.

## Correctness

**PASS.** Rather et al. identify the golden AME state with a 36-by-36 2-unitary object, so each balanced flattening is unitary up to the normalization factor. Fresh calculation reproduces the determinant normalization exactly. Cha’s Theorem 1 factorizes every composite-dimension stabilizer state into prime-power stabilizer factors; together with nonexistence of AME(4,2) and stabilizer Schmidt-rank quantization, some balanced qubit cut has rank at most two, hence the corresponding quhex cut has rank at most 18 and one determinant factor vanishes. Cauchy–Schwarz on the reduced-state fidelity gives \(F\le 1/\sqrt{2}\), so trace distance is at least \(1-1/\sqrt{2}\). Wójcik et al. independently confirm the pure stabilizer no-go and the rank-two mixed \(2\)-uniform reference of purity \(1/2\). The package’s four verifier sources were inspected and their finite algebraic checks agree with these derivations.

Residual risk: The rank-quantization and determinant-ideal steps use standard stabilizer/algebraic-geometry facts rather than a fully formalized in-package proof; the golden value is deductive from published 2-unitarity rather than recomputed from all 1296 amplitudes.

## Originality

**PASS.** Rather et al. supplies the golden AME state, Cha and Wójcik et al. supply qualitative stabilizer nonexistence, and Wójcik et al. supplies the mixed purity-\(1/2\) reference. None of those sources gives the triple-determinant SLOCC gap, the rank-18 fidelity radius, or the degree/Lipschitz structural-invariant obstruction. A semantic published-results search found this record as the only exact match.

Equivalent formulations: Searched by golden AME(4,6), stabilizer, balanced-flattening determinant, SLOCC invariant, rank 18, and trace-distance radius; no prior equivalent quantitative statement was located.

Broader coverage: Cha and Wójcik establish nonexistence of pure stabilizer AME(4,6); those qualitative results do not dominate the explicit invariant value or quantitative distance lower bound.

Exact database or table: No relevant exact database/table supplies the determinant gap or radius. AME existence tables encode existence/nonexistence, not this quantitative separation.

Claim versus prior implication: Prime-power factorization plus no AME(4,2) implies qualitative nonexistence; obtaining the stated \(1-1/\sqrt{2}\) radius additionally uses the cut-rank bound and reduced-state fidelity calculation.

Residual risk: Very recent quantum-information preprints can change quickly; the September 28, 2026 Wójcik revision was checked, but an unindexed contemporaneous quantitative bound could exist.

## Value

**PASS.** The claim quantitatively separates a prominent non-stabilizer perfect tensor from a foundational efficiently describable state class. A certified robustness radius and invariant obstruction are useful for circuit approximation, code robustness and resource-state comparisons, so the result is more than a restatement of qualitative nonexistence.

Residual risk: The numerical radius is a general rank/fidelity consequence and may not be sharp for the stabilizer polytope.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/061/RESULT.md — Full result, definitions, proof and limitations inspected from the source blob.
- https://github.com/SCOPE-Science/SCOPE2026/tree/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/061/artifacts — All four verifier sources inspected: fidelity-radius normalization, AME(4,3) negative control, degree-6 epsilon wiring, and paired-Bell cut-rank witnesses.
- https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE061 — Semantic exact-claim search; this record was the direct match.
- https://arxiv.org/abs/2104.05122 — Rather et al. abstract inspected; it explicitly identifies the golden AME(4,6) state equivalently with a 2-unitary matrix of size 36.
- https://arxiv.org/html/2603.13442v2 — Cha full text inspected; Theorem 1 gives prime-power factorization of every stabilizer state and Corollary 1 rules out stabilizer AME(4,6).
- https://arxiv.org/html/2603.18193v3 — September 28, 2026 revision inspected; it rules out pure stabilizer AME(4,6) under prime-power reduction and gives the rank-two mixed \(2\)-uniform four-quhex state of purity \(1/2\).

## Disposition

**PASS.** Correctness, originality and value all pass the review bar.
