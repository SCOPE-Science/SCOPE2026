# Field-uniform quantitative stability for sharp finite-field parabolic extension

## Finding

Let \(\mathbb F_q\) be a finite field of odd characteristic \(p>3\), let \(\psi:\mathbb F_q\to\mathbb C\) be a nontrivial additive character, and define the finite parabolic extension operator
\[
\mathcal E_q f(X,Y)=\frac1q\sum_{t\in\mathbb F_q}f(t)\psi(Xt+Yt^2).
\]
Put
\[
N(f)=\frac1q\sum_t|f(t)|^2,\qquad
C_q=1+\frac1q-\frac1{q^2},\qquad
\mathfrak D_q(f)=C_qN(f)^3-\sum_{X,Y}|\mathcal E_q f(X,Y)|^6.
\]
The sharp finite-field extension theorem of González-Riquelme and Oliveira e Silva gives \(\mathfrak D_q(f)\ge0\) for every \(f\). For any \(A,B\in\mathbb F_q\), write \(\gamma_{A,B}(t)=\psi(At+Bt^2)\). Each \(\gamma_{A,B}\) is an extremizer.

**Exact transverse curvature.** If \(h=u+iv\) has zero complex mean, with real-valued \(u,v\), then, for real \(\varepsilon\to0\),
\[
\boxed{\mathfrak D_q(\gamma_{A,B}(1+\varepsilon h))
=\varepsilon^2\left[\left(3-\frac6q+\frac{12}{q^2}\right)N(u)
+\left(3-\frac6q\right)N(v)\right]+O_{q,h}(\varepsilon^3).}
\tag{1}
\]
With the normalized real inner product \(q^{-1}\sum_t\operatorname{Re}(h(t)\overline{k(t)})\), the half-Hessian of \(\mathfrak D_q\) at \(\gamma_{A,B}\) has exactly three levels: \(0\) of real multiplicity \(2\), \(3-6/q\) of multiplicity \(q-1\), and \(3-6/q+12/q^2\) of multiplicity \(q-1\). The kernel comprises complex scalar multiples of \(\gamma_{A,B}\). The least positive quadratic coefficient, \(3-6/q\), is sharp and occurs precisely for purely imaginary zero-mean perturbations relative to that chirp.

**A quantitative neighborhood independent of field size.** For every zero-mean \(h\) with \(r=\sqrt{N(h)}\le1/64\),
\[
\boxed{\mathfrak D_q(\gamma_{A,B}(1+h))\ge
\frac12\left(3-\frac6q\right)N(h)\ge\frac9{10}N(h).}
\tag{2}
\]
Thus the explicit radius does not shrink as \(q\) grows. The quadratic coefficient in (1) is optimal; neither the neighborhood radius nor the factor \(1/2\) in (2) is claimed optimal.

## Assumptions and scope

All unspecified sums range over \(\mathbb F_q\); the target extension norm uses counting measure and the source \(L^2\) norm uses normalized counting measure. The sharp global inequality invoked in (2) is known for characteristic strictly greater than three, including nonprime field orders. Formula (1) uses a real perturbation parameter; the coefficients are **half-Hessian eigenvalues**, not full-Hessian eigenvalues. The zero-mean condition fixes the complex scalar gauge. Since the chirp family is discrete modulo scalar multiplication, no infinitesimal translation or quadratic modulation zero directions occur.

The estimate controls the squared distance to the complex line through a specified chirp: if \(f=\gamma_{A,B}(1+h)\) and \(N(h)=r^2\), then
\[
\inf_{\lambda\in\mathbb C}N(f-\lambda\gamma_{A,B})=N(h)
\]
because \(\sum_t h(t)=0\). Statement (2) is local around each chirp line and does not assert a global distance-to-all-extremizers inequality.

## Proof

**1. Reduce to the constant chirp.** Multiplying the input by \(\gamma_{A,B}\) translates \((X,Y)\) to \((X+A,Y+B)\). This translation permutes \(\mathbb F_q^2\), so both terms of the deficit are unchanged: \(\mathfrak D_q(\gamma_{A,B}f)=\mathfrak D_q(f)\). It suffices to work at the constant input \(\mathbf1\).

