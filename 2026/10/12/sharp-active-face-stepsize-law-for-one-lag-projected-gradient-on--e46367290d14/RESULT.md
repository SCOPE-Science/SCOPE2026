# Sharp active-face stepsize law for one-lag projected gradient on separable quadratics

## Finding
For any finite \(m\ge1\), consider the nonnegativity-constrained separable quadratic
\[
\min_{x\in\mathbb R^m_{\ge0}}f(x),\qquad
f(x)=\frac12\sum_{i=1}^{m}L_i(x_i-a_i)^2,
\quad L_i>0,\quad a_i\in\mathbb R.
\]
Let \(x_0,x_1\) be arbitrary feasible initial points and, for a fixed \(\eta>0\), take one delayed projected-gradient step per iteration:
\[
x_{k+1}=
\left[x_k-\eta\operatorname{diag}(L_1,\ldots,L_m)(x_{k-1}-a)\right]_+,
\qquad k\ge1.
\]
Here \([\cdot]_+\) denotes componentwise projection onto the nonnegative orthant. The unique minimizer is \(x_*=[a]_+\).

**Sharp global-convergence criterion.** The iterates converge to \(x_*\) for **every** feasible pair \((x_0,x_1)\) if and only if
\[
\boxed{\eta L_i<1\quad\text{for every index }i\text{ with }a_i>0.}
\]
There is no stepsize ceiling imposed by an index where \(a_i\le0\). More precisely, letting \(s_i=\eta L_i\), each coordinate behaves as follows.

* If \(a_i>0\), the corresponding recurrence converges geometrically for every initialization when \(0<s_i<1\); for \(s_i\ge1\), only the stationary initial pair \((a_i,a_i)\) can converge to \(a_i\).
* If \(a_i=0\), it converges for every \(s_i>0\). If \(s_i\ge1\), then its states at indices three and four, and all subsequent indices, vanish.
* If \(a_i<0\), it reaches the active minimizer exactly in finitely many steps for every \(s_i>0\), with the explicit upper bound given in the proof.

The result is a complete phase diagram for one-step stale information on diagonal bound-constrained strongly convex quadratics. In particular, strict complementarity changes the qualitative possibility of finite termination, while even an active coordinate without strict complementarity has no global step ceiling.

## Assumptions and scope
The iteration updates all coordinates simultaneously from the current vector, with a deterministic **one-iteration-old gradient**; this is a fixed-delay projected gradient scheme, not random coordinate selection and not a variable-delay asynchronous computation. The Hessian is strictly positive diagonal, so each coordinate follows an independent scalar recurrence. The projection is exact and arithmetic is exact. Initial states \(x_0,x_1\) are any nonnegative vectors, without requiring a separate conventional initial update. The phrase “global convergence” means convergence from every such initial pair, not an almost-sure guarantee under a random schedule.

## Proof
**Scalar reduction.** Fix one index, put \(s=\eta L>0\), and write its optimum parameter as \(a\in\mathbb R\). The recurrence reduces to
\[
 y_{k+1}=\max\{0,y_k-s(y_{k-1}-a)\},
\quad y_0,y_1\ge0.
\]
Its constrained minimizer is \(y_*=\max\{0,a\}\).

**Interior optimum and convergence below the exact threshold.** Suppose \(a\ge0\), and put \(e_k=y_k-a\), so \(e_k\ge-a\). For \(0<s<1\), let
\[
 c=\frac{s}{1+s},\qquad
 E(u,v)=u^2-2cuv+sv^2.
\]
The associated symmetric matrix
\[
 H_s=\begin{pmatrix}1&-c\\-c&s\end{pmatrix}
\]
is positive definite: its leading principal minor is one and
\[
 \det H_s=s-\frac{s^2}{(1+s)^2}>0.
\]
Write \(u=e_k\), \(v=e_{k-1}\), and the unprojected next error as \(w=u-sv\). Direct expansion gives the **exact identity**
\[
 E(w,u)-E(u,v)
 =-\frac{s(1-s)}{1+s}u^2-s(1-s)v^2.
\tag{1}
\]
The actual next error is \(z=\max\{-a,w\}\). If the projection is inactive, \(z=w\). If it acts, \(w<-a\) and \(z=-a\), so
\[
 E(z,u)-E(w,u)
 =(z-w)(z+w-2cu).
\]
Here \(z-w>0\), \(z+w<-2a\), and \(u\ge-a\), hence
\[
 z+w-2cu<-2a+2ca=-\frac{2a}{1+s}\le0.
\]
Thus projection never increases this energy. Combining with (1),
\[
 E(e_{k+1},e_k)
 \le E(e_k,e_{k-1})
 -\frac{s(1-s)}{1+s}e_k^2-s(1-s)e_{k-1}^2.
\tag{2}
\]
Since \(H_s\) is positive definite and the rightmost decrement is positive definite, there is a constant \(q_s\in(0,1)\), independent of the initial pair and of \(a\ge0\), such that
\[
 E(e_{k+1},e_k)\le q_s E(e_k,e_{k-1}).
\]
For instance, take
\[
 q_s=1-\frac{s(1-s)}{(1+s)\lambda_{\max}(H_s)}.
\]
This lies in \((0,1)\) because the exact identity is a difference of positive quadratic forms. Consequently \(e_k\to0\) geometrically. When \(a=0\), this proves convergence in the range \(0<s<1\) as well.

