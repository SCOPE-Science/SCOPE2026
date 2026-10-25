# Partwise-symmetric orbit spaces of higher independence complexes

## Finding

Let \(G=K_{m_1,\ldots,m_s}\) be any finite complete multipartite graph with \(s\ge2\) nonempty independent parts \(B_i\), of sizes \(m_i\ge1\). For every integer \(r\ge1\), let \(X=\operatorname{Ind}_r(G)\) denote the simplicial complex of vertex sets whose induced connected components have at most \(r\) vertices. Let \(H=\prod_{i=1}^{s}\mathfrak S_{B_i}\) act on \(X\) by independent permutations within the parts.

There is an explicit PL model for the ordinary **geometric orbit space** \(|X|/H\) that simplicially strongly collapses to the \((r-1)\)-skeleton of the simplex on the \(s\) parts (interpreted as the full simplex if \(r\ge s\)). Consequently,

\[
|\operatorname{Ind}_r(K_{m_1,\ldots,m_s})|/H\simeq
\begin{cases}
\displaystyle\bigvee^{\binom{s-1}{r}}S^{r-1},&1\le r<s,\\
\mathrm{pt},&r\ge s.
\end{cases}
\]

In particular, **the integral homotopy type of the orbit space is independent of all part sizes**, even though the homotopy type of the original complex generally varies with those sizes.

## Assumptions and scope

All graphs, simplicial complexes, and permutation groups here are finite. Each part is nonempty; the case \(s=1\) is excluded from the claimed uniform formula because the graph then has no edges, although its quotient is separately contractible. The notation \(|X|/H\) means the quotient of the ordinary geometric realization by the finite group, **not** a homotopy-orbit or Borel construction. A wedge of zero spheres is interpreted as a point; a wedge of \(q\) copies of \(S^0\) consists of \(q+1\) points.

For the explicit model, introduce vertices \(u_{i,j}\) for \(1\le i\le s\), \(1\le j\le m_i\). Define a simplicial complex \(L\) with a face \(F\) exactly if either all vertices of \(F\) have the same first index, or
\[
\sum_{i:F\cap\{u_{i,j}\}_j\ne\varnothing}
\max\{j:u_{i,j}\in F\}\le r.
\]
The empty face is admitted. The theorem asserts a concrete PL homeomorphism \(|X|/H\cong|L|\), followed by an explicit sequence of strong simplicial collapses \(L\searrow\operatorname{sk}_{r-1}\Delta^{s-1}\).

## Proof

**1. Faces of the higher independence complex.** If a vertex set intersects only one independent part, the induced graph has isolated vertices. If it intersects at least two parts, the induced complete multipartite subgraph is connected. Hence a subset is a face of \(X\) if and only if it is supported in one part or has total cardinality at most \(r\). This applies also to the empty set and every singleton.

**2. A canonical chamber for the quotient.** Represent points of \(|X|\) by barycentric coordinates \(w_{i,k}\ge0\) summing to one, with indices \(1\le k\le m_i\). The group \(H\) permutes the coordinates within each part. Sorting each part's coordinates in nonincreasing order defines a continuous orbit-invariant map, with exactly one sorted representative for every \(H\)-orbit. Its image \(C\) is compact. The induced continuous bijection from compact \(|X|/H\) onto Hausdorff \(C\) is a homeomorphism. Coordinate sorting is piecewise linear on the usual finite braid subdivision.

For a sorted coordinate vector, put \(w_{i,m_i+1}=0\) and define new barycentric coordinates
\[
t_{i,j}=j(w_{i,j}-w_{i,j+1}),\qquad
w_{i,k}=\sum_{j=k}^{m_i}\frac{t_{i,j}}{j}.
\]
Every \(t_{i,j}\) is nonnegative, the displayed equations are mutually inverse, and \(\sum_{i,j}t_{i,j}=\sum_{i,k}w_{i,k}=1\). This linear coordinate change identifies the full sorted chamber with a standard simplex on the vertices \(u_{i,j}\).

