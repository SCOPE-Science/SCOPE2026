# Review: A one-parameter counterexample to reversible two-lag variance bounds

## Correctness

**PASS.** The chain is stationary under the uniform law, irreducible and aperiodic for every \(0<\alpha<1\), and nonreversible. Its nonconstant Fourier eigenvalue gives \(\rho_k=\operatorname{Re}(\lambda^k)\); summing the convergent geometric series gives \(\tau=(1-\alpha)/\alpha\). Direct algebra yields the exact positive gap \((4-6\alpha+3\alpha^2)/(6\alpha(2-\alpha))\). The denominator is positive on the stated interval and the numerator has negative discriminant and positive leading coefficient.

## Originality

**PASS, with a bounded residual risk.** The closest literature is Berg–Song’s reversible autocovariance moment representation and Choi’s analysis of nonreversible chains and cycle walks. The inspected texts do not state the exact parameter-uniform comparison for this lazy one-way three-cycle. General spectral techniques may make the calculation accessible, so the originality claim is limited to this explicit family and exact gap, not to a new general theory.

## Value

**PASS.** Reversible moment constraints are used in autocovariance-shape methods for Markov-chain variance estimation. This exact family gives a uniform, quantified obstruction to extending one such two-lag lower bound beyond reversibility, rather than only a numerical example or a single parameter counterexample.

## Closest literature and limitations

- Berg and Song, arXiv:2207.12705v1 (2022-07-26), equation (7): the autocovariance moment representation is explicitly for reversible chains.
- Choi, arXiv:1706.00068v1 (2017-05-31), sections on asymmetric cycle walks and variance bounds: relevant nonreversible spectral context, but the inspected statements do not give this exact two-lag gap.
- Scope is limited to the three-state lazy clockwise family and the cosine observable. No optimal bound for general nonreversible chains is claimed.

Self-review: passed. Independent audit: not yet performed.
