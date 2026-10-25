# Exact inertia spectrum and two-scale limits for two-level Lipschitz poset polytopes

## Finding
For integers \(p\ge2\), \(q\ge1\), put \(n=p+q\) and define the full-dimensional Lipschitz polytope of the ordinal sum of two antichains:
\[
L_{p,q}=\{(x,y)\in\mathbb R^p\times\mathbb R^q:\ 0\le x_i\le1,\quad 0\le y_j-x_i\le1\quad\text{for every }i,j\}.
\]
Let \((X,Y)\) be uniform in \(L_{p,q}\) with respect to ordinary \(n\)-dimensional Euclidean volume. Set \(R=\max_iX_i-\min_iX_i\), and introduce
\[
s=\frac{(q+2)(q+3)}{(n+1)(n+2)},\qquad
 t=\frac{p(p-1)}{(n+1)(n+2)}.
\]
**Exact finite-dimensional law.** One has
\[
\operatorname{vol}_n(L_{p,q})=\frac{p!\,(q+1)!}{n!},\qquad R\sim\operatorname{Beta}(p-1,q+2).
\]
The coordinate means are \(\mathbb EX_i=1/2\) and \(\mathbb EY_j=1\). The entire covariance spectrum is:

* \(\lambda_X=(p+1)(p+2)/[12(n+1)(n+2)]\), repeated \(p-1\) times;
* \(\lambda_Y=s/12\), repeated \(q-1\) times;
* the two eigenvalues of the symmetric matrix
\[
M_{p,q}=\frac1{12}\begin{pmatrix}
 ps+(p-2)t/p & \sqrt{pq}\,s\\
 \sqrt{pq}\,s & (q+1)s
\end{pmatrix}.
\]
In particular,
\[
\det\operatorname{Cov}(X,Y)=\lambda_X^{p-1}\lambda_Y^{q-1}
\frac{p s^2+(q+1)(p-2)st/p}{144}.
\]
All formulas include \(q=1\), when the upper contrast multiplicity is zero.

**Two-scale asymptotic geometry.** If \(p,q\to\infty\) and \(p/(p+q)\to\alpha\in(0,1)\), write \(\beta=1-\alpha\), \(\bar X=p^{-1}\sum_iX_i\), \(\bar Y=q^{-1}\sum_jY_j\). Then
\[
\left(\bar X-\tfrac12,\ \sqrt n(\bar Y-\bar X-\tfrac12)\right)
\ \Longrightarrow\
\left(\beta(U-\tfrac12),\ Z/\sqrt{12}\right),
\]
where \(U\sim\operatorname{Uniform}[0,1]\) and \(Z\sim N(0,1)\) are independent. Thus the common coordinate shift does **not** concentrate, whereas the gap between level averages has universal Gaussian variance \(1/12\), independent of \(\alpha\).

For the standard affine-invariant isotropic constant
\[
L(L_{p,q})^2=\frac{\bigl(\det\operatorname{Cov}(X,Y)\bigr)^{1/n}}{\operatorname{vol}_n(L_{p,q})^{2/n}},
\]
one nevertheless has \(L(L_{p,q})\to1/\sqrt{12}\). If \(\kappa(\operatorname{Cov})\) denotes the ratio of its largest to smallest eigenvalue, then
\[
\frac{\kappa(\operatorname{Cov}(X,Y))}{n}
\longrightarrow\frac{\beta^2}{\min\{\alpha^2,\beta^2\}}.
\]
Consequently the cube-limit isotropic constant coexists with linearly diverging Euclidean inertia anisotropy and a nonconcentrating coordinate barycenter.

## Assumptions and scope
The inequalities are those of the Lipschitz polytope of the complete two-level poset \(A_p\oplus A_q\) in the sense of Sanyal–Stump. All covariance and volume statements use the **original coordinate Euclidean metric**, not the metric obtained by a change of poset coordinates. The asymptotic claim requires both layer proportions to converge to strictly positive limits. No claim is made about general finite posets or about the John/Löwner ellipsoids.

