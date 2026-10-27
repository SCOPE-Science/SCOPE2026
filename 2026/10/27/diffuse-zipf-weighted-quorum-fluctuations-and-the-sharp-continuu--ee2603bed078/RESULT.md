# Diffuse-Zipf weighted-quorum fluctuations and the sharp continuum-centering boundary

## Finding

For the aligned Zipf weighted-quorum model in the diffuse regime, there is a Gaussian limit on the \(\sqrt N\) scale around the **finite-population mean crossing**, and an explicit lower-order deterministic displacement of that crossing. The displacement changes the limiting law if the leading continuum crossing is used for centering, with a sharp transition at the Zipf exponent \(s=1/2\).

Write \(b=1-s\). Define the continuum profile, its threshold root, and its derivative:

\[
F_s(v)=b\int_0^1x^{-s}(1-e^{-bv x^{-s}})\,dx,\quad F_s(u)=\theta,\quad D=F_s'(u)=b^2\int_0^1x^{-2s}e^{-bu x^{-s}}\,dx.
\]

Define the positive variance integral

\[
V=b^2\int_0^1x^{-2s}e^{-bu x^{-s}}(1-e^{-bu x^{-s}})\,dx.
\]

Let \(u_N\) be the unique solution of

\[
\sum_{i=1}^Nq_{i,N}(1-e^{-u_NNq_{i,N}})=\theta.
\]

For all fixed \(0<s<1\), \(0<\theta<1\) and \(\lambda>0\), as \(N\to\infty\),

\[
\sqrt N\left(\frac{\lambda\tau_{N,\theta}}N-u_N\right)\Longrightarrow\mathcal N\left(0,\frac{V}{D^2}\right).
\]

The deterministic crossing has the **sharp displacement**

\[
N^{1-s}(u_N-u)\longrightarrow\delta_{s,\theta}
=-\frac{b\zeta(s)[1-\theta-uD]}{D},
\]

where the real \(\zeta(s)\) for \(0<s<1\) is defined without analytic continuation by

\[
\zeta(s)=\lim_{N\to\infty}\left(\sum_{j=1}^{N}j^{-s}-\frac{N^{1-s}}{1-s}\right).
\]

As a consequence, the continuum-centered fluctuation has the following three regimes:

\[
\sqrt N\left(\frac{\lambda\tau_{N,\theta}}N-u\right)
\Longrightarrow
\begin{cases}
\mathcal N(0,V/D^2),&0<s<1/2,\\
\mathcal N(\delta_{1/2,\theta},V/D^2),&s=1/2.
\end{cases}
\]

For \(1/2<s<1\) and \(\delta_{s,\theta}\ne0\), the same continuum-centered expression tends in probability to \(+\infty\) when \(\delta_{s,\theta}>0\), and to \(-\infty\) when \(\delta_{s,\theta}<0\). The finite-mean-root centered Gaussian law remains valid in all three regimes.

## Assumptions and scope

Take a fixed \(s\in(0,1)\), \(\theta\in(0,1)\), \(\lambda>0\), and integer \(N\ge1\). Set \(H_N^{(s)}=\sum_{j=1}^Nj^{-s}\), \(q_{i,N}=i^{-s}/H_N^{(s)}\). Let \(T_{i,N}\), for \(1\le i\le N\), be mutually independent exponential random variables with rates \(\lambda q_{i,N}\). The discovered weight at time \(t\) is

\[
M_N(t)=\sum_{i=1}^Nq_{i,N}\mathbf1_{\{T_{i,N}\le t\}},\qquad
\tau_{N,\theta}=\inf\{t\ge0:M_N(t)>\theta\}.
\]

All limits take \(N\to\infty\) with the other parameters fixed; the threshold is strictly crossed. The law is continuous at its Gaussian limiting quantiles even if a finite weighted sum can equal \(\theta\). The continuum integrals are finite: the exponential factor dominates every power singularity as \(x\downarrow0\).

## Proof

**1. Exact independent-summand representation.** Let \(Y_N=\lambda\tau_{N,\theta}/N\) and \(B_{i,N}(v)=\mathbf1_{\{T_{i,N}\le Nv/\lambda\}}\). The \(B_{i,N}(v)\) are independent Bernoulli random variables with success probabilities \(1-e^{-vNq_{i,N}}\). Set \(\mathcal M_N(v)=\sum_iq_{i,N}B_{i,N}(v)\). The displayed equation defining \(u_N\) is precisely \(\mathbb E\mathcal M_N(u_N)=\theta\), and strict monotonicity from zero to one gives uniqueness.

**2. Profile and variance limits.** Put \(c_N=N^{1-s}/H_N^{(s)}\). Then \(c_N\to b\) and \(Nq_{i,N}=c_N(i/N)^{-s}\). For any fixed \(v>0\), Riemann sums with the exponentially suppressed singularity give

\[
\mathbb E\mathcal M_N(v)\to F_s(v),\qquad
\frac{d}{dv}\mathbb E\mathcal M_N(v)\to F_s'(v),
\]

and

\[
N\operatorname{Var}(\mathcal M_N(v))\to V_s(v)
=b^2\int_0^1x^{-2s}e^{-bv x^{-s}}(1-e^{-bv x^{-s}})\,dx.
\]

These convergences hold locally uniformly for \(v\) in any compact subset of \((0,\infty)\): after multiplying the integrands by the appropriate powers of \(x^{-s}\), the exponential is still a uniform integrable envelope. Hence \(u_N\to u\) and \(V_s(u_N+z/\sqrt N)\to V\) for each fixed \(z\).

