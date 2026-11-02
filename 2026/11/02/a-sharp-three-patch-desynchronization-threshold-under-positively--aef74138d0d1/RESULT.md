# A sharp three-patch desynchronization threshold under positively correlated forcing

## Finding

Consider a stable, linearly regulated population on a chain of three equally regulated habitat patches. Increasing symmetric dispersal need not initially synchronize the two endpoint populations, even when every pair of patches experiences positively correlated environmental shocks. The precise initial-response criterion depends on three entries of the environmental covariance matrix. In a two-factor environmental model with an independent local-noise contribution, it yields a sharp threshold, a genuine intermediate dispersal optimum, and an exactly certified unique-minimum example.

**Three-patch initial-response law.** Let \(Q=(q_{ij})_{1\le i,j\le3}\) be any symmetric positive-definite environmental increment covariance. For the stationary endpoint Pearson correlation \(r(m)\) defined below,
\[
 r'(0)=\frac{q_{12}(1-q_{13}/q_{11})+q_{23}(1-q_{13}/q_{33})}{2\gamma\sqrt{q_{11}q_{33}}}.
\]
Consequently, initial desynchronization occurs precisely when the numerator is negative. Notably, the intermediate-patch noise variance \(q_{22}\) does not enter this first-order sign law.

**Positive-shock family and sharp boundary.** For the natural two-shared-driver-plus-local-noise construction
\[
 Q_\delta={\bf1}{\bf1}^{\mathsf T}+vv^{\mathsf T}+\delta I,
 \qquad v=(1,0,4)^{\mathsf T},\qquad \delta>0,
\]
all six distinct/symmetric covariance entries are strictly positive, and every variance is positive. Its endpoint correlation obeys
\[
 r_\delta'(0)=\frac{2\delta^2+28\delta-27}{2\gamma[(2+\delta)(17+\delta)]^{3/2}}.
\]
The unique positive critical noise intensity is
\[
 \delta_c=\frac{5\sqrt{10}-14}{2}\approx0.905694.
\]
For \(0<\delta<\delta_c\), increasing dispersal from zero strictly *reduces* stationary endpoint correlation. At \(\delta=\delta_c\) the initial derivative vanishes; for \(\delta>\delta_c\), it increases. For every \(\delta>0\), \(r_\delta(m)\to1\) as \(m\to\infty\). Hence every \(0<\delta<\delta_c\) has at least one strict-decrease interval and at least one positive finite global minimizing dispersal rate.

**Exactly classified example.** At \(\delta=1/4\), the correlation has *exactly one* positive critical point, its unique strict global minimum. In dimensionless dispersal \(t=m/\gamma\), it lies in
\[
 \frac{7967}{100000}<t_*<\frac{7968}{100000},
\]
with \(t_*\approx0.0796728110\), \(r(0)=20/\sqrt{621}\approx0.80257235\), and \(r(t_*)\approx0.80109570\). This is a local linear-response result: no assertion about nonlinear persistence, extinction, or field data is made.

**Minimality for the initial-response phenomenon.** For two equally regulated patches with arbitrary symmetric positive-definite environmental covariance \(\left(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\right)\) and symmetric dispersal, the stationary Pearson correlation has
\[
 r_2'(0)=\frac{(a+b)(ab-c^2)}{2\gamma(ab)^{3/2}}>0.
\]
Thus three patches are the smallest connected network capable of the *negative initial dispersal response* under equal local regulation; this does not assert that every two-patch correlation is monotone at all dispersal rates.

## Assumptions and scope

Let \(X_t\in\mathbb R^3\) denote centered fluctuations around a positive stable population equilibrium. Fix \(\gamma>0\) and symmetric, nonnegative exchange rate \(m\ge0\). The process is the linear Ornstein–Uhlenbeck model
\[
 dX_t=-(\gamma I+mL)X_t\,dt+dB_t,
 \qquad L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},
\]
where the Gaussian driving process has independent increments in time and instantaneous covariance \(d\langle B\rangle_t=Q\,dt\). In the general law, \(Q\) is any fixed real symmetric positive-definite matrix, independent of \(m\). In the sharp-noise subfamily, \(Q=Q_\delta\) with \(\delta>0\), so it is strictly positive definite and all pairwise environmental covariances are positive.

The real symmetric matrix \(L\) is the path-graph Laplacian with eigenvalues \(0,1,3\). The positive damping \(\gamma I+mL\) guarantees a unique stationary Gaussian law for all \(m\ge0\). Its covariance \(S(m)\) satisfies
\[
 (\gamma I+mL)S+S(\gamma I+mL)=Q,
\]
and \(r(m)=S_{13}(m)/\sqrt{S_{11}(m)S_{33}(m)}\). The model represents linearized dynamics and does not require an actual Gaussian population density or positivity of every sample-path fluctuation.

