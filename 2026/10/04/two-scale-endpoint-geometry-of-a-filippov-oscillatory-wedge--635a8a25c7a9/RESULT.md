# Two-scale endpoint geometry of a Filippov oscillatory wedge
## Finding
For the symmetric zero-divergence three-dimensional piecewise-linear Filippov class in arXiv:2609.33034, let \(t_g(\mu)\in(\pi,2\pi)\) solve
\[
\cos t_g-\mu\sin t_g=e^{-\mu t_g},
\]
and let
\[
H_g(\mu)=e^{-2\mu t_g(\mu)},\qquad H_{\mathrm{crit}}(\mu)=\frac{1}{2\cosh(\pi\mu)-1}.
\]
The source identifies \(H_g(\mu)<H<H_{\mathrm{crit}}(\mu)\) as the simple-period oscillatory interval. Its endpoint geometry satisfies, as \(\mu\to0^+\),
\[
t_g(\mu)=2\pi-2\sqrt{\pi}\,\mu^{1/2}+O(\mu^{3/2}),
\]
\[
H_g(\mu)=1-4\pi\mu+4\sqrt{\pi}\,\mu^{3/2}+O(\mu^2),
\]
\[
H_{\mathrm{crit}}(\mu)-H_g(\mu)=4\pi\mu-4\sqrt{\pi}\,\mu^{3/2}+O(\mu^2).
\]
For \(\mu\to\infty\), put \(q=e^{-\pi\mu}\). Then
\[
t_g(\mu)=\pi+\mu^{-1}-\frac{1}{3\mu^3}+O(\mu^{-5}+q/\mu),
\]
\[
H_g(\mu)=e^{-2}q^2\left(1+\frac{2}{3\mu^2}+O(\mu^{-4}+q)\right),\qquad H_{\mathrm{crit}}(\mu)=q+q^2+O(q^3),
\]
and therefore
\[
H_{\mathrm{crit}}(\mu)-H_g(\mu)=q+(1-e^{-2})q^2+O(q^2/\mu^2+q^3),
\]
\[
\frac{H_g(\mu)}{H_{\mathrm{crit}}(\mu)}=e^{-2}q\left(1+\frac{2}{3\mu^2}+O(\mu^{-4}+q)\right).
\]
Thus the large-\(\mu\) absolute coalescence of the two boundary curves hides a two-scale structure: the upper boundary has exponential rate \(\pi\), while the grazing boundary has rate \(2\pi\), with prefactor \(e^{-2}\).

## Assumptions and scope
The statement uses exactly the normalized symmetric zero-divergence class and the boundary definitions in Theorem 1 of arXiv:2609.33034, with \(\mu>0\). It concerns parameter-space boundaries, not the amplitude or Floquet multipliers of a fixed interior cycle. It makes no assertion for nonsymmetric perturbations or nonzero-divergence systems.

## Proof
Set \(F(\mu,t)=\cos t-\mu\sin t-e^{-\mu t}\). The source proves that \(F(\mu,t_g)=0\) has a unique root \(t_g\in(\pi,2\pi)\).

For \(\mu\to0^+\), put \(s=\sqrt{\mu}\) and \(2\pi-t_g=su\). The root equation becomes
\[
\cos(su)+s^2\sin(su)-e^{-2\pi s^2+s^3u}=0.
\]
After division by \(s^2\), the continuous extension at \(s=0\) has leading equation \(2\pi-u^2/2=0\). Its positive root \(u=2\sqrt{\pi}\) is simple. The implicit-function theorem and one further Taylor step give
\[
u(s)=2\sqrt{\pi}-\frac{2}{3}\pi^{3/2}s^2+O(s^3),
\]
which implies the stated expansion of \(t_g\). Then
\[
-2\mu t_g=-4\pi\mu+4\sqrt{\pi}\,\mu^{3/2}+O(\mu^{5/2}),
\]
so exponentiation gives the expansion of \(H_g\). Also
\[
H_{\mathrm{crit}}=(2\cosh(\pi\mu)-1)^{-1}=1-\pi^2\mu^2+O(\mu^4),
\]
and subtraction gives the small-\(\mu\) width.

