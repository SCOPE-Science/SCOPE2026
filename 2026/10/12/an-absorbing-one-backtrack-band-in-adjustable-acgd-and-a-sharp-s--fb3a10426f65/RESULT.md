# An absorbing one-backtrack band in adjustable ACGD, and a sharp scalar rate tradeoff

## Finding
Consider the adjustable-scaling AdaStep rule used by Adaptive Conditional Gradient Descent, specialized to unconstrained Euclidean normalized steepest descent on
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad \lambda>0.
\]
Let \(\delta>0\) be the source stabilizer in the local smoothness estimate, let \(\beta>1\) be the backtracking multiplier, let \(r\in\mathbb N\) be the adjustable-scaling checkpoint period, and let \(\gamma\in(0,1]\) be the scaling factor applied to the local estimate. Define
\[
\tau=\frac{\lambda}{\lambda+\delta}\in(0,1).
\]
At every nonzero iterate, the raw gradient-difference estimate is exactly \(\lambda+\delta\). If \(j(\gamma)\) denotes the number of backtracking multiplications in the current iteration, then
\[
j(\gamma)=\min\left\{j\in\mathbb N_0:\beta^j\gamma\ge\tau\right\}.
\]
The accepted effective curvature is
\[
M(\gamma)=\beta^{j(\gamma)}\gamma(\lambda+\delta),
\]
and the exact iterate map is
\[
x^+=\left(1-\frac{\lambda}{M(\gamma)}\right)x
=\left(1-\frac{\tau}{\beta^{j(\gamma)}\gamma}\right)x.
\]

The source's adjustable rule updates \(\gamma\) after each block of \(r\) iterations according to the total number of backtracks in that block: no backtracking decreases \(\gamma\), more than \(r\) backtracks increases \(\gamma\), and a positive total not exceeding \(r\) leaves \(\gamma\) unchanged. It follows that every
\[
\gamma\in\left(\frac{\tau}{\beta},\tau\right)
\]
is an absorbing scaling state as long as the iterate is nonzero. Indeed, exactly one backtrack occurs on every iteration, so every checkpoint block contains exactly \(r\) backtracks and the feedback leaves \(\gamma\) fixed. On this entire absorbing band the exact Q-linear factor is
\[
\rho(\gamma)=1-\frac{\tau}{\beta\gamma},
\qquad
0<\rho(\gamma)<1-\frac1\beta.
\]
As \(\gamma\) moves through the band, \(\rho(\gamma)\) ranges continuously from values arbitrarily close to \(0\) to values arbitrarily close to \(1-1/\beta\). At the lower endpoint \(\gamma=\tau/\beta\), one accepted step has \(M=\lambda\) and reaches the minimizer exactly, so the persistent-band statement is naturally open at that endpoint.

Thus the adjustable backtracking feedback does not identify a unique local curvature or a unique asymptotic rate even in a one-dimensional constant-curvature problem. Its balanced state controls backtracking work, not the exact contraction factor.

For the parameter values used as defaults in the source experiments,
\[
\beta=2,
\qquad r=10,
\qquad \gamma_0=\frac14,
\qquad \delta=10^{-10},
\]
and for \(\lambda=1\), one has
\[
\tau=\frac{1}{1+10^{-10}}.
\]
Initially \(j(\gamma_0)=2\), so each ten-iteration checkpoint block contains twenty backtracks and the adjustable rule multiplies \(\gamma\) by \(1.1\). The first checkpoint index at which \(\gamma\ge\tau/2\) is
\[
N=\left\lceil
\frac{\log(2\tau)}{\log(1.1)}
\right\rceil=8.
\]
Hence
\[
\gamma_8=\frac14(1.1)^8=0.5358972025,
\]
which lies in \((\tau/2,\tau)\). From then on there is exactly one backtrack per iteration and the scale freezes. The exact iterate factor changes from
\[
\rho_0=1-\tau=\frac{\delta}{1+\delta}
\]
at the initial two-backtrack scale to
\[
\rho_8
=1-\frac{\tau}{2\gamma_8}
=0.0669852396738\ldots
\]
after the feedback reaches the one-backtrack band. The objective contraction factor therefore changes from \(\rho_0^2\) to
\[
\rho_8^2=0.00448702233416\ldots .
\]
The adjustment saves one backtracking trial per iteration but moves the scalar iteration away from its nearly exact-curvature step.

## Assumptions and scope
The result concerns the adjustable scaling variant of AdaStep in Adaptive Conditional Gradient Descent and the unconstrained Euclidean normalized-steepest-descent specialization. The objective is the scalar strongly convex quadratic above, the linear minimization oracle is exact, and the iterates are assumed nonzero when a new local gradient-difference estimate is formed. The endpoint case that reaches the minimizer in one step is treated separately.

The finding does not claim that adjustable scaling harms wall-clock performance or violates the convergence theorem of the source. Backtracking has a computational cost, and the source feedback is explicitly designed to adapt its scaling from observed backtracking. The theorem isolates the exact tradeoff between this cost signal and contraction rate on constant curvature.

