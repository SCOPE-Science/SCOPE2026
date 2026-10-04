# Exact lower-tail phase diagram for the three-sample Beta variance
## Finding
Let \(X_1,X_2,X_3\) be independent with common \(\operatorname{Beta}(\alpha,\beta)\) law, where \(\alpha,\beta>0\). Define the unbiased three-sample variance
\[
S^2=\frac12\sum_{i=1}^3(X_i-\bar X)^2
\]
and its lower-tail distribution \(F_{\alpha,\beta}(y)=\Pr\{S^2\le y\}\). Put \(m=\min(\alpha,\beta)\) and \(B=B(\alpha,\beta)\). Let \(k=1\) if only one of \(\alpha,\beta\) equals \(m\), and \(k=2\) if \(\alpha=\beta=m\).

As \(y\downarrow0\), there are exactly three leading regimes:
\[
F_{\alpha,\beta}(y)\sim
\begin{cases}
\displaystyle \frac{2\sqrt3\,\pi\,B(3\alpha-2,3\beta-2)}{B(\alpha,\beta)^3}\,y, & m>2/3,\\[1.1em]
\displaystyle \frac{k\sqrt3\,\pi}{B(\alpha,\beta)^3}\,y\log(1/y), & m=2/3,\\[1.1em]
\displaystyle \frac{kJ_m}{B(\alpha,\beta)^3}\,y^{3m/2}, & 0<m<2/3,
\end{cases}
\]
where
\[
J_m=\int_{\{u_i\ge0:\,\frac12\sum_{i=1}^3(u_i-\bar u)^2\le1\}}(u_1u_2u_3)^{m-1}\,du_1du_2du_3.
\]
The integral \(J_m\) is finite exactly when \(0<m<2/3\). Consequently, the ordinary linear small-variance law holds precisely when both endpoint exponents exceed \(2/3\); at the threshold a logarithm appears; and below the threshold the more singular endpoint determines the power, with a factor of two when the endpoint exponents tie.

## Assumptions and scope
The theorem concerns exactly three i.i.d. observations, the unbiased sample-variance normalization above, fixed positive Beta parameters, and the limit \(y\downarrow0\). The Beta density is
\[
f(x)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},\qquad 0<x<1.
\]
No assertion is made here for sample sizes other than three or for a parameter sequence varying with \(y\).

For the subcritical constant an equivalent simplex representation is
\[
J_m=\frac1{3m}\int_{\Delta_2}(p_1p_2p_3)^{m-1}
\left[\frac12\sum_{i=1}^3\left(p_i-\frac13\right)^2\right]^{-3m/2}\,dp_1dp_2,
\]
where \(p_i\ge0\) and \(p_1+p_2+p_3=1\).

## Proof
Use orthogonal coordinates around the main diagonal:
\[
X_1=t+\frac{\xi_1}{\sqrt2}+\frac{\xi_2}{\sqrt6},\quad
X_2=t-\frac{\xi_1}{\sqrt2}+\frac{\xi_2}{\sqrt6},\quad
X_3=t-\frac{2\xi_2}{\sqrt6}.
\]
Then \(t=\bar X\),
\[
S^2=\frac{\xi_1^2+\xi_2^2}2,
\]
and the Euclidean volume element is \(dX_1dX_2dX_3=\sqrt3\,dt\,d\xi_1d\xi_2\). Thus \(S^2\le y\) is a tube of transverse radius \(\sqrt{2y}\) around the diagonal.

When \(\alpha,eta>2/3\), \(f^3\) is integrable. Away from the two endpoints the tube cross-section contributes
\[
2\sqrt3\,\pi y\int_0^1 f(t)^3\,dt+o(y).
\]
The endpoint pieces are \(o(y)\), because their masses are respectively of orders \(y^{3\alpha/2}\) and \(y^{3\beta/2}\). Since
\[
\int_0^1 f(t)^3\,dt=\frac{B(3\alpha-2,3\beta-2)}{B(\alpha,\beta)^3},
\]
the regular-regime constant follows.

Suppose next that \(m=2/3\). Near a critical endpoint, the product of the three densities along the diagonal is asymptotic to \(B(\alpha,\beta)^{-3}t^{-1}\). Integrating the transverse area \(2\pi y\) from the tube scale \(t\asymp\sqrt y\) to a fixed small cutoff gives
\[
2\sqrt3\,\pi y B(\alpha,\beta)^{-3}\int_{c\sqrt y}^\varepsilon\frac{dt}t
=\frac{\sqrt3\,\pi}{B(\alpha,\beta)^3}y\log(1/y)+O(y)
\]
per critical endpoint. The corner layer itself is only \(O(y)\), and every noncritical region is also \(O(y)\), proving the stated factor \(k\).

