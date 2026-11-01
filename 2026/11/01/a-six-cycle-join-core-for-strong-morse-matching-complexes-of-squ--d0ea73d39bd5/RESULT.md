# A six-cycle join core for strong Morse matching complexes of square bouquets

## Finding

For every integer \(m\geq2\), let \(B_m\) be the one-dimensional simplicial complex obtained from \(m\) unfilled four-cycles by identifying exactly one common vertex and making no further identifications. Let \(\mathcal{SM}(B_m)\) be the full strong discrete-Morse matching complex: its generating simplices are the matching pairs produced by injective vertex filtrations, and every subset of a generating simplex is a face.

**Theorem.** There is an ordinary simplicial collapse
\[
\mathcal{SM}(B_m)\searrow (C_6)^{*m},
\]
where \(C_6\) denotes the six-vertex simplicial circle and \(*\) denotes the simplicial join. Consequently,
\[
\bigl|\mathcal{SM}(B_m)\bigr|\simeq S^{2m-1},\qquad
\widetilde H_i(\mathcal{SM}(B_m);\mathbb Z)\cong
\begin{cases}\mathbb Z&i=2m-1,\\0&i\ne 2m-1.\end{cases}
\]
Moreover, writing \(f_{r-1}\) for the number of \(r\)-vertex faces (including \(f_{-1}=1\)), the entire face enumerator is
\[
\sum_{r\geq0}f_{r-1}z^r=
(1+6z+6z^2)^m+2mz(1+3z)(1+4z+3z^2)^{m-1}.
\]
In particular, the complex is pure of dimension \(2m-1\), with exactly \(6^m+2m3^m\) facets.

## Assumptions and scope

Each square has vertices \(o,a_i,b_i,c_i\), with edges \(oa_i,a_ib_i,b_ic_i,c_io\). Different squares meet only at the shared vertex \(o\). No four-cycle is filled by a two-simplex. A vertex of the strong matching complex is denoted \([v\to u]\), meaning the Hasse-diagram pair consisting of the graph vertex \(v\) and the incident edge \(uv\). For a vertex ordering, \([v\to u]\) occurs exactly when \(u\) is the **unique** neighbor of \(v\) earlier than \(v\). This follows directly from descending domination in a one-dimensional simplicial complex: a nonempty descending link is a cone precisely when it is one point. The complete strong matching complex is the downward closure of these matchings, not the ordinary complex of all acyclic matchings.

## Proof

**1. The local hexagon without a shared-vertex matching.** In square \(i\), abbreviate
\[
A_i=[a_i\to o],\quad B_i=[b_i\to a_i],\quad
C_i=[c_i\to o],\quad D_i=[b_i\to c_i],\quad
E_i=[a_i\to b_i],\quad F_i=[c_i\to b_i].
\]
Examine the \(24\) relative orders of \(o,a_i,b_i,c_i\). After omitting any pair having \(o\) as its source, the maximal remaining sets are exactly
\[
\{A_i,B_i\},\ \{A_i,C_i\},\ \{C_i,D_i\},\
\{D_i,E_i\},\ \{E_i,F_i\},\ \{F_i,B_i\}.
\]
Their downward closure \(L_i\) is an induced six-cycle. All six sets occur for suitable relative orders. Since local relative orders can be interleaved consistently around the one common vertex \(o\), the subcomplex \(X\) of all faces not involving a pair with source \(o\) is **exactly**
\[
X=L_1*\cdots*L_m\cong(C_6)^{*m}.
\]
The possibility that the global ordering also produces a pair with source \(o\) does not affect this equality, because the full strong complex includes all subsets.

**2. Links of shared-vertex pairings.** The only further vertices of \(\mathcal{SM}(B_m)\) are \(t_{i,a}=[o\to a_i]\) and \(t_{i,c}=[o\to c_i]\). No two such vertices share a simplex, because a Hasse-diagram matching cannot pair \(o\) twice. For \(t_{i,a}\) to occur, \(a_i\) must be the unique earlier neighbor of \(o\). In the same square, the possible simultaneous noncentral pairs are individually
\[
T_{i,a}=\{B_i,C_i,E_i\},
\]
with no two of these occurring together: here \(T_{i,a}\) denotes the zero-dimensional simplicial complex on these three vertices. Similarly, the link contribution of the distinguished square for \(t_{i,c}\) is the three-point complex
\[
T_{i,c}=\{F_i,A_i,D_i\}.
\]
For every other square \(j\ne i\), both \(a_j\) and \(c_j\) must lie after \(o\). Under exactly this restriction the allowed noncentral matching pairs span the three-edge path
\[
H_j=\langle\{A_j,B_j\},\{A_j,C_j\},\{C_j,D_j\}\rangle.
\]
If \(b_j\) precedes \(o\), no noncentral pair is produced in that square; this contributes only the empty face, already contained in \(H_j\). Every local choice described above is realized by a relative ordering, and all choices can be interleaved while preserving their positions relative to \(o\). Therefore the links are the *exact simplicial joins*
\[
\operatorname{lk}(t_{i,a})=T_{i,a}*\mathop{*}_{j\ne i}H_j,
\qquad
\operatorname{lk}(t_{i,c})=T_{i,c}*\mathop{*}_{j\ne i}H_j.
\]

