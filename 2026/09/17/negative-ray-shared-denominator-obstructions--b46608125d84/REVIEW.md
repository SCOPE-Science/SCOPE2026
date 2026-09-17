# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The source theorem was checked in the published 2025 article. It explicitly states geometric common-denominator approximation on \(( -\infty,0]\) for every finite family in \(\mathcal A(\mathbb C\setminus(-\infty,0])\), and the conclusion describes this as a “no assumptions” theorem.

The counterexamples were checked against the stated function class and against complex-coefficient rational approximants.

- \(e^{iz}\) is entire and bounded on the negative ray. Any rational function at finite uniform distance from it is bounded there and therefore has a finite limit at \(-\infty\). The two subsequences with target values \(1\) and \(-1\) force uniform error at least \(1\), attained by the zero rational function.
- \(g(z)=e^z\sin(e^{-z})\) is entire, bounded on the negative ray, and tends to \(0\) at \(-\infty\). At the alternating points \(x_k=-\log((k+\tfrac12)\pi)\), its magnitudes are exactly \(1/((k+\tfrac12)\pi)\).
- For a complex type-\((n,n)\) rational function, its real part on the real axis has numerator degree at most \(2n\) after writing it over the positive denominator \(2q q^\#\). The \(2n+2\) forced alternating signs would require \(2n+1\) real zeros, proving the stated lower bound.
- A genuine pole on the approximation ray gives infinite error; canceled poles are removed before the degree argument.
- The qualitative closure statement follows from the finite limit of every bounded rational function at infinity and from Weierstrass approximation after the compactifying substitution \(y=-x/(1-x)\). The transformed polynomials have the common denominator \((1-x)^n\).
- The conformal objection is topological: the slit plane is simply connected, while the plane exterior of the closed unit disk is not. Under the spherical interpretation, infinity is interior to the exterior disk but is a boundary point of the slit plane.

The stronger algebraic lower-bound example rules out the possibility that merely adding boundedness or a limit at \(-\infty\) would recover the claimed geometric conclusion.

## Originality

**PASS, to the best of our knowledge.**

The 2025 source article, its accessible version information, title/DOI searches, and searches for a correction or erratum were checked. No published correction addressing Theorem 1 was located. Current SCOPE records were also searched by the source title, author, shared-denominator terminology, and the negative-ray approximation claim, with no overlap located.

The compactification/Weierstrass closure argument is elementary approximation theory and is not claimed as novel in isolation. The originality claim concerns its use to diagnose the recent theorem, the exact \(E_n(e^{i\cdot})=1\) obstruction, the entire finite-limit example with the explicit \(\Omega(1/n)\) lower bound, and the identification of the incompatible exterior-domain conformal step.

No inaccessible paper was identified as especially likely to contain this specific correction. Residual originality risk remains from uncatalogued discussions, unpublished notes, or a correction not indexed by the searches consulted.

## Value

**PASS.**

The result corrects a broad theorem in a recent paper that is used to supply the theoretical justification for uniform geometric shared-pole approximation. It separates three logically distinct facts:

1. qualitative uniform approximability on the unbounded ray;
2. geometric convergence for a general analytic target;
3. the empirically successful shared-pole approximation of the specific \(\phi\)-functions.

The first has an exact elementary characterization, the second is false under the published hypotheses even for entire targets, and the third is not refuted. This distinction prevents an invalid general theorem from being used as support for the specific numerical method while preserving the parts of the paper not touched by the counterexamples.

## Literature boundary

The source article was available in full through its open-access publication. Schmelzer's 2026 result establishes the scalar Halphen-rate theorem for each \(\varphi_\ell\), but it does not convert the false general theorem into a common-denominator optimal-rate theorem. No claim is made here about the optimal asymptotic rate for simultaneous \(\varphi\)-function approximation with one shared denominator.

## Review status

This is a same-model scientific review, not independent validation, formal verification, journal peer review, or a guarantee of first discovery.