## Proof
For the scalar quadratic,
\[
\nabla f(x)=\lambda x.
\]
Whenever \(x^k\ne x^{k-1}\), the source gradient-difference local estimate before scaling is
\[
\frac{|\nabla f(x^k)-\nabla f(x^{k-1})|}{|x^k-x^{k-1}|}+\delta
=\lambda+\delta.
\]
After applying scaling \(\gamma\) and \(j\) backtracking multiplications, the tested curvature is
\[
M=\beta^j\gamma(\lambda+\delta).
\]

For Euclidean normalized steepest descent, the unit-ball linear minimization oracle gives
\[
d=-\operatorname{sign}(x),
\qquad |d|=1,
\]
and the source short step is
\[
t=\frac{|\nabla f(x)|}{M}=\frac{\lambda|x|}{M}.
\]
The exact quadratic expansion is
\[
f(x+td)=f(x)+t\nabla f(x)d+\frac{\lambda}{2}t^2.
\]
The sufficient-decrease model used by the backtracking test replaces the last coefficient \(\lambda\) by \(M\). For \(x\ne0\), and therefore \(t>0\), the test succeeds exactly when
\[
\lambda\le M.
\]
Equivalently,
\[
\beta^j\gamma\ge\frac{\lambda}{\lambda+\delta}=\tau.
\]
Minimality of the number of backtracks gives the formula for \(j(\gamma)\).

The accepted update is
\[
x^+=x-\frac{\lambda|x|}{M}\operatorname{sign}(x)
=\left(1-\frac{\lambda}{M}\right)x,
\]
which yields the claimed exact factor.

If \(\tau/\beta<\gamma<\tau\), then the unbacktracked test fails but one multiplication by \(\beta\) succeeds. Thus \(j(\gamma)=1\) at every nonzero iterate. Over any checkpoint block of \(r\) iterations the total number of backtracks is exactly \(r\). The adjustable-scaling rule therefore leaves \(\gamma\) unchanged, proving absorption. Substituting \(j=1\) gives the factor \(\rho(\gamma)\). Its monotonicity in \(\gamma\), together with the two endpoint limits, gives the full rate interval.

For the source defaults at \(\lambda=1\), direct comparison shows
\[
2\gamma_0=\frac12<\tau<1=4\gamma_0,
\]
so \(j(\gamma_0)=2\). The scale after \(n\) aggressive checkpoint updates is
\[
\gamma_n=\frac14(1.1)^n.
\]
The first \(n\) with \(\gamma_n\ge\tau/2\) is \(8\), while \(\gamma_8<\tau\), so the scale enters the one-backtrack absorbing band there. The displayed contraction factors follow by substitution.

## Verification
The bundled script `artifacts/verify_acgd_absorbing_band.py` uses exact rational arithmetic for the default-parameter checkpoint count and contraction identities. It also checks the backtracking classification and update formula on a grid of rational scalings in the one-backtrack band.

The finite checks are not used as a proof of the quantified statement. The proof is the exact scalar algebra above.

## Relationship to prior work
Khademi and Silveti-Falls introduce Adaptive Conditional Gradient Descent and its AdaStep routine. Their adjustable scaling rule uses checkpointed backtracking counts to decrease, increase, or retain the local scaling factor, and their reported defaults include \(\gamma=1/4\), \(\beta=2\), and checkpoint period \(r=10\). The source establishes global convergence properties and motivates the scaling logic as a practical way to adapt local smoothness estimates. It does not state the scalar backtracking-count formula, the absorbing one-backtrack band, the continuum of exact contraction factors inside that band, or the default-parameter rate tradeoff proved here.

Pedregosa, Négiar, Askari, and Jaggi analyze Frank-Wolfe variants with a generic backtracking line search that multiplies a local curvature estimate until a quadratic upper model is valid. That work provides the broader factor-of-\(\beta\) localization principle behind backtracking, but it does not contain the 2025 source's checkpoint feedback that changes \(\gamma\) according to aggregate backtracking counts. Consequently it does not imply the absorbing-band result or the default eight-checkpoint trajectory.

Other adaptive-gradient results concerning objective spikes, Barzilai--Borwein intervals, Polyak steps, or persistence of estimated spectral endpoints use different step-selection maps. Their sharp quadratic phenomena do not imply this source-specific checkpoint fixed band.

## Limitations
The theorem is exact only for the scalar constant-curvature specialization. In multiple dimensions the local gradient-difference estimate depends on the active spectral mixture, so a single constant \(\tau\) need not govern every iteration. The statement also does not compare total runtime: fewer backtracking trials may compensate for a larger iteration contraction factor.

The source stabilizer \(\delta\) is retained exactly. If \(\delta=0\), the same formulas hold with \(\tau=1\), but the displayed numerical default trajectory uses the strictly positive value reported by the source.

## References
1. A. Khademi and A. Silveti-Falls, *Adaptive Conditional Gradient Descent*, arXiv:2510.11440, first public 2025-10-13; Optimization Online 32199.
2. F. Pedregosa, G. Négiar, A. Askari, and M. Jaggi, *Linearly Convergent Frank-Wolfe with Backtracking Line-Search*, Proceedings of AISTATS 2020, PMLR 108, arXiv:1806.05123.
