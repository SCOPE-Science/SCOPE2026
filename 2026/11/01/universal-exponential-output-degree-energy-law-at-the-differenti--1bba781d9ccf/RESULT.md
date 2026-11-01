# Universal exponential output-degree energy law at the differential-Hilbert Bergman threshold

## Finding
Fix \(-1<\alpha<0\). For \(\delta>0\), let \(T_\delta=\mathcal H_2:A^2_\alpha\to A^2_{\alpha+2+\delta}\) be the differential Hilbert operator. Define the output-degree energy \(E_n(\delta)\), its total mass \(M_\delta\), and the probability distribution \(\nu_\delta\) precisely below. Then, with
\[
C_\alpha=\Gamma(\alpha+4)\Gamma(-\alpha)>0,
\]
the following three statements hold:
\[
\sum_{n=0}^{N-1}E_n(0)=C_\alpha\log N+O_\alpha(1)\qquad (N\to\infty),
\]
\[
M_\delta=\|T_\delta\|_{S_2}^2
=\frac{C_\alpha}{\delta}+O_\alpha(1)\qquad(\delta\downarrow0),
\]
and, most importantly, the *entire rescaled output-degree distribution* obeys the uniform exponential law
\[
\boxed{\ \sup_{s\ge0}\left|\nu_\delta([0,s])-(1-e^{-s})\right|=O_\alpha(\delta).\ }
\]
Equivalently, for every fixed \(s\ge0\), output degrees through \(\lfloor\exp(s/\delta)\rfloor\) account asymptotically for the fraction \(1-e^{-s}\) of the total Hilbert--Schmidt energy. In the symmetric test case \(\alpha=-1/2\), the exact critical coefficient is \(C_{-1/2}=15\pi/8\).

