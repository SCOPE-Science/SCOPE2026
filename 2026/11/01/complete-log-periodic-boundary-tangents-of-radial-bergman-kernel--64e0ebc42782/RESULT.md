# Complete log-periodic boundary tangents of radial Bergman kernels

## Finding

Fix \(\alpha>-1\), and let \(h:\mathbb R\to(0,\infty)\) be a positive continuous periodic function. Let \(K_h(z,w)\) be the reproducing kernel for the analytic subspace of \(L^2(\mathbb D,W_h\,dA/\pi)\), with
\[
W_h(z)=(1-|z|^2)^\alpha h\!\left(\log\frac1{1-|z|^2}\right).
\]
Put \(p=\alpha+2\), and define positive functions
\[
A(x)=\int_0^\infty e^{-v}v^\alpha h(x-\log v)\,dv,
\qquad Q(x)=\frac1{A(x)},
\]
\[
H_\theta(\zeta)=\int_0^\infty e^{-\zeta t}t^{\alpha+1}
 Q(\theta+\log t)\,dt,\qquad \operatorname{Re}\zeta>0.
\]
For the scalar kernel \(\mathcal K_h(s)=\sum_{n\ge0}s^n/m_n\), where \(K_h(z,w)=\mathcal K_h(z\overline w)\), the **uniform phase law** is
\[
N^{-p}\mathcal K_h(e^{-\zeta/N})
 =H_{\log N}(\zeta)+o(1),\qquad N\longrightarrow\infty,
\]
locally uniformly on the right half-plane. The phase is read modulo any period of \(h\). Equivalently, for \(u,v\) in the right half-plane, the two-variable reproducing kernels at \(z=e^{-u/(2N)}\), \(w=e^{-v/(2N)}\) converge after division by \(N^p\) to \(H_\theta((u+\overline v)/2)\) along a phase-\(\theta\) subsequence. These limiting kernels are positive definite because their Laplace densities are positive.

If \(h\) is nonconstant and \(T>0\) is its least positive period, the complete subsequential limit set of the rescaled kernels is exactly the circle
\[
\{H_\theta:\theta\in\mathbb R/T\mathbb Z\}.
\]
Every member is attained by an integer sequence \(N_j\to\infty\). More strongly, the positive scalar-normalized functions
\[
\frac{\mathcal K_h(e^{-\zeta/N})}{\mathcal K_h(e^{-1/N})}
\]
have precisely the circle of limit functions \(H_\theta(\zeta)/H_\theta(1)\), and **distinct phases yield distinct normalized analytic functions**. Even the diagonal scalar \(N^{-p}\mathcal K_h(e^{-1/N})\) has no ordinary limit: its cluster set is the nondegenerate interval \(\{H_\theta(1):0\le\theta\le T\}\).

Conversely, when \(h\) is constant, the unique scaling limit is \((\alpha+1)h^{-1}\zeta^{-p}\), and every normalized limit equals \(\zeta^{-p}\). Thus, among positive continuous periodic profiles, **unique boundary tangency holds if and only if the profile is constant**, despite every such weight satisfying the usual radial moment-doubling assumption.

## Assumptions and scope

Normalized planar area means \(dA/\pi\). The weight is not assumed smooth at the unit circle; it is strictly positive within the disk and comparable, above and below by fixed positive constants, to \((1-|z|^2)^\alpha\). Monomials constitute an orthogonal complete system. The exact positive monomial moments and scalar reproducing kernel are
\[
m_n=\int_0^1 u^n(1-u)^\alpha h\!\left(\log\frac1{1-u}\right)du,
\qquad \mathcal K_h(s)=\sum_{n=0}^\infty\frac{s^n}{m_n},\quad |s|<1.
\]
All limits concern integer \(N\to\infty\), complex \(\zeta\) with \(\operatorname{Re}\zeta>0\), and fixed \(\alpha\) and \(h\). The source's one-sided moment-doubling hypothesis holds because of comparability with the standard power weight. These are kernel-level statements, not assertions about zero sets or boundary pointwise traces of arbitrary analytic functions.

