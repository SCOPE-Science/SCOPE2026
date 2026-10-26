# Scientific review: sharp sixth-moment endpoints for quadratic harmonics on the three-sphere

## Correctness — PASS
The normalized degree-two harmonic is a traceless real-symmetric quadratic on four variables, or a complex combination of two. Gaussian cumulants, the fourth-order Newton identity and radial moment 322560 yield the exact normalized sixth-moment formula. Cauchy--Schwarz gives the lower endpoint with balanced eigenvalue equality; the paired-four-eigenvalue parametrization gives both sharp upper spectral inequalities and their joint equality at zonal eigenvalues. Uniform angular averaging of real parts proves the complex upper constant, its precise phase-rank deficit, and constant-phase necessity. `check.py` independently applies the spherical monomial integration formula to 9 real examples, 20 off-diagonal complex examples, and 3 symbolic identities: 32 successful checks, supplementary to the universal proof.

## Originality — PASS, best-knowledge qualification
Dai--Gorbachev--Tikhonov, *Nikolskii inequality for lacunary spherical polynomials*, arXiv:1905.00323v1, was inspected in complete six-page text and establishes growth-order Nikolskii bounds, not the exact sixth-moment interval at fixed spherical degree two. The closest published result, *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics* (2026, published-finding corpus record d4106097159f), was inspected in full: its fourth-moment theorem supplies a previously known sharp trace-fourth-power bound, but it does not state or logically give the exact sixth-moment identity, the sharp real lower sixth moment, or the complex sixth-moment phase-rank inequality. Dai--Feng--Tikhonov gives broad reverse-Hölder estimates rather than these exact fixed-degree endpoints; De Carli--Gorbachev--Tikhonov concerns a broader norm-ratio question with different exact target. Multiple published-finding corpus alias searches returned no direct covering record. Absence from search is not proof of novelty. Invariant-theoretic equivalents and uninspected older full texts remain priority risks.

## Mathematical value — PASS
A natural, dimension-specific sharp reverse-Hölder problem is solved completely: exact sixth-moment range for *all* nonzero real degree-two spherical harmonics on S^3, both spectral equality classes, sharp complex upper constant and its complete equality class, plus explicit deficits. The distinction between balanced and zonal eigenvalue geometry is structural rather than a numerical sample or arbitrary coefficient slice. The exact lower endpoint and complex phase-rank estimate are not implied by the known sharp fourth-moment constant alone.

## Limits
No complex lower endpoint, higher-degree generalization, or independent validation is claimed. The coefficient in the complex phase-rank deficit is not claimed sharp away from global maximizers. Older equivalent formulations remain possible.

Self-review: passed. Independent audit: not yet performed.
