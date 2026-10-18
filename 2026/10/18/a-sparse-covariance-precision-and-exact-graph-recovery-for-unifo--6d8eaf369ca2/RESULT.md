# A sparse covariance precision and exact graph recovery for uniform Lipschitz potentials on cactus graphs

## Finding

**Theorem (uniform-interior covariance tomography on cactus graphs).** Let \(G=(V,E)\) be any finite connected simple cactus graph, \(n=|V|\ge2\), with unit-length edges and the shortest-path metric. A cactus has no edge belonging to two simple cycles; its cycles may meet at articulation vertices. Write \(H=\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\}\). Let \(X\) be uniformly distributed, with respect to Lebesgue measure on \(H\), in the centered real Lipschitz unit ball
\[
Q_G=\{x\in H:|x_u-x_v|\le1\text{ for all }uv\in E\}.
\]
For an integer \(r\ge3\), let \(f_m\) denote the density of the sum of \(m\) independent uniform variables on \([-1,1]\), explicitly
\[
f_m(s)=\frac{1}{2^m(m-1)!}\sum_{j=0}^{m}(-1)^j\binom mj(s+m-2j)_+^{m-1},\qquad m\ge2,
\]
where \(z_+=\max(z,0)\). Define the strictly positive rational constant
\[
a_r=\frac{r}{r-1}\frac{\int_{-1}^{1}s^2 f_{r-1}(s)\,ds}{\int_{-1}^{1} f_{r-1}(s)\,ds},
\qquad a_3=\frac5{12},\quad a_4=\frac25.
\]
Put \(w_e=3\) on every bridge, and \(w_e=1/a_r\) on each edge of a cycle of length \(r\). Set
\[
L_w=\sum_{e=uv\in E}w_e(e_u-e_v)(e_u-e_v)^{\mathsf T}.
\]
Then the **full** covariance and its Moore--Penrose precision are exactly
\[
\boxed{\operatorname{Cov}(X)=L_w^+,\qquad \operatorname{Cov}(X)^+=L_w.}
\]
In particular, for distinct labeled vertices \(u,v\),
\[
\boxed{\bigl(\operatorname{Cov}(X)^+\bigr)_{uv}<0\iff uv\in E.}
\]
Hence the covariance of the continuous **uniform interior** law recovers the complete labeled graph and the edge weights \(w_e\), without seeing the original graph. If \(b\) is the number of bridges and \(\mathcal C\) is the collection of distinct simple cycles, its intrinsic Euclidean covariance determinant on \(H\) is
\[
\boxed{\det_H\operatorname{Cov}(X)=\frac{3^{-b}}{n}\prod_{C\in\mathcal C}\frac{a_{|C|}^{|C|-1}}{|C|}.}
\]
The empty product equals one. Finally, for large cycles the effective conductance has the quantitative expansion
\[
a_r=\frac13+\frac{1}{5r}+O(r^{-2}),\qquad a_r^{-1}=3-\frac{9}{5r}+O(r^{-2}).
\]
The cactus restriction is substantial: for the unit-edge complete bipartite graph \(K_{2,3}\), labeling its two-vertex class by \(0,2\) and its three-vertex class by \(1,3,4\), the nonedge \(02\) has \(\bigl(\operatorname{Cov}(X)^+\bigr)_{02}=-3/8\), not zero. Thus sparse precision need not hold for non-cactus graphs.

These are statements about centered vertex potentials and uniform volume in the polar Lipschitz ball, not uniformly chosen vertices, uniformly sampled facet normals, lattice-uniform height functions, or Gaussian random fields.

## Assumptions and scope

