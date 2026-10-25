# Book-graph Lipschitz polytopes have a sharp three-page inertia crossing

## Finding
For each integer \(m\ge2\), let \(G_m\) be the *book graph*: two adjacent hubs and \(m\) other vertices adjacent to each hub, with no edges between those other vertices. Write \(N=m+2\), \(d=m+1\), and take the intrinsic Euclidean Lipschitz polytope
\[
 Q_m=\bigl\{x\in\mathbb R^N:\sum_i x_i=0,\ |x_u-x_v|\le1\text{ for every edge }uv\in E(G_m)\bigr\}.
\]
It is the Euclidean polar in \(\mathbf1^\perp\) of the symmetric edge polytope of \(G_m\). Define the positive rational quantities
\[
 D_k=\frac{2^{k+1}-1}{k+1},\qquad
 T_m=4-4\frac{D_{m+1}}{D_m}+\frac{D_{m+2}}{D_m},\qquad
 B_m=\frac{D_{m+2}}{12D_m}.
\]
For a uniformly distributed volume point \(X\in Q_m\), the following identities hold exactly:
\[
 \operatorname{vol}_{d}(Q_m)=\frac{2D_m}{\sqrt N},\qquad
 \operatorname{Spec}(\operatorname{Cov}X)=
 \left\{\frac{T_m}{2}\ (1),\ \frac{2B_m}{N}\ (1),\ B_m\ (m-1)\right\}.
\]
Parenthetical numbers are eigenspace multiplicities. The hub-difference eigendirection has eigenvalue \(T_m/2\), the hub-versus-leaf-block direction has \(2B_m/N\), and leaf contrasts have \(B_m\). Their ordering undergoes one exact crossing:
\[
 \frac{2B_2}{4}<\frac{T_2}{2}<B_2,\qquad
 \frac{T_3}{2}=\frac{2B_3}{5}<B_3,\qquad
 \frac{T_m}{2}<\frac{2B_m}{m+2}<B_m\quad (m\ge4).
\]
In particular the two smallest eigenspaces exchange order exactly at \(m=3\). The covariance condition number and affine-invariant isotropic constant satisfy
\[
 \kappa(\operatorname{Cov}X)\sim\frac{m^2}{12},\qquad
 L(Q_m)^{2d}=\frac{T_m B_m^m}{4D_m^2},\qquad
 L(Q_m)\longrightarrow\frac1{\sqrt{12}}.
\]
As a separate exact volume comparison, adding the hub edge to \(K_{2,m}\) retains exactly \(1-2^{-(m+1)}\) of its Lipschitz-polar volume.

## Assumptions and scope
The graph is simple and unweighted, the hub edge and every hub-to-leaf edge have length one, and \(m\ge2\) is an integer. Volume, covariance and eigenvalues refer to the intrinsic dimension \(d=m+1\) in \(\mathbf1^\perp\) with its inherited Euclidean metric, not to the lattice-normalized measure or to the discrete vertex distribution. The isotropic constant is defined by \(L(K)^{2d}=\det(\operatorname{Cov}(\mathrm{Unif}(K)))/\operatorname{vol}_{d}(K)^2\). No independent validation is asserted.

## Proof
Choose anchored coordinates \(x_0=0\), \(x_1=t\) at the hubs and coordinates \(y_1,\ldots,y_m\) at the leaves. Shifting all coordinates by the same constant identifies these anchored coordinates linearly with \(\mathbf1^\perp\). The induced Euclidean Jacobian equals \(1/\sqrt N\) (the Gram determinant of the projected coordinate vectors is \(1/N\)). The hub edge requires \(|t|\le1\), and every leaf must lie in \([-1,1]\cap[t-1,t+1]\), an interval of length \(2-|t|\), centered at \(t/2\).

Thus the integration measure in anchored coordinates is \((2-|t|)^m\,dt\) after leaf integration. Write \(D_m=\int_0^1(2-t)^m\,dt\). Its integral is \(2D_m\), giving \(\operatorname{vol}_d(Q_m)=2D_m/\sqrt N\). In particular without the hub edge, \(|t|\le2\), so the corresponding complete-bipartite integral is \(2\int_0^2(2-t)^m\,dt=2^{m+2}/(m+1)\), proving the stated volume ratio.

