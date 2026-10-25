# Strict isotropic-constant interpolation in complete split-graph stable-set polytopes

## Finding

Let \(N\ge2\), let \(0\le p\le N-1\), and put \(q=N-p\ge1\). Let \(G_{p,q}=K_p\vee\overline K_q\): a clique of size \(p\) joined to each vertex of an independent set of size \(q\). The standard stable-set polytope \(P_{p,q}\subset\mathbb R^N\) has the following exact affine-invariant isotropic constant:

\[
L(P_{p,q})^{2N}
=\frac{(N!/q!)^2(q+1)^{q+1}(q+2)^q}
{12^q(N+1)^{N+1}(N+2)^N}.
\]

At fixed \(N\), the values increase **strictly** as one independent vertex is promoted to the clique, namely
\[
L(P_{0,N})<L(P_{1,N-1})<\cdots<L(P_{N-1,1}).
\]
The endpoints are the \(N\)-cube and the \(N\)-simplex. Thus this specific nested sequence has a strict isotropic-constant monotonicity law, although such monotonicity does not hold for arbitrary convex-body inclusions.

Moreover, uniformly across all choices \(0\le p<N\),
\[
\log L(P_{p,q})=-\frac pN-\frac{q}{2N}\log12
+O\!\left(\frac{\log(N+2)}N\right).
\]
Consequently, if \(p/N\to\alpha\in[0,1]\),
\[
L(P_{p,q})\longrightarrow
\frac{e^{-\alpha}}{12^{(1-\alpha)/2}}.
\]
This limiting function increases strictly from \(1/\sqrt{12}\) to \(1/e\).

## Assumptions and scope

The graph join \(K_p\vee\overline K_q\) has all clique edges and all edges between the two parts, and no edges within the independent part. The empty clique \(K_0\) is allowed. Write the coordinates of \(\mathbb R^N\) as \((x_1,\ldots,x_p,y_1,\ldots,y_q)\). By the stable-set indicator-vector definition,
\[
P_{p,q}=
\left\{(x,y):x_i\ge0,\ y_j\ge0,\ \sum_{i=1}^p x_i+y_j\le1
\ \text{for every }1\le j\le q\right\}.
\]
The Euclidean volume is measured in the displayed coordinate embedding. Let \(Z\) be uniformly distributed according to normalized volume on \(P_{p,q}\), let \(\Sigma_{p,q}=\operatorname{Cov}(Z)\), and define the affine-invariant isotropic constant by
\[
L(P_{p,q})=
\frac{(\det\Sigma_{p,q})^{1/(2N)}}
{\operatorname{Vol}_N(P_{p,q})^{1/N}}.
\]
The polytope is full-dimensional for every parameter in the theorem. No claim is made for more general split graphs, arbitrary graph joins, or other probability measures on the vertices.

## Proof

**1. Exact set and volume.** A stable set either consists of one clique vertex or is an arbitrary subset of the independent vertices. If \(t=\sum_i x_i\), every feasible point can be written as a convex combination of the clique singleton vectors with coefficients \(x_i\) and the independent-cube point \((0,y/(1-t))\) with coefficient \(1-t\). The case \(t=1\) forces \(y=0\), and the cases \(p=0\) or \(t=0\) are immediate. Thus the inequality description above is exact, not merely a relaxation.

For \(p\ge1\), the simplex slice \(x\ge0,\sum x_i=t\) has coarea density \(t^{p-1}/(p-1)!\) relative to \(dt\). Each independent coordinate ranges over \([0,1-t]\). Direct integration gives
\[
\operatorname{Vol}_N(P_{p,q})
=\frac1{(p-1)!}\int_0^1t^{p-1}(1-t)^q\,dt
=\frac{q!}{N!}.
\]
For \(p=0\), this also holds because \(P_{0,N}=[0,1]^N\).

**2. An exact covariance-killing shear.** Suppose first that \(p\ge1\). For a uniform point \((X,Y)\in P_{p,q}\), put \(T=\sum_{i=1}^pX_i\). The preceding slice formula implies
\[
T\sim\operatorname{Beta}(p,q+1).
\]
Conditional on \(T=t\), the normalized clique coordinates are uniformly distributed on the simplex of sum one, and the \(q\) independent coordinates \(Y_j\) are conditionally independent uniforms on \([0,1-t]\), independent of those normalized clique coordinates.

Set \(W_j=Y_j+T/2\). Then \(\mathbb E[W_j\mid X]=1/2\); conditional on \(X\), the centered variables \(W_j-1/2\) are independent with variance \((1-T)^2/12\). Hence each \(W_j\) is uncorrelated with every clique coordinate, the \(W_j\)'s are pairwise uncorrelated, and
\[
\operatorname{Var}(W_j)=
\frac{\mathbb E(1-T)^2}{12}
=\frac{(q+1)(q+2)}{12(N+1)(N+2)}=:\lambda.
\]
The shear \((X,Y)\mapsto(X,W)\) has determinant one, so it leaves the determinant of the covariance matrix unchanged. Direct beta/Dirichlet moments give
\[
\operatorname{Cov}(X)=
\frac{I_p}{(N+1)(N+2)}
-\frac{\mathbf1_p\mathbf1_p^{\mathsf T}}{(N+1)^2(N+2)}.
\]
This has the eigenvalue \(1/((N+1)(N+2))\) with multiplicity \(p-1\) and the eigenvalue \((q+1)/((N+1)^2(N+2))\) on the span of \(\mathbf1_p\). Therefore
\[
\det\Sigma_{p,q}
=\frac{q+1}{(N+1)^{p+1}(N+2)^p}\lambda^q
=\frac{(q+1)^{q+1}(q+2)^q}
{12^q(N+1)^{N+1}(N+2)^N}.
\]
For \(p=0\) the point is uniform on the cube and the same determinant formula reduces to \(12^{-N}\). Dividing by the square of the volume establishes the claimed isotropic-constant formula.

