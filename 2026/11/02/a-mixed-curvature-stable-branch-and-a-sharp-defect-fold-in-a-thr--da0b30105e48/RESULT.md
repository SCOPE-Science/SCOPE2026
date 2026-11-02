# A mixed-curvature stable branch and a sharp defect fold in a three-body oscillator ring

## Finding

For every integer \(N\geq3\) and coupling \(K>0\), consider the nearest-neighbor three-body phase ring
\[
\dot\theta_i=\omega_i+K\sin(\theta_{i+1}-2\theta_i+\theta_{i-1}),\qquad i\in\mathbb Z/N\mathbb Z.
\]
A frequency-locked solution means \(\theta_i(s)=\Omega s+\phi_i\) modulo \(2\pi\), and its *orbital exponential stability* means all linearized eigenvalues except the unavoidable common-rotation eigenvalue have strictly negative real part.

**Theorem (complete local stability test and one-defect fold).** For any locked state, write \(q_i=\phi_{i+1}-2\phi_i+\phi_{i-1}\) and \(c_i=\cos q_i\). This state is orbitally exponentially stable if and only if exactly one of the following holds:

1. Every \(c_i>0\).
2. Exactly one \(c_i=0\), and all the other coefficients are strictly positive.
3. Exactly one coefficient \(c_j<0\), all remaining ones are strictly positive, and
   \[
   -c_j<\left(\sum_{i\neq j}\frac{1}{c_i}\right)^{-1}.
   \]

In particular, a stable locked solution may have one *negative* local cosine. If precisely one coefficient is negative and equality holds in the displayed condition, there is an additional zero eigenvalue; if the inequality reverses strictly, there is exactly one positive eigenvalue. Configurations with at least two nonpositive coefficients are never orbitally exponentially stable.

For the natural one-impurity family \(\omega_1=0\), \(\omega_2=\cdots=\omega_N=\Delta\), let \(n=N-1\), and define
\[
F_n(t)=\sin(nt)+\sin t,\qquad 0<t<\pi/n.
\]
For each \(t\) there is a locked state with \(q_1=nt\), \(q_2=\cdots=q_N=-t\), forcing contrast \(\Delta=K F_n(t)\), and collective speed \(\Omega=K\sin(nt)\). The function \(F_n\) has a unique maximum at \(t_*=t_*(n)\in(\pi/(2n),\pi/n)\), determined by
\[
 n\cos(nt_*)+\cos t_*=0.
\]
All these states are orbitally exponentially stable for \(0<t<t_*\), have precisely one positive transverse eigenvalue for \(t_*<t<\pi/n\), and have one extra zero eigenvalue at \(t=t_*\). The fold is nondegenerate. Write \(\Delta_*(N)=K F_n(t_*)\). For every
\[
K\sin(\pi/n)<\Delta<\Delta_*(N)
\]
there are exactly two states **within this specified one-parameter curvature family**, one stable and one with a one-dimensional unstable direction. In particular, on the open forcing window
\[
K\bigl[1+\sin(\pi/(2n))\bigr]<\Delta<\Delta_*(N)
\]
the stable state has \(\cos q_1<0\), so it lies beyond the all-principal-arcsine stability regime. This nonempty window has the sharp large-ring width
\[
\Delta_*(N)-K\bigl[1+\sin(\pi/(2n))\bigr]
=\frac{K}{2n^2}+O(Kn^{-3})\quad(n\to\infty).
\]
No claim is made that \(\Delta_*(N)\) is a global locking threshold among *all* curvature branches.

## Assumptions and scope

Indices are cyclic, \(N\ge3\), \(K>0\), and phases are elements of the circle. Curvatures in the explicit family are real representatives with sum zero, so they come from a real phase vector modulo common rotation. Exponential stability is always transverse to common phase rotation; at the fold an additional neutral mode precludes such stability. The forcing contrast \(\Delta\) is a *one-impurity frequency difference*, not the width of an independently sampled random-frequency distribution.

