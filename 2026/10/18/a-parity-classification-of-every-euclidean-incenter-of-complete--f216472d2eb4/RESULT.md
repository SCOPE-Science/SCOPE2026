# A parity classification of every Euclidean incenter of complete-bipartite symmetric edge polytopes

## Finding
For integers \(2\le p\le q\), set \(N=p+q\), let \(A,B\) be disjoint index sets of sizes \(p,q\), and work in the intrinsic Euclidean hyperplane \(H=\{z\in\mathbb R^N:\sum_i z_i=0\}\). Consider the canonical symmetric-edge polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in A,\ j\in B\}\subset H.
\]
Let \(\mathcal I_{p,q}\) be the set of centers of all largest-radius Euclidean balls contained in this polytope. Put
\[
T=q-\frac{q\bmod 2}{N},\qquad r=T^{-1/2}.
\]
Then \(r\) is the exact inradius, and the following describes **every** optimal center and its affine dimension.

For \(p<q\) and odd \(q\), precisely the vectors \(z=(x,0_B)\) belong to \(\mathcal I_{p,q}\) when
\[
\sum_{i\in A}x_i=0,\qquad
\left|\sum_{i\in A}\varepsilon_i x_i\right|\le
1-r\sqrt{p-\frac{(\sum_{i\in A}\varepsilon_i)^2}{N}}
\quad\text{for every }\varepsilon\in\{-1,1\}^A.
\tag{1}
\]
This incenter polytope has affine dimension \(p-1\).

For \(p<q\) and even \(q\), precisely the vectors \(z=(x,b\mathbf1_B)\) belong to \(\mathcal I_{p,q}\) when
\[
\sum_{i\in A}x_i=-qb,\qquad
|b|\le\frac{1-\sqrt{1-4/(Nq)}}2,
\tag{2}
\]
and the \(2^p\) sign inequalities in (1), with the same right sides but no longer requiring \(\sum_i x_i=0\), all hold. This incenter polytope has affine dimension \(p\). Thus the exponentially many facets indexed by signs on the larger part reduce to a single scalar interval bound.

For equal part sizes \(p=q=m\), the incenter is **unique exactly when \(m\) is odd**: \(\mathcal I_{m,m}=\{0\}\). When \(m\) is even, the complete locus instead is the explicit line segment
\[
\boxed{\mathcal I_{m,m}=
\left\{(a\mathbf1_A,-a\mathbf1_B): |a|\le\frac{1-\sqrt{1-2/m^2}}2\right\}.}
\tag{3}
\]
In particular, among genuine complete-bipartite graphs, **the origin is the unique Euclidean incenter if and only if both parts have the same odd size**.

The exact number of facets tangent to the *origin-centered* maximum-radius ball is
\[
F_{p,q}=\begin{cases}
\binom{q}{q/2},&p<q,\ q\text{ even},\\
2\binom{q}{(q-1)/2},&p<q,\ q\text{ odd},\\
2\binom{q}{q/2},&p=q,\ q\text{ even},\\
4\binom{q}{(q-1)/2},&p=q,\ q\text{ odd}.
\end{cases}
\tag{4}
\]
At either endpoint of the segment (3), the number of tangent facets increases by \(1\) for \(m=2\), and by \(2\binom{m}{m/2-1}\) for every even \(m\ge4\). (When \(m=2\), the two formally described additional sign labels define the *same* facet.)

## Assumptions and scope
The graph is exactly the unweighted complete bipartite graph with two nonempty parts of sizes at least two, embedded through signed incidence vectors; arbitrary affine transformations generally change the answer. Its dimension is \(N-1\), and all distances, affine dimensions, and inscribed balls use the Euclidean metric inherited by \(H\). The locus includes every possible center; the origin is one but need not be the only one. The primary cited 2018 paper has primary MSC \(52B12\).

