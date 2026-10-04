# Square-root confidence horizons are globally minimax for worst fixed-time-relative width
## Finding
Fix \(\Delta>1\) and \(\alpha\in(0,1)\). Let \(W\) be standard Brownian motion. Consider any deterministic boundary \(g:[1,\Delta]\to(0,\infty)\) calibrated so that
\[
\Pr\!\left( |W(s)|\le g(s)\text{ for every }s\in[1,\Delta]\right)\ge 1-\alpha.
\]
Let \(z_\alpha=\Phi^{-1}(1-\alpha/2)\), and let \(c_\alpha(\Delta)\) denote the \(1-\alpha\) quantile of
\[
\sup_{1\le s\le\Delta}\frac{|W(s)|}{\sqrt{s}}.
\]
For a Brownian boundary \(g\), define its worst fixed-time-relative half-width by
\[
R(g)=\sup_{1\le s\le\Delta}\frac{g(s)}{z_\alpha\sqrt{s}}.
\]
Then
\[
\inf_g R(g)=\frac{c_\alpha(\Delta)}{z_\alpha},
\]
where the infimum is over all calibrated deterministic boundaries above, and it is attained by
\[
g_*(s)=c_\alpha(\Delta)\sqrt{s}.
\]
Thus the square-root, or Pocock-shaped, boundary is globally minimax for this precision criterion. In the power-boundary confidence-horizon family of Mathis and Waudby-Smith, this is exactly the member \(q=1/2\).

## Assumptions and scope
The claim concerns the Brownian limiting calibration used for bounded-horizon asymptotic confidence horizons. The horizon is the full continuum \([1,\Delta]\), the boundary is deterministic and fixed before observing the process, and the loss is the largest multiplicative half-width relative to a nominal fixed-time Gaussian interval at the same information time. No claim is made about expected stopping time, power against a specified alternative, average width, finite-sample exactness, or data-adaptive boundary selection.

For a partial-sum boundary \(g(s)\), the corresponding mean half-width at information time \(t=ms\) is asymptotically proportional to \(g(s)/s\). The fixed-time Gaussian half-width is proportional to \(z_\alpha/\sqrt{s}\). Their ratio is therefore exactly \(g(s)/(z_\alpha\sqrt{s})\) in the Brownian limit.

## Proof
Let \(K=R(g)\). By definition of the supremum,
\[
g(s)\le K z_\alpha\sqrt{s}\qquad\text{for every }s\in[1,\Delta].
\]
Hence the path event for the candidate boundary is contained in the path event for the square-root envelope:
\[
\left\{|W(s)|\le g(s)\text{ for every }s\right\}
\subseteq
\left\{|W(s)|\le K z_\alpha\sqrt{s}\text{ for every }s\right\}.
\]
If \(g\) has simultaneous coverage at least \(1-\alpha\), the right-hand event must therefore also have probability at least \(1-\alpha\). Equivalently,
\[
\Pr\!\left(\sup_{1\le s\le\Delta}\frac{|W(s)|}{\sqrt{s}}\le K z_\alpha\right)\ge 1-\alpha.
\]
By the definition of \(c_\alpha(\Delta)\), this forces
\[
K z_\alpha\ge c_\alpha(\Delta),
\]
and therefore \(R(g)\ge c_\alpha(\Delta)/z_\alpha\).

Now take \(g_*(s)=c_\alpha(\Delta)\sqrt{s}\). Its calibration event is exactly
\[
\left\{\sup_{1\le s\le\Delta}\frac{|W(s)|}{\sqrt{s}}\le c_\alpha(\Delta)\right\},
\]
which has probability \(1-\alpha\) under the continuous Brownian supremum distribution used in the confidence-horizon calibration. Moreover \(R(g_*)=c_\alpha(\Delta)/z_\alpha\). This attains the lower bound and proves the minimax statement.

For the power family in Confidence Horizons, the Brownian boundary is \(g_q(s)=c_q s^{1-q}\). Setting \(q=1/2\) gives a square-root boundary, so the source paper's \(q=1/2\) member realizes the global minimizer above.

## Verification
The proof is an event-inclusion argument and does not depend on numerical approximation. The critical steps checked directly are: (i) converting a Brownian partial-sum boundary \(g(s)\) into fixed-time-relative mean width \(g(s)/(z_\alpha\sqrt{s})\); (ii) the pointwise envelope \(g(s)\le R(g)z_\alpha\sqrt{s}\); and (iii) inversion of the square-root-boundary crossing probability at its \(1-\alpha\) quantile. A standalone script, `verify_boundary.py`, checks the deterministic envelope algebra on representative non-power and power boundary shapes; it is a reproducibility aid, not a substitute for the analytic proof.

## Relationship to prior work
Mathis and Waudby-Smith introduce confidence horizons, prove the power-boundary family for every real \(q\), identify \(q=1/2\) with a square-root/Pocock-type boundary, and analyze its Brownian crossing distribution. Their Appendix also records a time-reversal relation between \(q\) and \(1-q\), while their power discussion compares choices of \(q\) through power and expected rejection time. The paper does not state an optimization over arbitrary deterministic boundary functions under the worst fixed-time-relative-width criterion.

Wang and Tsiatis study a one-parameter family of approximately optimal group-sequential testing boundaries, with optimization criteria tied to testing design rather than the global repeated-interval width loss above. Jennison and Turnbull develop repeated confidence intervals for group-sequential trials, establishing the relevant repeated-inference framework, but the inspected abstract and metadata do not state this arbitrary-boundary minimax characterization.

## Limitations
The result is an asymptotic Brownian-design statement. It does not turn the \(q=1/2\) confidence horizon into a finite-sample confidence sequence, and it does not strengthen the source paper's uniformity mode for \(q=1/2\). The objective is specifically the maximum multiplicative half-width relative to fixed-time Gaussian inference; another criterion such as power, expected stopping time, average width, endpoint width, or a weighted loss can favor a different shape. No uniqueness claim is made: the theorem identifies the optimal value and an attaining boundary. Older group-sequential literature may contain an equivalent decision-theoretic observation under different terminology; targeted searches and the highly relevant sources inspected did not reveal one.

## References
1. Chase Mathis and Ian Waudby-Smith, “Confidence Horizons,” arXiv:2608.03889v1, first submitted 2026-08-04.
2. Samuel K. Wang and Anastasios A. Tsiatis, “Approximately Optimal One-Parameter Boundaries for Group Sequential Trials,” Biometrics 43(1), 1987, 193–199, DOI 10.2307/2531959.
3. Christopher Jennison and Bruce W. Turnbull, “Repeated Confidence Intervals for Group Sequential Clinical Trials,” Controlled Clinical Trials 5(1), 1984, 33–45, DOI 10.1016/0197-2456(84)90148-X.