## Proof
**1. Exact conditional disintegration.** For fixed \(x\in[0,1]^p\), each upper coordinate ranges independently in the interval \([\max_i x_i,1+\min_i x_i]\), of length \(1-R\). Since \(p\ge2\), the Jacobian density for the minimum \(A\) and range \(R\) of \(p\) cube coordinates is \(p(p-1)R^{p-2}\), on \(0\le A\le1-R\). Integrating the upper coordinates gives
\[
\operatorname{vol}(L_{p,q})=p(p-1)\int_0^1r^{p-2}(1-r)^{q+1}\,dr
=\frac{p!\,(q+1)!}{(p+q)!}.
\]
The normalized distribution of \(R\) is therefore \(\operatorname{Beta}(p-1,q+2)\). Conditional on \(R\), the minimum has the form \(A=(1-R)T\) with \(T\sim\operatorname{Uniform}[0,1]\) independent of \(R\). Conditional also on \(A,R\), the \(p\) lower coordinates consist of the values \(A\), \(A+R\), and \(p-2\) independent uniform values in \([A,A+R]\), assigned to uniformly random distinct labels; the \(q\) upper coordinates are independent uniform values in \([A+R,A+1]\). This constructs exactly the normalized uniform-volume measure, including the case \(p=2\).

**2. Covariance.** Let \(C=A+R/2=1/2+(1-R)(T-1/2)\). The conditional mean of every lower coordinate is \(C\) and the conditional mean of every upper coordinate is \(C+1/2\). Hence
\[
\operatorname{Var}(C)=\frac{\mathbb E(1-R)^2}{12}=\frac{s}{12},
\qquad \mathbb ER^2=t.
\]
For the randomly labeled normalized lower-coordinate pattern, its diagonal conditional variance divided by \(R^2\) is \((p+4)/(12p)\) and its off-diagonal conditional covariance divided by \(R^2\) is \(-1/[2p(p-1)]\). This follows by assigning the two extrema and summing the independent centered \(p-2\) interior values. Conditional upper coordinates have variance \((1-R)^2/12\) and zero off-diagonal conditional covariance. The groups are conditionally independent after subtracting their means. The law of total covariance therefore yields
\[
\begin{aligned}
\operatorname{Var}(X_i)&=s/12+t(p+4)/(12p),\\
\operatorname{Cov}(X_i,X_k)&=s/12-t/[2p(p-1)]&& (i\ne k),\\
\operatorname{Var}(Y_j)&=s/6,\\
\operatorname{Cov}(Y_j,Y_l)&=s/12&&(j\ne l),\\
\operatorname{Cov}(X_i,Y_j)&=s/12.
\end{aligned}
\]
The covariance matrix commutes with coordinate permutations within each level. Its orthogonal decomposition is the \((p-1)\)-dimensional lower zero-sum space, the \((q-1)\)-dimensional upper zero-sum space, and the plane spanned by the two normalized all-ones vectors. Subtracting diagonal and off-diagonal entries produces \(\lambda_X\) and \(\lambda_Y\) above; the normalized all-ones plane gives \(M_{p,q}\). Its determinant is the displayed rational expression. For \(p\ge2\), \(s>0\), \(t>0\), and that determinant is positive, as required for a full-dimensional body.

**3. Joint weak limit.** With \(U_i,V_j\) independent \(\operatorname{Uniform}[0,1]\) variables, the disintegration gives the exact identities
\[
\bar X-\tfrac12=(1-R)(T-\tfrac12)+\frac{R}{p}\sum_{i=1}^{p-2}(U_i-\tfrac12),
\]
\[
\bar Y-\bar X-\tfrac12=
\frac{1-R}{q}\sum_{j=1}^q(V_j-\tfrac12)
-\frac{R}{p}\sum_{i=1}^{p-2}(U_i-\tfrac12).
\]
The first expression's second term tends to zero in probability. The beta mean and variance give \(R\to\alpha\) in probability. The usual independent bounded-summand central limit theorem, followed by Slutsky's theorem, makes the scaled difference converge to a normal with variance
\[
\frac1{12}\left(\frac{\beta^2}{\beta}+\frac{\alpha^2}{\alpha}\right)=\frac1{12}.
\]
Independence of the Gaussian limit and \(T\) holds because \(T\) is exactly independent of the range and both centered interior sums for every finite \(p,q\). This proves the joint limit, rather than merely its two marginals.

