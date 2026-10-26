# Exact small-target first-order resetting transition in a three-dimensional spherical shell

## Finding

For a shrinking inner absorbing sphere in a three-dimensional concentric spherical shell, the **inner first-order resetting transition** has the exact asymptotic location
\[
 x_{\mathrm{tr}}(c)=Zc^{1/3}+Kc+O(c^{4/3}),\quad
 Z=\left(\frac{2}{3e^2}\right)^{1/3},\quad
 K=\frac13+\frac{1}{9e^2}.
\]
At this starting radius there is coexistence of two **global** mean-first-passage minimizers: reset rate zero and a strictly positive rate with
\[
 s_{\mathrm{tr}}(c)=\frac{4}{Z^2}c^{-2/3}\bigl(1+O(c^{2/3})\bigr).
\]
Consequently, the exact exponents for this transition are \(1/3\) and \(-2/3\), and the leading constants are \(Z\approx0.448511165448\) and \(4/Z^2\approx19.884444974955\). They replace fitted effective exponents and prefactors, not previously proved asymptotic constants.

More generally, at any fixed \(z>0\) and \(x=zc^{1/3}\),
\[
 \lim_{c\downarrow0}\inf_{s\geq0} M_c(x,s)
 =\min\left\{\frac16,\frac{e^2z^3}{4}\right\}.
\]
If \(z<Z\), the unique optimum is strictly positive for sufficiently small \(c\), and \(c^{2/3}s_{\mathrm{opt}}\to4/z^2\). If \(z>Z\), the unique global optimum is \(s=0\) for sufficiently small \(c\). At \(z=Z\), the next-order shift above resolves the crossing; this is not a claim of an equal minimum at exactly \(x=Zc^{1/3}\) for each finite \(c\).

## Assumptions and scope

Diffusion has generator \(\Delta\) (physical diffusivity \(D=1\)); the outer sphere has radius \(1\), the inner sphere radius \(0<c<1\), and the Brownian particle starts at any radius \(c<x<1\). Absorption at **either** sphere terminates the search. An independent homogeneous Poisson clock with rate \(s\geq0\) instantaneously returns the surviving particle to its original starting point. \(M_c(x,s)\) denotes the mean completion time. Constants in \(O(\cdot)\) are uniform for the scaled radius \(z\) in compact positive neighborhoods of \(Z\). The result is about the inner transition as the inner sphere shrinks, not the separate outer transition or other ambient dimensions.

## Proof

**1. Exact finite-shell transform.** Let \(T\) denote absorption time without resets and \(u_c(x,s)=\mathbb E_x[e^{-sT}]\). The radial Dirichlet problem is
\[
 u''+\frac2x u'=su,\qquad u(c)=u(1)=1.
\]
Writing \(xu\) as a combination of hyperbolic sines gives, for \(s>0\) and \(a=\sqrt{s}\),
\[
 u_c(x,s)=\frac{c\sinh(a(1-x))+\sinh(a(x-c))}
 {x\sinh(a(1-c))}.
\]
The renewal identity for resetting to the starting point then gives
\[
 M_c(x,s)=\frac{1-u_c(x,s)}{s\,u_c(x,s)},\quad s>0.
\]
At \(s=0\), direct solution of \(\Delta m=-1\), \(m(c)=m(1)=0\), gives
\[
 M_c(x,0)=m_c(x)=\frac{1-x^2-c(1+c)(x^{-1}-1)}6.
\]
These expressions, not fitted data, define the optimization problem.

**2. The competing high-reset saddle.** Put \(\delta=c^{1/3}\), \(x=z\delta\), and \(h=x\sqrt s\); thus \(s=h^2/(z^2\delta^2)\). For positive \(z,h\) in compact sets, the outer-boundary contribution to the transform is exponentially small in \(1/\delta\). The inner-boundary contribution yields the uniform expansions, including derivatives in \(z,h\),
\[
 u_c=\frac{\delta^2}{z}e^{-h}\left[1+\frac{h\delta^2}{z}+O(\delta^4)\right]
 +O\bigl(e^{-\eta/\delta}\bigr),
\]
\[
 M_c(z\delta,h^2/(z^2\delta^2))
 =\underbrace{\frac{z^3e^h}{h^2}}_{F(z,h)}
 +\delta^2\left(-\frac{z^2e^h}{h}-\frac{z^2}{h^2}\right)+O(\delta^4),
\]
and
\[
 m_c(z\delta)=\frac16-\frac{\delta^2}{6}(z^2+z^{-1})+O(\delta^3).
\]
For each \(z>0\), \(F(z,h)\) has one global minimum at \(h=2\), with \(F(z,2)=e^2z^3/4\) and \(\partial_{hh}F(z,2)=e^2z^3/8>0\). Its crossing with the no-reset limit \(1/6\) occurs exactly when \(z=Z=(2/(3e^2))^{1/3}\).

