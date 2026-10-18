# Scientific review

## Correctness — PASS

The update matrices are reconstructed by substituting \(g=h^*=\|\cdot\|^2/2\), \(K=1\), and \(\gamma=\tau=1\) into the published Bernoulli-skip algorithm. Symbolic multiplication proves \(W-\mathcal L_p(W)=2D(p)I_2\) and the strictly positive determinant of \(W(p)\) for every \(p>0\). These identities imply a strict positive drift of the negative Lyapunov normalization below the unique positive root, strict negative drift above, and positive-definite energy conservation exactly at the root. Conditional expectations prove the all-iteration estimates for every nonzero deterministic starting state; no unjustified finite-to-infinite inference is made. The standalone program verifies 111 exact identities and path-enumeration comparisons. Its rational experiments are supplemental, not the proof.

## Originality — PASS, with risk

The primary RandProx paper [1] specifies this update family but provides a sufficient constraint that, at these fixed stepsizes, only covers \(p=1\). It does not imply the continuous probability interval of stable fixed stepsizes, the sharp nondecay boundary, or mean-square growth below it. Its ProxSkip specialization [1, Appendix A.1] and the original ProxSkip analysis [2] both scale the dual proximal parameter with the update probability, so their guarantees cannot be transplanted to the fixed parameter in this theorem. Semantic research-record searches and available earlier scientific claims found related random-sampling stability questions but not this specific two-branch map and its exact polynomial threshold. Residual risk: an equivalent two-dimensional random-matrix calculation may appear in unindexed or independently titled work; literature search is not independent priority certification.

## Value — PASS

Probability-scaled correction is used to make occasional proximal updates unbiased, but leaving both normalized primal and dual step parameters fixed as updates become rarer is a natural, operationally meaningful question. A generic sufficient condition provides no useful rare-update guarantee at unit steps; the theorem instead fully resolves the smallest strictly convex instance and exhibits both a nontrivial stable region and catastrophic second-moment growth across an exact boundary. Its positive-definite conserved form at equality separates bounded critical behavior from either geometric regime. This supplies a reproducible benchmark for probability/stepsize coupling; it does not imply a general algorithmic convergence theorem or a computational-cost claim.

## Closest literature and limitations

[1] Condat and Richtárik, *RandProx* (arXiv:2207.12891), Algorithm 5, Appendix A.1, Theorem 1: same update rule but broader sufficient, not sharp, conditions.

[2] Mishchenko et al., *ProxSkip* (arXiv:2202.09357), Algorithm 1 and convergence proof: different probability-scaled proximal update, not the fixed-dual-step dynamics.

The boundary applies only to the specific scalar quadratic, iid Bernoulli decisions, and the full-state second moment. Almost-sure trajectories, generic convex models, and other parameter schedules remain outside the claim. Independent comparison with all possible equivalent formulations is incomplete.

Self-review: passed. Independent audit: not yet performed.
