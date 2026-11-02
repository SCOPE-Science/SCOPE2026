# A geometric nilpotency classification for exact-line-search PolyCD with away steps on triangles

## Finding

Let \(T=\operatorname{conv}\{v_1,v_2,v_3\}\subset\mathbb R^2\) be a nondegenerate triangle, \(H\in\mathbb R^{2\times2}\) symmetric positive definite, and \(t\in\operatorname{int}T\). Apply the exact-line-search PolyCD-with-away-steps (PolyCDwA) algorithm of Mazumder and Wang to
\[
f(x)=\tfrac12(x-t)^\top H(x-t),\qquad x\in T,
\]
using the three vertices once per sweep in a fixed permutation \(\pi=(\pi_1,\pi_2,\pi_3)\). Let \(F_\pi\) denote the completed-sweep map, and put
\[
n_i=v_i-t,\quad D_i=n_i^\top Hn_i,\quad
c_{ij}=\frac{n_i^\top Hn_j}{\sqrt{D_iD_j}}.
\]
Then \(F_\pi\) is analytic near \(t\), fixes \(t\), and its exact linearization \(J_\pi=DF_\pi(t)\) satisfies
\[
\|J_\pi\|_H=|c_{\pi_1\pi_2}c_{\pi_2\pi_3}|<1,
\quad \det J_\pi=0,\quad
\operatorname{tr}J_\pi=c_{12}c_{23}c_{31}=:\lambda_*,\quad
J_\pi^2=\lambda_*J_\pi.
\]
The nonzero eigenvalue, when present, is independent of vertex ordering. Exactly the following possibilities arise.

1. If none of the three \(H\)-inner products \(n_i^\top Hn_j\) vanish, then \(J_\pi\) has rank one and \(\lambda_*\neq0\) for every permutation. The derivative of no positive power of \(F_\pi\) at \(t\) vanishes; the leading local asymptotic spectral rate is \(|\lambda_*|\).
2. If the unique \(H\)-orthogonal vertex pair is **consecutive** in the order \(\pi\), then \(J_\pi=0\) and
\[
\|F_\pi(x)-t\|_H=O(\|x-t\|_H^2)\qquad(x\to t).
\]
Thus completed sweeps converge locally at least quadratically.
3. If the unique orthogonal pair occurs as the **first and third** vertices of \(\pi\), then \(J_\pi\neq0\) but \(J_\pi^2=0\). One completed sweep is not uniformly quadratic, whereas
\[
\|F_\pi^2(x)-t\|_H=O(\|x-t\|_H^2)\qquad(x\to t).
\]
Hence grouping sweeps into pairs gives at least quadratic local convergence.

Two distinct vertex pairs cannot simultaneously be \(H\)-orthogonal for an interior \(t\). For a chosen pair \(i,j\), its exceptional targets form precisely the interior part of the \(H\)-metric circle
\[
\left\|t-\tfrac12(v_i+v_j)\right\|_H^2=
\tfrac14\|v_i-v_j\|_H^2.
\]
That circle meets \(\operatorname{int}T\) if and only if the opposite \(H\)-angle is acute, meaning
\[
(v_i-v_k)^\top H(v_j-v_k)>0,
\qquad \{i,j,k\}=\{1,2,3\}.
\]

The two exceptional local orders are not merely formal: for \(H=I\), \(v_1=(0,0)\), \(v_2=(2,0)\), \(v_3=(0,2)\), and \(t=(2/5,4/5)\), the pair \(1,2\) is orthogonal. With \(e_1=(1,0)\),
\[
F_{(1,2,3)}(t+\varepsilon e_1)-t
=\varepsilon^2(-3/5,-1/5)+O(\varepsilon^3),
\]
whereas
\[
DF_{(1,3,2)}(t)=
\begin{pmatrix}1/5&-1/10\\2/5&-1/5\end{pmatrix}\neq0,
\qquad DF_{(1,3,2)}(t)^2=0,
\]
and
\[
F_{(1,3,2)}^2(t+\varepsilon e_1)-t
=\varepsilon^2(1/40,1/20)+O(\varepsilon^3).
\]
In contrast, ordinary PolyCD, whose steps are restricted to the forward line segment, has a nonzero first-order error for that same start and ordering:
\[
F_{\mathrm{forward},(1,2,3)}(t+\varepsilon e_1)-t
=\varepsilon(3/5,1/5)+O(\varepsilon^2)
\quad(\varepsilon\downarrow0).
\]
Thus the away-step feasibility, not simply a change of the vertex order, enables the quadratic cancellation.

