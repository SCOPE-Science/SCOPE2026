# Scientific review

## Correctness — PASS
The exact physical-energy criterion is positive semidefiniteness of \(Q=I-R^{\mathsf T}R\). Explicit multiplication yields the two principal polynomial identities and determinant factorization, verified by `verify.py` in exact rational polynomial arithmetic. Strict monotonicity of \(g_t\), evaluations at both candidate cutoffs, and a two-by-two principal-minor argument prove the full if-and-only-if region. The unique optimizer follows from an implicit derivative. The independent eigenvalue-domain cubic comparison and dominant balance establish the strict stability gap and its asymptotic order. Endpoints, a positive coupling assumption, and spectral-versus-energy definitions were checked. Rational tests are support for, not a replacement for, the analytical proof.

## Originality — PASS, best knowledge
The closest relevant publication (Achleitner–Arnold–Jüngel, arXiv:2308.05689v1) treats strong-stability conditions for general semidissipative matrices using hypocoercivity. Its structural/local criteria do not quantify the *largest finite* Euclidean energy-nonexpansive step for the entire coupling family, identify the unique maximizing ratio, or establish the unbounded separation from scalar eigenvalue stability. The authors' 2023 follow-up and Sun–Wei–Wu's general linear seminegative energy analysis were compared in material available in full text. Known fixed-coefficient \(t=1\) oscillator thresholds are explicitly excluded from the new contribution; Strang splitting and convex-gradient contractivity concerns distinct hypotheses/maps. Exact equivalence in unindexed literature remains a risk. No independent bibliographic audit has occurred.

## Value — PASS
Physical Euclidean energy is a natural invariant inequality for semidissipative oscillators. The complete sharp phase diagram, unique optimal oscillator coupling, and proof that the spectral stability test can be arbitrarily less restrictive form a parameter-design and method-selection benchmark, beyond a textbook scalar stability interval or a preexisting fixed-parameter calculation. The result is restricted to two dimensions, constant-step explicit second order, and unweighted energy.

## References and limits
- Achleitner, Arnold, Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1.
- Achleitner, Arnold, Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge–Kutta Methods*, arXiv:2310.19758v1.
- Sun, Wei, Wu, *On Energy Laws and Stability of Runge–Kutta Methods for Linear Seminegative Problems*, arXiv:2201.06501.
- Sun, Shu, *Enforcing strong stability of explicit Runge–Kutta methods with superviscosity*, arXiv:1912.11596.

Self-review: passed. Independent audit: not yet performed.
