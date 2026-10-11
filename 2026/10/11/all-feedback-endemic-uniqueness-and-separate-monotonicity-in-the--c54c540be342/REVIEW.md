# Same-model scientific review

## Correctness — PASS

The theorem concerns the positive-rate, constant-contact prevalence-driven SIRCm equations on the unit simplex. The infected equilibrium condition gives \(S+\sigma C=(\mu+\alpha)/\beta\), excluding endemic equilibria at or below threshold. The recovered/cross-immune stationary subsystem has a positive determinant and yields explicit rational formulas for both coordinates. The mass balance reduces exactly to \(H(I)=1-(\mu+\alpha)/\beta\). Equations (2) and (3) in RESULT.md give \(H'(I)>1\) for the full rectangular parameter domain, guaranteeing exactly one positive root. Reconstructing all compartments proves positivity and the remaining differential equations. The two explicit quotient-rule identities (4) prove independent-parameter monotonicity and the \(\sigma=1\) exception. Analytic simplicity gives analytic parameter dependence. The embedded symbolic checker confirms these identities and tests 80 rational parameter tuples; numerical checks are not used as a universal proof.

## Originality — PASS, subject to residual priority risk

The nearest same-model source [1] establishes existence for arbitrary feedback, uniqueness in weak and strong regimes, and a diagonal sufficient condition in Remark 4.4. Its statements do not entail the all-strength uniqueness assertion for arbitrary independent feedback values. The present proof establishes a globally strictly increasing scalar elimination function and two parameter-sensitivity factorizations that are not given there. The zero-feedback SIRC results [2] and fixed-transition-rate network SIRS results [3] do not cover the same two-channel prevalence-responsive dynamics. Searches for alternate terminology and stronger coverage did not reveal an equivalent statement, but priority cannot be proved by search; earlier implicit derivations remain a risk. The publication record of [2] was accessible only via bibliography and abstract rather than full manuscript, which limits that particular comparison.

## Mathematical value — PASS

The source leaves intermediate-strength and off-diagonal feedback uniqueness unclassified. Eliminating possible endemic multiplicity **for every** admissible feedback pair is a substantial extension on a naturally defined model, rather than an arbitrary parameter slice. Separate positive response of endemic prevalence to the two immune-escape channels and exact degeneracy at \(\sigma=1\) give an interpretable equilibrium sensitivity law. The result does not inflate uniqueness to claims about stability or forecast ability.

## Closest literature and limitations

[1] Ramírez-Gutiérrez et al., arXiv:2610.01111v1, Sections 2–4 and Appendix 8 (full text read); [2] Casagrandi et al., Mathematical Biosciences 200 (2006), original zero-feedback SIRC model (abstract/bibliography available); [3] Gatti–Como, arXiv:2604.21065, network SIRS with fixed transition rates (full-text equations and results inspected). Remaining risk: possible equivalent reductions in earlier immune-escape or SIRC equilibrium literature. Independent review, clinical validation, and stability analysis have not been performed.

Same-model review: passed. Independent audit: not yet performed.