**2. Compute the exact baseline.** Set \(Z(X,Y)=\mathcal E_q\mathbf1(X,Y)\). Additive orthogonality gives \(Z(0,0)=1\) and \(Z(X,0)=0\) for nonzero \(X\). For \(Y\ne0\), completing the square gives
\[
Z(X,Y)=q^{-1}G(Y)\psi\left(-\frac{X^2}{4Y}\right),
\qquad G(Y)=\sum_t\psi(Yt^2).
\]
The invertible substitution \((s,t)\mapsto(s-t,s+t)\) yields \(|G(Y)|^2=\sum_{a,b}\psi(Yab)=q\), whence \(|Z(X,Y)|^2=q^{-1}\) for \(Y\ne0\). Consequently
\[
\sum_{X,Y}|Z(X,Y)|^6=1+q(q-1)q^{-3}=C_q,
\]
consistent with the sharp extension theorem.

**3. Reconstruct the quadratic term.** Write \(H=\mathcal E_qh\). Because \(h\) has mean zero, \(H(0,0)=0\), so the points with \(Y=0\) make no contribution through second order. Directly multiplying the three holomorphic and three conjugate factors in \(|Z+\varepsilon H|^6\) gives the quadratic coefficient
\[
9\sum_{X,Y\ne0}|Z|^4|H|^2+
6\operatorname{Re}\sum_{X,Y\ne0}|Z|^2\overline Z^{\,2}H^2.
\tag{3}
\]
For each fixed \(Y\), Parseval in \(X\) gives \(\sum_X|H(X,Y)|^2=N(h)\). Thus the first term of (3) is \(9(q-1)N(h)/q^2\).

For the second term, expand \(h(t)=\sum_{a\ne0}c_a\psi(at)\) using \(c_a=q^{-1}\sum_t h(t)\psi(-at)\). Define the complex bilinear average \(Q(h)=q^{-1}\sum_t h(t)^2=\sum_{a\ne0}c_ac_{-a}\). The shifted Gauss sum identity reads
\[
\frac{H(X,Y)}{Z(X,Y)}=
\sum_{a\ne0}c_a\psi\left(-\frac{2aX+a^2}{4Y}\right),\qquad Y\ne0.
\]
Inserting this expression and using \(|Z|^6=q^{-3}\), the sum over \(X\) annihilates all pairs except \(b=-a\). Each remaining nonzero \(a\) contributes
\[
q^{-2}\sum_{Y\ne0}\psi\left(-\frac{a^2}{2Y}\right)=-q^{-2},
\]
by additive orthogonality and the bijection \(Y\mapsto Y^{-1}\). Therefore
\[
\sum_{X,Y\ne0}|Z|^2\overline Z^{\,2}H^2
=-\frac1{q^2}Q(h).
\tag{4}
\]
Equations (3)--(4) show that the quadratic coefficient in the extension sixth moment is
\[
\frac{9(q-1)}{q^2}N(h)-\frac6{q^2}\operatorname{Re}Q(h).
\tag{5}
\]
The bilinear average \(Q(h)\) is distinct from the nonnegative norm \(N(h)\).

**4. Normalize and classify the curvature.** Since \(\sum_t h(t)=0\),
\[
N(1+\varepsilon h)=1+\varepsilon^2N(h),\qquad
C_qN(1+\varepsilon h)^3=C_q+3C_q\varepsilon^2N(h)+O(\varepsilon^4).
\]
Subtract (5), use \(N(h)=N(u)+N(v)\) and \(\operatorname{Re}Q(h)=N(u)-N(v)\), and simplify. This proves (1). Both positive levels are strictly positive for \(q\ge5\). Homogeneity \(\mathfrak D_q(\lambda f)=|\lambda|^6\mathfrak D_q(f)\) and first-order stationarity at each extremizer remove the two scalar directions and all cross terms. Orthogonal real and imaginary mean-zero subspaces have dimension \(q-1\) each, giving all eigenvalues and multiplicities. Any nonzero imaginary mean-zero direction attains the smaller coefficient exactly to second order, proving optimality.

