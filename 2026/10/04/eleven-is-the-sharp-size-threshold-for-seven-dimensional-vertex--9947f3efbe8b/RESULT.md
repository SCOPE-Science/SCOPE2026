# Eleven is the sharp size threshold for seven-dimensional vertex-facet assignment obstructions

## Finding

A vertex-facet assignment of a polytope is a matching of non-incident vertex-facet pairs that covers all vertices or all facets.

For every seven-dimensional convex polytope \\(P\\) without a vertex-facet assignment,
\[
f_0(P)\ge 11
\qquad\text{and}\qquad
f_6(P)\ge 11.
\]
Both inequalities are sharp simultaneously.

Let \\(T\\) be a triangular prism and let \\(T^\\Delta\\) be its dual triangular bipyramid. Their free join
\[
J=T\bowtie T^\Delta
\]
is a self-dual seven-dimensional polytope with
\[
f_0(J)=f_6(J)=11,
\]
and \\(J\\) has no vertex-facet assignment. Consequently, the smallest possible vertex/facet pair of a seven-dimensional obstruction is exactly
\[
(11,11).
\]

## Assumptions and scope

All polytopes are finite-dimensional convex polytopes. For a face \\(F\\) of a \\(d\\)-polytope, \\(F^\\Delta\\) denotes its dual face, whose vertices correspond to the facets of the ambient polytope containing \\(F\\). Thus
\[
\dim F+\dim F^\Delta=d-1.
\]

The statement concerns the combinatorial vertex-facet assignment property. It does not classify all seven-dimensional counterexamples and does not assert reducedness or non-reducedness for every realization of a combinatorial type.

## Proof

Jahn and Winter prove that if, for every face \\(F\\), at least one of \\(F\\) and \\(F^\\Delta\\) has at least as many facets as vertices, then the ambient polytope has a vertex-facet assignment. Therefore, if a seven-polytope \\(P\\) has no assignment, there is a face \\(F\\) for which both \\(F\\) and \\(F^\\Delta\\) have strictly more vertices than facets.

A polytope of dimension at most two has equally many vertices and facets. Since
\[
\dim F+\dim F^\Delta=6,
\]
both dimensions must therefore be at least three, hence
\[
\dim F=\dim F^\Delta=3.
\]

We first note that a three-polytope with strictly more vertices than facets has at least six vertices. If it has \\(v\\) vertices, \\(e\\) edges and \\(f\\) facets, then every vertex has degree at least three, so
\[
2e\ge3v.
\]
Euler's formula gives
\[
f=2-v+e\ge 2+\frac v2.
\]
For \\(v=4\\) or \\(v=5\\), integrality yields \\(f\\ge v\\). Hence strict vertex excess first becomes possible at \\(v=6\\), and the triangular prism realizes \\((v,f)=(6,5)\\).

Thus
\[
f_0(F)\ge6,
\qquad
f_0(F^\Delta)\ge6.
\]
Because \\(F\\) has dimension three inside a seven-polytope, at least four vertices of \\(P\\) lie outside \\(F\\): each additional vertex can increase the affine span by at most one dimension. Hence
\[
f_0(P)\ge10.
\]

It remains to rule out equality. Suppose \\(f_0(P)=10\\). Then necessarily \\(F\\) has exactly six vertices and exactly four vertices lie outside \\(F\\). Equality in the affine-dimension count forces those four outside vertices to be affinely independent modulo \\(\operatorname{aff}F\\); equivalently, their convex hull is a tetrahedron in an affine subspace skew to \\(\operatorname{aff}F\\), and
\[
P=F\bowtie\Delta_3.
\]
In a free join \\(F\\bowtie\\Delta_3\\), the facets containing the whole factor \\(F\\) are exactly
\[
F\bowtie G,
\]
where \\(G\\) runs through the four facets of the tetrahedron. Thus \\(F\\) is contained in exactly four facets of \\(P\\), so
\[
f_0(F^\Delta)=4,
\]
contradicting \\(f_0(F^\\Delta)\\ge6\\). Therefore
\[
f_0(P)\ge11.
\]

The vertex-facet assignment property is invariant under duality. Applying the same argument to \\(P^\\Delta\\) gives
\[
f_6(P)=f_0(P^\Delta)\ge11.
\]

For sharpness, let \\(T\\) be a triangular prism. It has six vertices and five facets, while its dual \\(T^\\Delta\\) has five vertices and six facets. The free join
\[
J=T\bowtie T^\Delta
\]
has dimension \\(3+3+1=7\\), eleven vertices, and eleven facets. The copy of \\(T\\) inside \\(J\\) has six vertices and is contained in the six facets indexed by facets of \\(T^\\Delta\\). Jahn--Winter's exact face criterion therefore gives
\[
6+6=12>11,
\]
so \\(J\\) has no vertex-facet assignment. Finally, duality interchanges the two join factors, so \\(J\\) is self-dual.

## Verification

The proof uses only Euler's formula, the minimum degree bound for three-polytopes, affine dimension counting, the elementary face structure of a free join, and Jahn--Winter's published assignment criteria.

The packaged `verify.py` checks the low-vertex Euler arithmetic, the prism/bipyramid face counts, the free-join dimension and vertex/facet totals, the numerical Hall-face violation, and the arithmetic contradiction at a hypothetical ten-vertex equality case. Its replay output is:

`VERIFY_OK sharp d7 vertex-facet obstruction threshold`

The checker is a consistency test for the finite arithmetic. The general lower bound itself is proved by the structural argument above.

## Relationship to prior work

Jahn and Winter characterize vertex-facet assignments by a face inequality, prove a convenient sufficient criterion, show that every polytope of dimension at most six admits an assignment, and construct counterexamples in every dimension at least seven by free joins. Their displayed seven-dimensional template uses a three-cube and a three-dimensional cross-polytope, which produces fourteen vertices and fourteen facets. They ask more generally about the nature of further seven-dimensional counterexamples.

The same paper states neither an eleven-vertex example nor a lower bound on the size of a seven-dimensional counterexample. The triangular-prism/triangular-bipyramid join is the smallest free-join witness because six is the smallest vertex count of a three-polytope with more vertices than facets, while the lower-bound argument shows that no non-free-join construction can do better in total vertex or facet count.

Targeted searches for the exact assignment terminology together with `11 vertices`, `triangular prism`, `bipyramid`, `smallest`, `minimal seven-dimensional counterexample`, and Hall-deficiency formulations did not locate a prior statement of this sharp threshold.

## Limitations

The result determines the smallest possible numbers of vertices and facets, not the complete combinatorial classification of eleven-by-eleven counterexamples. In particular, it does not resolve whether every size-minimal obstruction is a free join or whether non-free-join counterexamples occur at the same size.

The originality search found no covering statement, but a short extremal consequence of a known criterion can exist under different terminology or in unindexed notes; that remains a residual risk.

## References

T. Jahn and M. Winter, “Vertex-Facet Assignments For Polytopes,” arXiv:1812.08640, first submitted 2018-12-20; Beiträge zur Algebra und Geometrie 62 (2021), 55–63, DOI 10.1007/s13366-020-00504-9.

G. Ziegler, *Lectures on Polytopes*, Graduate Texts in Mathematics 152, Springer, 1995.
