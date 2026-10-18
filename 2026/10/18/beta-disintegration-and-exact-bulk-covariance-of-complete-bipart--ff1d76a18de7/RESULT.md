# Beta disintegration and exact bulk covariance of complete-bipartite Lipschitz dual balls

## Finding

For integers \(p,q\ge2\), let \(K_{p,q}\) have unit cross edges and its shortest-path metric. Its real Lipschitz dual unit ball, in the quotient of vertex potentials by constants, is the \(d=p+q-1\)-dimensional body
\[
Q_{p,q}=\{(x,y):x_1=0,\ |x_i-y_j|\le1\ (1\le i\le p,\ 1\le j\le q)\}.
\]
Let \(X=(x,y)\) be uniformly distributed in \(Q_{p,q}\). The first assertion is an exact probability disintegration, not merely a formula for volume. Put \(N=p+q\); independently draw

* \(S\sim\operatorname{Beta}(p-1,q+1)\);
* a uniformly random permutation \((T_1,\ldots,T_p)\) of \((0,1,U_1,\ldots,U_{p-2})\), where the \(U_i\) are independent uniform variables on \([0,1]\);
* independent \(V_1,\ldots,V_q\sim\operatorname{Uniform}[-1,1]\).

Then the complete law of \(X\), with the vertex indexing fixed, is
\[
\boxed{x_i=2S(T_i-T_1),\qquad y_j=2S(\tfrac12-T_1)+(1-S)V_j.}
\]
In particular, the range of the first bipartition class has the exact law
\[
\boxed{\frac12(\max_i x_i-\min_i x_i)\sim\operatorname{Beta}(p-1,q+1).}
\]

Let \(H=\{z\in\mathbb R^N:\sum_i z_i=0\}\), with its inherited Euclidean metric. Let \(Z=X-N^{-1}(\sum_i X_i)\mathbf1_N\in H\). Write \(P_A,P_B,P_C\) for the orthogonal projections in \(H\) onto the zero-sum vectors supported on the first part, zero-sum vectors supported on the second part, and the one-dimensional subspace of vectors constant on each part, respectively. Then the **entire** uniform-interior covariance operator is
\[
\boxed{\operatorname{Cov}(Z)=\frac{(p+1)(p+2)P_A+(q+1)(q+2)P_B+(pq+2)P_C}{3N(N+1)}.}
\]
Thus it has exactly the three displayed eigenvalues, with multiplicities \(p-1,q-1,1\), respectively; some numerical eigenvalues may coincide. In the invariant Euclidean coordinates the intrinsic volume and the affine-invariant isotropic constant are
\[
\operatorname{vol}_{d}(Q_{p,q})=\frac{2^d p!q!}{d!\sqrt N},
\]
\[
\boxed{L(Q_{p,q})=
\frac{\bigl([(p+1)(p+2)]^{p-1}[(q+1)(q+2)]^{q-1}(pq+2)\bigr)^{1/(2d)}}{\sqrt{3N(N+1)}}
\left(\frac{d!\sqrt N}{2^d p!q!}\right)^{1/d}.}
\]
The volume identity is included to fix normalization and is not asserted as a new evaluation. Uniformly over all integer splits \(p,q\ge2\) with \(N\to\infty\),
\[
\boxed{L(Q_{p,q})=\frac1{\sqrt{12}}\left(1+O\left(\frac{\log N}{N}\right)\right).}
\]

There is also a non-Gaussian-to-Gaussian joint limit, for every fixed \(p\ge3\) and \(q\to\infty\). With \(G\sim\operatorname{Gamma}(p-1,1)\) and \(W\sim N(0,1/3)\), independent of each other and of the uniform ordered \(T\) above,
\[
\boxed{\bigl(qx_2,\ldots,qx_p,\ \sqrt q\,q^{-1}\sum_{j=1}^{q}y_j\bigr)
\ \xrightarrow{\ d\ }
\bigl(2G(T_2-T_1),\ldots,2G(T_p-T_1),W\bigr).}
\]
The same limit implies \(q(\max_i x_i-\min_i x_i)/2\Rightarrow G\). The cross-part mean fluctuation is independent of the Gamma–order-statistic limit. These claims concern the Lipschitz **dual** ball, not the primal transportation-cost ball.

## Assumptions and scope

