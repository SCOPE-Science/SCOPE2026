# Disconnected contractive windows and an exact one-third-moment law for stochastic-gradient Leimkuhler–Matthews

## Finding

Consider the stochastic-gradient Leimkuhler–Matthews (SGLM) method on a scalar quadratic with two equally likely, strictly positive sample curvatures. Its random-coefficient evolution can be contractive in two *disconnected* intervals of positive stepsizes, including a second interval beyond the full-gradient linear stability range. In part of the first interval and throughout the second, the unique stationary marginal exists but has infinite second moment. Along the entire natural one-step-reset curve inside the second interval, the stationary marginal is a geometric mixture of centered Gaussians and has an explicit sharp moment threshold. At one rational point that threshold equals \(1/3\). These are exact statements about the specified scalar recurrence, not bounds for general SGLM.

Fix \(\lambda>0\), let \(1/\sqrt2<q<1\), and independently choose each sampled curvature as \(\lambda(1+q)\) or \(\lambda(1-q)\), with probability \(1/2\). Put \(t=h\lambda\) and define
\[
  t_{\mathrm{ms}}=\frac{2}{1+q^2},\qquad
  t_{\pm}=\frac{1\pm\sqrt{2q^2-1}}{1-q^2},\qquad
  t_{\mathrm{end}}=\frac{2}{1-q^2}.
\]
Then \(0<t_{\mathrm{ms}}<t_-<t_+<t_{\mathrm{end}}\). The homogeneous random recursion is almost-surely contractive exactly for
\[
  t\in(0,t_-)\cup(t_+,t_{\mathrm{end}}).
\]
At each such stepsize the full SGLM recurrence admits a unique strictly stationary one-time marginal. That marginal has finite second moment precisely if \(t<t_{\mathrm{ms}}\); in that range it has the exact variance
\[
  \operatorname{Var}(Z)=\frac{2-h\lambda}{2\lambda-h(\lambda^2+\lambda^2q^2)}
  =\frac1\lambda+\frac{hq^2}{2-h\lambda(1+q^2)}.
\]
In particular, the second contractive window consists entirely of stationary laws of infinite variance.

More generally, choose the **reset stepsize** \(h=1/[\lambda(1-q)]\) for any \(1/\sqrt2<q<1\), and define \(R=2q/(1-q)>1\). This stepsize lies in the second contractive window, and its sampled multipliers are \(0\) and \(-R\). With \(\Pr(K=k)=2^{-(k+1)}\), the stationary marginal has the exact law
\[
  Z\ \overset d=\ G\sqrt{\frac{h}{R+1}(R^{2K+1}+1)},
  \qquad \mathbb E|Z|^p<\infty
   \quad\Longleftrightarrow\quad
  0<p<\frac{\log2}{\log R}.
\]
The Gaussian \(G\sim N(0,1)\) is independent of \(K\). These formulas cover every point on the reset curve and include divergence at the critical exponent. In particular, at \(\lambda=1\), \(q=4/5\), and \(h=5\), the sampled update multipliers are precisely \(0\) and \(-8\). If \(K\) has \(\Pr(K=k)=2^{-(k+1)}\) for \(k=0,1,\ldots\), and \(G\) is an independent standard Gaussian, the stationary SGLM marginal has the explicit representation
\[
  Z\ \overset{d}{=}\ G\sqrt{\frac59\bigl(8\cdot64^K+1\bigr)}.
\]
For every real \(p>0\),
\[
  \boxed{\ \mathbb E|Z|^p<\infty\quad\Longleftrightarrow\quad p<\frac13.\ }
\]
Both stochastic-gradient sample losses remain strictly convex at this example: their curvatures are \(1/5\) and \(9/5\).

## Assumptions and scope

All random variables are real, and all computations are in exact arithmetic. Let \(U(z)=\lambda z^2/2\). At each step choose independently \(\varepsilon_n\in\{-1,1\}\) uniformly, and independently draw \(\chi_n\sim N(0,1)\). The unbiased gradient sample is \(g(z;\varepsilon_n)=\lambda(1+q\varepsilon_n)z\). The method, with constant \(h>0\), is
\[
  Z_{n+1}=[1-h\lambda(1+q\varepsilon_n)]Z_n
    +\sqrt{h/2}\,(\chi_n+\chi_{n+1}).
\]
The same Gaussian \(\chi_n\) is reused in two successive updates. A *stationary marginal* refers to \(Z_n\) in a strictly stationary version of the joint process with this Gaussian reuse; \(Z_n\) alone need not be Markov. Almost-sure contraction refers to decay of the difference between two copies driven by the same sequence of independent stochastic gradients and Gaussian variables.