For completeness, the original, unsheared covariance block entries, for \(p\ge1\), are exactly
\[
\begin{aligned}
\operatorname{Cov}(X_i,X_k)&=\frac{\mathbf1_{i=k}}{(N+1)(N+2)}-\frac1{(N+1)^2(N+2)},\\
\operatorname{Cov}(X_i,Y_j)&=-\frac{q+1}{2(N+1)^2(N+2)},\\
\operatorname{Cov}(Y_j,Y_k)&=\lambda\mathbf1_{j=k}
+\frac{p(q+1)}{4(N+1)^2(N+2)}.
\end{aligned}
\]
These formulas specify actual Euclidean inertia. The sheared eigenvalues above are not asserted to be Euclidean eigenvalues of the original covariance.

**3. Strict finite-dimensional ordering.** At fixed \(N\), let \(B_N(q)=L(P_{N-q,q})^{2N}\). Cancellation in the exact formula gives, whenever \(q\ge1\),
\[
\frac{B_N(q+1)}{B_N(q)}
=\frac{(q+2)^2}{12(q+1)^2}
\left(\frac{q+3}{q+1}\right)^{q+1},
\]
provided \(q+1\le N\). Write \(s=q+1\ge2\). The ratio is
\[
\frac1{12}\left(1+\frac1s\right)^2
\left(1+\frac2s\right)^s.
\]
For \(s=2\) it equals \(3/4\), and for \(s=3\) it equals \(500/729\). For all integers \(s\ge4\), use \((1+1/s)^2\le25/16\) and \((1+2/s)^s<e^2<(11/4)^2=121/16\), whose product is less than \(12\). Thus the ratio is always strictly less than one, proving the entire chain. Promoting one independent vertex to the clique adds graph edges and strictly shrinks the stable-set polytope, so this is a monotonicity result along genuine convex-body inclusions.

**4. Uniform asymptotic interpolation.** Uniform Stirling estimates \(\log(k!)=k\log k-k+O(\log(k+2))\), with the convention \(0\log0=0\), applied to the exact formula yield
\[
\log L(P_{p,q})^{2N}=-2p-q\log12+O(\log(N+2)).
\]
The bound is uniform for \(1\le q\le N\), even if one part remains bounded. Division by \(2N\) proves the stated uniform estimate and limiting law. Since \(\tfrac12\log12-1>0\), the limit grows strictly with \(\alpha\).

## Verification

The accompanying standalone script `check_split_isotropy.py` independently obtains finite-dimensional covariances by rational beta/Dirichlet moments, checks the determinant and shear identities, computes Euclidean volumes from convex hulls of the actual stable-set vertices, and tests a broad finite range of the consecutive-ratio formula. Its output was:

`VERIFY_OK exact_covariance_determinants=29 convex_hull_volumes=15 strict_ratio_cases=498`

These computations verify finite instances and arithmetic; the universal monotonicity and asymptotic claims are established analytically above, not by finite testing.

## Relationship to prior work

Aliniaeifard, Benedetti, Bergeron, Li, and Saliola introduced a general geometric study of stable-set-polytope one-skeleta (first public version 2018-04-02). The present family is an elementary but infinite subfamily of their stable-set-polytope framework. Their edge and diameter results do not supply the volume-normalized covariance determinant or a monotonicity classification. The known perfect-graph clique-facet description gives the inequalities here but also does not determine inertia.

The paper of Kohl, Olsen, and Sanyal on unconditional reflexive polytopes concerns different signed/unconditional polytope constructions. Published results on isotropic constants of Hanner polytopes concern centrally symmetric Hanner bodies, whereas the nontrivial complete split-graph stable-set bodies here are not Hanner polytopes. The affine-invariant statistic computed here is different from Euclidean inradius, John ellipsoid, combinatorial diameter, and vertex-uniform inertia.

## Limitations

The theorem applies only to complete split graphs and to the continuous uniform volume distribution. It does not classify isotropic constants for arbitrary split graphs, nor does it assert monotonicity for arbitrary graph-edge additions. The finite checker is not a proof of the all-dimension results. A bibliographic search can miss equivalent identities expressed through simplex–cube pyramids, beta slices, or general join formulas; an independent audit has not been carried out.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first posted 2018-04-02), https://arxiv.org/abs/1804.00360 .
2. *On the linear extension complexity of stable set polytopes for perfect graphs*, European Journal of Combinatorics 80 (2019), 247–260, DOI:10.1016/j.ejc.2018.02.014 .
3. F. Kohl, M. Olsen, and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry 64 (2020), 427–452, DOI:10.1007/s00454-020-00199-8 .
4. R. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23 (background for chain-polytope interpretations).