**3. No unseen global competitor.** We justify why the two branches above, rather than merely stationary points, are the global minimizers. Consider arbitrary sequences \(c_n\downarrow0\), \(z_n\to z\in(0,\infty)\), \(s_n>0\). If \(s_n\) stays in a finite positive interval, then \(u_{c_n}\to\sqrt{s}/\sinh\sqrt{s}\) and
\[
 M_{c_n}(z_nc_n^{1/3},s_n)\longrightarrow
 \frac{\sinh\sqrt{s}-\sqrt{s}}{s^{3/2}}>\frac16.
\]
For \(s_n\to0\), the derivative of this last expression at zero is \(1/120>0\); uniform convergence of the first two moment derivatives of the finite-shell transform therefore implies \(M_{c_n}(x,s)>M_{c_n}(x,0)\) on a fixed small interval of rates (for sufficiently small \(c_n\)). If \(s_n\to\infty\), set \(h_n=z_nc_n^{1/3}\sqrt{s_n}\). When \(h_n\) remains in a compact subset of \((0,\infty)\), the limit is \(F(z,h)\). When \(h_n\to0\) or \(h_n\to\infty\), the mean tends to infinity: the explicit transform and \(x=z\delta\) give the bound
\[
 s\,u_c(x,s)\le C\left(\frac{h^2}{z^3}e^{-h/2}+a^3e^{-a/2}\right)
\]
for sufficiently small \(c\), with \(a=\sqrt s\to\infty\), and \(u_c\to0\). This bound tends to zero at both excluded ends. Hence all globally minimizing positive-rate sequences must lie near \(h=2\) whenever that branch can compete with zero. Strict local convexity in \(h\) there, together with the uniform convergence of derivatives, gives its uniqueness. The zero-rate branch is separated from every positive competitor except this high-rate minimum. Thus the limiting optimized mean is the minimum of the two claimed values, with the stated strict regions for \(z<Z\) and \(z>Z\).

**4. The coexistence curve and its correction.** Near \((z,h)=(Z,2)\), solve the simultaneous equations
\[
 M_c(z\delta,h^2/(z^2\delta^2))-m_c(z\delta)=0,
 \qquad \partial_h M_c(z\delta,h^2/(z^2\delta^2))=0.
\]
At \(\delta=0\), the Jacobian of these equations with respect to \((z,h)\) is triangular with nonzero diagonal entries \(3e^2Z^2/4\) and \(e^2Z^3/8=1/12\). The implicit-function theorem, using the exponentially accurate smooth extension of the two equations, yields the unique nearby coexistence branch. Expanding the first equation through \(\delta^2\) gives
\[
 z_{\mathrm{tr}}(c)=Z+\left(\frac13+\frac{1}{9e^2}\right)\delta^2+O(\delta^3).
\]
The second gives \(h_{\mathrm{tr}}=2+3Z^2(e^2-1)\delta^2+O(\delta^3)\). Consequently \(x_{\mathrm{tr}}=z_{\mathrm{tr}}\delta\) and \(s_{\mathrm{tr}}=h_{\mathrm{tr}}^2/(z_{\mathrm{tr}}^2\delta^2)\) have the displayed asymptotic laws. Step 3 guarantees that the equal-valued branches here are actual **global** minima. Their strict ordering switches on passing through this curve, proving it is a first-order transition rather than just a metastable stationary-point crossing.

## Verification

The standalone `check.py` reconstructs the finite-shell Laplace transform with stable exponentials, locates the inner coexistence point by nested bounded minimization and bisection for shrinking \(c\), checks its observed convergence to the exact constants, uses the exact no-reset mean, and checks algebraic identities for the limiting saddle and correction coefficient. `checks.txt` records a successful run. Computation corroborates the formula but is not substituted for the uniform asymptotic and global-minimum arguments in the proof.

## Relationship to prior work

Chen and Huang (arXiv:2109.11101, publicly posted September 23, 2021), Section IV and Fig. 9, derive the mean time for this same three-dimensional two-absorber model and identify the inner discontinuous transition. They fit effective small-\(c\) laws of approximately \(0.532c^{0.352}\) for its position and \(29.59c^{-0.625}\) for the jump rate; they do not derive the exponents, limiting amplitudes, or second-order position correction proved here. The leading transform and resetting renewal formula are prior ingredients, not asserted as new. Pal and Prasad (arXiv:1812.03009) analyze interval resetting in one dimension; that setting does not imply the shrinking three-dimensional spherical-shell scaling. Other more general restart phase-transition theory supplies qualitative mechanisms, but no inspected result was found that explicitly entails the inner-radius asymptotics here.

## Limitations

Only the small-inner-radius \(c\downarrow0\) regime with a concentric *three-dimensional*, doubly absorbing shell and constant-rate Poisson resetting is proved. The result does not classify the full transition diagram for finite \(c\), higher dimensions, other boundary conditions, or random reset positions. The analysis is independent mathematical derivation with numerical checks, not an independently audited theorem; scholarly priority beyond the inspected literature remains open.

## References

- H. Chen and F. Huang, “First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry,” arXiv:2109.11101 (first public posting September 23, 2021), *Physical Review E* 105, 034109 (2022). https://arxiv.org/html/2109.11101v2 ; https://doi.org/10.1103/PhysRevE.105.034109 . Relevant Section IV, equations (29) and Fig. 9.
- A. Pal and V. V. Prasad, “First passage under stochastic resetting in an interval,” arXiv:1812.03009 (2018). https://arxiv.org/html/1812.03009v2 .
