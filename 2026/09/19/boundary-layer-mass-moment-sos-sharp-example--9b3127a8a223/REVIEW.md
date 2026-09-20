# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The exact weight normalization follows from logarithmic differentiation of the source polynomial at x=1 and standard endpoint derivatives of Chebyshev polynomials. The exterior and fixed-index interior scaling limits follow by substituting x=cosh(a/r) and x=cos(z/r) into the exact root equation and taking locally uniform limits. The limiting mass identity follows from the genus-zero product of F(z)=cos(z)+z sin(z), equivalently from the spectrum of the associated one-dimensional Robin Sturm-Liouville problem, and agrees with independent high-precision finite-r computations. The verification artifact checks normalization, the exact relaxation objective, endpoint locations, weights, and spectral sums.

Adversarial checks included sign/index consistency for the exterior versus interior atoms, the sign of the source objective, the normalization constant, and the possibility that untracked interior atoms retain positive limiting mass. The product identity gives total limiting mass exactly one, closing the latter gap.

## Originality

**PASS, to the best of our knowledge.** The motivating paper arXiv:2609.20544v1 was inspected for its sharp degree-four example, root distribution, atomic functional, and exact error. The related Stengle analysis arXiv:2512.19141 was inspected for its finitely atomic construction and special-polynomial root structure. arXiv:2509.01382 was checked for the established pseudo-moment terminology and general certificate context. Searches were also made using the exact defining Chebyshev combination, the limiting equations cos(z)+z sin(z)=0 and a tanh(a)=1, and boundary-layer/exterior-mass formulations.

No source was located stating the claimed source-specific asymptotic law: persistent exterior mass 2/a^4, the complete r^2-rescaled atomic limit, or the trace-identity explanation of the sharp relaxation constant. The novelty claim excludes the source example itself, standard Chebyshev root analysis, classical Sturm-Liouville product formulas, pseudo-moment certificates, and general truncated-moment theory.

No single inaccessible paper was identified as concrete evidence of prior coverage. The main residual originality risk is diffuse: classical orthogonal-polynomial, quadrature, and Robin spectral asymptotics may contain equivalent zero/weight limits in different notation. That risk is why the claim is restricted to the moment-SOS interpretation and the combined boundary-layer law, rather than claiming the underlying special-function asymptotics as new.

## Value

**PASS.** The result gives a geometric mechanism for a newly proved sharp O(r^-2) moment-SOS lower-bound example. It shows that weak convergence of the explicit certificate to the true boundary minimizer can coexist with approximately 96.554% infeasible mass, because the infeasibility distance shrinks at the same r^-2 scale as the relaxation gap. The full limit quantifies both the exterior leakage and compensating interior tail and may be useful when interpreting moment relaxations, extraction heuristics, or certificate diagnostics near degenerate constraints.

## Limitations

The theorem concerns the explicit positive atomic certificate constructed for one univariate sharp example. It does not prove uniqueness of the SDP optimizer or persistence of exterior mass for general moment-SOS problems. It is an exact-arithmetic asymptotic statement, not a floating-point stability result. Parts of the special-function analysis may be recoverable from older orthogonal-polynomial theory even if the combined optimization interpretation was not located.