## Proof
**1. Exact facet inequalities.** Higashitani, Jochemko, and Michałek, Proposition 3.4 of the first public version [1], give every facet label, up to adding a common constant: either \(f=(\varepsilon,0_B)\), \(\varepsilon\in\{-1,1\}^A\), or \(f=(0_A,\eta)\), \(\eta\in\{-1,1\}^B\). The facet inequality is \(f\cdot z\le1\). The all-constant sign choices yield duplicate labels between the two families but do not invalidate the halfspace system. Orthogonally projecting the normal to \(H\) gives \(\tilde f=f-(\sum f_i/N)\mathbf1\). For a part of size \(s\) and sign sum \(t\),
\[
\|\tilde f\|^2=s-\frac{t^2}{N}.
\tag{5}
\]
These are **all** facets, not merely selected supporting inequalities.

**2. Global inradius, without assuming a center.** Central symmetry sends every feasible radius-\(\rho\) ball at \(z\) to a feasible ball at \(-z\). Convexity implies the same-radius ball at zero is feasible. Equivalently, every facet pair \(f,-f\) bounds any feasible radius by \(\rho\le1/\|\tilde f\|\). For a part of size \(s\), the maximum of (5) over sign vectors is \(s-(s\bmod 2)/N\), since \(|t|\) is \(0\) for even \(s\) and \(1\) for odd \(s\). This value is strictly increasing in integer \(s\), so for \(q\ge p\) the largest projected-normal squared norm is precisely \(T\). The centered ball of radius \(r=1/\sqrt T\) satisfies every facet inequality; no larger ball at any center exists.

**3. Complete optimal-center constraints.** A radius-\(r\) ball at \(z\in H\) is contained in the polytope if and only if
\[
f\cdot z+r\|\tilde f\|\le1
\tag{6}
\]
for every facet label in step 1. Including all sign vectors turns (6) into the equivalent absolute-value inequalities
\[
|\varepsilon\cdot z_A|\le 1-r\sqrt{p-(\sum\varepsilon)^2/N},\qquad
|\eta\cdot z_B|\le1-r\sqrt{q-(\sum\eta)^2/N}.
\tag{7}
\]
This already is a complete explicit halfspace description. For all sign patterns that maximize (5), the right side of the corresponding inequality is zero. These equalities determine the affine hull of the locus, because all remaining finitely many inequalities are **strict at the origin**.

**4. Sign-vector spans and the parity dimension law.** Among \(q\)-component sign vectors, those of sum \(0\) (for even \(q\)) span precisely the coordinate-sum-zero subspace of \(\mathbb R^q\): transposing a plus and minus gives every coordinate difference. Those of sum \(1\) (for odd \(q\)) span all of \(\mathbb R^q\): the same differences span the zero-sum space, and any chosen vector has nonzero sum. If \(p<q\), only the larger part's sign vectors maximize (5). Hence for odd \(q\), their zero-clearance equalities force \(z_B=0\), while \(\sum_i z_i=0\) forces \(\sum_i z_{A,i}=0\). Their common nullspace has dimension \(p-1\), and (7) reduces exactly to (1). For even \(q\), those equalities force \(z_B=b\mathbf1_B\), leaving \(\sum_i z_{A,i}=-qb\), a linear space of dimension \(p\).

For even \(q\), the remaining larger-part sign patterns have even nonzero sign sum \(t\) with \(2\le |t|\le q\). On \(z_B=b\mathbf1_B\), their inequalities in (7) are
\[
|b|\le g(|t|),\qquad
g(u)=\frac{1-\sqrt{1-u^2/(Nq)}}{u}
=\frac{u}{Nq(1+\sqrt{1-u^2/(Nq)})}.
\tag{8}
\]
The displayed positive function is strictly increasing for \(0<u\le q\); hence \(|t|=2\) imposes the strongest condition and gives (2). There are no additional restrictions beyond the smaller-part inequalities in (7). Since these are strict at the origin, (2) has full relative dimension \(p\).

