# Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes

## Finding

Fix an integer \(n\ge2\) and a set of ranks \(S\subseteq\{0,1,\ldots,n\}\), with at least two ranks and \(S\ne\{0,n\}\). The full-dimensional \(S\)-hypersimplex is
\[
P_{n,S}=\operatorname{conv}\{v\in\{0,1\}^{n}:\sum_i v_i\in S\}.
\]
The following finite algebraic procedure determines its **unique minimum-volume enclosing Euclidean ellipsoid**, its center, every squared principal semiaxis, its volume, and the exact ranks of all contact vertices. It uses at most \(|S|\) one-variable quadratic equations, irrespective of the number \(\sum_{j\in S}\binom nj\) of vertices.

Define the moment polygon
\[
\mathcal C_S=\operatorname{conv}\{(j,j^2):j\in S\},\qquad
q_\square=\left(\frac n2,\frac{n(n+1)}4\right).
\]
**Cube-ball case.** If \(q_\square\in\mathcal C_S\), the optimal ellipsoid is the Euclidean ball
\[
\boxed{\ \|x-\tfrac12\mathbf1\|_2^2\le\frac n4\ }.
\]
Every vertex of \(P_{n,S}\) is a contact, and all \(n\) squared semiaxes equal \(n/4\).

**Two-rank case.** If \(q_\square\notin\mathcal C_S\), form the candidate rank pairs consisting of the two extreme ranks and every consecutive pair in the sorted set \(S\). Discard the pair \((0,n)\) if it occurs, because the two corresponding layers alone do not span \(\mathbb R^n\).

For each remaining candidate \(a<b\), set
\[
A=a(n-a),\quad B=b(n-b),\quad \Delta=B-A.
\]
Let \(p\in(0,1)\) be the unique maximizer of
\[
p(1-p)(A+p\Delta)^{n-1},
\]
or equivalently the unique interior root of
\[
A+[n\Delta-2A]p-(n+1)\Delta p^2=0.
\]
When \(\Delta=0\), \(p=1/2\); when \(A=0<B\), \(p=n/(n+1)\); and when \(B=0<A\), \(p=1/(n+1)\). Define
\[
\mu=a+p(b-a),\quad V=p(1-p)(b-a)^2,\quad
T=(1-p)A+pB,\quad
D_{a,b}=V\left(\frac{T}{n-1}\right)^{n-1}.
\]
Choose the candidate pair maximizing \(D_{a,b}\). Then, writing \(H=\mathbf1\mathbf1^{\mathsf T}/n\), the unique Löwner ellipsoid has center and shape matrix
\[
\boxed{\quad c=\frac\mu n\mathbf1,\qquad
\Sigma=V H+\frac{T}{n-1}(I-H)\quad}.
\]
Here the ellipsoid is \(\{x:(x-c)^{\mathsf T}\Sigma^{-1}(x-c)\le1\}\). Its squared semiaxes are \(V\) once and \(T/(n-1)\) with multiplicity \(n-1\). **Exactly** the vertices of weights \(a\) and \(b\) contact this ellipsoid; every other allowed rank lies strictly inside.

In either case its volume is
\[
\operatorname{vol}_n(E)=\frac{\pi^{n/2}}{\Gamma(n/2+1)}\sqrt{\det\Sigma}.
\]
For the cube-ball case \(\det\Sigma=(n/4)^n\); otherwise \(\det\Sigma=D_{a,b}\).

Membership in the moment polygon has a direct exact test. Put \(x=n/2\), \(y=n(n+1)/4\), \(a=\min S\), \(b=\max S\). First require \(a\le x\le b\). Let \(u\) be the largest rank in \(S\) not exceeding \(x\), and \(v\) the smallest rank not less than \(x\). Then
\[
\boxed{\quad (u+v)x-uv\le y\le(a+b)x-ab\quad}
\]
is necessary and sufficient for the cube-ball case. Thus the entire calculation is finite and exact, using rational arithmetic and quadratic radicals.

**A nonextremal contact phenomenon.** With \(n=8\) and \(S=\{0,1,5\}\), the winning pair is \((1,5)\), not the extreme pair \((0,5)\). The rank-five weight is
\[
p=\frac{25+\sqrt{1129}}{72},\qquad
\mu=1+4p,\quad V=16p(1-p),\quad T=7+8p.
\]
Every rank-one and rank-five vertex contacts the ellipsoid, while the origin lies strictly inside: its covariance-normalized squared distance is
\[
\frac{\mu^2}{V}=\frac{617+19\sqrt{1129}}{168}<8.
\]
In contrast, filling in the missing ranks \(2,3,4\) restores the cube ball as the Löwner ellipsoid. Hence the gap pattern in \(S\), not just its extrema, can determine both anisotropy and the supporting layers.

