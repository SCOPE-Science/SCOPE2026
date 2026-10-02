# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** After translating and scaling so the fixed point is zero and the current error is one, let \(a=g(1)\), \(c=g(a)\), and \(t=(c-a)/(a-1)\). The contraction constraints give \(|a|\le q\), \(|c|\le q|a|\), \(|t|\le q\), while the accelerated error is \((a-t)/(1-t)\). Optimizing the feasible positive and negative endpoint branches yields \(W(q)=2q^2/((1-q)(1+2q))\); the stated continuous piecewise-affine contraction attains equality. Imposing monotonicity yields \(W_\uparrow(q)=q^2/(1-q^2)\) with its own sharp witness. Independent endpoint-grid optimization at several values of \(q\) approached both formulas from below, while exact substitution verifies the witnesses and thresholds.
- Originality: **PASS.** The complete Johnson--Scholz paper studies convergence of generalized Steffensen iteration under divided-difference regularity and local/semilocal parameters; its contractive theorem still includes a divided-difference Lipschitz constant and an initial residual condition. It does not state the bare-global-contraction one-cycle minimax factor or thresholds. Other classical sources checked concern convergence speed, monotone enclosure, convexity, or posterior bounds. No exact factor matching the audited theorem was located.
- Scientific value: **PASS.** The theorem gives an exact robustness frontier for a classical accelerator under the minimal black-box contraction assumption, identifies sharp stability thresholds, quantifies the gap against two ordinary Picard evaluations at equal function-call cost, and separately solves the monotone subclass. These are natural and practically interpretable boundaries rather than a small-instance calculation.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model scientific evidence
remains separately identified in `AUDIT.json` and is not relabeled as this
independent assessment.
