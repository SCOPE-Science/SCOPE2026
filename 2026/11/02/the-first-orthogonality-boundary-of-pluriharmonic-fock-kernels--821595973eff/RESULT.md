# The first orthogonality boundary of pluriharmonic Fock kernels

## Finding

Let \(\mathrm{PH}^2_\alpha(\mathbb C^n)\) be the complex pluriharmonic Fock space under normalized Gaussian measure with parameter \(\alpha>0\). The reproducing kernel is
\[
K^{\mathrm{ph}}_\alpha(z,w)=2\operatorname{Re}\exp(\langle z,w\rangle/\alpha)-1,
\]
where \(\langle z,w\rangle=\sum_j z_j\overline{w_j}\). **The sharp origin-ball first-orthogonality radius** is \(\sqrt{\alpha\log2}\): whenever \(\|z\|,\|w\|\le R\) and \(R^2/\alpha<\log2\), the two evaluation kernels have strictly positive inner product. At equality \(R^2/\alpha=\log2\), orthogonality occurs precisely for \(w=-z\) with \(\|z\|=R\).

In one complex dimension, fix the equal-radius circle \(z=\sqrt{\alpha t}\), \(w=\sqrt{\alpha t}\,e^{i\theta}\), \(0\le\theta\le\pi\). For every \(t>\log2\) there is a well-defined *least* orthogonality angle \(\Theta(t)\in(0,\pi)\), the least positive root of
\[
2e^{t\cos\theta}\cos(t\sin\theta)=1.
\]
It is smooth and strictly decreasing for all \(t>\log2\), and its endpoint laws are
\[
\Theta(t)=\pi-\sqrt{\frac{2}{(\log2)(1-\log2)}}\,\sqrt{t-\log2}
+O\bigl((t-\log2)^{3/2}\bigr),\qquad t\downarrow\log2,
\]
\[
\Theta(t)=\frac{\pi}{2t}+\frac{\pi^3}{48t^3}+O(t^{-5}),\qquad t\to\infty.
\]
The least Euclidean chord \(d_\alpha(t)=2\sqrt{\alpha t}\sin(\Theta(t)/2)\) between two points on this circle whose evaluation vectors are orthogonal therefore satisfies
\[
\frac{d_\alpha(t)}{\sqrt\alpha}=\frac{\pi}{2\sqrt t}+\frac{\pi^3}{64t^{5/2}}+O(t^{-9/2}).
\]
In particular, orthogonal normalized evaluation vectors can occur at arbitrarily small Euclidean separation, even though the holomorphic Fock kernel \(e^{\langle z,w\rangle/\alpha}\) never vanishes.

## Assumptions and scope

The Gaussian measure is \((\pi\alpha)^{-n}e^{-\|z\|^2/\alpha}\,dV(z)\); all functions are complex-valued pluriharmonic and square integrable under this measure. The full-radius threshold is valid for every integer \(n\ge1\), with the standard Hermitian inner product. The angular and chord classifications concern the one-dimensional equal-radius circle; the phrase *least root* does not exclude additional zeros at larger angular separations when \(t\) is large. Each \(O(\cdot)\) is in the stated one-parameter limit with \(\alpha\) fixed; the dimension-free angular formulas use \(t=R^2/\alpha\).

## Proof

**Kernel normalization.** The orthogonal splitting of the pluriharmonic Fock space into the entire Fock space and the conjugate of the subspace of entire functions vanishing at zero yields \(K^{\mathrm{ph}}_\alpha=K_\alpha+\overline{K_\alpha}-1\), with \(K_\alpha(z,w)=\exp(\langle z,w\rangle/\alpha)\). Thus evaluation-kernel orthogonality is exactly the displayed scalar equation.

**Sharp ball threshold.** Put \(u=\langle z,w\rangle/\alpha\) and \(r=R^2/\alpha\). Cauchy--Schwarz gives \(|u|\le r\). For \(0<r\le\log2<1\), the harmonic function \(u\mapsto\operatorname{Re}e^u\) has minimum over \(|u|\le r\) attained on its circumference. Parametrize \(u=re^{i\phi}\). Its derivative with respect to \(\phi\) is
\[
-r e^{r\cos\phi}\sin(\phi+r\sin\phi).
\]
For \(0<\phi<\pi\), \(0<\phi+r\sin\phi<\pi\), using \(\sin\phi<\pi-\phi\) and \(r<1\). Hence the boundary value is strictly decreasing on \([0,\pi]\), and even under \(\phi\mapsto-\phi\). Its unique minimum is \(e^{-r}\) at \(u=-r\). Therefore \(K^{\mathrm{ph}}_\alpha(z,w)\ge2e^{-r}-1\), positive for \(r<\log2\). Equality at \(r=\log2\) forces \(u=-r\), and equality in Cauchy--Schwarz forces maximal norms and \(w=-z\). Conversely, such antipodal pairs have kernel zero.

