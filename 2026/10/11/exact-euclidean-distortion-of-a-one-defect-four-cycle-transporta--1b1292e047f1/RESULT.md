# Exact Euclidean distortion of a one-defect four-cycle transportation space

## Finding
Let \(0<t\leq3\), and let \(C_4(t)\) be the four-vertex metric induced by a cyclic weighted graph whose consecutive edge lengths are \(1,1,1,t\). Let \(\mathcal F(C_4(t))\) be its **real** Lipschitz-free (transportation-cost) Banach space. Its dimension is three. The exact squared Banach–Mazur distance to Euclidean three-space is
\[
 d_{\mathrm{BM}}\!\left(\mathcal F(C_4(t)),\ell_2^3\right)^2
 = \begin{cases}
 \displaystyle \frac{3(7+t^2)}{9-t^2},&0<t\leq1,\\[3pt]
 \displaystyle \frac{3(5t^2+3)}{t^2(9-t^2)},&1\leq t\leq3/\sqrt5,\\[3pt]
 \displaystyle \frac{25}{9},&3/\sqrt5\leq t\leq2,\\[3pt]
 \displaystyle \frac{(t+3)(7-t)}{(t+1)(5-t)},&2\leq t\leq3.
 \end{cases}
\]
The expressions agree at shared endpoints. In particular, this geometric invariant has an **exact flat interval**, \(d_{\mathrm{BM}}=5/3\) for every \(3/\sqrt5\leq t\leq2\), although the four-cycle metric changes with \(t\). At the equal-edge cycle and the path-metric endpoint one has \(d_{\mathrm{BM}}=\sqrt3\); as \(t\downarrow0\), the distance tends to \(\sqrt{7/3}\).

## Assumptions and scope
For finite-dimensional real Banach spaces \(X,Y\) of equal dimension, the multiplicative Banach–Mazur distance is
\[
 d_{\mathrm{BM}}(X,Y)=\inf_{T:X\to Y\,\mathrm{invertible}}\|T\|\,\|T^{-1}\|.
\]
Fix four labelled vertices, their indicated cyclic edge weights, and the resulting shortest-path distance (even when the last edge is redundant at \(t=3\)). All assertions refer to the **real** Lipschitz-free norm; no complex-scalar or higher-cycle version is claimed. At \(t=3\), the weighted edge of length three is redundant but the metric remains well-defined. Every claimed equality is over all invertible linear maps, not only coordinate-diagonal maps.

## Proof
**1. An exact dual hyperplane.** Let \(f\) be a real-valued Lipschitz function on the four metric vertices. Orient the cycle consecutively and form the three normalized edge increments \(x_1,x_2,x_3\), and the fourth normalized increment \(y\). Telescoping gives \(x_1+x_2+x_3+t y=0\). Conversely, every real tuple obeying this identity integrates along the cycle to a vertex function, unique modulo constants. The shortest-path graph norm is exactly the largest absolute normalized edge increment: the upper bound on every edge implies the bound on every shortest path, and every edge inequality is included. Thus
\[
 \operatorname{Lip}_0(C_4(t))\cong
 \left\{(x_1,x_2,x_3,y)\in\ell_\infty^4:\ x_1+x_2+x_3+t y=0\right\}.
\]
Eliminating \(y\) gives a norm \(N_t\) on \(\mathbb R^3\), with \(s=x_1+x_2+x_3\):
\[
 N_t(x)=\max\left\{|x_1|,|x_2|,|x_3|,\frac{|s|}{t}\right\},\qquad
 K_t=\{x: |x_i|\leq1,\ |s|\leq t\}.
\]
The Lipschitz-free space is the Banach dual of this three-dimensional Lipschitz space. Because \(d_{\mathrm{BM}}(X,Y)=d_{\mathrm{BM}}(X^*,Y^*)\) in finite dimensions and Euclidean space is self-dual, it suffices to compute the distance from \((\mathbb R^3,N_t)\) to \(\ell_2^3\).

