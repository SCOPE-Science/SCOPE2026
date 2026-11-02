# Sharp three-cell lag between projected descent and a single capped-simplex projection

## Finding

For the three-cell capped simplex \(C_s=\{z\in[0,1]^3:\sum_i z_i=s\}\), the continuous minimal-selection flow for a linear objective and the Euclidean projection of the *single accumulated drift* need not agree. A natural four-parameter family has a completely explicit, sharp discrepancy:

\[
\sup_{t\ge0}\|g(t)-r(t)\|_\infty
=\min\!\left\{\frac b2\left(1-\frac{2a}{H}\right),\;1-p-b\right\}.
\]

The supremum of this discrepancy over the specified family is exactly \(1/3\), approached but not attained at admissible parameters. The first release of an initially saturated coordinate occurs at \(2b/H\) in the continuous flow and at \(b/a\) in the one-shot projection path. Their ratio \(H/(2a)\) has no finite upper bound. A capped simplex with two cells never exhibits such a discrepancy, for any feasible initial point and linear objective, so three is the smallest possible cell count.

## Assumptions and scope

Take real parameters \(0<p\), \(0<b\), \(p+b<1\), \(a>0\), and \(H>2a\). Define
\[
s=1+p+b,\quad x^0=(p,1,b),\quad c=(0,a,H),\quad C_s=\{z\in[0,1]^3:\sum_{i=1}^3z_i=s\}.
\]
The objective is the linear functional \(f(z)=c\cdot z\). Let \(N_{C_s}\) and \(T_{C_s}\) denote the Euclidean normal and tangent cones. Let \(g:[0,\infty)\to C_s\) be the unique solution of the convex gradient inclusion
\[
\dot g(t)\in-c-N_{C_s}(g(t)),\quad g(0)=x^0,
\]
whose right derivative equals \(\operatorname{proj}_{T_{C_s}(g(t))}(-c)\). Independently, define the **single-shot** drift projection \(r(t)=\operatorname{proj}_{C_s}(x^0-tc)\). It is not an iteration of repeated finite-step projections and is not the solution of the inclusion by definition. Time is the dimensionless positive parameter in these two explicitly specified paths.

Set
\[
\tau_g=\frac{2b}{H},\qquad \tau_r=\frac ba,\qquad
L=\frac{2(1-p-b)}a,\qquad
\ell(u)=\min\{1-p-b,\max\{0,au/2\}\}.
\]
Then \(0<\tau_g<\tau_r\), and both paths have exact formulas:
\[
g(t)=\begin{cases}
(p+Ht/2,\,1,\,b-Ht/2),&0\le t\le\tau_g,\\
(p+b+\ell(t-\tau_g),\,1-\ell(t-\tau_g),\,0),&t\ge\tau_g;
\end{cases}
\]
\[
r(t)=\begin{cases}
(p+Ht/2,\,1,\,b-Ht/2),&0\le t\le\tau_g,\\
(p+b+\ell(t-\tau_r),\,1-\ell(t-\tau_r),\,0),&t\ge\tau_g.
\end{cases}
\]
In particular, \(r(t)=(p+b,1,0)\) on \([\tau_g,\tau_r]\), while \(g\) begins transferring mass from the second to the first cell immediately at \(\tau_g\). Both reach the same optimum \((1,p+b,0)\).

## Proof

**1. Projected flow.** The negative objective gradient is \(-c=(0,-a,-H)\). At states \((q,1,z)\) with both \(q,z\) strictly between zero and one, the tangent cone has velocity constraints \(v_1+v_2+v_3=0\) and \(v_2\le0\). The Euclidean minimizer of \(\|v+c\|_2^2\) over that cone is
\[
v^{(I)}=(H/2,0,-H/2),
\]
because the unconstrained hyperplane projection would have second component \((H-2a)/3>0\), violating the upper-bound tangent constraint. The first and third coordinates therefore meet the point \((p+b,1,0)\) exactly at \(\tau_g=2b/H\); the first coordinate cannot reach its cap earlier since \(p+b<1\).

At \((p+b,1,0)\), both the upper constraint on coordinate two and the lower constraint on coordinate three are active. Minimizing the same velocity-distance objective over \(v_2\le0\), \(v_3\ge0\), and \(\sum_i v_i=0\) gives
\[
v^{(II)}=(a/2,-a/2,0).
\]
One direct verification is to parameterize \(v_1=-v_2-v_3\); the resulting strictly convex quadratic has minimizer \(v_2=-a/2\), \(v_3=0\) under \(H>2a\). Once coordinate two is strictly below its upper cap, the same velocity remains the tangent-cone projection until coordinate one reaches one. That takes the additional time \(L=2(1-p-b)/a\). At \((1,p+b,0)\), \(-c\) projects to zero on the tangent cone, as is also certified by minimizing the objective over \(C_s\): the most costly third coordinate is zero and the least costly first coordinate is one. Concatenating these velocities gives the displayed \(g\), a solution of the unique maximal-monotone gradient inclusion.

