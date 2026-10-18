# A sharp continuum of Euclidean mean widths among lattice-equivalent tree crosspolytopes

## Finding
For every tree \(T\) on \(n\ge3\) vertices, put
\[
H_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\},\qquad
P_T=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(T)\}\subset H_n.
\]
Use the Euclidean norm inherited from \(\mathbb R^n\) and define mean width by
\[
w(P_T)=\mathbb E_{U\in S(H_n)}[h_{P_T}(U)+h_{P_T}(-U)]
\]
for uniform intrinsic unit direction \(U\). Let \(Z_1,\ldots,Z_n\) be independent standard normal random variables, let
\[
M_T=\max_{\{i,j\}\in E(T)}|Z_i-Z_j|,\qquad
 a_{n-1}=\sqrt2\,\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}.
\]
Then the exact identity is
\[
\boxed{w(P_T)=\frac{2\,\mathbb E M_T}{a_{n-1}}.}
\]
Every one of these polytopes is a lattice-unimodular copy of the \((n-1)\)-dimensional standard crosspolytope; their face vectors and Ehrhart polynomials coincide, and each has the same intrinsic Euclidean volume
\[
\boxed{\operatorname{vol}_{n-1}(P_T)=\frac{2^{n-1}\sqrt n}{(n-1)!}.}
\]
Nevertheless their normalized mean widths have **exactly the full interval of attainable limit constants**
\[
\boxed{[\,2\sqrt2,\,4\,].}
\]
Precisely, for every sequence of \(n\)-vertex trees \(T_n\),
\[
2\sqrt2\le\liminf_{n\to\infty}\sqrt{\frac{n}{\log n}}w(P_{T_n})
\le\limsup_{n\to\infty}\sqrt{\frac{n}{\log n}}w(P_{T_n})\le4,
\]
and for each \(c\) in the displayed interval there exists a sequence of trees for which the scaled mean width converges to \(c\). The lower endpoint is realized by stars, the upper by paths, and every intervening constant by brooms with a prescribed power-law handle length.

There is also a nonasymptotic comparison, valid for every such tree:
\[
\boxed{\frac{2}{a_{n-1}}\left(\mathbb E\max_{1\le i\le n}|Z_i|-\sqrt{\frac2\pi}\right)
\le w(P_T)\le\frac{4}{a_{n-1}}\sqrt{\log(2n-2)}.}
\]

## Assumptions and scope
The graph is a finite simple connected tree, with no edge weights; its canonical root realization in \(H_n\) is essential. Volume and mean width always use the intrinsic Euclidean metric, not an abstract lattice metric or a rescaled individual polytope. A claim about sharp **asymptotic** endpoints is not a claim that stars or paths uniquely optimize mean width at every finite \(n\). A Gaussian vector is independent coordinatewise before projection onto \(H_n\); ties have probability zero.

## Proof
**1. Crosspolytope and volume.** Arbitrarily orient each edge and form the incidence columns \(b_e=e_i-e_j\). A tree has \(n-1\) edges and the columns are a \(\mathbb Z\)-basis of the root lattice \(A_{n-1}=H_n\cap\mathbb Z^n\): deleting any one row leaves an integer matrix with determinant \(\pm1\). Thus the signed-column convex hull is the image of the standard crosspolytope under a lattice isomorphism. By Cauchy–Binet, every maximal minor of the \(n\)-row incidence matrix has absolute determinant one, and
\[
\det(B^\mathsf TB)=\sum_{j=1}^n\det(B_{\widehat j})^2=n.
\]
The image of the standard crosspolytope therefore has Euclidean volume \(2^{n-1}\sqrt n/(n-1)!\). The lattice-isomorphism gives the common Ehrhart polynomial and face vector independently of the Euclidean calculation.

**2. Gaussian width identity.** The support function of \(P_T\) is
\[
h_{P_T}(x)=\max_{\{i,j\}\in E(T)}|x_i-x_j|.
\]
Let \(Z_H\) be the orthogonal projection of \(Z=(Z_1,\ldots,Z_n)\) onto \(H_n\). Since every edge root lies in \(H_n\), \(h_{P_T}(Z)=h_{P_T}(Z_H)=M_T\). The direction \(Z_H/\|Z_H\|\) is uniform on the intrinsic unit sphere and independent of \(\|Z_H\|\), whose mean is \(a_{n-1}\). Finally central symmetry gives \(w(P_T)=2\mathbb E h_{P_T}(U)\). This proves the exact identity without any approximation.

**3. Uniform finite bounds.** Write \(A_n=\max_i|Z_i|\). Choose, once and for all, a neighbor \(j(i)\) of each vertex \(i\), and let \(I\) be the almost-surely unique maximizing index of \(|Z_i|\). Then
\[
M_T\ge |Z_I-Z_{j(I)}|\ge A_n-|Z_{j(I)}|.
\]
Conditionally on \(I=i\) and \(|Z_i|=a\), the absolute values at all other vertices have the half-normal law truncated above at \(a\). A truncated-above nonnegative random variable has mean no greater than its untruncated mean. Consequently
\[
\mathbb E|Z_{j(I)}|\le\mathbb E|Z_1|=\sqrt{2/\pi},
\quad \mathbb EM_T\ge\mathbb EA_n-\sqrt{2/\pi}.
\]
For the upper bound, \(M_T\) is the maximum of \(2(n-1)\) centered Gaussian linear forms \(\pm(Z_i-Z_j)\), each of variance two. For every \(\lambda>0\), Jensen's inequality and the Gaussian exponential moment give
\[
\mathbb EM_T\le\frac{\log(2n-2)}\lambda+\lambda.
\]
Minimizing at \(\lambda=\sqrt{\log(2n-2)}\) gives \(\mathbb EM_T\le2\sqrt{\log(2n-2)}\). Substitute into the exact width identity for both claimed inequalities.