## Proof

**1. Spectral reduction.** Let \(L\) be the cyclic second-difference matrix, \((Lx)_i=x_{i-1}-2x_i+x_{i+1}\); let \(H=-L\), a symmetric positive-semidefinite matrix with kernel \(\operatorname{span}\{\mathbf 1\}\). The Jacobian at a locked solution is \(J=K\operatorname{diag}(c_i)L=-KDH\). The nonzero eigenvalues of \(DH\) coincide, counting algebraic multiplicity, with those of the symmetric matrix \(H^{1/2}DH^{1/2}\) (the \(AB/BA\) principle). Consequently all nonzero eigenvalues of \(J\) are real. On the mean-zero space \(V=\{x:\sum_i x_i=0\}\), \(H^{1/2}\) is invertible. Sylvester's inertia law therefore identifies the signs of nontrivial eigenvalues of \(-J\) with the inertia of the quadratic form \(Q(x)=\sum_i c_i x_i^2\) on \(V\). Thus transverse exponential stability is equivalent to \(Q(x)>0\) for every nonzero \(x\in V\).

**2. Exhaustive sign classification.** Positive coefficients make \(Q\) positive. With exactly one zero and the rest positive, a nonzero mean-zero vector cannot be supported on the sole zero coordinate, so \(Q\) is still positive. With two nonpositive coefficients, a vector supported on these two with entries \(1\) and \(-1\) has nonpositive \(Q\), excluding positive definiteness. Finally suppose exactly one coefficient \(c_j<0\) and all others are positive. Fix \(x_j=s\); the mean-zero constraint gives \(\sum_{i\ne j}x_i=-s\). Weighted Cauchy–Schwarz gives
\[
\sum_{i\ne j}c_i x_i^2\ge \frac{s^2}{\sum_{i\ne j}c_i^{-1}},
\]
with equality at \(x_i=-s/(c_i\sum_{k\ne j}c_k^{-1})\). Hence \(Q\) is positive definite precisely under the strict inequality in the theorem. Equality yields a one-dimensional null direction; strict reversal yields precisely one negative direction for \(Q\), hence precisely one unstable eigenvalue for \(J\). These cases exhaust all possible signs, including zeros.

**3. Exact impurity branch and realization.** For every \(t\in(0,\pi/n)\), the vector \(q=(nt,-t,\ldots,-t)\) sums to zero. Since \(L\) is invertible on \(V\), there exists \(\phi\) with \(L\phi=q\), unique modulo common shifts. At site one, \(\Omega=K\sin(nt)\); at the other sites, \(\Omega=\Delta-K\sin t\). These agree if and only if \(\Delta=K F_n(t)\). This establishes an actual locked configuration for every point on the branch, not merely a formal force-balance equation.

