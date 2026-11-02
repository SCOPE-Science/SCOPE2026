# Probe averaging can reverse almost-sure stability in Gaussian zeroth-order descent

## Finding
Consider independent fresh Gaussian directions in the centered two-point zeroth-order gradient estimator for the scalar quadratic \(f(x)=\lambda x^2/2\), where \(\lambda>0\). When each iteration averages \(n\) directions and the dimensionless step size is \(a=\eta\lambda>0\), the exact iterate multiplier is \(1-aY_n\), where \(Y_n\) has the \(\chi^2_n/n\) distribution. Define the logarithmic gain \(F_n(a)=\mathbb E\log|1-aY_n|\). For any nonzero initialization, \(F_n(a)<0\) implies almost-sure exponential convergence to zero, while \(F_n(a)>0\) implies almost-sure exponential divergence in magnitude.

**Exact finite-probe reversal.** At the rational step size \(a=107/40\), the two-probe iteration converges almost surely, but the four-probe iteration diverges almost surely:
\[
F_2(107/40)<0< F_4(107/40).
\]
This reverses the ordering suggested by the monotone improvement of the mean-square stability threshold with additional probes. The two exact logarithmic gains are
\[
F_2(a)=-e^{-1/a}\operatorname{Ei}(1/a),\qquad
F_4(a)=1-(1+2/a)e^{-2/a}\operatorname{Ei}(2/a),
\]
where \(\operatorname{Ei}(z)=\gamma+\log z+\sum_{j\ge1}z^j/(j\,j!)\) for \(z>0\). Each has exactly one positive root, respectively \(a_2=2.684510350820707\ldots\) and \(a_4=2.662995668706913\ldots\). Thus adding two Gaussian probes can shrink the almost-sure stable step-size interval, even on a strongly convex one-dimensional quadratic.

**Large-probe separation.** For every bounded real \(c\), uniformly on compact sets of \(c\),
\[
F_n(2+c/n)=\frac{c-4}{n}+O(n^{-2})\qquad(n\to\infty).
\]
Consequently, for all sufficiently large integers \(n\), a locally unique zero \(a_n\) exists in \((2+3/n,2+5/n)\) and satisfies \(a_n=2+4/n+O(n^{-2})\). The exact mean-square stability boundary is \(b_n=2n/(n+2)=2-4/n+O(n^{-2})\); hence \(a_n-b_n=8/n+O(n^{-2})\). No global uniqueness or monotonicity in \(n\) is claimed for the large-probe zeros.

## Assumptions and scope
For each integer \(n\ge1\), take independent \(U_{t,j}\sim N(0,1)\), independent over iteration index \(t\) and probe index \(j\). At iteration \(t\), average \(n\) centered two-point estimators with any fixed smoothing radius \(\mu>0\); for the stated quadratic the central difference is exactly \(\lambda x_tU_{t,j}^2\), independent of \(\mu\). Apply the constant positive step \(\eta\) to obtain
\[
x_{t+1}=\left(1-\frac{a}{n}\sum_{j=1}^{n}U_{t,j}^2\right)x_t.
\]
All statements use exact arithmetic, fixed finite \(n\) followed by iteration time tending to infinity, or a separate \(n\to\infty\) asymptotic. They address pathwise behavior for every fixed \(x_0\ne0\), not finite-time high-probability sample complexity, expected-iterate convergence, or general nonlinear objectives.

## Proof
**1. Logarithmic criterion.** The multipliers are independent and identically distributed across iterations, continuous with no atoms at zero, and \(\mathbb E|\log|1-aY_n||<\infty\) for every \(a>0\): the logarithmic singularity is integrable against the gamma density and its far tail grows only logarithmically. The strong law gives \(t^{-1}\log|x_t/x_0|\to F_n(a)\) almost surely. This proves the asserted strict-sign implications. Separately, \(\mathbb E[x_{t+1}^2\mid x_t]=[1-2a+a^2(1+2/n)]x_t^2\), because \(\mathbb E Y_n=1\) and \(\mathbb E Y_n^2=1+2/n\). Its strict mean-square stability interval is exactly \(0<a<2n/(n+2)\).

**2. Two- and four-probe closed forms.** If \(Y_2\sim\operatorname{Gamma}(1,1)\), direct integration, with the variable \(z=1/a\), gives \(F_2(a)=-e^{-z}\operatorname{Ei}(z)\). If \(Y_4\sim\operatorname{Gamma}(2,2)\), put \(w=2/a\). Integration against \(s e^{-s}\,ds\), or differentiation of its logarithmic potential followed by the normalization at \(w=0\), gives \(F_4(a)=1-(1+w)e^{-w}\operatorname{Ei}(w)\). The expansions are valid for every real \(a>0\), not merely near the roots.