**3. Triangular-array Lyapunov estimate and inversion.** At \(v_N=u_N+z/\sqrt N\), write \(\mathcal M_N(v_N)-\mathbb E\mathcal M_N(v_N)=\sum_i X_{i,N}\), where \(X_{i,N}=q_{i,N}(B_{i,N}(v_N)-\mathbb E B_{i,N}(v_N))\). For Bernoulli success probability \(p\), \(\mathbb E|B-p|^3\le p(1-p)\le e^{-v_NNq_{i,N}}\). Thus

\[
N^{3/2}\sum_i\mathbb E|X_{i,N}|^3
\le N^{3/2}\sum_iq_{i,N}^3e^{-v_NNq_{i,N}}
=O(N^{-1/2})\longrightarrow0.
\]

The estimate follows from the bounded Riemann sums of \(x^{-3s}e^{-\varepsilon b x^{-s}}\), with \(v_N\ge\varepsilon>0\), \(c_N\) bounded away from zero and infinity. The Lyapunov theorem yields \(\sqrt N(\mathcal M_N(v_N)-\mathbb E\mathcal M_N(v_N))\Rightarrow\mathcal N(0,V)\). Uniform convergence of the mean derivative gives

\[
\sqrt N(\mathbb E\mathcal M_N(v_N)-\theta)\to zD.
\]

Since \(\{Y_N\le v_N\}=\{\mathcal M_N(v_N)>\theta\}\), normal continuity implies \(\mathbb P(\sqrt N(Y_N-u_N)\le z)\to\Phi(zD/\sqrt V)\). This proves the first theorem.

**4. Exact deterministic correction.** The generalized harmonic asymptotic (Euler summation) is

\[
H_N^{(s)}=\frac{N^{1-s}}b+\zeta(s)+O(N^{-s}),
\quad c_N=b-b^2\zeta(s)N^{s-1}+o(N^{s-1}).
\]

Define \(I(v,c)=\int_0^1cx^{-s}e^{-vcx^{-s}}\,dx\). The function \(x\mapsto cx^{-s}e^{-vcx^{-s}}\), continuously extended by zero at \(x=0\), has a uniformly bounded first derivative for \((v,c)\) near \((u,b)\). Because \(\sum_iq_{i,N}=1\), the normalized mean obeys the more precise identity

\[
\mathbb E\mathcal M_N(v)
=1-\frac1N\sum_{i=1}^Nc_N(i/N)^{-s}e^{-vc_N(i/N)^{-s}}
=1-I(v,c_N)+O(N^{-1}),
\]

with the error locally uniform in \(v\). Also \(I(u,b)=1-\theta\), and differentiation under the integral gives

\[
\partial_cI(u,b)=\frac{1-\theta-uD}{b}.
\]

Taylor expansion at \(c=b\) therefore yields

\[
\mathbb E\mathcal M_N(u)-\theta
=b\zeta(s)(1-\theta-uD)N^{s-1}+o(N^{s-1}).
\]

Applying the mean-value theorem between \(u_N\) and \(u\) and using the derivative limit \(D>0\) proves the stated \(\delta_{s,\theta}\). Combining this with the finite-root CLT via Slutsky's theorem gives both Gaussian continuum-centered regimes and, when \(s>1/2\) and \(\delta\ne0\), divergence of the deterministic shift \(\sqrt N(u_N-u)=\delta N^{s-1/2}(1+o(1))\) relative to a tight Gaussian residual.

## Verification

The accompanying `verify.py` independently evaluates the continuum integrals and finite-population mean-root, derivative, and variance sums, checking the asymptotic shift at \(s=1/4,1/2,3/4\) and exact normalized Bernoulli moment formulas. Run `python verify.py` after installing dependencies listed in `requirements.txt`. These numerical tests support, but do not replace, the all-\(N\) proof above.

## Relationship to prior work

Müller and Šebek, *Weighted-threshold Coupon Collection* (arXiv:2607.08551, first submitted 2026-07-09), introduce this exact aligned Zipf quorum model and prove its first-order diffuse law of large numbers (Theorem 5.3), with the same limiting mean profile \(F_s\). Their Sections 2–5 provide a mean profile, concentration, and first-order convergence; they do not give the finite-root Gaussian fluctuation theorem or the explicit zeta-normalization correction that creates the continuum-centering transition. The result here retains their basic model and limiting crossing, and establishes a distinct second-order statement.

Chebunin and Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models* (arXiv:1906.10949; DOI:10.1007/s10959-020-01053-6), prove general central limit theorems for fixed **infinite** summable sequences of urn probabilities satisfying regular variation. Their hypotheses and normalizations do not directly cover the finite, \(N\)-dependent Zipf probability vector \(q_{i,N}\) on the macroscopic time scale \(N/\lambda\), or the specific inverse mean crossing and \(N^{s-1}\) finite-normalizer displacement. The latter is not a mere restatement of an occupancy CLT.

## Limitations

The result fixes \(s,\theta,\lambda\); it does not address simultaneous parameter limits, full-collection thresholds, or the atomic \(s>1\) regime. It gives no continuum-centered limit for the exceptional supercritical cases \(\delta_{s,\theta}=0\), where finer deterministic expansions could matter. The proof is analytic; finite numerical checks cannot establish novelty or asymptotic correctness. Independent literature assessment remains outstanding, particularly concerning general triangular-array inverse-process theorems and second-order occupancy theory.

## References

1. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1, 2026-07-09, https://arxiv.org/abs/2607.08551 .
2. M. Chebunin and S. Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, arXiv:1906.10949, https://arxiv.org/abs/1906.10949 ; DOI:10.1007/s10959-020-01053-6.
3. Classical Lyapunov central limit theorem, Euler summation for generalized harmonic numbers, and Slutsky's theorem (standard results used in the proof).
