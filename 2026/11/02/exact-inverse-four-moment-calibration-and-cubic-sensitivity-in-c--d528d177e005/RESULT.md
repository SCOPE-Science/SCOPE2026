# Exact inverse four-moment calibration and cubic sensitivity in cyclic Erlang phase-type models

## Finding

Fix an integer \(s\geq3\). Consider an \(s\)-phase continuous-time Markov model: begin in phase 1, advance sequentially through phases 2 to \(s\), wait for an independent exponential holding time of rate \(\lambda>0\) in each phase, and at the end of phase \(s\) either absorb with probability \(1-p\) or return to phase 1 with probability \(p\), where \(0\leq p<1\). Let \(T\) denote its absorption time, \(\mu_j=\mathbb E[T^j]\), and define the scale-free four-moment calibration statistic
\[
R_s(p)=\frac{\mu_2\mu_4}{\mu_3^2}.
\]
Then \(R_s\) is strictly increasing, independently of \(\lambda\), and maps \([0,1)\) bijectively onto
\[
\left[\frac{s+3}{s+2},\frac43\right).
\]
Thus every target \(r\) in this interval determines exactly one feedback probability \(p\); a given positive mean \(m\) then determines the unique holding rate \(\lambda=s/[m(1-p)]\). A moment quadruple is a full fit only when its remaining moment equations also agree with these recovered parameters. In fact the lower-order ratio has the simpler identity \(\mu_2/\mu_1^2=2-(s-1)(1-p)/s\); hence the cubic instability is specific to fourth-moment-ratio inversion, not to optimal identification from all available moments. Moreover, with \(K_s=(s^2-1)/(18s^3)\),
\[
\frac43-R_s(p)=K_s(1-p)^3+O((1-p)^4),\qquad p\uparrow1,
\]
and the inverse sensitivity obeys
\[
\frac{dp}{dr}\sim\frac{1}{3K_s^{1/3}}\left(\frac43-r\right)^{-2/3}
\quad\text{as }r\uparrow\frac43.
\]
For \(0<p<1\) these absorption laws have genuine cyclic representations and no finite acyclic phase-type representation. The inverse-calibration statement is for the specified cyclic Erlang-feedback family, not arbitrary phase-type distributions.

## Assumptions and scope

All phase holding times are independent and identically distributed \(\operatorname{Exp}(\lambda)\); decisions to return after completing each \(s\)-phase circuit are independent with common probability \(p\). The stage count \(s\geq3\) is known, and parameters are \((p,\lambda)\in[0,1)\times(0,\infty)\). Moments are raw moments and finite for every admitted parameter. We require \(\mu_3>0\), automatically satisfied. Inversion of \(R_s\) and the mean does not claim that an arbitrary four-moment target lies on the two-parameter moment manifold.

## Proof