**Existence and simplicity of the first angle.** Define
\[
F(t,\theta)=2e^{t\cos\theta}\cos(t\sin\theta)-1,\qquad
q(t,\theta)=\theta+t\sin\theta.
\]
Then \(F(t,0)>0\), \(F(t,\pi)=2e^{-t}-1<0\) for \(t>\log2\), and
\[
\partial_\theta F=-2t e^{t\cos\theta}\sin q.
\]
For \(\log2<t\le1\), \(0<q<\pi\) whenever \(0<\theta<\pi\), so \(F\) is strictly decreasing and has one simple zero. For \(1<t<\pi/2\), the function \(q\) increases through \(\pi\) once and then stays between \(\pi\) and \(2\pi\) until its endpoint value \(\pi\). Thus \(F\) decreases to one interior minimum and subsequently increases. Since \(F(t,\pi)<0\), the minimum is negative, and its first zero is before that minimum and is simple. For \(t\ge\pi/2\), set \(\theta_0=\arcsin(\pi/(2t))\le\pi/2\). Then \(F(t,\theta_0)=-1\), while \(0<q<\pi\) on \((0,\theta_0)\). Hence \(F\) decreases strictly from positive to negative there, and the least zero is simple. The implicit function theorem gives a smooth \(\Theta(t)\).

**Strict motion.** Differentiation gives \(\partial_t F=2e^{t\cos\theta}\cos q\). At any least root we have \(0<q<\pi\). We also have \(q>\pi/2\): if \(\theta\ge\pi/2\) this is immediate; otherwise, if \(q(t,\theta)\le\pi/2\), then \(\partial_sF(s,\theta)\ge0\) for all \(0\le s\le t\), contradicting \(F(0,\theta)=1\) and \(F(t,\theta)=0\). Thus
\[
\Theta'(t)=\frac{\cos(q(t,\Theta(t)))}{t\sin(q(t,\Theta(t)))}<0.
\]

**Antipodal square-root onset.** The global threshold proves \(\Theta(t)\to\pi\) as \(t\downarrow\log2\). Put \(\xi=\pi-\Theta(t)\). In a neighborhood of the endpoint, the zero equation can be logged:
\[
0=\log2-t\cos\xi+\log\cos(t\sin\xi)
=\log2-t+\frac{t(1-t)}2\xi^2+O(\xi^4).
\]
Analyticity in \((t,\xi^2)\) and the nonzero coefficient \((\log2)(1-\log2)/2\) give \(\xi^2=2(t-\log2)/((\log2)(1-\log2))+O((t-\log2)^2)\), and the stated square-root expansion.

**Far-field inverse-radius law.** For \(t\ge\pi/2\), put \(y=t\sin\Theta(t)\). The first-root bracket gives \(0<y<\pi/2\) and \(\Theta(t)<\arcsin(\pi/(2t))\). Its defining equation is \(\cos y=\tfrac12 e^{-t\cos\Theta(t)}\), so
\[
\frac\pi2-y=\arcsin\!\left(\frac12e^{-t\cos\Theta(t)}\right)=O(e^{-t+O(1/t)}).
\]
Using \(\Theta(t)=\arcsin(y/t)\), the Taylor expansion of arcsine gives the displayed angular expansion. Finally,
\[
\frac{d_\alpha(t)}{\sqrt\alpha}=\sqrt{2t\left(1-\sqrt{1-y^2/t^2}\right)}
=\frac{y}{\sqrt t}+\frac{y^3}{8t^{5/2}}+O(t^{-9/2}),
\]
which yields the stated two-term chord expansion after substituting \(y=\pi/2+O(e^{-t})\).

## Verification

The analytical argument proves the global nonvanishing threshold, equality cases, least-root smoothness and monotonicity, and both asymptotic expansions. The included `check_first_orthogonality.py` (Python standard library only) evaluates fifteen parameter points, checks the scaled kernel equation and the phase inequality, checks monotonic ordering, and compares both limiting laws. Run `python check_first_orthogonality.py` in the directory containing this document and the code. Its finite calculations are supplementary and are not used as infinite-dimensional proofs.

## Relationship to prior work

Looi's 2026 work provides the pluriharmonic Gaussian reproducing kernel and Schatten estimates for positive Toeplitz operators; the kernel formula itself is not new. Fulsche (2019) also records the holomorphic/antiholomorphic splitting and discusses Toeplitz quantization. The present result optimizes the first orthogonality geometry of those kernels, including the exact contact radius and two asymptotic regimes, which are not asserted in the inspected source sections. The polyanalytic Fock kernels treated by Fulsche and Hagger (2024) have Laguerre-polynomial zeros depending on point difference; they are different kernels and exhibit a different zero geometry.

## Limitations

The angular classification concerns the *first* equal-radius zero in one complex dimension, not all later oscillatory zeros or a full classification for arbitrary radii and points in multiple dimensions. This is not a sampling theorem or a new global Toeplitz norm inequality. Historical coverage of the first-zero geometry outside the inspected primary texts cannot be ruled out; the scalar kernel formula was previously known. No independent audit has been performed.

## References

1. S. Looi, *Comparing positive Toeplitz operators on holomorphic and pluriharmonic Fock spaces*, arXiv:2608.13550 (first public version 2026-08-13), Sections 2, 3, 6. https://arxiv.org/abs/2608.13550
2. R. Fulsche, *Toeplitz operators on pluriharmonic function spaces: Deformation quantization and spectral theory*, arXiv:1901.02644 (2019), Sections 1–2 and spectral discussion. https://arxiv.org/abs/1901.02644
3. R. Fulsche and R. Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces*, J. Fourier Anal. Appl. 30 (2024), article 63, Section 3. https://doi.org/10.1007/s00041-024-10124-9
