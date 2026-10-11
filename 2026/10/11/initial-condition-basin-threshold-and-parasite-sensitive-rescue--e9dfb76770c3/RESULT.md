# Initial-condition basin threshold and parasite-sensitive rescue in a harvested commensal system

## Finding

A three-species commensalism–parasitism system with saturating harvesting has two locally attracting outcomes in an open harvesting regime: commensal extinction and persistence at a positive density. For **every fixed pair** of positive initial host and parasite densities, the outcome is selected by exactly one critical initial commensal density. The critical density is strictly below the autonomous unstable equilibrium, and its small-host displacement is given by an explicit parasite-sensitive integral.

More precisely, let \(x_c(y_0,z_0)\) denote the unique critical density defined below. Then
\[
\lim_{t\to\infty}(x,y,z)(t)=
\begin{cases}
(0,0,k_3), & 0<x_0<x_c,\\
(u_-,0,k_3), & x_0=x_c,\\
(u_+,0,k_3), & x_0>x_c.
\end{cases}
\]
The threshold is continuous and satisfies \(0<x_c(y_0,z_0)<u_-\). Its derivative at zero initial host density depends monotonically on the initial parasite density.

## Assumptions and scope

The model is
\[
\begin{aligned}
\dot x&=r_1x\left(1-\frac{x}{k_1}+\frac{ay}{k_1}\right)-\frac{qEx}{m_1E+m_2x},\\
\dot y&=r_2y\left(1-\frac{y}{k_2}-\frac{bz}{k_2}\right),\\
\dot z&=r_3z\left(1-\frac{z}{k_3}+\frac{cy}{k_3}\right).
\end{aligned}
\]
All eleven model parameters and the initial densities \(x_0,y_0,z_0\) are strictly positive. Assume the three strict conditions
\[
bk_3>k_2,\qquad k_1m_2>m_1E,\qquad
r_1m_1<q<q_*:=\frac{r_1(m_1E+k_1m_2)^2}{4Ek_1m_2}.
\]
Set \(P(u)=r_1(1-u/k_1)(m_1E+m_2u)-qE\). The assumptions ensure \(P(0)<0\), a positive quadratic maximum, and two distinct positive roots \(0<u_-<u_+\). Define
\[
F(u)=\frac{uP(u)}{m_1E+m_2u},\qquad
\lambda_-:=F'(u_-)=\frac{r_1m_2u_-(u_+-u_-)}{k_1(m_1E+m_2u_-)}>0.
\]
No assertion is made for the fold \(q=q_*\), for vanishing or negative parameters, or for the host-persistence case \(bk_3\le k_2\).

## Proof

**Host and parasite limits.** Positivity is forward invariant. Since \(\dot y\le r_2y(1-y/k_2)\), host density is bounded. Consequently the parasite equation is bounded above by a logistic equation with carrying capacity \(k_3+c\sup_{t\ge0}y(t)\). Because \(y(t)\ge0\), comparison from below with the logistic flow \(\dot Z=r_3Z(1-Z/k_3)\) shows \(\liminf z(t)\ge k_3\). Choose \(\delta>0\) such that \(b(k_3-\delta)>k_2\). For all sufficiently large times, \(z\ge k_3-\delta\), whence \(\dot y\le-\eta y\) for some \(\eta>0\); thus \(y(t)\) decays exponentially. Comparing \(z\) to logistic equations whose carrying capacities tend to \(k_3\) yields \(z(t)\to k_3\).

**Scalar limiting dynamics.** We may write \(\dot x=F(x)+(r_1a/k_1)xy(t)\). The negative quadratic growth controls all \(x(t)\) because \(y\) is bounded. On the positive axis, \(F\) is negative between \(0\) and \(u_-\), positive between \(u_-\) and \(u_+\), and negative above \(u_+\). The nonautonomous perturbation tends uniformly to zero on every bounded interval. For each closed interval avoiding these three isolated zeros, the limiting sign is therefore eventually fixed; repeated crossings of such an interval in opposite directions are impossible. Bounded scalar solutions consequently converge to exactly one of \(0,u_-,u_+\).

**Unique basin separator.** For each fixed positive pair \((y_0,z_0)\), solutions are strictly ordered in \(x_0\) by uniqueness of the scalar initial-value problem. The limiting equilibria \((0,0,k_3)\) and \((u_+,0,k_3)\) are hyperbolic sinks: the \(y,z\) eigenvalues are \(r_2(1-bk_3/k_2)<0\) and \(-r_3<0\), while their \(x\) eigenvalues are \(F'(0)=r_1-q/m_1<0\) and \(F'(u_+)<0\). Their basins are open. Small enough \(x_0>0\) enters the extinction sink basin after a finite time: for fixed \((y_0,z_0)\), first choose a time after which the host is small and then use continuous dependence as \(x_0\downarrow0\) on this finite interval. Conversely, comparison with the autonomous equation \(\dot v=F(v)\) shows that every \(x_0\ge u_-\) converges to \(u_+\): for the borderline \(x_0=u_-\), strict positivity of \(y(t)\) makes \(x(t)>u_-\) for \(t>0\), after which comparison with the autonomous solution starting at this larger value gives \(\liminf x(t)\ge u_+\).