## Proof

**1. Markov representation and contraction.** Write \(s=\sqrt{h/2}\), \(A_n=1-h\lambda(1+q\varepsilon_n)\), and \(Z_n=Y_n+s\chi_n\). Substitution (with the same \(\chi_n\) on both occurrences) gives exactly
\[
  Y_{n+1}=A_nY_n+s(A_n+1)\chi_n,\qquad
  Z_n=Y_n+s\chi_n.
\]
The pairs \((A_n,\chi_n)\) are independent and identically distributed across \(n\), and independent of \(Y_n\), which depends on preceding pairs only. For coupled initial states, \(Y_n-\widetilde Y_n=\prod_{j<n}A_j\,(Y_0-\widetilde Y_0)\). The strong law, interpreting \(\log 0=-\infty\), gives exponential almost-sure contraction when \(\mathbb E\log|A_0|<0\). In that regime an absolutely convergent backward affine series defines a unique stationary \(Y\), since the coefficients are bounded and the Gaussian innovations have finite logarithmic positive part; the same coupling establishes uniqueness and yields stationary \(Z=Y+s\chi\), with current \(\chi\) independent of \(Y\).

The two coefficients are \(A_+=1-(1+q)t\) and \(A_-=1-(1-q)t\), so
\[
  \mathbb E\log|A_0|=\frac12\log|A_+A_-|,\qquad
  A_+A_-=P_q(t)=1-2t+(1-q^2)t^2.
\]
Consequently almost-sure contraction holds exactly where \(|P_q(t)|<1\). The upper inequality \(P_q(t)<1\) reduces, for \(t>0\), to \(t<t_{\mathrm{end}}\). The lower inequality \(P_q(t)>-1\) reduces to
\[
 (1-q^2)t^2-2t+2>0.
\]
For \(1/\sqrt2<q<1\) this quadratic has two distinct positive roots \(t_-\) and \(t_+\), and is positive outside their closed interval. This proves the exact two-window contraction classification. It makes no assertion of nonexistence of invariant measures at the boundary or in the noncontractive gap.

**2. Exact second-moment frontier.** Since \(Y_n\) is independent of the present innovations and \(\mathbb E[(A+1)\chi]=0\), a stationary finite-second-moment solution must satisfy
\[
  \mathbb EY^2=\rho\,\mathbb EY^2+s^2\mathbb E(A+1)^2,
  \quad\rho=\mathbb EA^2=(1-t)^2+t^2q^2.
\]
The additive term is strictly positive for every \(h>0\). Hence no stationary \(Y\), and therefore no stationary \(Z=Y+s\chi\), can have finite second moment when \(\rho\ge1\). When \(\rho<1\), the series in step 1 converges in \(L^2\), and
\[
  \mathbb EZ^2=\mathbb EY^2+s^2
  =\frac{h(2-t)}{1-\rho}
  =\frac{2-t}{2\lambda-h\lambda^2(1+q^2)}.
\]
This is the displayed variance, with mean zero. The finite-variance criterion \(\rho<1\) is exactly \(0<t<t_{\mathrm{ms}}\). At \(t=t_{\mathrm{ms}}\),
\[
 |P_q(t)|=\left|1-\frac{8q^2}{(1+q^2)^2}\right|<1
\]
for the stipulated strict range of \(q\), and hence \(t_{\mathrm{ms}}<t_-\). Strict positivity and the order of the remaining endpoints are immediate from their root formulas. The bias identity follows by subtracting \(1/\lambda\) from the variance. Note that the full-gradient case \(q=0\) gives exactly \(1/\lambda\) wherever its stationary variance exists.

