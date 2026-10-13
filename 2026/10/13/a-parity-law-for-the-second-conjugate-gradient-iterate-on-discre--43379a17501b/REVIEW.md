# Scientific assessment

## Correctness — PASS
The exact proof uses only standard Galerkin characterization of two-step CG, strict positive definiteness of its moment Gram matrix, independently reconstructed four-moment identities for two natural difference profiles, and convexity of an explicit quartic. Strict signs, the unique root, the asymptotic root expansion, and the integer eight-node counterexample follow algebraically. The full-rational checker reconstructs both actual iterates from the packaged code. Finite computations are supplementary and do not establish the infinite-family claims on their own.

## Originality — PASS, subject to historical uncertainty
The closest fully inspected source is Beckermann and Kuijlaars (2002): it uses the *same* finite-difference Poisson matrix and special forcing to study superlinear **energy-norm convergence**, not first-coordinate signs after exactly two iterations. Shewchuk (1994) derives the general conjugate-gradient algorithm and Krylov geometry, not the discrete-hat parity law. Relevant published search results describe inverse-positive Poisson coordinate sampling, nonstandard CG-type methods, and Krylov error behavior but do not imply the specific discrete-hat, sharp amplitude-root theorem. A recent manuscript on non-negative CG was accessible only by abstract, leaving residual risk of unrecognized equivalent treatment; neither failed search nor restricted topic establishes uniqueness of discovery. Earlier results about positivity loss for generic inverse-positive matrices already establish *existence of failures*, but not the new structured Poisson, parity, and exact frontier statement.

## Value — PASS
A one-dimensional discretization of the Poisson boundary-value problem is a canonical inverse-positive system. Discrete triangular and plateau loading profiles model localized nonnegative piecewise-linear forcing. The theorem identifies a genuine discrete-maximum-principle failure in an intermediate Krylov iterate, gives an exact universal-in-grid sharp recovery threshold for each load width, and explains a non-obvious one-site-versus-two-site peak distinction. The explicit integer counterexample and width-dependent asymptotic rule give specific interpretive and reproducible value beyond merely observing that CG does not always preserve positivity.

## Scientific limits and residual risk
The exact threshold applies only to the **first component of the second iterate** and this structured load family; for the single-peak load only the small-source comparison is established. An inaccessible relevant 2026 manuscript may contain a stronger or equivalent example. No claim is made about uniqueness among all prior publications, arbitrary load profiles, floating-point arithmetic, or independent verification.

Self-review: passed. Independent audit: not yet performed.