For \(n=2\), \(\operatorname{Ei}'(z)=e^z/z>0\) on the positive axis, with limits \(-\infty\) and \(+\infty\), so \(F_2\) has exactly one positive zero. For \(n=4\), write \(K(w)=(1+w)e^{-w}\operatorname{Ei}(w)\). At any zero of \(1-K(w)\), \(K(w)=1\) and
\[
K'(w)=-w e^{-w}\operatorname{Ei}(w)+\frac{1+w}{w}
=\frac{1+2w}{w(1+w)}>0.
\]
Furthermore \(F_4(a)\to0^-\) as \(a\downarrow0\), whereas \(F_4(a)\to+\infty\) as \(a\to\infty\). Each zero therefore crosses from negative to positive as \(a\) increases, so there can be exactly one. The same small-step and large-step signs hold for \(F_2\).

The decisive signs at \(a=107/40\) admit elementary rigorous rational enclosures. Use \(\gamma\in(0.5772156649,0.5772156650)\), the positive-term series for \(\operatorname{Ei}(z)-\gamma-\log z\), and
\[
\log z=2\sum_{j=0}^{30}\frac{t^{2j+1}}{2j+1}+R,
\quad t=\frac{z-1}{z+1},\quad
|R|\le\frac{2|t|^{63}}{63(1-t^2)}.
\]
For \(0<z<1\), truncating the exponential-integral series after index 16 leaves a remainder between zero and \(3z^{17}/(17\cdot17!)\). For \(e^{-z}\), alternating Taylor sums of orders 19 and 20 enclose its value. Applied to \(z=40/107\), these estimates certify \(\operatorname{Ei}(z)>0.00515427079\), hence \(F_2(107/40)<0\). Applied to \(z=80/107\), they certify \(1-(1+z)e^{-z}\operatorname{Ei}(z)>0.00642896092\), hence \(F_4(107/40)>0\). The standalone verifier constructs the rational enclosures without invoking floating-point special functions for either decisive sign.

**3. Large-probe expansion.** Let \(\delta_n=Y_n-1\), so \(\mathbb E\delta_n=0\), \(\mathbb E\delta_n^2=2/n\), \(\mathbb E\delta_n^3=8/n^2\), and \(\mathbb E\delta_n^4=12/n^2+48/n^3\). For \(a=2+c/n\), on the event \(|\delta_n|\le1/4\) and for any fixed bounded range of \(c\),
\[
\log|1-aY_n|=\log\left[1+\frac cn+(2+\frac cn)\delta_n\right].
\]
The logarithm is analytic in its argument throughout this event for all sufficiently large \(n\). Taylor's formula through degree four, together with the displayed central moments and \(\mathbb E|\delta_n|^5=O(n^{-5/2})\), gives \(F_n(2+c/n)=(c-4)/n+O(n^{-2})\). The complement has exponentially small gamma probability; its contribution remains exponentially small even after the logarithmic singularity near \(Y_n=1/a\) is included, by splitting there and using local integrability and gamma density bounds. These bounds are uniform for \(c\) in compact intervals.

The same localized argument applied to the derivative of the logarithmic potential (interpreting the exponentially small singular-tail term by a principal value) gives \(F_n'(2+c/n)=1+O(n^{-1})\) uniformly for \(3\le c\le5\). The expansion gives opposite signs at \(c=3\) and \(c=5\) when \(n\) is large, and the derivative is positive there, so exactly one root lies between them. Evaluating at \(c=4\) and using the derivative lower bound places that root within \(O(n^{-2})\) of \(2+4/n\). Finally, expanding \(2n/(n+2)\) completes the stated gap.

## Verification
Run `python verify.py` with Python, `mpmath`, and `scipy`. The program independently computes two exact rational sign enclosures from truncated convergent series, checks the root brackets and normalized gamma integrals, and checks the independent mean-square formula. Its 21 assertions passed on the delivered source version. The analytical proof, not the numerical root finder or numerical quadrature, establishes the strict inequalities and asymptotic claims. In particular finite numerical evidence does not establish a general assertion about all probe counts.

## Relationship to prior work
Song, Zhang, Li, He, Muehlebach, and Oh (2026), Appendix B.3, derive precisely the averaged Gaussian two-point estimator and its mean-square covariance operator; their analysis shows that larger probe counts improve the mean-square threshold. Their inspected formulation does not give logarithmic Lyapunov exponents or a two-versus-four probe almost-sure reversal. Ziyin, Li, Galanti, and Ueda (2023) establish the broader relevance of Lyapunov exponents for probabilistic stability of multiplicative stochastic optimization; the logarithmic-sign criterion itself is not claimed new here. An earlier scalar Gaussian LMS calculation gives an already-known one-probe threshold near \(2.42125\), excluded from the claim. The contribution is the exact nonmonotonic probe comparison and the first-order asymptotic splitting of pathwise and mean-square boundaries for the specified averaged estimator.

## Limitations
The self-review is not an independent validation. The exact finite reversal is for two versus four probes and is not a claim about all adjacent probe counts. The large-probe theorem identifies a locally unique crossing near the deterministic step \(a=2\), not necessarily a globally unique stability boundary for arbitrary \(n\). The numerical root values are informational; strict signs use rational enclosures. All conclusions are scalar and require independent real Gaussian directions at each update. Historical priority beyond inspected and searched sources is not exhaustively certified.

## References
1. M. Song, L. Zhang, B. Li, N. He, M. Muehlebach, S. Oh. *Zeroth-Order Optimization at the Edge of Stability*, arXiv:2604.14669v1 (first public April 16, 2026), especially Appendix B.3. https://arxiv.org/html/2604.14669v1
2. L. Ziyin, B. Li, T. Galanti, M. Ueda. *Type-II Saddles and Probabilistic Stability of Stochastic Gradient Descent*, arXiv:2303.13093 (2023). https://arxiv.org/abs/2303.13093
3. *For which values of step size is LMS filter stable?*, Math Stack Exchange (2023), earlier scalar one-probe Gaussian calculation. https://math.stackexchange.com/
