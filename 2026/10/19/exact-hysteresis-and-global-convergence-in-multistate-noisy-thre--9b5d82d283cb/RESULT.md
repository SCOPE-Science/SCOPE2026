# Exact hysteresis and global convergence in multistate noisy three-majority dynamics

## Finding

Fix an integer \(k\geq3\). In the synchronous, complete-mixing, three-sample plurality mechanism with independent uniform communication noise \(0<p<1\), the deterministic population-frequency update has **two distinct critical noise levels**
\[
p_{\mathrm{lin}}=\frac1{k+1},\qquad
p_{\mathrm{fold}}=\frac{k}{5k-4},\qquad
0<p_{\mathrm{lin}}<p_{\mathrm{fold}}<1.
\]
Every orbit of this deterministic map converges to a fixed point. Its locally asymptotically stable fixed points are exactly: (i) the equal-opinion state when \(p>p_{\mathrm{lin}}\); and (ii) the \(k\) permutations of a one-dominant-opinion state on the upper branch when \(0<p<p_{\mathrm{fold}}\). Thus, throughout the open interval \(p_{\mathrm{lin}}<p<p_{\mathrm{fold}}\), the disordered state and \(k\) different ordered states are simultaneously locally attracting. All other fixed points are not locally asymptotically stable. Endpoint statements refer to strict local asymptotic stability: at the lower threshold the disordered state is nonlinearly unstable, and at the upper threshold the merging ordered state is not locally asymptotically stable.

More explicitly, for each integer \(1\le r\le k-1\) every nonuniform fixed point has \(r\) equal larger *received-opinion* frequencies \(a\) and \(k-r\) equal smaller ones \(b\). Writing \(t=a/b>1\), all and only these fixed points are parametrized by
\[
a=\frac{t}{rt+k-r},\qquad
b=\frac1{rt+k-r},\qquad
p=\frac{kt}{(rt+k-r)^2+kt},\qquad
x_i=\frac{z_i-p/k}{1-p},
\]
where \(z_i\) equals \(a\) on the larger group and \(b\) on the smaller group. A nonuniform fixed point is locally asymptotically stable **if and only if** \(r=1\) and \(t>k-1\).

For \(k=3\), choose \(p=9/34\), which lies strictly between \(1/4\) and \(3/11\). There are exactly seven fixed points: the uniform state, three permutations of \((87,19,19)/125\), and three permutations of \((53,36,36)/125\). Exactly four are locally attracting (the uniform state and the first set of three); the remaining three are saddles. The coexistence is an exact rational phenomenon, not an inference from simulation.

## Assumptions and scope

The state space is the \((k-1)\)-simplex \(\Delta_k=\{x\in\mathbb R^k:x_i\ge0,\ \sum_i x_i=1\}\). At each synchronous update, each individual draws three independent opinions with replacement from the current population composition. Each message independently is replaced, with probability \(p\), by a uniformly random opinion from the \(k\) labels; otherwise it is delivered unchanged. The update chooses the label appearing at least twice, or, if the three received labels are distinct, chooses uniformly among the three. The deterministic frequency map is the exact conditional expectation for complete mixing with uniform population draws, equivalently the infinite-population frequency update. It is not an assertion that a finite random population follows the deterministic orbit sample by sample.

Let \(z_i=(1-p)x_i+p/k\), let \(S(z)=\sum_{j=1}^{k}z_j^2\), and set
\[
F_{p,i}(x)=z_i\bigl(1+z_i-S(z)\bigr),\quad 1\le i\le k.
\]
The three-sample rule yields this map exactly. The claims concern \(F_p:\Delta_k\to\Delta_k\), fixed-point stability relative to \(\Delta_k\), and all forward iterates for any \(x(0)\in\Delta_k\), with fixed integer \(k\ge3\) and fixed real \(0<p<1\). In particular the theorem does not assert a finite-population noise threshold, an exponentially long stochastic metastability law, or a high-probability convergence time.

## Proof

**1. Exact update map.** Given received-label probabilities \(z\), output label \(i\) occurs with probability \(z_i^3+3z_i^2(1-z_i)\) from at least two appearances, and with probability \(2z_i\sum_{j<\ell,\ j,\ell\ne i}z_jz_\ell\) from three-way ties. Because \(\sum_i z_i=1\), this simplifies exactly to \(F_{p,i}(x)=z_i(1+z_i-S(z))\). Each coordinate is positive when \(p>0\) and the coordinates sum to one.