**2. No symmetry-breaking Hilbert norm improves the answer.** For a positive definite quadratic form \(Q\), write
\[
 L(Q)=\min_{N_t(x)=1}Q(x),\qquad M(Q)=\max_{N_t(x)=1}Q(x).
\]
Its squared distortion is \(M(Q)/L(Q)\). Normalize \(Q\) so that \(N_t(x)^2\leq Q(x)\leq D^2 N_t(x)^2\) for every \(x\). Both inequalities survive averaging \(Q\) over the group of all six coordinate permutations because \(N_t\) is permutation invariant. Hence some globally optimal form is permutation invariant. Every such positive form, up to a positive factor, has the shape
\[
 Q_\alpha(x)=x_1^2+x_2^2+x_3^2+\alpha(x_1+x_2+x_3)^2,
 \qquad \alpha>-\tfrac13.
\]
Consequently the globally optimal squared distortion is exactly
\[
 \inf_{\alpha>-1/3}\frac{M_t(\alpha)}{L_t(\alpha)},
 \quad M_t(\alpha)=\max_{N_t(x)=1}Q_\alpha(x),\quad L_t(\alpha)=\min_{N_t(x)=1}Q_\alpha(x).
\]

**3. Compute the outer maximum exactly.** The positive definite quadratic \(Q_\alpha\) is convex, so its maximum over the polytope \(K_t\) occurs at a vertex; by homogeneity this equals its maximum over the norm sphere. For \(0<t\leq1\), vertices of the clipped cube have two coordinates \(\pm1\) of opposite signs and the remaining coordinate \(\pm t\), with sum \(\pm t\). Thus
\[
 M_t(\alpha)=2+(1+\alpha)t^2\qquad(0<t\leq1).
\]
For \(1\leq t\leq3\), the vertices are cube corners of sum \(\pm1\), and (when distinct) intersections with the two bounding slab planes, represented by permutations/sign reversals of \((1,1,t-2)\). Hence
\[
 M_t(\alpha)=\max\left\{3+\alpha,\ 2+(t-2)^2+\alpha t^2\right\}\qquad(1\leq t\leq3).
\]
This vertex description includes the coalescing endpoint cases \(t=1\) and \(t=3\).

**4. Compute the inner minimum exactly.** Each norm-unit vector belongs to a facet of \(K_t\). On either facet \(|s|=t\), the Cauchy inequality \(\sum x_i^2\geq s^2/3\) gives the attained minimum
\[
 L_1=t^2\left(\alpha+\frac13\right),
\]
attained at \(x_i=\pm t/3\), which is feasible as \(t\leq3\). On a cube facet, say \(x_1=1\), averaging the other two coordinates decreases \(Q_\alpha\) at fixed sum. Without the facet-box restriction, the remaining one-variable expression is \(1+(s-1)^2/2+\alpha s^2\); its minimum is
\[
 L_2=\frac{1+3\alpha}{1+2\alpha},\qquad
 s_0=\frac{1}{1+2\alpha}.
\]
The unrestricted computation always supplies a lower bound on cube-facet values. Put
\[
 \alpha_1(t)=\frac{3-t^2}{2t^2}.
\]
When \(\alpha\leq\alpha_1(t)\), one has \(L_1\leq L_2\), so the feasible slab-facet minimizer gives \(L_t=L_1\) without requiring cube-facet feasibility. When \(\alpha\geq\alpha_1(t)\), one has \(L_2\leq L_1\), and the cube-facet minimizer is feasible: \(0<s_0\leq t^2/3\leq t\), with \(x_2=x_3=(s_0-1)/2\in[-1,1]\). Hence, for every admissible \(\alpha\),
\[
 L_t(\alpha)=\min\left\{t^2\left(\alpha+\frac13\right),\ \frac{1+3\alpha}{1+2\alpha}\right\}.
\]
Both sides are positive because \(\alpha>-1/3\).

**5. Optimize the only remaining scalar.** When \(0<t\leq1\), \(\alpha_1(t)\geq1\). The quotient \(M_t/L_1\) strictly decreases with \(\alpha\), whereas \(M_t/L_2\) strictly increases for \(\alpha\geq\alpha_1(t)\). For the latter claim its derivative has the sign of \(3\alpha^2t^2+2\alpha t^2-1\), which is already positive at \(\alpha_1(t)\). Thus the unique minimizing parameter is \(\alpha_* =\alpha_1(t)\) for \(0<t\leq1\).