## Assumptions and scope

All statements use the standard coordinate Euclidean metric of \(\mathbb R^n\). Each admitted binary vector is a vertex because it is already a vertex of the ambient cube. The exclusions \(|S|=1\) and \(S=\{0,n\}\) are necessary for full dimension; no intrinsic lower-dimensional ellipsoid is claimed. No symmetry assumption is made on competing ellipsoids. The formula covers every allowed nonconsecutive as well as consecutive set of ranks.

## Proof

**1. Minimum ellipsoids and covariance.** Let \(X\) be a finite full-dimensional point set in \(\mathbb R^n\). For a probability distribution \(\pi\) on \(X\), let \(m=\mathbb E_\pi X\) and \(C=\mathbb E_\pi[(X-m)(X-m)^{\mathsf T}]\). Choose \(\pi\) maximizing \(\det C\) (a positive maximum exists). Differentiating \(\log\det C\) when an infinitesimal mass is transferred to \(x\in X\) gives
\[
(x-m)^{\mathsf T}C^{-1}(x-m)-n\le0.
\]
Thus \(E=\{x:(x-m)^{\mathsf T}(nC)^{-1}(x-m)\le1\}\) contains \(X\). Conversely, if another ellipsoid with center \(c'\) and shape \(\Sigma'\) contains \(X\), averaging its squared defining inequality under \(\pi\) yields
\[
\operatorname{tr}((\Sigma')^{-1}C)
+(m-c')^{\mathsf T}(\Sigma')^{-1}(m-c')\le1.
\]
The arithmetic-geometric mean inequality for positive matrix eigenvalues gives \(\det\Sigma'\ge n^n\det C\), with equality at \(\Sigma=nC\). The constructed ellipsoid is therefore globally minimum-volume. Its uniqueness is the standard uniqueness theorem for the Löwner ellipsoid of a full-dimensional compact convex body.

**2. Reduction to two scalar moments.** Symmetrize a maximizing distribution over coordinate permutations. The covariance of a mixture is the average of the component covariances plus a positive-semidefinite between-means term. Together with concavity of \(\log\det\), this shows symmetrization cannot decrease \(\det C\). The resulting distribution is uniform within every allowed rank layer. Let \(J\in S\) denote its random rank, \(\mu=\mathbb E J\), and \(\nu=\mathbb E J^2\). The feasible moment pairs are exactly \(\mathcal C_S\). Set
\[
V=\nu-\mu^2,\qquad T=n\mu-\nu.
\]
For the rank-mixture random indicator \(X\), the covariance has eigenvalues \(V/n\) on \(\operatorname{span}(\mathbf1)\) and \(T/[n(n-1)]\) on its orthogonal complement. Consequently
\[
\det(nC)=V\left(\frac{T}{n-1}\right)^{n-1}.
\]
For a full-dimensional \(S\)-hypersimplex the optimum has \(V,T>0\).

**3. The sole interior stationary point.** On the positive domain of the moment polygon, maximize
\[
F(\mu,\nu)=\log(\nu-\mu^2)+(n-1)\log(n\mu-\nu).
\]
Its two partial derivatives vanish precisely when
\[
n\mu-\nu=(n-1)(\nu-\mu^2),\qquad n=2\mu.
\]
These imply \(\mu=n/2\), \(\nu=n(n+1)/4\), i.e. \(q_\square\). If this point is feasible, \(C=I/4\). This is a global maximum: for every random binary vector, \(C_{ii}=\operatorname{Var}(X_i)\le1/4\), so Hadamard's inequality gives \(\det C\le(1/4)^n\), attained here. Every binary vertex has squared distance \(n/4\) from \(\mathbf1/2\), giving all contacts.

**4. The boundary and candidate equations.** If \(q_\square\notin\mathcal C_S\), a maximum cannot be in the relative interior of the moment polygon (unless it is one-dimensional). The lower boundary of the convex hull of points on the strictly convex parabola \(\nu=\mu^2\) consists of the chords between consecutive allowed ranks, and the upper boundary is the chord joining the extreme ranks. A polygon vertex corresponds to deterministic rank and has \(V=0\), hence determinant zero. Therefore the maximum lies in the relative interior of one of precisely the listed boundary chords. For the chord from \(a\) to \(b\), assign probability \(1-p\) to rank \(a\), probability \(p\) to rank \(b\), and uniform probability conditional on each rank. This gives the stated \(\mu,V,T\). Its determinant is \(D_{a,b}\). The log-determinant is strictly concave in \(p\in(0,1)\) after dropping constant terms, so its unique maximizer solves the displayed quadratic. A pair \((0,n)\) has \(T=0\) and cannot maximize the positive determinant. Maximizing among the boundary candidates is therefore the global covariance determinant maximum; Step 1 supplies the ellipsoid and its full-dimensional optimality.

**5. Contacts and uniqueness of the active pair.** At a binary vertex of rank \(j\), its covariance-normalized squared distance is
\[
L(j)=\frac{(j-\mu)^2}{V}+\frac{(n-1)j(n-j)}{T}.
\]
The optimal-design derivative inequality gives \(L(j)\le n\) for all \(j\in S\), with equality at every rank given positive weight, namely \(a,b\). Since \(L(j)-n\) is quadratic in \(j\), any third equality rank would make it identically zero. Comparing its coefficients then forces the cube moments \(q_\square\), contrary to the current case. All other rank layers are strictly interior. A maximizing moment pair is unique: mixing two different rank-moment optima strictly increases the covariance determinant, by strict determinant concavity and the between-means covariance term. Thus the active boundary pair is unique, apart from duplicate listings of the same chord. The full minimum ellipsoid is unique independently of any symmetry imposed in the derivation.

**6. The exact cube test.** At fixed mean \(x\in[a,b]\), the maximum attainable second rank moment lies on the chord joining the extreme ranks and equals \((a+b)x-ab\). The minimum is the chord between the allowed ranks immediately below and above \(x\), and equals \((u+v)x-uv\). These bounds characterize the vertical section of \(\mathcal C_S\), proving the exact membership test.

The eight-dimensional example follows by inserting \(A=7\), \(B=15\) into the quadratic. The root is \((25+\sqrt{1129})/72\), and the strict interior inequality reduces to \(727>19\sqrt{1129}\), whose squared difference is \(120960>0\).

## Verification

The included `verify_rank_shell_ellipsoids.py` is a Python standard-library-only, finite numerical cross-check. Run `python3 verify_rank_shell_ellipsoids.py 11`. It enumerates every full-dimensional set \(S\) for \(2\le n\le11\), constructs the proposed moment-polygon optimizer, checks all allowed rank-orbit distances against the ellipsoid, checks equality at the chosen support ranks, and verifies the nonextremal contact example. In this range it passes \(8089\) cases and \(44957\) rank-layer distance inequalities representing \(5588288\) binary vertices. It does not enumerate each binary vector individually and uses floating-point arithmetic for quadratic roots; the exact theorem relies on the preceding analytic proof, not these tests.

## Relationship to prior work

Manecke, Sanyal, and So introduced and studied general \(S\)-hypersimplices, especially their faces, pulling triangulations, and monotone paths. Those combinatorial results establish the natural family but do not give the present optimal ellipsoid. Standard minimum-volume-ellipsoid / D-optimal-design duality supplies the variational principle, not the rank-moment polygon classification or its exact contact-rank consequences. Related consecutive-layer ellipsoid formulas do not determine nonconsecutive cases: for instance, adjoining the missing ranks to \(S=\{0,1,5\}\) changes its Löwner ellipsoid from the two-contact-rank anisotropic case to the cube ball. The result is restricted to the standard binary-coordinate realization rather than arbitrary affine deformations.

## Limitations

This theorem concerns minimum-volume enclosing ellipsoids, not John inscribed ellipsoids, and does not classify lower-dimensional singleton-rank hypersimplices. The finite verifier is numerical evidence only, and it does not constitute a formal proof or an independent audit. Literature comparisons cannot certify worldwide publication priority; related optimal-design formulations may exist under different terminology. The candidate equations are exact, but comparisons of algebraic determinants may require symbolic real-algebraic comparison for large parameters.

## References

1. S. Manecke, R. Sanyal, J. So, *S-hypersimplices, pulling triangulations, and monotone paths*, Electronic Journal of Combinatorics 27(3), P3.16 (2020), DOI 10.37236/8457; first preprint arXiv:1812.07491v1 (2018-12-18).
2. M. J. Todd, *Minimum-Volume Ellipsoids: Theory and Algorithms*, SIAM (2016), DOI 10.1137/1.9781611974386.
3. F. Gürtuna, *Duality of Ellipsoidal Approximations via Semi-Infinite Programming*, SIAM Journal on Optimization (2010), DOI 10.1137/080717973.
4. N. Gündüz and B. Torsney, *D-Optimal Designs for Binary and Weighted Linear Regression Models: One Design Variable*, Mathematics 11(9), 2075 (2023), DOI 10.3390/math11092075 (methodological comparison; different models).
