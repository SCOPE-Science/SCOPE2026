# Three exact magnitude phases for two points on the three-objective simplex

## Finding

For every scale \(L>0\), define the Pareto simplex \(\Delta_L=\{x\in[0,\infty)^3:x_1+x_2+x_3=L\}\). Given two **distinct** points \(x,y\in\Delta_L\), let \(D(\{x,y\})=[0,x]\cup[0,y]\), where \([0,x]\) is the closed coordinate box from the origin to \(x\). Magnitude uses the ambient \(\ell_1\) metric with its ordinary (unrescaled) distance normalization.

The maximum of \(\operatorname{Mag}(D(\{x,y\}))\) is attained at precisely one unordered pair modulo common permutations of the three objective coordinates. There are three regimes:

| Scale | Unique maximizing pair, up to symmetry | Optimal magnitude |
| --- | --- | --- |
| \(0<L\le2\) | \(\{(L,0,0),(0,L/2,L/2)\}\) | \((L^2+16L+16)/16\) |
| \(2<L\le16/5\) | \(\{((L+4)/3,(L-2)/3,(L-2)/3),(0,L/2,L/2)\}\) | \((L+4)^2(2L+35)/432\) |
| \(L>16/5\) | \(\{((11L+20)/23,(6L-10)/23,(6L-10)/23),((5L-16)/23,(9L+8)/23,(9L+8)/23)\}\) | \(27(L+6)^3/4232\) |

The pieces agree exactly at their junctions; each junction has a unique maximizing pair modulo symmetry. At the two transitions the pair's combinatorial location changes from vertex plus opposite-edge midpoint to edge midpoint plus simplex interior, then to two interior points.

## Assumptions and scope

The problem is the unconstrained maximization over unordered sets of exactly two **distinct** points of \(\Delta_L\) for a fixed finite real \(L>0\), with three maximization objectives and the origin as common anchor. Repeated points may be admitted during the compactness argument without affecting the maximizer. Magnitude is the metric-geometric magnitude of the downward-closed box union in unscaled \(\ell_1^3\), not hypervolume alone and not the magnitude of the discrete two-point metric subspace. No discrete lattice constraint is imposed on the two Pareto points.

## Proof

**1. Exact objective and ordered coordinates.** For one box, the standard product formula is \(\operatorname{Mag}([0,a])=\prod_{i=1}^3(1+a_i/2)\). Magnitude is a valuation on unions of anchored boxes; see Emmerich [1], Theorem 3.3 and Section 12. Thus, for any two points,
\[
8\operatorname{Mag}(D(\{x,y\}))=\prod_{i=1}^3(2+x_i)+\prod_{i=1}^3(2+y_i)-\prod_{i=1}^3(2+\min\{x_i,y_i\}). \tag{1}
\]
Because both points have the same coordinate sum, coordinate relabeling and exchanging the points reduce all pairs, including ties, to
\[
x=(B+u+v,C,E),\qquad y=(B,C+u,E+v),\tag{2}
\]
where \(B,C,E,u,v\ge0\) and \(B+C+E+u+v=L\). Here \(x_1\ge y_1\), \(x_2\le y_2\), \(x_3\le y_3\); the first-coordinate difference equals the sum of the other two coordinate differences by conservation of the total.

Writing \(q=B+2\), (1) and (2) give the **exact** identity
\[
8\operatorname{Mag}=(q+u+v)(C+2)(E+2)+q\bigl[u(E+2)+v(C+2)+uv\bigr].\tag{3}
\]

**2. Global symmetrization, not a stationarity ansatz.** Put \(W=u+v\), \(s=C+E=L-B-W\), \(C=s/2+c\), \(E=s/2-c\), \(u=W/2+w\), \(v=W/2-w\). Feasibility is \(B\ge0\), \(W\ge0\), \(B+W\le L\), \(|c|\le s/2\), \(|w|\le W/2\). Let \(r=2+s/2\). A direct expansion of (3) gives
\[
8\operatorname{Mag}=J(B,W)-\bigl[(B+2+W)c^2+2(B+2)cw+(B+2)w^2\bigr],\tag{4}
\]
where
\[
J(B,W)=(B+2+W)r^2+(B+2)Wr+\frac{B+2}{4}W^2,\qquad r=2+\frac{L-B-W}{2}.\tag{5}
\]
If \(W>0\), the subtracted quadratic has a positive-definite matrix: its leading minor is \(B+2+W>0\) and its determinant is \((B+2)W>0\). Therefore, **for fixed** \(B,W\), equality with \(J\) occurs only at \(c=w=0\), i.e. \(C=E=s/2\) and \(u=v=W/2\). If \(W=0\) then \(w=0\), and (4) is uniquely maximized at \(c=0\). This establishes global symmetrization on the entire feasible region, not only local optimality.

**3. Maximize over the separation.** For fixed \(B\in[0,L]\), differentiate (5) exactly:
\[
\frac{\partial J}{\partial W}=\frac{(B-L+W-4)(B-L+3W-4)}4.\tag{6}
\]
The first factor is strictly negative for all \(0\le W\le L-B\). Thus \(J\) strictly increases then strictly decreases, with unique maximizing
\[
W_*(B)=\min\left\{L-B,\frac{L-B+4}{3}\right\}.\tag{7}
\]
This is positive whenever \(B<L\), while \(B=L\) gives a singleton with strictly smaller objective than for any nearby smaller \(B\). If \(L-B\le2\), equation (7) gives the edge branch \(W=L-B\); otherwise it gives the interior branch \(W=(L-B+4)/3\).