## Proof

**1. Uniform Mellin–Laplace moment asymptotics.** Put \(v=N(1-u)\) with an integer \(N\ge1\). Then
\[
N^{\alpha+1}m_N=\int_0^N v^\alpha(1-v/N)^N
h(\log N-\log v)\,dv.
\]
Since \(0\le(1-v/N)^N\mathbf1_{v<N}\le e^{-v}\), the absolute difference from \(A(\log N)\) is bounded by
\[
\|h\|_\infty\left[\Gamma(\alpha+1)-N^{\alpha+1}B(N+1,\alpha+1)\right]
=O_{\alpha,h}(N^{-1}).
\]
The last equality follows directly from the fixed-shift gamma-ratio expansion. Positivity of \(h\) gives \(0<c\le A(x)\le C<\infty\). Consequently,
\[
\frac1{m_N}=\frac{N^{\alpha+1}}{A(\log N)}+O_{\alpha,h}(N^\alpha).
\]
For the displayed scalar kernel, the \(N=0\) coefficient is a harmless fixed constant.

**2. Complete phase-dependent scaling.** Insert the reciprocal-moment estimate into the power series with \(s=e^{-\zeta/N}\). On each compact set \(\operatorname{Re}\zeta\ge\delta>0\), the cumulative error in the scaled sum is \(O(N^{-1})\), because \(\sum_{n\ge1}n^\alpha e^{-\delta n/N}=O(N^{\alpha+1})\). The main term becomes
\[
\frac1N\sum_{n\ge1}\left(\frac nN\right)^{\alpha+1}
 e^{-\zeta n/N}\,Q\!\left(\log N+\log\frac nN\right).
\]
This is a Riemann sum for \(H_{\log N}(\zeta)\), **uniformly in the phase**: on any compact \(t\)-interval away from zero, \(Q\) is uniformly continuous and periodic; the ranges near zero and infinity are bounded uniformly by integrable multiples of \(t^{\alpha+1}\) and \(t^{\alpha+1}e^{-\delta t}\). These estimates also give local uniformity in complex \(\zeta\) and justify the analytic limit.

**3. The Mellin smoothing preserves all periods.** Let \(\omega=2\pi/T\) and denote Fourier coefficients of a continuous \(T\)-periodic function by hats. Fubini's theorem yields
\[
\widehat A(k)=\widehat h(k)\Gamma(\alpha+1-ik\omega),\qquad k\in\mathbb Z.
\]
Euler's gamma function has no zeros. A real shift is a period of \(A\) exactly when it is a period of \(h\), by uniqueness of Fourier coefficients. Hence a nonconstant \(h\) and its smoothed profile \(A\) have the same least period \(T\); so does \(Q=1/A\).

**4. Exhaustion of all phases and genuine diagonal oscillation.** Every sequence of phases \(\log N\bmod T\) has a convergent subsequence by compactness. Conversely, for any \(\theta\in[0,T)\), choosing \(N_j=\lfloor e^{\theta+jT}\rfloor\) gives \(\log N_j\bmod T\to\theta\). Continuity of the phase family in the compact-open topology proves the claimed complete limit set.

For \(D(\theta)=H_\theta(1)\), the Fourier coefficients satisfy
\[
\widehat D(k)=\widehat Q(k)\Gamma(\alpha+2+ik\omega).
\]
The gamma factor again never vanishes. Therefore \(D\) has the same periods as nonconstant \(Q\), and is nonconstant. Since \(D\) is positive and continuous on a circle, the entire nondegenerate interval between its minimum and maximum is attained as the diagonal cluster set.

