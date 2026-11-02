# Two-stage symmetry breaking and sixfold spectral fibers in first-Hermite strip localization

## Finding

Let \(h_1(t)=\sqrt2\,\pi^{-1/4}t e^{-t^2/2}\), with \(\|h_1\|_2=1\). For \(a>0\), define the infinite time-frequency strip \(S_a=[-a,a]\times\mathbb R\) and the positive short-time Fourier transform (STFT) concentration operator
\[
H_a=V_{h_1}^{*}\mathbf1_{S_a}V_{h_1}\quad\text{on }L^2(\mathbb R).
\]
The operator is exactly multiplication by the real-analytic function
\[
F_a(t)=\int_{t-a}^{t+a}\frac{2u^2e^{-u^2}}{\sqrt\pi}\,du
=J(t+a)-J(t-a),\qquad
J(t)=\frac12\operatorname{erf}(t)-\frac{te^{-t^2}}{\sqrt\pi}.
\]
For each \(a>0\), there is a unique \(b(a)>a\) solving
\[
b(a)=a\coth(a b(a)).
\]
There is a unique critical half-width \(a_*\in(1,\infty)\), characterized without approximations by
\[
F_{a_*}(0)=F_{a_*}(b(a_*)).
\]
Numerically, \(a_*=1.0776636283762369\ldots\) and \(b(a_*)=1.238236621768071\ldots\). The sharp concentration norm is
\[
\|H_a\|=\max_t F_a(t)=
\begin{cases}
F_a(b(a)),&0<a<a_*,\\
F_a(0)=F_a(b(a)),&a=a_*,\\
F_a(0),&a>a_*.
\end{cases}
\]
Its maximizing locations are exactly \(\{-b(a),b(a)\}\) before the threshold, exactly \(\{0,-b(a_*),b(a_*)\}\) at the threshold, and exactly \(\{0\}\) afterwards. The center is a strict local minimum for \(0<a\le1\) (quartically flat at \(a=1\)) and a strict local maximum for \(a>1\). The change in its local type therefore precedes the global switch; the global maximizing locations jump discontinuously at \(a_*\) and the optimal norm is nondifferentiable there.

There is also a complete spectral multiplicity classification. Put \(C_a=F_a(0)\), \(O_a=F_a(b(a))\). For \(a>1\), let \(u(a)\in(0,a)\) be the unique solution of \(u=a\tanh(au)\) and set \(m_a=F_a(u(a))\). For almost every \(y\in(0,\|H_a\|)\), spectral multiplicity equals the number of real solutions to \(F_a(t)=y\). If \(0<a\le1\), it is \(2\) for \(0<y<C_a\) and \(4\) for \(C_a<y<O_a\). If \(a>1\), it is \(2\) for \(0<y<m_a\) and \(6\) for \(m_a<y<\min(C_a,O_a)\); additionally it is \(4\) on \((C_a,O_a)\) when \(C_a<O_a\), and \(2\) on \((O_a,C_a)\) when \(O_a<C_a\). Empty intervals are omitted. For all \(a>0\), \(\sigma(H_a)=[0,\|H_a\|]\) is purely absolutely continuous and \(H_a\) has no eigenvalues.

## Assumptions and scope

The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\), and the STFT is \(V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt\). The window is the normalized first Hermite function in the displayed unitary-dilation convention. The frequency direction of the concentration region is the entire real line, not a finite band. The operator acts on all of \(L^2(\mathbb R)\), not on a finite Hermite band. All thresholds and multiplicities concern that specific window and those strips, with \(a>0\) arbitrary.

## Proof

**1. Exact reduction.** For fixed \(x\), Plancherel in \(\xi\) gives
\[
\int_{\mathbb R}|V_{h_1}f(x,\xi)|^2\,d\xi
=\int_{\mathbb R}|f(t)|^2|h_1(t-x)|^2\,dt.
\]
Tonelli and integration over \(-a\le x\le a\) imply
\(\langle H_af,f\rangle=\int_{\mathbb R}F_a(t)|f(t)|^2\,dt\). Polarization establishes \(H_a=M_{F_a}\). The stated primitive follows by differentiating \(J\), and \(F_a\) is positive, even, real analytic, and tends to zero at both ends.

**2. All critical locations.** Write \(w(t)=2t^2e^{-t^2}/\sqrt\pi\); then
\(F_a'(t)=w(t+a)-w(t-a)\). On \(t>a\), the equation \(F_a'(t)=0\) is equivalent to \(t=a\coth(at)\). The difference \(a\coth(at)-t\) is strictly decreasing, positive at \(t=a\), and tends to \(-\infty\); there is exactly one root \(b(a)>a\), and the derivative changes from positive to negative there. For \(0<t<a\), stationarity is equivalent to \(t=a\tanh(at)\). The function \(a\tanh(at)-t\) has second derivative strictly negative for \(t>0\), derivative \(a^2-1\) at zero and negative value at \(t=a\). Thus no positive interior solution exists when \(a\le1\), and exactly one \(u(a)\in(0,a)\) exists when \(a>1\). Directly comparing \(w(t+a)\) to \(w(t-a)\) shows that \(F_a\) increases on \((0,b(a))\) when \(a\le1\); when \(a>1\) it decreases on \((0,u(a))\), increases on \((u(a),b(a))\), and decreases on \((b(a),\infty)\). Moreover, \(F_a''(0)=8a(1-a^2)e^{-a^2}/\sqrt\pi\) and \(F_1^{(4)}(0)=16/(e\sqrt\pi)>0\), so the center is a strict local minimum through \(a=1\) and a strict local maximum when \(a>1\). Thus all global maxima occur among the center and the two outer peaks.

