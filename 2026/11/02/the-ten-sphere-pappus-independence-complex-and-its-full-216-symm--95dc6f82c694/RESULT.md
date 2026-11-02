# The ten-sphere Pappus independence complex and its full 216-symmetry character

## Finding
Let \(P\) be the standard eighteen-vertex Pappus graph (the Levi graph of the Pappus \((9_3)\) point-line configuration), and \(X=\operatorname{Ind}(P)\) its independence complex. Then there is an integral homotopy equivalence
\[
X\simeq\bigvee^{10}S^4.
\]
Let \(G=\operatorname{Aut}(P)\), which has order \(216\). Its representation on \(\widetilde H_4(X;\mathbb Q)\cong\mathbb Q^{10}\) has the following **complete value distribution** over the \(216\) individual automorphisms:

| Character \(\chi(g)\) | Number of elements |
| ---: | ---: |
| \(-2\) | 21 |
| \(-1\) | 72 |
| \(0\) | 54 |
| \(1\) | 32 |
| \(2\) | 36 |
| \(10\) | 1 |

The exact character on **each individual group element**, beyond this histogram, is specified by the finite signed-face formula and the exhaustive permutation algorithm below. The sum of the character values is \(0\), and its squared character norm is \(2\). Thus the complex representation is the direct sum of **two distinct irreducible constituents, each with multiplicity one**, and its full-group invariant part vanishes. In particular,
\[
\widetilde H_j\bigl(X/G;\mathbb Q\bigr)=0\qquad(j\geq0).
\]
This does **not** claim that the ten-dimensional rational homology or its order-three subgroup character is new: those are covered by the previously indexed calculation described below. The new mathematical assertions are the integral *homotopy equivalence* and the *complete* \(216\)-symmetry character with its consequences.

## Assumptions and scope
The graph is finite, simple, and unweighted, with vertices \(0,1,\ldots,17\) and the \(27\) unordered edges specified verbatim in `pappus_independence_checker.py` as `EDGES`. This is a fixed combinatorial labeling of the usual Pappus graph; no choice of geometric embedding is used. A simplex of \(X\) is a nonempty vertex set with no adjacent pair. The group \(G\) consists of **all** adjacency-preserving permutations of these eighteen vertices, not merely those preserving the two bipartition classes. The quotient is the topological orbit space of the geometric realization, and homology is reduced where indicated. All homotopy and integral homology statements use ordinary integral coefficients.

## Proof
**Exact face-poset matching.** Enumerate every nonempty independent set as an eighteen-bit integer using the recurrence: from an independent set \(S\) and starting index \(i\), append any vertex \(v\ge i\) that is outside the closed neighborhood of \(S\), then recurse with indices strictly above \(v\). The enumeration has exactly \(2597\) distinct nonempty faces and face vector
\[
(18,126,438,801,756,348,90,18,2).
\]
Use the vertex order
\[
(11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12).
\]
For each vertex in this order, take every currently unpaired face \(\sigma\) not containing that vertex and pair it with \(\sigma\cup\{v\}\) whenever both are still unpaired. The checker constructs all \(1293\) pairings and checks each is a face-poset cover relation. It independently constructs the full oriented Hasse diagram: unmatched cover arrows point toward the lower-dimensional face, matched cover arrows are reversed. Topological sorting visits **all \(2597\) faces** across **\(11430\) oriented cover incidences**. This is an exhaustive acyclicity certificate, not a sample. The unmatched faces are exactly one vertex and ten four-faces. By the discrete-Morse CW theorem, \(X\) has the homotopy type of a CW complex with one zero-cell and ten four-cells and no other cells. Every attaching map into the zero-skeleton is constant, so this CW complex is a wedge of ten four-spheres. Thus the integral claim follows without any field-specific rank inference.

**Group character.** Exhaustively enumerate all graph automorphisms as permutations \(g\) of \(\{0,\ldots,17\}\), requiring adjacency and nonadjacency to agree for every mapped vertex pair. The self-contained checker counts exactly \(216\) distinct bijections. For an invariant nonempty oriented simplex \(\sigma=(v_0<\cdots<v_d)\), let \(\operatorname{sgn}(g|_\sigma)\) be the sign of the permutation of its ordered vertices induced by \(g\). Signed simplicial Lefschetz gives the following fully explicit function on \(G\):
\[
\chi(g)=\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)-1.
\]
The subtracted one is the trace on ordinary \(H_0(X;\mathbb Q)\). All other positive-degree rational homology apart from degree four vanishes by the matching. The checker enumerates every simplex and every automorphism and verifies the displayed character distribution. The exact sums are \(\sum_{g\in G}\chi(g)=0\) and \(\sum_{g\in G}\chi(g)^2=432=2|G|\). Character orthogonality therefore gives exactly two inequivalent complex irreducible constituents, multiplicity one each. Averaging characters shows that the \(G\)-fixed rational homology has rank zero. For finite group actions, rational homology of the orbit space agrees with the invariant rational homology (for example, after equivariant barycentric subdivision and averaging), giving the quotient conclusion.

## Verification
Run `python3 pappus_independence_checker.py` with Python 3.9 or newer; it uses only the standard library. It checks the explicit graph, all faces, all matching pairs, all Hasse arrows, independent mod-two simplicial-boundary ranks, every graph automorphism and every signed character. The independent mod-two ranks in degrees one through eight are
\[
(17,109,329,472,274,74,16,2),
\]
which agree with the integrally proved wedge. The checker verifies that the order-three cyclic shift \(r(i)=i+6\pmod{18}\) and its square both have trace \(-2\), matching the previously indexed subgroup calculation. Expected completion marker: `PAPPUS_2597_FACES_1293_ACYCLIC_PAIRS_216_FULL_CHARACTERS_OK`.

## Relationship to prior work
Tsukuda's 2017 incidence-graph theorem identifies the independence complex of an incidence graph with a suspension of a hypergraph Alexander-dual complex. It is applicable as a **general reduction** to this graph, but does not provide the present explicit ten-sphere matching or \(216\)-element homology character. Berghoff (2020) supplies spectral-sequence methods for graph independence-complex homology and examples such as the Petersen graph; those results likewise do not compute the Pappus full-group character. A previously indexed public note entitled *Order-three symmetry on Pappus independence homology* already determines the rational ten-dimensional homology and its \(C_3\)-character \((10,-2,-2)\). A restriction to that proper subgroup cannot determine the distinct traces on the other automorphisms, the inner product of the full character, or the full quotient invariant dimension. The calculation here agrees with that known restriction and does not reclaim it. Studies of the Pappus matching complex, topological Čech complexes, and graph braid spaces concern other constructions.

## Limitations
This finite result applies only to the standard Pappus graph and its specified independence complex. It makes no claim about arbitrary \((9_3)\)-configurations, other graph complexes, characteristic-dependent representations, or equivariant homotopy equivalences. The wedge equivalence itself is not asserted to respect the group action. A direct group-theoretic naming of the two irreducible constituents is not given, although the algorithm specifies their sum completely. The public indexed order-three source was accessible through its published summary but not its complete source document; an unindexed equivalent full-group computation remains a bibliographic risk. No independent external audit has been performed.

## References
1. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46; DOI `10.55016/ojs/cdm.v12i1.62277` (public 2017-09-27), especially Corollary 4.11 and Section 5.
2. M. Berghoff, *On the homology of independence complexes*, arXiv:`2008.06267` (first submitted 2020-08-14); Combinatorial Theory 2 (2022), no. 1.
3. *Order-three symmetry on Pappus independence homology*, publicly indexed research result, identifier `2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31` (subgroup result; full text not retrieved).
