# A one-third spectral crossover in complete split-graph Lipschitz dual balls

## Finding

Let \(p,q\ge2\) be integers, \(N=p+q\), and let \(G_{p,q}=K_p\vee\overline{K_q}\) be the *complete split graph*: the first \(p\) vertices form a clique, the remaining \(q\) vertices have no edges among themselves, and every vertex in one class is adjacent to every vertex in the other. All edges have length one and the vertex set carries the shortest-path metric. Let \(Q_{p,q}\) be the unit ball of the real Lipschitz dual \(\operatorname{Lip}_0(G_{p,q})\). Fix one clique vertex as basepoint and use its zero-valued anchored coordinates to define volume. Choose a point uniformly from this ball and project its \(N\) vertex values orthogonally onto the zero-sum hyperplane \(H_N\subset\mathbb R^N\); denote the random vector by \(Z\).

Define the positive one-dimensional integrals
\[
I_j(p,q)=\int_0^1 r^{p-2+j}(2-r)^q\,dr,\qquad j=0,1,2,
\]
and set \(\mu_2=I_2/I_0\) and \(\nu_2=(4I_0-4I_1+I_2)/I_0\). Then the **exact anchored volume** is
\[
\operatorname{vol}(Q_{p,q})=p(p-1)I_0(p,q).
\]
Both it and the covariance are explicitly rational; indeed,
\[
I_j(p,q)=\sum_{s=0}^{q}\frac{(-1)^s\binom qs 2^{q-s}}{p-1+j+s}.
\]

Write \(P_A\) and \(P_B\) for the orthogonal projectors onto the zero-sum subspaces on the clique and independent-set vertex classes, and let \(P_C\) project onto the line of vectors constant on each class and globally zero-sum. Then
\[
\operatorname{Cov}(Z)=\lambda_A P_A+\lambda_B P_B+\lambda_C P_C,
\]
where
\[
\lambda_A=\frac{(p+1)(p+2)}{12p(p-1)}\mu_2,\qquad
\lambda_B=\frac{\nu_2}{12},\qquad
\lambda_C=\frac{q(p-2)}{12pN}\mu_2+\frac{p}{12N}\nu_2.
\]
The eigenvalue multiplicities are respectively \(p-1\), \(q-1\), and \(1\); there are no other eigenvalues.

The **spectral crossover** is sharp in the following asymptotic sense. If \(p\to\infty\) and \(q/p\to c\in(0,1)\), then
\[
\lim_{p\to\infty}p(\lambda_C-\lambda_A)
=\frac{c(3c-1)}{6(1-c^2)}.
\]
Consequently the contrast eigenvalue is eventually smaller than the clique-internal eigenvalue for every fixed limiting ratio \(0<c<1/3\), and eventually larger for every fixed \(1/3<c<1\). At the second natural boundary, \(q=p\to\infty\),
\[
\lim_{p\to\infty}\sqrt p\,(\lambda_C-\lambda_A)=\frac1{6\sqrt\pi}>0.
\]
For \(q/p\to c>1\), a macroscopic gap replaces this vanishing splitting:
\[
\lim_{p\to\infty}(\lambda_C-\lambda_A)=\frac{c-1}{3(1+c)^2}>0.
\]
No finite-parameter uniqueness of a crossing index and no limiting sign at the special ratio \(c=1/3\) are asserted.

## Assumptions and scope

All random variables and covariance operators are real; \(p,q\) are arbitrary integers at least two. The Euclidean inner product is the ambient standard inner product on \(H_N=\{z\in\mathbb R^N:\sum z_i=0\}\). Anchored coordinates have a *different* Euclidean volume normalization from the intrinsic \(H_N\) volume; the latter equals the anchored volume divided by \(\sqrt N\). The three projectors are mutually orthogonal and sum to the identity on \(H_N\). The distribution used here is uniform Lebesgue measure in the **dual unit ball**, not uniform distribution over vertices or facets of the primal symmetric-edge polytope.

## Proof