**4. Unique fold, exact stability, and two-state interval.** On \((0,\pi/n)\),
\[
F_n''(t)=-n^2\sin(nt)-\sin t<0.
\]
Moreover \(F_n'(\pi/(2n))=\cos(\pi/(2n))>0\) and \(F_n'(\pi/n)=-n+\cos(\pi/n)<0\). Thus a unique \(t_*\) exists where \(F_n'=0\), and \(F_n\) is strictly increasing then strictly decreasing. As \(F_n(0)=0\) and \(F_n(\pi/n)=\sin(\pi/n)\), every forcing between \(K\sin(\pi/n)\) and \(K F_n(t_*)\) has exactly two parameter values in the stated open branch. On this branch \(c_1=\cos(nt)\), \(c_i=\cos t>0\) for \(i\ne1\). When \(c_1<0\), the criterion from step 2 reduces to
\[
\cos(nt)+\frac{\cos t}{n}>0\quad\Longleftrightarrow\quad F_n'(t)>0.
\]
For \(c_1\ge0\), the stability criterion is also satisfied, including equality \(c_1=0\). Thus the full stability claim follows. At \(t_*\), the zero of the restricted quadratic form is simple, and \(F_n''(t_*)<0\) gives a nondegenerate saddle-node in the quotient by phase rotation. The stable branch's one-negative-cosine portion starts at \(t=\pi/(2n)\), where \(F_n=1+\sin(\pi/(2n))\), and continues to \(t_*\).

**5. Width of the mixed-curvature window.** Put \(x_*=nt_*\). The fold equation becomes \(n\cos x_*+\cos(x_*/n)=0\). Taylor expansion at \(x_*=\pi/2\) gives \(x_*=\pi/2+n^{-1}+O(n^{-3})\). Consequently
\[
F_n(t_*)=1+\frac{\pi}{2n}+\frac{1}{2n^2}+O(n^{-3}),\qquad
1+\sin(\pi/(2n))=1+\frac{\pi}{2n}+O(n^{-3}).
\]
Subtracting and multiplying by \(K\) yields the claimed sharp leading width.

## Verification

The bundled standalone `VERIFY.py` constructs the actual cyclic Jacobian and tests the sign classification against a symmetric mean-zero restriction for \(N=3,\ldots,15\), including random sign configurations and exact-zero samples. It independently solves the scalar fold equation, constructs actual phase vectors with the prescribed second differences, checks the force-balance residuals, and checks the predicted stable, unstable, and double-neutral spectra. These finite tests supplement, and do not replace, the universal analytic arguments above. Run `python VERIFY.py` with NumPy and SciPy installed.

## Relationship to prior work

Liang, Zhu, Li, Dai, Li, and Yang introduced this exact pure three-body nearest-neighbor ring in arXiv:2512.18983v1 (first posted 2025-12-22). Their main text states both sine-inverse possibilities but develops the principal-branch quantization and the uniform-cosine stability calculation. The present result makes a distinct assertion: one locally negative cosine can be stable; the complete linear-stability sign test and a nondegenerate one-defect fold with an asymptotically sharp parameter window follow. The motivating article's separately mentioned supplemental material was not available for full comparison, leaving a genuine priority risk.

The signed-network definiteness theory of Song, Hill, and Liu (arXiv:1906.07632, 2019) provides broader precedent for effective-resistance and signed-form arguments. No general claim of discovering the constrained quadratic-form test is made. The mathematical contribution is its complete application to this specific triadic ring and, especially, the explicit mixed-branch existence, stability, bifurcation, and width. Bick, Böhle, and Kuehn (SIAM J. Appl. Dyn. Syst. 22, 2023, DOI:10.1137/22M1500940) study a different nonlocal higher-order model in the infinite-particle setting, not this one-impurity local ring.

## Limitations

The assertion is local orbital exponential stability, not global attraction, basin size, or noise tolerance. The explicit fold enumerates only the \(q=(nt,-t,\ldots,-t)\) branch; other curvature branches and winding sectors may contain other locks. At equality, nonhyperbolicity does not alone determine nonlinear stability. The general test is conditional on an existing locked state and does not classify existence for arbitrary frequencies. Historical priority against unpublished or inaccessible supplemental results remains provisional.

## References

1. J. Liang, S. Zhu, Y. Li, Q. Dai, H. Li, and J. Yang, “Quantized Frequency-locking and Extreme Transitions in a Ring of Phase Oscillators with Three-Body Interactions,” arXiv:2512.18983v1, first posted 2025-12-22, https://arxiv.org/html/2512.18983v1.
2. Y. Song, D. J. Hill, and T. Liu, “On Extension of Effective Resistance with Application to Graph Laplacian Definiteness and Power Network Stability,” arXiv:1906.07632, 2019, https://arxiv.org/abs/1906.07632.
3. C. Bick, T. Böhle, and C. Kuehn, “Phase Oscillator Networks with Nonlocal Higher-Order Interactions: Twisted States, Stability, and Bifurcations,” SIAM J. Appl. Dyn. Syst. 22 (2023), DOI:10.1137/22M1500940.
