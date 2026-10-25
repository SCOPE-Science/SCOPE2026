# Four-light illumination and a sharp directional transition in polar tetrahedral truncations

## Finding

Let \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), and \(v_3=(-1,-1,1)\). For every real \(\lambda>0\), define the three-dimensional convex polytope
\[
P_\lambda=\operatorname{conv}\{v_0,v_1,v_2,v_3,-\lambda v_0,-\lambda v_1,-\lambda v_2,-\lambda v_3\}.
\]
For ordinary illumination number \(I\) and finite fractional illumination number \(I^*\), the complete parameter classification is
\[
I(P_\lambda)=I^*(P_\lambda)=\begin{cases}8,&\lambda=1,\\4,&\lambda\ne1.\end{cases}
\]
Here a direction illuminates a boundary point if a short positive displacement in that direction enters the polytope's interior. Fractional illumination assigns nonnegative weights to finitely many directions, requiring total illuminating weight at least one at every boundary point.

The maximum \(\alpha(P_\lambda)\) of the number of distinct **vertices** simultaneously illuminated by one direction has the separate, sharp profile
\[
\alpha(P_\lambda)=\begin{cases}
1,&0<\lambda\le1/3\text{ or }\lambda=1\text{ or }\lambda\ge3,\\
4,&1/3<\lambda<1/2\text{ or }2<\lambda<3,\\
3,&1/2\le\lambda<1\text{ or }1<\lambda\le2.
\end{cases}
\]
In particular, for every nondegenerate regular tetrahedron truncated uniformly by a fraction \(0<t<1/2\) of each edge, its polar has both illumination numbers equal to four. At the rectified endpoint \(t=1/2\), the polar is a cube and both values jump to eight. On the proper-truncation interval, the maximum simultaneously illuminated vertex count is four for \(0<t<1/4\) and three for \(1/4\le t<1/2\); the polar of the Archimedean regular truncated tetrahedron \(t=1/3\) has maximum three.

## Assumptions and scope

All polars are taken in the three-dimensional affine span translated to the origin. The parameter \(\lambda\) is positive, and the four base vectors are exactly those displayed above; affine images have the same illumination invariants. The count \(\alpha\) refers only to the vertices actually extreme at that parameter, not to redundant points in the convex-hull generating set. The fractional infimum uses finite weighted families of directions, not a probabilistic convention. For a polytope, illuminating all vertices (respectively covering each vertex by weight at least one) suffices for illuminating its full boundary (respectively weighted covering): every facet active at a face point is active at any vertex of that face.

For a tetrahedron in barycentric coordinates \(x_i\ge0\), \(\sum_{i=0}^3x_i=1\), uniform corner truncation at depth \(t\) has inequalities \(x_i\le1-t\). Centering at \((1/4,1/4,1/4,1/4)\), polarizing in the zero-sum hyperplane, and applying a common positive scale produces \(P_{3-4t}\). Thus the named geometric family is exactly a subinterval of the analytic one.

## Proof

**1. The outer parameter intervals.** The vectors satisfy \(\sum_i v_i=0\) and \(v_i\cdot v_j=4\delta_{ij}-1\). When \(\lambda\ge3\), every \(v_i\) belongs to the simplex \(\operatorname{conv}\{-\lambda v_j:0\le j\le3\}\): its barycentric coefficients are \((1-3/\lambda)/4\) at index \(i\) and \((1+1/\lambda)/4\) at each other index. Therefore \(P_\lambda\) is precisely that simplex. By \(P_\lambda=-\lambda P_{1/\lambda}\), the same conclusion holds for \(0<\lambda\le1/3\). Each direction illuminates at most one simplex vertex, and four directions suffice, giving both illumination numbers four and \(\alpha=1\).

For \(\lambda=1\), the generating vertices are exactly the eight vertices of \([-1,1]^3\). Two distinct cube vertices require contradictory strict signs in some coordinate of an illuminating direction, so each direction illuminates at most one vertex. Eight directions are necessary and sufficient, even fractionally; \(\alpha=1\).

**2. Exact facets for the interior range.** By the reciprocal symmetry it remains to treat \(1<\lambda<3\). Write \(t_i=u\cdot v_i\) for a direction \(u\); then \(\sum_i t_i=0\), and every zero-sum quadruple \((t_i)\) is obtained uniquely from \(u=(1/4)\sum_i t_i v_i\).

There are exactly twelve triangular facets, indexed by an ordered pair \((i,l)\) with \(i\ne l\). Facet \((i,l)\) contains \(+v_i\) and the two vertices \(-\lambda v_j,-\lambda v_k\), where \(\{i,l,j,k\}=\{0,1,2,3\}\). Its outward normal \(n_{i,l}\), normalized so the supporting value is one, is uniquely determined by
\[
n_{i,l}\cdot v_i=1,\quad n_{i,l}\cdot v_j=n_{i,l}\cdot v_k=-1/\lambda,\quad n_{i,l}\cdot v_l=2/\lambda-1.
\]
Every other generating vertex has support value strictly below one: the values at \(+v_j,+v_k,+v_l\) are \(-1/\lambda,-1/\lambda,2/\lambda-1\), and those at \(-\lambda v_i,-\lambda v_l\) are \(-\lambda,\lambda-2\). Thus each indicated triangle is a genuine facet. All eight generating points are extreme, and a three-polytope with eight vertices has at most twelve facets, proving completeness.

