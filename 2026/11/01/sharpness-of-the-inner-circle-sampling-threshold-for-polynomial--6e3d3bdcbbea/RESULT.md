# Sharpness of the inner-circle sampling threshold for polynomial phase retrieval

## Finding

Fix an integer \(d\ge1\) and radius \(0<r<1\). Let \(\mathcal P_d\) denote the complex polynomials of degree at most \(d\). Suppose the magnitude of a polynomial is measured on the entire unit circle and additionally at a prescribed set of distinct points on the interior circle \(r\mathbb T\).

The smallest integer \(m\) for which **every choice of \(m\) distinct interior-circle points** guarantees recovery of **every** \(f\in\mathcal P_d\) up to a unimodular multiple is
\[
\boxed{m=2d-1.}
\]
The sufficiency of \(2d-1\) samples is the published 2017 result of Pohl, Li and Boche (Lemma 6 together with the boundary measurements), **not claimed as new here**. The contribution is that this threshold is optimal for every degree and every inner-circle radius: for each \(d\ge2\) there exist two non-proportional polynomials having identical magnitudes on the entire unit circle and at \(2d-2\) distinct inner-circle points. They admit fully explicit, two- or three-term formulas.

For \(d\ge3\), choose the positive number \(A\) by
\[
A^2=\frac{1-r^{2d}}{r^2-r^{2d-2}},
\]
and set
\[
f(z)=1+A z^{d-1},\qquad g(z)=A z+z^d.
\]
Then \(|f|=|g|\) on the unit circle, and the inner-circle intensity difference is exactly
\[
|f(re^{it})|^2-|g(re^{it})|^2
=2A r^{d-1}(1-r^2)\cos((d-1)t).
\]
Consequently, the same magnitudes occur at exactly \(2d-2\) distinct inner-circle points. The case \(d=2\) has an explicit pair described below, and the case \(d=1\) is also sharp.

## Assumptions and scope

All polynomials have complex coefficients and degree at most \(d\); no root-location or nonvanishing condition is imposed. The outer-circle information consists of \(|f(z)|\) for every \(|z|=1\). The interior sample locations are arbitrary distinct points of one fixed circle \(|z|=r\), with \(r\) strictly between zero and one. "Optimal" means worst-case universal sampling over all such finite sets: it does **not** assert that each particular smaller sampling configuration admits a collision. Global phase is the only allowed ambiguity.

## Proof

**Known sufficiency, included to establish the exact cutoff.** Let \(f,g\in\mathcal P_d\) have equal magnitudes on \(|z|=1\), and write \(f(z)=\sum_{j=0}^d a_jz^j\) and \(g(z)=\sum_{j=0}^d b_jz^j\), allowing zero leading coefficients. The \(d\)-th Fourier coefficient of their unit-circle squared-magnitude difference is \(a_d\overline{a_0}-b_d\overline{b_0}\), hence zero. On the circle of radius \(r\), the \(d\)-th Fourier coefficient is precisely \(r^d\) times this difference, hence also zero. Therefore
\[
H_r(t)=|f(re^{it})|^2-|g(re^{it})|^2
\]
is a real trigonometric polynomial of degree at most \(d-1\). Multiplication by \(e^{i(d-1)t}\) produces an ordinary polynomial of degree at most \(2d-2\) in \(e^{it}\). Unless \(H_r\equiv0\), it cannot have \(2d-1\) distinct zeros. Thus equality at \(2d-1\) distinct interior points forces equal moduli on both complete circles.

For completeness, equality on two concentric circles forces global phase. If one polynomial vanishes identically, the other does too. Otherwise, the rational function \(R=f/g\) satisfies the meromorphic reflection identity \(R(z)\overline{R(s^2/\overline z)}=1\) for each \(s\in\{1,r\}\). Combining the two identities yields \(R(r^2z)=R(z)\) as an identity of rational functions (initially off poles and zeros). The Laurent expansion of \(R\) near zero has only its constant term, since \(r^{2k}\ne1\) for every nonzero integer \(k\); hence \(R\) is constant. Boundary equality makes its modulus one. This reproduces the published sufficiency argument by an elementary direct route.