**3. The complete reset-curve stationary mixture.** Fix the reset stepsize \(h=1/[\lambda(1-q)]\). One sampled multiplier equals zero, while the other is \(-R\) with \(R=2q/(1-q)>1\), each with probability \(1/2\). Since their product vanishes, this is inside the almost-sure contraction region; since \(h\lambda>t_-\), it belongs to the *second* interval. There is a reset almost surely in any infinite past. Let \(K\) denote the number of consecutive \(-R\) multipliers immediately before a given time, counted back to the most recent \(0\). Then \(\Pr(K=k)=2^{-(k+1)}\). A reset gives \(Y=s\chi\), and each subsequent \(-R\) step transforms a centered Gaussian \(Y\) of variance \(v\) to one of variance \(R^2v+(R-1)^2s^2\). Thus \(\operatorname{Var}(Y\mid K=k)=s^2[(2R/(R+1))R^{2k}-(R-1)/(R+1)]\), and the fresh Gaussian shift yields \(\operatorname{Var}(Z\mid K=k)=h(R^{2k+1}+1)/(R+1)\). Specializing to \(\lambda=1,q=4/5,h=5\), where \(R=8\) and \(s^2=5/2\), this gives
\[
  \operatorname{Var}(Y\mid K=k)=s^2\left(\frac{16}{9}64^k-\frac79\right).
\]
Because the fresh \(\chi_n\) in \(Z_n=Y_n+s\chi_n\) is independent of the past, the conditional variance of \(Z\) is
\[
  \operatorname{Var}(Z\mid K=k)=\frac59(8\cdot64^k+1).
\]
This proves the Gaussian-mixture identity. For any \(p>0\), \(\mathbb E|G|^p=2^{p/2}\Gamma((p+1)/2)/\sqrt\pi\) is positive and finite, so
\[
  \mathbb E|Z|^p=\frac{2^{p/2}\Gamma((p+1)/2)}{\sqrt\pi}
  \sum_{k=0}^\infty2^{-(k+1)}
  \left[\frac59(8\cdot64^k+1)\right]^{p/2}.
\]
The general reset-curve term is comparable to \((R^p/2)^k\), establishing the exact threshold \(p<\log 2/\log R\) and divergence at equality; specializing to \(R=8\) gives \(p<1/3\). No continuous-tail power-law constant is asserted: the geometric mixture may have discrete-scale oscillations.

## Verification

Run `python verify.py` with Python 3 (standard library only). It checks 15,397 algebraic identities and seeded finite-sample assertions, including: the two-root phase classification at five strict curvature ratios; exact rational reset multipliers and conditional variances for run lengths through 34; equivalence of the original and Markovized recurrences on random inputs; and an 180,000-step Monte Carlo stationary-variance diagnostic inside the finite-moment interval. The run reports `VERIFY_OK`. All infinite-horizon and quantifier claims are established by the preceding proof, not by the tests.

## Relationship to prior work

Ye, Wang, Lin, and Kong (2026) introduce the SGLM recurrence, Gaussian reuse, Markov representation, and small-step sampling-bias results. Their bounded-*uniform-in-state* gradient-variance Assumption 3 and small-step conditions do **not** include the present gradient noise, whose variance is \(\lambda^2q^2z^2\), or the large-step reset example. No contradiction with their theorem is claimed. The underlying affine-recursion contraction criterion and the possibility of heavy tails under multiplicative noise are classical; in particular, Hodgkinson and Mahoney (2021) and Gürbüzbalaban, Şimşekli, and Zhu (2021) study this mechanism in SGD. The contribution here is the method-specific **disconnected, exact timestep windows** and the **explicit full reset-curve Gaussian-mixture and moment-cutoff formula** for the recycled-noise SGLM method, with strictly convex individual sample losses. The generic prior results do not state this coefficient geometry or exact lattice-reset distribution.

## Limitations

Only scalar quadratics, independent symmetric two-point sample curvatures, Gaussian reuse as defined above, and exact arithmetic are covered. The result classifies almost-sure **contraction** and stationary laws *inside* its two strict windows; it does not prove absence of other stationary laws outside those windows. Infinite variance is not a claim of nonexistence of a stationary probability measure. Large steps in the second window should not be interpreted as accurate sampling of the target Gaussian law. The continuous-time Langevin sampler, multidimensional curvatures, finite-step weak accuracy, full numerical implementation, and singular boundary cases are not classified. General affine-recursion theory may subsume the qualitative contraction or heavy-tail mechanism; historical priority for the precise SGLM specialization remains open.

## References

1. X. Ye, Y. Wang, G. Lin, C. X. Kong, *Stochastic Gradient Leimkuhler–Matthews Integrator with Second Order Discretization Error*, arXiv:2610.24781v1, publicly posted 2026-10-17, especially (SGLM), Assumption 3, Section 3.2, and Theorem 3. https://arxiv.org/html/2610.24781v1
2. L. Hodgkinson and M. W. Mahoney, *Multiplicative Noise and Heavy Tails in Stochastic Optimization*, Proceedings of Machine Learning Research 139 (2021), 4262–4274, Sections 2–4. https://proceedings.mlr.press/v139/hodgkinson21a.html
3. M. Gürbüzbalaban, U. Şimşekli, L. Zhu, *The Heavy-Tail Phenomenon in SGD*, Proceedings of Machine Learning Research 139 (2021), 3964–3975, especially Section 3. https://proceedings.mlr.press/v139/gurbuzbalaban21a.html