Put \(s=(3-\lambda)/(1+\lambda)\in(0,1)\). Substitution into the normals yields \(u\cdot n_{i,l}\) as a positive multiple of \(t_i+s t_l\). Consequently the *strict* vertex-illumination criteria are
\[
+v_i\text{ lit }\Longleftrightarrow t_i+s t_l<0\quad(\forall l\ne i),
\]
\[
-\lambda v_i\text{ lit }\Longleftrightarrow t_p+s t_l<0\quad(\forall p\ne l\text{ in }\{0,1,2,3\}\setminus\{i\}).
\]
No unverified numerical generalization is used in these criteria.

**3. Fractional lower bound.** No direction can illuminate two vertices from the negative orbit. Indeed, summing the six inequalities for \(-\lambda v_i\) gives \(t_i>0\). If two distinct negative-orbit vertices \(i,j\) were illuminated, writing \(\{k,h\}=\{0,1,2,3\}\setminus\{i,j\}\), the two inequalities with first index \(j\) and second index \(k,h\) give \((2-s)t_j<s t_i\); exchanging \(i,j\) gives \((2-s)t_i<s t_j\). As both variables are positive and \(2-s>s\), this is impossible. Every finite fractional cover must devote aggregate weight at least four to cover the four negative-orbit vertices, so \(I^*(P_\lambda)\ge4\), and hence \(I(P_\lambda)\ge4\).

**4. Uniform four-direction covering.** For any \(s\in(0,1)\), define
\[
\delta=\frac12\min\left\{s,\frac{(1-s)^2}{s}\right\},\qquad A=2-s+\delta,\qquad C=s-\delta.
\]
Then \(0<C<s\), \(A<1/s\), and \(A+C=2\). For each \(i\) modulo four, take the unique direction with transformed coordinates
\[
t_i=A,\qquad t_{i+1}=C,\qquad t_{i+2}=t_{i+3}=-1.
\]
The facet criteria show that it illuminates \(-\lambda v_i\) and both \(+v_{i+2}\), \(+v_{i+3}\). In detail, the potentially tight negative-orbit inequality is \(C-s=-\delta<0\); the potentially tight positive-orbit inequality is \(-1+sA<0\). The other inequalities are strict because \(0<C<s<1\). Over the four cyclic values of \(i\), every one of the eight vertices is illuminated. Thus \(I(P_\lambda)\le4\). Combined with step 3, \(I=I^*=4\).

**5. Sharp single-direction capacity.** By step 3, at most one negative-orbit vertex can be illuminated. If three positive-orbit vertices were illuminated, add the two cross-inequalities for each pair of these three to conclude that their sum is negative; hence the fourth transformed coordinate, \(T\), is positive. Each of the three illuminated vertices then satisfies \(t_i+sT<0\). Adding these gives \((3s-1)T<0\), which is impossible for \(s\ge1/3\). Therefore at most three total vertices are illuminated in that range; the explicit rays from step 4 achieve three. When \(0<s<1/3\), the direction with \((t_0,t_1,t_2,t_3)=(3,-1,-1,-1)\) illuminates the negative vertex at index zero and all three positive vertices at the other indices. Four is also the trivial upper bound from the one-negative-orbit restriction. Thus \(\alpha=3\) for \(1<\lambda\le2\) and \(\alpha=4\) for \(2<\lambda<3\). Reciprocal symmetry supplies the other intervals. The cases from step 1 finish the classification.

## Verification

The accompanying `verify.py` uses only Python's exact `fractions.Fraction`. It reconstructs the twelve rational supporting planes and their three-vertex contact sets for nine rational parameters; cross-checks the inequalities against actual Euclidean facet normals on 36 explicitly constructed directions; verifies the cyclic four-direction covering; checks the cube and simplex endpoint descriptions; and tests finite integer profiles separately from the general proof. Run `python verify.py` from the artifact directory. The exact construction, rather than finite integer-profile enumeration, proves the continuous-parameter statements. In particular, near \(\lambda=1\) optimal directions may require large coordinate ratios, so a bounded direction grid does not constitute a completeness proof.

## Relationship to prior work

Fractional illumination is a standard weighted form of geometric illumination. Gorodzha (arXiv:2609.23913, first public September 20, 2026) proves the universal bound \(I^*(K)\le2^d\) and characterizes equality by parallelotopes. That theorem explains the distinguished cube endpoint but does not give the exact value four on its neighboring, nonparallelotopal family or the sharp directional transition. Livshyts and Tikhomirov (arXiv:1710.05070) give a general upper bound of seven for sufficiently small nonparallelotopal perturbations of a three-dimensional cube; it does not imply the present exact four-direction cover. Recent exact illumination studies of cube–octahedron intersections and of independent cube-corner truncations concern different vertex/facet configurations and do not supply this polar tetrahedral-truncation classification. The stated contribution is the complete two-orbit family evaluation and exact vertex-capacity threshold, not a general new illumination bound.

## Limitations

The analysis is specific to the one-parameter family with full tetrahedral symmetry; it does not determine illumination for arbitrary deformations of the triakis tetrahedron or all Catalan solids. The maximum \(\alpha\) is a single-direction count of vertices, not an independent covering invariant. Earlier work may contain an equivalent result under alternate language for homothetic tetrahedra, and historical priority has not been independently certified. The combinatorial diagram changes at the degenerate parameters \(\lambda=1/3,1,3\), which are explicitly treated rather than silently extrapolated.

## References

- Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913, first posted 2026-09-20. https://arxiv.org/abs/2609.23913
- G. Livshyts and K. Tikhomirov, *Cube is a strict local maximizer for the illumination number*, arXiv:1710.05070, first posted 2017-10-13. https://arxiv.org/abs/1710.05070
- A. Naszódi, *Fractional illumination of convex bodies*, 2009, referenced in arXiv:2609.23913, Introduction.
