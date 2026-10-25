# Sharp antipodal critical-window profile for spherical Fourier extension

## Finding
For every integer \(d\ge2\), the truncated critical radial–angular extension integral has an exact logarithmic leading coefficient, including a universal two-sided exponent crossover at distance \(O(1/\log R)\) from the critical exponent. The coefficient depends on input data through precisely two scalar invariants: total squared mass and real antipodal correlation. Its sharp maxima occur exactly at even or odd spherical data, with a dimension-dependent globally sharp parity-defect inequality.

Write \(p=d/(d-1)\), \(q_c=2p\), and for \(f\in L^2(S^{d-1})\) define
\[
A=\int_{S^{d-1}}|f(\omega)|^2\,d\sigma(\omega),\qquad
B=\int_{S^{d-1}}f(\omega)\overline{f(-\omega)}\,d\sigma(\omega).
\]
Here \(B\) is real, \(|B|\le A\), and \(d\sigma\) is unnormalized surface measure. For real \(\lambda\), set \(q_R=q_c+\lambda/\log R\) and
\[
T_R(f,\lambda)=\frac{1}{\log R}\int_1^R
\left(\int_{S^{d-1}}|Ef(r\theta)|^2\,d\sigma(\theta)\right)^{q_R/2}r^{d-1}\,dr,
\quad Ef(x)=\int_{S^{d-1}}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega).
\]
Then, uniformly as \(R\to\infty\) for \(\lambda\) in each bounded interval,
\[
\boxed{\lim_{R\to\infty}T_R(f,\lambda)=
\left(\frac{(2\pi)^d}{\pi}\right)^p
\left(\int_0^1e^{-(d-1)\lambda t/2}\,dt\right)
\frac{1}{2\pi}\int_0^{2\pi}(A+B\cos u)^p\,du.}
\]
This includes the exact critical exponent \(q_R=q_c\) at \(\lambda=0\).

For \(A>0\), let \(M_p=2^p\Gamma(p+1/2)/(\sqrt\pi\Gamma(p+1))\). The final phase mean \(\Phi_p(A,B)\) satisfies sharp inequalities
\[
A^p\le\Phi_p(A,B)\le M_pA^p,
\qquad M_pA^p-\Phi_p(A,B)\ge (M_p-1)A^{p-2}(A^2-B^2).
\]
The upper equality cases are exactly \(f(-\omega)=f(\omega)\) almost everywhere or \(f(-\omega)=-f(\omega)\) almost everywhere; the lower equality case is exactly \(B=0\), equivalently equal squared masses of the even and odd parts. The stated stability coefficient is optimal: equality in the stability inequality occurs for \(B=0\) (and at the two pure-parity endpoints). At \(d=2\), the phase mean reduces to \(\Phi_2(A,B)=A^2+B^2/2\).

## Assumptions and scope
All quantities are for fixed integer \(d\ge2\), fixed complex \(L^2\) datum on the standard unit sphere, and unnormalized surface measure. The exponent \(q_R\) is positive for sufficiently large \(R\). The convergence is uniform for \(\lambda\) in arbitrary fixed compact subsets of \(\mathbb R\), for each fixed datum, but no simultaneous uniformity over all \(L^2\) data is asserted. When \(f=0\), both sides vanish; the stability inequality is then interpreted as the trivial zero statement, rather than using the factor \(A^{p-2}\). For \(f\ne0\), \(A>0\). The result concerns the \(L^2\) angular mean followed by radial integration; it is not an ordinary \(L^{q_R}(\mathbb R^d)\) estimate.

## Proof
**1. Exact angular identity.** Decompose \(f=\sum_{k\ge0}P_kf\) into spherical harmonics of degree \(k\), and put \(a_k=\|P_kf\|_2^2\). Let \(\nu=d/2-1\). Funk–Hecke and spherical-harmonic orthogonality give the exact identity
\[
Q_f(r):=\int_{S^{d-1}}|Ef(r\theta)|^2\,d\sigma(\theta)
=(2\pi)^d r^{-2\nu}\sum_{k\ge0}a_kJ_{\nu+k}(r)^2.
\]
Since spherical harmonics have antipodal parity \((-1)^k\), Parseval gives \(A=\sum a_k\) and \(B=\sum(-1)^ka_k\). The latter is real because the antipodal flip is a self-adjoint involution.