**1. Exact disintegration.** Label the clique vertices \(C_1,\ldots,C_p\), with \(C_1=0\), and the independent vertices \(Y_1,\ldots,Y_q\). The Lipschitz inequalities say exactly
\[
|C_i-C_j|\le1,\qquad |Y_\ell-C_i|\le1.
\]
The omitted independent-to-independent inequalities have bound \(2\) and follow from those displayed. Write \(m=\min_i C_i\), \(M=\max_i C_i\), and \(R=M-m\in[0,1]\). Conditional on the clique coordinates, each \(Y_\ell\) varies independently throughout the interval \([M-1,m+1]\), of length \(2-R\). Except for a null set where extrema tie, choose which two clique labels attain the minimum and maximum, put the minimum at \(0\), the maximum at \(R\), and assign the other \(p-2\) labels independent positions uniform on \([0,R]\). Subtract the chosen basepoint's coordinate from every coordinate. This quotient-coordinate change has unit Jacobian, while the interior positions contribute \(R^{p-2}\). There are \(p(p-1)\) ordered endpoint choices. Integrating the \(q\) leaf intervals proves the volume formula and shows that \(R\) has density
\[
f_{p,q}(r)=\frac{r^{p-2}(2-r)^q}{I_0(p,q)}\,\mathbf1_{(0,1)}(r).
\]
Given \(R\), the labeled clique values, up to common translation, are a uniform random permutation of \(0,R\) and \(p-2\) independent \(\operatorname{Unif}[0,R]\) variables. Given these values, the independent-set coordinates have the exact representation
\[
Y_\ell=\frac{m+M}{2}+\left(1-\frac R2\right)U_\ell,
\]
where \(U_1,\ldots,U_q\) are independent uniform variables on \([-1,1]\), independent of the clique variables and \(R\). Reflection of all potentials ensures the centered random vector has mean zero.

**2. Clique fluctuations.** Conditional on \(R=r\), the sum of squared pairwise differences among clique coordinates has mean
\[
\mathbb E\left[\sum_{i<j}(C_i-C_j)^2\mid R=r\right]
=r^2\left[1+\frac{2(p-2)}3+\frac{(p-2)(p-3)}{12}\right]
=\frac{(p+1)(p+2)}{12}r^2.
\]
Use \(\sum_{i<j}(C_i-C_j)^2=p\sum_i(C_i-\overline C)^2\), exchangeability, and the \(p-1\) dimensional clique-internal eigenspace. Its eigenvalue is therefore \(\lambda_A\) as displayed.

**3. Independent-set fluctuations and contrast.** Since \(\operatorname{Var}(U_\ell)=1/3\), the covariance on the independent-set zero-sum subspace is \(\mathbb E[(1-R/2)^2]/3=\nu_2/12=\lambda_B\). With \(H=(m+M)/2\), the conditional mean of \(H-\overline C\) vanishes and its conditional variance is \((p-2)r^2/(12p^2)\), because only the \(p-2\) internal uniform positions contribute random deviations from the midrange. Consequently
\[
\operatorname{Var}(\overline Y-\overline C)
=\frac{p-2}{12p^2}\mu_2+\frac{\nu_2}{12q}.
\]
The unit-normalized contrast coordinate is \(\sqrt{pq/N}(\overline Y-\overline C)\). Its variance is \(\lambda_C\). Permutation invariance within both classes forces all cross-covariances between distinct irreducible class components to vanish, which completes the covariance decomposition.

**4. First crossover.** Put \(X=1-R\). Its density on \([0,1]\) is proportional to \((1-x)^{p-2}(1+x)^q\). For \(q/p\to c\in(0,1)\), a boundary Laplace estimate gives \(pX\) convergence, with its first two moments, to an exponential random variable of rate \(1-c\). This follows directly by substituting \(x=u/p\), using the pointwise limit \((1-u/p)^{p-2}(1+u/p)^q\to e^{-(1-c)u}\) and an exponential dominating function for every compact limiting-ratio interval inside \((0,1)\). In particular,
\[
p\mathbb EX\longrightarrow\frac1{1-c},\qquad
p^2\mathbb EX^2\longrightarrow\frac2{(1-c)^2}.
\]
From the exact eigenvalues,
\[
\lambda_C-\lambda_A=
\frac{F_{p,q}}{12(p+q)(p-1)},
\]
where
\[
F_{p,q}=p(p-1)\,\mathbb E(2-R)^2-
\big((p+1)(p+2)+6q\big)\,\mathbb ER^2.
\]
Writing \(R=1-X\), expanding \((1\pm X)^2\), and substituting the moment limits gives
\[
\frac{F_{p,q}}p\longrightarrow
-4-6c+\frac4{1-c}=
\frac{2c(3c-1)}{1-c}.
\]
Division by the exact denominator proves the announced one-third threshold and its precise coefficient.