The underlying metric is the shortest-path metric of the unit-edge graph \(K_{p,q}\): opposite-part distances are \(1\), and distinct same-part distances are \(2\). The dual of the finite-dimensional real Lipschitz-free space is the vector space of real potentials modulo constants with norm \(\max_{i,j}|x_i-y_j|\). Anchoring \(x_1=0\) fixes one representative. All draws called uniform use Lebesgue measure in these \(d\) anchored coordinates, equivalently normalized Euclidean volume after orthogonal projection into \(H\); the two volume measures differ by a fixed Jacobian and induce the same probability distribution. The boundary of the polytope has measure zero. All covariance assertions use Euclidean geometry on \(H\); no arbitrary basis-dependent covariance is being silently substituted.

Define \(a=\mathbf1_p\oplus0_q\) and \(b=0_p\oplus\mathbf1_q\). In \(\mathbb R^N\), the projections are
\[
P_A=\operatorname{diag}(I_p-\tfrac1p\mathbf1_p\mathbf1_p^{\mathsf T},0_q),\qquad
P_B=\operatorname{diag}(0_p,I_q-\tfrac1q\mathbf1_q\mathbf1_q^{\mathsf T}),
\]
\[
P_C=I_N-\frac{\mathbf1_N\mathbf1_N^{\mathsf T}}N-P_A-P_B.
\]
Their mutually orthogonal ranges sum to \(H\). For a full-dimensional centrally symmetric convex body \(K\subset H\), we use \(L(K)=\det_H(\operatorname{Cov}(U_K))^{1/(2d)}/\operatorname{vol}_d(K)^{1/d}\), where \(U_K\) is uniform in \(K\). The Gamma convention is the density \(g^{p-2}e^{-g}/\Gamma(p-1)\) for positive \(g\).

## Proof

**1. Exact range disintegration and independent draws.** Fix \(x_1=0\). Given the first-part coordinates \((x_1,\ldots,x_p)\), write \(A=\min_i x_i\), \(B=\max_i x_i\), \(R=B-A\). The inequalities on all cross edges say, independently for each second-part coordinate,
\[
B-1\le y_j\le A+1.
\]
This interval has length \(2-R\); feasibility requires \(0\le R\le2\). Hence the anchored-coordinate volume element after integrating the second part is \((2-R)^q\,dx_2\cdots dx_p\).

Outside the measure-zero set of tied extrema, choose the indices of \(A,B\) in \(p(p-1)\) ways. Represent all first-part coordinates as \(x_i=A+RT_i\), with the indexed \(T\) containing the endpoints \(0,1\) and \(p-2\) independent variables in \((0,1)\). The anchor forces \(A=-RT_1\). The Jacobian for \((x_2,\ldots,x_p)\mapsto(R,U_1,\ldots,U_{p-2})\) has absolute value \(R^{p-2}\): this follows by subtracting the anchored coordinate from the other coordinates and using the two extreme equations, followed by factoring \(R\) from each interior column. This also holds when the anchor is either extreme. Summing over the \(p(p-1)\) extremal index choices gives
\[
\operatorname{vol}_{\rm anchor}(Q_{p,q})
=p(p-1)\int_0^2 r^{p-2}(2-r)^q\,dr
=\frac{2^d p!q!}{d!}.
\]
In the final equality set \(s=r/2\), and use the beta integral \(B(p-1,q+1)=\Gamma(p-1)\Gamma(q+1)/\Gamma(N)\). This factorization says simultaneously that \(S=R/2\) has the claimed beta law, that the extrema locations and interior \(U_i\) have the specified distribution independently of \(S\), and that each \(y_j\) is an independent uniform draw from \([B-1,A+1]\) conditional on \(x\). Substituting its center \((A+B)/2=2S(\tfrac12-T_1)\) and radius \((2-R)/2=1-S\) gives the displayed exact sampling law. No asymptotic approximation has entered.

**2. Exact second moments and the three invariant sectors.** The centered random vector \(Z\) has mean zero by the inversion symmetry \((x,y)\mapsto(-x,-y)\). The law is invariant under \(S_p\times S_q\) once interpreted in \(H\). Therefore its covariance is scalar on the two zero-sum part subspaces and on their orthogonal one-dimensional contrast subspace, with no mixed blocks. To evaluate the scalars, beta moments from part 1 give
\[
\mathbb E S^2=\frac{p(p-1)}{N(N+1)},\qquad
\mathbb E(1-S)^2=\frac{(q+1)(q+2)}{N(N+1)}.
\]
The symmetric endpoint-plus-interior sample \(T\) satisfies
\[
\mathbb E\sum_{i=1}^p(T_i-\bar T)^2=\frac{(p+1)(p+2)}{12p},\qquad
\mathbb E(\bar T-\tfrac12)^2=\frac{p-2}{12p^2}.
\]
Both are elementary consequences of \(\sum_i T_i=1+\sum_{i=1}^{p-2}U_i\), \(\mathbb E U_i=1/2\), \(\operatorname{Var}(U_i)=1/12\), and \(\mathbb E U_i^2=1/3\).