**2. Leading oscillatory term.** First suppose \(f\) is a finite spherical-harmonic sum. For each of its finitely many Bessel orders, the fixed-order asymptotic is
\[
J_{\nu+k}(r)=\sqrt{\frac{2}{\pi r}}\cos\left(r-\frac{\pi(\nu+k)}2-\frac\pi4\right)+O_{d,k}(r^{-3/2}).
\]
Squaring and summing yields, as \(r\to\infty\),
\[
Q_f(r)=\frac{(2\pi)^d}{\pi}\,r^{-(d-1)}
\bigl(A+B\cos(2r-\pi\nu-\pi/2)+O_f(r^{-1})\bigr).
\]
The error is additive inside the nonnegative bracket. It remains legitimate when the leading bracket vanishes: for exponents in a compact subset of \([1,\infty)\), the power map is uniformly Lipschitz on a bounded nonnegative interval. Hence the integrated contribution of the \(O_f(r^{-1})\) remainder is \(O_f(1)\) before division by \(\log R\), uniformly for bounded \(\lambda\).

**3. Critical-window logarithmic average.** Write \(p_R=q_R/2=p+\lambda/(2\log R)\) and \(c_d=(2\pi)^d/\pi\). Since \((d-1)(1-p)=-1\), the principal radial factor becomes
\[
r^{d-1-(d-1)p_R}=r^{-1}\exp\left(-\frac{(d-1)\lambda}{2}\frac{\log r}{\log R}\right).
\]
The parameters \(p_R\to p\) and \(c_d^{p_R}\to c_d^p\) uniformly for bounded \(\lambda\). Also \((A+B\cos u)^{p_R}\to(A+B\cos u)^p\) uniformly in \(u\in\mathbb R\), even at zeros. For any continuous periodic \(h\), subtracting its mean gives a periodic function with a bounded primitive. Integration by parts against \(r^{-1}\exp(-c\log r/\log R)\) shows the contribution of that mean-zero part is \(O_h(1)\) uniformly for bounded \(c\), whereas substituting \(t=\log r/\log R\) gives exactly \(\int_0^1e^{-ct}dt\) for the mean. This proves the formula for finite sums.

**4. Extension to all \(L^2\) data.** Here a near-critical published radial–angular estimate is used only as a uniform approximation bound, not as a substitute for the calculation above. Set \(q_*=q_c+1/\log R\). The sharp supercritical spherical mixed-norm extension inequality of Xu states
\[
\left(\int_0^\infty Q_f(r)^{q_*/2}r^{d-1}\,dr\right)^{1/q_*}
\le(2\pi)^{d/2}I_{\nu,0}(q_*)^{1/q_*}\|f\|_2,
\]
with \(I_{\nu,0}(q)=\int_0^\infty J_\nu(r)^q r^{d-1-\nu q}\,dr\) for \(q>q_c\). Fixed-order Bessel bounds at zero and infinity give \(I_{\nu,0}(q_*)\le C_d\log R\) for large \(R\). For \(q_R\le q_*\), Hölder on the annulus \(1\le r\le R\) with measure \(r^{d-1}dr\) yields a factor at most \(\exp(O_{d,L}(1))\), since \(|q_R-q_*|=O_L(1/\log R)\). For \(q_R>q_*\), Cauchy–Schwarz gives the uniform pointwise bound \(Q_f(r)\le\sigma(S^{d-1})^2\|f\|_2^2\), allowing the extra powers to be absorbed. Thus for each \(L>0\),
\[
\sup_{|\lambda|\le L}\sup_{R\ge R_0(d,L)}
T_R(f,\lambda)\le C_{d,L}\|f\|_2^{q_R}.
\]
The normalized truncated mixed norms therefore vary uniformly continuously with \(f\) on bounded \(L^2\) subsets, uniformly for \(R\) large and \(|\lambda|\le L\). Approximate \(f\) in \(L^2\) by finite spherical-harmonic sums, apply the reverse triangle inequality to the normalized mixed norms, and then continuity of powers and of \(\Phi_p(A,B)\). This extends the limit uniformly on compact \(\lambda\)-ranges to every \(f\in L^2\).

