# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness — PASS

For both source models, the claimed non-identifiability follows by solving the two observed-state equations algebraically for the two free time-dependent rates after fixing arbitrary positive values of the three constant interaction coefficients. Direct substitution is an identity, so the result does not depend on a perturbation argument, generic numerical fit, or approximate degeneracy.

The regularity assumptions are explicit. With \(x,y\in C^1\), \(x,y>0\), and \(x^4\ne1\), the reconstructed rates are continuous. If the observed trajectory and inputs have greater regularity, the rates inherit the corresponding regularity away from the stated denominators.

Sign constraints were checked adversarially. On compact positive trajectories, the predator gain factor multiplying \(C\) has a positive minimum, so sufficiently large positive \(C\) guarantees \(\delta>0\). When \(x<1\), sufficiently large \(A\) also guarantees \(\alpha>0\) if that extra requirement is imposed. Thus positivity does not generically eliminate the ambiguity. The source itself models the rates as time-varying outputs rather than as a fixed known forcing law.

A compact deterministic calculation reconstructs two positive rate pairs for two distinct constant triples in each response model. The largest sampled ODE residual is about \(1.39\times10^{-16}\), consistent with roundoff. This is only a sanity check; the proof is algebraic.

The principal scope distinction is preserved: the theorem concerns structural identifiability of the non-autonomous ODE model with free time-dependent rates. A particular finite neural-network parametrization may restrict the admissible function class enough to alter identifiability. No claim is made about that separate architecture-restricted model without a corresponding analysis.

## Originality — PASS, to the best of our knowledge

The novelty claim is deliberately source-specific. General unknown-input observability, structural identifiability with time-varying parameters, continuous-symmetry ambiguities, and the warning that replacing a time-varying quantity by a constant can change identifiability are established subjects and are excluded from novelty.

Martinelli's arXiv:2211.13507 explicitly treats time-varying parameters as unknown inputs and provides a general analytical identifiability framework. His 2024 Journal of Theoretical Biology paper similarly analyzes variants of an HIV model with constant or time-varying parameters and characterizes indistinguishable families using continuous symmetries. Conrad and Eisenberg, arXiv:2407.02771, explicitly discuss the identifiability consequences of replacing time-varying quantities by constants.

The claimed contribution is narrower: for the two specific non-autonomous Moose–Wolf models in arXiv:2609.20793v1, the state equations themselves expose a closed-form three-constant gauge, which directly invalidates the source's inference from its frozen autonomous identifiability calculation to the time-varying inverse problem.

Searches covered the exact paper title and arXiv identifier, correction/comment combinations, structural identifiability and non-identifiability, time-varying rates as unknown inputs, Holling type-II and ratio-dependent predator–prey formulations, and equivalent symmetry/gauge language. No source-specific correction or prior note containing the displayed gauge was located.

The main residual risk is recency: arXiv:2609.20793 was submitted on 17 September 2026, so an author revision or discussion may not yet be broadly indexed.

## Value — PASS

Structural identifiability is used by the source as a prerequisite for interpreting simultaneous recovery of constant ecological parameters and time-varying rates. The exact gauge shows that, at the ODE-model level, even ideal full-state observations leave those quantities nonunique. This is stronger than practical ill-conditioning under sparse or noisy data.

The result is useful because it also identifies the missing information needed to make the inverse problem well posed: independently observed forcing, a finite-dimensional rate law, extra outputs tied to the rates, or another constraint that breaks the parameter–function gauge.

## Limitations

The result does not invalidate population-trajectory reconstruction or forecasting, does not analyze finite-sample statistical uncertainty, and does not prove that every compensating rate lies in the image of the particular neural-network architecture used by the source. It applies on positive intervals away from \(x=1\); carrying-capacity contact requires separate compatibility conditions. It also does not dispute identifiability of the autonomous constant-rate surrogate considered in the source.

The cited general time-varying-identifiability literature establishes broader methodology and is not part of the originality claim.