**2. Exhaustive fixed-point classification.** If \(x=F_p(x)\), substitute \(x_i=(z_i-p/k)/(1-p)\). Every received frequency \(z_i>0\) satisfies the same quadratic equation
\[
(1-p)z_i^2-[p+(1-p)S(z)]z_i+\frac pk=0.
\]
Hence there are at most two distinct coordinate values. If there are two, write \(a>b>0\) with multiplicities \(r\) and \(k-r\), respectively. The product-of-roots identity is \(ab=p/[k(1-p)]\); the normalization \(ra+(k-r)b=1\) and \(t=a/b\) give the displayed parametrization. Conversely, for any \(r,t,p\) satisfying the parametrization, the sum-of-roots identity follows from \(a+b=S(z)+kab\) (itself a consequence of normalization), so these formulae give a fixed point. For fixed \(p>0\) and \(r\), the equation for \(t\) is quadratic with nonzero leading coefficient; there are only finitely many fixed points, including the uniform point \(x_i=1/k\).

**3. Linear stability of nonuniform points.** The map Jacobian is the symmetric matrix
\[
DF_p(x)=(1-p)\left[\operatorname{diag}(1+2z_i-S(z))-2zz^{\mathsf T}\right].
\]
For every real vector \(v\), weighted Cauchy--Schwarz gives
\[
v^{\mathsf T}DF_p(x)v\ge(1-p)(1-S(z))\|v\|^2>0
\]
because \(\sum_i z_i=1\) and all \(z_i>0\). Thus all eigenvalues on the invariant tangent space \(\sum_i v_i=0\) are positive. At a two-level fixed point, tangent perturbations splitting the \(r\) high coordinates have eigenvalue
\[
\lambda_{\mathrm{high}}=1+(1-p)(a-b)>1
\]
with multiplicity \(r-1\). Perturbations splitting the \(k-r\) low coordinates have eigenvalue
\[
\lambda_{\mathrm{low}}=1-(1-p)(a-b)<1
\]
with multiplicity \(k-r-1\). The final, group-contrast eigenvalue is
\[
\lambda_{\mathrm{contrast}}=1+(1-p)(a-b)(1-2ra)
=1+(1-p)(a-b)\frac{k-r-rt}{rt+k-r}.
\]
If \(r\ge2\), the high-splitting eigenvalue is larger than one, so the fixed point is unstable. If \(r=1\), the other eigenvalues are in \((0,1)\) and the contrast eigenvalue is below one exactly when \(t>k-1\), above one when \(1<t<k-1\), and equal to one at equality. This proves hyperbolic stability or instability away from the boundary cases.

**4. Exact folds, uniform state, and boundary cases.** For \(r=1\) the fixed-point parameter curve is
\[
p(t)=\frac{kt}{(t+k-1)^2+kt},\qquad t>1.
\]
It increases from \(1/(k+1)\) at \(t=1\) to a unique maximum \(k/(5k-4)\) at \(t=k-1\), then decreases to zero. The equal-opinion state's \(k-1\) tangent eigenvalues are \((1-p)(1+1/k)\); it is hyperbolically attracting precisely for \(p>1/(k+1)\).

For completeness the nonhyperbolic cases are decided on the invariant one-high line \(x_1=1/k+u\), \(x_i=1/k-u/(k-1)\) for \(i>1\). The first-coordinate increment equals exactly
\[
F_{p,1}(x)-x_1=u\left[A+B u-Cu^2\right],\quad
A=(1-p)(1+1/k)-1,\quad B=\frac{(1-p)^2(k-2)}{k-1},\quad C=\frac{(1-p)^3k}{k-1}.
\]
At \(p=1/(k+1)\), \(A=0\) and \(B>0\), so arbitrarily small positive \(u\) are repelled from the uniform state. At \(p=k/(5k-4)\), the two positive nonuniform roots of the scalar fixed-point equation merge at \(u_*=B/(2C)\) and the increment is \(-Cu(u-u_*)^2\); points just below \(u_*\) move away from it. The merging point therefore is not locally asymptotically stable.