## Assumptions and scope

All vertices are distinct and affinely independent in \(\mathbb R^2\). The minimizer is strictly interior, the Hessian is constant and positive definite, each vertex is visited exactly once in a fixed cyclic order, and the one-dimensional line search is **exact** on the feasible interval from Algorithm 2 of [1]. For an interior triangle point, the barycentric representation is unique. The stated map \(F_\pi\) is the primal map of this exact algorithm, including its actual away-step constraint; it is not a surrogate projection algorithm. The norm \(\|z\|_H=\sqrt{z^\top Hz}\) and corresponding induced matrix norm are used throughout. All asymptotics are local around \(t\) and with \(\varepsilon>0\).

## Proof

**Step 1: Feasible local exact updates.** The barycentric coordinates \(\ell_i(t)\) are strictly between zero and one. The algorithm permits steps \(\alpha\in[-\ell_i(x)/(1-\ell_i(x)),1]\). At \(x=t\) the exact unconstrained step is \(\alpha=0\), strictly inside this interval. By continuity, all three intermediate updates remain interior-feasible for sufficiently small \(\|x-t\|_H\), so none of their line-search bounds is active. The exact quadratic line search along \(d=v_i-x\) then gives the analytic map
\[
T_i(x)=x-\frac{(x-t)^\top H(v_i-x)}{(v_i-x)^\top H(v_i-x)}(v_i-x).
\]
The denominator is positive near \(t\). Differentiating at \(t\) yields
\[
P_i:=DT_i(t)=I-\frac{n_in_i^\top H}{D_i}.
\]
These are \(H\)-orthogonal rank-one projections onto the lines \(n_i^{\perp_H}\). Thus \(J_\pi=P_{\pi_3}P_{\pi_2}P_{\pi_1}\).

**Step 2: Complete projector product.** Change coordinates by \(H^{1/2}\). Let \(u_i=H^{1/2}n_i/\sqrt{D_i}\), and choose unit vectors \(q_i\) obtained by rotating all \(u_i\) by the same right angle. Then \(H^{1/2}P_iH^{-1/2}=q_iq_i^\top\) and \(q_i^\top q_j=c_{ij}\). Therefore
\[
H^{1/2}J_\pi H^{-1/2}
=c_{\pi_3\pi_2}c_{\pi_2\pi_1}
q_{\pi_3}q_{\pi_1}^\top.
\]
The induced norm is the absolute coefficient, the trace is \(c_{\pi_1\pi_2}c_{\pi_2\pi_3}c_{\pi_3\pi_1}\), and the determinant is zero. The Cayley--Hamilton identity gives \(J_\pi^2=\lambda_*J_\pi\). Since \(t\) is strictly interior, no two vectors \(n_i,n_j\) are parallel; hence \(|c_{ij}|<1\), giving \(\|J_\pi\|_H<1\) and local attraction.

**Step 3: Exhaustiveness and orders.** If two distinct pairs were orthogonal, their two nonshared normals would be parallel to each other; the corresponding two vertices and \(t\) would be collinear, contradicting strict interiority. Thus at most one pair is orthogonal. When none is, the rank-one expression is nonzero and its trace is nonzero. When a pair is consecutive, one of its two scalar factors is zero, so \(J_\pi=0\). When the pair occupies the first and third positions, both scalar factors are nonzero, but the trace is zero: \(J_\pi\) is nonzero and square-zero. Analyticity gives \(F_\pi(t+e)=t+J_\pi e+O(\|e\|_H^2)\), and by the chain rule \(D(F_\pi^2)(t)=J_\pi^2\). Hence the claimed one- versus two-sweep quadratic estimates. When \(J_\pi\neq0\), a direction with \(J_\pi e\neq0\) rules out a uniform one-sweep quadratic estimate; when \(\lambda_*\neq0\), \(J_\pi^m=\lambda_*^{m-1}J_\pi\neq0\) for all \(m\ge1\). The norm bound from Step 2 and a local mean-value estimate establish convergence of all sufficiently close iterates.