**3. Exact support comparison.** In each part \(i\), the number of *strictly positive* sorted coordinates \(w_{i,k}\) equals the largest tier index \(j\) having \(t_{i,j}>0\), or zero if all its tier coordinates vanish. Indeed, \(w_{i,k}=\sum_{j\ge k}t_{i,j}/j\). By Step 1, a point lies in \(|X|\) precisely when its positive coordinates occur in one part or their total number is at most \(r\). Under the linear change this is exactly the stated face condition for \(L\). We therefore obtain the homeomorphism \(|X|/H\cong|L|\), piecewise linear in the natural quotient triangulation.

**4. Strong collapses.** For every part \(i\) and tier \(j\ge2\), whenever a face \(F\) of \(L\) contains \(u_{i,j}\), the face \(F\cup\{u_{i,1}\}\) is also present. Adding the first-tier vertex changes neither the set of active parts nor the maximum tier index in any part. Thus \(u_{i,j}\) is dominated by \(u_{i,1}\), and can be strongly collapsed away. Perform these deletions for every tier \(j\ge2\). At the end, the only vertices are \(u_{i,1}\) for \(i=1,\ldots,s\), and a set of them is a face precisely when its cardinality is at most \(r\). The remaining complex is \(\operatorname{sk}_{r-1}\Delta^{s-1}\) (or the whole simplex for \(r\ge s\)). Each strong collapse is a homotopy equivalence and yields an ordinary simplicial collapse after suitable elementary face pairings.

**5. Sphere multiplicities.** If \(1\le r<s\), the standard elementary matching that toggles the first vertex of \(\operatorname{sk}_{r-1}\Delta^{s-1}\) leaves precisely \(\binom{s-1}{r}\) critical \((r-1)\)-faces and a base vertex. Its acyclicity follows because each matched pair changes only membership of that first vertex. For \(r=1\), this says the skeleton is \(s\) discrete points; for \(r\ge2\), it yields the claimed wedge of \((r-1)\)-spheres. If \(r\ge s\), the whole simplex is contractible.

## Verification

The accompanying standalone Python program `verify.py` independently builds each original induced graph, finds connected components by graph traversal, enumerates allowed original faces, builds the tier complex, checks each dominated-vertex coface condition, computes full reduced mod-two simplicial Betti vectors and evaluates signed permutation traces averaged over all within-part permutations. It checks \(203\) parameter configurations, including up to four parts, and reports `VERIFY_OK`.

These exact finite tests verify instances of the face criterion, collapse and predicted rational invariant ranks, but are **not** the general proof; Steps 1–5 prove the theorem for every stated parameter.

For example, \(\operatorname{Ind}_2(K_{3,3,3})\) has the previously known nonequivariant homotopy type of a wedge of \(25\) circles. Its ordinary quotient by \(\mathfrak S_3^3\) is instead a single circle.

## Relationship to prior work

Deshpande and Singh, Theorem 3.5 of [1], classify the **nonequivariant** homotopy types of higher independence complexes of complete multipartite graphs, with \(\binom{\sum_i m_i-1}{r}-\sum_i\binom{m_i-1}{r}\) sphere summands. Their result neither asserts a homeomorphism of the geometric group quotient to a tier complex nor supplies the strong-collapse classification independent of part sizes. The present theorem does not claim that nonequivariant result as new.

Sawant [2] establishes vertex decomposability for the higher independence complexes of trees. Deshpande, Goyal and Sawant [3] study forbidden-path complexes of complete multipartite graphs, including objects that intersect this family at one threshold. These statements concern different properties; no priority assertion is made from their abstracts alone. The complete full text of [3] was not accessible for a definitive comparison, and that bibliographic risk remains.

## Limitations

This identifies the ordinary quotient only for the full group of independent within-part permutations, not for arbitrary subgroups or permutations exchanging parts. It does not determine the homotopy types of homotopy-orbit spaces. The complete graph-metric and graph-ideal invariants are not addressed. The calculations are finite supplementary checks, and no claim of exhaustive bibliographic priority or independent audit is made.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15; Theorem 3.5. https://arxiv.org/html/2001.05448v2

[2] R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24. https://arxiv.org/html/2605.25150v1

[3] P. Deshpande, S. Goyal and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358, first posted 2026-07-06. https://arxiv.org/abs/2607.05358