Under normalized volume measure \(t\) is symmetric with density \((2-|t|)^m/(2D_m)\). Conditional on \(t\), one can write the anchored leaf coordinates as \(y_j=t/2+\eta_j\), with the \(\eta_j\) independent and uniform on \([-(2-|t|)/2,(2-|t|)/2]\). The centered projected vector is
\[
 X=\frac{t}{2}(-1,1,0,\ldots,0)+P(0,0,\eta_1,\ldots,\eta_m),\qquad P=I-\frac{\mathbf1\mathbf1^{\mathsf T}}N.
\]
The conditional noises have mean zero. Hence they have zero cross covariance with \(t\), with all leaves mutually uncorrelated, and their unconditional common variance is
\[
 \mathbb E\eta_j^2=\frac{\int_0^1(2-t)^{m+2}\,dt}{12D_m}=B_m.
\]
The hub-gap variance is
\[
 \mathbb Et^2=\frac{\int_0^1t^2(2-t)^m\,dt}{D_m}=4-4\frac{D_{m+1}}{D_m}+\frac{D_{m+2}}{D_m}=T_m.
\]
The orthogonal \(S_m\)-invariant decomposition of \(\mathbf1^\perp\) consists of the hub difference, the \((m-1)\)-dimensional leaf-contrast space, and the remaining hub-versus-leaf-block line. Projecting the noise covariance \(B_m\operatorname{diag}(0,0,1,\ldots,1)\) to these three subspaces gives the eigenvalues \(0\), \(B_m\), and \(2B_m/N\), respectively. The hub-gap term contributes precisely \(T_m/2\) on the hub-difference line. This proves the spectrum and
\[
 \det\operatorname{Cov}(X)=\frac{T_m B_m^m}{N}.
\]

For the sharp crossing, algebraic substitution of \(D_k=(2^{k+1}-1)/(k+1)\) gives
\[
 (m+2)(4D_m-4D_{m+1}+D_{m+2})-\frac{D_{m+2}}3
 =-\frac{2^{m+1}(4m-20)+3m^2+20m+41}{3(m+1)(m+3)}.
\]
Its sign is that of \(T_m/2-2B_m/(m+2)\). The numerator on the right is negative for \(m=2\), zero for \(m=3\), positive at \(m=4\), and strictly positive for all \(m\ge5\). Also \(2B_m/(m+2)<B_m\). At \(m=2\) direct exact values \(T_2/2=4/35\), \(2B_2/4=31/280\) and \(B_2=31/140\) complete the ordering.

Finally \(D_m\sim 2^{m+1}/(m+1)\). The hub-gap density and its exponential rescaling show \(m|t|/2\Longrightarrow\operatorname{Exp}(1)\), with convergence of second moments, so \(T_m\sim8/m^2\); also \(B_m\to1/3\). For \(m\ge4\), the largest and smallest eigenvalues are \(B_m\) and \(T_m/2\), respectively, and therefore \(\kappa\sim m^2/12\). Combining the determinant with the volume gives the displayed exact isotropic-constant identity, and taking its \(1/d\)-th power yields \(L(Q_m)^2\to1/12\).

## Verification
The included `check.py` verifies the rational identities, signs and unique eigenvalue crossing for dimensions \(m=2,\ldots,100\); separately evaluates the two basic moment integrals numerically for \(m=2,\ldots,8\); and independently computes anchored-coordinate convex hull volumes from the facet inequalities for \(m=2,3\). These finite checks corroborate, but do not replace, the all-dimensional proof above. Execute `python check.py` with Python, NumPy, and SciPy installed.

## Relationship to prior work
D'Alì, Delucchi and Michałek established the symmetric-edge, adjacency, and Kantorovich–Rubinstein connections, including the Lipschitz-polar definition; Gordon and Petrov studied the face combinatorics of finite-metric Lipschitz polytopes. The existing complete-bipartite \(K_{2,m}\) polar analysis has a different allowed hub-gap interval: adding the hub edge truncates it from \([-2,2]\) to \([-1,1]\). Existing book-graph results about the Löwner ellipsoid of the primal symmetric edge polytope are distinct from the covariance ellipsoid of the polar's continuous uniform measure. The present claim is specifically the exact three-mode covariance spectrum, its sharp finite crossing, its asymptotic anisotropy and its isotropic limit for the *non-cactus* book family.

## Limitations
This result concerns unweighted book graphs and uniform volume sampling only. It does not classify arbitrary graph-Lipschitz bodies, weighted books, or their John/Löwner ellipsoids. A broader equivalent in general uniform-slice integration or an unindexed source cannot be ruled out by bibliographic searching alone. No independent mathematical audit has been performed.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public October 11, 2019), Sections 2 and 4. https://arxiv.org/abs/1910.05193
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (2016), Sections 1–2. https://arxiv.org/abs/1608.06848
3. A. Mori, K. Mori, H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (2023); only abstract compared. https://arxiv.org/abs/2312.11287
