# Self-review

## Correctness — PASS
The stationary ratio is obtained from the specified finite irreducible birth–death generator. Its consecutive ratio factors into two explicit \(F_j\) terms, and \(F_j<1\) for all \(j\ge2\); hence only the boundary constraints can fail. The exact \(1/3\) population-uniform condition follows by letting the opposite index grow, including the equality cases. Reflection symmetry, the exact first two ratios and the strictly decreasing middle ratios prove the separate endpoint and log-concavity transitions, with the critical asymptotic derived from Taylor expansion. The full proof is in RESULT.md. The finite exact-rational test suite returned 114964 checks and selected asymptotic spot checks, not an infinite proof.

## Originality — PASS, with bounded uncertainty
The October 2026 Xiang–KhudaBukhsh manuscript establishes stationary weights and mixing cutoff behavior, but not these exact stationary count-index shape inequalities. A full-text SIAM Togashi–Kaneko comparison treats a differently normalized Moran/weighted-beta-binomial stationary law. The 2014 Saito–Kaneko paper's explicitly different count rates prevent direct implication of this coefficient criterion. Focused searches for log-concavity, beta-binomial coefficient products, and birth–death mode transitions found no covering statement. A broad hypergeometric-coefficient theorem may still imply it; that risk is explicitly not certified away.

## Mathematical value — PASS
Sharp stationary count log-concavity is a natural structural property of this stochastic reaction chain. The mutation ratios needed for uniform concentration are completely classified, and the symmetric model has a nontrivial interval of stationary unimodality without log-concavity; below it boundary and central local peaks coexist. These are useful exact boundaries, not simulation-derived parameter choices.

## Limitations and closest literature
No assertion is made about transient mixing laws, global highest peaks, other reaction generators, multitype systems, or historical priority beyond the inspected material. Closest sources: Xiang–KhudaBukhsh (2026), arXiv:2610.17775; *Fragility in a Togashi–Kaneko Stochastic Model with Mutations* (2026), SIAM; Saito–Kaneko (2014), arXiv:1403.6222. Independent replication has not been performed.

Self-review: passed. Independent audit: not yet performed.
