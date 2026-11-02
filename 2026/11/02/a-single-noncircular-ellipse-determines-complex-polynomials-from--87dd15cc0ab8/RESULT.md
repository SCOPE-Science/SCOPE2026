# A single noncircular ellipse determines complex polynomials from their magnitudes

## Finding
Let \(E\) be any nondegenerate Euclidean ellipse in \(\mathbb C\). The following properties are equivalent:

1. The major and minor semiaxes of \(E\) are different.
2. For every two complex polynomials \(P,Q\), equality \(|P(z)|=|Q(z)|\) for every \(z\in E\) implies \(Q=\lambda P\) identically, for some \(\lambda\in\mathbb C\) with \(|\lambda|=1\).
3. For every integer \(n\ge0\), any \(4n+1\) pairwise distinct points of \(E\) form a phaseless uniqueness set for complex polynomials of degree at most \(n\): equality of the two lists of magnitudes forces the same conclusion.

The proof gives the stronger rational-modulus rigidity: on a noncircular ellipse there is no nonconstant rational function whose modulus is identically one at all its defined boundary points. This concerns rational functions on the entire complex plane, not arbitrary holomorphic functions defined only near \(E\).

## Assumptions and scope
An ellipse is nondegenerate when its two semiaxes are strictly positive. After a complex translation and rotation, write its boundary as
\[
E=\{a\cos t+i b\sin t:0\le t<2\pi\},\qquad a\ge b>0.
\]
In the noncircular case \(a>b\), set \(c=(a+b)/2\), \(d=(a-b)/2\), and \(r=d/c\). Thus \(0<r<1\), and the rational Joukowski parametrization is
\[
z(w)=cw+d/w,\qquad |w|=1.
\]
Polynomials have arbitrary complex coefficients, including zero coefficients and degrees below the given upper bound. Samples are individually labelled by their spatial locations; no phase, coefficient normalization, or genericity assumption is imposed. The zero polynomial is included.

## Proof
**Step 1: A rational-function rigidity lemma.** Let \(H\) be a nonzero rational function such that \(|H(z)|=1\) at every point of the noncircular ellipse at which \(H\) is finite. Define \(h(w)=H(cw+d/w)\), a nonzero rational function in \(w\). Since \(d=cr\), the parametrization has the deck symmetry
\[
z(r/w)=z(w),\qquad h(r/w)=h(w).\tag{1}
\]
For a rational function \(u\), let \(u^*(w)=\overline{u(\overline w)}\), which conjugates the coefficients. The unit-modulus condition on infinitely many points of \(|w|=1\) gives the rational-function identity
\[
h(w)h^*(1/w)=1.\tag{2}
\]
(Any isolated poles or zeros of the original expression are bypassed when establishing the identity on infinitely many other points.) Replacing \(w\) by \(r/w\) in (2) and applying (1) yields
\[
h(w)h^*(w/r)=1.
\]
Comparing this with (2), and using that \(h\not\equiv0\), gives \(h^*(1/w)=h^*(w/r)\). Coefficientwise conjugation then gives \(h(1/w)=h(w/r)\). By (1), \(h(w/r)=h(r^2/w)\), so after replacing \(w\) by \(1/v\) we obtain
\[
h(v)=h(r^2v).\tag{3}
\]
A rational function has a Laurent expansion \(h(v)=\sum_{k=-K}^{\infty}c_kv^k\) in some punctured neighborhood of zero. Equation (3) forces \(c_k(1-r^{2k})=0\) for each integer \(k\). Since \(0<r<1\), only \(k=0\) is possible. Hence \(h\) is constant. As \(z(w)\) is a nonconstant rational map, \(H\) itself is constant; by the boundary condition this constant has modulus one.

**Step 2: Polynomial phase rigidity.** If \(|P|=|Q|\) on \(E\) and \(P\not\equiv0\), the nonzero ratio \(H=Q/P\) is rational and has modulus one wherever defined on \(E\). Step 1 implies \(H=\lambda\) with \(|\lambda|=1\); thus \(Q=\lambda P\). If \(P\equiv0\), then \(Q\) has infinitely many zeros and is also zero, so the assertion holds.

**Step 3: Finite sampling.** If \(P\) has degree at most \(n\), then \(P(z(w))\) is a Laurent polynomial with exponents between \(-n\) and \(n\). Consequently
\[
I_P(t)=|P(ce^{it}+de^{-it})|^2
\]
is a trigonometric polynomial of degree at most \(2n\), and the same holds for \(I_Q\). Thus \(I_P-I_Q\), unless zero, has at most \(4n\) distinct zeros modulo \(2\pi\): multiply its Laurent polynomial by \(w^{2n}\) to obtain a polynomial of degree at most \(4n\). The parametrization \(t\mapsto z(e^{it})\) is one-to-one on the ellipse, so equality at any \(4n+1\) distinct ellipse points forces equality at all of them. Step 2 now applies.

**Step 4: The circular exception.** For a circle of center \(z_0\) and radius \(R>0\), put \(u=(z-z_0)/R\). The distinct degree-one polynomials \(P(z)=u-2\) and \(Q(z)=1-2u\) satisfy \(|P(z)|=|Q(z)|\) whenever \(|u|=1\), but are not unimodular scalar multiples. Hence no set of circle samples, finite or infinite, has properties 2 or 3 for all degree-one inputs.

Translation and rotation of the ellipse preserve all arguments, completing the equivalence.

## Verification
The main argument consists entirely of rational-function identities and a finite-degree root count; no infinite statement is inferred from a finite computation. The companion executable checker verifies the deck identity exactly, the coefficientwise intensity-band limit for multiple Gaussian-integer polynomials, the maximal \(2n\) harmonic's existence in example polynomials, the circle counterexample, and representative numerical interpolation identities. Run with `python CHECK.py`. Its checks are supplementary to Steps 1–4.

## Relationship to prior work
Chalendar and Partington (2024) establish phase rigidity from two lines at irrational relative angles and from specified pairs of circles for holomorphic classes. Their hypotheses involve two loci rather than an arbitrary single ellipse. Perez (2020) proves corresponding two-line and two-circle results. Orevkov and Pakovich (2023) investigate when level sets of rational functions have common components and develop a general rational-lemniscate framework; their inspected statements do not identify the single-noncircular-ellipse criterion or the all-degree labelled finite-sample count proved here. The proof is elementary and does not claim those background results as new.

The uniqueness mechanism is specific to rational dependence on \(z\); the conclusion is not asserted for arbitrary functions holomorphic only on a neighborhood of the ellipse. The circle counterexample is the classical reciprocal-polynomial ambiguity.

## Limitations
The finite bound \(4n+1\) is sufficient, not claimed to be optimal, or quantitatively stable under measurement noise. No reconstruction complexity, uniform conditioning, or extension to all analytic functions is asserted. Historical priority remains provisional: a broader earlier classification of rational lemniscates might imply the rigidity lemma even if it does not state the polynomial sampling corollary. The comparison was with the accessible cited text and mathematical-record searches, not a proof of worldwide uniqueness.

## References
1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, first posted 2024-03-24, https://arxiv.org/abs/2403.16255 .
2. S. Orevkov and F. Pakovich, *On intersection of lemniscates of rational functions*, first posted 2023-09-10, https://arxiv.org/abs/2309.04983 .
3. R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, first posted 2020-09-04, https://arxiv.org/abs/2009.02061 .
