# Exponential-tilt logarithmic transport at the critical power-law restart threshold

## Finding

Let \(X_N\) be the observed position of the weighted three-state Grover quantum walk described below, with independent full-state restarts having waiting-time law
\[
 \Pr(T=m)=\frac{m^{-s_N}}{\zeta(s_N)},\qquad s_N=2+\frac{\lambda}{\log N},\qquad m=1,2,\ldots,
\]
where \(\lambda\in\mathbb R\) is fixed and the waiting-time exponent is fixed **within** each experiment of length \(N\). For every self-loop weight \(\ell>0\), normalized initial coin state \(\chi\in\mathbb C^3\), and fixed real \(\lambda\), as integer \(N\to\infty\),
\[
 \frac{\log(1+|X_N|)}{\log N}
 \ \Longrightarrow\ W(\ell,\chi)\,\delta_0+(1-W(\ell,\chi))\,\nu_\lambda,
 \qquad
 \nu_\lambda(du)=\frac{e^{-\lambda u}}{I_\lambda}\mathbf1_{(0,1)}(u)\,du,
 \qquad I_\lambda=\int_0^1e^{-\lambda v}\,dv.
\]
Here \(I_0=1\), and \(I_\lambda=(1-e^{-\lambda})/\lambda\) otherwise. The explicit non-restart flat-band weight is
\[
 W(\ell,\chi)=\frac{\sqrt{\ell+2}}{\sqrt{\ell+2}+\sqrt2}|\langle s_\ell,\chi\rangle|^2
 +\frac{\sqrt2}{\sqrt{\ell+2}+\sqrt2}|\langle\chi_A,\chi\rangle|^2,
\]
where \(s_\ell=(1,\sqrt\ell,1)/\sqrt{\ell+2}\) and \(\chi_A=(1,0,-1)/\sqrt2\). Independently, the logarithmic backward recurrence age \(A_N\), the number of steps since the most recent restart, satisfies
\[
\frac{\log(1+A_N)}{\log N}\Longrightarrow \nu_\lambda.
\]
For the flat-band-dark coin \(\chi_\perp=(\sqrt\ell,-2,\sqrt\ell)/\sqrt{2(\ell+2)}\), one has \(W=0\); at \(\lambda=0\) the logarithmic position is uniform on \((0,1)\). For the active coin \(s_\ell\), the origin has limiting log-scale mass \(\sqrt{\ell+2}/(\sqrt{\ell+2}+\sqrt2)\). The limits \(\lambda\to\pm\infty\) concern the limiting family after the fixed-\(\lambda\) large-\(N\) limit, not an interchange of limits.

## Assumptions and scope

The spatial Hilbert space is \(\ell^2(\mathbb Z)\) and the three coin labels mean left, stay, right. The one-step operator is \(U_\ell=S(C_\ell\otimes I)\), where \(C_\ell=2|s_\ell\rangle\langle s_\ell|-I_3\), and \(S\) conditionally translates by \(-1,0,+1\). The initial state and **each** restarted state are \(|0\rangle\otimes\chi\). Between restarts the evolution is fully unitary, and only the final position is measured; there are no intermediate projective detections. Each positive integer waiting time is independent and sampled from the specified zeta-normalized law. For each \(N\), \(s_N>1\) is assumed (automatically true for sufficiently large \(N\)), and a fresh process with that law is considered. All limiting statements allow arbitrary but **fixed** \(\lambda\in\mathbb R\), \(\ell>0\), and normalized complex \(\chi\), without uniformity in \(\lambda\) or simultaneous variation of \(\ell\).

Write the waiting times as \(T_1,T_2,\ldots\), renewal epochs \(S_k=T_1+\cdots+T_k\) with \(S_0=0\), and the renewal count \(R_n=\max\{k:S_k\le n\}\). Let \(A_n=n-S_{R_n}\). The observation position \(X_N\), conditional on \(A_N=a\), has the distribution of the position \(Y_a\) of the unrestarted walk after \(a\) steps. The benchmark dispersive velocity law is the weak limit \(Y_a/a\Rightarrow V\), whose only atom at zero is the flat-band weight \(W\); fixed-site position probabilities approach the flat-band profile summing to \(W\) [1]. These input spectral facts also follow from Fourier decomposition of the displayed unitary: its flat eigenvalue is one, the other two eigenvalues are dispersive, and their group velocity vanishes only on a set of zero Lebesgue measure.

## Proof