The real scalar field and the fixed labeled Euclidean coordinates are essential. Edge length is one, and all pairwise metric inequalities are equivalent to the displayed edge inequalities by the path triangle inequality. A uniform law in anchored coordinates transported to the zero-mean subspace equals the law specified above: the change of coordinates is invertible with constant Jacobian, and the normalization removes that Jacobian. The graph can be a tree, a cycle, have several cycles sharing vertices, or contain arbitrarily many bridge attachments. There are no loops, multiple edges, or edges shared by distinct simple cycles. The covariance is a rank-\(n-1\) matrix acting on \(\mathbb R^V\), zero on the constant vector; the superscript \(+\) is the Moore--Penrose inverse in these canonical coordinates. The determinant is taken in an orthonormal basis of \(H\), not in arbitrary anchored coordinates.

## Proof

**1. Exact gradient parametrization.** Orient each cactus cycle consistently and each bridge arbitrarily. Let \(D:H\to\mathbb R^E\) send a potential to its oriented edge differences, \((Dx)_e=x_{e^+}-x_{e^-}\). As \(G\) is connected, \(D\) is injective. Since a cactus has edge-disjoint simple cycles, its cycle space has basis the oriented cycle indicator vectors \(\mathbf1_C\) with mutually disjoint supports. Therefore
\[
W:=D(H)=\mathbb R^{E_{\mathrm{bridge}}}\oplus\bigoplus_{C\in\mathcal C}
\left\{y\in\mathbb R^{E(C)}:\sum_{e\in C}y_e=0\right\}.
\]
The statement follows from \(D(H)=(\ker D^{\mathsf T})^\perp\): the displayed cycle vectors are independent, their number is \(|E|-|V|+1\), and hence they span \(\ker D^{\mathsf T}\). The image \(D(Q_G)\) is exactly \(W\cap[-1,1]^E\). Since \(D:H\to W\) has constant positive Jacobian, its pushforward of normalized uniform measure is normalized uniform measure on this cube section. The direct orthogonal product decomposition of \(W\) and the factorization of the cube now give independent bridge and cycle-block gradients.

**2. The covariance of each independent block.** Each bridge gradient is \(\operatorname{Unif}[-1,1]\), centered with variance \(1/3\). On a consistently oriented cycle with \(r\) edges, its gradient is uniform on
\[
K_r=\{y\in[-1,1]^r:\sum_{i=1}^r y_i=0\}.
\]
The coordinate permutations of \(K_r\) preserve its uniform measure, so its covariance is a scalar multiple of \(P_r=I_r-\mathbf1\mathbf1^{\mathsf T}/r\). To determine the scalar, condition \(r\) independent \(\operatorname{Unif}[-1,1]\) variables on their sum being zero in the standard density/disintegration sense. The resulting measure is precisely the uniform law on \(K_r\) because the normal Jacobian is constant. Its one-coordinate conditional density is proportional to \(f_{r-1}(-s)=f_{r-1}(s)\) for \(-1\le s\le1\). Thus the conditional coordinate variance is the ratio of the two displayed integrals, and since the diagonal of \(P_r\) equals \((r-1)/r\), the cycle-gradient covariance is exactly \(a_r P_r\). The denominator is positive and both integrals are rational: the inclusion--exclusion expression for \(f_{r-1}\) is a piecewise polynomial with integer breakpoints, so integration over \([-1,1]\) consists of finitely many rational endpoint evaluations.

**3. Precision and graph reconstruction.** Let \(K\) be the covariance of the complete edge-gradient vector \(Y=DX\), acting on \(W\). By Step 2 and independence,
\[
K=\frac13 I_{E_{\mathrm{bridge}}}\oplus\bigoplus_{C\in\mathcal C}a_{|C|}P_C
\quad\text{on }W.
\]
It is positive definite on \(W\), and its inverse there is \(3I\oplus\bigoplus_C a_{|C|}^{-1}P_C\). Since \(D:H\to W\) is a linear isomorphism, covariance transforms by congruence. Inverting that congruence gives, for all \(h,k\in H\),
\[
\langle h,\operatorname{Cov}(X)^{-1}_{H}k\rangle
=\langle Dh,K^{-1}Dk\rangle
=3\sum_{e\text{ bridge}}(Dh)_e(Dk)_e
+\sum_{C\in\mathcal C}\frac1{a_{|C|}}\sum_{e\in C}(Dh)_e(Dk)_e.
\]
The last equality uses \(P_CDk=Dk\) on every cycle. The right-hand side equals \(\langle h,L_wk\rangle\). This proves \(\operatorname{Cov}(X)=L_w^+\) in \(\mathbb R^V\). For distinct vertices, the off-diagonal entry of the Laplacian \(L_w\) is \(-w_{uv}<0\) on an edge and zero off the graph, because the cactus is simple and every \(w_e\) is positive. This proves labeled recovery. It **does not assert** that the non-Gaussian uniform law has conditional-independence relations given by the inverse covariance.

