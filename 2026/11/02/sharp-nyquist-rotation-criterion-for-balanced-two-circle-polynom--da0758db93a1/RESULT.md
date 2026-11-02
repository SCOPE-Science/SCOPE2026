# Sharp Nyquist rotation criterion for balanced two-circle polynomial phase retrieval

## Finding

**Theorem.** Fix an integer \(d\ge1\), distinct radii \(0<r<s<1\), and an angular offset \(\delta\in\mathbb R\). Form the two regular \(2d\)-gons

\[
\Omega_{r}=\{r e^{\pi i k/d}:0\le k<2d\},\qquad
\Omega_{s,\delta}=\{s e^{i\delta+\pi i k/d}:0\le k<2d\}.
\]

The intensity map \(P\mapsto (|P(z)|^2)_{z\in\Omega_{r}\cup\Omega_{s,\delta}}\) is injective, modulo multiplication of polynomials by constants of modulus one, on **all complex polynomials of degree at most \(d\)** if and only if

\[
\boxed{\sin(d\delta)\ne0.}
\]

For a nonresonant offset, the only angular alias in the sampled squared magnitudes is explicitly invertible. After normalizing by the appropriate radial powers, its two-real-variable coefficient recovery matrix is

\[
B_{\delta}=\begin{pmatrix}1&0\\\cos(d\delta)&-\sin(d\delta)\end{pmatrix}.
\]

Its singular values are \(\sqrt{1+|\cos(d\delta)|}\) and \(\sqrt{1-|\cos(d\delta)|}\). Hence its spectral condition number is

\[
\boxed{\kappa_2(B_{\delta})=
\sqrt{\frac{1+|\cos(d\delta)|}{1-|\cos(d\delta)|}}}
\]

when \(\sin(d\delta)\ne0\), and the **unique optimal offset modulo a grid step \(\pi/d\)** is the half-step \(\delta=\pi/(2d)\), where both singular values are one. This is a conditional linear stability statement for the highest Fourier coefficient, not an estimate for reconstruction of all polynomial coefficients.

## Assumptions and scope

All intensities are exact squared moduli of point evaluations. The two radii are fixed, positive, distinct, and strictly less than one. Degrees smaller than \(d\), including constant and zero polynomials, are included. No lower bound on the leading or constant coefficient is assumed. The second polygon may be rotated by any real angle. Angular offsets are considered modulo \(\pi/d\), since that period relabels its vertices. Equal radii are not asserted to give phase retrieval.

## Proof

**1. Intensity Fourier coefficients.** Write

\[
P(z)=\sum_{j=0}^{d}a_j z^j,\qquad
U_t(\theta)=|P(te^{i\theta})|^2=\sum_{m=-d}^{d}c_m(t)e^{im\theta}.
\]

For \(0\le m\le d\), direct multiplication gives

\[
c_m(t)=t^m\sum_{j=0}^{d-m}a_{j+m}\overline{a_j}t^{2j},\qquad
c_{-m}(t)=\overline{c_m(t)}.
\]

In particular \(c_d(t)=t^d A\), where \(A=a_d\overline{a_0}\) is independent of the radius. Set \(N=2d\) and define the angular discrete Fourier transform of the observed real intensities on a radius-\(t\), offset-\(\phi\) polygon by

\[
\widehat U_{t,\phi}(m)=\frac1N\sum_{k=0}^{N-1}U_t(\phi+2\pi k/N)\,
e^{-im(\phi+2\pi k/N)}.
\]

The root-of-unity identity annihilates all unmatched Fourier indices modulo \(N\). Since \(U_t\) has degree \(d=N/2\), for \(0\le m<d\) no modes alias, and

\[
\widehat U_{t,\phi}(m)=c_m(t).
\]

At the Nyquist mode \(m=d\), exactly the modes \(d\) and \(-d\) alias, giving

\[
\widehat U_{t,\phi}(d)=t^d\big(A+e^{-2id\phi}\overline A\big).
\]

**2. Removing the only alias.** The two observed real numbers

\[
X=\frac{\widehat U_{r,0}(d)}{2r^d},\qquad
Y=\frac{\widehat U_{s,\delta}(d)}{2s^d}e^{id\delta}
\]

are real, with exact identities

\[
X=\operatorname{Re}A,\qquad
Y=\operatorname{Re}(e^{id\delta}A).
\]

Writing \(A=u+iv\) therefore yields

\[
\binom X Y=
\begin{pmatrix}1&0\\\cos(d\delta)&-\sin(d\delta)\end{pmatrix}\binom u v.
\]

When \(\sin(d\delta)\ne0\), the inverse is explicit:

\[
A=X+i\frac{X\cos(d\delta)-Y}{\sin(d\delta)}.
\]

All remaining intensity Fourier coefficients on *both* circles were already read directly from the non-Nyquist DFT modes. Thus the original \(4d\) real observations uniquely determine the entire continuous functions \(U_r\) and \(U_s\) at both radii.