**1. Uniform truncated-moment and survival estimates.** Write \(s=s_N\), \(\Phi_a=\Pr(T>a)=\zeta(s,a+1)/\zeta(s)\), and \(m_n=\mathbb E(T\wedge n)=\sum_{a=0}^{n-1}\Phi_a\). For every fixed \(0<\alpha<\beta\le1\), comparison of the decreasing power series with its integral gives, uniformly for \(N^\alpha\le a\le N^\beta\),
\[
\Phi_a=\frac{a^{1-s}}{(s-1)\zeta(s)}\bigl(1+O(a^{-1})\bigr).
\]
Consequently, for \(0\le\alpha<\beta\le1\), splitting off finitely many small ages if necessary,
\[
\sum_{N^\alpha\le a\le N^\beta}\Phi_a
\sim\frac{\log N}{\zeta(2)}\int_\alpha^\beta e^{-\lambda u}\,du
\]
whenever \(\alpha<\beta\); the same holds for \(\alpha=0\) by bounding ages smaller than \(N^\varepsilon\) and then letting \(\varepsilon\downarrow0\). Thus \(m_N\sim (\log N)I_\lambda/\zeta(2)\), and \(m_{\lfloor cN\rfloor}/m_N\to1\) for every fixed \(c>0\). The tail estimate also yields \(\mathbb E[(T\wedge\lfloor cN\rfloor)^2]=O(N)\). Constants in these bounds may depend on \(\lambda,c\), but not on \(N\).

**2. A triangular renewal theorem, including local masses.** Fix \(n=n_N\) with \(n/N\to c\in(0,\infty)\); all expectations in this step refer to the row-\(N\) waiting law. For any fixed \(d>0\), put \(k_N=\lfloor d n/m_N\rfloor\). The sum of \(k_N\) variables truncated at \(n\) has expectation asymptotic to \(dn\) and variance \(O(n^2/\log N)\), and
\[
\Pr(\max_{1\le j\le k_N}T_j>n)\le k_N\Phi_n=O(1/\log N).
\]
Chebyshev's inequality therefore shows \(S_{k_N}/n\to d\) in probability. To pass from renewal-count convergence to its expectation, note that
\[
 n\bigl(1-\mathbb E e^{-T/n}\bigr)
 = n(1-e^{-1/n})\sum_{a\ge0}e^{-a/n}\Phi_a
 =m_n+O(1).
\]
The final bound uses \(\sum_{a<n}a\Phi_a=O(n)\) and \(\sum_{a\ge n}e^{-a/n}\Phi_a=O(1)\), uniformly near \(s=2\). For every integer \(k\ge1\), exponential Markov inequality gives
\[
\Pr(S_k\le n)\le e\bigl(\mathbb E e^{-T/n}\bigr)^k
 \le e\exp\bigl(-km_N/(2n)\bigr)
\]
for all sufficiently large \(N\). By dominated Riemann sums, \(\mathbb E R_n=\sum_{k\ge1}\Pr(S_k\le n)\sim n/m_N\). Therefore, writing \(u_j=\sum_{k\ge0}\Pr(S_k=j)\), the integrated renewal mass satisfies
\[
\sum_{j=0}^{n}u_j=\mathbb E R_n+1\sim n/m_N.
\]

We require a **local**, not merely averaged, renewal bound. This follows here from a monotonicity feature of the power-law waiting times, which we prove. The gamma integral represents their probability mass as a positive mixture of geometric laws:
\[
\frac{m^{-s}}{\zeta(s)}=\int_0^1(1-x)x^{m-1}\,\mu_s(dx),\qquad
\mu_s(dx)=\frac{(-\log x)^{s-1}}{\Gamma(s)\zeta(s)(1-x)}\,dx.
\]
Normalization of the probabilities proves that \(\mu_s\) is a probability measure. Hence \(\Phi_j=\int_0^1x^j\mu_s(dx)\) is log-convex by Cauchy–Schwarz. Set \(B(z)=\sum_{j\ge0}\Phi_jz^j\), and write its formal reciprocal as \(B(z)^{-1}=1-\sum_{j\ge1}b_jz^j\). Comparing coefficients gives \(\Phi_n=\sum_{j=1}^n b_j\Phi_{n-j}\). If \(b_1,\ldots,b_{n-1}\ge0\), then log-convexity implies
\[
\sum_{j=1}^{n-1}b_j\Phi_{n-j}
\le\frac{\Phi_n}{\Phi_{n-1}}\sum_{j=1}^{n-1}b_j\Phi_{n-1-j}=\Phi_n,
\]
so \(b_n\ge0\) by induction. Since the waiting-time generating function is \(1-(1-z)B(z)\), its renewal generating function is \(1/[(1-z)B(z)]\); thus \(u_n=1-\sum_{j=1}^n b_j\) is nonincreasing in \(n\). Sandwiching \(u_n\) between averages of this monotone sequence on \([(1-\epsilon)n,n]\) and \([n,(1+\epsilon)n]\), using the preceding integrated asymptotics at each fixed proportional endpoint, yields
\[
 u_{n_N}\sim\frac1{m_N}\sim\frac{\zeta(2)}{I_\lambda\log N}.
\]
The conclusion is uniform for \(n\in[c_1N,c_2N]\) for any fixed \(0<c_1<c_2<\infty\): otherwise a violating subsequence would have a convergent proportional subsequence, contradicting this result.