**Step 4: Metric-circle locus.** The identity
\[
(v_i-t)^\top H(v_j-t)
=\left\|t-\tfrac12(v_i+v_j)\right\|_H^2
-\tfrac14\|v_i-v_j\|_H^2
\]
gives the circle. Its closed disk is convex and contains the open edge \((v_i,v_j)\) in its interior. If \((v_i-v_k)^\top H(v_j-v_k)\le0\), the opposite vertex lies on or inside the disk, so every interior triangle point lies strictly inside it and the circle misses the interior. If this product is positive, the opposite vertex lies outside; joining it to the midpoint of edge \(i,j\) crosses the circle inside the triangle. This proves the if-and-only-if characterization and, with Step 3, the disjointness of exceptional arcs.

**Step 5: Nontrivial example.** The example has positive barycentric weights \((2/5,1/5,2/5)\) and \(n_1^\top n_2=0\), with the other inner products nonzero. Substituting the rational data into the exact maps from Step 1, differentiating the rational functions with respect to \(\varepsilon\), and composing two sweeps for the separated order gives the displayed coefficients; these exact symbolic identities are reproduced in `verify.py`. For forward-only PolyCD, the middle proposed step has negative coefficient for small positive \(\varepsilon\) and is clipped to zero; composing the other two updates yields the stated nonzero first-order term. This establishes both quadratic effects as genuine and the away-step distinction.

## Verification

Execute `python verify.py` with Python 3.10 or later and SymPy 1.12 or later; dependencies are listed in `requirements.txt`. It reproduces the two concrete Taylor expansions with exact rational symbolic differentiation, the two-sweep second-order coefficient, actual feasible away-step bounds, and the forward-only clipped-step comparison. It also checks the trace, determinant, projector and square identities on 100 reproducibly generated rational triangle/positive-metric configurations in all six orders. The program prints `PASS 1840 exact symbolic/rational checks`. These finite tests support the computations and are not a substitute for Steps 1--4, which prove the arbitrary-triangle assertions.

## Relationship to prior work

Mazumder and Wang [1] introduce the precise PolyCDwA algorithm and prove global linear convergence for strongly convex objectives (their Theorem 3.2). The local Jacobian, exact geometry of nilpotency, order-dependent one- versus two-sweep quadratic estimates, and the interior metric-circle locus are not provided by that global contraction theorem. Klopfenstein et al. [2] study local linear rates and identification for separable composite coordinate descent with prox-linear updates, rather than the vertex-directed away-step algorithm. Beck, Pauwels and Sabach [3] treat cyclic block conditional gradients with a different block-update structure. The orthogonal-projector algebra used above is elementary classical linear algebra; the specific finding is its exact realization and geometric classification for the nonlinear feasible PolyCDwA sweep, not a claim of inventing projection products.

## Limitations

The classification is local and restricted to nondegenerate triangles, exact line searches, a constant positive-definite quadratic Hessian, strictly interior minimizers, and a fixed order repeated at every sweep. It does not supply a global quadratic rate or a statement for higher-dimensional polytopes, inexact line searches, or general smooth objectives. The exceptional metric-circle set has no interior in the two-dimensional target domain, so the quadratic cases are nongeneric; the generally observed local behavior is linear. The comparison with existing mathematical literature is limited to the inspected sources and may not exhaust specialized local convergence or projection-product studies.

## References

[1] R. Mazumder and H. Wang, *A Cyclic Coordinate Descent Method for Convex Optimization on Polytopes*, arXiv:2303.07642 (first version publicly posted 2023-03-14), especially Algorithm 2, exact line search (3.4), and Theorem 3.2. https://arxiv.org/abs/2303.07642 ; https://arxiv.org/html/2303.07642v2

[2] Q. Klopfenstein, Q. Bertrand, A. Gramfort, J. Salmon and S. Vaiter, *Model identification and local linear convergence of coordinate descent*, arXiv:2010.11825. https://arxiv.org/abs/2010.11825

[3] A. Beck, E. Pauwels and S. Sabach, *The Cyclic Block Conditional Gradient Method for Convex Optimization Problems*, arXiv:1502.03716. https://arxiv.org/abs/1502.03716

[4] F. Pedregosa, G. Negiar, A. Askari and M. Jaggi, *Linearly Convergent Frank-Wolfe with Backtracking Line-Search*, arXiv:1806.05123. https://arxiv.org/abs/1806.05123
