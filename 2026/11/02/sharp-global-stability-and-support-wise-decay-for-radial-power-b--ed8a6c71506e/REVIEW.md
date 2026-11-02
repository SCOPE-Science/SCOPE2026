# Self-review

## Correctness — PASS

The radial dual map \(x\mapsto (1+\|x\|^{p-2})x\) is invertible for \(p>2\). In the stated step interval, every active component of the next dual vector has absolute multiplier strictly below the radial factor. This yields strict Euclidean-radius contraction, including at the endpoint \(\eta=2/a_{\max}\); compactness and continuity turn strict contraction into convergence. The scalar axis map gives the exact inequality, two-cycle boundary, and monotone magnitude divergence. The nonseparable update becomes coordinatewise in dual variables with a common coefficient tending to \(\eta\), so inverse-power differences prove the exact support-wise asymptotic. The proof treats finite coordinate extinctions separately. The companion verifier passed all described finite checks. No experiment is used as an infinite proof.

## Originality — PASS, qualified

The primitive update is not original. Ding–Li–Toh's arXiv:2306.14522 explicitly uses the radial polynomial kernel and analyzes stochastic robustness, but its inspected Introduction, Sections 3–5 and associated derivations do not provide this weighted homogeneous fixed-step global frontier, the exact unstable axis basin, or the asymptotic coefficient by surviving coordinate. Bolte–Sabach–Teboulle–Vaisbourd (arXiv:1706.06461) and Lu–Freund–Nesterov (arXiv:1610.05708) provide relative-smoothness convergence guarantees at sufficient stepsizes, which do not imply this exact sharp threshold and explicit divergence beyond it. Dragomir–d'Aspremont–Bolte (arXiv:1901.10791) permits more aggressive selected steps via dynamic descent checks, but does not classify this unconditional fixed-step family. The published mathematical-finding index was searched for the objects, aliases, rates, and threshold; two closest hits concern different algorithms or kernels, and no equivalent or dominating claim was found in their visible summaries. This is not a proof of universal novelty, and a specialized equivalent dynamical-systems derivation remains a residual risk.

## Value — PASS

A natural non-Lipschitz test class, used to motivate polynomial Bregman kernels, admits an exact fixed-step global-stability ceiling independent of exponent and dimension. It also shows a sharply contrasting unstable regime with a computable separatrix and an initialization-independent leading decay constant for each surviving coordinate. Both the step-size diagnostic and the support-wise rate are mathematically motivated benchmarks for nonlinear mirror-gradient dynamics, going beyond restating a standard sufficient descent condition.

## Scope and integrity

All formulas apply to the deterministic exact-gradient model; they do not imply a stochastic or neural-network convergence theorem, a dimension-free wall-clock guarantee, or a classification of the nonaxial unstable basin. Publication priority is not independently validated. Source text is cited for prior methods rather than copied.

Self-review: passed. Independent audit: not yet performed.
