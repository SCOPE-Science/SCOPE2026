# Independent scientific audit — SCOPE-20260920-107c9b8148b4

Audited at: 2026-10-01T19:12:08.377982Z

Disposition: **passed**

## Correctness — PASS

For every real \(\lambda>0\), the Gegenbauer product formula defines the continuous hypergroup used in the cap convolution. The two-variable change of coordinates gives the cap self-convolution profile proportional to \(\int_{r/2}^{\beta}(\tan^2\beta-\tan^2 u)^\lambda\,du\); its Gegenbauer coefficients are squares of cap coefficients and are positive except at finitely many cap radii. Lu's Lemma 3.3 is explicitly stated for arbitrary real \(\lambda>0\) and supplies the required positive-mixture transfer for \(0<\beta<\pi/2\), while its complete-monotonicity part handles the endpoint regime. Full-support positive mixtures therefore give strict positivity of every boundary coefficient, and the beta convolution in the exponent extends it to every \(\delta>\lambda+1\).

### Correctness sources

- assigned RESULT.md
- Beatson-zu Castell-Xu arXiv:1110.2437v1 full HTML
- Lu, Journal of Approximation Theory 306 (2025) 106120 full PDF
- Xu, Proc. AMS 146 (2018)

### Correctness risks

- The proof imports Lu's complete-monotonicity lemmas rather than reproving their analytic derivative calculations from first principles; those lemmas were inspected in the primary full text.

## Originality — PASS

Beatson–zu Castell–Xu explicitly formulate Conjecture 1.4 for arbitrary real \(\lambda>0\), explicitly note that this is more general than their integer-dimensional sphere application, and prove only selected low-dimensional cases. Xu's 2018 theorem assumes integer Jacobi parameters. Lu's 2025 theorem is stated on ordinary spheres, so its spectral Gegenbauer parameter remains tied to integer dimension, even though the positive-mixture lemmas used here hold for real exponents. No inspected source states the literal continuous-real boundary theorem.

### Equivalent formulations

The assigned theorem proves the sufficiency half of the literal all-real conjecture rather than renaming an established discrete-dimensional result.

### Broader coverage

These papers provide discrete cases and analytic tools, not the continuous real Gegenbauer-parameter conclusion.

### Exact database or table

No prior theorem table or database entry supplied the continuous parameter conclusion.

### Claim versus prior implication

The final claim needs a new continuous-hypergroup convolution step and is not mechanically implied by either discrete theorem.

### Sources inspected

- A Pólya criterion for (strict) positive definiteness on the sphere — https://arxiv.org/html/1110.2437v1. OPEN_PROBLEM_SOURCE: It states the all-real if-and-only-if conjecture and proves only selected low-dimensional cases.
- Positive definite functions on the unit sphere and integrals of Jacobi polynomials — https://doi.org/10.1090/proc/13913. NOT_COVERING: Its theorem assumes nonnegative integer Jacobi parameters, so it does not cover arbitrary real Gegenbauer \(\lambda\).
- Strictly positive definite functions on spheres — https://doi.org/10.1016/j.jat.2024.106120. COVERING_INGREDIENT: The mixture lemmas hold for real positive exponents, but the main sphere theorem remains dimension-indexed and does not state the all-real Gegenbauer coefficient theorem.

### Checked sources

- https://arxiv.org/html/1110.2437v1
- https://doi.org/10.1090/proc/13913
- https://doi.org/10.1016/j.jat.2024.106120
- Resultary semantic search

### Residual risks

- A hypergroup-literature formulation equivalent to the all-real coefficient theorem could be poorly indexed, but the main conjecture paper, later Jacobi theorem, and modern positive-mixture paper were directly compared.

## Value — PASS

The result settles the sufficiency boundary for the literal continuous-parameter version of a published conjecture and supplies a reusable hypergroup cap-convolution identity. This is a motivated analytic gap, not an arbitrary interpolation between integer dimensions.

### Value sources

- https://arxiv.org/html/1110.2437v1
- https://doi.org/10.1016/j.jat.2024.106120

### Value risks

- The necessity direction for \(\delta<\lambda+1\) remains open in the record.

## Limitations

- The theorem proves the boundary and \(\delta\ge\lambda+1\) sufficiency direction only; necessity below the boundary is not established.
- The novelty is the continuous real Gegenbauer-parameter extension, not the previously known integer-dimensional sphere cases.
- The proof legitimately imports Lu's positive-mixture lemmas.
