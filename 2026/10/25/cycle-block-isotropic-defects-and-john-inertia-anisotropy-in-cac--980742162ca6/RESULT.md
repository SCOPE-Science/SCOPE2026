# Cycle-block isotropic defects and John–inertia anisotropy in cactus Lipschitz polytopes

## Finding
Let \(G=(V,E)\) be any finite connected simple cactus graph, with \(n=|V|\ge2\), bridge count \(b\), and edge-disjoint simple cycles \(C_1,\ldots,C_c\) of lengths \(m_1,\ldots,m_c\ge3\). Put \(d=n-1\) and consider the intrinsic polar of its symmetric edge polytope,
\[
Q_G=\{x\in\mathbb R^V:\sum_{v\in V}x_v=0,\ |x_u-x_v|\le1\text{ for every }uv\in E\}.
\]
For each integer \(m\ge3\), let \(f_m\) be the density of the sum of \(m\) independent \(\operatorname{Unif}[-1,1]\) random variables, and set
\[
v_m=\frac{\int_{-1}^1t^2 f_{m-1}(t)\,dt}{\int_{-1}^1f_{m-1}(t)\,dt},\qquad
\Theta_m=\frac{\left(3m v_m/(m-1)\right)^{m-1}}{4m f_m(0)^2}.
\]
Then \(0<v_m<1/3\), and all the following identities hold for *every* such cactus, including trees (empty products equal one):
\[
\boxed{\operatorname{vol}_d(Q_G)=\frac{2^{|E|}}{\sqrt n}\prod_{i=1}^c f_{m_i}(0),\qquad
\left(12L(Q_G)^2\right)^d=\prod_{i=1}^c\Theta_{m_i}.}\tag{1}
\]
Here \(L(K)\) is the affine-invariant isotropic constant, defined precisely below. Both formulas depend on cycle lengths and the elementary graph counts, not on where the cycles or bridges are attached. In particular,
\[
\boxed{\Theta_3=\frac{25}{27},\quad\Theta_4=\frac{243}{250}.}\tag{2}
\]
For example, if every cycle is a triangle, then \((12L(Q_G)^2)^d=(25/27)^c\) *exactly*, irrespective of all bridge attachments.

There is also a precise John/inertia distinction. Orient each cycle consistently, orient bridges arbitrarily, and write \(y_e=x_{\mathrm{head}(e)}-x_{\mathrm{tail}(e)}\). Let
\[
W=\bigoplus_{i=1}^c\left\{y\in\mathbb R^{m_i}:\sum_{e\in C_i}y_e=0\right\}\oplus\mathbb R^b.
\]
The edge-difference map \(B:\{\sum x_v=0\}\to W\) is an isomorphism. The unique John ellipsoid of \(Q_G\), expressed by its image under \(B\), is
\[
\boxed{B(J(Q_G))=\left\{y\in W:
\sum_{i=1}^c\frac{m_i-1}{m_i}\|y_{C_i}\|_2^2
+\sum_{e\text{ bridge}}y_e^2\le1\right\}.}\tag{3}
\]
For \(X\) uniform in \(Q_G\), its John-normalized image \(Z\) is obtained by dividing each cycle block of \(BX\) by \(\sqrt{m_i/(m_i-1)}\) and leaving bridge coordinates unchanged. Its covariance is exactly
\[
\boxed{\operatorname{Cov}(Z)=\bigoplus_{i=1}^c v_{m_i} I_{m_i-1}\ \oplus\ \frac13 I_b.}\tag{4}
\]
Consequently, whenever \(G\) has both a cycle and a bridge, its volume-inertia ellipsoid is **not** homothetic to its John ellipsoid. The contrast persists upon arbitrarily many pendant-edge additions, although for fixed cycle lengths the isotropic constant tends to \(1/\sqrt{12}\) as the number of bridges increases. For a graph containing only triangles as cycles and at least one bridge, the John-position covariance condition number is exactly \(6/5\), independently of its number of vertices or attachment arrangement.

## Assumptions and scope
A cactus is a connected finite simple graph in which each edge belongs to at most one simple cycle; cycles may share vertices but cannot share edges. Its \(c\) cycles are independent and its numbers satisfy \(|E|=b+\sum_i m_i\) and \(d=b+\sum_i(m_i-1)\). No parity or orientation restriction is imposed on the original undirected graph.

For a full-dimensional convex body \(K\) in a \(d\)-dimensional Euclidean space, write \(\Sigma_K\) for the covariance operator of its uniform volume distribution and define
\[
L(K)^{2d}=\frac{\det\Sigma_K}{\operatorname{vol}_d(K)^2}.
\]
This is invariant under all invertible affine maps between \(d\)-dimensional Euclidean spaces. The John ellipsoid is the unique maximal-volume ellipsoid contained in \(K\). The 'inertia ellipsoid' refers to the ellipsoid centered at the centroid with quadratic shape proportional to \(\Sigma_K\); its normalization is irrelevant for homothety comparisons.