For \(\mu\to\infty\), define \(t_0=\pi+\arctan(\mu^{-1})\) and write \(t_g=t_0+h\). The trigonometric part has the exact phase form
\[
\cos(t_0+h)-\mu\sin(t_0+h)=\sqrt{1+\mu^2}\,\sin h.
\]
The unique root lies before \(h=\pi/2\) for all sufficiently large \(\mu\), because the defining function is negative at \(h=0\) and positive at \(h=\pi/2\). Hence
\[
\sqrt{1+\mu^2}\,\sin h=e^{-\mu t_0}e^{-\mu h}.
\]
Using \(\sin h\ge 2h/\pi\) on \([0,\pi/2]\) gives \(h=O(e^{-\mu t_0}/\mu)=O(q/\mu)\). Since
\[
\arctan(\mu^{-1})=\mu^{-1}-\frac{1}{3\mu^3}+O(\mu^{-5}),
\]
the claimed expansion of \(t_g\) follows. Hence
\[
-2\mu t_g=-2\pi\mu-2+\frac{2}{3\mu^2}+O(\mu^{-4}+q),
\]
which gives the expansion of \(H_g\). Finally
\[
H_{\mathrm{crit}}=\frac{q}{1-q+q^2}=q+q^2+O(q^3).
\]
Subtraction and division yield the final two formulas.

## Verification
The argument uses only the source's exact boundary equations, Taylor expansion, the implicit-function theorem at a simple rescaled root, and a mean-value estimate. Numerical experiments are not used as proof. The formulas recover the source's endpoint limits and respect its bound \(0<H_g<e^{-2\pi\mu}\).

## Relationship to prior work
The full text of arXiv:2609.33034 defines \(t_g\), \(H_g\), and \(H_{\mathrm{crit}}\), identifies the lower curve with grazing and the upper curve with the infinite-amplitude boundary, and in Proposition 16 proves only that both tend to \(1\) as \(\mu\to0^+\) and to \(0\) as \(\mu\to\infty\). It does not state rates or the large-\(\mu\) boundary ratio.

The closest accessible earlier full-text comparison, arXiv:2010.03018, studies planar two-zone piecewise-linear systems and weak-focus bifurcation at infinity, not this three-dimensional visible-visible two-fold boundary pair. A 2020 paper on symmetric three-dimensional continuous piecewise-linear systems uses a continuous three-zone geometry; its accessible abstract reports period and amplitude formulas but not the present boundary pair.

## Limitations
This is an asymptotic refinement of an explicit parameter region, not a new existence or stability theorem. It does not give cycle-amplitude or Floquet-multiplier boundary asymptotics. A reliable full-text copy of the 2020 continuous three-zone comparison was not obtained during the literature check, so an equivalent hidden formulation there remains a residual risk, although the switching geometry and parameters differ.

## References
1. S. C. S. Ferreira, *Global classification of oscillatory dynamics in symmetric zero-divergence 3D piecewise-linear Filippov systems with a visible-visible two-fold*, arXiv:2609.33034. First public 2026-09-27; Theorem 1 and Section 6, Proposition 16.
2. E. Freire, E. Ponce, J. Torregrosa, F. Torres, *Limit cycles from a monodromic infinity in planar piecewise linear systems*, arXiv:2010.03018.
3. E. Freire, E. Ponce, F. J. Ros, E. Vela, A. Amador, *Hopf bifurcation at infinity in 3D symmetric piecewise linear systems. Application to a Bonhoeffer-van der Pol oscillator*, Nonlinear Analysis: Real World Applications 54 (2020), 103112, DOI:10.1016/j.nonrwa.2020.103112.