**2. One-shot projection.** The standard KKT characterization of capped-simplex projection is
\[
\bigl[\operatorname{proj}_{C_s}(y)\bigr]_i
=\min\{1,\max\{0,y_i-\lambda\}\},
\quad\text{with }\sum_i\min\{1,\max\{0,y_i-\lambda\}\}=s.
\]
For \(y(t)=(p,1-at,b-Ht)\), on \([0,\tau_g]\) take \(\lambda=-Ht/2\): coordinates one and three are free and coordinate two is at one, since \(H>2a\). On \([\tau_g,\tau_r]\), take \(\lambda=-b\), giving \((p+b,1,0)\). Indeed, the second coordinate is still clipped above at one because \(b-at\ge0\), while the third is clipped below at zero because \(2b-Ht\le0\). On \([\tau_r,\tau_r+L]\), take \(\lambda=-(at+b)/2\), giving
\[
r(t)=(p+(at+b)/2,\,1+(b-at)/2,\,0).
\]
The box inequalities hold throughout this interval, using \(H>2a\). Beyond \(\tau_r+L\), the projection is the common optimum. Strict convexity of squared Euclidean distance ensures these KKT candidates are the unique projections.

**3. Exact discrepancy and envelope.** The two paths agree until \(\tau_g\). Afterward their first coordinates differ by \(\ell(t-\tau_g)-\ell(t-\tau_r)\), their second coordinates differ by its negative, and their third coordinates are equal. Since \(\ell\) is a nondecreasing ramp of slope \(a/2\), total height \(1-p-b\), and duration \(L\), the maximum difference of ramps translated by \(\tau_r-\tau_g\) is
\[
\min\!\left\{\frac a2(\tau_r-\tau_g),\,1-p-b\right\}
=\min\!\left\{\frac b2(1-2a/H),\,1-p-b\right\}.
\]
It is attained at \(t=\min\{\tau_r,\tau_g+L\}\). Because \(p>0\) and \(H>2a\), the discrepancy is strictly less than
\[
\min\{b/2,1-b\}\le 1/3.
\]
The latter bound follows by splitting at \(b=2/3\). Choosing \(b=2/3\), \(a=1\), \(p\downarrow0\), and \(H\to\infty\) yields discrepancies converging to \(1/3\), establishing a sharp but unattained family supremum. The first-release time ratio is \(\tau_r/\tau_g=H/(2a)\), which is unbounded as \(H/a\to\infty\).

**4. Minimal cell count.** For two cells and any \(s\in(0,2)\), write feasible points \((z,s-z)\), with \(z\) in the interval \(I=[\max(0,s-1),\min(1,s)]\). For arbitrary costs \((c_1,c_2)\), projection of \((z_0,s-z_0)-t(c_1,c_2)\) onto this line segment has first coordinate
\[
\operatorname{proj}_{I}\bigl(z_0-t(c_1-c_2)/2\bigr).
\]
The tangent-projected flow has the constant interior first-coordinate speed \(-(c_1-c_2)/2\) and stops at the first endpoint reached along its direction. Thus the same interval-projection formula holds at all times. Degenerate masses \(s\in\{0,2\}\) give a singleton and also agree. A one-cell feasible set is a singleton. This proves the sharp three-cell onset.

## Verification

The standalone Python 3 file `verify.py` uses only `fractions`, `itertools`, and `random` from the standard library and asserts 7,007 exact-rational family comparisons plus 300 exact two-cell cases. It independently computes capped-simplex projections by enumerating bound/free active sets (with a breakpoint fallback), compares them with the formulas on random rational parameter sets and times, verifies a 128-step local projection iteration on the rational witness, and tests the limiting sharpness. Run `python3 verify.py` from the extraction directory; expected output begins `VERIFY_OK 7007` and ends `VERIFY_2CELL_OK 300`. The general theorem is proved analytically above; finite tests are not used to infer its universal quantifiers.

For the concrete data \(p=b=1/4\), \(a=1\), \(H=8\), one has \(s=3/2\), \(\tau_g=1/16\), \(\tau_r=1/4\), maximum discrepancy \(3/32\), and first-release ratio four.

## Relationship to prior work

Langlois, Onwunta, and Darbon [1] prove piecewise explicit minimal-selection trajectories for linear and quadratic programming, develop algorithms for the flow, and apply their optimization framework to conservative positivity limiters. Their work supplies the correct tangent-projection dynamics. The present theorem instead compares that continuous trajectory to the **single accumulated-drift projection** on a mass-conserving capped simplex, and optimizes their time-dependent gap over an explicit natural parameter family. The exact three-site onset, sharp \(1/3\) envelope, and unbounded release-time ratio are not stated by their general flow theorem. Wang and Lu [2] characterize the capped-simplex Euclidean projection by KKT equations; these are used as existing ingredients, not attributed here as new. General projected-gradient-flow overviews [3] describe the infinitesimal projected iteration, which must not be confused with a single finite projection of the cumulative drift.

## Limitations

The sharp \(1/3\) envelope is **only over the parameter family stated above**, not all three-dimensional or higher-dimensional polytopes, all costs, or all initial states. This is a comparison of continuous projected descent against a *one-shot* drift projection, not a claim that repeated projected Euler steps fail to converge to the flow. No PDE discretization instability or failure of a specific limiter is asserted. Historical-priority risk remains because a general projection-semigroup or sweeping-process theorem might imply some or all of this comparison even without the same numerical constants.

## References

[1] G. P. Langlois, A. Onwunta, and J. Darbon, *Continuous-time analysis and algorithms for linear and convex quadratic programs via exactly solvable differential inclusions*, arXiv:2610.30300v1, first publicly posted 21 October 2026. https://arxiv.org/html/2610.30300v1

[2] W. Wang and C. Lu, *Projection onto the capped simplex*, arXiv:1503.01002, 3 March 2015. https://arxiv.org/abs/1503.01002

[3] *Optimization algorithms as robust feedback controllers*, Annual Reviews in Control (2024), DOI:10.1016/j.arcontrol.2024.100941. https://doi.org/10.1016/j.arcontrol.2024.100941
