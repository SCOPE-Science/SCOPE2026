# Scientific review: sharp complex-sector law for sketched Hermitian Ritz values

## Correctness — PASS

The claim is a finite-dimensional, exact-arithmetic statement with universal quantifiers over Hermitian positive-definite inputs, full-rank trial bases, and sketches embedding the joint trial/image subspace. For each sketched Ritz eigenpair, positive definiteness of the sketched Gram matrix yields a single quadratic-form quotient. The compression of the sketch Gram error has operator norm at most the specified distortion. Maximizing the rotated numerator over Hermitian contractions gives an exact ellipse, not an upper disk; tangent geometry yields the sharp angular formula. The positive operator inequality for \(A\) then optimizes the ratio of orthogonal to parallel components of \(Au\). Two-mode equality sketches, the exact algebraic example, and a real zero/negative family verify both the angular and threshold sharpness statements. The included verifier checked exact identities and finite random stress tests; those tests do not substitute for the argument.

## Originality — PASS (provisional self-review)

The inspected 2026 motivating manuscript introduces the same sketched Rayleigh--Ritz matrix and arbitrary-embedding framework, but the eigenvalue section gives residual comparisons rather than the exact complex spectral-sector law. The 2021 Nakatsukasa--Tropp manuscript explicitly recognizes nonreal sketched Ritz values for Hermitian inputs and analyzes residual accuracy, without identifying the parameter-dependent sharp angular bound in its inspected eigenvalue sections. Gustafson's 1968 paper gives older operator-angle and noncommuting positive-product accretivity inequalities, which explain part of the underlying technique, but the inspected result states positivity criteria and lower bounds, not the same sharp complex sector for the sketched eigenvalue pencil.

A related sharp positive-real threshold for a **sketched harmonic** Ritz pencil does not imply the angular law for the **ordinary** sketched Rayleigh--Ritz pencil: the former weights the quadratic form with \(AB\) on the left, whereas the present result weights it with \(B\); its conclusion was positivity, not the exact nonzero complex argument. A separate published result on normal spectral-filter Rayleigh-residual distortion bounds residual magnification, not Ritz eigenvalue angles. Semantic database searches over equivalent numerical-range, sector, eigenvalue-location, positive-product, and squared-norm-embedding terminology did not identify matching stronger coverage. This is not a claim of exhaustive uniqueness: the main residual risk is that an older matrix-angle or numerical-range theorem may imply the exact formula after a change of variables. Independent scientific review remains necessary.

## Value — PASS

The same algorithm can return nonreal eigenvalues even when the original matrix is Hermitian. Merely knowing that this is possible, or that real parts stay positive under a restrictive embedding, does not quantify the imaginary drift. The exact sharp sector connects three independently interpretable numerical quantities: spectral condition ratio, squared-norm embedding distortion, and worst-case complex Ritz angle. It supplies a deterministic tolerance rule, an attainable extremal instance, and a precise strict-positive-real boundary. The result applies simultaneously to all Ritz eigenvalues and every trial dimension; a two-mode witness establishes that no universal improvement is possible under the stated assumptions. This is a meaningful spectral-location guarantee, not a routine substitution into an existing stated sRR bound.

## Closest literature and limitations

- Bergermann (2026), arXiv:2604.07158v1, Sections 2.4, 3, 5.3: same sketched Ritz construction and arbitrary sketch embeddings; no corresponding sharp sector statement in inspected material.
- Nakatsukasa and Tropp (2021), arXiv:2111.00113v2, Sections 6.3--6.8: same sRR pencil, subspace-embedding residual controls, explicit warning that Hermitian sRR values need not be real; no sharp distortion-to-argument envelope in inspected material.
- Gustafson (1968), DOI:10.1090/S0002-9904-1968-11974-3, Sections 2, 4, 5: classical operator turning and positive-product accretivity; prior foundational technique rather than an identified identical theorem.
- Published comparison on normal spectral-filter Rayleigh-residual distortion: distinct transformation and a residual-norm conclusion, not this sRR eigenvalue location law.

Scientific limits: exact arithmetic; positive-definite Hermitian inputs; squared-norm embedding on the joint trial/image space; sharpness presently demonstrated with complex sketches; no conclusion for learned/random distribution tails, finite precision, or full Krylov convergence. Reparameterized classical theorems remain a possible originality risk.

Self-review: passed. Independent audit: not yet performed.
