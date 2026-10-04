# Warm-start correction for one-step over-relaxed ADMM on regularized quadratics
## Finding
Consider the strongly convex split quadratic
\[
\min_{x,z} \; \frac12 x^{\top}Qx+q^{\top}x+\frac{\delta}2\lVert z\rVert_2^2
\quad\text{subject to}\quad x=z,
\]
with \(Q\succ0\) and \(\delta>0\). For the over-relaxed ADMM iteration analyzed by Ghadimi, Teixeira, Shames, and Johansson, choose the paper's jointly rate-optimal parameters \(\rho=\delta\) and \(\alpha=2\). Let
\[
\eta^0:=\mu^0-\delta z^0,
\qquad
x^*=z^*=-(Q+\delta I)^{-1}q,
\qquad
\mu^*=\delta x^*.
\]
Then the first update satisfies
\[
x^1-x^*=-(Q+\delta I)^{-1}\eta^0,
\]
\[
z^1-x^*=\frac{1}{2\delta}(Q-\delta I)(Q+\delta I)^{-1}\eta^0,
\]
and \(\mu^1=\delta z^1\). Therefore the second update is exact:
\[
x^2=z^2=x^*,\qquad \mu^2=\delta x^*.
\]
Full one-update termination holds if and only if \(\eta^0=0\), equivalently \(\mu^0=\delta z^0\). Hence the source paper's statement that these parameters make the ADMM iterations converge in one iteration is valid on the dual-consistency initialization manifold. With the paper's general arbitrary-initialization convention, the exact uniform finite-termination bound is two updates.

## Assumptions and scope
The claim concerns only the split \(\ell_2\)-regularized quadratic model above, the unscaled dual variable \(\mu\), and the over-relaxed update convention used in equations (16) of the cited source. The matrix \(Q\) is real symmetric positive definite, \(\delta>0\), \(\rho=\delta\), and \(\alpha=2\). The starting values \(z^0\) and \(\mu^0\) are arbitrary; \(x^0\) is irrelevant because the first \(x\)-subproblem overwrites it. No claim is made for other splittings, inexact subproblem solves, adaptive penalties, floating-point finite termination, or inequality-constrained ADMM.

## Proof
For \(\rho=\delta\) and \(\alpha=2\), the source iteration becomes
\[
x^{k+1}=(Q+\delta I)^{-1}(\delta z^k-\mu^k-q),
\]
\[
z^{k+1}=\frac{\mu^k+\delta(2x^{k+1}-z^k)}{2\delta},
\]
\[
\mu^{k+1}=\mu^k+\delta\bigl(2(x^{k+1}-z^{k+1})-(z^k-z^{k+1})\bigr).
\]
The optimality equations give \(x^*=z^*=-(Q+\delta I)^{-1}q\) and \(\mu^*=\delta x^*\). Writing \(\eta^k=\mu^k-\delta z^k\), subtraction immediately gives
\[
x^{k+1}-x^*=-(Q+\delta I)^{-1}\eta^k.
\]
Using the \(z\)-update and the preceding identity,
\[
z^{k+1}-x^*=\frac{\eta^k}{2\delta}-(Q+\delta I)^{-1}\eta^k
=\frac{1}{2\delta}(Q-\delta I)(Q+\delta I)^{-1}\eta^k.
\]
Finally, multiplying the \(z\)-update by \(2\delta\) gives \(\mu^k+2\delta x^{k+1}-\delta z^k=2\delta z^{k+1}\). Substitution into the \(\mu\)-update yields \(\mu^{k+1}=\delta z^{k+1}\), so \(\eta^{k+1}=0\) after every completed update. Therefore \(\eta^1=0\) for arbitrary initialization. Applying the first two displayed error formulas with \(k=1\) gives \(x^2=x^*\) and \(z^2=x^*\), and then \(\mu^2=\delta x^*\).

For one-update termination of all primal-dual variables, \(x^1=x^*\) is necessary. Since \(Q+\delta I\) is invertible, the first error formula implies \(x^1=x^*\) if and only if \(\eta^0=0\). Under that condition the formula for \(z^1\) and the invariant \(\mu^1=\delta z^1\) also give \(z^1=x^*\) and \(\mu^1=\delta x^*\). This proves the equivalence.

A scalar witness makes the distinction explicit. Take \(Q=[2]\), \(\delta=1\), \(q=-3\), \(z^0=0\), and \(\mu^0=1\). Then \(x^*=1\), while the first update gives \(x^1=2/3\), \(z^1=7/6\), and \(\mu^1=7/6\), so one-update termination fails. The second update gives exactly \(x^2=z^2=\mu^2=1\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to replay the scalar counterexample and a family of scalar instances, checking the first-step formulas, the invariant \(\mu^1=\delta z^1\), and exact second-update termination. The general proof above is algebraic and does not depend on numerical experimentation.

The source paper explicitly defines ADMM with arbitrary initial \(x^0,z^0,\mu^0\), and its proof of the over-relaxed theorem derives \(\mu^{k+1}=\delta z^{k+1}\) before substituting \(\mu^k=\delta z^k\) into a reduced recurrence. That substitution is valid automatically from \(k=1\) onward, but at \(k=0\) it requires the additional initialization condition \(\mu^0=\delta z^0\).

## Relationship to prior work
Ghadimi, Teixeira, Shames, and Johansson derive the jointly optimal parameters \(\rho=\delta\), \(\alpha=2\) for this regularized quadratic model and state that the corresponding ADMM iterations converge in one iteration. Their general ADMM setup allows arbitrary primal and dual initial values. The present result isolates the initialization manifold needed for the one-update statement and gives the exact two-update global finite-termination law outside that manifold.

Targeted searches for the source title together with initialization, warm-start, one-iteration, dual-consistency, and finite-termination terms did not reveal an erratum or a publication stating this correction. published-finding corpus searches for the same claim and its equivalent formulations returned findings about other first-order methods and initialization effects, but no result matching this ADMM initialization manifold or the exact two-update law. A later global-rate paper by Giselsson and Boyd cites the source and studies tight Douglas--Rachford/ADMM rate bounds and metric selection; the inspected relevant sections do not discuss this finite-termination initialization point.

## Limitations
The originality check cannot exclude an unindexed note, informal erratum, code comment, or later paper that mentions the same initialization issue without searchable wording. The result corrects the interpretation of a finite-termination statement; it does not alter the source paper's rate-optimal parameter calculation on the invariant state manifold. Exact two-update termination is an exact-arithmetic statement and can be blurred by inexact linear solves or floating-point roundoff.

## References
E. Ghadimi, A. Teixeira, I. Shames, and M. Johansson, *Optimal parameter selection for the alternating direction method of multipliers (ADMM): quadratic problems*. Optimization Online, first posted 2013-06-10; arXiv:1306.2454; later published in IEEE Transactions on Automatic Control 60(3), 2015, DOI 10.1109/TAC.2014.2354892.

P. Giselsson and S. Boyd, *Linear Convergence and Metric Selection for Douglas-Rachford Splitting and ADMM*. arXiv:1410.8479; later published in IEEE Transactions on Automatic Control 62(2), 2017.
