# The John ellipsoid and full contact structure of balanced complete-multipartite stable-set polytopes

## Finding

Let \(r\ge3\) and \(a\ge2\) be integers, and let \(G=K_{a,\ldots,a}\) be the complete \(r\)-partite graph with \(a\) vertices in each part. Its stable-set polytope \(P_{a,r}\subset\mathbb R^{ar}\), in standard indicator-vector coordinates and the standard Euclidean metric, has a unique maximum-volume inscribed ellipsoid. Put
\[
 b=\sqrt{r-\frac{r-1}{a}},\qquad t=\frac1{r+b},\qquad
 u=\frac{b}{r(r+b)(b+1)},\quad v=\frac1{r(r+b)},\quad w=\frac{b}{r(r+b)^2}.
\]
Let \(\Pi_U\) project orthogonally onto the subspace of vectors summing to zero within each of the \(r\) parts; let \(\Pi_W\) project onto the all-ones line; and let \(\Pi_V\) project onto the complementary subspace of vectors constant within each part, with overall sum zero. Then the John ellipsoid is
\[
 E_{a,r}=\{x:(x-t\mathbf1)^\mathsf T\Sigma^{-1}(x-t\mathbf1)\le1\},\qquad
 \Sigma=u\Pi_U+v\Pi_V+w\Pi_W.
\]
Its squared principal semiaxes are \(u\) with multiplicity \(r(a-1)\), \(v\) with multiplicity \(r-1\), and \(w\) with multiplicity one, with \(0<w<u<v\). Its Euclidean volume is exactly
\[
 \operatorname{vol}_{ar}(E_{a,r})=\frac{\pi^{ar/2}}{\Gamma(ar/2+1)}
 u^{r(a-1)/2}v^{(r-1)/2}w^{1/2}.
\]
Every one of the \(ar+a^r\) facets of \(P_{a,r}\) is tangent to \(E_{a,r}\), at distinct points. In particular, the exponentially many transversal-clique facets all actively determine the same optimal ellipsoid.

## Assumptions and scope

Index coordinates by pairs \((j,i)\), with \(1\le j\le r\) and \(1\le i\le a\). The polytope is
\[
 P_{a,r}=\operatorname{conv}\{\mathbf1_S:S\text{ lies entirely in a single part}\}
 =\left\{x\ge0:\sum_{j=1}^r x_{j,i_j}\le1
 \text{ for every }(i_1,\ldots,i_r)\in\{1,\ldots,a\}^r\right\}.
\]
The second description follows by putting \(m_j=\max_i x_{j,i}\): all transversal inequalities imply \(\sum_jm_j\le1\), and the vector \(x\) is a convex mixture of the \(r\) within-part cubes and the origin, with mixing coefficients \(m_j\). When a coefficient vanishes, its block contributes zero. The inequalities \(x_{j,i}\ge0\) and all \(a^r\) transversal inequalities define distinct facets: respectively take one coordinate zero and all others sufficiently small, or take selected coordinates equal to \(1/r\) and unselected coordinates strictly between zero and \(1/r\). These points satisfy every other defining inequality strictly. Consequently \(P_{a,r}\) is full dimensional in \(\mathbb R^{ar}\).

The statement is specific to equal part sizes \(a\), at least three parts, and the given Euclidean coordinates. It is not a general claim for arbitrary multipartite graphs or for other metrics.

## Proof

**1. Symmetry subspaces and candidate.** The three projectors are pairwise orthogonal and sum to the identity. Their ranks are \(r(a-1)\), \(r-1\), and one. The parameters \(u,v,w\) are strictly positive. The defining radical satisfies the exact identity
\[
 a b^2=ar-r+1. \tag{1}
\]
For a coordinate vector \(e_{j,i}\), the squared distance to the center in the ellipsoid dual metric is controlled by
\[
 e_{j,i}^{\mathsf T}\Sigma e_{j,i}
 =\frac{a-1}{a}u+\frac{r-1}{ra}v+\frac1{ra}w=t^2. \tag{2}
\]
For a transversal \(C=(i_1,\ldots,i_r)\), write \(n_C=\sum_j e_{j,i_j}\). Its \(V\)-projection vanishes; its squared \(U\)- and \(W\)-projection lengths are \(r(a-1)/a\) and \(r/a\). Thus
\[
 n_C^{\mathsf T}\Sigma n_C
 =\frac{r(a-1)}a u+\frac ra w=(1-rt)^2,
 \qquad 1-rt=\frac b{r+b}>0. \tag{3}
\]
Equations (2) and (3) follow by direct substitution using (1); their respective numerator differences are multiples of \(ab^2-ar+r-1\).

**2. Containment and tangencies.** The support of \(E_{a,r}\) in direction \(z\) equals \(z^{\mathsf T}(t\mathbf1)+\sqrt{z^{\mathsf T}\Sigma z}\). The minimum coordinate is \(t-\sqrt{e_{j,i}^{\mathsf T}\Sigma e_{j,i}}=0\). Every clique support is \(rt+\sqrt{n_C^{\mathsf T}\Sigma n_C}=1\). Hence the proposed ellipsoid lies in every facet halfspace, touching each one. The relative contact displacements from the center are
\[
 p_{j,i}=-\frac{\Sigma e_{j,i}}t,\qquad
 q_C=\frac{\Sigma n_C}{1-rt}. \tag{4}
\]
These are distinct because the supporting normal of a nonsingular ellipsoid is unique at each boundary point, and the listed facet normals are mutually nonparallel.