**5. Equality and sharp global deficit.** The even and odd projections \(f_\pm=(f\pm f\circ(-\mathrm{id}))/2\) have energies \(E_\pm=(A\pm B)/2\). For \(A>0\), let \(b=B/A\in[-1,1]\). The binomial expansion, integrated termwise, yields
\[
\Phi_p(A,B)=A^p\left(1+\sum_{m\ge1}c_m b^{2m}\right),
\quad c_m={p\choose2m}\frac{\binom{2m}{m}}{4^m}>0.
\]
For \(1<p<2\), these coefficients are strictly positive and summable at \(|b|=1\); at \(p=2\) only \(c_1=1/2\) remains. Their sum is \(M_p-1\), by the beta integral at \(b=1\). Hence the phase mean increases strictly with \(|b|\), proving both equality characterizations. Finally, \(1-b^{2m}\ge1-b^2\) gives
\[
M_pA^p-\Phi_p(A,B)
=A^p\sum_{m\ge1}c_m(1-b^{2m})
\ge(M_p-1)A^{p-2}(A^2-B^2).
\]
Taking \(b=0\) proves optimality of the coefficient. Because \(A^2-B^2=4E_+E_-\), this is a global quantitative parity-defect formula.

## Verification
The accompanying standalone Python checker evaluates fixed-harmonic Bessel models on large radial shells in three dimensions, compares nine critical-window configurations to the analytically predicted shell mean, checks the gamma integral, and checks the sharp parity-defect inequality. Its successful output is `CHECK_OK: Bessel shell convergence (3 dimensions x 3 exponents), gamma identity and sharp parity-deficit inequalities`. The calculation is a finite numerical sanity check; it is not an infinite-dimensional or asymptotic certificate. The proof above establishes the universal theorem analytically. Run `python check.py` with NumPy and SciPy installed.

## Relationship to prior work
Xu (2026) proves sharp supercritical radial–angular Fourier extension on spheres for \(q>2d/(d-1)\). That result is invoked in Step 4 for uniform approximation control, but it does not state the endpoint logarithmic coefficient, the \(\lambda/\log R\) two-sided crossover, the antipodal dependence, or the sharp parity stability law. Carneiro, Oliveira e Silva, and Sousa developed an earlier sharp mixed-norm spherical restriction framework with Bessel/spherical-harmonic reductions. Bakas, Ciccone, and Wright discuss a critical logarithmic upper bound for the two-dimensional circle; a logarithmic upper bound is not the exact all-data leading coefficient or the all-dimensional critical-window classification proved here. The logarithmic crossover of mollified Euclidean-ball Fourier kernels concerns a different transform and a distinct critical exponent \(2d/(d+1)\). No priority claim is made for the classical Bessel expansion, the Funk–Hecke identity, or the supercritical extension bound.

## Limitations
This is a leading-order result for a logarithmically expanding radial interval; no lower-order expansion is asserted. The convergence is for each fixed \(L^2\) input, not uniform over arbitrary varying functions with growing spherical-harmonic degree. It does not establish ordinary spatial \(L^{q_c}\) restriction/extension estimates. The source literature may contain unindexed equivalent endpoint formulas; independent historical-priority checking and independent mathematical validation remain outstanding.

## References
- Zewei Xu, “Sharp radial–angular mixed norm Fourier extension and global stability on spheres,” arXiv:2610.19648v1, first posted 2026-10-14, https://arxiv.org/html/2610.19648v1.
- Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, “Sharp mixed norm spherical restriction,” arXiv:1710.10365, https://arxiv.org/abs/1710.10365.
- Odysseas Bakas, Valentina Ciccone, James Wright, “Walter Rudin meets Elias M. Stein,” Notices of the AMS (2023), https://doi.org/10.1090/noti2804.
