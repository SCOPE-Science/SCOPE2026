# Exact numerical index along the short-edge four-cycle deformation

## Finding
For \(0<t\le 1\), let \(M_t\) be the four vertices of a cycle with successive edge lengths \(1,1,1,t\), equipped with the shortest-path metric. The **real** Lipschitz-free space \(X_t=\mathcal F(M_t)\) has exact numerical index
\[
\boxed{n(X_t)=\frac{1}{2-t}.}
\]
The value is attained by an explicit rank-one operator. Thus the complete short-edge deformation interpolates continuously from the equilateral-triangle limit \(n=1/2\), as \(t\downarrow0\), to the unit square \(n=1\) at \(t=1\). The limiting triangle is not included in the claimed four-point domain.

## Assumptions and scope
All scalar fields in the theorem are \(\mathbb R\). There are exactly four distinct vertices. The three long edges have length \(1\); the remaining edge has length \(t\in(0,1]\); the distance is the infimum of weighted path lengths. In particular, each edge is strictly shorter than the alternative path between its endpoints. The base vertex can be chosen arbitrarily.

The numerical radius of a bounded operator \(T:X_t\to X_t\) is
\[
v(T)=\sup\{|f(Tx)|:x\in S_{X_t},\ f\in S_{X_t^*},\ f(x)=1\},
\]
and \(n(X_t)=\inf_{\|T\|=1}v(T)\). The result determines this index, not the numerical range of every individual operator nor the index for arbitrary four edge lengths.

Orient the four edges cyclically, and denote their normalized edge molecules in \(X_t\) by \(p_1,p_2,p_3,p_4\). There is precisely one linear dependence,
\[
p_1+p_2+p_3+t p_4=0.
\]
Use \((p_1,p_2,p_3)\) as a basis, so that \(p_4=-(p_1+p_2+p_3)/t\). Write a dual functional by its evaluations \(u_i=f(p_i)\) for \(1\le i\le3\). The dual unit ball in these coordinates is
\[
K_t=\{u\in[-1,1]^3:|u_1+u_2+u_3|\le t\},
\]
with \(f(p_4)=-(u_1+u_2+u_3)/t\).

## Proof
**1. Exact polytopal models.** A real function on the four vertices is one-Lipschitz precisely when the absolute increment across each of the four edges does not exceed its length. The increments have the sole cycle relation displayed above, and every compatible increment vector integrates uniquely up to an additive constant. Consequently the stated \(K_t\) is exactly the dual unit ball. The primal ball is the convex hull of the eight signed edge molecules \(\pm p_i\). All eight are its vertices: the direct edge between adjacent endpoints has length strictly less than the sum along the complementary path, so its molecule is extreme; any nonedge molecule decomposes along a geodesic path. The finite-metric extreme-molecule criterion also gives this conclusion.

For \(0<t<1\), the vertices of \(K_t\) are exactly the distinct coordinate permutations of
\[
(1,-1,t)\quad\text{and}\quad(1,-1,-t).
\]
Indeed, at least two of the three coordinate inequalities must be tight at a vertex, since at most one of the two slab boundaries is active when the slab has positive width. If two coordinates have equal signs, their sum has magnitude \(2\), which cannot be offset by the remaining coordinate while keeping the slab width below \(1\). Hence the saturated coordinates have opposite signs and the last coordinate is \(\pm t\). Conversely these candidates have three linearly independent active constraints. At \(t=1\), the vertex list reduces to the six permutations of \((1,-1,1)\) and their negatives (identical up to repetitions). Every dual vertex \(u\) satisfies \(|f(p_4)|=1\); the entries corresponding to \(p_1,p_2,p_3\) are \(\pm1\) or \(\pm t\).

**2. Sharp universal lower bound.** For every linear \(T\), the finite-dimensional extreme-pair formula gives
\[
v(T)=\max\{|u(Tp_i)|:1\le i\le4,\ u\in\operatorname{ext}K_t,\ |u(p_i)|=1\}.
\]
The use of absolute-value normalization is equivalent to choosing the orientation of each extreme molecule. In particular, the displayed formula implies \(|u(Tp_i)|\le v(T)\) whenever \(|u(p_i)|=1\).

Consider a dual vertex whose coordinate at \(p_1\) is not saturated. Up to permutation of coordinates and overall sign, this is \(a=(t,1,-1)\). There is an **exact identity of dual functionals**
\[
(t,1,-1)
=(1,t,-1)-(1-t)\frac{(1,-1,t)+(1,-1,-t)}2.
\]
The three constituent functionals on the right are dual vertices whose evaluations at \(p_1\) are all \(1\). Applying this identity to \(Tp_1\), the triangle inequality yields
\[
|a(Tp_1)|\le(2-t)v(T).
\]
Permuting the three coordinates and reversing their signs proves the identical estimate for every nonnorming dual vertex at each of \(p_1,p_2,p_3\). Saturated dual vertices already obey the stronger bound \(v(T)\). For \(p_4\), *every* dual vertex is saturated. As the norm of a vector is the maximum of its absolute evaluations by dual vertices, we conclude
\[
\|Tp_i\|\le(2-t)v(T)\quad(1\le i\le4).
\]
The primal ball is the convex hull of \(\pm p_i\), so \(\|T\|=\max_i\|Tp_i\|\). Thus \(\|T\|\le(2-t)v(T)\) for all \(T\), proving \(n(X_t)\ge1/(2-t)\). The endpoint \(t=1\) follows directly too, since every dual vertex then saturates every edge molecule.

