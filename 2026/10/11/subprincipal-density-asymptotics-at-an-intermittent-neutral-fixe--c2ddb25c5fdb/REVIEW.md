# Scientific review

## Correctness: PASS
The claim has fixed parameter \(0<\gamma<1\), a normalized invariant probability density and explicit right-hand values at \(1/2\). The density identity follows from the exact neutral inverse-branch renewal formula in [1], Section 6. The Abel coordinate has a controlled differentiable expansion through the first \(x^\gamma\) coefficient ([1], Theorem 2.1); Euler--Maclaurin is applied to a function whose first four derivatives have proved inverse-power bounds. The Bernoulli term gives \((\gamma+1)2^\gamma q_0 x^\gamma/12\), and the Abel correction cancels it to the displayed coefficient. The remainder follows for every fixed parameter. Symbolic substitution verifies all coefficients; finite computations are not used as an infinite proof.

## Originality: PASS, with residual risk
The focal 2026 paper [1] provides the inverse-branch series and bounded error after its singular density approximation, and gives the \(x^{1-\gamma}\) term already. It neither states nor deduces as a concluded limit the finite constant \((\gamma+2)H/4\), the neutral \(x^\gamma\) coefficient, or their parameter crossover. The 2025 work [2] establishes statistical stability and linear response, not these local coefficients. The leading-order asymptotics discussed in [3] and the infinite-measure operator-iterate problem [4] do not imply the stated finite-regime expansion. The published computation framework makes this a closely related refinement: a differently formulated old expansion remains a genuine literature risk.

## Mathematical value: PASS
The unresolved bounded term in a canonical neutral-density estimate is replaced by an exact intercept and an explicit signed next correction. The competition between exponents \(\gamma\) and \(1-\gamma\) is a natural parameter boundary affecting the local regularity and precision of density approximation. The coefficient is universally nonzero for \(0<\gamma<1/2\), so it is not just a normalization restatement. No downstream mixing or memory-loss theorem is asserted.

## Scope and limits
Fixed finite-measure LSV parameters only; no general perturbed neutral maps, no uniform parameter control, and no claimed strict nonvanishing of the right-branch derivative for \(\gamma>1/2\). Closest source: [1], Section 6, especially equation (6.3) and Lemma 6.5.

Same-model review: passed. Independent audit: not yet performed.
