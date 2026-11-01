# Braess-free completion of a three-oscillator Kuramoto path, with sharp equality cases

## Finding
Consider three sine-coupled phase oscillators with constant intrinsic frequencies \(\Omega_1,\Omega_2,\Omega_3\in\mathbb R\), where \(\Omega_1+\Omega_2+\Omega_3=0\). The path edges \(12\) and \(23\) have positive weights \(w_1,w_2\), and the closing edge \(13\) has weight \(a\geq0\). All edge weights are multiplied by the common gain \(K>0\). Put
\[
K_0=\max\left\{\frac{|\Omega_1|}{w_1},\frac{|\Omega_3|}{w_2}\right\}.
\]
Call a phase-locked solution *exponentially stable* when the two nontrivial eigenvalues of its linearization, after quotienting the common-phase symmetry, have negative real parts. Let \(K_c(a)\) be the infimum of gains admitting such a solution.

**Theorem.** For every \(w_1,w_2>0\), every real zero-sum frequency triple, and every \(a\geq0\):

1. The path threshold is exactly \(K_c(0)=K_0\).
2. For every \(a\geq0\) and \(K>K_0\), exactly one phase-locked solution has both path-edge phase differences in \((-\pi/2,\pi/2)\). It is exponentially stable modulo common rotation.
3. For every \(a>0\), \(K_c(a)\leq K_0\). The inequality is strict **if and only if** \(\Omega_1/w_1\ne\Omega_3/w_2\). If the two normalized leaf frequencies coincide, then \(K_c(a)=K_0\), independently of the closing-edge weight. This includes the zero-frequency case, for which both thresholds are zero.

Thus adding the third positive edge to any positively weighted three-node path never produces a Braess increase of the phase-locking threshold. The characterization of equality is sharp and holds for arbitrarily strong added coupling, not just an infinitesimal perturbation.

## Assumptions and scope
The system is
\[
\dot\theta_i=\Omega_i+K\sum_{j\ne i}w_{ij}\sin(\theta_j-\theta_i),
\qquad w_{12}=w_{21}=w_1>0,\quad w_{23}=w_{32}=w_2>0,\quad w_{13}=w_{31}=a\geq0.
\]
There are no phase lags, delays, asymmetric weights, or inertial terms. Angles are modulo \(2\pi\), and a locked state is stationary in the zero-mean rotating frame. All statements about uniqueness are **restricted to the principal path-difference square**; no uniqueness is claimed among all phase classes on the torus. The threshold is defined using local exponential stability and is an infimum, so a nonhyperbolic equilibrium at exactly the threshold need not be exponentially stable.

Write \(\alpha=\theta_1-\theta_2\), \(\beta=\theta_3-\theta_2\), and \(\delta=\alpha-\beta\). A phase-locked state solves
\[
\Omega_1=K\bigl(w_1\sin\alpha+a\sin\delta\bigr),\qquad
\Omega_3=K\bigl(w_2\sin\beta-a\sin\delta\bigr).
\tag{1}
\]
The potential on the principal closed square \(Q=[-\pi/2,\pi/2]^2\) is
\[
U_K(\alpha,\beta)=K\bigl[w_1(1-\cos\alpha)+w_2(1-\cos\beta)+a(1-\cos(\alpha-\beta))\bigr]-\Omega_1\alpha-\Omega_3\beta.
\tag{2}
\]
Its critical points are exactly solutions of (1). The relative-phase flow is \(\dot z=-G\nabla U_K(z)\), where
\[
G=\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]
is positive definite. Consequently, positive definiteness of the Hessian of \(U_K\) at a critical point implies exponential attraction modulo the neutral common-phase direction.

## Proof
**Step 1: The original path threshold.** At \(a=0\), equations (1) give \(\sin\alpha=\Omega_1/(Kw_1)\), \(\sin\beta=\Omega_3/(Kw_2)\). For a tree, the two weighted cosines \(w_1\cos\alpha\) and \(w_2\cos\beta\) must both be positive for the phase Hessian to be positive definite modulo common phase: this follows immediately by using the two edge differences as independent coordinates. Such a phase lock exists exactly for \(K>K_0\), with the unique principal choice provided by the two inverse sines. Thus \(K_c(0)=K_0\), including \(K_0=0\).

