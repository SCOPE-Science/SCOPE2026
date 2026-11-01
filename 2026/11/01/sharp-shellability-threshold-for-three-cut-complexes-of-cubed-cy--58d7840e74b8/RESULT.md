# Sharp shellability threshold for three-cut complexes of cubed cycles

## Finding
For every integer \(n\ge9\), the ordinary three-cut complex of the third power of the cycle graph is shellable **if and only if** \(n\ge13\):
\[
\boxed{\Delta_3(C_n^3)\text{ is shellable}\quad\Longleftrightarrow\quad n\ge13.}
\]
In the shellable range its complete integral homotopy type is
\[
\boxed{\Delta_3(C_n^3)\simeq\bigvee^{\binom{n-6}{2}-20} S^{n-4}\qquad(n\ge13).}
\]
In particular, the two previously untreated boundary parameters admit explicit complete shellings, with \(169\) facets and one spanning facet at \(n=13\), and \(238\) facets and eight spanning facets at \(n=14\). For the nonshellable cases, exhaustive integral-combinatorial chain construction and exact binary row reduction yield the following nonzero reduced mod-two homology: \(\widetilde H_3\cong\mathbb F_2\) at \(n=9\); \(\widetilde H_4\cong\mathbb F_2^{11}\) at \(n=10\); \(\widetilde H_5\cong\mathbb F_2\) at \(n=11\); and \(\widetilde H_7\cong\mathbb F_2^2\) at \(n=12\). Each of these degrees is strictly below the pure top dimension \(n-4\). For \(3\le n\le8\) the three-cut complex has no facets because no induced triple is disconnected.

The genuinely new part is the sharp boundary classification for the cubed-cycle family, especially the explicit shelling certificates for \(n=13,14\). The all-parameter statement for \(n\ge15\) uses the previously published general shellability theorem, not a new proof of that range.

## Assumptions and scope
The vertex set of \(C_n\) is \(\mathbb Z/n\mathbb Z\). Distinct vertices are adjacent in \(C_n^3\) when their graph distance in \(C_n\) is at most three. The ordinary cut complex \(\Delta_3(G)\) has as facets the complements \(V(G)\setminus T\) of all three-element subsets \(T\) for which the induced graph \(G[T]\) is disconnected. Thus, when nonvoid, it is pure of dimension \(n-4\). It is not the *total* three-cut complex, which would require a three-vertex independent set. All shellability claims are for pure simplicial shellability. Homology calculations below threshold use coefficients \(\mathbb F_2\); the sphere wedges above threshold are integral homotopy conclusions.

## Proof
**1. The void range.** For \(3\le n\le7\), \(C_n^3\) is complete. For \(n=8\) it is a complete graph with the four antipodal edges removed: an induced three-vertex subgraph always has at least two edges, so is connected. Thus the defining set of disconnected triples is empty for \(n\le8\).

**2. Exhaustive obstruction at \(9\le n\le12\).** For each \(n\), the companion `verify.py` independently enumerates every three-element set \(T\), constructs all edges of \(C_n^3[T]\), tests connectedness by breadth-first search, and collects the complementary facets. It constructs their complete downward-closed face set, organizes simplicial chain groups by dimension, forms every mod-two boundary column from the codimension-one subfaces, and performs exact bit-vector Gaussian elimination. The resulting facet counts are \(9,30,66,112\) at \(n=9,10,11,12\) respectively, and the nonzero reduced mod-two groups are those stated above. The complete face vectors and boundary ranks are printed by the verifier, so none of the homology assertions depends on a non-reproducible precomputed table. A pure shellable complex has reduced homology only in its top dimension, so the verified subtop classes prohibit shellability for all four values. These are complete finite exhaustive proofs, not incomplete sampling.

