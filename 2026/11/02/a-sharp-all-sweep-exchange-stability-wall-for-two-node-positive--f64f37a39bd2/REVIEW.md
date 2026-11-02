# Scientific review

## Correctness

PASS. The exact two-node exponential predictor and correction rules are taken from the SPIDeC construction, with the trapezoidal endpoint weights. Differentiation at each positive fixed equilibrium gives a commuting polynomial recurrence in the two-rate exchange generator. The nonzero eigenmode yields an explicit formula whose parity determines the exact stability boundary, including equality. The collocation branch follows from an invertible implicit-function Jacobian; its derivative is computed independently. The packaged verifier evaluates the original nonlinear map as well as exact rational identities. The theorem makes no extrapolation from finite tests to the infinite parameter family.

## Originality

PASS under inspected-source and prior-record comparisons, with residual priority risk. Pezzella's source supplies the method, unconditional positivity, diagonal scalar exactness, and small-step nonlinear estimates; its relevant equations and stability sections do not present the fixed two-species exchange multiplier or the fact that every finite sweep count shares one exact stability threshold. Scheiber's earlier additive Picard-collocation theory supplies small-step convergence principles, not this multiplicative method's two-rate all-sweep classification. A classical Picard/eigenvalue derivation can be specialized to yield these identities, and an undiscovered earlier specialization may exist. The result is not claimed to be an independent new general theory of collocation.

## Mathematical value

PASS. The exchange generator is a minimal natural coupled positive system in which diagonal scalar test stability does not characterize the finite-sweep method. The exact barrier differentiates unconditional positivity, transverse contraction, and the implicit collocation limit. The absence of stability improvement from any finite number of corrections is mathematically useful when deciding whether further sweeps can handle a stiffness regime; asymmetric exchange rates, equality, and parity are all classified without numerical fitting. This concerns the linearization only, not global stability or conservation of the discrete mass.

## References and limits

Pezzella, arXiv:2606.29523, Sections 2, 3, 5; Scheiber (2019), Sections 2–3. The checker supports but does not replace the complete proof. The result assumes two Gauss–Lobatto nodes, positive two-species exchange rates, and finite sweep count. Historical priority remains independently unconfirmed.

Self-review: passed. Independent audit: not yet performed.