**5. Second boundary and macroscopic regime.** For \(q=p\), the density of \(X\) is proportional to \((1-x^2)^p(1-x)^{-2}\), so \(\sqrt p\,X\) converges with its first moments to the half-Gaussian density \(2e^{-u^2}/\sqrt\pi\) on \(u\ge0\). Thus \(\sqrt p\,\mathbb EX\to1/\sqrt\pi\). The exact formula for \(F_{p,p}\) above then yields the stated \(1/(6\sqrt\pi)\) limit. If \(q/p\to c>1\), the strictly concave exponent \(\log r+c\log(2-r)\) has unique maximizer \(r_c=2/(1+c)\) in \((0,1)\). Laplace concentration yields \(\mathbb ER^2\to r_c^2\) and \(\mathbb E(2-R)^2\to (2-r_c)^2\). Substitution in the exact covariance formula gives
\[
\lambda_A\to\frac{r_c^2}{12},\qquad
\lambda_C\to\frac{cr_c^2}{12},
\]
and hence the stated positive macroscopic gap.

## Verification

The standalone `verify_split.py` enumerates vertices from active integer edge constraints, triangulates boundary facets against the origin, and integrates all first and second moments over the resulting simplices with exact rational arithmetic. Its polytope integrals independently reproduce the volume and the *entire* covariance matrix for \((p,q)=(2,1),(3,1),(4,1),(2,2),(2,3),(3,2)\). The case \(q=1\) is an auxiliary equilateral boundary check, not an additional theorem domain. Exact rational positivity and the equilateral endpoint identities are tested for \(323\) pairs with \(2\le p\le18\) and \(1\le q\le19\). The all-parameter formulas and asymptotic limits are proved above and do not rely on finite tests.

## Relationship to prior work

The finite-metric transportation-polytope viewpoint and the equilateral benchmark belong to Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, first posted 2019). D'Alì, Delucchi and Michałek (arXiv:1910.05193, first posted 2019) investigate graph symmetric-edge polytopes, their combinatorial invariants and connections to Lipschitz polytopes. Chen, Davis and Korchevskaia (arXiv:2107.12315, first posted 2021) classify facet/face subgraphs. These cited sources do not state the one-third and one-to-one asymptotic spectral regimes. The elementary exact disintegration here is also obtainable by conditioning the corresponding complete-bipartite dual-ball range law to \(R\le1\); the range-conditioning step and resulting rational moment evaluation are supporting tools, not asserted as standalone discoveries. The distinctive assertion is the sharp two-stage **ordering and scaling of the covariance eigenvalues** for the continuously sampled split-graph dual ball; it is not a vertex-covariance, facet-count, inball, or enclosing-ellipsoid statement.

## Limitations

The asymptotic sign at the critical ratio \(q/p\to1/3\) is not classified without finer control of the deviation of \(q\) from \(p/3\); no assertion of a unique finite-dimensional crossing is made. Full-text novelty checking covered relevant accessible primary material but cannot rule out every unindexed equivalent treatment. Computations cover finitely many small dimensions and are supplemental. This is an analytic mathematical claim with self-review; independent audit has not been performed.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (initial public version 2019-10-11), https://arxiv.org/abs/1910.05193.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and Volume Product of Finite Dimensional Lipschitz-Free Spaces*, arXiv:1911.10642 (initial public version 2019-11-24), https://arxiv.org/abs/1911.10642.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and Facet Subgraphs of Symmetric Edge Polytopes*, arXiv:2107.12315 (initial public version 2021-07-26), https://arxiv.org/abs/2107.12315.
