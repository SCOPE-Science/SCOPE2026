# Three six-spheres and an irreducible symmetry character in the Möbius–Kantor two-independence complex

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph and \(X=\operatorname{Ind}_2(M)\) its two-independence complex. Then, integrally,
\[
X\simeq \bigvee^{3}S^{6}.
\]
The full automorphism group \(G=\operatorname{Aut}(M)\) has \(96\) elements. Its action on the sole nonzero reduced rational homology group, \(\widetilde H_6(X;\mathbb Q)\cong\mathbb Q^3\), is absolutely irreducible. For the order-eight rotation \(r\), the character is
\[
\bigl(\chi(r^j)\bigr)_{j=0}^{7}=(3,-1,-1,-1,3,-1,-1,-1).
\]
The homology action has kernel of order two, and the full symmetry quotient is rationally acyclic:
\[
\widetilde H_k(|X|/G;\mathbb Q)=0\qquad(k\ge0).
\]
The complete character is determined by the signed fixed-simplex formula below and verified on every automorphism. Neither rational acyclicity nor the integral nonequivariant homotopy equivalence implies contractibility of the quotient.

## Assumptions and scope
Use vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/8\mathbb Z\). The edge set is \(\{u_i,u_{i+1},u_iv_i,v_iv_{i+3}:i\in\mathbb Z/8\mathbb Z\}\). This is a simple undirected graph of sixteen vertices and twenty-four edges. The simplices of \(X\) are all subsets \(\sigma\subseteq V(M)\) such that each connected component of the induced graph \(M[\sigma]\) has at most two vertices. Equivalently, every vertex of \(M[\sigma]\) has degree at most one. This is **not** the ordinary independence complex (where the induced degree must be zero), a matching complex, or a clique complex. The result is specific to this graph.

For finite-chain verification, assign bit \(i\) to \(u_i\) and bit \(8+i\) to \(v_i\), for \(0\le i<8\). Orient each simplex by increasing bit index. The complete verifier `mk_ind2_check.py` requires Python 3.9 or later, using only the standard library.

## Proof
**Finite complex and acyclic matching.** Enumerating all nonempty masks with induced maximum degree at most one gives \(6812\) simplices and dimension-indexed face vector \((16,120,512,1324,2064,1840,816,120)\). The \(216\) maximal faces consist of \(96\) six-dimensional and \(120\) seven-dimensional facets. For each vertex bit \(j=0,1,\dots,15\) in order, pair each currently unmatched face \(\sigma\) lacking \(j\) with \(\sigma\cup\{j\}\), if both faces are currently unmatched. Iterate eligible lower masks in ascending integer order. There are \(3400\) pairs and the following critical masks:

| Dimension | Critical face masks |
| --- | --- |
| 0 | `1` |
| 4 | `818` |
| 5 | `8916`, `10898`, `17304`, `17714` |
| 6 | `15048`, `18344`, `21924`, `23714`, `43684`, `58008` |

The verifier reverses exactly the matched cover arrows in the face poset, orients all other Hasse covers downwards, and topologically sorts the resulting graph. Every one of the \(6812\) face nodes is removed, across all \(35104\) cover incidences. Therefore this is a globally acyclic discrete-Morse matching. The reduced CW complex has one basepoint, one four-cell, four five-cells, and six six-cells.

**Signed integral Morse boundary.** The orientation rule and the matched-pair signed boundary recursion, without modular reduction, give
\[
\partial^{\rm Morse}_5=\begin{pmatrix}-1&0&-1&-1\end{pmatrix},
\qquad
\partial^{\rm Morse}_6=
\begin{pmatrix}
-1&0&0&0&1&-1\\
-1&0&-1&-1&1&0\\
0&1&0&0&0&1\\
1&-1&0&0&-1&0
\end{pmatrix}.
\]
Their product is zero. The first matrix has a unit entry, and the second has rank exactly three: it lies in the rank-three kernel of the first, while its first three rows and first three columns have determinant \(-1\). This unit minor also proves that the image of the second matrix is primitive in \(\mathbb Z^4\). Its image therefore equals the kernel of the first matrix. In particular, reduced integral homology vanishes away from degree six and is \(\mathbb Z^3\) in degree six.

The CW model has no positive-dimensional cells below degree four. Since \(\pi_4(\bigvee S^4)\cong\bigoplus\mathbb Z\), the unit degree in the five-cell attaching matrix allows a four/five-cell homotopy cancellation. The resulting five-skeleton is a wedge of three five-spheres, and \(\pi_5(\bigvee^3S^5)\cong\mathbb Z^3\) identifies all six-cell attaching maps with the transformed integral degree matrix. The primitive rank-three image allows a further three unit cancellations, leaving precisely three six-cells attached to a point. Thus the claimed **integral homotopy type**, not merely its homology, follows.