The two shared environmental factors have loadings \({\bf1}=(1,1,1)^{\mathsf T}\) and \(v=(1,0,4)^{\mathsf T}\), respectively. The latter can represent a regional driver shared by the two endpoints with very different sensitivities and absent at the center; adding \(\delta I\) represents patch-specific independent fluctuations. This non-distance-monotone covariance pattern is an explicit modeling assumption, not a claim about typical geographical correlations.

## Proof

**1. Stationary covariance and initial perturbation.** Write \(H(m)=\gamma I+mL\). Since \(H(m)\) is symmetric positive definite,
\[
 S(m)=\int_0^\infty e^{-H(m)s}Qe^{-H(m)s}\,ds
\]
is the unique stationary covariance and is positive definite. Differentiating its defining Lyapunov equation at \(m=0\), where \(S(0)=Q/(2\gamma)\), gives
\[
 S'(0)=-\frac{LQ+QL}{4\gamma^2}.
\]
For the path Laplacian,
\[
 S'_{13}(0)=\frac{q_{12}+q_{23}-2q_{13}}{4\gamma^2},\quad
 S'_{11}(0)=\frac{q_{12}-q_{11}}{2\gamma^2},\quad
 S'_{33}(0)=\frac{q_{23}-q_{33}}{2\gamma^2}.
\]
Apply the quotient and chain rules to \(S_{13}(S_{11}S_{33})^{-1/2}\) and substitute \(S(0)=Q/(2\gamma)\); the result simplifies exactly to the asserted general three-patch formula.

**2. Sharp noise threshold.** For \(Q_\delta\), the entries needed above are \(q_{11}=2+\delta\), \(q_{33}=17+\delta\), \(q_{13}=5\), and \(q_{12}=q_{23}=1\). The derivative numerator reduces to
\[
 2-\frac5{2+\delta}-\frac5{17+\delta}
 =\frac{2\delta^2+28\delta-27}{(2+\delta)(17+\delta)}.
\]
The quadratic is strictly increasing for \(\delta\ge0\) and has the sole positive zero \(\delta_c=(5\sqrt{10}-14)/2\). Hence all asserted strict inequalities and the equality case follow without numerical approximation.

