# Self-review

## Correctness — PASS

The domain is every positive initial state for all source-admissible positive rates and \(0<c\le1\), \(0\le\delta<1\). Positivity and logistic comparisons establish global existence and boundedness unconditionally. At and below invasion equality, two scalar comparisons prove convergence to the prey-only equilibrium. Above equality, strict monotonicity of the predator-nullcline restriction gives exactly one stable coexistence equilibrium; the strictly negative Dulac divergence rules out interior cycles; the two boundary saddles and the acyclic boundary connection eliminate competing planar limit graphs. At equality, the exact prey-deficit quotient equation is a forced, asymptotically damped linear equation whose limit determines both \(1/t\) constants. The attached symbolic checker returned `VERIFY_OK`. Risk: the planar limit-set step uses standard Poincaré--Bendixson and invariant-manifold results, rather than a formalized proof.

## Originality — PASS

The motivating paper [1] contains local equilibrium calculations and finite-horizon numerical convergence, but explicitly leaves rigorous global stability open and has no critical extinction-amplitude formula. Hsu--Huang [2] develop general global-stability techniques for a distinct Holling--Tanner predator law; Umrao et al. [3] and Chatterjee [4] use different nonlinear functional responses and report different regimes, including cycles. The new result is not priority for Dulac theory or generic transcritical reciprocal-time decay; it is the exact two-sided, globally valid, fear-sensitive critical amplitude in the source's coupled-denominator model, together with the all-parameter convergence classification. Indexed published-finding and predecessor-claim searches found no covering statement. Residual risk: a differently indexed earlier paper could provide an equivalent general theorem, and literature searches cannot prove uniqueness.

## Value — PASS

The exact transition from predator persistence to extinction is the ecological model's natural control boundary; the paper identifies global stability as missing. The result answers whether convergence holds without the source's restricted quadratic parameter condition. More importantly, the invasion threshold being fear-independent conceals two *strictly fear-dependent* late-time observables of opposite direction: smaller predator tail and larger prey deficit. Both constants are explicit, valid for all positive initial states, and useful for interpreting slow transients near criticality. This is a substantive endpoint refinement rather than an arbitrary parameter slice.

## Scope, source comparison and limitations

Only the exact integer-order deterministic equation is addressed; empirical predictions and off-critical transient speed are unproved. Reference [1] supplies the actual printed model and local threshold, [2] covers older global techniques for a different predator law, [3] and [4] demonstrate that fear can yield qualitatively different dynamics in other equations. The independent audit channel remains unperformed.

Self-review: passed. Independent audit: not yet performed.
