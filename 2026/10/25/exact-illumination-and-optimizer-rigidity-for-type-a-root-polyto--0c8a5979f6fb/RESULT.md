# Exact illumination and optimizer rigidity for type-\(A\) root polytopes

## Finding
For every integer \(m\ge3\), let
\[
H_m=\left\{x\in\mathbb R^m:\sum_{i=1}^m x_i=0\right\},\qquad
R_m=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le m\}\subset H_m.
\]
The ordinary illumination number and the finite weighted-direction fractional illumination number obey
\[
I(R_m)=I^*(R_m)=m.
\]
More precisely, each illuminating direction covers a directed star of at most \(m-1\) root vertices. A direction illuminates exactly \(m-1\) root vertices if and only if it has a unique strictly negative coordinate and all other coordinates strictly positive, or a unique strictly positive coordinate and all other coordinates strictly negative. These are respectively the full outgoing and incoming stars in the complete directed graph on \(m\) coordinate indices.

There is a complete description of every optimal fractional illumination family: after aggregating direction weights by their full-star vertex-incidence patterns, there exists one \(\theta\in[0,1]\) such that every outgoing star has weight \(\theta\) and every incoming star has weight \(1-\theta\). Conversely, each such aggregate assignment is optimal. Up to replacing directions by others with identical illuminated vertex sets, the only two optimal ordinary direction families consist of all \(m\) outgoing stars or all \(m\) incoming stars. Consequently, the aggregate optimal fractional solution space is the line segment joining two integral optimal coverings.

## Assumptions and scope
An illuminating direction lies in the affine-direction space \(H_m\). It illuminates \(x\in\partial R_m\) when \(x+tu\) lies in the relative interior of \(R_m\) for some \(t>0\). The fractional invariant is defined using **finite** families of directions with nonnegative real weights such that the total weight of directions illuminating each boundary point is at least one. Directions may be rescaled by positive numbers. A full-star *class* means the set of vertices a direction illuminates, not one prescribed vector. The boundary and interior are taken within the \((m-1)\)-dimensional affine hull \(H_m\).

Write \(\Delta_{m-1}=\operatorname{conv}\{e_1,\ldots,e_m\}\). Then \(R_m=\Delta_{m-1}-\Delta_{m-1}\), so affine invariance also gives the stated results for the difference body of any nondegenerate \((m-1)\)-simplex. The assertion does not concern the polar root polytope or the positive-root polytope.

## Proof
**1. Exact body and vertices.** One has
\[
R_m=\left\{x\in H_m:\sum_{k=1}^m |x_k|\le2\right\}.
\]
Indeed, convex combinations of roots satisfy both conditions. Conversely, if the positive coordinate mass \(T=\sum_k x_k^+\) is at most one, then \(x=T(y-z)\) with \(y,z\) probability vectors when \(T>0\). This is a convex combination of roots and the origin, which itself is a convex combination of roots. The case \(T=0\) is the origin. Each \(v_{ij}=e_i-e_j\), \(i\ne j\), is an exposed vertex, as witnessed by the functional \(x\mapsto x_i-x_j\). Thus the vertex set has exactly \(m(m-1)\) elements.

**2. Strict illumination test.** Fix a nonzero \(u\in H_m\). Set
\[
T=\sum_{k=1}^m(u_k)^+=\sum_{k=1}^m(-u_k)^+>0,\quad
a_i=(-u_i)^+,\quad b_j=(u_j)^+.
\]
For all sufficiently small \(t>0\),
\[
\|v_{ij}+tu\|_1=2+t\left(u_i-u_j+\sum_{k\ne i,j}|u_k|\right)
=2+2t(T-a_i-b_j).
\]
A segment from a boundary point to an interior point stays in the interior except at its initial endpoint. Accordingly, \(u\) illuminates \(v_{ij}\) if and only if this right derivative is strictly negative, namely
\[
a_i+b_j>T.\tag{1}
\]
If the derivative is zero, the point stays on the boundary for all sufficiently small positive \(t\), and convexity prevents a later interior entry along the same ray: the intersection of the ray with a convex body is an interval, and once inside it would already be inside at all earlier positive parameters. Condition (1) implies \(a_i>0\) and \(b_j>0\), so \(i\) is a strictly negative index of \(u\) and \(j\) a strictly positive one.

**3. The directed-star lemma.** If both \(v_{ij}\) and \(v_{k\ell}\) were illuminated with \(i\ne k\) and \(j\ne\ell\), then
\[
(a_i+b_j)+(a_k+b_\ell)>2T,
\]
whereas \(a_i+a_k\le T\) and \(b_j+b_\ell\le T\); a contradiction. The illuminated directed edges are edges of a bipartite graph (negative indices to positive indices) in which every pair of edges shares an endpoint. Such a nonempty bipartite graph is a star: if it contains two distinct edges with common source, any edge must meet both and therefore has the same source, and similarly for a common target. Therefore the number of illuminated roots is at most \(m-1\).

