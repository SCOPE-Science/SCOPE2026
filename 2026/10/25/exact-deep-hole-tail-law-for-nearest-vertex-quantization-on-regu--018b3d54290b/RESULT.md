# Exact deep-hole tail law for nearest-vertex quantization on regular simplices

## Finding
Let \(S\) be a regular Euclidean \(d\)-simplex of side length \(1\), \(d\ge2\), and let \(X\) be uniformly distributed in its full-dimensional interior. Let \(v_1,\ldots,v_m\) denote the vertices, with \(m=d+1\), and set
\[
D(X)=\min_{1\le i\le m}\|X-v_i\|,\qquad R^2=\frac{d}{2m},\qquad \Delta=R^2-D(X)^2.
\]
The maximum of \(D\) on \(S\) equals \(R\) and is attained **only at the centroid**.

For \(0<\varepsilon<1/[2m(m-1)]\), write \(P=(P_1,\ldots,P_d)\sim\operatorname{Dirichlet}(1,\ldots,1)\) and
\[
Q=m^2\sum_{j=1}^d P_j^2-m.
\]
Then the **exact endpoint distribution** is
\[
\boxed{\mathbb P(\Delta<\varepsilon)=m^d\,\mathbb E\left[\left(\frac{2\varepsilon}{1+\sqrt{1-2\varepsilon Q}}\right)^d\right].}
\]
Moreover its complete absolutely convergent positive-coefficient expansion in this range is
\[
\boxed{\mathbb P(\Delta<\varepsilon)=(m\varepsilon)^d
\sum_{k=0}^\infty\frac{d}{d+2k}\binom{d+2k}{k}
\left(\frac{\varepsilon}{2}\right)^k\mathbb E[Q^k].}
\]
The first two corrections are explicitly
\[
\boxed{\mathbb P(\Delta<\varepsilon)=(m\varepsilon)^d\left[1+\frac{dm}{2}\varepsilon+
\frac{d(d+3)m^2(m^2+7m-6)}{8(m+1)(m+2)}\varepsilon^2+O_d(\varepsilon^3)\right].}
\]
For example, for a regular tetrahedron \(d=3\) the bracket equals \(1+6\varepsilon+\tfrac{228}{5}\varepsilon^2+O(\varepsilon^3)\), and the leading factor is \(64\varepsilon^3\).

If \(X_1,\ldots,X_N\) are independent uniform samples from \(S\), then for every \(x\ge0\)
\[
\boxed{\lim_{N\to\infty}\mathbb P\left(mN^{1/d}
\left[R^2-\max_{i\le N}D(X_i)^2\right]>x\right)=e^{-x^d}.}
\]
This gives the exact extreme-sample scale for the worst vertex-quantization errors.

## Assumptions and scope
All lengths are Euclidean, the simplex has side length \(1\), the point distribution is the normalized \(d\)-dimensional volume measure, and the sites are the fixed original vertices (not optimally repositioned centroids). The dimension \(d\ge2\) is arbitrary but fixed for the power series and its asymptotic remainder. Boundaries and Voronoi ties have zero volume and do not change the probability. The endpoint window is \(0<\varepsilon<1/[2(d+1)d]\). The random vector \(P\) in the formula has exactly \(d\) components, each with Dirichlet parameter \(1\).

## Proof
**1. Euclidean reduction and unique farthest point.** Write \(X=\sum_{i=1}^{m}\lambda_i v_i\), where \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\). Uniform volume makes \(\lambda\sim\operatorname{Dirichlet}(1,\ldots,1)\). For edge length \(1\), squared-distance identities give
\[
\|X-v_i\|^2=\frac{1+\sum_j\lambda_j^2}{2}-\lambda_i.
\]
Put \(z_i=\lambda_i-1/m\), \(T=\max_i z_i\), and \(H=\sum_i z_i^2\). Consequently
\[
\Delta=T-\frac12H.
\]
Since \(\sum_i\lambda_i^2\le\max_i\lambda_i\), we have \(H\le T\), hence \(\Delta\ge T/2\ge0\). Equality implies \(T=0\), so every \(\lambda_i=1/m\). This proves the unique deep hole.

**2. Homothetic cap and directional coordinates.** Define \(t_0=1/[m(m-1)]\). For \(0<t\le t_0\), the polytope \(\{\lambda: T\le t\}\) is a homothetic simplex of linear ratio \(mt\) inside the original simplex: specifically, \(\lambda_i=1/m+t-mt y_i\) with \(y_i\ge0\), \(\sum_i y_i=1\). Therefore
\[
\mathbb P(T\le t)=(mt)^d\qquad(0\le t\le t_0).
\]
Almost every radial ray of the boundary of this inner simplex belongs to one face \(y_i=0\). By permutation symmetry and the uniform-volume Jacobian, the \(d\) nonzero coordinates on that face, written \(P_j=y_j\), follow \(\operatorname{Dirichlet}(1,\ldots,1)\) independently of \(T\). This also follows by decomposing the homothetic cap into the \(m\) pyramidal cones joining its centroid to its \(m\) facets. On such a cone \(z_i=T\), \(z_j=T(1-mP_j)\), so
\[
H=Q T^2,\qquad Q=m^2\sum_{j=1}^{d}P_j^2-m.
\]
The shape variable lies in \(m/(m-1)\le Q\le m(m-1)\); in particular it is strictly positive.

