# Sharp compact-recurrence fold and finite exit budget in a three-dimensional Hénon map

## Finding
Consider the real quadratic diffeomorphism
\[
F_{\alpha,\sigma,\delta}(x,y,z)
 = (\delta z+\alpha-\sigma y+x^2,\ x,\ y),
\qquad 0<\delta<1,\quad \alpha,\sigma\in\mathbb R.
\]
Put
\[
\kappa=\delta-\sigma-1,\qquad
\alpha_{\mathrm{SN}}=\frac{\kappa^2}{4},\qquad
c=-\frac{\kappa}{2},\qquad
\varepsilon=\alpha-\alpha_{\mathrm{SN}}.
\]
The fixed-point fold \(\alpha=\alpha_{\mathrm{SN}}\) is also the **sharp existence boundary for all bounded forward dynamics**, and it separates three global regimes:

1. If \(\varepsilon>0\), every forward trajectory escapes to infinity, with the universal lower rate
\[
\liminf_{N\to\infty}\frac{\|F^N(p)\|_{\infty}}{N}\ge\frac{\varepsilon}{1+|\delta-\sigma|+\delta}>0.
\]
Moreover, if the \(N+1\) states \(p,F(p),\ldots,F^N(p)\) lie in \([-R,R]^3\), then necessarily
\[
N\le \frac{2R(1+|\delta-\sigma|+\delta)}{\varepsilon}.
\]
2. If \(\varepsilon=0\), every bounded forward trajectory converges to the unique fixed point \((c,c,c)\). The singleton \(\{(c,c,c)\}\) is the only nonempty compact **two-sided invariant** set (\(F(K)=K\)), and its point mass is the only compactly supported invariant probability measure.
3. If \(\varepsilon<0\), there are exactly two fixed points \((c\pm\sqrt{-\varepsilon},c\pm\sqrt{-\varepsilon},c\pm\sqrt{-\varepsilon})\), so nonempty compact invariant sets exist.

In all three regimes, every compactly supported invariant probability \(\mu\), if one exists, obeys the exact stationary second-moment law
\[
\int_{\mathbb R^3}(x-c)^2\,d\mu(x,y,z)=\alpha_{\mathrm{SN}}-\alpha.
\]
Here and below all boundedness and convergence refer to the full real phase space, not just a local center manifold.

## Assumptions and scope
All quantifiers range over \(0<\delta<1\), arbitrary real \(\sigma,\alpha\), every real initial state, every integer \(N\ge0\), and every real \(R\ge0\). Compact two-sided invariance means \(F(K)=K\), not merely \(F(K)\subseteq K\). The map is invertible since its constant Jacobian determinant is \(\delta>0\). An invariant probability is a Borel probability satisfying \(F_*\mu=\mu\); compact support makes all displayed moments finite.

## Proof
**Exact polynomial balance.** Define the affine height
\[
H(x,y,z)=x+(\delta-\sigma)y+\delta z.
\]
A direct substitution, without approximation, gives
\[
H(F(x,y,z))-H(x,y,z)
 =x^2+\kappa x+\alpha
 =(x-c)^2+\varepsilon. \tag{1}
\]
The fixed-point equation forces \(x=y=z=u\) and
\[
0=u^2+\kappa u+\alpha=(u-c)^2+\varepsilon. \tag{2}
\]
Equation (2) gives the exact number and coordinates of fixed points in each parameter regime.

**Above the fold.** When \(\varepsilon>0\), equation (1) gives \(H(F^N p)-H(p)\ge N\varepsilon\). If all \(N+1\) states lie in \([-R,R]^3\), each height has absolute value at most \(R(1+|\delta-\sigma|+\delta)\). Subtracting the endpoint bounds proves the stated finite exit budget. In addition, \(H(F^N p)\ge H(p)+N\varepsilon\) and \(H(q)\le(1+|\delta-\sigma|+\delta)\|q\|_\infty\) for all states \(q\), so dividing by \(N\) proves the asserted positive lower escape rate. In particular, every forward orbit eventually leaves each bounded cube and never returns.

**At the fold, forward rigidity.** When \(\varepsilon=0\), equation (1) says that \(H(F^n p)\) is nondecreasing and that
\[
\sum_{n=0}^{N-1}(x_n-c)^2
 =H(F^N p)-H(p),
\quad x_n=\pi_1(F^n p). \tag{3}
\]
If the forward orbit is bounded, the heights are bounded, so the series on the left converges. Hence \(x_n\to c\). As the last two coordinates at time \(n\) equal the first coordinate at times \(n-1\) and \(n-2\), the full state tends to \((c,c,c)\).

