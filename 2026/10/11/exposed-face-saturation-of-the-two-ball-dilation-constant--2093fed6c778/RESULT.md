# Exposed-face saturation of the two-ball dilation constant

## Finding

Let \(K\subset\mathbb R^d\), \(d\ge2\), be a full-dimensional, compact, origin-symmetric convex body with Minkowski norm \(\|\cdot\|_K\). Define the two-ball dilation constant, following Dall'Ara and Dumitrescu, by
\[
\rho_2(K)=\max\left\{\min\{\|x-y_1\|_K,\|x-y_2\|_K\}:x\in K,\ y_1,y_2\in2K,\ \|y_1-y_2\|_K\ge2\right\}.
\]
For \(x\in\partial K\), let its *exposed-face star* be
\[
\mathcal E_K(x)=\bigcup_{\substack{\|\varphi\|_{K^*}=1\\\varphi(x)=1}}\{z\in K:\varphi(z)=1\}.
\]
Then the universal upper bound \(\rho_2(K)\le3\) is attained **if and only if**
\[
\max_{x\in\partial K}\operatorname{diam}_K\mathcal E_K(x)\ge1.
\]
In particular, this yields sharp phase boundaries for two canonical planar families:

1. For the Euclidean disk clipped by two parallel lines,
\[
K_a=\{(s,t)\in\mathbb R^2:s^2+t^2\le1,\ |s|\le a\},\qquad0<a\le1,
\]
one has \(\rho_2(K_a)=3\) exactly for \(0<a\le\sqrt3/2\), and \(\rho_2(K_a)<3\) exactly for \(\sqrt3/2<a\le1\).

2. For a regular centrally symmetric \(N\)-gon \(P_N\), \(N\ge4\) even, the equality \(\rho_2(P_N)=3\) holds exactly for \(N\in\{4,6,8,10,12\}\). Every even \(N\ge14\) has \(\rho_2(P_N)<3\).

The clipped-disk transition is strictly stronger than applying the modulus-of-convexity estimate in the originating paper: throughout
\[
\sqrt3/2<a\le\sqrt{15}/4
\]
we have simultaneously \(\rho_2(K_a)<3\) and \(\delta_{K_a}(1/2)=0\), where \(\delta\) is the standard modulus of convexity. Thus the modulus-based bound supplies only \(\rho_2(K_a)\le3\) throughout this nonempty parameter interval.

## Assumptions and scope

The bodies are compact, convex, centrally symmetric about the norm origin, and full-dimensional; the initial criterion is valid in every finite dimension \(d\ge2\). The two centers \(y_1,y_2\) range through \(2K\), with separation at least \(2\) in the \(K\)-norm. Boundaries and supporting faces are included. In the clipped-disk family \(0<a\le1\); in the regular-polygon family \(N\ge4\) is even and \(P_N\) is centered at the origin (its Euclidean scale is immaterial).

The statement classifies saturation versus strictness of the new two-ball factor. It does **not** give the exact numerical value of \(\rho_2(K)\) when this value is below \(3\), nor does it assert that the resulting numerical covering bound improves every existing planar covering estimate.

## Proof

**1. Compactness and exact equality criterion.** The admissible triples form a nonempty compact set, so the maximum exists. The triangle inequality gives \(\|x-y_i\|_K\le\|x\|_K+\|y_i\|_K\le3\). If \(\rho_2(K)=3\), take an attaining triple. Both distances equal \(3\), and necessarily \(\|x\|_K=1\) and \(\|y_i\|_K=2\). For each \(i=1,2\), choose a dual-unit supporting linear functional \(\varphi_i\) of \(x-y_i\). Since
\[
3=\varphi_i(x-y_i)\le\|x\|_K+\|y_i\|_K=3,
\]
equality forces \(\varphi_i(x)=\varphi_i(-y_i/2)=1\). Consequently \(z_i=-y_i/2\in\mathcal E_K(x)\) and
\[
\|z_1-z_2\|_K=\tfrac12\|y_1-y_2\|_K\ge1.
\]
Conversely, suppose \(z_1,z_2\in\mathcal E_K(x)\) and \(\|z_1-z_2\|_K\ge1\). Choose supporting functionals \(\varphi_i\) with \(\varphi_i(x)=\varphi_i(z_i)=1\). Setting \(y_i=-2z_i\) gives admissible separation and
\[
\|x-y_i\|_K=\|x+2z_i\|_K\ge\varphi_i(x+2z_i)=3.
\]
The universal upper bound forces equality. The union defining \(\mathcal E_K(x)\) is compact, because it is the projection of a closed subset of the compact product of the dual-unit sphere with \(K\). The maximum over boundary points exists by the same compactness argument applied to triples \((x,\varphi,z)\). This proves the equivalence, including endpoint cases.

**2. Clipped disks.** Put \(b=\sqrt{1-a^2}\) for \(0<a<1\). The only nontrivial exposed faces of \(K_a\) are the vertical boundary segments
\[
F_\pm=\{(\pm a,t): -b\le t\le b\}.
\]
At an arc point every exposed face through the point is a singleton. At an endpoint of a vertical segment, all exposed faces containing it lie within that segment, while the vertical support functional exposes the whole segment. Thus every exposed-face star is either a singleton or one of \(F_+,F_-\). Because the vertical diameter of \(K_a\) is \(2\), the \(K_a\)-gauge of a vertical vector \((0,t)\) is exactly \(|t|\). Hence
\[
\max_{x\in\partial K_a}\operatorname{diam}_{K_a}\mathcal E_{K_a}(x)=2b=2\sqrt{1-a^2}.
\]
At \(a=1\), the disk is strictly convex and the maximum is \(0\). The criterion now yields \(\rho_2(K_a)=3\) if and only if \(2\sqrt{1-a^2}\ge1\), equivalently \(a\le\sqrt3/2\). For the upper phase, compactness upgrades nonattainment of \(3\) to the strict inequality \(\rho_2(K_a)<3\); no unproved quantitative gap is asserted.