**Step 2: A strict Hessian lemma at all gains \(K\geq K_0\).** Let \((\alpha,\beta)\) be any critical point strictly inside \(Q\), with \(K\geq K_0\). Apart from the positive factor \(K\), its Hessian is
\[
H_0=\operatorname{diag}(w_1\cos\alpha,w_2\cos\beta)
+a\cos\delta\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{3}
\]
If \(\cos\delta\geq0\), (3) is strictly positive definite. For \(\delta>\pi/2\), necessarily \(\alpha>0>\beta\). Since \(|\Omega_1/K|\leq w_1\) and \(|\Omega_3/K|\leq w_2\), equations (1) give
\[
a\sin\delta\leq w_1(1-\sin\alpha),\qquad
a\sin\delta\leq w_2(1+\sin\beta).
\tag{4}
\]
Put \(A=\pi/2-\alpha\), \(B=\pi/2+\beta\). Then \(A,B>0\), \(A+B=\pi-\delta\in(0,\pi/2)\), and (4) implies
\[
\begin{aligned}
a|\cos\delta|\left(\frac1{w_1\cos\alpha}+\frac1{w_2\cos\beta}\right)
&\leq\cot(A+B)\bigl[\tan(A/2)+\tan(B/2)\bigr]\\
&<1.
\end{aligned}
\tag{5}
\]
The strict inequality follows from \(\tan(A/2)+\tan(B/2)<\tan((A+B)/2)<\tan(A+B)\). The rank-one negative-update criterion for a positive diagonal matrix now proves that (3) is positive definite. The case \(\delta<-\pi/2\) follows by simultaneously changing the signs of \(\alpha,\beta,\Omega_1,\Omega_3\). This proves the lemma for every interior critical point, including all possible frustrated chord angles.

**Step 3: Existence and uniqueness above the path threshold.** If \(K>K_0\), the gradient of (2) points strictly outward on each face of \(Q\). For example, on \(\alpha=\pi/2\),
\[
\partial_\alpha U_K=K(w_1+a\cos\beta)-\Omega_1>0,
\]
and the three analogous inequalities hold on the other faces. Compactness yields an interior minimum. By Step 2 every interior critical point has a positive-definite Hessian and hence has local index \(+1\) for the gradient field. The outward-boundary degree of \(\nabla U_K\) on \(Q\) is \(+1\): equivalently, deform \(a\) continuously to zero, never encountering a boundary zero, and use the unique two-arcsine zero at \(a=0\). The zeros are isolated and finite by compactness and nonsingularity. Their local indices must sum to one, so there is exactly one. It is exponentially stable by the positive-definite metric relation displayed after (2).

**Step 4: The sharp strictness/equality alternative.** Suppose \(K_0>0\), \(a>0\), and \(\Omega_1/w_1\ne\Omega_3/w_2\). Minimize (2) over \(Q\) at \(K=K_0\). There can be no minimum in the relative interior of a face: for instance, on \(\alpha=\pi/2\) with \(|\beta|<\pi/2\), the outward normal derivative \(K_0(w_1+a\cos\beta)-\Omega_1\) is strictly positive. At a corner, if either relevant normalized leaf frequency is not saturated with that corner's sign, an inward coordinate motion lowers the energy. This leaves only corners where both leaf edges are saturated. The *same-sign* saturated corners require \(\Omega_1/w_1=\Omega_3/w_2\) and are excluded here. At an *opposite-sign* saturated corner, for example \((\alpha,\beta)=(\pi/2,-\pi/2)\), take the inward perturbation \((\pi/2-t,-\pi/2+t)\). Its energy difference from the corner is exactly
\[
K_0(w_1+w_2)(t-\sin t)+K_0a(\cos(2t)-1),
\tag{6}
\]
which is negative for every sufficiently small \(t>0\), since its leading term is \(-2K_0a t^2\). The opposite corner is symmetric. Thus no point of \(\partial Q\) minimizes the potential. There is an interior minimum, and Step 2 makes its Hessian positive definite. The implicit-function theorem therefore continues this exponentially stable equilibrium to all gains in some interval immediately **below** \(K_0\). Hence \(K_c(a)<K_0\).