**Interior optimum at or above the threshold.** Suppose now \(a>0\) and \(s\ge1\). Were a feasible nonstationary trajectory to converge to \(a\), it would eventually stay strictly positive and obey the unprojected error equation
\[
 e_{k+1}=e_k-se_{k-1}.
\]
Its characteristic roots solve \(\lambda^2-\lambda+s=0\). Because \(s\ge1\), they are nonreal, each with modulus \(\sqrt{s}\ge1\). No nonzero solution of this second-order linear recurrence tends to zero. Hence some consecutive error pair would have to be identically zero. But if two consecutive states equal \(a>0\), the positive (unclipped) recurrence forces the preceding state also to equal \(a\); backward induction gives \(y_0=y_1=a\), contrary to nonstationarity. Therefore no other initial pair converges. Sharpness at the boundary is visible without asymptotic reasoning: for \(a=1\), \(s=1\), \(y_0=3/2\), and \(y_1=1\), all terms stay positive and repeat the nonoptimal six-cycle
\[
 \frac32,\quad1,\quad\frac12,\quad\frac12,\quad1,\quad\frac32,\quad\frac32,\ldots .
\]

**Active optimum with zero multiplier.** If \(a=0\), then
\[
 0\le y_{k+1}=\max\{0,y_k-sy_{k-1}\}\le y_k.
\]
Thus \((y_k)_{k\ge1}\) decreases to a limit \(\ell\ge0\). Passing to the limit yields \(\ell=\max\{0,(1-s)\ell\}\), hence \(\ell=0\) for every \(s>0\). Moreover, for \(s\ge1\), \(y_2\le y_1\), and therefore
\[
 y_3=\max\{0,y_2-sy_1\}=0,
 \qquad y_4=\max\{0,-sy_2\}=0.
\]
All later terms are zero.

**Strictly active optimum.** If \(a<0\), then \(y_{k-1}\ge0\) implies
\[
 0\le y_{k+1}
 =\max\{0,y_k-sy_{k-1}-s|a|\}
 \le \max\{0,y_k-s|a|\}.
\]
Iteration yields the explicit bound
\[
 y_k\le \max\{0,y_1-(k-1)s|a|\},\qquad k\ge1.
\]
Therefore \(y_k=0\) no later than
\[
 k=1+\left\lceil\frac{y_1}{s|a|}\right\rceil.
\]
Once a zero is reached it remains zero, since the stale value is nonnegative and \(a<0\).

**All-dimensional conclusion.** Every coordinate is independent. If all strictly interior indices satisfy \(s_i<1\), each coordinate converges by the relevant case above and the finite vector converges. If any such index satisfies \(s_i\ge1\), choose a feasible initial pair nonstationary only on that coordinate and stationary at all others. That coordinate cannot converge; thus global convergence of the vector is impossible. This completes necessity and sufficiency.

## Verification
The embedded standalone `verify.py` replays the exact nonoptimal six-cycle at the critical interior step \(s=1\), checks finite-time absorption at the boundary \(a=0\) for rational steps \(s\ge1\), checks strict-activity finite termination for rational cases, and checks exact rational instances of the Lyapunov identity (1) and projection inequality (2). The first-listed MSC and original public submission dates are documented by the cited bibliographic records; the executable checks only the mathematics. These finite checks corroborate but do not substitute for the universal analytic proof.

## Relationship to prior work
Liu, Wright, Ré, Bittorf, and Sridhar (2013) developed asynchronous stochastic coordinate descent for smooth functions with separable constraints. Liu and Wright (2014) presented a stochastic proximal-coordinate framework with stale gradient readings and bounded delay. In their full open manuscript, the update is current-state proximal projection of a delayed coordinate gradient, and the convergence theorem imposes quantitative stepsize/delay conditions. These are classical methodological foundations, not the present claimed contribution. Their algorithms involve random coordinate selection and more general objectives.

The result here concerns the deterministic one-step stale recurrence on a diagonal, orthant-constrained strongly convex quadratic. It identifies an **if-and-only-if** global convergence criterion depending on whether the *constrained optimizer* is interior in each coordinate; this is not implied by general small-step sufficient conditions or by an unconstrained spectral-radius argument. The proof uses a quadratic energy whose decrease persists through clipping, and separately captures the unlimited-step and finite-termination behavior of active coordinates. Literature searches for equivalent stale-gradient recurrences, active-set-specific step thresholds, and period-six boundary cycles did not identify this exact trichotomy. The distinction remains limited to the specified one-lag, diagonal system.

## Limitations
This is an exact-arithmetic theorem about fixed deterministic lag one, simultaneous vector updates, independent diagonal curvature, and projection onto the nonnegative orthant. It makes no claim for general coupled positive-definite Hessians, stochastic coordinate-selection schedules, inconsistent reads of different ages, noise, or floating-point effects. The geometric contraction constant supplied in the proof is sufficient, not asserted rate-optimal; the sharp quantity is the **convergence interval**, not the rate. Classical coordinate-descent and delayed fixed-point literature may contain the same scalar trichotomy under different terminology; this is a residual originality risk. Finite replay examples do not prove global convergence.

## References
1. J. Liu, S. J. Wright, C. Ré, V. Bittorf, and S. Sridhar, “An Asynchronous Parallel Stochastic Coordinate Descent Algorithm,” arXiv:1311.1873v1, submitted 2013-11-08; Journal of Machine Learning Research 16 (2015), 285–322.
2. J. Liu and S. J. Wright, “Asynchronous Stochastic Coordinate Descent: Parallelism and Convergence Properties,” arXiv:1403.3862v1, submitted 2014-03-15; SIAM Journal on Optimization 25 (2015), 351–376, DOI 10.1137/140961134. The journal's first-listed MSC is 90C25.
