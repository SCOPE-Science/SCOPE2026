# First multiple-sphere reflection-fixed loci in \(3\times n\) grid matching complexes

## Finding
Let \(G_n=P_3\square P_n\) be the rectangular grid, let \(X_n=\mathcal M(G_n)\) be its ordinary matching complex, and let \(c(r,j)=(r,n-1-j)\) reverse columns. For the first five positive even widths, the **actual geometric fixed-point space** has the following integral homotopy type:
\[
\begin{array}{c|ccccc}
 n&2&4&6&8&10\\\hline
 |X_n|^{\langle c\rangle}&\mathrm{pt}&S^2&S^3&\bigvee^4 S^4&\bigvee^{11} S^5.
\end{array}
\]
In particular, width \(8\) is the first positive even width whose reflection-fixed space is a wedge of more than one positive-dimensional sphere, and width \(10\) already has eleven spheres. The statement determines homotopy types, not just reduced Euler characteristics.

## Assumptions and scope
Rows have indices \(r\in\{0,1,2\}\); columns have indices \(0\le j<n\). Graph edges join vertices at Manhattan distance one. An ordinary matching is a set of graph edges with pairwise disjoint endpoints. The geometric fixed-point notation refers to the fixed points **of the topological realization**, not to the subcomplex on graph edges fixed individually. The theorem is for \(n=2m\) and \(1\le m\le5\); no formula for larger \(m\) is asserted.

For each \(m\), define the auxiliary graph \(H_m\) from the \(3\times m\) grid by attaching one new leaf to each of its three vertices in the final column. Its graph vertices are labeled \(3j+r\), with \(0\le j<m\) and \(0\le r<3\), together with terminal leaves \(3m+r\), \(0\le r<3\). Edges are exactly \((3j+r,3j+r+1)\) for \(r=0,1\); \((3j+r,3(j+1)+r)\) when \(j<m-1\); and \((3(m-1)+r,3m+r)\) for the three leaves. These formulas specify the graph without pictures.

## Proof
**1. Geometric fixed-orbit lemma.** A point of the realization of a finite simplicial complex has unique barycentric coordinates, supported on a face. If a finite-order simplicial automorphism fixes the point, its nonzero barycentric coordinates are constant on each orbit of vertices. Consequently the fixed-point space is piecewise-linearly homeomorphic to the realization of the simplicial complex whose vertices are *admissible orbits* (orbits themselves forming faces) and whose simplices are collections of orbits whose union forms a face. The homeomorphism sends each orbit vertex to the normalized orbit barycenter and is affine on simplices.

**2. Identification of the reflection-fixed complex.** Write \(n=2m\). Reflection has no fixed grid vertex. Every off-axis grid edge and its reflected partner are vertex-disjoint; each contributes one admissible orbit vertex. Taking the representative edge in columns \(0,\ldots,m-1\) identifies these orbit vertices with all ordinary edges of the left \(3\times m\) grid. The three horizontal edges between columns \(m-1\) and \(m\) are fixed individually; they are identified with the three terminal-leaf edges of \(H_m\). For any two orbits, their unions have a common graph endpoint if and only if the corresponding two \(H_m\)-edges share an endpoint. As being a matching is a pairwise condition, this identifies the entire orbit complex, not merely its one-skeleton, with \(\mathcal M(H_m)\). Thus there is a piecewise-linear homeomorphism
\[
|X_{2m}|^{\langle c\rangle}\cong_{\mathrm{PL}}|\mathcal M(H_m)|.
\tag{1}
\]
This reduction is valid for every \(m\ge1\), although the asserted homotopy classification below is restricted to five values.

**3. Exhaustive acyclic Morse matchings for the five graphs.** Enumerate the \(5m\) edges of \(H_m\) in this fixed order: for each column in increasing order, its two vertical edges from top to bottom, followed by its three rightward horizontal edges (or, in the last column, its three terminal leaf edges), again from top to bottom. Represent an ordinary matching by a bit mask over this edge order. Enumerate *every nonempty matching* recursively by increasing edge index and a used-endpoint mask. On the face poset of nonempty matchings, process edge indices in the following orders:

- \(m=1\): \((4,3,2,1,0)\).
- \(m=2\): \((9,8,7,6,5,4,3,2,1,0)\).
- \(m=3\): \((7,1,0,14,9,3,6,4,13,8,5,10,12,11,2)\).
- \(m=4\): \((2,11,10,1,4,18,0,17,12,19,8,9,5,16,13,15,3,6,14,7)\).
- \(m=5\): \((24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0)\).

At stage \(i\), pair any two *still unmatched* nonempty faces \(\sigma\subset\sigma\cup\{i\}\) whenever \(i\notin\sigma\) and adding the indexed graph edge preserves the matching condition. Remove both faces. Each pair is a genuine codimension-one face relation and no face is paired twice. To establish global acyclicity rather than assuming it from the staged construction, orient **all** remaining Hasse cover relations downward and every matched cover upward; the accompanying verifier constructs this entire directed graph and verifies it is a DAG by exhausting a topological sort.

The exact critical-cell vectors, listed by dimension, are
\[
\begin{array}{c|l}
m&\text{critical cells}\\\hline
1&1\text{ in dimension }0\\
2&1\text{ in dimension }0,\ 1\text{ in dimension }2\\
3&1\text{ in dimension }0,\ 1\text{ in dimension }3\\
4&1\text{ in dimension }0,\ 4\text{ in dimension }4\\
5&1\text{ in dimension }0,\ 11\text{ in dimension }5.
\end{array}
\]
By Forman's discrete Morse theorem, each matching yields a CW complex with precisely these cells. A single zero-cell with no positive-dimensional cells except cells of one dimension \(d\ge2\) is a wedge of \(d\)-spheres (each attaching map lands in the zero-skeleton). The first case is contractible. Combining with (1) proves the theorem.

## Verification
Execute `python verify_reflection_homotopy.py` with Python 3; no external packages are needed. The program reconstructs the full \(3\times2m\) grid edge orbits, checks that every orbit is admissible, establishes the pairwise compatibility isomorphism with \(H_m\), enumerates **every nonempty matching** of \(H_m\), implements all specified Morse pairs, checks that all critical cells have the stated dimensions, and verifies acyclicity using **every nonempty Hasse cover** and a full topological sort. For \(m=1,2,3,4,5\), the respective face counts are \(11,66,426,2635,16402\), and directed-cover counts are \(13,144,1378,10976,83597\). A successful replay terminates with `VERIFY_OK`. These are exhaustive finite certificates for exactly the five values claimed; no extrapolation is used.

## Relationship to prior work
Chauhan–Sharma–Shukla (2026) investigate the *nonequivariant* matching complexes of the full width-three grids, establishing connectivity and homology statements, not the five geometric reflection-fixed homotopy types asserted here. An earlier work of Goyal–Shukla–Singh (2021) about the full grid matching complex is explicitly retracted and is not used as mathematical evidence. A prior calculation titled *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes* derives alternating rational homology traces for both reflections and, in its proof, describes the underlying reflection-edge orbits. Thus **neither the existence of the orbit description nor the five reduced Euler numbers** is claimed new here. The new contribution is the exact acyclic-Morse collapse classification upgrading the even-axis fixed-point **homotopy types**. Euler characteristics do not themselves specify these homotopy types, the homological degrees, or the vanishing of lower homotopy groups.

## Limitations
This is a finite, five-width result. It proves no all-width recurrence for sphere counts and makes no claim of independent verification. The September 2026 preprint's full text could not be inspected through the available lawful access routes; a coincidentally equivalent full-text argument would remain an originality risk. Related unpublished or unindexed calculations may exist. The certified matching and all mathematical conclusions are restricted to the stated graph definitions and five even widths.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first posted 2026-09-23, https://arxiv.org/abs/2609.27366.
2. *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes* (2026), publicly indexed mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-orthogonal-reflection-lefschetz-formulas-for-3-times-n-grid-matc--c1da8c8f4653. The published RESULT.md statement and proof were read for implication comparison.
3. S. Goyal, S. Shukla, A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), https://doi.org/10.37236/10496. **Retracted; consulted only for literature overlap, not relied on as a theorem.**
4. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Mathematics 346 (2023), 113428, https://doi.org/10.1016/j.disc.2023.113428. This concerns chains of polygons, not the terminally whiskered grid in (1).