**4. Maximize over the remaining common coordinate.** On the edge branch (the interval \(B\in[\max\{0,L-2\},L]\)), the derivative is
\[
\frac{d}{dB}J(B,L-B)=\frac{3B^2-(4L+12)B+L^2+4L-16}{4}.\tag{8}
\]
This derivative is negative throughout the edge interval: its numerator is convex in \(B\), hence no greater than the larger endpoint value, which is strictly negative. More explicitly, when \(L\le2\), the endpoint values at \(B=0,L\) are \(L^2+4L-16<0\) and \(-8L-16<0\); when \(L>2\), the endpoint values at \(B=L-2,L\) are \(20-12L<0\) and \(-8L-16<0\). Hence the edge optimum occurs at the smallest feasible \(B\).

For \(L>2\), on the interior branch \(0\le B\le L-2\), substituting (7) gives
\[
J\!\left(B,\frac{L-B+4}{3}\right)=\frac{(B-L-4)^2(23B+4L+70)}{108},\qquad
\frac{dJ}{dB}=\frac{(B-L-4)(23B-5L+16)}{36}.\tag{9}
\]
The factor \(B-L-4\) is strictly negative. For \(2<L\le16/5\), \(5L-16\le0\), so this branch strictly decreases and is optimized at \(B=0\). For \(L>16/5\), it increases until its unique maximizer \(B=(5L-16)/23\) and decreases afterward; this point satisfies \(0<B<L-2\). Both branches match at \(B=L-2\) and the edge branch is strictly decreasing, so these are also the unique **global** optimal \(B\)-values. For \(0<L\le2\) there is only the edge branch, with unique best \(B=0\).

**5. Reconstruct both points and their optimal values.** Use \(C=E=(L-B-W)/2\), \(u=v=W/2\) in (2). The optimal pairs listed in the Finding follow on substituting, successively, \((B,W)=(0,L)\), \((0,(L+4)/3)\), and \(((5L-16)/23,6(L+6)/23)\). Substitution into (5), divided by eight, gives respectively
\[
\frac{L^2+16L+16}{16},\qquad \frac{(L+4)^2(2L+35)}{432},\qquad \frac{27(L+6)^3}{4232}.\tag{10}
\]
Strictness at every reduction establishes uniqueness up to the stated symmetries. At \(L=2\) and \(L=16/5\) the neighboring coordinate formulas coincide, so the boundaries create no extra or missing optimizers. This proves the global statement for all real \(L>0\).

## Verification

A standalone dependency-free verifier is supplied in `artifacts/verify_two_point_simplex.py`. It recomputes the box-union valuation with exact rational arithmetic, checks all three closed-form phase formulas at exact rational inputs on both sides of each transition, and compares randomly sampled feasible pairs against the asserted maxima. It also checks representative derivative identities by symmetric polynomial expansion. Execute `python artifacts/verify_two_point_simplex.py` from the package root. The displayed algebraic reductions (1)–(10), not the finite tests, certify the quantified infinite theorem.

## Relationship to prior work

Emmerich [1] introduced dominated-set magnitude for multiobjective optimization and supplies both its anchored-box inclusion–exclusion formula and numerical three-objective simplex studies involving nine and ten points. Equations (1)–(3) deliberately use that known formula; they are **not** claimed as novel. The additional result here is the complete global two-point optimizer for **every** scale, including two exact phase transitions and uniqueness.

Because the magnitude valuation of finite anchored boxes can also be written as hypervolume after a uniform \((-2,-2,-2)\) reference translation and division by eight, the statement is equivalently a sharp **two-point, three-objective, triangular-front reference-point classification**. Shang, Ishibuchi, Chen, Nan, and Liao [2] analyze the same triangular plane for classical hypervolume but describe numerical population optimizers and local properties of regular grids, not this global two-point classification; notably their Section IV.A investigates population sizes at least three. Ishibuchi and collaborators [3] had earlier examined triangular and inverted triangular fronts and reference-point dependence numerically; the accessible abstract does not establish an exact two-point phase diagram. These objects are close enough that rediscovery in earlier or unindexed reference-point literature remains a genuine originality risk.

## Limitations

The theorem covers exactly two unconstrained nondominated points and the unscaled \(\ell_1\) magnitude of their origin-anchored box union in three objectives, at arbitrary positive total objective scale. It does not classify larger population sizes, other Pareto geometries, unequal coordinate weights, arbitrary anchors not reducible by a common translation, or the convergence of any set-gradient algorithm. The equivalent shifted-hypervolume formulation means differences from hypervolume at the **same anchor** must not be confused with non-equivalence at a changed reference. Primary literature searches cannot establish the absence of unindexed equivalent results. Independent audit has not been performed.

## References

[1] M. T. M. Emmerich, *The Magnitude of Dominated Sets: A Pareto Compliant Indicator Grounded in Metric Geometry*, arXiv:2604.18147v1 (first public 2026-04-20), especially Theorem 3.3 and Section 12. https://arxiv.org/abs/2604.18147

[2] K. Shang, H. Ishibuchi, W. Chen, Y. Nan, and W. Liao, *Hypervolume-Optimal \(\mu\)-Distributions on Line/Plane-based Pareto Fronts in Three Dimensions*, arXiv:2104.09736v1 (2021), especially Section IV.A. https://arxiv.org/abs/2104.09736

[3] H. Ishibuchi, R. Imada, Y. Setoguchi, and Y. Nojima, *Hypervolume Subset Selection for Triangular and Inverted Triangular Pareto Fronts of Three-Objective Problems*, FOGA (2017), DOI:10.1145/3040718.3040730.