Conversely, if \(\Omega_1/w_1=\Omega_3/w_2=c\), summing (1) cancels the closing-edge flow and gives
\[
c(w_1+w_2)=K(w_1\sin\alpha+w_2\sin\beta).
\]
For every phase lock, even one outside the principal square, this forces \(K\geq|c|=K_0\). Step 3 supplies exponentially stable principal locks for all larger gains. Therefore \(K_c(a)=K_0\). If \(K_0=0\), all frequencies vanish and synchronized stable states exist for every \(K>0\), again giving equality. This completes the classification.

**Exact witness.** With \(w_1=w_2=a=1\), \((\Omega_1,\Omega_2,\Omega_3)=(-1,0,1)\), the original path threshold equals one. The phase differences \((\alpha,\beta)=(-\pi/4,\pi/4)\) solve (1) at \(K=2-\sqrt2<1\), and (3) is diagonal positive because \(\cos(\alpha-\beta)=0\). In contrast, for frequencies \((1,-2,1)\) and the same weights, the exact threshold remains one for every \(a\geq0\), by the saturated center-node cut.

## Verification
The proof is independent of numerical tests. The included `CHECK.py` performs deterministic finite-precision checks of the exact strict-improvement and equality witnesses and of 450 additional unequal-weight parameter configurations with \(K=1.05K_0\). It reconstructs a principal-square stationary point by constrained energy minimization, checks the residual equations, and calculates the smallest Hessian eigenvalue. It has been executed successfully in Python 3 with NumPy and SciPy. Numerical checks are illustrations, not a replacement for the rank-one Hessian estimate, boundary corner analysis, or degree count.

## Relationship to prior work
Arches, Fleurantin, Holzer, Sood, and Uddin [1] study the first-order sensitivity of the phase-locking threshold when an edge is added to a network, along with network-scale Braess examples. The present result instead supplies a nonperturbative statement valid for every added-edge weight on the complete three-vertex motif, and classifies exactly when the tree threshold fails to improve. The primary paper's complete text was not available for direct comparison; its abstract and an independently rendered section-level account were available. Accordingly historical priority should be checked against that text before publication.

Witthaut and Timme [2] analyze how cycle constraints cause Braess-type desynchronization, with their explicit example involving a larger graph. Dekker and Taylor [3] establish threshold formulas for trees; the path threshold here is elementary and not claimed as new. Zhao and Zhou [4] analyze equilibria of three oscillators on an isosceles triangle, but the retrieved description concerns identical natural frequencies and does not provide this arbitrary-frequency edge-completion classification. A separately located four-oscillator example [5] describes a Braess penalty for a different motif; neither its threshold nor that of [1] is used as a premise of the proof.

## Limitations
The theorem proves no Braess increase when **completing a path of exactly three vertices** with a positive reciprocal sine edge. It does not assert that adding an edge to a larger graph cannot be harmful, or that every pre-existing stable locked state remains stable after edge addition. It does not classify all stable equilibria outside the principal square, global basins, inertial swing equations, negative or directed couplings, or phase-lagged models. Literature priority remains provisional because the full text of [1] was inaccessible in this review.

## References
[1] J. Arches, E. Fleurantin, M. Holzer, S. Sood, and S. Uddin, *Predicting the occurrence of Braess paradox in the synchronization threshold of coupled oscillator systems*, arXiv:2608.03594, first posted 2026-08-04. https://arxiv.org/abs/2608.03594

[2] D. Witthaut and M. Timme, *Braess's paradox in oscillator networks, desynchronization and power outage*, New Journal of Physics 14 (2012), 083036. https://doi.org/10.1088/1367-2630/14/8/083036

[3] A. H. Dekker and R. Taylor, *Synchronization Properties of Trees in the Kuramoto Model*, SIAM Journal on Applied Dynamical Systems 12 (2013), 596–617. https://doi.org/10.1137/120899728

[4] X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, Applied Mathematics Letters 158 (2024), 109246. https://arxiv.org/abs/2407.11314

[5] *Exact reversal of a Braess locking penalty on a four-oscillator cycle*, public mathematical research record, 2026-10-11, identifier fbd39164c275. (Comparison only; not a proof input.)
