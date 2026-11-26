# Joint Gaussian fluctuations at fixed offsets in the logarithmic-time Kac ring

## Finding

Consider the Kac ring on \(N\) sites, with every initial spin \(+1\). The scatterer signs \(\xi_j\) are independent with \(\Pr(\xi_j=-1)=p\in(0,1/2)\), and are held fixed during the evolution. Write \(\mu=1-2p\), \(\kappa=-\log\mu\), and \(\tau_N=\log N/(2\kappa)\). Let \(M_N(t)\) be the mean spin at integer time \(t\).

Let \(t_N\) be integers with \(t_N\to\infty\) and \(t_N=O(\log N)\). For any \(m\ge 2\) distinct fixed integer offsets \(h_1,\ldots,h_m\), under the annealed scatterer law,
\[
\sqrt N\bigl(M_N(t_N+h_i)-\mu^{t_N+h_i}\bigr)_{i=1}^m
\ \Longrightarrow\ \mathcal N_m(0,C),\qquad
C_{ij}=\mu^{|h_i-h_j|}\left(|h_i-h_j|+\frac{1+\mu^2}{1-\mu^2}\right).
\]
Along subsequences with \(t_N-\tau_N\to a\in\mathbb R\), the **joint** limit without centering is \(\mathcal N_m(b,C)\), where \(b_i=e^{-\kappa(a+h_i)}\). This determines the dependence of fluctuations at distinct nearby times, not just their one-time scales. For example, it determines limiting simultaneous positivity probabilities by Gaussian orthant probabilities, since each marginal has positive variance. Integer-time rounding can leave different subsequential means: for \(t_N=\lfloor\tau_N+s\rfloor\) the centered time offset is \(s-\{\tau_N+s\}\).

## Assumptions and scope

The law is over the independent scatterers, not conditional on their realization. The parameter \(p\) is fixed. With cyclic indices, write \(Y_j(t)=\prod_{r=0}^{t-1}\xi_{j-r}\), so that for \(0\le t\le N\), \(M_N(t)=N^{-1}\sum_jY_j(t)\) and \(\mathbb EY_j(t)=\mu^t\). The theorem does not describe microscopic mixing, a fixed-number scatterer law, or times near recurrence.

## Proof

For \(1\le u\le v\) with \(u+v<N\), fix a window of length \(u\). Among the cyclic shifts of a window of length \(v\), exactly \(v-u+1\) contain the first window and exactly two have overlap \(u-r\) for each \(1\le r<u\); disjoint windows have zero covariance. Squaring a common sign cancels it, so overlaps of size \(u-r\) leave a product with expectation \(\mu^{v-u+2r}\). Consequently,
\[
N\operatorname{Cov}(M_N(u),M_N(v))
=(v-u+1)\mu^{v-u}+2\sum_{r=1}^{u-1}\mu^{v-u+2r}-(u+v-1)\mu^{u+v}.
\]
At the asserted times, \(d=v-u\) is fixed, \((u+v-1)\mu^{u+v}\to0\) and \(2\sum_{r=1}^{u-1}\mu^{d+2r}\to 2\mu^{d+2}/(1-\mu^2)\), giving \(C\).

For any real coefficients \(a_i\), put \(Z_j=\sum_i a_i(Y_j(t_N+h_i)-\mu^{t_N+h_i})\). Each \(Z_j\) is bounded by \(2\sum_i|a_i|\) and depends on at most \(L_N=t_N+\max_i h_i=O(\log N)\) consecutive signs. Each pair of window lengths in this sum differs by a fixed amount. The overlap covariances for that pair are nonnegative and bounded by the corresponding expectations \(\mu^d\) or \(\mu^{d+2r}\), so their absolute sum over shifts is bounded uniformly in \(N\). By the triangle inequality the same holds for the \(Z_j\) covariances. Thus any discarded set of \(o(N)\) summands has variance \(o(N)\).

Keep blocks of length \(b_N=\lfloor N^{1/3}\rfloor\) and discard intervening gaps of length \(L_N\), with a wraparound gap as well. The kept block sums use disjoint signs and are independent; only \(O(NL_N/b_N+b_N+L_N)=o(N)\) terms are omitted. Their normalized omission tends to zero in \(L^2\). The total variance of the retained sum divided by \(N\) tends to \(a^\top C a\), by the covariance formula and the negligible omission. Each block is bounded by \(2b_N\sum_i|a_i|=o(\sqrt N)\), so the Lindeberg condition holds when the limiting variance is positive. If it is zero, Chebyshev's inequality gives convergence to zero instead. The scalar Lindeberg–Feller theorem followed by Cramér–Wold establishes the vector limit. Finally \(\sqrt N\mu^{t_N+h_i}=\exp[-\kappa(t_N-\tau_N+h_i)]\), giving the uncentered vector limit by Slutsky's theorem.

## Verification

The unchanged `verify_kac.py` (Python and NumPy) compares the overlap formula against finite enumeration and evaluates finite covariance matrices. These are finite diagnostics only; the joint limit uses the uniform variance bound and independent-block argument above.

## Relationship to prior work

Hiura's fixed-horizon annealed covariance, specialized to the all-positive initial state, gives the same covariance identity in its fixed-time setting. It does not provide the joint Gaussian limit when the observation times themselves diverge. The Kac-ring revival analysis cited below already proves a scalar central limit theorem for the early-time circular product average at logarithmic times and uses the same signal-to-noise scale. Those one-time conclusions are not claimed here. The distinct assertion is joint normality across different fixed offsets at a diverging time, with the explicit non-diagonal kernel. Scalar normal limits and covariances alone do not establish joint Gaussianity. Cardoen's thesis remains a historical-priority risk because the relevant full text was not available for comparison.

## References

1. K. Hiura, *Macroscopic dynamical fluctuations in Kac ring model*, [arXiv:2109.06434](https://arxiv.org/abs/2109.06434), §3.3, Eq. (3.16).
2. *A logarithmic Gaussian-mixture revival window in the Kac ring*, [Resultary record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-logarithmic-gaussian-mixture-revival-window-in-the-kac-ring--3f13b8f70833), proof of the early-time product-average CLT.
3. D. Cardoen, *The Gibbs hypothesis for macroscopic fluctuations: study of the Kac ring model*, [DOI 10.13140/RG.2.1.2887.4323](https://doi.org/10.13140/RG.2.1.2887.4323).
