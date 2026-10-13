# Self-review

## Correctness — PASS

The exact block-energy expansion proves the finite-parameter theorem without an unverified structural lemma. For positive orientations the rowwise nonnegativity lower bound yields an explicit neighborhood certificate. For subcritical orientations a feasible singleton perturbation has negative second-order term. At the exact boundary the constrained second variation is nonnegative, but an explicitly normalized rotation of the positive head profile combined with a singleton perturbation lowers energy by precisely half the square of the perturbation parameter. All hypotheses, including strictly positive orientation and enough factor columns to attain the global zero loss, are used. The standalone exact-rational verification exercises the polynomial identities and perturbation inequality; it does not substitute for proof of universal statements.

## Originality — PASS (with residual risk)

Richard Y. Zhang, *Nonnegative Low-rank Matrix Recovery Can Have Spurious Local Minima* (arXiv:2505.03717, Theorem 4 and Lemma 12), already proves the balanced-profile spurious minimum for \(m>r\); that case is not new. The full text's statement and proof fix equal positive factor coordinates and do not classify general orientations, their sharp necessity, or the second-order stationary but nonminimizing equality stratum. The new assertion concerns the entire continuous, Gram-equivalent stationary family and its threshold, not just a separate imbalance example. Related symmetric-factorization algorithms (Hayashi et al., DOI:10.1137/24M1638355) and unconstrained benign-landscape work address different questions. Published-record searches returned no statement covering the orientation classification; this is not proof of universal novelty. Potentially unindexed equivalent analyses and simple extensions of the cited block proof remain limitations.

## Value — PASS

The phase diagram resolves a natural ambiguity in the motivating cluster-collapse counterexample: identical low-rank Gram matrices, identical loss, and zero first derivative do **not** determine local-minimum status under nonnegativity. It identifies precisely which latent positive orientations are traps, which are negative-curvature directions, and which satisfy second-order tests yet have higher-order escape. The explicit one-sided stability tube and sharp rank-versus-cluster-size existence condition characterize practical landscape geometry rather than an arbitrary enumeration or numerical slice. It does not claim a general algorithmic convergence theorem.

## Limitations

This covers only the collapsed-block stationary fiber of the fully observed nonnegative symmetric Gram loss. The initial 2025 public version and later 2026 journal version of Zhang's paper are the same motivating source, not two independent results. General nonnegative factorization landscapes may exhibit other stationary types. The exact second-order escape and the value assessment have not undergone independent validation.

Self-review: passed. Independent audit: not yet performed.