## Assumptions and scope
The unit-disk weighted Bergman norm is defined for \(\gamma>-1\) by
\[
\|f\|_{A^2_\gamma}^2=\frac{\gamma+1}{\pi}\int_{|z|<1}|f(z)|^2(1-|z|^2)^\gamma\,dx\,dy.
\]
Consequently, monomials are orthogonal and have squared norms
\[
w_m(\gamma)=\|z^m\|_{A^2_\gamma}^2
=\frac{\Gamma(\gamma+2)\Gamma(m+1)}{\Gamma(m+\gamma+2)}.
\]
For every \(\delta\ge0\), define
\[
(T_\delta f)(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt,
\quad \beta_\delta=\alpha+2+\delta,
\]
with the standard bounded extension for \(\delta\ge0\) in this range of \(\alpha\). Relative to the normalized monomial bases in source and target, let \(b_{nk}(\delta)\) be its matrix entries, and set
\[
E_n(\delta)=\sum_{k=0}^\infty |b_{nk}(\delta)|^2,\qquad
M_\delta=\sum_{n=0}^\infty E_n(\delta)\quad(\delta>0).
\]
For \(\delta>0\), \(M_\delta<\infty\), and
\[
\nu_\delta=\frac1{M_\delta}\sum_{n=0}^\infty E_n(\delta)\,\delta_{\delta\log(n+1)}.
\]
Here the second \(\delta\) with a subscript denotes a Dirac point mass, not the positive real parameter. All estimates are for each *fixed* \(\alpha\in(-1,0)\); no uniformity as \(\alpha\) approaches an endpoint is claimed. The error in the exponential-law comparison is uniform in every \(s\ge0\).

## Proof
**1. Exact matrix and a single integral.** Since \((1-tz)^{-2}=\sum_{n\ge0}(n+1)t^n z^n\), evaluation on the orthonormal input monomial yields
\[
b_{nk}(\delta)=\frac{n+1}{n+k+1}
\sqrt{\frac{w_n(\beta_\delta)}{w_k(\alpha)}}.
\]
Therefore, on writing
\[
S_n(\alpha)=\sum_{k=0}^\infty\frac{\Gamma(k+\alpha+2)}{\Gamma(\alpha+2)\Gamma(k+1)(n+k+1)^2},
\]
one has the exact identity
\[
E_n(\delta)=(n+1)^2\frac{\Gamma(\beta_\delta+2)\Gamma(n+1)}{\Gamma(n+\beta_\delta+2)}\,S_n(\alpha).
\]
The positive-coefficient binomial series and
\(\int_0^1t^{n+k}(-\log t)\,dt=(n+k+1)^{-2}\)
justify, by Tonelli's theorem,
\[
S_n(\alpha)=\int_0^1t^n(-\log t)(1-t)^{-\alpha-2}\,dt.
\]
For \(-1<\alpha<0\), this integral is finite, including at \(t=1\), since its integrand is asymptotic there to \((1-t)^{-\alpha-1}\).

**2. A uniform sharp row estimate.** For \(0<t<1\), set \(u=1-t\); the elementary logarithmic power series gives
\[
u\le-\log(1-u)\le u+\frac{u^2}{2(1-u)}.
\]
Thus for every integer \(n\ge1\), using the Euler beta integral,
\[
B(n+1,-\alpha)\ \le\ S_n(\alpha)\ \le\
B(n+1,-\alpha)+\tfrac12B(n,1-\alpha).
\]
The gamma-ratio asymptotic \(\Gamma(n+a)/\Gamma(n+b)
=n^{a-b}(1+O(n^{-1}))\), uniformly for \(a,b\) in fixed compact subsets of \(\mathbb R\), now implies
\[
S_n(\alpha)=\Gamma(-\alpha)(n+1)^\alpha(1+O_\alpha((n+1)^{-1})).
\]
For all \(0\le\delta\le1/2\), the same uniform gamma-ratio formula applied to the target monomial norm yields
\[
E_n(\delta)=C_\alpha(\delta)(n+1)^{-1-\delta}
+O_\alpha((n+1)^{-2-\delta}),\qquad
C_\alpha(\delta)=\Gamma(\alpha+4+\delta)\Gamma(-\alpha).
\]
One enlarges the implied constant for the finite case \(n=0\); every remaining estimate is uniformly valid. In particular the sum of the absolute errors over *any* set of rows is bounded independently of \(\delta\in[0,1/2]\).

**3. Critical logarithm and near-critical mass.** At \(\delta=0\), summing the sharp row estimate up to \(N-1\) and using \(\sum_{m=1}^N1/m=\log N+O(1)\) gives the first claimed asymptotic. For \(\delta>0\), summing to infinity gives
\[
M_\delta=C_\alpha(\delta)\sum_{m=1}^\infty m^{-1-\delta}+O_\alpha(1).
\]
By the integral comparison for a positive decreasing function,
\[
\frac1\delta\le\sum_{m=1}^\infty m^{-1-\delta}\le1+\frac1\delta.
\]
Moreover \(C_\alpha(\delta)=C_\alpha+O_\alpha(\delta)\). Thus \(M_\delta=C_\alpha/\delta+O_\alpha(1)\), and finiteness for \(\delta>0\) follows simultaneously.

**4. Uniform distribution, including very large degrees.** Fix \(0<\delta\le1/2\) and any \(s\ge0\), and put \(X=e^{s/\delta}\), \(N=\lfloor X\rfloor\). The atoms counted in \(\nu_\delta([0,s])\) are exactly those with \(1\le n+1\le N\). Integral comparison, with the rounding bound \(0\le \log(X/N)\le\log2\) for \(X\ge2\) (and a direct bound if \(1\le X<2\)), establishes the uniform estimate
\[
\sum_{m=1}^{N}m^{-1-\delta}
=\frac{1-e^{-s}}{\delta}+O(1)
\quad\text{for all }s\ge0,\ 0<\delta\le1/2.
\]
Indeed the integral through \(N\) is \((1-N^{-\delta})/\delta\), its sum differs by at most one, and the rounding correction differs by at most \(\log2\). The uniform row-error bound from Step 2 then yields
\[
\sum_{n=0}^{N-1}E_n(\delta)
=\frac{C_\alpha(\delta)}{\delta}(1-e^{-s})+O_\alpha(1),
\]
where the remainder does not depend on \(s\). Divide by \(M_\delta=C_\alpha(\delta)/\delta+O_\alpha(1)\). Because \(C_\alpha(\delta)\) stays bounded above and below by positive constants, the resulting error is \(O_\alpha(\delta)\) *uniformly for all* \(s\ge0\). This proves the theorem.

## Verification
The standalone standard-library script `verify.py` evaluates \(S_n(-1/2)\) after removing its integrable endpoint singularity and checks it against the *analytically proved* beta-integral sandwich at three sample degrees. It also checks the known exact constant \(\Gamma(7/2)\Gamma(1/2)=15\pi/8\) and confirms approach of \(nE_n(0)/C_{-1/2}\) to one. The numerical tests are optional reproducibility checks; they do **not** replace the universal gamma-ratio, integral-comparison, or distribution proofs.

## Relationship to prior work
Songxiao Li and Mengmeng Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces* (arXiv:2610.05672; first public 2026-10-05), determine the boundedness/compactness/Schatten regimes and give an exact double series for the Hilbert--Schmidt norm. The matrix identities used here are consistent with that prior exact series. The present claim is not a new characterization of Hilbert--Schmidt membership: it is the **sharp, uniformly quantified law for the output-degree energy distribution at the endpoint**, including its exponential rescaling and critical logarithmic mass. These statements are not present in the inspected original text.

Generalized Hilbert operators in the earlier work of Peláez and Seco concern Schatten classifications on a single weighted analytic space, rather than the cross-weight differential-Hilbert row-energy crossover. Earlier studies of derivative-Hilbert operators on Dirichlet and Bergman spaces furnish related boundedness and compactness settings, without comparable distribution formulas in the accessible inspected material. Equivalence to an implicit older calculation cannot be categorically excluded; this is a residual historical-priority risk.

## Limitations
The theorem controls a basis-dependent output-row Hilbert--Schmidt energy distribution; it does not claim the singular-value distribution, eigenvalue asymptotics, or an operator-norm limit. The endpoint \(\delta=0\) is not Hilbert--Schmidt, although its finite output-row sums are well defined. Uniformity in \(\alpha\) near \(-1\) or \(0\) is not proved. Numerical checks only test finite cases. Independent mathematical validation has not been performed.

## References
1. S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672, first submitted 2026-10-05. https://arxiv.org/abs/2610.05672
2. J. Á. Peláez and J. Seco, *Schatten classes of generalized Hilbert operators*, arXiv:1510.05455, first submitted 2015-10-19. https://arxiv.org/abs/1510.05455
3. R. Xu, S. Ye and Z. Zhou, *A derivative-Hilbert operator acting on Dirichlet spaces*, Mathematics 2022, DOI:10.1515/math-2022-0559.
4. S. Ye and Z. Zhou, *A derivative-Hilbert operator acting on Bergman spaces*, Journal of Mathematical Analysis and Applications 506 (2022), 125553, DOI:10.1016/j.jmaa.2021.125553 (abstract accessible; complete text not materially inspected).