**Full rational character.** Every graph automorphism permutes the simplices of \(X\). As the only nonzero reduced rational homology is in even degree six, its character equals the reduced signed simplicial Lefschetz number. For every \(g\in G\),
\[
\chi(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]
The sign is that of the permutation induced on the increasingly ordered vertices of an invariant simplex. Exact adjacency-preserving backtracking enumerates all \(96\) graph automorphisms. The following table groups their **individual** trace values by vertex-permutation cycle type; cycle type alone need not determine the trace. Exponent notation \(a^b\) in a table denotes \(b\) cycles of length \(a\).

| Vertex cycle type | Trace and number of automorphisms |
| --- | --- |
| \(1^{16}\) | \(3:1\) |
| \(1^4 2^6\) | \(-1:12\) |
| \(1^4 3^4\) | \(0:8\) |
| \(2^8\) | \(1:18,\ 3:1\) |
| \(2^2 6^2\) | \(0:8\) |
| \(4^4\) | \(-1:6,\ -3:2\) |
| \(4\cdot12\) | \(0:16\) |
| \(8^2\) | \(-1:12,\ 1:12\) |

The total trace is zero. The sum of squared traces is \(96\), so the usual character inner product is \(\langle\chi,\chi\rangle_G=1\). The complex representation is irreducible; it is defined over \(\mathbb Q\), hence is absolutely irreducible over \(\mathbb Q\). Exactly two elements have trace three; because a finite-order operator of dimension three has trace three only when it is the identity, the homology-action kernel has order two. The rotational trace vector shown above is the inflated augmentation character of \(\mathbb Q[C_4]\).

For a finite simplicial group action, barycentric subdivision removes simplex inversions. Over \(\mathbb Q\), averaging identifies quotient homology with invariant homology. The only potentially nonzero reduced invariant group has dimension \(|G|^{-1}\sum_{g\in G}\chi(g)=0\). The quotient is connected, proving the rational acyclicity assertion.

## Verification
Execute `python3 mk_ind2_check.py` in the directory containing this document. It runs exhaustive mask enumeration, a complete directed-Hasse acyclicity check, signed integer Morse reduction, a unimodular minor test, an **independent** computation of all original mod-two simplicial boundary ranks, enumeration of all graph automorphisms, and every signed Lefschetz trace. It prints `MOBIUS_KANTOR_IND2_HOMOTOPY_AND_FULL_AUT_CHARACTER_OK` if all assertions hold. The direct reduced mod-two Betti vector is zero outside degree six, where it equals three. The finite checker is a reproducibility aid, not an external certification or an independent audit.

## Relationship to prior work
Deshpande and Singh (2020) introduced explicit homotopy classifications of higher-independence complexes for complete multipartite, fully whiskered, path, cycle, and perfect rooted tree families. The Möbius–Kantor graph is none of these, and the stated results do not compute its two-independence homotopy or full symmetry character. Abdelmalek and collaborators (2021) study chordal higher-independence complexes and shellability; the Möbius–Kantor graph has induced cycles and is not chordal.

A previously published exact calculation of the **ordinary** Möbius–Kantor independence complex gives \(\operatorname{Ind}_1(M)\simeq\bigvee^4 S^3\vee S^4\). The ordinary complex is a proper subcomplex of \(X=\operatorname{Ind}_2(M)\). Neither that homotopy classification nor the published ordinary-homology rotation character implies the present \(\bigvee^3 S^6\) and absolutely irreducible full-group character. Literature and indexed mathematical-record searches found no statement covering this exact object and claim; the absence of a search hit is not a proof of absolute novelty.

## Limitations
The theorem is for one finite graph and does not classify all generalized Petersen graphs or all higher-independence complexes. The integral sphere-wedge equivalence is nonequivariant; the full-group action is determined on **rational homology**, not by an integral equivariant cellular splitting. The quotient is shown rationally acyclic, not contractible or integrally acyclic. An equivalent unindexed calculation remains possible. A same-graph paper on unrelated graph/geometric Lefschetz invariants was accessible by abstract and author exposition, but its large PDF was not inspected in full; this is a limited bibliographic risk, not evidence of coverage. Independent audit has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first publicly submitted 2020-01-15; Sections 1 and 3, Theorems 3.5 and 3.8; https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first publicly submitted 2021-06-21; https://arxiv.org/abs/2106.10863.
3. *Integral homotopy type of the Möbius–Kantor independence complex*, public published-finding corpus research record, 2026-10-11; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3.
4. *Cyclic symmetry on Möbius–Kantor independence homology*, public published-finding corpus research record, 2026-10-11; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e.
5. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799 (2026), abstract and linked author exposition consulted; https://arxiv.org/abs/2605.30799.
