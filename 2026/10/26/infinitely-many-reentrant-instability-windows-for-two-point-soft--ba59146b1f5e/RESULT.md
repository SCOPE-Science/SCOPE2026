# Infinitely many reentrant instability windows for two point softeners on a Winkler beam

## Finding
Let \(H_{a,d}\) be the fourth-order self-adjoint operator on the infinite real line associated with
\[
\mathfrak q_{a,d}[u]=\int_{\mathbb R}\bigl(|u''(x)|^2+|u(x)|^2\bigr)\,dx-a\bigl(|u(0)|^2+|u(d)|^2\bigr),\qquad u\in H^2(\mathbb R).
\]
The two identical concentrated softeners have strength \(a>0\) and separation \(d>0\). For every
\(\sqrt2<a<2\sqrt2\), the number of strictly negative eigenvalues (with multiplicity) satisfies
\[
N_-(H_{a,d})=\mathbf 1_{\left\{\left|e^{-d/\sqrt2}\left(\cos\frac d{\sqrt2}+\sin\frac d{\sqrt2}\right)\right|>\frac{2\sqrt2-a}{a}\right\}}.
\]
In particular, **as separation varies through all positive real numbers, the set of unstable separations consists of exactly**
\[
\boxed{\quad C(a)=\left\lceil\frac1\pi\log\frac{a}{2\sqrt2-a}\right\rceil\quad}
\]
**pairwise disjoint bounded open intervals**. It has arbitrarily many components as \(a\uparrow2\sqrt2\), although each of the two softeners is individually insufficient to cause instability.

There is one component next to zero separation for every \(a>\sqrt2\). A further component centered about separation \(d_n=\sqrt2\,n\pi\), for each integer \(n\ge1\), exists precisely when
\[
\boxed{\quad a>a_n=\frac{2\sqrt2}{1+e^{-n\pi}}.\quad}
\]
At the equality \(a=a_n\) and separation \(d=d_n\), the beam has a square-integrable **zero-frequency neutral mode** but **no strictly negative eigenvalue**. Therefore the strict inequalities are essential. The transition strengths \(a_n\) increase to the isolated-defect critical strength \(2\sqrt2\).

## Assumptions and scope
The model is a linear Euler--Bernoulli beam of infinite extent on a uniform positive Winkler foundation, with no axial compression and two *destabilizing concentrated increments* of negative stiffness. The nondimensionalization uses the characteristic length \(\ell=(EI/k)^{1/4}\), where \(EI>0\) is bending rigidity and \(k>0\) is the Winkler stiffness per length. For a physical negative point-stiffness magnitude \(\kappa>0\), the dimensionless coefficient is \(a=\kappa/(k\ell)\), and \(d\) is physical separation divided by \(\ell\). The kinetic mass density is positive and does not affect the sign of squared natural frequencies. Instability here means the existence of a **strictly negative stiffness eigenvalue**, corresponding to exponential growth in undamped linear transverse dynamics; a zero eigenvalue is neutral rather than unstable.

Only the regime \(\sqrt2<a<2\sqrt2\) is claimed for the component formula. Separated sites satisfy \(d>0\). Point softeners are idealized negative incremental stiffnesses, not arbitrary passive reductions of a finite-width foundation.

## Proof
**1. The quadratic form and its zero-energy Green kernel.** Point evaluation is continuous on \(H^2(\mathbb R)\). Hence the displayed quadratic form is closed and bounded below, and defines a self-adjoint operator \(H_{a,d}\). Set \(H_0=D^4+1\), with domain \(H^4(\mathbb R)\). Fourier inversion and the decaying solutions of \((D^4+1)G=\delta_0\) give
\[
G(x)=\frac{e^{-|x|/\sqrt2}}{2\sqrt2}\left(\cos\frac{|x|}{\sqrt2}+\sin\frac{|x|}{\sqrt2}\right).
\]
The normalization follows either from \(G^{(3)}(0+)-G^{(3)}(0-)=1\) and continuity of its two lower derivatives, or from
\(G(x)=(2\pi)^{-1}\int_{\mathbb R}e^{i\xi x}(\xi^4+1)^{-1}\,d\xi\). In particular, \(G(0)=1/(2\sqrt2)\).

**2. Exact negative inertia.** Let \(E:H^2(\mathbb R)\to\mathbb C^2\) be \(Eu=(u(0),u(d))\). Upon making the invertible form transformation \(v=H_0^{1/2}u\), the form becomes
\[
\|v\|^2-a\|EH_0^{-1/2}v\|^2.
\]
Its strictly negative inertia equals the number of eigenvalues greater than one of the positive rank-two operator \(a(EH_0^{-1/2})(EH_0^{-1/2})^*\). The latter has matrix
\[
a\begin{pmatrix}G(0)&G(d)\\G(d)&G(0)\end{pmatrix},
\]
with eigenvalues \(a(G(0)+G(d))\) and \(a(G(0)-G(d))\). This finite-rank inertia identity is exact for the continuum operator; no truncation or sampling is used. Finite-rank form perturbations also preserve the essential-spectrum bottom \(1\).