Suppose there are exactly \(m-1\) illuminated roots. A star has at most \(m-1\) opposite indices, so either there is one negative index and all remaining \(m-1\) indices are positive or the sign-reversed configuration. Conversely, with exactly one negative index \(i\), its mass is \(a_i=T\), and every positive coordinate \(j\ne i\) gives \(a_i+b_j>T\). The sign-reversed case gives the full incoming star. This proves the equality characterization.

**4. Sharp ordinary and fractional numbers.** Given any finite fractional illuminating family with weights \(w_h\), sum the vertex-coverage inequalities over all \(m(m-1)\) vertices. Step 3 yields
\[
m(m-1)\le\sum_h w_h\,\#\{v_{ij}:u_h\text{ illuminates }v_{ij}\}
\le(m-1)\sum_h w_h,
\]
so \(I^*(R_m)\ge m\). For each index \(i\), choose a direction with \(u_i=-(m-1)\) and \(u_j=1\) for \(j\ne i\). Its illuminated roots are exactly \(\{v_{ij}:j\ne i\}\). The \(m\) directions partition the vertices into illuminated sets. They also illuminate the entire boundary: every boundary point belongs to a face containing a vertex, and a direction strictly entering the body at that vertex strictly enters at each point of the same face because all the supporting facet inequalities active on the face are among those active at the vertex. With weight one on each direction, every boundary point receives weight at least one. Thus \(I(R_m)\le m\), proving both equalities.

**5. Classification of optimal families.** If a fractional family has total weight \(m\), equality in both inequalities of Step 4 forces every positive-weight direction to illuminate exactly \(m-1\) vertices and each root vertex to receive total weight exactly one. Aggregate the weights of full outgoing stars with center \(i\) as \(\alpha_i\), and incoming stars with center \(j\) as \(\beta_j\). The vertex constraints become exact equalities
\[
\alpha_i+\beta_j=1\qquad(i\ne j).\tag{2}
\]
For \(m\ge3\), any two source indices share a distinct possible target, so all \(\alpha_i\) coincide; likewise, all \(\beta_j\) coincide. Hence \(\alpha_i=\theta\) and \(\beta_j=1-\theta\), with \(0\le\theta\le1\). Conversely, for each \(\theta\) these assignments illuminate each root vertex with total weight exactly one and therefore every boundary point with weight at least one. This proves the full fractional optimizer claim. An ordinary optimal family has precisely \(m\) distinct directions of unit weight. In (2) its aggregate weights are integers, forcing \(\theta\in\{0,1\}\). The two advertised complete-star coverings follow.

## Verification
The accompanying self-contained standard-library script `verify.py` performs exact-integer tests of the vertex derivative condition on bounded direction grids for small dimensions. It checks the star restriction, the explicit full-star witnesses, and the exact vertex-coverage constraints for rational choices of \(\theta\). The proof above, not the finite tests, establishes the statements for all integers \(m\ge3\). The general case requires no external numerical certificate.

## Relationship to prior work
Gorodzha (2026) establishes the universal bound \(I^*(K)\le2^d\) and characterizes its parallelotope equality cases. The present result instead computes an exact value below that bound for the nonparallelotope simplex difference body, and determines *all* optimal fractional vertex-incidence patterns. Naszódi (2009) introduced the finite-direction fractional illumination invariant. Živaljević (2013) identifies the simplex difference body with the type-\(A\) root polytope and studies its polar through a topological illumination-complex construction; this is not the inward-direction illumination invariant used here. Ardila, Beck, Hosten, Pfeifle, and Seashore (2008) study triangulations, face data and growth series of root polytopes, not direction-covering optimizers. The planar \(m=3\) fractional value agrees with the existing equiangular-hexagon theorem, and the three-dimensional \(m=4\) ordinary value agrees with earlier cuboctahedron illumination calculations; these low-dimensional evaluations are treated as known special cases, not independent discoveries. Cartesian products of simplices and type-\(D\) root polytopes obey different tangent-cone incidence patterns and their illumination evaluations do not imply the all-dimensional star classification for type \(A\).

## Limitations
This statement is restricted to finite-dimensional simplex difference bodies in the affine subspace \(H_m\) and finite nonnegative fractional direction families. It does not assert corresponding formulas for arbitrary root polytopes, general centrally symmetric bodies, their polars, or alternative weighted costs assigned to point light sources. Searches and inspected primary papers found no prior exact type-\(A\) optimizer classification, but independent priority review has not been performed and differently indexed historical results remain a residual risk. The direction-level choice within each full-star class is not uniquely determined; rigidity concerns aggregate weights and vertex-incidence classes.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, first public September 20, 2026, https://arxiv.org/html/2609.23913.
2. M. Naszódi, *Fractional illumination of convex bodies*, 2009, https://doi.org/10.55016/ojs/cdm.v4i2.62022.
3. R. Živaljević, *Illumination complexes, Δ-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138v1, 2013, https://arxiv.org/html/1307.5138v1.
4. F. Ardila, M. Beck, S. Hosten, J. Pfeifle, and K. Seashore, *Root polytopes and growth series of root lattices*, 2008, https://fardila.com/Articles/rootpolytopes.pdf.