Finally suppose \(0<m<2/3\), first with \(m=\alpha<\beta\). Localize to the lower endpoint and set \(X_i=\sqrt y\,u_i\). Homogeneity gives \(S^2(X)=yS^2(u)\), while the density product times volume converges to
\[
B(\alpha,\beta)^{-3}y^{3\alpha/2}(u_1u_2u_3)^{\alpha-1}\,du_1du_2du_3.
\]
Hence the lower corner contributes \(B(\alpha,\beta)^{-3}J_\alpha y^{3\alpha/2}\). In simplex coordinates \(u_i=sp_i\), the radial integral is
\[
\int_0^{1/\sqrt{S^2(p)}}s^{3m-1}\,ds=\frac1{3m}S^2(p)^{-3m/2}.
\]
Near the simplex center, \(S^2(p)\) is quadratic in distance, so the remaining two-dimensional integral behaves as \(\int r^{1-3m}dr\), finite exactly for \(m<2/3\). Face singularities are integrable because \(m>0\). The upper endpoint and tube interior have strictly smaller order when \(\beta>\alpha\). The case \(\beta<\alpha\) is symmetric, and when \(\alpha=\beta=m\) the two disjoint endpoint neighborhoods contribute equally, producing the factor \(k=2\).

## Verification
The normalization bridge to the closest exact predecessor gives a stringent constant check. Royen's Theorem 3 treats the pure-power density \(f_p(x)=px^{p-1}\) and \(Q=2S^2\). At \(n=3\) and \(p=2/3\), his critical constant is \(4\pi\sqrt3/27\) for \(F_Q(x)\sim Cx\log(1/x)\). Substitution \(x=2y\) therefore gives \(8\pi\sqrt3/27\) for \(S^2\). The present critical formula for \(\operatorname{Beta}(2/3,1)\), where \(B(2/3,1)=3/2\), gives exactly the same value.

The accompanying deterministic checker verifies this normalization identity, the uniform-parent regular constant, and the exponent ordering on both sides of the threshold. These computations check constants and normalizations; the asymptotic theorem itself rests on the analytic localization proof above, not on finite numerical experiments.

## Relationship to prior work
Osan, Chu, and Yu (2026) study the exact distribution of the sample variance for three observations, including singular parents. Their arcsine example exhibits a lower-tail power \(y^{3/4}\) with a numerically evaluated leading coefficient, while their general Beta discussion emphasizes other endpoint structure. The theorem above explains the arcsine exponent as the tied-endpoint case \(m=1/2\) and identifies the exact coefficient as \(2J_{1/2}/B(1/2,1/2)^3\).

Royen (2008) is the decisive predecessor for the small-variance singularity. His Theorem 3 proves the exact one-sided pure-power phase transition for \(f_p(x)=px^{p-1}\), including the critical logarithm when \(np=n-1\). Therefore the threshold \(2/3\), the pure-power exponent, and its critical constant are not claimed as new. The assessed contribution here is the exact transfer to the full two-endpoint \(\operatorname{Beta}(\alpha,\beta)\) family for \(n=3\): the regular \(f^3\) constant, the critical endpoint-count coefficient, the subcritical corner integral, and the rule for competition or addition of the two endpoints.

## Limitations
This is a first-order lower-tail theorem. It does not provide second-order terms, a closed form for \(J_m\) in general, or a finite-sample error bound. In particular, for the arcsine parent the representation of the leading constant by \(J_{1/2}\) does not by itself simplify that constant to elementary or standard special functions.

The closest prior theorem already contains the critical mechanism for a one-sided pure-power density, so the originality claim is deliberately narrow. A broader regular-variation theorem for small sample variance under a different formulation could subsume parts of the localization argument; no such statement was located in the checked literature or the published-finding searches.

## References
1. R. Osan, K. T. Chu, and R. Yu, “Closed forms and open obstructions: the sample variance of three observations,” arXiv:2609.25333, first public version 2026-09-21.
2. T. Royen, “The exact distribution of the sample variance from bounded continuous random variables,” arXiv:0810.1572, 2008; especially Theorem 3 and the endpoint-singular density classes in Section 3.