**3. Full shellings at the missing parameters \(13,14\).** The files `order13.txt` and `order14.txt` give permutations of **all** \(169\) and \(238\) facets respectively, encoded as increasing vertex labels on each line. The verifier reconstructs the defining facets independently and requires exact equality of the certificate's facet set with the set of all actual facets, with no duplicates. Let \(F\) be a new facet in a proposed order and \(F_1,\ldots,F_{j-1}\) its predecessors. Define the *old-ridge removal set*
\[
A(F)=\{v\in F:\exists i<j,\ F\setminus\{v\}\subseteq F_i\}.
\]
A pure shelling step is valid exactly when \(A(F)\ne\varnothing\) and, for every \(i<j\), there exists \(v\in A(F)\setminus F_i\). Indeed, the second condition says the intersection \(F\cap F_i\) lies in a codimension-one face \(F\setminus\{v\}\) already present, and the first ensures there is at least one such ridge. Conversely every pure intersection along previous facets forces these conditions. The script checks the conditions for every prior facet at every step. A separately executed direct method checks instead that **all inclusion-maximal intersections** of each new facet with older facets have codimension one; it agrees for all steps at both parameters. Thus both finite certificates are genuine shellings, not numerical guesses. Spanning facets are precisely those with \(A(F)=F\): the verifier counts one at \(n=13\), eight at \(n=14\). Attaching shellable facets consequently yields \(S^9\) and \(\bigvee^8S^{10}\), respectively.

**4. Every larger parameter.** Chauhan and Shukla [1, Theorem 1.4] prove shellability and the homotopy type \(\bigvee^{\binom{n-2p}{2}-(2p^2+p-1)}S^{n-4}\) for \(p\ge2\) and \(n\ge6p-3\). At \(p=3\) this covers precisely \(n\ge15\), with exponent \(\binom{n-6}{2}-20\). At \(n=13\) and \(n=14\) that exponent equals \(1\) and \(8\), agreeing with the independently supplied shellings. Combining the exact finite obstruction, the two finite shellings, and the cited published infinite theorem proves the entire asserted classification.

## Verification
Run `python3 verify.py` in the directory containing `verify.py`, `order13.txt`, and `order14.txt` with the Python 3 standard library. The exact run reported `SUBTOP_OK` for each \(n=9,10,11,12\), `SHELLING_OK 13 facets 169 top_sphere_count 1`, `SHELLING_OK 14 facets 238 top_sphere_count 8`, and finally `ALL_VERIFY_OK`. Its printed face vectors, including dimension-zero through maximal dimension, are \((9,36,81,90,45,9)\), \((10,45,120,210,242,135,30)\), \((11,55,165,330,462,451,264,66)\), and \((12,66,220,495,792,924,780,432,112)\). An independent direct maximal-intersection shelling check (not needed as a separate dependency) returned `INDEPENDENT_SHELL_INTERSECTIONS_OK` for \(n=13\) and \(n=14\). The finite files certify only \(n\le14\); the infinitely many larger values follow from [1]. No separate external scientific audit is asserted.

## Relationship to prior work
The main inspiration is Chauhan and Shukla [1], publicly posted March 24, 2026. Their Theorem 1.4 covers \(p=3\) only when \(n\ge15\), and their conclusion explicitly cites the conjectural sharp division \(2p+3\le n\le4p\) nonshellable versus \(n\ge4p+1\) shellable. The present theorem proves that division for \(p=3\), adding exactly the missing \(n=13,14\) shelling cases and the finite lower obstruction. Chauhan, Shukla, and Vinayak [2] settle the corresponding \(p=2\) question, not the cubed-cycle boundary. The published cyclic-character computation [3] and a related dihedral-character calculation [4] both assume \(n\ge6p-3\); representation results in that already-shellable range do not imply shellability of the missing boundary cases. Our finite certificates therefore do not merely re-express an existing theorem; they close the explicit gap left by the applicable parameter bounds. Literature searches cannot rule out all unindexed equivalent results.

## Limitations
The proof determines pure shellability at third cycle power, not at arbitrary exponent \(p\ge4\). It does not claim integrally classified homotopy types below the shellability threshold: the reported obstruction there is mod-two homology. The two shellings are finite, fully specified certificates, and the large-parameter case relies explicitly on the independent published theorem. The result does not supply an equivariant sphere-wedge decomposition, a minimal geometric cell model, or an algorithm for the conjectural general sharp threshold.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first public 2026-03-24, Theorem 1.4 and Section 4, https://arxiv.org/abs/2603.23155.
2. P. Chauhan, S. Shukla, and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, first public 2024-06-04, https://arxiv.org/abs/2406.01979.
3. *Rational cyclic homology representations of three-cut complexes of cycle powers*, published research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d.
4. A related published dihedral-character analysis for three-cut complexes of cycle powers assumes \(n\ge6p-3\); it does not address shellability below that bound.