**3. The one-mode instability criterion.** Write \(t=d/\sqrt2\) and \(F(t)=e^{-t}(\cos t+\sin t)\). The two rank-two eigenvalues are
\[
\frac{a}{2\sqrt2}(1+F(t)),\qquad \frac{a}{2\sqrt2}(1-F(t)).
\]
For \(\sqrt2<a<2\sqrt2\), their average is less than one, so they cannot both exceed one. At least one exceeds one if and only if
\(\lvert F(t)\rvert>r(a)\), where \(r(a)=(2\sqrt2-a)/a\in(0,1)\). Equality gives a zero mode of \(H_{a,d}\), not a negative mode.

**4. Exact separation-component count.** Differentiation yields
\[
F'(t)=-2e^{-t}\sin t.
\]
The positive zeros of \(F\) are \(t=(n+3/4)\pi\), for integers \(n\ge0\). On the first lobe \((0,3\pi/4)\), \(F\) strictly decreases from \(1\) to \(0\), so \(\lvert F\rvert>r\) gives one interval. Every later lobe contains exactly one extremum of \(\lvert F\rvert\), attained at \(t=n\pi\), with height \(e^{-n\pi}\) for \(n\ge1\), and zero at both endpoints. Its strict superlevel set is one open interval exactly when \(e^{-n\pi}>r\), otherwise empty. Thus the number of separation components is
\[
\#\{n\in\mathbb Z_{\ge0}:e^{-n\pi}>r\}
=\left\lceil \frac{\log(1/r)}\pi\right\rceil.
\]
Substitution for \(r(a)\) gives the claimed exact count. The \(n\)-th later component appears when \(r(a)<e^{-n\pi}\), equivalently \(a>a_n\). At equality, the maximum reaches the threshold at only its central point; it contributes no open unstable interval. As \(a\uparrow2\sqrt2\), the logarithm diverges and the number of components tends to infinity. \(\square\)

## Verification
The companion standalone `beam_instability_checker.py` evaluates the zero-energy Green function independently by Fourier quadrature, checks strict threshold inclusions and the exact component count, and compares negative-eigenvalue counts against an independent spatial finite-difference discretization on long periodic domains. It produced `PASS: 10079 quadrature/phase/threshold/finite-difference checks` with Python, NumPy and SciPy. Execute `python beam_instability_checker.py`. Numerical sampling and domain discretization corroborate but do not establish the infinite-separation theorem; the exact proof above does.

## Relationship to prior work
Coman [1] treats localized buckling from spatially varying foundation properties on a **finite** elastica, using asymptotic and numerical tools. Wang [2] treats an **infinite compressed** foundation-supported beam weakened by joints or cracks, with a distinct interface constitutive law. Indeitsev--Kuklin--Mochalova [3] analyze a **single finite-width foundation defect** in an infinite beam under compression, including localized frequencies and their zero crossings. Shishkina--Gavrilov--Mochalova [4] solve the **single negative point-spring** infinite-beam problem and provide the isolated-defect threshold. Abramian and collaborators [5] study **multiple concentrated spring inclusions in a finite beam**, including perturbative spatial resonance of vibration and buckling mode indices. Their first-order finite-domain formulas do not imply the exact nonperturbative separation-component count in the infinite-domain, two-defect model. The claimed contribution is the **exact reentrant instability classification and infinite sequence of sharp placement thresholds**, not the known beam Green function, the single-inclusion theory, or the general finite-rank method.

## Limitations
Negative point stiffness is an idealization, and no conclusion is asserted for nonlinear postbuckling, finite beam boundaries, viscous damping, nonidentical defects, random disorder, finite-width compliant inclusions, or axial loading. An explicit formula for the number of components does not establish their mechanical robustness in nonideal systems. Priority cannot be guaranteed against inaccessible historical technical reports or mathematical treatments of biharmonic point interactions. Relevant primary articles [1] and [2] were materially accessible only through abstracts and bibliographic descriptions, not their complete texts. The theorem has not received an independent mathematical audit.

## References
[1] C. D. Coman, *Inhomogeneities and localised buckling patterns*, IMA Journal of Applied Mathematics 71 (2006), 133–152, DOI:10.1093/imamat/hxh088; first online 2005-05-17.

[2] C. Y. Wang, *Buckling of a Weakened Infinite Beam on an Elastic Foundation*, Journal of Engineering Mechanics 136 (2010), 534–537, DOI:10.1061/(ASCE)EM.1943-7889.0000097.

[3] D. A. Indeitsev, T. S. Kuklin, and Yu. A. Mochalova, *Localization in a Bernoulli–Euler Beam on an Inhomogeneous Elastic Foundation*, Vestnik St Petersburg University Mathematics 48 (2015), 40–47, DOI:10.3103/S1063454115010069.

[4] E. V. Shishkina, S. N. Gavrilov, and Yu. A. Mochalova, *Non-stationary localized oscillations of an infinite Bernoulli-Euler beam lying on the Winkler foundation with a point elastic inhomogeneity of time-varying stiffness*, arXiv:1806.08667 (2018).

[5] Dynamics and buckling loads for a vibrating damped Euler–Bernoulli beam connected to an inhomogeneous foundation, *Archive of Applied Mechanics*, DOI:10.1007/s00419-020-01823-y (2020/2021), especially section 4, Example B, on finite-domain concentrated springs.