**5. Uniform nonasymptotic remainder.** Put \(r=\sqrt{N(h)}\le1\) and \(M(f)=\sum|\mathcal E_qf|^6\). The published sharp inequality gives \(M(h)\le C_qr^6\), while \(M(1)=C_q\). Hölder's inequality bounds the absolute coefficient of total order \(k\) in the six-factor expansion of \(M(1+h)\) by \(\binom6k C_q r^k\). Since \(N(1+h)^3=(1+r^2)^3\), the terms of order at least three in the full deficit have absolute value at most
\[
C_q(20r^3+18r^4+6r^5+2r^6)\le46C_qr^3.
\tag{6}
\]
The exact quadratic term (1) is at least \(b_qr^2\), where \(b_q=3-6/q\). As \(q\ge5\), \(b_q\ge9/5\) and \(C_q\le29/25\). For \(r\le1/64\),
\[
46C_qr\le\frac{46\cdot29}{64\cdot25}=\frac{667}{800}<\frac9{10}\le\frac{b_q}{2}.
\]
Combining this with (6) yields (2). All steps are uniform in the field order.

## Verification

The standalone script `verify.py` uses only the Python standard library. Run `python verify.py` to reconstruct the extension arrays, exact Gauss-magnitude pattern, quadratic coefficients, chirp invariance, and the quantitative neighborhood inequality for prime fields of orders \(5,7,11,13\) and the nonprime field of order \(25\). The final recorded line is `ALL_VERIFIED total_checks=1069. Finite tests are not the universal proof.` The unrestricted proof is the character-orthogonality and Hölder argument above; finite checks serve solely as independent computational tests.

## Relationship to prior work

González-Riquelme and Oliveira e Silva (2024, Theorem 1.3 and Section 6) prove the sharp global \(L^2\)-to-\(L^6\) extension inequality for the finite parabola in characteristic greater than three, with constant inputs among the extremizers and constant modulus necessary for any maximizer. Their result supplies the sharp global constant used here, but does not state the complete real Hessian or a quantitative neighborhood independent of field size.

A published complementary calculation, *Exact local sixth-moment stability of the parabola in characteristic three*, determines two local curvature bands in the excluded characteristic-three case. Its hypotheses do not cover characteristic greater than three, and its claim does not supply a field-uniform finite-radius inequality. The present argument uses quadratic Gauss-sum modulation and the characteristic-greater-than-three sharp global inequality to establish both (1) and (2). Work on anisotropic finite-field paraboloids concerns a two-dimensional frequency surface and a fourth moment; finite-field moment-curve endpoint problems likewise use a different exponent. Carneiro, Negro, and Oliveira e Silva (2021) investigate stability for Euclidean spheres, not finite parabolas.

## Limitations

The proved stability neighborhood is centered on a specified quadratic-character extremizer modulo complex scalars. No globally sharp stability constant for arbitrary input, no optimal positive neighborhood radius, and no classification of every finite-field parabolic extremizer is claimed. The exact quadratic spectral coefficients do not imply that the nonasymptotic factor \(1/2\) is optimal. The present calculations exclude characteristic two and three because the cited global sharp inequality assumes characteristic greater than three. Historical literature may contain an equivalent local calculation under a different normalization; the novelty assessment is therefore qualified.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public submission 2024-05-26, especially Theorem 1.3 and Section 6, https://arxiv.org/pdf/2405.16647.
2. E. Carneiro, G. Negro, and D. Oliveira e Silva, *Stability of sharp Fourier restriction to spheres*, arXiv:2108.03412, first public submission 2021-08-07, https://arxiv.org/pdf/2108.03412.
3. *Exact local sixth-moment stability of the parabola in characteristic three*, public mathematical finding, record `2026/10/11/SCOPE-exact-local-sixth-moment-stability-of-the-parabola-in-characteri--158763dab4f3` (comparison; distinct characteristic).
4. *Two-band Hessian and sharp local gap for anisotropic finite-field paraboloid extension*, public mathematical finding, record `2026/10/11/SCOPE-two-band-hessian-and-sharp-local-gap-for-anisotropic-finite-fiel--80ecd3989428` (comparison; different surface and fourth moment).
