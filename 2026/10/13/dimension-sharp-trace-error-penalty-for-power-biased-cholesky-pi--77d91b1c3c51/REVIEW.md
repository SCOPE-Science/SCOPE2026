# Self-review

## Correctness — PASS

The theorem's exact domain is finite real positive-semidefinite matrices of dimension \(n\ge2\), rank at least two, strictly positive diagonals, and any real power \(q>1\). A Gram-factor Schur projection shows that all conditional one-pivot residuals are positive semidefinite with positive trace. Hölder's inequality proves the stated \(n^{1-1/q}\) bound on the ratio of *expected residual traces*, not the ratio of independent realization errors. Direct two-outcome calculations for \(\operatorname{diag}(t,J_m)\) prove the sign boundary and the positive asymptotic power constant. Elementary differentiation gives the exact \(q=2\) maximum in the specified orthogonal equal-entry two-block class, with the claimed scaling and equality cases. Continuity under a small diagonal perturbation gives positive-definite instances. The embedded standard-library verifier passed 2137 exact-rational checks of concrete residual matrices, weights, and examples. These finite checks do not prove the general statements; the algebraic and analytic arguments do.

## Originality — PASS, with residual priority risk

Chen, Epperly, Tropp and Webber, arXiv:2207.06503, already defined Gibbs/power sampling in Section 2.3.4 and developed \(q=1\) trace-error results (Section 5); their Appendix C supplies greedy (infinite-power) bad cases. The new method of sampling is **not** claimed original. Steinerberger, arXiv:2404.11487, already proved the \(q=2\) Frobenius guarantee and numerically reported a small trace-error reversal for the squared rule (Table 1). The fact of a qualitative trace reversal is **not** claimed original. The present result instead establishes the exact *first-pivot expected trace-error ratio*, sharp \(n^{1-1/q}\) exponent for *every fixed finite* \(q>1\), precise two-block sign frontier and restricted-class squared-rule optimum, which are not implied by either source's norms, greedy limits, or tabulated multi-step observations.

Other published mathematical comparisons concern worst-case multistage adaptive random pivoting (record 77e11f8220ee), weighted ACA deflation (record f46330fd3a80), and complete-pivot ACA Frobenius growth (record 71dd3abf0659). Their mathematical statements involve different operations or error criteria. A related power-pivot result on the same rank-two example concerns *squared Frobenius contraction*, not the expected-trace competitive ratio. Another result analyzes worst-target quadratic-form risk rather than trace error. These distinctions do not preclude an equivalent result under other terminology; originality is not independently certified.

## Value — PASS

The published sampling rules optimize different error criteria. A polynomial worst-case ratio for all finite \(q>1\) quantifies the possible cost of using a Frobenius-motivated rule when the required numerical objective is nuclear-norm error. The exponent is globally sharp and the squared-rule constant is exactly optimized within a motivated rank-two two-block class, making the result useful for selecting and stress-testing numerical matrix compression rules rather than simply recomputing a known table.

## Scope, literature and residual risks

The statement is confined to one pivot and expected trace-norm error, not later adaptive iterations, convergence rates or Frobenius error. The universal constant is not proved optimal; the restricted two-block extremum is not a claim over all PSD matrices. The source full texts inspected are Chen et al., arXiv:2207.06503, Sections 2.2, 2.3.4, 5 and Appendix C (https://onlinelibrary.wiley.com/doi/10.1002/cpa.22234), and Steinerberger, arXiv:2404.11487, Sections 1–3 and Table 1 (https://arxiv.org/html/2404.11487v1). No search establishes absolute priority or independence.

Self-review: passed. Independent audit: not yet performed.