**5. Global convergence, not just linearization.** Define
\[
\Phi(x)=\frac1{1-p}\left[\frac12S(z)+\frac13\sum_i z_i^3-\frac14S(z)^2\right],\qquad
\mathcal L(x)=\Phi(x)-\frac12\|x\|^2.
\]
Direct differentiation yields \(\nabla\Phi(x)=F_p(x)\). Its Hessian, restricted to line segments in \(\Delta_k\), equals the positive-definite matrix in Step 3; hence \(\Phi\) is convex on the simplex. Set \(y=F_p(x)\). The supporting-plane inequality implies
\[
\mathcal L(y)-\mathcal L(x)\ge\frac12\|y-x\|^2.
\]
The continuous function \(\mathcal L\) is bounded on compact \(\Delta_k\), so \(\sum_{m\ge0}\|x(m+1)-x(m)\|^2<\infty\). Every accumulation point is therefore fixed. As Step 2 gives a *finite* fixed-point set and the step lengths tend to zero, an orbit cannot move infinitely often between disjoint small neighborhoods of different fixed points. Thus the entire orbit converges to one fixed point. This argument includes unstable and nonhyperbolic equilibria when initial conditions lie in their exceptional basins; it does not assert all orbits converge to a stable point.

**6. Rational witness.** At \(k=3\), \(p=9/34\), the two ratios on the one-high branches are \(t=3\) and \(t=4/3\). The corresponding fixed points are permutations of \((87,19,19)/125\) and \((53,36,36)/125\). Their tangent eigenvalue pairs are, respectively, \((12/17,16/17)\) and \((63/68,69/68)\). The uniform point has the tangent eigenvalue \(50/51\) with multiplicity two. No other fixed points exist because the \(r=2\) parameter branch lies below the uniform threshold for \(t>1\).

## Verification

The standalone Python program `verify.py` uses exact integer/rational arithmetic and SymPy. Run `python verify.py` with SymPy installed. It independently enumerates all ordered three-message samples for 24 rational probability profiles; checks 210 parametrized fixed points and complete tangent Jacobian eigenvalue multiplicities for \(3\le k\le9\); verifies four symbolic potential-gradient identities and forty exact Lyapunov inequalities; and checks the seven fixed points and eigenvalues in the rational example. All programmed checks pass. These finite checks support, but do not replace, the quantified algebraic and convexity proof above.

## Relationship to prior work

D'Amore and Ziccardi [1] prove high-probability finite-population results for **two** opinions and uniform communication noise, and expressly raise the many-opinion transition as a further question. The present result characterizes the exact **deterministic population-frequency** response for every finite number of opinions; it does not automatically settle finite-population metastability. Becchetti and collaborators [2] derive the three-majority sampling rule and analyze plurality consensus without communication noise; their formula informs Step 1, but their zero-noise convergence results do not imply these positive-noise folds. Nowak, Stoń, and Sznajd-Weron [3] find discontinuous transitions and two-level equilibria in a multistate noisy *q-voter* mechanism. That mechanism copies a unanimous panel or independently chooses a label, with sequential updates and noise applied at the agent decision, whereas here there are three **independently corrupted messages** followed by their plurality and a **synchronous** map. Its rate equation differs from the cubic map above, so its qualitative coexistence findings do not supply the exact thresholds or global convergence theorem here. Fraigniaud and Natale [4] treat multicolor noisy communication for different rumor/plurality protocols; their results do not prescribe this exact three-sample population-frequency map.

## Limitations

This is a mean-field theorem for a deterministic simplex map. It does not identify finite-population stationary distributions, escape times, high-probability phase transitions, or noise thresholds for sparse graphs. The presence of several stable fixed points does not by itself determine global basin volumes. The literal stochastic process with finite population size and sampling excluding an updating individual can differ at order \(1/N\). There remains a possibility of equivalent earlier formulae in specialist multistate majority-vote or stochastic-population literature; the closest located papers use mathematically different mechanisms. A separate independent scientific audit has not been performed.

## References

[1] F. d'Amore and I. Ziccardi, *Phase Transition of the 3-Majority Dynamics with Uniform Communication Noise*, arXiv:2112.03543, first version 2021-12-07. https://arxiv.org/abs/2112.03543

[2] L. Becchetti, A. Clementi, E. Natale, F. Pasquale, R. Silvestri, L. Trevisan, *Simple Dynamics for Plurality Consensus*, arXiv:1310.2858, first version 2013-10-10. https://arxiv.org/abs/1310.2858

[3] B. Nowak, B. Stoń, K. Sznajd-Weron, *Discontinuous phase transitions in the multi-state noisy q-voter model: quenched vs. annealed disorder*, Scientific Reports 11, 6098 (2021). https://doi.org/10.1038/s41598-021-85361-9

[4] P. Fraigniaud and E. Natale, *Noisy Rumor Spreading and Plurality Consensus*, arXiv:1507.05796, first version 2015-07-21. https://arxiv.org/abs/1507.05796