**3. Limit of the logarithmic backward age.** The exact renewal decomposition gives \(\Pr(A_N=a)=u_{N-a}\Phi_a\) for \(0\le a\le N\). For any \(0<\alpha<\beta<1\), the local bound from Step 2 is uniform on \(N-a\), \(N^\alpha\le a\le N^\beta\), and Step 1 yields
\[
\Pr\bigl(N^\alpha\le A_N\le N^\beta\bigr)
\longrightarrow\frac{\int_\alpha^\beta e^{-\lambda u}\,du}{I_\lambda}.
\]
The right side integrates to one over \((0,1)\), so there are no unaccounted endpoint masses. It follows that \(\log(1+A_N)/\log N\Rightarrow\nu_\lambda\).

**4. Logarithmic position as a spectral selector.** Let \(Y_a\) be the unrestarted measured position. The spatial support bound \(|Y_a|\le a\) and the nonzero-velocity ballistic weak law imply, for each \(0<\varepsilon<1\),
\[
\limsup_{a\to\infty}\Pr\bigl(|Y_a|\le a^{1-\varepsilon}\bigr)\le\Pr(V=0)=W.
\]
The fixed-site limiting flat-band probabilities sum to \(W\), so the reverse lower bound holds for \(\Pr(|Y_a|\le a^{\varepsilon})\). Thus \(\log(1+|Y_a|)/\log a\Rightarrow W\delta_0+(1-W)\delta_1\). This convergence is also uniform over all integers \(a\ge A\) once \(A\to\infty\), by the definition of sequential convergence. Conditional on ages in \([N^\alpha,N^\beta]\), it implies for bounded continuous \(f\)
\[
\mathbb E\left[f\!\left(\frac{\log(1+|X_N|)}{\log N}\right)\biggm| A_N\right]
=W f(0)+(1-W)f\!\left(\frac{\log A_N}{\log N}\right)+o(1)
\]
with error uniform for fixed \(0<\alpha<\beta<1\). The age limit makes the complement of these windows arbitrarily small by taking \(\alpha\downarrow0\), \(\beta\uparrow1\), completing the claimed weak convergence.

## Verification

The accompanying `verify.py` evaluates the exact renewal convolution and survival law at three observation sizes and three critical-window parameters. It verifies normalization to floating-point tolerance, monotonic renewal mass and finite-scale logarithmic-age diagnostics. It separately constructs the Fourier-space coin and numerically integrates the flat-band projector for three positive self-loop weights and several initial coin states, including the exact dark state; the numerical integral agrees with the analytic weight. The script passed on Python with NumPy and SciPy. Numerical convergence in this problem is logarithmically slow; these checks are diagnostics only, and the arbitrary-size statement rests on the proof above.

## Relationship to prior work

Das [1], Secs. II–V and App. C/E, proves the underlying flat-band decomposition, fixed-site localization, renewal formulas, and fixed-exponent thresholds at \(s=2\). It does **not** provide the triangular power-law protocol \(s_N=2+\lambda/\log N\), the associated local renewal estimate uniform in a moving exponent, or a limiting logarithmic-position distribution. Applying either side's fixed-exponent limit directly at a moving exponent would not justify this result. The positive geometric-mixture argument above supplies the needed local renewal control. General power-law restart phenomena for classical continuous-time random walks are discussed in [2], but they do not determine this quantum flat-band/ballistic logarithmic distribution. The contribution is the explicit critical-window law with a tunable tilt and a separately identifiable flat-band atom, not the known existence of ballistic propagation or the fixed-exponent renewal threshold.

## Limitations

Only complete-state independent renewal restarts, a single-time final position measurement, fixed positive self-loop weight, and fixed real critical-window parameter are treated. No total-variation claim, finite-size error bound or uniformity for a growing parameter is proved. The limiting law describes a position *exponent*, not the full rescaled ballistic-position density or a monitored first-detection distribution. The renewal proof does not require a lattice walk, but the localization weight and its combination with ballistic transport are model-specific. The literature comparisons support best-knowledge originality, not a certification of research priority; a more general uninspected triangular renewal theorem might imply part of the result.

## References

[1] D. Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization*, arXiv:2609.08973v1 (first submitted September 8, 2026), https://arxiv.org/abs/2609.08973 . Full text consulted, including Secs. II–V and App. C/E.

[2] A. S. Bodrova and I. M. Sokolov, *Continuous time random walks under power-law resetting*, arXiv:2001.01350 (2020), https://arxiv.org/abs/2001.01350 . Full text consulted for the earlier classical power-law-reset context.