**4. Determinant.** The weighted matrix--tree identity gives \(\det_H L_w=n\tau_w\), where \(\tau_w\) is the weighted spanning-tree sum. In a cactus every bridge belongs to every spanning tree, and exactly one edge of each cycle must be removed; the choices across cycles are independent. Since the conductance is constant along any one cycle,
\[
\tau_w=3^b\prod_{C\in\mathcal C}|C|\,a_{|C|}^{-(|C|-1)}.
\]
Take its reciprocal to obtain the determinant formula. This also covers trees via the empty product.

**5. Large-cycle constant.** Write \(\psi(t)=\sin(t)/t\). The Fourier transforms of the sum density and of the second-moment-weighted sum density, evaluated at zero, give
\[
\frac{r-1}{r}a_r=
\frac{\int_{\mathbb R}[-\psi''(t)]\psi(t)^{r-1}\,dt}
{\int_{\mathbb R}\psi(t)^r\,dt}.
\]
The integrals are absolutely convergent for \(r\ge3\); this is simply Fourier inversion of the conditional density calculation in Step 2. Near zero,
\[
\log\psi(t)=-\frac{t^2}{6}+O(t^4),\qquad
\frac{-\psi''(t)}{\psi(t)}=\frac13-\frac{2t^2}{45}+O(t^4).
\]
Rescale \(t=u/\sqrt r\). Gaussian integration shows that under the normalized \(\psi(t)^r\) weight, \(\mathbb E[t^2]=3/r+O(r^{-2})\) and \(\mathbb E[t^4]=O(r^{-2})\). These estimates are justified by analytic Taylor bounds on a fixed neighborhood of zero and exponentially small tails: \(|\psi(t)|<1\) away from zero and \(|\psi(t)|\le1/|t|\) for \(|t|\ge1\). The weight may change sign for odd \(r\), but its signed tail is exponentially smaller than the positive main integral, so the ratio expansion remains valid. Therefore
\[
\frac{r-1}{r}a_r=\frac13-\frac{2}{15r}+O(r^{-2}),
\]
which rearranges to the two claimed expansions.

**6. Natural non-cactus boundary.** For the unit-edge \(K_{2,3}\), label the two-vertex class \(0,2\) and the other class \(1,3,4\). Work modulo translation with hub values \(h/2,-h/2\). The three remaining potentials, conditionally on \(h\), are independent uniforms on \([-1+|h|/2,1-|h|/2]\), for \(|h|\le2\). The marginal density of \(h\) is proportional to \((2-|h|)^3\); direct beta integration gives \(\mathbb E h^2=4/15\), \(\mathbb E|h|=2/5\), and each leaf's unconditional coordinate variance before centering is \(\mathbb E[(1-|h|/2)^2]/3=2/9\). Orthogonal decomposition into the hub contrast, the two-dimensional leaf-contrast subspace, and the one-dimensional hub-versus-leaf contrast yields covariance eigenvalues \(2/15,2/9,4/45\), respectively. Inverting them on the zero-sum space, the resulting precision is precisely
\[
\begin{pmatrix}
57/8&-9/4&-3/8&-9/4&-9/4\\
-9/4&9/2&-9/4&0&0\\
-3/8&-9/4&57/8&-9/4&-9/4\\
-9/4&0&-9/4&9/2&0\\
-9/4&0&-9/4&0&9/2
\end{pmatrix}.
\]
The entry \(02\) is nonzero even though there is no edge. This is a finite exact counterexample to a **universal** edge-supported precision claim; it does not assert the cactus class is maximal.