For the modulus statement, \(\delta_{K_a}(1/2)=0\) means there exist \(u,v\in K_a\) with \(\|u-v\|_{K_a}\ge1/2\) and \(\|(u+v)/2\|_{K_a}=1\). A norm-one supporting functional of the midpoint must have value \(1\) on both endpoints, so \(u,v\) lie on a common exposed face. Conversely any two points of such a face realize a unit-norm midpoint. The largest face diameter is \(2b\); therefore \(\delta_{K_a}(1/2)=0\) exactly when \(2b\ge1/2\), equivalently \(a\le\sqrt{15}/4\). The two phase thresholds are distinct. An explicit witness in the intermediate regime is \(a=15/16\), whose exposed side has norm diameter \(\sqrt{31}/8\), lying strictly between \(1/2\) and \(1\).

**3. Regular even polygons.** Take \(P_N\) with circumradius \(1\) and vertices \(v_j=(\cos(2\pi j/N),\sin(2\pi j/N))\). For a point in an edge interior, the exposed-face star is that edge. At a vertex \(v_j\) it is the union of the two incident edges; convexity of the norm ensures that its diameter is attained among \(v_{j-1},v_j,v_{j+1}\). By rotational symmetry it suffices to take \(j=0\). The two-step chord is vertical and has norm
\[
D_N=\|v_{-1}-v_1\|_{P_N}=
\begin{cases}
2\sin(2\pi/N),&N\equiv0\pmod4,\\
4\sin(\pi/N),&N\equiv2\pmod4.
\end{cases}
\]
Indeed its Euclidean length is \(2\sin(2\pi/N)\), and the radial intercept of \(P_N\) in the vertical direction is \(1\) for \(4\mid N\), and \(\cos(\pi/N)\) otherwise. The norm of an edge is at most \(2\tan(\pi/N)\), because the Euclidean edge length is \(2\sin(\pi/N)\) and the radial function is everywhere at least the apothem \(\cos(\pi/N)\). For \(N\ge4\),
\[
2\tan(\pi/N)\le2\sin(2\pi/N)\le D_N,
\]
where the first inequality follows from \(\cos^2(\pi/N)\ge1/2\). Thus the maximal exposed-face-star diameter is exactly \(D_N\). The displayed formulas show \(D_N\ge1\) for even \(4\le N\le12\), with \(D_{12}=1\), while \(D_N<1\) for all even \(N\ge14\): for \(4\mid N\) this follows from \(2\sin(2\pi/N)<1\) when \(N\ge16\); for \(N\equiv2\pmod4\), it follows from \(4\sin(\pi/N)<1\) when \(N\ge14\) (already true at \(N=14\), then decreasing). The general criterion completes the classification.

## Verification

The inequalities in the proof are analytic and dimension-uniform; no numerical experiment is used to infer them. The standalone script `verify.py` checks the two algebraic clipping thresholds, the exact rational intermediate example, the radial formulas at sample even polygon sizes, and explicit equality witnesses at the saturation endpoints. It also verifies both sides of the critical strict comparisons by high-precision evaluation. All these checks passed. The finite sample is not substituted for the monotonicity and compactness arguments establishing the infinite statements.

## Relationship to prior work

Dall'Ara and Dumitrescu introduced the displayed two-ball factor and derived its exact Euclidean value, a universal upper bound of \(3\), and the sufficient bound \(\rho_2(K)\le3-2\delta_K(1/2)\) (arXiv:2609.25288v1, §§2.5–3.2). Their modulus bound is vacuous on the explicit intermediate clipped-disk interval, whereas the present exposed-face criterion proves strictness there. Their paper does not state an exposed-face saturation criterion or the clipped-disk and regular-polygon transitions.

A separately published calculation entitled “Exact two-disk covering radius of every regular even polygon” concerns the minimum Euclidean radius of two disks covering one polygon, with unrestricted disk centers. That continuous Euclidean two-center problem is a different invariant from the three-translate Minkowski-norm dilation problem above, despite a shared notation. Standard Banach-space accounts of exposed faces and norm equality supply background geometric tools but do not determine these two-ball thresholds. Direct searches of related published records did not identify equivalent conclusions; the search cannot establish absolute novelty.

## Limitations

Only the saturation/non-saturation boundary is classified: there is no closed formula for \(\rho_2\) below \(3\) and no uniform quantitative gap for the entire clipped-disk family. The general criterion is finite-dimensional and symmetric. The geometric test is elementary once equality in the triangle inequality is expressed through common supporting faces; possible unindexed formulations of this equality test in geometric functional analysis remain a residual originality risk. The polygon corollary assumes even regularity. A strict improvement in the two-ball factor need not by itself improve the best existing *planar* numerical bound in the Radó selection problem.

## References

G. M. Dall'Ara and A. Dumitrescu, “Exponential improvements in Rado's covering problem,” arXiv:2609.25288v1, first posted 2026-09-21, especially Definitions 2.1 and Proposition 3.2; https://arxiv.org/html/2609.25288v1.

“Exact two-disk covering radius of every regular even polygon,” published-finding corpus published record 2026/10/4/SCOPE-exact-two-disk-covering-radius-of-every-regular-even-polygon--5ecef0f3d939, `RESULT.md` (different Euclidean two-center invariant).

“Geometric Invariants of Surjective Isometries between Unit Spheres,” Mathematics 9 (2021), article 2346, DOI 10.3390/math9182346 (general normed-space exposed-face background).