**New necessity for every degree.** Suppose \(d\ge3\). Take the two polynomials in the finding. The denominator defining \(A^2\) is positive because \(r^2>r^{2d-2}\) for \(d\ge3\). They obey the reciprocal identity \(g(z)=z^d\overline{f(1/\overline z)}\) for \(z\ne0\); continuity gives the asserted boundary modulus equality. Expanding on the smaller circle gives
\[
\begin{aligned}
|f(re^{it})|^2&=1+A^2r^{2d-2}+2Ar^{d-1}\cos((d-1)t),\\
|g(re^{it})|^2&=A^2r^2+r^{2d}+2Ar^{d+1}\cos((d-1)t).
\end{aligned}
\]
The constant terms cancel exactly by the defining equation for \(A\). The difference is the claimed nonzero cosine, which has exactly \(2d-2\) distinct zeros modulo \(2\pi\). The polynomials are not scalar multiples because their constant terms are different (one equals one, the other zero).

For \(d=2\), fix any real \(c\ne0\) and put
\[
f(z)=1+ic z+z^2,\qquad g(z)=1-ic z+z^2.
\]
On \(|z|=1\), division by \(z\) shows \(|f(z)|=|2\cos t+ic|=|2\cos t-ic|=|g(z)|\). Direct expansion for the smaller circle gives
\[
|f(re^{it})|^2-|g(re^{it})|^2=-4cr(1-r^2)\sin t,
\]
which vanishes at exactly two distinct points. The two polynomials are not scalar multiples.

For \(d=1\), the familiar reciprocal pair \(f(z)=1+az\), \(g(z)=\overline a+z\), with \(|a|\ne1\), has equal modulus on the unit circle without being proportional; thus no interior measurement is insufficient. The degree-zero interior intensity difference equals \((1-|a|^2)(1-r^2)\), so the single-sample sufficiency already proved applies. Therefore the exact universal cutoff is \(2d-1\) for every \(d\ge1\). \(\square\)

## Verification

The algebraic expansion proves the identity for all admissible degrees and radii. A standalone standard-library checker `checker.py` tests reciprocal-circle identities and the explicit inner-circle differences across a deterministic set of degrees, radii and angles. It also checks that the constructed degrees and coefficient supports meet the assumptions. Numerical checks are corroborative; they do not establish the universal quantifiers. The proof of sharpness itself uses no numerical calculation.

## Relationship to prior work

Pohl, Li and Boche (2017), Lemmas 5–6 and Theorem 7, **already establish the \(2d-1\) sufficient interior sampling count** after boundary magnitude information (or \(2d+1\) outer samples). The present result explicitly makes no originality claim for that bound, for trigonometric interpolation, or for the two-circle uniqueness theorem. Its distinct contribution is a uniform all-degree, all-radius necessity construction, completing the exact minimax threshold within this geometric acquisition scheme.

Chalendar and Partington (arXiv:2403.16255, first submitted 2024-03-24) study holomorphic phase retrieval on unions of circles and lines, including full-circle uniqueness. Their accessible abstract is background evidence rather than proof of absence of the sharp finite cutoff. Previously established balanced-grid phase retrieval with both circles finitely sampled is a different acquisition model and does not imply this lower bound.

## Limitations

The lower bound is a worst-case statement: the \(2d-2\) indistinguishable points are explicitly constructed, not arbitrary prescribed points. No noise-stability or quantitative inverse bound is asserted. No assertion of independent review is made. Priority assessment may be affected by historical results not located in accessible full text, including alternative descriptions of reciprocal-polynomial zero flips.

## References

1. V. Pohl, N. Li, H. Boche, “Phase retrieval in spaces of analytic functions on the unit disk,” *2017 International Conference on Sampling Theory and Applications*, 336–340, DOI:10.1109/SAMPTA.2017.8024411. Author-uploaded full text consulted, especially Lemmas 5–6 and Theorem 7.
2. I. Chalendar, J. R. Partington, “Phase retrieval on circles and lines,” arXiv:2403.16255, first publicly submitted 2024-03-24, subsequently *Canadian Mathematical Bulletin* (2024). Abstract and bibliographic record consulted.