**3. Unique global transition.** Let \(D(a)=F_a(0)-F_a(b(a))\) for \(a>1\). Smoothness of \(b\) follows from the strict derivative of its defining equation. By differentiating at a stationary outer peak,
\[
D'(a)=2w(a)-2w(a+b(a))>0,
\]
because \(a>1\), \(b(a)>a\), and \(w\) is strictly decreasing on \((1,\infty)\). At \(a=1\), the center is a strict local minimum, so \(D(1)<0\). As \(a\to\infty\), \(F_a(0)\to1\), while \(F_a(b(a))<1/2\) because its integration interval is contained in \((0,\infty)\). Continuity and strict increase prove the unique crossing \(a_*>1\). For \(a<a_*\), symmetry and the monotonicity intervals give exactly the two global peaks; at equality all three peaks attain the norm; above it only the center does. At \(a_*=\text{critical}\), the one-sided derivatives of the norm are \(2w(a_*+b(a_*))\) and \(2w(a_*)\), respectively, and differ strictly.

**4. Spectrum and multiplicities.** Each positive branch listed in Step 2 is strictly monotone and extends to its endpoint values, and symmetry doubles the number of preimages for almost every positive level. Counting inverse branches gives all stated multiplicities. As multiplication by \(F_a\), the spectrum is its essential range \([0,\max F_a]\). All level sets are finite (indeed at most six points), so they have Lebesgue measure zero: no eigenvalues occur. On each monotone open branch \(F_a\) is a real-analytic diffeomorphism except at isolated critical points. Change of variables shows that the pushforward of \(|f(t)|^2dt\) under \(F_a\) is absolutely continuous for every \(f\in L^2\). Hence the spectrum is purely absolutely continuous. The norm is not attained by any nonzero \(L^2\) vector, although it is approached by normalized functions concentrated near maximizing locations.

## Verification

The standalone `checker.py` uses only the Python standard library. Run `python3 checker.py` from a directory containing that file. It validates the normalized primitive, all defining root equations, multiple regimes around both thresholds, the strict comparison across the unique crossing, and representative inverse-branch counts. The numerical values above are reproducible to the shown precision using bisection and `math.erf`. All universal existence, uniqueness, spectral, and multiplicity claims are proved in Steps 1–4; finite checks are supplementary and do not constitute exhaustive proof.

## Relationship to prior work

Abreu and Speckbacher [1] develop Hermite-window STFT concentration and large-sieve inequalities on general phase-space regions, with local reproducing formulas for disks. They supply the STFT framework and motivating concentration problem, not a determination of the sharp norm, global peaks, or spectral multiplicities for an infinite frequency strip. Keller and Luef [2] give the broader equivalence with polyanalytic Toeplitz quantization and symbolic calculus, but no displayed global strip-phase classification. Huang and Zhang [3] extend analytic-Fock norm bounds to nonradial integrable symbols, but the strip has infinite area and the first-Hermite localization is not the analytic Gaussian level. The present proof uses the exact full-frequency marginal to distinguish the central peak's local onset from the later global exchange and to recover the full spectral fibers. Finite-dimensional Hermite-band concentration matrices and disk-localization Toeplitz operators address different operators; neither implies this infinite-strip multiplier's full spectrum. The novelty assessment is conditional on the inspected literature: elementary sliding-window reductions or further specialized publications could contain some of these formulas.

## Limitations

The strip is infinite in frequency; the operator is not compact, and its norm has no nonzero \(L^2\) maximizer. Replacing the strip by a bounded rectangle changes the problem. No analogous transition classification for higher Hermite windows, arbitrary windows, or stability of finite-frequency approximations is claimed. The numerical critical width is an approximation to the uniquely defined analytic root, not a closed elementary expression. No independent mathematical audit or validation has been performed.

## References

[1] L. D. Abreu and M. Speckbacher, *Donoho-Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces*, arXiv:1808.02258v1 (first public 2018-08-07), https://arxiv.org/html/1808.02258v1.

[2] J. Keller and F. Luef, *Polyanalytic Toeplitz Operators: Isomorphisms, Symbolic Calculus and Approximation of Weyl Operators*, arXiv:1905.07741v1 (first public 2019-05-19), https://arxiv.org/abs/1905.07741.

[3] Y. C. Huang and J.-Y. Zhang, *Norm Bounds for Self-Adjoint Toeplitz Operators with Non-Radial Symbols on the Fock Space*, arXiv:2405.11147v1 (first public 2024-05-18), https://arxiv.org/abs/2405.11147.