Since \(x_i-\bar x=2S(T_i-\bar T)\), the covariance eigenvalue on the first part is the expected squared projected norm divided by its dimension \(p-1\):
\[
\lambda_A=\frac{4\mathbb E S^2}{p-1}\,\mathbb E\sum_i(T_i-\bar T)^2
=\frac{(p+1)(p+2)}{3N(N+1)}.
\]
Likewise \(y_j-\bar y=(1-S)(V_j-\bar V)\), so the second-part eigenvalue is
\[
\lambda_B=\frac13\mathbb E(1-S)^2=\frac{(q+1)(q+2)}{3N(N+1)}.
\]
Here the variance eigenvalue of the zero-sum projection of \(q\) independent centered variance-\(1/3\) variables is \(1/3\).

The difference between the two part means is
\[
h=\bar x-\bar y=2S(\bar T-\tfrac12)-(1-S)\bar V.
\]
Its variance, using independence and \(\operatorname{Var}(\bar V)=1/(3q)\), simplifies exactly to
\[
\operatorname{Var}(h)=\frac{1+2/(pq)}{3(N+1)}.
\]
On \(H\), the squared norm of the contrast vector with mean gap \(h\) is \((pq/N)h^2\); consequently
\[
\lambda_C=\frac{pq}N\operatorname{Var}(h)=\frac{pq+2}{3N(N+1)}.
\]
The three projections are mutually orthogonal and span \(H\), proving the covariance formula. The above calculations are exact for all integer \(p,q\ge2\).

**3. Volume normalization and isotropic constant.** The map from the \(d\) anchored coordinate basis to the zero-sum Euclidean hyperplane \(H\) has Gram matrix \(I_d-N^{-1}\mathbf1_d\mathbf1_d^{\mathsf T}\), whose determinant is \(1/N\). Hence intrinsic \(d\)-dimensional volume is anchored-coordinate volume divided by \(\sqrt N\). The product of the positive covariance eigenvalues is \(\lambda_A^{p-1}\lambda_B^{q-1}\lambda_C\). Substituting the preceding formulas into the definition of \(L\) proves its exact displayed expression.

For uniform asymptotics, write \(d=N-1\) and use \(\log(m!)=m\log m-m+O(\log(m+1))\), with the absolute implicit constant valid for all positive integers \(m\). As \(2\le p,q\le N-2\), the logarithm of the geometric mean of covariance eigenvalues is
\[
\frac{(p-1)\log\lambda_A+(q-1)\log\lambda_B+\log\lambda_C}{2d}
=\frac{p\log p+q\log q}{N}-\log N-\tfrac12\log3
+O\left(\frac{\log N}{N}\right),
\]
uniformly over the split. The logarithm of the inverse volume radius satisfies
\[
-\frac1d\log\operatorname{vol}_d(Q_{p,q})
=\log N-\frac{p\log p+q\log q}{N}-\log2
+O\left(\frac{\log N}{N}\right),
\]
also uniformly. Their sum is \(-\log(2\sqrt3)+O((\log N)/N)\), and exponentiation proves the claimed \(1/\sqrt{12}\) limit with its uniform error.

**4. Fixed-first-part Gamma–Gaussian limit.** When \(p\ge3\) is fixed and \(q\to\infty\), the beta–gamma representation \(S=G_1/(G_1+G_2)\), with independent \(G_1\sim\operatorname{Gamma}(p-1,1)\) and \(G_2\sim\operatorname{Gamma}(q+1,1)\), shows \(qS\Rightarrow G_1\): divide \(G_2\) by \(q\) and apply the law of large numbers. Independently, \(\sqrt q\,\bar V\Rightarrow N(0,1/3)\) by the classical central limit theorem. Both limits are independent of \(T\), and their joint independence follows already from the exact product construction. For fixed \(p\), \(T_1\) is bounded and \(\sqrt q S\to0\) in probability; likewise \(1-S\to1\). Substituting in the exact equations for \(x_i,y_j\) and applying Slutsky's theorem gives the joint vector limit. The range limit follows directly from \(R/2=S\). No finite-dimensional computation is being used as a substitute for these probability limits.

