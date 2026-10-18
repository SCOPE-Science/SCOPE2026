# Correlated patch catastrophes: stochastic persistence ordering and a sharp variance peak

## Finding
Consider two identical habitat patches, initially both occupied, subject to the patch-occupancy process defined below. Fix the marginal local-extinction intensity \(m>0\), the directional recolonization rate \(\lambda\ge0\), and vary the simultaneous-catastrophe intensity \(0\le c\le m\). Let \(T_c\) be the first time neither patch is occupied. Then for every \(t>0\) and \(0\le c_0<c_1\le m\),
\[
\Pr(T_{c_1}>t)<\Pr(T_{c_0}>t).
\]
Indeed, writing \(p_{2,c}(t)\) for the probability that both patches remain occupied at time \(t\) without prior global extinction, the entire survival curve satisfies
\[
\frac{\partial}{\partial c}\Pr(T_c>t)
=-\int_0^t p_{2,c}(u)p_{2,c}(t-u)\,du<0.
\]
Nevertheless the **absolute** extinction-time variance need not decrease with correlated catastrophes. It initially *increases* with \(c\) exactly when
\[
0\le\lambda/m<\sqrt5-2.
\]
In that regime it has a unique strict global maximum on \([0,m]\), attained at
\[
c_* =\frac{m^2-4m\lambda-\lambda^2}{2(m-\lambda)}\in(0,m).
\]
For \(\lambda/m\ge\sqrt5-2\), absolute variance is strictly decreasing on \((0,m)\), with a horizontal tangent at \(c=0\) only at equality. For every \(\lambda\ge0\), the squared coefficient of variation increases strictly for \(0\le c<m\), reaching \(1\) at \(c=m\). For each \(c<m\), \(T_c\) has a strictly increasing failure hazard in elapsed time; at \(c=m\) its hazard is the constant \(m\).

## Assumptions and scope
Each patch is either occupied or empty. Each occupied patch suffers independent local-extinction events at intensity \(m-c\). A single common Poisson disaster process of intensity \(c\), independent of the local processes, simultaneously empties all occupied patches. Thus the marginal instantaneous extinction intensity of a single occupied patch is always \(m\), regardless of \(c\). When exactly one patch is occupied, the empty patch is recolonized at intensity \(\lambda\), and recolonization does not occur from an empty metapopulation. All clocks are exponential and independent except for the stipulated shared disaster. Both patches start occupied. Time is continuous, and global extinction is absorbing. The claim is about a two-patch occupancy abstraction, not population size, nonexponential catastrophe durations, or real-world extinction forecasting.

Aggregating the states by number of occupied patches gives the transient generator (ordered states \(2,1\))
\[
Q_c=\begin{pmatrix}-(2m-c)&2(m-c)\ \lambda&-(m+\lambda)\end{pmatrix}.
\]
The transition to extinction has rate \(c\) from state \(2\) and rate \(m\) from state \(1\). At \(c=m\), the population goes directly from two occupied patches to extinction at intensity \(m\).

## Proof
**(1) Resolvent and exact distributional sensitivity.** Define \(S_c(t)=\Pr(T_c>t)\), \(p_{2,c}(t)=(e^{Q_ct})_{11}\), and \(K_c=2m^2+c(\lambda-m)>0\). The generator resolvent, with Laplace variable \(s>0\), gives
\[
D_c(s)=s^2+(3m+\lambda-c)s+K_c,
\quad \widehat{S}_c(s)=\frac{s+3m+\lambda-2c}{D_c(s)},
\quad\widehat{p}_{2,c}(s)=\frac{s+m+\lambda}{D_c(s)}.
\]
Differentiating the first rational function at fixed \(s\), cancelling the terms in \(c\), yields the exact identity
\[
\partial_c\widehat{S}_c(s)
=-\frac{(s+m+\lambda)^2}{D_c(s)^2}
=-\widehat{p}_{2,c}(s)^2.
\]
Finite-dimensional matrix exponentials are analytic in \(c\), locally uniformly on compact time intervals. Uniqueness of Laplace transforms and the convolution theorem therefore give the stated time-domain sensitivity identity. Since \(p_{2,c}(u)\ge e^{-(2m-c)u}>0\), its convolution is strictly positive for every \(t>0\). Integration in \(c\) proves the strict survival ordering, including endpoints by continuity. Stochastic ordering is stronger than comparison of expected extinction times or Laplace transforms alone.

