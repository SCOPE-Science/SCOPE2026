# Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius

## Finding

Let \(\mathcal H\) be a nonzero complex Hilbert space. For any nonzero \(T\in\mathcal B(\mathcal H)\), let \(R=\omega(T)\), and let \(Q=\omega_2(T)\) be the \(L^2\)-Cartesian numerical radius of Audeh--Moradi--Sahoo [1]. Define its phase-self-adjoint distance by
\[
d(T)=\inf_{\phi\in\mathbb R,\ S=S^*}\|T-e^{i\phi}S\|.
\]
Then
\[
\boxed{\omega_2(T)^2-\frac{\omega(T)^2}{2}\ \ge\ \frac{d(T)^3}{2\pi\,\omega(T)}.}
\]
In particular, equality in the sharp lower comparison \(\omega_2(T)\ge \omega(T)/\sqrt2\) holds if and only if \(T\) is a unimodular multiple of a self-adjoint operator. The equivalent stability inequality
\[
d(T)\le \big(2\pi\,\omega(T)[\omega_2(T)^2-\tfrac12\omega(T)^2]\big)^{1/3}
\]
has the largest possible universal deficit exponent \(1/3\), even when restricted to normal four-dimensional operators. The displayed coefficient \(1/(2\pi)\) is a rigorous universal coefficient, not asserted optimal.

## Assumptions and scope

No normality, finite-dimensionality, spectral-gap, or compactness assumption is needed. All norms below are operator norms. Write \(T=H+iK\), where \(H=H^*\), \(K=K^*\), and define
\[
\omega(T)=\sup_{\|x\|=1}|\langle Tx,x\rangle|,\qquad
\omega_2(T)^2=\frac1{2\pi}\int_0^{2\pi}\|\cos\theta\,H+\sin\theta\,K\|^2\,d\theta.
\]
For an operator \(A\), \(\operatorname{Im}A=(A-A^*)/(2i)\). The distance has the exact elementary form
\[
d(T)=\min_{\phi\in[0,2\pi]}\|\operatorname{Im}(e^{-i\phi}T)\|.
\]
Indeed, for each fixed phase, the self-adjoint approximant \(\operatorname{Re}(e^{-i\phi}T)\) gives the upper bound; contractivity of the imaginary-part projection supplies the matching lower bound. A minimizing phase exists by continuity and compactness. Since \(T\ne0\), the numerical radius \(R\) is positive.

## Proof

**1. Symmetric numerical-range support.** Let \(W(T)=\{\langle Tx,x\rangle:\|x\|=1\}\) and let
\[
C=\operatorname{conv}(\overline{W(T)}\cup-\overline{W(T)})\ \subset\ \mathbb C.
\]
This is a compact centrally symmetric convex set. Its support function at angle \(\theta\) is
\[
h(\theta)=\max_{z\in C}\operatorname{Re}(e^{-i\theta}z)
           =\|\operatorname{Re}(e^{-i\theta}T)\|.
\]
It is \(\pi\)-periodic, so \(Q^2=\pi^{-1}\int_0^\pi h(\theta)^2\,d\theta\); moreover \(R=\max_{z\in C}|z|=\max_\theta h(\theta)\). Multiplication by a unit complex scalar does not affect \(R,Q,d\), so rotate until \(R\in C\) on the real axis. Central symmetry gives \(h(\theta)\ge R|\cos\theta|\). Thus the deficit \(\Delta=Q^2-R^2/2\) has the nonnegative integral representation
\[
\Delta=\frac1\pi\int_0^\pi\big(h(\theta)^2-R^2\cos^2\theta\big)\,d\theta.
\]

**2. A transverse support forces a cubic gap.** Set \(b=h(\pi/2)=\|\operatorname{Im}T\|\), so \(0\le b\le R\), and select a support point \(z=a+ib\in C\). If \(b=0\) the desired estimate is immediate. Let \(s=b/R\) and \(\alpha=\arctan s\). Choose the side of \(\pi/2\) pointing toward the sign of \(a\). For every \(0\le t\le\alpha\), at \(\theta=\pi/2-\operatorname{sgn}(a)t\) (either sign if \(a=0\)),
\[
h(\theta)\ge |a|\sin t+b\cos t\ge b\cos t\ge R\sin t=R|\cos\theta|.
\]
Therefore the nonnegative integrand above can be restricted to this side of the interval, giving the exact one-dimensional estimate
\[
\begin{aligned}
\Delta&\ge\frac1\pi\int_0^\alpha\big(b^2\cos^2t-R^2\sin^2t\big)\,dt\\
&=\frac{R^2}{2\pi}\big[s+(s^2-1)\arctan s\big].
\end{aligned}
\]
The bracket is at least \(s^3\), because
\[
s+(s^2-1)\arctan s=s^3+(1-s^2)(s-\arctan s)\ge s^3
\]
for \(s\in[0,1]\). Thus \(\Delta\ge b^3/(2\pi R)\). The phase-self-adjoint distance is no larger than this particular transverse imaginary norm, \(d(T)\le b\), proving
\[
\Delta\ge\frac{d(T)^3}{2\pi R}.
\]
If \(\Delta=0\) then \(d(T)=0\), whence a minimizing phase makes \(T\) self-adjoint. Conversely, for a phase multiple of a self-adjoint operator the support function is \(R|\cos(\theta-\phi)|\), and \(Q^2=R^2/2\).