All volumes here are ordinary intrinsic Euclidean Hausdorff volumes, not lattice-normalized volumes. In (3) the John ellipsoid itself is an ellipsoid in the zero-sum vertex-coordinate hyperplane; (3) describes its edge-difference image and does **not** claim that the edge-difference map is an isometry.

## Proof
**1. Edge-coordinate product and Jacobian.** Choose consistent orientations along each of the edge-disjoint cycles. Since a potential difference sums to zero along a cycle, \(B(H)\subseteq W\), where \(H=\{x:\sum_vx_v=0\}\). Connectivity makes \(B\) injective on \(H\). Because \(\dim W=b+\sum_i(m_i-1)=n-1=\dim H\), it is an isomorphism. The inequalities defining \(Q_G\) become
\[
B(Q_G)=\prod_{i=1}^c\left([-1,1]^{m_i}\cap\{\textstyle\sum_jy_j=0\}\right)\times[-1,1]^b=:K_W.
\tag{5}
\]
The squared intrinsic Jacobian of \(B\) is the product of the positive eigenvalues of the graph Laplacian \(B^{\mathsf T}B\). By the matrix-tree identity it equals \(n\tau(G)\), where \(\tau(G)\) is the spanning-tree count. A cactus spanning tree is obtained by deleting exactly one edge from each of its cycles, hence \(\tau(G)=\prod_i m_i\). Therefore
\[
|\det(B|_H)|=\sqrt{n\prod_i m_i}.
\tag{6}
\]

**2. Intrinsic volume and one-block covariance.** Let \(U_1,\ldots,U_m\) be independent uniforms on \([-1,1]\). Coarea applied to their sum gives the exact Euclidean \((m-1)\)-volume
\[
\operatorname{vol}_{m-1}([-1,1]^m\cap\{\sum_j y_j=0\})=2^m\sqrt m\,f_m(0).
\tag{7}
\]
The uniform distribution on this central section is the conditional distribution of \((U_1,\ldots,U_m)\) given \(\sum_j U_j=0\), in the usual regular-conditional-density sense. Symmetry gives zero mean. Conditioning on \(U_1=t\) gives marginal density proportional to \(f_{m-1}(-t)\) for \(|t|\le1\), so its diagonal variance is \(v_m\). Exchangeability and \(\sum_jU_j=0\) imply all off-diagonal covariances equal \(-v_m/(m-1)\), and therefore the covariance operator on the zero-sum subspace is \(\frac{m}{m-1}v_m I_{m-1}\). For the independent bridge factors the variance is \(1/3\).