**(2) Moments and the sharp variance switch.** The Laplace transform of \(T_c\) is
\[
\mathbb E[e^{-sT_c}]
=1-s\widehat S_c(s)
=\frac{K_c+cs}{D_c(s)}.
\]
Differentiation at \(s=0\) produces
\[
\mathbb E[T_c]=\frac{3m+\lambda-2c}{K_c},
\qquad
\operatorname{Var}(T_c)=\frac{(m+\lambda)(5m+\lambda-4c)}{K_c^2},
\]
and hence
\[
\frac{\partial}{\partial c}\mathbb E[T_c]
=-\frac{(m+\lambda)^2}{K_c^2}<0,
\]
\[
\frac{\partial}{\partial c}\operatorname{Var}(T_c)
=\frac{2(m+\lambda)[m^2-4m\lambda-\lambda^2-2c(m-\lambda)]}{K_c^3}.
\]
The last derivative has the sign of an affine function of \(c\), whose value at \(c=m\) is \(-(m+\lambda)^2<0\). Its value at \(c=0\) is positive exactly when \(0\le\lambda/m<\sqrt5-2\). In that case \(\lambda<m\), so the affine numerator decreases strictly and has exactly one zero \(c_*\) inside \((0,m)\); positivity of \(c_*\) follows from the threshold, and \(c_*<m\) follows by subtracting its numerator from \(2m(m-\lambda)\), obtaining \((m+\lambda)^2>0\). Otherwise the numerator is negative for every \(0<c\le m\) (possibly vanishing only at \(c=0\)). This proves the complete absolute-variance classification.

For relative variance, one has
\[
\operatorname{CV}(T_c)^2
=\frac{(m+\lambda)(5m+\lambda-4c)}{(3m+\lambda-2c)^2},
\qquad
\partial_c\operatorname{CV}(T_c)^2
=\frac{8(m-c)(m+\lambda)}{(3m+\lambda-2c)^3}>0
\]
for \(c<m\), and its value at \(c=m\) is \(1\).

**(3) Hazard behavior.** Write \(p_1(t)=\Pr(\text{exactly one patch occupied at }t)\) and \(w(t)=p_{2,c}(t)/(p_{2,c}(t)+p_1(t))\). The conditional extinction hazard is
\[
h_c(t)=c w(t)+m(1-w(t))=m-(m-c)w(t).
\]
The forward equations yield \(w(0)=1\) and
\[
w'(t)=\lambda-(\lambda+m-c)w(t)-(m-c)w(t)^2.
\]
When \(c<m\), the right-hand side is strictly decreasing as a function of \(w\), is negative at \(w=1\), and has a unique nonnegative zero below \(1\). The scalar uniqueness theorem ensures \(w'(t)<0\) for all finite \(t\ge0\); hence \(h_c'(t)>0\). When \(c=m\), the initial two-occupied state is removed directly by the common catastrophe at rate \(m\), so \(T_m\) is exponential with rate \(m\).

## Verification
A reproducible Python checker `verify.py` is included and uses SymPy to verify all resolvent, moment, derivative, threshold and endpoint identities exactly. It then compares the analytic moments and Laplace transform against independently inverted transient generators for \(128\) parameter triples, and checks strict survival ordering at multiple times numerically. Floating calculations are corroboration, not substitutes for the analytical proof. For \(m=1\), \(\lambda=1/10\), the exact variance grows from \(561/400\) at \(c=0\) to \(400/279\) at the unique maximum \(c=59/180\), then falls to \(1\) at \(c=1\), while every survival probability strictly decreases throughout.

## Relationship to prior work
Spatially correlated disturbances and their adverse effects on metapopulation persistence are established ecological ideas, notably in Johst and Drechsler (2003). The present claim does not assert that disturbance correlation harms persistence is novel in itself. It addresses the **full survival-time stochastic ordering**, the **exact time-domain convolution sensitivity**, and a **sharp parameter-dependent reversal for the absolute extinction-time variance** in an explicitly stated continuous-time two-patch process. Schreiber (2010) addresses spatial/temporal environmental correlations via invasion growth exponents, rather than the exact finite-state extinction-time distribution. Elkin and Possingham (2008) investigate landscape-dependent disturbance and dispersal in spatially explicit metapopulations; that context does not imply the stated formulas without an additional theorem. The full Johst–Drechsler paper was not available for comprehensive inspection, so an older equivalent special case remains a residual originality risk; no global novelty certification is claimed.

## Limitations
All conclusions require two identical occupancy patches, exponentially distributed events, marginal extinction hazard held fixed while changing common shock intensity, and recolonization only from occupied patches. The pointwise ordering of survival probabilities is **not** a general theorem for arbitrary spatially correlated environmental processes, nor does stochastic ordering imply monotonicity of variance. The derived peak concerns **absolute variance** while relative variance is monotone. This is a mathematical benchmark, not an empirical statement about the magnitude of correlation effects in nature.

## References
- Johst, K. and Drechsler, M. (2003). *Are spatially correlated or uncorrelated disturbance regimes better for the survival of species?* Oikos 103, 449–456. DOI: `10.1034/j.1600-0706.2003.12770.x`. First publicly dated 2003-10-21.
- Schreiber, S. J. (2010). *Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence.* Proceedings B 277, 1907–1914. DOI: `10.1098/rspb.2009.2006`.
- Elkin, C. M. and Possingham, H. (2008). *The Role of Landscape-Dependent Disturbance and Dispersal in Metapopulation Persistence.* The American Naturalist 172, 563–575. DOI: `10.1086/590962`.