**3. Optimality of the cubic exponent.** On \(\mathbb C^4\) consider the normal diagonal operator
\[
T_\varepsilon=\operatorname{diag}(1,-1,i\varepsilon,-i\varepsilon),\qquad0<\varepsilon\le1.
\]
Its numerical radius is \(R=1\), and for all real \(\theta\) the angular support is
\[
h_\varepsilon(\theta)=\max\{|\cos\theta|,\varepsilon|\sin\theta|\}.
\]
Direct integration on the four quadrants, splitting at \(\arctan\varepsilon\), gives
\[
\Delta_\varepsilon
=\frac{\varepsilon+(\varepsilon^2-1)\arctan\varepsilon}{\pi}
=\frac{4}{3\pi}\varepsilon^3+O(\varepsilon^5)
\qquad(\varepsilon\downarrow0).
\]
On the other hand,
\[
d(T_\varepsilon)=\min_\phi\max\{|\sin\phi|,\varepsilon|\cos\phi|\}
=\frac{\varepsilon}{\sqrt{1+\varepsilon^2}}
\sim\varepsilon.
\]
Hence \(\Delta_\varepsilon/d(T_\varepsilon)^3\to4/(3\pi)\). In particular, for any exponent \(q<3\), no lower estimate \(\Delta\ge c\,d(T)^q/R^{q-2}\) with \(c>0\) can hold uniformly; equivalently, no improvement of the \(1/3\) distance-versus-deficit exponent is possible. This does not assert sharpness of the numerical coefficient \(1/(2\pi)\).

## Verification

Every step above is dimension-free and deterministic: the support identity follows from the real part of the numerical range, the one-sided integral has elementary antiderivatives, and the diagonal example is an exact evaluation of four scalar eigenvalues. The auxiliary standalone script `verify_example.py` recomputes the normal diagonal example by direct angular quadrature and compares it with its closed formula. Finite checks are supplementary; the Hilbert-space theorem is proved by the preceding analytic argument.

## Relationship to prior work

Audeh--Moradi--Sahoo [1, Theorem 4] introduced the angular \(L^2\)-Cartesian radius and proved the sharp lower estimate \(\omega_2(T)^2\ge\omega(T)^2/2\), with equality for self-adjoint operators. Their theorem does not state an operator-norm distance estimate, a quantitative inverse equality criterion, or the optimal \(1/3\) stability exponent. Kittaneh--Moslehian--Yamazaki [2] established the classical *supremal* Cartesian representation of \(\omega(T)\); that identity is used here but does not itself bound the difference between its squared angular average and half the maximum. The nearby generalized Euclidean operator-radius literature [3] concerns a different, supremal-type tuple invariant. The present theorem concerns the integrated invariant, a phase-self-adjoint distance in operator norm, and a sharp asymptotic obstruction in a normal four-dimensional family.

## Limitations

The constant \(1/(2\pi)\) is not claimed best. The optimal cubic *exponent* is the established sharp feature. The theorem concerns the Hilbert-space operator norm, not Schatten-norm distances or unbounded operators. The equality characterization applies to the lower bound for \(\omega_2\), not to unrelated numerical-radius inequalities. Other equivalent versions may be implicit in general convex-support literature; the accessible comparisons did not identify such coverage.

## References

[1] W. Audeh, H. R. Moradi, and S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1 (first public 4 October 2026), https://arxiv.org/html/2610.04844v1.

[2] F. Kittaneh, M. S. Moslehian, and T. Yamazaki, *Cartesian decomposition and numerical radius inequalities*, Linear Algebra and its Applications **471** (2015), 46--53, DOI:10.1016/j.laa.2014.12.016; open preprint arXiv:1511.02094.

[3] M. W. Alomari, G. Bercu, C. Chesneau, and H. Alaqad, *On Some Inequalities for the Generalized Euclidean Operator Radius*, Axioms **12** (2023), article 542, DOI:10.3390/axioms12060542 (generalized tuple setting).