**3. Matching rank-one operator.** Define \(z\in X_t\) and \(\varphi\in X_t^*\) by
\[
z=\frac{1-t}{1+t}p_1+\frac2{1+t}p_2,
\qquad
(\varphi(p_1),\varphi(p_2),\varphi(p_3))
=\left(1,-\frac12,-\frac12\right).
\]
The edge relation gives \(\varphi(p_4)=0\). Since the primal unit ball is the convex hull of the signed edge molecules, \(\|\varphi\|=\max_i|\varphi(p_i)|=1\).

For every dual vertex with first coordinate of modulus \(1\), the absolute evaluation of \(z\) is at most \(1\): after fixing first coordinate \(1\), the possibilities are \((1,-1,\pm t)\) or \((1,\pm t,-1)\), whose evaluations on \(z\) are respectively \(-1\), \(1\), and \((1-3t)/(1+t)\). The last number lies in \([-1,1]\) for \(0<t\le1\).

Across *all* dual vertices, the largest absolute evaluation of \(z\) is exactly \(2-t\), achieved at \((t,1,-1)\), because
\[
(t,1,-1)(z)=\frac{t(1-t)+2}{1+t}=2-t.
\]
To see no larger value occurs, when the second coordinate is saturated the corresponding absolute evaluation is bounded by \((2+t(1-t))/(1+t)=2-t\); when the first coordinate is saturated it is bounded by \(1\); when the third coordinate is the sole unsaturated one, the first two have opposite signs and the absolute evaluation is \(1\). Hence \(\|z\|=2-t\).

Set \(T(x)=\varphi(x)z\). It follows that \(\|T\|=\|\varphi\|\|z\|=2-t\). For any extreme norming pair at \(p_1\), we have \(|u(Tp_1)|\le1\) by the preceding first-coordinate bound. At \(p_2\) or \(p_3\), the bound is \(|u(Tp_i)|\le\|z\|/2=(2-t)/2\le1\); at \(p_4\), the evaluation is zero. Thus \(v(T)\le1\). Equality holds at the norming pair \((p_1,(1,t,-1))\), because \(u(Tp_1)=u(z)=1\). So \(v(T)=1\), and \(v(T)/\|T\|=1/(2-t)\) proves sharpness.

## Verification
The preceding argument is a proof for **every real** \(0<t\le1\), not a finite parameter sweep. A standalone standard-library checker, `verify.py`, enumerates the exact rational dual vertices, reproduces the norming-pair inequalities, and verifies the displayed extremal rank-one operator for \(t\in\{1/5,1/3,1/2,2/3,3/4,9/10,1\}\). It also confirms an explicit norming-vertex decomposition for each nonnorming vertex at those parameters. Run `python verify.py`. Its output is `VERIFY_OK rational_parameters=7 three_dimensional_vertex_profiles=True analytic_family_proof_required=True`.

## Relationship to prior work
Cobollo, Guirao and Montesinos (2023) give the complete numerical index of every three-point Lipschitz-free space; the metric limit at \(t\downarrow0\) is their equilateral triangle case. Their theorem does not determine the index of this four-vertex three-dimensional family. Aliaga and Pernecká (2018) establish the general finite-support extreme-molecule criterion used to identify the primal vertices. McGregor's finite-dimensional characterization concerns the threshold value \(1\) and does not produce this quantitative formula. General polyhedral numerical-index methods likewise require additional estimates or exact optimization.

An existing qualitative weighted-cycle criterion determines exactly *when* the numerical index equals \(1\), including the unit-square endpoint and strict inequality for each shorter-edge deformation. Its threshold statement does not imply either the precise value \(1/(2-t)\) or the rank-one attainment proved here. Previously obtained exact cycle values for equal edge lengths likewise do not cover the interval \(0<t<1\).

## Limitations
The formula applies only to real spaces and four-vertex cycles with three consecutive edges of equal length and the last edge no longer than them. The interval \(t>1\), general independent edge weights, complex numerical indices, and operator-by-operator numerical radii are not determined here. The case \(t=0\) is a degenerate three-point metric and is mentioned only as a limit. The finite exact computations are supporting evidence; the proof of the full parameter interval is analytic. Prior-art searches cannot rule out every unindexed equivalent statement, and independent mathematical audit remains outstanding.

## References
1. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first public 2023-04-25), especially Theorem 1.1 and Sections 4–5.
2. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278v1 (first public 2018-10-26), Theorem 1.1.
3. C. M. McGregor, *Finite-dimensional normed linear spaces with numerical index 1*, J. London Math. Soc. (2) 3 (1971), 717–721, DOI:10.1112/jlms/s2-3.4.717.
4. D. Sain, K. Paul, P. Bhunia and S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778v2 (2018), finite-dimensional methods.
5. S. Pal, S. Roy and D. Sain, *A characterization of Banach spaces with numerical index one*, arXiv:2604.03690v1 (2026), modern statement of McGregor's finite-dimensional criterion.