## Verification

The accompanying `verify_bipartite_covariance.py` enumerates the known extreme Lipschitz potentials of the dual polytope, obtains its boundary triangulation from the actual convex hull, forms cones over those simplices, and independently integrates all pairwise second moments of the zero-sum ambient coordinates. Simplex determinants, volume integrals and the complete covariance comparison are all computed with exact integers and `fractions.Fraction`; only the *choice of boundary triangulation* uses floating-point Qhull. Exact determinants eliminate any degenerate simplices. In eight cases \((p,q)=(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(3,4),(4,3)\), the exact reconstructed volumes and every covariance matrix entry agree identically with the theorem. Run `python verify_bipartite_covariance.py` with Python 3 and SciPy installed. Successful output ends with `EXACT_BIPARTITE_BULK_MOMENTS_PASS 8 cases`.

The test's extreme points are the two families of anchored integer potentials in which either all first-part values are constant and each second-part value is an independent sign, or vice versa, with the two constant configurations deduplicated. These are the complete vertices by the connected-tight-edge criterion (or Proposition 3.4 in [1]). As a separate consistency check, substituting \(p=q=2\) gives first- and second-part covariance eigenvalues \(1/5\) and contrast eigenvalue \(1/10\); substituting \(p=q=3\) gives eigenvalues \(10/63,10/63,11/126\). The finite tests certify these exact cases, while the beta disintegration and moment calculations prove every dimension and the asymptotics.

## Relationship to prior work

Higashitani, Jochemko and Michałek [1] completely classify the facets of symmetric edge polytopes and evaluate complete-bipartite Ehrhart data, including their normalized volumes. Those results supply a geometric starting point and the vertex classification but do not evaluate the uniform interior law, its covariance, or an isotropic constant. Alexander, Fradelizi, García-Lirola and Zvavitch [2] identify the Lipschitz-free unit ball with the symmetric edge polytope of a graph and analyze Mahler products and Hanner cases; the explicit bulk second moments and Gamma–Gaussian limit here are different quantities. D'Alì, Delucchi and Michałek [3] treat symmetric-edge facets and face geometry without the uniform interior covariance evaluation.

The published complete-bipartite Hilbert-distance result [4] optimizes a permutation-invariant quadratic form over **vertices** of the dual Lipschitz polytope. Its vertex quadratic form and Banach–Mazur distance are not probabilistic interior second moments and imply neither the three covariance eigenvalues nor the independent Gamma–Gaussian limit. Published book-graph computations with a two-vertex first part do not determine the general \(p\ge3\) exact distribution. A published integer-height-function range law [5] applies to a discrete model, whereas the beta range here has an absolutely continuous law. Generic cube-section/Beta integral formulas alone do not evaluate the stated covariance or its uniform asymptotics. An unindexed equivalent continuous-volume identity cannot be categorically excluded.

## Limitations

The body is the **dual** Lipschitz ball, not the symmetric-edge primal ball; the two have different interior moments. All formulas assume unit cross edges on a complete bipartite graph, real scalars, and \(p,q\ge2\). The fixed-part Gamma–Gaussian result requires a fixed \(p\ge3\) and growing \(q\); it does not describe arbitrary weighted graphs or nonlinear observables beyond the variables stated. The complete covariance is a second-moment statement, not a claim of Gaussianity in finite dimension or conditional independence from sparse precision matrices. Exact polynomial or integral formulas that indirectly imply particular moments might exist in older, differently named literature. The independent scientific audit and independent bibliographic verification remain unperformed.

## References

[1] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first public 2018-07-20), especially Proposition 3.4 and Section 4, https://arxiv.org/abs/1807.07678.

[2] M. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11-24), https://arxiv.org/abs/1911.10642.

[3] A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public 2019-10-11), https://arxiv.org/abs/1910.05193.

[4] *Maximal Hilbert distortion for complete-bipartite transportation spaces*, public mathematical record 203c5ca21810 (full proof analyzed; a result on vertexwise quadratic optimization, not uniform interior covariance).

[5] *Exact range laws for integer height functions on complete bipartite graphs*, public mathematical record c645403cd639 (integer-valued discrete heights, not continuous volume-uniform potentials).