The symmetric convolutions \(f_k\) are strictly decreasing on the positive interior of their support for all \(k\ge2\): the triangular density \(f_2\) has this property, and differentiation of the uniform convolution gives \(f_{k+1}'(t)=\tfrac12(f_k(t+1)-f_k(t-1))<0\) for \(0<t<1\). Accordingly, \(t^2\), increasing in \(|t|\), is strictly negatively correlated with \(f_{m-1}(t)\) under a uniform \([-1,1]\) variable. The conditional second moment satisfies \(0<v_m<1/3\).

Combining the product volume (5), section formula (7), and Jacobian (6) proves the first identity in (1).

**3. Exact isotropic-defect factorization.** By the preceding covariance calculation,
\[
\det\operatorname{Cov}(BX)=3^{-b}\prod_i\left(\frac{m_i}{m_i-1}v_{m_i}\right)^{m_i-1},
\]
while
\[
\operatorname{vol}_d(K_W)=2^{|E|}\prod_i\sqrt{m_i}\,f_{m_i}(0).
\]
The isotropic constant is affine invariant, so it can be calculated in edge coordinates. Substitute these two expressions into its definition and use \(d=b+\sum_i(m_i-1)\) and \(|E|=d+c\). After canceling powers of two and three, the answer is exactly
\[
\left(12L(Q_G)^2\right)^d=
\prod_i\frac{(3m_i v_{m_i}/(m_i-1))^{m_i-1}}{4m_i f_{m_i}(0)^2}.
\]
In particular, adding a bridge changes \(d\) but does not change the right-hand side.

**4. Exact John ellipsoid.** Write \(H_m=\{y:\sum_j y_j=0\}\). The cube section \([-1,1]^m\cap H_m\) is invariant under all coordinate permutations and central inversion. Uniqueness of its John ellipsoid forces a centered Euclidean ball in \(H_m\), since the permutation representation on \(H_m\) is irreducible. The distance within \(H_m\) from the origin to any coordinate facet \(y_j=\pm1\) is
\[
r_m=1/\|\Pi_{H_m}e_j\|=\sqrt{m/(m-1)}.
\]
Thus the John ellipsoid of each cycle section is the ball of radius \(r_m\); that of each bridge interval is the unit interval. The John ellipsoid of a Cartesian product of centered convex bodies is the ellipsoid with the *sum* of their individual John quadratic forms at most one. To verify this last assertion, map the factor John ellipsoids to unit balls, take the unit ball in the product space, and combine the individual symmetric John contact decompositions on mutually orthogonal coordinate blocks. Its contacts certify maximality in the product. Applying this lemma to (5) gives (3) by affine equivariance.

Rescaling the cycle blocks by \(r_m\) makes this ellipsoid the unit ball. Their covariance eigenvalues become \((m/(m-1))v_m/r_m^2=v_m\), while bridge eigenvalues remain \(1/3\). This proves (4) and the strict failure of John/inertia homothety for every mixed cactus.

**5. Exact examples and limiting contrast.** The convolution spline formula
\[
f_m(0)=\frac1{2^m(m-1)!}\sum_{j=0}^{\lfloor m/2\rfloor}(-1)^j\binom mj(m-2j)^{m-1}
\tag{8}
\]
permits exact integration of the polynomial pieces of \(f_{m-1}\). It gives \(f_3(0)=3/8\), \(v_3=5/18\), \(f_4(0)=1/3\), \(v_4=3/10\). Substitution yields (2). If the number of cycles and all their lengths are held fixed while \(b\to\infty\), then \(d\to\infty\) and the right side of the second identity in (1) remains a fixed positive constant. Therefore \(L(Q_G)\to1/\sqrt{12}\). The John-coordinate covariance retains its fixed cycle eigenvalues strictly below \(1/3\), independently of added bridge coordinates. For exclusively triangular cycles and \(b>0\), the two eigenvalues are \(5/18\) and \(1/3\), giving ratio \(6/5\).

## Verification
The included Python 3 checker `verify.py` needs only the standard library. It independently integrates the explicit polynomial spline pieces using exact rational arithmetic, checks the cycle densities and conditional variances for cycle lengths \(3\) through \(12\), recovers \(\Theta_3=25/27\) and \(\Theta_4=243/250\), and verifies the graph matrix-tree count and cycle/bridge bookkeeping on seven distinct cactus configurations, including two cycles sharing a vertex. Seeded numerical rejection sampling separately checks the zero-sum-section conditional variances for cycle lengths \(3\) through \(6\). Execute `python verify.py` from the directory containing this document and script. Its tested completion marker is `VERIFY_OK`. Exact computations test special instances and identities; the proof above establishes the general results.

## Relationship to prior work
D'Alì, Delucchi and Michałek developed the graph-to-Lipschitz/Kantorovich–Rubinstein connection and showed that vertex gluing of graph symmetric edge polytopes corresponds to a direct sum; their Section 4 treats even cycles and outerplanar graphs. This prior direct-sum structure is explicitly used in motivation and **not claimed as new**. The present statement instead gives the ordinary intrinsic polar volume, the *volume-uniform covariance*, the exact John ellipsoid, and an isotropic-defect factor for cactus cycles of **any** length, including odd ones.

The general multiplicative formula for isotropic constants under Cartesian products is classical; it also appears in a published result on Hanner polytopes (see references). That general formula is background, not a claim of novelty. The cycle-section factors \(\Theta_m\), the graph-polar interpretation and exact John/inertia dichotomy for mixed cacti are the assessed contributions. A separate published result on semi-balanced cactus *root* polytopes concerns affine Minkowski asymmetry of a different, generally nonsymmetric polytope; it neither states nor implies the present volume-uniform covariance and isotropic identities. Results on cycle-graph symmetric-edge *inradii*, as well as graphical zonotope Laplacian spectra, also study different bodies or invariants.

## Limitations
The formulas require edge-disjoint cycles (cactus graphs). For general graphs, overlapping cycle constraints prevent the product decomposition (5). The reported strict anisotropy conclusion requires at least one cycle and one bridge; no classification of equality among multiple unequal cycle lengths without bridges is asserted. The constants \(f_m(0)\) and \(v_m\) arise from classical univariate uniform-convolution spline facts. It remains possible that the same graph-family identities have been written elsewhere using central cube sections, probability-bridge, or product-isotropy terminology; the literature checks are evidence of a gap, not a universal priority proof. No independent mathematical audit is represented.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (11 October 2019), especially Definition 2.1, Theorem 2.5, Sections 4.1–4.2 and 4.4–4.5; *Electronic Journal of Combinatorics* 29 (2022), P3.24, DOI 10.37236/10387. The primary subject classification in the preprint is 52B20.
2. *Sharp isotropic-constant range of all Hanner polytopes*, publicly accessible mathematical research record, 2026-10-11, identifier `2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2`. Formula (2) in that record treats the general Cartesian-product isotropic recursion; it does not supply cycle-section factors.
3. *Exact Minkowski asymmetry and unique centers of semi-balanced cactus root polytopes*, publicly accessible mathematical research record, 2026-10-11, identifier `2026/10/11/SCOPE-exact-minkowski-asymmetry-and-unique-centers-of-semi-balanced-ca--a52784552f6c`. This concerns a different root-polytope invariant and is not a premise of the proof.