For \(p=q=m\), both sign families attain the same largest norm. If \(m\) is odd, each active family spans all coordinates of its own part, forcing \(z_A=z_B=0\). If \(m\) is even, the active families force \(z_A=a\mathbf1_A\), \(z_B=b\mathbf1_B\); the zero-sum condition gives \(b=-a\). Applying (8) with \(N=2m\) and \(|t|=2\) gives exactly the endpoints in (3). Thus the interval is nondegenerate and exhausts every optimal center.

**5. Contact counts and endpoint behavior.** At the origin a facet contacts the radius-\(r\) ball exactly when its squared normal norm in (5) equals \(T\), i.e. when its sign imbalance is minimal on a maximum-size part. Counting balanced sign choices gives (4). No two maximizers belong to duplicate all-constant sign-label classes, since \(p,q\ge2\). For balanced even sizes \(m\), every interior-segment center remains tangent to precisely the sign-zero facets. At an endpoint, the first additional tight constraints are the sign-sum \(+2\) facets on one part and the sign-sum \(-2\) facets on the other. Each family has \(\binom{m}{m/2-1}\) labels. For \(m\ge4\) none are constant labels, so the two families are disjoint; for \(m=2\), they represent the same facet, resulting in exactly one additional contact.

## Verification
The accompanying standalone standard-library program `verify.py` reconstructs all sign-labeled facet normals, performs their norm comparisons with exact rational arithmetic, computes the rank of the active facet constraints and the resulting affine dimension, and verifies small independent positive and negative perturbations along every claimed incenter direction using squared exact rational inequalities. It checks \(49\) pairs with \(2\le p\le8\) and \(p\le q\le11\), totaling \(30{,}676\) sign-labeled facets and \(11{,}312\) active facet labels. A separate endpoint test handles duplicate facets and confirms the four balanced even examples \(m=2,4,6,8\). Exact reproducibility command: `python3 verify.py`. These finite checks do not replace the all-dimensional proof.

## Relationship to prior work
The source [1] proves the decisive complete-bipartite facet classification, and is fully credited for it. It studies facets and Ehrhart theory; it does not state the Euclidean largest-ball-center locus or its parity-dependent dimension. Source [2] identifies connections with Kantorovich–Rubinstein/Lipschitz polytopes and discusses the same root realization, but does not derive this center classification.

Earlier indexed mathematical results determine the inradius and tangent facets for **complete multipartite graphs with at least three parts**, a different graph family, and determine the full one-dimensional incenter locus for **stars**, where one bipartition part has size one. They do not imply the present two-part result with \(p,q\ge2\), particularly the dimensions \(p-1\) or \(p\) for unequal parts and the exact exceptional segment for equal even parts. Another earlier result gives John and Löwner ellipsoids for this exact bipartite family; those affine-ellipsoid invariants do not determine the centers of largest Euclidean balls. The present theorem therefore concerns the **complete metric incenter locus**, not a reinterpretation of an Ehrhart number, an ellipsoid result, or a claim that the facet description itself is new.

## Limitations
This theorem uses the exact canonical Euclidean embedding and integer cardinalities; it does not claim arbitrary edge-weight versions, other graphs, or affine invariance. For unequal sizes it gives complete inequalities and an affine-dimension classification, not a closed formula for the vertices or volume of the incenter polytope. The radius and contact-count calculations follow straightforwardly from the cited facet theorem; the mathematical claim of interest is the complete optimal-center geometry and its parity/uniqueness transition. Older equivalent metric-polytope terminology may contain an unindexed formulation; no independent mathematical audit has been performed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public 2018-07-20), Proposition 3.4; Mathematika 65 (2019), 763–784. https://arxiv.org/html/1807.07678v1
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11); Electronic Journal of Combinatorics 29 (2022), P3.24. https://arxiv.org/abs/1910.05193