Let \(N\) be the number of complete circuits before absorption. It has geometric law \(\Pr(N=n)=(1-p)p^{n-1}\) for \(n\ge1\). Conditional on \(N=n\), \(T\) is the sum of \(sn\) independent exponential holding times. Consequently, for \(t\) near zero,
\[
M_T(t)=\mathbb E e^{tT}=\frac{1-p}{(1-t/\lambda)^s-p}.
\]
Write \(x=p/(1-p)\ge0\). Coefficient comparison through degree four in this rational moment-generating function yields
\[
\mu_1=\frac{s(1+x)}{\lambda},\qquad
\mu_j=\frac{s(1+x)B_j(x)}{\lambda^j}\quad(j=2,3,4),
\]
where
\[
\begin{aligned}
B_2&=s+1+2sx,\\
B_3&=(s+1)(s+2)+6s(s+1)x+6s^2x^2,\\
B_4&=(s+1)(s+2)(s+3)+2s(s+1)(7s+11)x\\
&\qquad+36s^2(s+1)x^2+24s^3x^3.
\end{aligned}
\]
The factors of \(\lambda\) and \(s(1+x)\) cancel in the ratio, giving
\[
R_s(p)=F_s(x):=\frac{B_2(x)B_4(x)}{B_3(x)^2}.
\]
An exact expansion of its derivative yields
\[
F_s'(x)=\frac{2s(s-1)(s+1)Q_s(x)}{B_3(x)^3},
\]
with
\[
Q_s(x)=18s^2x^2+(4s^3+18s^2+14s)x+(2s^3+7s^2+7s+2).
\]
Every coefficient of \(Q_s\) is positive for \(s\ge3\); also \(B_3(x)>0\) for \(x\ge0\). Thus \(F_s'\) is positive, and \(x=p/(1-p)\) increases strictly with \(p\). At \(x=0\), direct substitution gives \(F_s(0)=(s+3)/(s+2)\), while comparison of the leading degrees gives \(\lim_{x\to\infty}F_s(x)=4/3\). Strict monotonicity and continuity prove the exact image and uniqueness of inversion. The mean formula then recovers \(\lambda\) uniquely.

For sensitivity, divide the numerator and denominator in \(F_s'\) by their leading powers of \(x\). This gives
\[
F_s'(x)=\frac{s^2-1}{6s^3}x^{-4}+O(x^{-5}).
\]
Since \(F_s(x)\to4/3\), integrating from \(x\) to infinity gives
\[
\frac43-F_s(x)=\frac{s^2-1}{18s^3}x^{-3}+O(x^{-4}).
\]
Finally, \(x^{-1}=(1-p)/p\) and \(p\uparrow1\) yield the claimed cubic law. Differentiation and inversion show \(dp/dr\sim[3K_s^{1/3}]^{-1}(4/3-r)^{-2/3}\). Equivalently, \(1-p\sim[(4/3-r)/K_s]^{1/3}\).

To show genuine cyclicity, the Laplace transform has denominator \((\lambda+u)^s-p\lambda^s\). For \(p>0\) and \(s\ge3\), its zeros include nonreal values \(u=\lambda(p^{1/s}\zeta-1)\), with \(\zeta^s=1\) a nonreal root of unity. The numerator is nonzero, so these are genuine poles. A finite acyclic phase-type generator can be ordered triangular with real negative diagonal, hence its Laplace transform can have only real poles. Thus no such acyclic representation exists for these laws.

## Verification

The accompanying standard-library-only `VERIFIER.py` checks the four moments by a Taylor-coefficient recurrence independently of the displayed closed formulas, exact rational evaluations of \(F_s\), and the expanded derivative identity for \(s=3,\ldots,24\) at multiple rational values of \(x\). It reports 132 exact-rational moment cases, additional derivative checks, and no failed assertions. The universal proof is the displayed rational-function identity plus coefficient positivity; these finite checks are not used as a substitute for that proof. No stochastic simulation, fitting convergence certificate, or floating-point claim is required.

## Relationship to prior work

Sherzer, Resheff and Telek (2025), *An Unconstrained Optimization Approach to Moment Fitting with Phase Type Distributions*, develop approximate multi-moment fitting through nonconvex numerical optimization over broad PH parameterizations. They do not give this exact one-parameter cyclic inversion or its cubic inverse-conditioning law. He, Horváth, Horváth and Telek (2019), *Moment bounds of PH distributions with infinite or finite support based on the steepest increase property*, establish broad stochastic/moment bounds in terms of representation dimension and dominant eigenvalue; these do not identify the feedback parameter from the second, third and fourth raw moments. Classical Erlang mixture and PH moment formulas underpin the calculation and are not claimed as new. Yu, Zhu and Weng (2026), *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, give general low-order moment-ratio bounds and the higher-order acyclic case, while reporting a higher-order cyclic case as open in general. The present complete inverse formula concerns only the specified homogeneous feedback cycle. Discovery of an equivalent older specialized Erlang-feedback calibration formula would alter the priority assessment.

## Limitations

The number of stages is fixed; unknown \(s\) is not identified by this result. Heterogeneous phase rates, branching graphs, arbitrary initial phase distributions and general cyclic generators are excluded. Only the stated scale-invariant ratio and mean are guaranteed to fit any target in the calibration range; the entire moment quadruple may be incompatible. The simpler ratio \(\mu_2/\mu_1^2\) determines \(p\) affinely whenever the first two moments are reliable. The cubic sensitivity describes inversion using \(R_s\) alone and must not be interpreted as an intrinsic statistical conditioning barrier for every estimator. Near \(p=1\), the ratio becomes cubically flat, so finite-precision or statistical inversion is ill-conditioned. The theorem does not supply confidence intervals, finite-sample error bars, guarantees for general PH optimizers, or a universal higher-order moment inequality.

## References

1. E. Sherzer, Y. Resheff and M. Telek, *An Unconstrained Optimization Approach to Moment Fitting with Phase Type Distributions*, arXiv:2505.20379, first public 2025-05-26, https://arxiv.org/abs/2505.20379.
2. Q.-M. He, G. Horváth, I. Horváth and M. Telek, *Moment bounds of PH distributions with infinite or finite support based on the steepest increase property*, *Advances in Applied Probability* 51 (2019), 168–183, DOI:10.1017/apr.2019.7; author manuscript https://webspn.hit.bme.hu/~telek/cikkek/he18a.pdf.
3. H. Yu, Q. Zhu and Z. Weng, *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, arXiv:2610.37425, 2026, https://arxiv.org/abs/2610.37425.