**3. High-dispersal limit and finite minimizers.** Let \(P_0={\bf1}{\bf1}^{\mathsf T}/3\) project onto the zero eigenmode of \(L\). In the eigenbasis of \(L\), covariance mode \((j,k)\) has denominator \(2\gamma+m(\lambda_j+\lambda_k)\). As \(m\to\infty\), only \((0,0)\) survives. Thus
\[
 S(m)\longrightarrow\frac{P_0QP_0}{2\gamma}
 =\frac{{\bf1}^{\mathsf T}Q{\bf1}}{18\gamma}{\bf1}{\bf1}^{\mathsf T},
\]
whose nonzero scalar coefficient is positive, and \(r(m)\to1\). For \(0<\delta<\delta_c\), \(r'(0)<0\), while \(r(0)<1\) because \(Q_\delta\) is positive definite. Continuity, strict decrease immediately after zero, and convergence to a larger limit imply that a global minimum is attained at a positive, finite \(m\).

**4. Exact unique minimum at \(\delta=1/4\).** Put \(t=m/\gamma\). The factor \(1/\gamma\) cancels from Pearson correlation, so it suffices to solve the covariance equation at \(\gamma=1\). Define
\[
\begin{aligned}
 A(t)&=36+268t+759t^2+1031t^3+763t^4+278t^5,\\
 C(t)&=276+1948t+4899t^2+5351t^3+2383t^4+278t^5,\\
 K(t)&=(t+2)(2t+1)(139t^3+268t^2+188t+40).
\end{aligned}
\]
Solving the six Lyapunov equations exactly (replayed in the accompanying standalone checker) yields
\[
 r(t)=\frac{K(t)}{\sqrt{A(t)C(t)}}.
\]
Because \(A,C,K\) are positive for \(t\ge0\), the sign of \(r'(t)\) equals the sign of
\[
 N(t)=2K'(t)A(t)C(t)-K(t)\bigl(A'(t)C(t)+A(t)C'(t)\bigr)=2P(t).
\]
The exact coefficient list of \(P(t)\), in ascending powers of \(t\), is

```text
[-40704, -212480, 3518496, 45433888, 238288032, 722717640,
 1402044574, 1824837840, 1671621225, 1185727765,
 743643377, 406303950, 152176644, 26431128]
```

There is exactly one coefficient sign change (reading descending or ascending), so Descartes' rule permits at most one positive root. As \(P(0)<0\) and the leading coefficient is positive, there is at least one positive root; it is unique. Its sign changes from negative to positive, yielding a strict global minimum, with the exact rational enclosure certified by direct evaluation at \(7967/100000\) and \(7968/100000\). No finite sampling argument is used to deduce uniqueness.

**5. Two-patch boundary.** For two patches, \(L_2=\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\), \(Q_2=\left(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\right)\), \(a,b>0\), and \(ab>c^2\). The same differentiation gives \(S_{12}'(0)=(a+b-2c)/(4\gamma^2)\), \(S_{11}'(0)=(c-a)/(2\gamma^2)\), and \(S_{22}'(0)=(c-b)/(2\gamma^2)\). Substituting into the Pearson quotient derivative yields \((a+b)(ab-c^2)/(2\gamma(ab)^{3/2})>0\). Thus the three-patch sign reversal is genuinely outside the two-patch equal-damping initial-response law.

## Verification

The included pure-Python standard-library program `CHECK.py` independently constructs rational-polynomial expressions for all six entries of \(S(t)\) in the explicit example. It verifies all six distinct Lyapunov matrix entries, the Pearson identity \(r(t)^2=K(t)^2/[A(t)C(t)]\), the derivative polynomial, its coefficient signs and exact rational root bracket, and the symbolic \(\delta\)-slope identity. It also performs 24 supplementary finite rational and numerical checks; these are diagnostics, not the basis for the all-parameter conclusions. Reproduce with `python3 CHECK.py`. Successful output includes `VERIFY_OK symbolic_identities=13 exact_sample_checks=24`.

## Relationship to prior work

Spatial correlation of environmental disturbances and dispersal-induced synchrony are established topics. Kendall et al. (2000) give a full analytic treatment of a *two-patch discrete-time* correlated-noise and dispersal model (section “The Model,” equations (3)–(17)); its findings do not supply the present three-patch path criterion. Ripa (2000) develops general linearized population-synchrony theory, and Abbott (2011) explicitly reviews earlier *nonmonotone* dispersal–synchrony examples. No novelty is claimed for nonmonotonicity in general. Vasseur (2007) studies temporally colored forcing and heterogeneous population dynamics, rather than the present white-noise path with common regulation. Wang, Haegeman and Loreau (2015) use continuous-time linearized Lyapunov covariance, and consider homogeneous many-patch equicorrelated noise and heterogeneous two-patch settings. The stationary Lyapunov method is therefore known; the particular general three-path initial derivative, sharp positive-forcing-family threshold, and exact unique-minimum certificate are the claims under review.

The closely relevant broader literature leaves a residual historical-priority risk: the full generality of some older contributions, including Lande, Engen and Sæther (1999) and Ripa (2000), has not been exhaustively inspected. The present work does not claim independent priority certification.

## Limitations

The process is a stable local linearization with temporally white Gaussian forcing. Dispersal is undirected, nearest-neighbor, density-independent, and symmetric; local damping is equal across patches. The positive environmental covariance is *not* assumed to decrease with graph distance. In the explicit example the correlation dip is small (about 0.00148 absolute), so no large field effect is inferred. The threshold classifies only the sign of the initial derivative; for general \(\delta\) below the threshold it establishes the existence, but not uniqueness, of a positive finite minimizing rate. Uniqueness is proved only at \(\delta=1/4\). This calculation does not establish nonlinear population persistence, extinction probabilities, or observational applicability.

## References

1. Ripa, J. (2000). “Analysing the Moran effect and dispersal: their significance and interaction in synchronous population dynamics.” *Oikos* 89:175–187. DOI: `10.1034/j.1600-0706.2000.890119.x`.
2. Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H. and Fagan, W. F. (2000). “Dispersal, Environmental Correlation, and Spatial Synchrony in Population Dynamics.” *American Naturalist* 155:628–636. DOI: `10.1086/303350`.
3. Vasseur, D. A. (2007). “Environmental colour intensifies the Moran effect when population dynamics are spatially heterogeneous.” *Oikos* 116:1726–1736. DOI: `10.1111/j.0030-1299.2007.16101.x`.
4. Abbott, K. C. (2011). “A dispersal-induced paradox: synchrony and stability in stochastic metapopulations.” *Ecology Letters*. DOI: `10.1111/j.1461-0248.2011.01670.x`.
5. Wang, S., Haegeman, B. and Loreau, M. (2015). “Dispersal and metapopulation stability.” *PeerJ* 3:e1295. DOI: `10.7717/peerj.1295`.
6. Lande, R., Engen, S. and Sæther, B.-E. (1999). “Spatial Scale of Population Synchrony: Environmental Correlation versus Dispersal and Density Regulation.” *American Naturalist* 154:271–281. DOI: `10.1086/303240`.