For \(1<t\leq3\) define the vertex-switch parameter \(\alpha_\times(t)=(3-t)/(1+t)\). Direct subtraction yields \(\alpha_1(t)<\alpha_\times(t)\), with equality only at \(t=1\). On \(\alpha\leq\alpha_1\), the ratio \((3+\alpha)/L_1\) strictly decreases. On \(\alpha_1\leq\alpha\leq\alpha_\times\), the ratio \((3+\alpha)/L_2\) decreases until \(\alpha=1/3\) and increases afterward, because its derivative is
\[
 \frac{2(\alpha+1)(3\alpha-1)}{(3\alpha+1)^2}.
\]
On \(\alpha\geq\alpha_\times\), the ratio \(\bigl[2+(t-2)^2+\alpha t^2\bigr]/L_2\) strictly increases; its derivative is
\[
 \frac{2(\alpha t+1)(3\alpha t+2t-3)}{(3\alpha+1)^2}>0
\]
throughout that region and \(1<t\leq3\). (Indeed the second linear factor is positive already at \(\alpha_\times\).) Consequently the minimizing parameter for \(1<t\leq3\) is the median of \(\alpha_1(t)\), \(1/3\), and \(\alpha_\times(t)\). Explicitly,
\[
 \alpha_*(t)=\begin{cases}
 (3-t^2)/(2t^2),&0<t\leq3/\sqrt5,\\
 1/3,&3/\sqrt5\leq t\leq2,\\
 (3-t)/(1+t),&2\leq t\leq3.
 \end{cases}
\]
Substitution into the exact formulas for \(M_t\) and \(L_t\) yields the four displayed expressions. This proves the theorem for every real \(t\) in the entire stated interval, not just for rational values.

## Verification
The analytic derivation is self-contained: only finite-dimensional duality, group averaging, vertex classification of a clipped cube, Cauchy–Schwarz, and one-variable differentiation are used. The standalone standard-library program `verify_weighted_cycle.py` independently enumerates cube/slab vertices, minimizes the quadratic on each type of facet by a separate constrained formula, and checks 189 exact-rational parameter/ellipsoid cases across every branch. Its expected terminal line is `WEIGHTED_CYCLE_RATIONAL_CHECK_OK 189`. This finite test is a reproducibility aid, not a proof of the continuum assertion.

## Relationship to prior work
Godard's treatment of tree metrics identifies the free space of a weighted tree with a finite-dimensional \(\ell_1\) space; this agrees with the endpoint \(t=3\) but gives no deformed four-cycle profile. Alexander, Fradelizi, García-Lirola, and Zvavitch study convex polytopes of finite Lipschitz-free spaces, including the fact that an equal-edge four-cycle has a cube free-space ball and that unequal edge weights destroy its zonotope structure (Proposition 3.9). Their results concern isometries, decompositions and volume products, not the best Euclidean ellipsoid throughout this parameter family. Ostrovska and Ostrovskii represent transportation-cost spaces of finite graphs as quotients of weighted edge \(\ell_1\) by cycle spaces, without the sharp Euclidean approximation investigated here. Published numerical-index work on unweighted real cycle free spaces determines an operator numerical-radius invariant rather than this Banach–Mazur distortion, and does not imply the claimed constant plateau.

## Limitations
No claim is made for arbitrary four-point metrics, more than one independent edge weight, complex spaces, or cycles of arbitrary size. The optimizer is an optimal symmetric Euclidean position; uniqueness among all possibly non-symmetric positions has not been established. The rational test suite is finite and cannot certify the continuous parameter range independently of the proof. Full originality against unindexed or differently named hyperplane-section/ellipsoid literature remains a bibliographic risk. Independent external validation has not been performed.

## References
1. A. Godard, “Tree metrics and their Lipschitz-free spaces,” arXiv:0904.3178v1, first submitted 21 April 2009; Proceedings of the American Mathematical Society 138 (2010), 4311–4320.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, “Geometry and volume product of finite dimensional Lipschitz-free spaces,” arXiv:1911.10642v1 (2019), Journal of Functional Analysis 280 (2021), 108849.
3. S. Ostrovska, M. I. Ostrovskii, “Isometric structure of transportation cost spaces on finite metric spaces,” arXiv:2112.02689v1 (2021).
4. M. Cúth, M. Doucha, T. Titkos, “Isometries of Lipschitz-free Banach spaces,” Journal of the London Mathematical Society 110 (2024), e70000; DOI 10.1112/jlms.70000.
