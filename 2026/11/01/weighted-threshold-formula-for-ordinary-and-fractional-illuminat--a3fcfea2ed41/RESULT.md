# Weighted threshold formula for ordinary and fractional illumination of capped cubes

## Finding

Fix an integer \(d\ge 2\), positive real weights \(a_1,\ldots,a_d\), and \(T>0\). Define the full-dimensional convex polytope
\[
Q(a,T)=\left\{x\in[-1,1]^d:\ \sum_{i=1}^d\frac{a_i(x_i+1)}2\le T\right\}.
\]
For a subset \(S\subseteq[d]=\{1,\ldots,d\}\), write \(a(S)=\sum_{i\in S}a_i\), with \(a(\varnothing)=0\). Let \(I(Q)\) be its classical directional illumination number, and let \(I^*(Q)\) be its fractional illumination number, defined using nonnegative weights on finitely many illuminating directions.

**Theorem.** For every choice of the stated parameters, including every threshold equal to a subset sum,
\[
\boxed{\ I(Q(a,T))=I^*(Q(a,T))
=d+1+\#\{S\subseteq[d]:|S|\ge2,\ a(S)\le T\}.\ }
\]
In particular, the two illumination numbers coincide, and the only jumps as \(T\) increases occur when an entire subset of at least two weights becomes feasible. A subset of size one does not cause a jump: its newly retained cube vertex replaces an illuminating direction previously required at a cut-edge vertex.

Equivalently, if \(V(T)=\{S\subseteq[d]:a(S)\le T\}\) and \(J(T)=\{i:a_i>T\}\), then
\[
I(Q(a,T))=I^*(Q(a,T))=|V(T)|+|J(T)|.
\]
For \(T\ge\sum_i a_i\), the body is the uncut cube and the formula gives \(2^d\).

For equal weights \(a_i=1\), the result becomes the exact binomial staircase
\[
I(Q(\mathbf1,T))=I^*(Q(\mathbf1,T))
=d+1+\sum_{j=2}^{\min(d,\lfloor T\rfloor)}\binom dj,
\qquad T>0,
\]
where an empty sum is zero. For example, the three-dimensional family has values \(4\) for \(0<T<2\), \(7\) for \(2\le T<3\), and \(8\) for \(T\ge3\).

Weighted cuts behave differently. For \(d=3\), weights \((3,1,1)\), and \(T=5/2\), the polytope retains only four original cube vertices yet has illumination number \(5\): one additional direction is forced by the unique cut edge leaving the all-negative cube vertex in the first coordinate. This is a genuine obstruction not detected by merely counting retained vertices.

## Assumptions and scope

An illumination direction is a nonzero vector \(u\) such that for a boundary point \(x\), the point \(x+\varepsilon u\) lies in \(\operatorname{int}Q\) for all sufficiently small \(\varepsilon>0\). A finite family of directions illuminates \(Q\) when every boundary point is illuminated by one member. The number \(I(Q)\) is the minimum cardinality of such a family. The fractional number \(I^*(Q)\) is the infimum of \(\sum_j w_j\) over finite families of directions with nonnegative weights \(w_j\), where the sum of weights of directions illuminating every boundary point is at least one. Normalizing directions to unit length does not affect illumination.

All weights must be strictly positive; no rationality, generic-position, or distinct-subset-sum assumption is made. Every \(T>0\) gives a convex body with interior. The statement is invariant under nonsingular affine transformations of the whole configuration, but no arbitrary non-diagonal truncation is asserted.

## Proof

Put \(A=\sum_i a_i\). The cutting inequality is \(a\cdot x\le2T-A\). For every \(S\subseteq[d]\), let \(v_S\) be the cube vertex whose coordinates equal \(+1\) on \(S\) and \(-1\) outside \(S\). Its weighted height is \(a(S)\); hence \(v_S\in Q\) if and only if \(S\in V(T)\). These retained cube vertices have all their \(d\) coordinate-facet inequalities active. Any direction illuminating \(v_S\) therefore lies in the strict sign orthant
\[
\mathcal O_S=\{u:u_i<0\text{ for }i\in S,\ u_i>0\text{ for }i\notin S\}.
\]
The orthants \(\mathcal O_S\) are pairwise disjoint. Thus \(I^*(Q)\ge |V(T)|\), and the same lower bound holds for ordinary illumination.

There are further unavoidable directions. For every index \(i\in J(T)\), the cube edge from \(v_\varnothing=(-1,\ldots,-1)\) toward \(v_{\{i\}}\) is cut in its relative interior at
\[
p_i=(-1,\ldots,-1,\,-1+2T/a_i,\,-1,\ldots,-1).
\]
The point \(p_i\) is a vertex of \(Q\): the cutting hyperplane and the \(d-1\) fixed coordinate facets have linearly independent normals. Any direction \(u\) illuminating \(p_i\) must satisfy \(u_j>0\) for all \(j\ne i\) and \(a\cdot u<0\). Since every weight is positive, \(u_i<0\). These additional open illumination cones are pairwise disjoint for distinct \(i\in J(T)\). Moreover, no retained set \(S\) can contain \(i\in J(T)\), since \(a(S)\ge a_i>T\). Thus every direction illuminating a retained cube vertex has \(u_i>0\), whereas every direction illuminating \(p_i\) has \(u_i<0\). All \(|V(T)|+|J(T)|\) required vertex-cones are pairwise disjoint.

A weighted illumination must allocate total weight at least one to each of these disjoint cones. Therefore
\[
I^*(Q)\ge |V(T)|+|J(T)|,
\qquad I(Q)\ge |V(T)|+|J(T)|.
\]

We construct exactly this many directions. For the retained vertex \(v_\varnothing\), select \(u^\varnothing=(1,\ldots,1)\); the cut inequality is strict there because \(T>0\). For each nonempty \(S\in V(T)\), choose any index \(r\in S\) and define
\[
u^S_r=-2A/a_r,\qquad
u^S_j=\begin{cases}-1,&j\in S\setminus\{r\},\\+1,&j\notin S.\end{cases}
\]
Every coordinate moves strictly inward at \(v_S\), and \(a\cdot u^S<0\), so this direction illuminates \(v_S\), including when its weighted height equals \(T\).

For each \(i\in J(T)\), add the direction \(w^i\) whose \(i\)-th component is \(-2A/a_i\) and whose remaining components are all \(+1\). Then \(a\cdot w^i<0\), and \(w^i\) strictly enters through every facet active at \(p_i\).

It remains to verify that every other vertex is illuminated. For a cube intersected with one halfspace, each vertex is either a retained cube vertex or the intersection of the cutting hyperplane with a cube edge joining a retained and a removed cube vertex. Indeed, a new vertex in the relative interior of a face of dimension at least two would lie in a positive-dimensional intersection of that face with the hyperplane. Since every \(a_i>0\), the hyperplane contains no cube edge, and no extra vertex type arises.

The orientation of any crossing edge is from \(v_S\) with \(a(S)<T\) toward \(v_{S\cup\{i\}}\) with \(a(S)+a_i>T\), where \(i\notin S\). Its new vertex has precisely the \(d-1\) coordinate facets fixed by \(v_S\) outside coordinate \(i\), together with the cutting facet, active. If \(S\ne\varnothing\), the direction \(u^S\) strictly enters through every one of those facets: the coordinate directions have signs opposite the fixed coordinates, and \(a\cdot u^S<0\). If \(S=\varnothing\), the cut edge exists exactly when \(a_i>T\), and \(w^i\) enters through its active facets.

Thus every vertex is illuminated by the listed \(|V(T)|+|J(T)|\) directions. A direction that strictly enters through all facets at a vertex of a polytope also illuminates every boundary point in the relative interior of a face containing that vertex. Therefore illuminating all vertices illuminates the entire boundary. We conclude
\[
I(Q)\le |V(T)|+|J(T)|.
\]
Combining the lower and upper bounds and \(I^*(Q)\le I(Q)\) proves both equalities. Finally,
\[
|V(T)|=1+\#\{i:a_i\le T\}
+\#\{S:|S|\ge2,\ a(S)\le T\},
\]
while \(|J(T)|=d-\#\{i:a_i\le T\}\). This yields the boxed threshold formula. The cancellation remains exact at all tied subset sums. \(\square\)

## Verification

The standalone pure-Python file `verify.py` uses rational arithmetic to generate all retained cube vertices and cut-edge intersection vertices, construct the displayed directions, and verify the strict active-facet illumination inequalities. It checks that the predicted lower-bound witness cones are incompatible with the constructed old-vertex directions. Selected small-dimensional instances also receive an independent exact active-facet vertex enumeration by Gaussian elimination rather than using the cut-edge formula.

Actual execution returned: `VERIFY_OK weighted cube-cap illumination: 354 exact parameter systems; 15035 checks`.

The finite tests do not certify the universal statement. Its proof for arbitrary dimension, positive real weights, and all thresholds (including ties) is the geometric argument above. The checker requires only Python's standard library and is run with `python3 verify.py`.

## Relationship to prior work

Livshyts and Tikhomirov proved that the cube is a strict local maximizer for illumination and gave a one-corner example requiring exactly \(2^d-1\) directions. An earlier published independent-corner truncation construction computes the values \(2^d-|R|\) for shallow cuts at any independent set of cube corners \(R\). Neither result implies the full depth- and weight-dependent law for a **single** cutting hyperplane, nor the correction from cut edges adjacent to the bottom vertex.

Ivanov's 2026 work proves the illumination conjecture for primitive polytopes, without evaluating the present family for arbitrary weights and thresholds. The theorem of Gorodzha (2026) gives the universal fractional upper bound \(I^*(K)\le2^d\) with equality only for parallelotopes, rather than the exact fractional values and their integer equality here. Naszódi introduced the fractional invariant in 2009. These developments motivate the search for exact non-symmetric examples for both invariants.

In the new family, the obstruction cones have a particularly transparent Boolean-lattice interpretation: every retained cube vertex contributes one, and each absent singleton contributes a separate cone, so singleton thresholds cancel and higher subset thresholds contribute precisely one. This classification is not a consequence of the above broad upper bounds. A previously unindexed or differently named formula for clipped boxes remains a historical-priority possibility.

## Limitations

The result is specific to the intersection of a cube with **one** halfspace having strictly positive coefficients after coordinate sign changes. It does not classify simultaneous cuts, arbitrary polyhedral perturbations, quantitative illumination costs, or complex illumination. For general real weights, the answer is given by a subset-sum count, not claimed to be computable in polynomial time as the dimension varies. Independent mathematical audit and exhaustive historical-priority verification have not been performed.

## References

1. I. Ivanov, *Illuminating Primitive Polytopes*, arXiv:2607.08944, first publicly submitted 2026-07-09.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913, first publicly submitted 2026-09-20.
3. G. Livshyts and K. Tikhomirov, *Cube is a Strict Local Maximizer for the Illumination Number*, arXiv:1710.05070, first submitted 2017-10-13; Discrete & Computational Geometry 63 (2020), 209–228.
4. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), DOI 10.55016/ojs/cdm.v4i2.62022.
5. *Independent corner truncations realize the high illumination spectrum near the cube*, publicly accessible mathematical research record (2026), theorem and proof.