**5. Scalar normalization cannot erase the phase.** If two normalized analytic limits coincide on \(\operatorname{Re}\zeta>0\), uniqueness of Laplace transforms of locally integrable functions of exponential order implies
\[
\frac{Q(\theta+\log t)}{H_\theta(1)}
=\frac{Q(\psi+\log t)}{H_\psi(1)}\quad(t>0).
\]
Both sides are continuous. Their proportionality constant is one: integrate the corresponding periodic functions \(Q\) over a complete log-period. Thus \(Q(x+\theta)=Q(x+\psi)\) for all real \(x\), and minimality of \(T\) forces \(\theta=\psi\pmod T\). The normalized map is a continuous injection from a compact circle into the Hausdorff space of analytic functions; it is therefore a homeomorphism onto its image. If \(h\) is constant, evaluating the two elementary gamma integrals gives the stated single limit.

For clarity, the tangent functions also obey the discrete-scale covariance
\[
H_\theta(b\zeta)=b^{-p}H_{\theta-\log b}(\zeta),\qquad b>0.
\]
It follows directly by substituting \(u=bt\) in the defining integral.

## Verification

An independently executable finite arithmetic and quadrature check accompanies this manuscript as `verify.py`, with its single numerical dependency stated in `requirements.txt`. It compares exact beta-function moments with the Mellin-phase asymptotic, compares finite scalar kernels with their predicted phase integrals, and checks the gamma/Fourier identity for a sinusoidal profile. Numerical checks are **not** used to establish the uniform-in-phase theorem, Laplace uniqueness, or the all-periods assertion; those follow from the proof above.

For the illustrative profile \(h(x)=1+\varepsilon\cos(\omega x)\), \(0<\varepsilon<1\), \(\omega>0\), one has exactly
\[
A(x)=\Gamma(\alpha+1)+\varepsilon\operatorname{Re}
\!\left(\Gamma(\alpha+1-i\omega)e^{i\omega x}\right).
\]
This explicit example already produces the full circle of inequivalent normalized tangents. The general theorem applies to every positive continuous periodic profile, including nontrigonometric functions.

## Relationship to prior work

Pennanen, Rättyä, Wang and Wu (first public version 2026-07-22) prove sharp off-diagonal upper estimates **equivalent** to the one-sided radial moment-doubling property. All weights here satisfy that property, but their two-sided scale comparisons do not determine a unique rescaled boundary kernel. The present exact, complete and projectively injective phase-limit classification addresses information not given by those upper bounds.

Blaschke's 2012 paper derives boundary expansions for radial **power-logarithmic** weights and certain asymptotic power-log series. Such profiles differ from persistent periodic oscillations in the logarithm of boundary distance, which have no single slowly varying asymptotic coefficient. Zeytuncu's 2010 paper studies radial weights comparable to one, their projection boundedness and kernel zeros, but not the log-periodic boundary tangent family. The Fourier/Laplace steps use classical gamma and Abelian ideas; no novelty is claimed for those general-purpose tools in isolation.

## Limitations

The result gives no universal limit for nonconstant profiles; it classifies the whole limit family instead. It does not classify zeros of the limiting kernels, nor assert a general result for nonperiodic or discontinuous oscillations, nonradial weights or higher-dimensional domains. The proof is self-contained for continuous periodic profiles. The comparison with earlier literature supports a distinct theorem but cannot exclude all implicit equivalents in older abstract Mellin–Tauberian theory; independent historical-priority review has not been performed.

## References

1. A. Pennanen, J. Rättyä, S. Wang and F. Wu, *Optimal off-diagonal upper estimates for Bergman reproducing kernels*, arXiv:2607.19959, first posted 2026-07-22, https://arxiv.org/abs/2607.19959. Theorem 1, equation (1.2), and Sections 2–4.
2. P. Blaschke, *Asymptotic behavior of Bergman kernels with logarithmic weight*, J. Math. Anal. Appl. **385** (2012), 293–302, DOI:10.1016/j.jmaa.2011.06.044, Theorems 1–2 and Section 3.
3. Y. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806, 2010, https://arxiv.org/abs/1009.2806, Sections 1–3.
4. P. Flajolet and A. Odlyzko, *Singularity Analysis of Generating Functions*, SIAM J. Discrete Math. **3** (1990), 216–240, DOI:10.1137/0403019 (background asymptotic methodology; not a claimed source of the phase-family theorem).