**3. Actual simplicial collapses.** Every \(H_j\) is a three-edge path, hence collapsible. The join of any finite simplicial complex with a nonempty collapsible complex is collapsible: an elementary collapse in one join factor extends to a sequence of free-face collapses in the join, ordered by decreasing dimension in the other factor. Because \(m\geq2\), each displayed link has at least one factor \(H_j\) and is therefore collapsible.

If a vertex \(t\) of a finite simplicial complex has collapsible link, the closed star \(t*\operatorname{lk}(t)\) collapses **relative to its link**: cone the free-face pairs of a collapse of the link to a single vertex, and finally remove the remaining pair consisting of \(t\) and the edge from \(t\) to that vertex. This deletes exactly those faces containing \(t\), leaving the vertex-deletion subcomplex. Apply this to each of the \(2m\) shared-vertex matching vertices. Since no two can share a simplex, deleting one leaves the other links unchanged. The residue is precisely \(X\). Thus \(\mathcal{SM}(B_m)\searrow X\).

Each \(L_i\) triangulates \(S^1\), and the join of \(m\) copies of \(S^1\) triangulates \(S^{2m-1}\). This proves the homotopy and integral-homology assertions without any limiting argument or finite-case extrapolation.

**4. Faces and purity.** For a simplicial complex \(Y\), let \(F_Y(z)\) enumerate all its faces by vertex count, including the empty face. Then \(F_{Y*Z}=F_YF_Z\). We have \(F_{L_i}=1+6z+6z^2\), \(F_{H_i}=1+4z+3z^2\), and \(F_{T_{i,*}}=1+3z\). The faces without a shared-vertex matching have enumerator \(F_X=(1+6z+6z^2)^m\). Every other face contains **exactly one** such matching vertex, and the \(2m\) corresponding stars contribute disjointly
\(2mz(1+3z)(1+4z+3z^2)^{m-1}\).
All facets of \(X\) and of these stars have exactly \(2m\) vertices; the numbers are respectively \(6^m\) and \(2m3^m\). This proves the face enumerator and purity.

## Verification

The accompanying `verify.py` uses only the Python standard library. For \(m=1,2,3\), it enumerates **every** permutation of the \(1+3m\) graph vertices and constructs the associated strong matching directly from earlier-neighbor sets, independently of the proposed hexagon/path decomposition. It then checks equality of the actual and predicted maximal-face sets, all face-count coefficients, and mod-two chain ranks. For \(m=2,3\), it additionally constructs and checks every elementary free-face removal until no shared-vertex matching vertices remain and verifies exact equality with the join of local six-cycles.

The observed face-count vectors, indexed by the number of vertices in a face starting at zero for the empty face, are \((1,8,12)\), \((1,16,76,132,72)\), and \((1,24,192,708,1296,1134,378)\). The actual deletion certificates contain respectively \(64\) and \(768\) elementary collapse pairs for \(m=2,3\). The program prints `ALL_VERIFY_OK` only after these checks pass. These finite checks corroborate the explicitly proved all-parameter decomposition; they are not the basis of the infinite proof.

## Relationship to prior work

Knudson and Owens-White introduce the full strong discrete-Morse matching complex and study paths, stars, individual cycles, simplices, and their boundaries [1]. Their Proposition 8.5 computes the single four-cycle case, while their Proposition 10.3 handles **disjoint** unions by joins. Neither result covers four-cycles identified at one vertex: the identified vertex changes the allowable filtration matchings. The present all-parameter collapse is stronger than the statement of homology ranks, and the face enumerator gives a separate exact combinatorial characterization.

The ordinary Morse complex of Chari and Joswig [2] is not the full strong-matching complex used here. Likewise, ordinary matching-complex calculations for squares sharing an **edge** concern both a different graph family and a different functor. A bouquet of triangles has a different local matching structure; its sphere-wedge multiplicities do not imply the hexagonal join collapse for square bouquets.

## Limitations

The cycles must be unfilled squares with a **single shared vertex** and no further identifications. The theorem is not a classification for arbitrary cactus graphs, cycles of other lengths, ordinary discrete Morse matching complexes, or equivariant homotopy types. The exceptional one-square case has the previously known type \(\mathcal{SM}(C_4)\simeq\bigvee^5S^1\), and does **not** satisfy the claimed collapse to one six-cycle; the theorem explicitly assumes \(m\ge2\).

## References

[1] Kevin P. Knudson and Abigail Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first public version dated 2026-09-06), especially Sections 3–4, Proposition 8.5, and Section 10. https://arxiv.org/abs/2609.06844

[2] Manoj K. Chari and Michael Joswig, *Complexes of discrete Morse functions*, Discrete Mathematics 302 (2005), 39–51; arXiv:math/0011234. https://arxiv.org/abs/math/0011234