**3. Exact inversion, including the domain boundary.** For fixed \(Q\), \(\Delta=T-QT^2/2\). This function is strictly increasing on \([0,t_0)\), since \(QT<1\) there. Outside the inner cap, \(T\ge t_0\) and \(\Delta\ge T/2\ge t_0/2\); hence for \(\varepsilon<t_0/2\) all contributing points lie strictly inside the cap. Within the cap the boundary condition \(\Delta=\varepsilon\) has the unique root
\[
T_\varepsilon(Q)=\frac{2\varepsilon}{1+\sqrt{1-2Q\varepsilon}}<t_0.
\]
Conditional radial integration of the \(d m^d T^{d-1}\) volume density proves \(\mathbb P(\Delta<\varepsilon)=m^d\mathbb E[T_\varepsilon(Q)^d]\).

**4. Convergent series and exact coefficients.** The identity \(T_\varepsilon=\varepsilon+(Q/2)T_\varepsilon^2\) and the Lagrange--Bürmann inversion formula give the coefficient of \(\varepsilon^{d+k}\) in \(T_\varepsilon^d\):
\[
\frac{d}{d+2k}\binom{d+2k}{k}\left(\frac Q2\right)^k.
\]
The bound \(2\varepsilon Q<1\) uniformly over the compact Dirichlet simplex ensures convergence; all coefficients are nonnegative. Dirichlet factorial moments make every coefficient rational. In particular,
\[
\mathbb E Q=m,\qquad \mathbb E Q^2=\frac{m^2(m^2+7m-6)}{(m+1)(m+2)}.
\]
Substitution yields the displayed first- and second-order correction terms. To calculate arbitrary rational coefficients without integration, expand \(Q^k\) using the multinomial theorem and
\[
\mathbb E\prod_{j=1}^{d}P_j^{a_j}
=\frac{(d-1)!\prod_j a_j!}{(d+\sum_j a_j-1)!}.
\]

**5. Independent-sample extremal limit.** Write \(F_d(\varepsilon)=\mathbb P(\Delta<\varepsilon)\); the leading term is \(F_d(\varepsilon)\sim m^d\varepsilon^d\). Thus for \(\varepsilon_N=x/[m N^{1/d}]\),
\[
\mathbb P\left(\min_{1\le i\le N}\Delta(X_i)>\varepsilon_N\right)
=(1-F_d(\varepsilon_N))^N\longrightarrow e^{-x^d}.
\]
This is the claimed Weibull-type law because \(\min_i\Delta(X_i)=R^2-\max_iD(X_i)^2\).

## Verification
The package includes a standalone Python reproducibility script `checker.py`. It tests the exact Dirichlet moment coefficients using rational arithmetic in dimensions \(1\) through \(14\), independently samples \(1{,}600{,}000\) uniform barycentric points per tested dimension and compares their geometric nearest-site deficits with the conditional exact distribution, and uses deterministic Simpson integration for the triangular-shape case. The checker passes. Those finite checks corroborate, but cannot replace, the all-dimensional proof above. Run with \(`python checker.py`\); the independent sampling tests require NumPy.

## Relationship to prior work
Conway and Sloane established classical second-moment and lattice-quantization formulas, including second moments of regular simplices. Their analysis does not supply the present near-worst-case distribution for fixed vertex sites. Geiß, Klein, Penninger and Rote established geometric transportation methods using weighted Voronoi regions; their full preprint sets a natural point-site and metric-geometry context, but its exact optimizing-partition theorem does not imply the tail law or its rational coefficients. Yurochkin, Guha, Sun and Nguyen analyze Dirichlet simplices and Voronoi partitions for statistical inference, not the near-deep-hole quantization distribution of the fixed simplex vertices. A separately indexed discrete Minkowski-vertex-average spectrum concerns discrete \(k\)-point averages, not continuous uniform points and their nearest vertex. These distinctions are about the mathematical objects and logical implications, not title similarity.

## Limitations
Only regular simplices and their original vertices are covered, with uniform interior sampling. No assertion is made about optimal quantizer sites, arbitrary distorted simplices, nonuniform densities, or complete distribution outside the stated endpoint interval. The finite checker cannot establish the infinite-dimensional statement by itself. The searches and full-text inspections do not constitute a definitive historical-priority certificate, and no independent mathematical audit has been performed.

## References
1. J. H. Conway and N. J. A. Sloane, *Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization*, IEEE Trans. Information Theory **28** (1982), 211–226. Author-hosted full text: https://neilsloane.com/doc/Me82.pdf.
2. D. Geiß, R. Klein, R. Penninger, G. Rote, *Optimally solving a transportation problem using Voronoi diagrams*, arXiv:1206.3057v1, first public version 2012-06-14, https://arxiv.org/abs/1206.3057.
3. M. Yurochkin, A. Guha, Y. Sun, X. Nguyen, *Dirichlet Simplex Nest and Geometric Inference*, Proceedings of ICML (2019), https://proceedings.mlr.press/v97/yurochkin19b.html.