**4. Sharp uniform asymptotics.** Standard elementary Gaussian tail estimates yield
\[
\mathbb EA_n\sim\sqrt{2\log n},\qquad a_{n-1}\sim\sqrt n.
\]
The finite bounds therefore imply the universal interval bounds for every sequence of trees.

For the star with hub \(0\), the triangle inequality yields
\[
\max_{j\ne0}|Z_j|-|Z_0|\le M_{\mathrm{star}}\le
\max_{j\ne0}|Z_j|+|Z_0|,
\]
so \(\mathbb EM_{\mathrm{star}}\sim\sqrt{2\log n}\), proving the lower endpoint.

For the path, all \(n-1\) edge differences are centered normal of variance two. The collection of \(\lfloor n/2\rfloor\) disjoint edges yields independent differences; therefore its maximum absolute increment has expectation \((2+o(1))\sqrt{\log n}\). The preceding upper bound shows that the maximum over all path edges has exactly the same leading asymptotic. Hence \(\mathbb EM_{\mathrm{path}}\sim2\sqrt{\log n}\), proving the upper endpoint.

**5. Every intermediate constant.** Fix \(1/2\le\alpha<1\). Form a broom with path edges \(\{0,1\},\ldots,\{m_n-1,m_n\}\), where \(m_n=\lfloor n^\alpha\rfloor\), and attach all remaining vertices directly to \(0\). The maximum over its hub-leaf edges, divided by \(\sqrt{\log n}\), converges in probability to \(\sqrt2\). The maximum over its path edges converges after the same normalization to \(2\sqrt\alpha\): a union bound on \(m_n\) variance-two Gaussian increments proves the upper half and \(\lfloor(m_n+1)/2\rfloor\) disjoint edges prove the lower half. Therefore
\[
\frac{M_{\mathrm{broom}}}{\sqrt{\log n}}\xrightarrow{\mathbb P}
\max\{\sqrt2,2\sqrt\alpha\}=2\sqrt\alpha.
\]
To pass from convergence in probability to convergence of means, use the uniform tail estimate
\[
\Pr(M_T>t)\le2(n-1)e^{-t^2/4}.
\]
Integrating it above \(2\sqrt{\log(2n)}\) gives the uniform second-moment bound \(\mathbb E M_T^2\le4\log(2n)+4\). Thus \(M_T/\sqrt{\log n}\) is uniformly integrable and \(\mathbb EM_{\mathrm{broom}}\sim2\sqrt\alpha\sqrt{\log n}\). The scaled width tends to \(4\sqrt\alpha\). For \(\alpha=1\) take paths. Since \(4\sqrt\alpha\) runs over the entire interval \([2\sqrt2,4]\), the classification is complete.

## Verification
The supplied standalone `CHECK.py` uses only Python's standard library. It enumerates all Prüfer codes for labeled trees on 3 through 6 vertices (1,440 cases) and exactly checks the Gram determinant \(n\), tests the support function against the signed-edge vertex list, and makes reproducible finite Gaussian-sampling comparisons for stars, brooms, and paths. The program exits with `PASS` if every assertion holds. The universal and limit assertions follow from the preceding analytical steps, **not** from these finite samples.

## Relationship to prior work
D'Alì, Delucchi, and Michałek [1, Example 2.3] state the tree-to-crosspolytope lattice equivalence and study combinatorial, metric-space, and Ehrhart links. D'Alì, Juhnke-Kubitzke, and Koch [2, Theorem 4.6] establish graphical-matroid control of lattice unimodular equivalence more generally. Kabluchko, Litvak, and Zaporozhets [3, Sections 1–2] give the Gaussian characterization of Euclidean mean width and classical Gaussian-maximal estimates. Those results furnish the *setup and proof tools* here, not the sharp tree-family limit-set classification.

A graphical zonotope of a tree is a **Minkowski sum** of edge segments, so its directional support uses a sum of absolute edge increments; in contrast \(P_T\) is their **convex hull**, whose support is a maximum. Published invariance of tree-zonotope mean widths cannot be transferred to the convex-hull problem by identifying the two bodies.

## Limitations
The theorem classifies leading-order asymptotic mean-width constants, not exact finite-dimension minimizers, second-order corrections, or complete angular normal-cone spectra. It concerns unweighted trees in their canonical type-A root realization only. The reviewed bibliography did not identify an equivalent sharp interval theorem, but an earlier result using Gaussian-increment or graph-indexed-process terminology remains a possible overlap. The finite checker is independent supporting computation, not an all-dimensional proof and not independent human mathematical validation.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), especially Section 2.1 and Example 2.3. https://arxiv.org/abs/1910.05193
2. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a Generalization of Symmetric Edge Polytopes to Regular Matroids*, arXiv:2307.04933v1 (first public 2023-07-10), especially Theorem 4.6. https://arxiv.org/abs/2307.04933
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479 (first public 2015-11-26), Sections 1–2. https://arxiv.org/abs/1511.08479