Ordering implies that extinction initial data form a lower interval and upper-equilibrium initial data form an upper interval, both nonempty and open within the positive axis. Their common boundary contains at least one \(x_c\in(0,u_-)\); it cannot converge to either hyperbolic sink, so it converges to \(u_-\). There cannot be two distinct such initial values: their solution difference \(d(t)>0\) obeys \(\dot d=G(t)d\), with \(G(t)\to F'(u_-)=\lambda_->0\) if both solutions tend to \(u_-\); hence \(d(t)\) would grow exponentially, contradicting boundedness. Therefore precisely one \(x_c\) exists, and the three-way classification follows. To prove continuity of \(x_c(y_0,z_0)\), bracket it by extinction and persistence initial data on either side and use finite-time continuous dependence together with openness of the two sink basins.

**Quantitative small-host response.** Fix \(z_0>0\) and first set \(y_0=0\). Along the resulting base trajectory \(x(t)=u_-\), \(y(t)=0\), \(z(t)=Z_{z_0}(t)\), the unique threshold is \(u_-\). The hyperbolic equilibrium \((u_-,0,k_3)\) has a two-dimensional stable manifold and a one-dimensional unstable direction. The segment of the threshold orbit with \(z_0\ne k_3\) lies in its global stable manifold. Finite-time smooth flow pullback from a local stable-manifold chart therefore gives differentiability of the threshold initial value in \(y_0\) at zero. The host's first variation is
\[
Y(t)=\exp\left(r_2\int_0^t\left[1-\frac{b}{k_2}Z_{z_0}(s)\right]ds\right).
\]
The commensal first variation along a threshold orbit satisfies
\[
\dot X=\lambda_-X+\frac{r_1a u_-}{k_1}Y(t).
\]
Its unique initial value producing a bounded stable variation is
\[
X(0)=-\frac{r_1a u_-}{k_1}\int_0^\infty e^{-\lambda_-t}Y(t)dt.
\]
The integral is finite and strictly positive because \(Z_{z_0}(t)\to k_3\) and \(r_2(1-bk_3/k_2)<0\). Thus
\[
x_c(y_0,z_0)=u_--\frac{r_1a u_-}{k_1}I(z_0)y_0+o(y_0),\quad
I(z_0)=\int_0^\infty e^{-\lambda_-t}Y(t)dt.
\]
For distinct \(z_0^{(1)}<z_0^{(2)}\), strict scalar logistic comparison gives \(Z_{z_0^{(1)}}(t)<Z_{z_0^{(2)}}(t)\) for all finite \(t\), hence \(I(z_0^{(1)})>I(z_0^{(2)})\). If \(z_0=k_3\), then \(Z(t)=k_3\) identically and
\[
I(k_3)=\left[\lambda_-+r_2\left(\frac{bk_3}{k_2}-1\right)\right]^{-1}.
\]
This proves the basin and sensitivity assertions.

## Verification

Direct factorization gives \(P(u)=-(r_1m_2/k_1)(u-u_-)(u-u_+)\), and the negative host invasion eigenvalue at \((u_-,0,k_3)\) justifies the stable-manifold calculation. A small numerical illustration (not used as proof) takes \(r_1=r_2=r_3=k_2=k_3=a=c=E=m_1=1\), \(k_1=4\), \(m_2=b=q=2\). Then \(q_*=81/32\), \(u_-=(7-\sqrt{17})/4\), \(u_+=(7+\sqrt{17})/4\), and \(\lambda_-\approx0.304029\). The initial-host derivative for \(z_0=k_3\) is approximately \(-0.137885\); direct ODE shooting estimates the threshold at \(y_0=1,z_0=1\) to be approximately \(0.64114\), strictly smaller than \(u_-\approx0.71922\). The accompanying checker independently reconstructs the displayed algebraic quantities.

## Relationship to prior work

The **existence of two positive equilibrium branches is not new**: the 2021 analysis of Puspitasari and collaborators gives the double-root equilibrium regime. The 2019 and two 2022 source papers principally present existence and local stability classification or monostable global results; the 2022 Liu–Yue source treats harvesting thresholds that do not provide this entire open bistability basin classification. The present statement instead determines the **global fate for all positive initial data** by a unique separator depending on the host and parasite initial densities, and calculates its first-order parasite sensitivity. This is an implication-level refinement, not a renamed equilibrium count.

## Limitations

The claim assumes strictly positive parameters and initial data, a strictly host-extinct asymptotic regime, and distinct positive commensal equilibria. It proves a basin graph and a one-sided small-host derivative, not a closed elementary formula for arbitrary \(x_c(y_0,z_0)\). The scalar comparison and stable-manifold arguments are analytic; numerical examples merely support reproducibility. A residual literature risk is possible later work on an exact equivalent three-species harvest basin that is not indexed by the consulted searches.

## References

- Xiaowan Liu and Qin Yue, “Stability property of the boundary equilibria of a symbiotic model of commensalism and parasitism with harvesting in commensal populations,” *AIMS Mathematics* 7 (2022), 18146–18168, doi:10.3934/math.20221034. Published 2022-08-23. Full text: https://www.aimspress.com/aimspress-data/math/2022/10/PDF/math-07-10-1034.pdf.
- Puspitasari et al., “Dynamics of a symbiotic model of commensalism and parasitism with harvesting,” *JTAM* (2021), doi:10.31764/jtam.v5i1.3893. https://journal.ummat.ac.id/index.php/jtam/article/download/3893/2627.
- Chen, Zhou and Lin, “Global stability of symbiotic model of commensalism and parasitism with harvesting in commensal populations,” *WSEAS Transactions on Mathematics* 21 (2022), doi:10.37394/23206.2022.21.50. https://wseas.com/journals/mathematics/2022/b025106-027%282022%29.pdf.
- Baoguo Chen, “The influence of commensalism on a Lotka–Volterra commensal symbiosis model with Michaelis–Menten type harvesting,” *Advances in Difference Equations* (2019), doi:10.1186/s13662-019-1989-4. https://link.springer.com/article/10.1186/s13662-019-1989-4.