**3. Exact positive John certificate.** Assign to every coordinate contact the positive weight
\[
 \alpha=\frac r{r+b},
\]
and to every transversal contact the positive weight
\[
 \gamma=\frac{rb}{a^{r-1}(r+b)}.
\]
Because \(\sum_Cn_C=a^{r-1}\mathbf1\) and \(\alpha/t=\gamma a^{r-1}/(1-rt)=r\), equation (4) gives
\[
 \alpha\sum_{j,i}p_{j,i}+\gamma\sum_Cq_C=0. \tag{5}
\]
Let \(F=a^{-r}\sum_C n_Cn_C^{\mathsf T}\). Its entries are \(1/a\) on the diagonal, zero off-diagonal within a part, and \(1/a^2\) between different parts. Therefore it acts by eigenvalues \(1/a\), zero, and \(r/a\) on \(U,V,W\), respectively. Direct calculation gives
\[
 K:=\frac\alpha{t^2}I+\frac{\gamma a^r}{(1-rt)^2}F
 =u^{-1}\Pi_U+v^{-1}\Pi_V+w^{-1}\Pi_W=\Sigma^{-1}. \tag{6}
\]
Multiplying (6) by \(\Sigma\) on both sides and applying (4) yields
\[
 \alpha\sum_{j,i}p_{j,i}p_{j,i}^{\mathsf T}
 +\gamma\sum_Cq_Cq_C^{\mathsf T}=\Sigma. \tag{7}
\]
Under the affine map \(z=\Sigma^{-1/2}(x-t\mathbf1)\), equations (2)--(4) send the contacts to the unit sphere. Equations (5) and (7) become the zero-first-moment and identity-second-moment contact conditions. John's ellipsoid characterization therefore proves the contained ellipsoid has largest volume among *all* inscribed ellipsoids, without a symmetry assumption on the competitor. The maximum-volume inscribed ellipsoid is unique.

**4. Spectrum, volume and ordering.** The spectrum follows from the projectors' ranks. Moreover \(u/v=b/(b+1)<1\) and \(w/u=(b+1)/(r+b)<1\) because \(r\ge3\). Taking the square root of \(\det\Sigma\) times the volume of the Euclidean unit ball gives the displayed volume formula. The relative-interior facet constructions in the assumptions and the normal-uniqueness argument finish the facet classification.

## Verification

The accompanying standard-library `CHECK.py` uses exact fractions and a quadratic-number field to replay the tangency identities, all first- and second-moment equations, and projector spectral conditions, for \(1\le a,r\le4\). Its completed execution reported `EXACT_PASS cases= 16 coordinate facet contacts= 100 transversal facet contacts= 494 all first/second John moments`. These finite checks detect algebraic errors but do not substitute for the proof for arbitrary \(a,r\). The asserted theorem uses only \(a\ge2\), \(r\ge3\); smaller values in the test are boundary calibrations.

## Relationship to prior work

The stable-set-polytope objects and their combinatorial traversal belong to established polyhedral combinatorics. In particular, Merino and Mütze treat stable-set polytopes among combinatorial \(0/1\)-polytopes; their results concern optimization-driven traversal rather than a Euclidean maximum-volume inscribed ellipsoid. Rodríguez-Heck and collaborators study stable-set linear-programming relaxations and their persistency, a different invariant. Classical John's theorem gives an optimality criterion, not this two-parameter center, spectrum, full contact structure, or explicit positive certificate without further calculation.

For complete bipartite graphs (two parts) there are related, previously derived inscribed-ellipsoid formulas. The present result restricts to \(r\ge3\) and establishes the three-eigenspace structure and simultaneous contact with all transversal cliques. The literature comparison does not constitute independent priority certification: an equivalent earlier formulation under free sums of cubes or optimal experimental design remains a possibility.

## Limitations

This is an exact result for balanced complete multipartite graphs and their canonical stable-set coordinates. Unequal part sizes, arbitrary graphs, other norms, and asymptotic optimality for unrelated polytopes are not addressed. Finite computer checks cannot establish the infinite-dimensional parameter statement; it is proved by the analytical John certificate above. Independent validation and a definitive literature-priority investigation have not been performed.

## References

1. A. Merino and T. Mütze, *Traversing combinatorial \(0/1\)-polytopes via optimization*, arXiv:2304.08567v1 (first publicly posted 2023-04-17), https://arxiv.org/abs/2304.08567. Primary subject: 52B05.
2. E. Rodríguez-Heck et al., *Persistency of Linear Programming Relaxations for the Stable Set Problem*, arXiv:1911.01478 (first publicly posted 2019-11-04), https://arxiv.org/abs/1911.01478.
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday* (1948), pp. 187–204. John's contact theorem is used as an established result.
