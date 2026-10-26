# Review: Correct level-set constant for a homogeneous finite-time control bound

## Correctness — PASS

The HJB equation and the optimal feedback give \(\dot V_\infty\leq-F\). Properness and positive definiteness make \(K=\{V_\infty=1\}\) compact, so \(m=\min_KF>0\). Weighted homogeneity then yields \(F(x)\geq mV_\infty(x)^{d/(d+\mu)}\), and integrating the resulting scalar differential inequality gives the stated bound. An admissible anisotropic example proves that \(\min_KF\) and \(\max_KF\) need not coincide.

## Originality — PASS, with scope limitation

The contribution is a source-specific correction to the coefficient used in Theorem 6.5 of the 2026 preprint, not a claim to a new general finite-time comparison theorem. The generic comparison principle is established in prior work; the inspected source's use of the maximum does not furnish the lower bound its displayed argument requires. Targeted searches found no exact equivalent correction, but search absence does not prove global uniqueness.

## Value — PASS

A settling-time upper bound is a quantitative control guarantee. Correctly identifying the level-set extremum prevents the proof from using an upper bound where a lower comparison coefficient is required. The minimum-based replacement is explicit, valid under the stated assumptions, and backed by an admissible example showing the distinction is substantive.

## Closest literature and limitations

- Weng, Chitour, and Mason, arXiv:2607.22191v1, Theorem 5.1, Lemma 6.1, and Theorem 6.5.
- Bhat and Bernstein, DOI 10.1137/S0363012997321358: foundational finite-time Lyapunov comparison; full PDF was not accessible in this review.
- Kisole, Garg, and Peet, arXiv:2501.11255: explicit general settling-time bound from \(\dot V\leq-aV^\gamma\).

No trajectory-level counterexample to the source's printed maximum-based numerical bound is claimed; the result establishes the valid minimum-based bound and the failure of the maximum substitution in the displayed proof.

Self-review: passed. Independent audit: not yet performed.