**4. Isotropic limit and anisotropy.** Stirling's formula and the exact volume give
\[
\operatorname{vol}(L_{p,q})^{1/n}\longrightarrow
\alpha^{\alpha}\beta^{\beta}.
\]
The contrast eigenvalues tend to \(\alpha^2/12\) and \(\beta^2/12\). The two remaining eigenvalues have asymptotics \(n\beta^2/12\) and \(\alpha\beta/12\), obtained from the trace and determinant of \(M_{p,q}\). Since their logarithms divided by \(n\) vanish, the determinant formula gives
\[
\bigl(\det\operatorname{Cov}(X,Y)\bigr)^{1/n}
\longrightarrow \frac{\alpha^{2\alpha}\beta^{2\beta}}{12}.
\]
Division by the squared volume root proves the claimed isotropic limit. Moreover \(\alpha\beta\ge\min\{\alpha^2,\beta^2\}\), so the smallest covariance eigenvalue approaches \(\min\{\alpha^2,\beta^2\}/12\), whereas the largest divided by \(n\) tends to \(\beta^2/12\). This yields the condition-number limit.

## Verification
Run `python checker.py` using Python with SymPy. The checker performs direct chamber integration of seven monomial moments for \((p,q)=(2,1)\), verifies the resulting volume/means/covariances, independently integrates six beta-volume formulas, and evaluates six exact full-matrix covariance determinants against the eigenvalue factorization. Its expected terminal result is `VERIFY_OK direct_exact_moments=7 beta_volumes=6 covariance_determinants=6`. These finite exact checks corroborate the proof; they are not offered as certificates of the large-dimension probability limits.

## Relationship to prior work
Sanyal and Stump introduced Lipschitz polytopes of posets and established their alcoved triangulations, lattice and symmetry properties; their definition (1.1) is specialized here to the ordinal sum of two antichains. In particular, their Proposition 4.1 already implies central symmetry of the ranked family and is **not** asserted as new. The present contribution is the uniform-volume disintegration, complete original-coordinate inertia spectrum, joint nonconcentration/Gaussian behavior, and the contrast between cube-limit isotropic constant and diverging condition number. The polytope considered is not the ordinary order polytope, chain polytope, or the signed-chain construction: in addition to bounding each lower coordinate, it bounds **every individual cross-level difference from both sides**. Related results about the John ellipsoids of ordinary height-two order/chain polytopes concern different bodies and an extremal ellipsoid rather than uniform-volume inertia. This statement makes no priority claim over inaccessible full texts.

## Limitations
The asymptotic statement excludes vanishing layer proportions. Complete originality relative to every alternate polytope nomenclature is not independently certified; the most directly relevant earlier article was inspected through its publicly available full HTML version, while some neighboring mathematical-record summaries could not be checked in full. No independent mathematical audit has been performed. The script verifies selected finite cases only; the analytic argument supplies the general proof.

## References
1. R. Sanyal and C. Stump, *Lipschitz polytopes of posets and permutation statistics*, arXiv:1703.10586, first publicly posted 2017-03-30; Journal of Combinatorial Theory, Series A **158** (2018), 605–620. Full author-distributed HTML: https://arxiv.org/abs/1703.10586.
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (2016). Concerns metric Lipschitz polytopes rather than the directed-poset body treated here.
3. Relevant publicly indexed distinct results on balanced height-two order-polytope John ellipsoids and signed-chain volume are identified and their limited comparability noted in the review material.