**At the fold, two-sided rigidity.** Let \((p_n)_{n\in\mathbb Z}\) be any bounded entire orbit. The nonnegative increments in (1) have finite sum over all \(n\in\mathbb Z\), since the monotone sequence \(H(p_n)\) is bounded. Thus \(\pi_1(p_n)\to c\) as \(n\to\pm\infty\), and the shift-coordinate structure implies \(p_n\to(c,c,c)\) at both ends. Consequently the two limits of \(H(p_n)\) coincide. Its total nonnegative increment is zero, so every first coordinate is exactly \(c\) and the entire orbit is the fixed orbit. Since \(\delta>0\) makes \(F\) invertible, every point of a nonempty compact set satisfying \(F(K)=K\) lies on a bounded entire orbit. Such a set is therefore precisely the fixed-point singleton.

**Stationary law.** Integrating the exact identity (1) against a compactly supported invariant probability yields \(0=\int(x-c)^2\,d\mu+\varepsilon\). This is the claimed moment identity. At \(\varepsilon=0\), it forces \(x=c\) almost surely; invariance and the coordinate shifts then give \(y=z=c\) almost surely, so the measure is the fixed-point Dirac mass. When \(\varepsilon>0\), the right side would have to be negative, which is impossible. When \(\varepsilon<0\), both fixed-point Dirac masses exist and satisfy the identity, proving that the existence boundary is sharp.

## Verification
The standalone standard-library program `verify.py` replays 498 exact rational identity and fixed-point checks at varied parameter values, including the noninvertible limiting coefficient for an algebraic stress test. The proof for every real parameter, arbitrary orbit, and unbounded time is the symbolic identity (1) plus elementary monotone-sequence and nonnegative-series arguments; the finite checks do not constitute infinite verification. To reproduce, run `python verify.py` using Python 3. The program tests only finite algebra and makes no external requests.

## Relationship to prior work
Hampton and Meiss introduce this three-dimensional Hénon family and explicitly derive the fixed-point saddle-node threshold \(\alpha_{\mathrm{SN}}\) and a cube containing all bounded *two-sided* orbits; their Section IV and numerical explorations do not establish that the fold controls **all bounded forward trajectories** or that the fold itself has only trivial compact two-sided dynamics. Their fixed-point equation and cube lemma are recognized as prior results.

Lomelí and Meiss study general quadratic volume-preserving maps and, under a positive-definiteness assumption on the quadratic form, derive an enclosure for bounded orbits. This neither covers the semidefinite one-square quadratic term with arbitrary \(0<\delta<1\) nor implies the present fold identity. Zheng and collaborators examine a different three-dimensional Hénon generalization with nonlinear term involving the **second** coordinate rather than the first; their local fold analysis does not establish this global recurrence statement. The novelty claimed here is solely the exact affine-height balance and its global fold, critical, moment, and finite-residence consequences, not the known saddle-node location.

## Limitations
The theorem does not assert that every trajectory converges at the critical parameter: escaping initial conditions can exist, and convergence is asserted only for bounded forward trajectories. It gives an upper bound, not a sharp asymptotic formula, for time spent inside a fixed cube above the fold. For \(\alpha<\alpha_{\mathrm{SN}}\), it proves existence of two fixed points but does not classify other invariant sets. The stationary identity is for compactly supported measures; no moment statement is made for invariant laws lacking integrability. Historical priority has not been independently audited, and stronger general recurrence theorems not found in the checked sources remain a possible overlap risk.

## References
- Amanda E. Hampton and James D. Meiss, *Visualizing Attractors of the Three-Dimensional Generalized Hénon Map* (first posted June 16, 2022), arXiv:2206.07855, https://arxiv.org/abs/2206.07855; journal version, *Chaos* 32 (2022), 113127, DOI:10.1063/5.0103436.
- Héctor E. Lomelí and James D. Meiss, *Quadratic Volume Preserving Maps* (first posted May 30, 1997), arXiv:chao-dyn/9706001, https://arxiv.org/abs/chao-dyn/9706001; *Nonlinearity* 11 (1998), 557–574.
- Jingjing Zheng, Ziwei Wang, You Li and Jinliang Wang, *Bifurcations and chaos in a three-dimensional generalized Hénon map*, *Advances in Difference Equations* 2018, 185, https://doi.org/10.1186/s13662-018-1622-y.