**3. Two concentric circles force phase agreement.** Suppose polynomials \(P,Q\) have identical intensity on both complete circles. If \(P\equiv0\), then \(Q\equiv0\), so assume neither is identically zero. Their rational quotient \(R=P/Q\) has modulus one at every non-pole point of each circle. Let \(R^\sharp(w)=\overline{R(\overline w)}\), a rational function. Reflection across each circle gives the rational identities

\[
R(z)R^\sharp(r^2/z)=1,\qquad
R(z)R^\sharp(s^2/z)=1.
\]

The meromorphic identities imply \(R^\sharp(w)=R^\sharp((s/r)^2w)\). A rational function invariant under multiplication of its argument by a real factor strictly greater than one must be constant: its Laurent expansion at zero otherwise contains some term with nonzero index, whose coefficient is altered by that dilation. Therefore \(R\) is constant; equal magnitudes make its constant unimodular. This proves injectivity, even if any coefficients of \(P,Q\) vanish. The two-circle rigidity is also consistent with Chalendar--Partington's continuous-data theorem [1].

**4. Necessity at resonance.** If \(\sin(d\delta)=0\), then \(e^{id\delta}\) is real, equal to \(1\) or \(-1\). Consequently \(z^d\) is real on *every point of both grids*. The distinct degree-\(d\) polynomials

\[
P_+(z)=1+iz^d,\qquad P_-(z)=1-iz^d
\]

have identical moduli on all sampling points, because \(1+it\) and \(1-it\) have the same modulus for every real \(t\). They are not unimodular scalar multiples. Hence a resonant offset never performs phase retrieval.

**5. Exact offset conditioning.** Write \(c=\cos(d\delta)\) and \(h=\sin(d\delta)\). The trace of \(B_\delta^{\mathsf T} B_\delta\) is two and its determinant is \(h^2=1-c^2\); its two eigenvalues are \(1\pm|c|\). Their square roots are the two singular values stated above. Since \(\kappa_2\ge1\), with equality exactly when \(c=0\), its unique minimizer modulo the angular step is the half-step \(\delta=\pi/(2d)\).

## Verification

The accompanying standard-library Python script `check.py` reproduces the discrete Fourier identities, direct top-mode inversion, normalized Fourier reconstruction, resonant ambiguity examples, and the optimal half-step condition in dimensions \(1\le d\le9\). It passed 9,639 deterministic floating-point assertions with seed 20261026. These finite arithmetic tests are corroboration; the universal statement follows from the displayed algebraic identities and rational-function argument. Reproduce with `python3 check.py`.

## Relationship to prior work

Pohl, Li and Boche [2, Theorem 7] obtain \(4d\) evaluations for degree-\(d\) polynomial phase retrieval using an *unbalanced* pattern: \(2d+1\) distinct points on one circle and \(2d-1\) on another. Their theorem does not give injectivity for the **balanced** \(2d+2d\) pattern, where both individual rings undersample the single Nyquist harmonic. Chalendar and Partington [1, Theorem 2.16] establish phase retrieval for complete, distinct, nested circles; they do not resolve precisely which finite critical cyclic samples suffice. Bodmann and Hammen [3, Theorem 2.3] give a \(4d\)-measurement construction of an intersecting-circle configuration for degree-\(d\) polynomials (under a change of their dimension notation), not the concentric balanced-grid resonance and optimal-offset classification.

The new assertion is the **if-and-only-if geometric phase diagram and exact highest-harmonic angular conditioning for an equal-budget two-ring grid**. The discrete Fourier calculation and the concentric-circle uniqueness statement are established ingredients; neither alone determines the critical balanced-grid phase diagram. Priority beyond the identified sources remains subject to broader human literature review.

## Limitations

This is an exact finite-dimensional algebraic result for complex polynomials and *two distinct concentric circles*. It does not assert phase retrieval for arbitrary analytic functions from finitely many samples; it does not classify irregular two-ring grids or more than two radii. Conditioning is proved only for normalized linear recovery of the one complex Nyquist Fourier coefficient; global phaseless coefficient recovery may be poorly conditioned as radii approach one another, or as a polynomial approaches exceptional coefficient patterns. The algorithmic recovery of coefficients after obtaining the full two-circle intensities is not numerically analyzed. The literature assessment is not an independence or exhaustive priority certification.

## References

[1] I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, first posted March 24, 2024, especially Theorem 2.16; https://arxiv.org/abs/2403.16255 .

[2] V. Pohl, N. Li and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, Sampling Theory and Applications (SampTA), 2017, DOI:10.1109/SAMPTA.2017.8024411, especially Theorem 7; https://doi.org/10.1109/SAMPTA.2017.8024411 .

[3] B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), especially Theorem 2.3; https://arxiv.org/abs/1302.5487 .