## Verification

Run `python check.py` with SymPy installed. The independent calculation enumerates integer-valued anchored Lipschitz potentials in the integer dilates of the actual graph polytope. By total unimodularity of the directed graph incidence matrix, this polytope is a lattice polytope. The lattice-point count is an Ehrhart polynomial of degree \(n-1\); sums of centered coordinate-pair products are weighted Ehrhart polynomials of degree \(n+1\). Forward differences recover their leading coefficients exactly, and their ratio yields the continuous covariance. The checker compares **every** covariance entry against \(L_w^+\), also checks the intrinsic determinant and the precision off-diagonal support.

Seven exact cactus configurations pass, and the distinct \(K_{2,3}\) non-cactus boundary matrix is checked exactly: a triangle, a square, a triangle with a bridge, a square with a bridge, two triangles sharing one vertex, a four-vertex path, and two triangles joined by a bridge. They cover graphs of up to six vertices with zero, one or two cycles. The proof in the preceding section, not these finite tests, establishes the result for all cactus graphs. The explicit non-cactus example proves that edge-supported precision is not universal, without classifying all graphs for which it nevertheless holds.

## Relationship to prior work

Novotný's 2019 study (arXiv:1905.13188, primary MSC 46B20) studies retractional Schauder bases for graph-circle Lipschitz-free spaces. Dilworth, Kutzarova and Ostrovskii (arXiv:1807.03814) establish finite-graph transportation quotients by cycle flows, rather than uniform **interior** covariance. Peled (arXiv:1005.4636) studies principally **integer-valued** random Lipschitz height functions and explicitly discusses real-valued models as a distinct problem. The published calculation titled *Sharp coordinate-projection norms for edge bases of cactus transportation spaces* concerns coordinate projection operator norms, not covariance.

A related exact cactus covariance calculation for **uniformly selected facet normals** has a different sampling law, different conductances, and a different determinant; its existence is not used to claim the underlying idea of a graph-Laplacian Green kernel as new. A previously recorded **single weighted cycle** precision calculation concerns an anchored cube **slab**, and its precision cannot alone cover independent combinations of arbitrary cactus cycle blocks and bridges. The new claim is the explicit uniform-volume precision and graph-recovery theorem across all connected cacti, including simultaneous distinct cycle lengths, with exact block weights and determinant. No assertion of universal bibliographic novelty is made.

## Limitations

The theorem is exact only for the unit-edge cactus metric, uniform continuous interior sampling, and the specified labeled Euclidean representation; it does not give a Gaussian Markov structure, statistical sample complexity for estimating covariance, or universal non-cactus precision sparsity; indeed, the exhibited \(K_{2,3}\) shows the latter is false. The recovery is population-level and assumes exact covariance and labels. Earlier cycle-space and graph covariance results are mathematical foundations or nearby special models; an unindexed equivalent formula could exist. The secondary large-cycle expansion is asymptotic and supplies no explicit universal error constant.

## References

1. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, initially posted 2019-05-30; primary MSC 46B20. https://arxiv.org/abs/1905.13188.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz Free Spaces on Finite Metric Spaces*, arXiv:1807.03814 (2018). https://arxiv.org/abs/1807.03814.
3. R. Peled, *High-Dimensional Lipschitz Functions Are Typically Flat*, arXiv:1005.4636 (2010 initial preprint). https://arxiv.org/abs/1005.4636.
4. *Sharp Coordinate-Projection Norms for Edge Bases of Cactus Transportation Spaces*, publicly accessible `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd.
