# An elementary collapse between Möbius–Kantor higher-independence complexes

## Finding

For the Möbius–Kantor graph \(M=\operatorname{GP}(8,3)\), the inclusion of its second into its third higher-independence complex is a *simplicial collapse*:
\[
\operatorname{Ind}_3(M)\searrow\operatorname{Ind}_2(M).
\]
There is an explicit sequence of exactly **4,192 elementary free-face/coface collapses**. Thus the displayed inclusion is a simple-homotopy equivalence and its geometric realization is a strong deformation retract. In particular it induces isomorphisms on all integral homotopy and homology groups. This is a **relative** result about the actual inclusion, not a claim merely that its source and target happen to have equal homology or abstract homotopy type.

## Assumptions and scope

Write the vertices of \(M\) as \(u_i,v_i\), where \(i\in\mathbb Z/8\mathbb Z\); its 24 undirected edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\), for all eight values of \(i\). The labels used in the certificate are \(u_0,\ldots,u_7\) at bit positions 0–7 and \(v_0,\ldots,v_7\) at positions 8–15.

For each positive integer \(r\), define \(\operatorname{Ind}_r(M)\) to be the abstract simplicial complex of vertex sets \(S\subseteq V(M)\) for which every connected component of the *induced* subgraph \(M[S]\) has at most \(r\) vertices. These are full abstract complexes, including the empty face; no weighted, directed, or clique-complex convention is used.

Let \(F_2\) and \(F_3\) denote their respective face sets, represented by 16-bit nonnegative integers. A pair \((a,b)\) in `collapse_pairs.txt` means that \(a\) is a codimension-one face of \(b\). Rows are applied in the indicated order.

## Proof

**Exhaustive face construction.** The checker enumerates all \(2^{16}=65,536\) vertex masks. It computes the connected components of each induced subgraph using bit-set searches and independently tests whether the mask contains any connected triple (for \(F_2\)) or connected quadruple (for \(F_3\)). These are equivalent characterizations: a connected component of at least \(r+1\) vertices contains a connected induced subset of exactly \(r+1\) vertices, obtained by successively adding a neighboring vertex. At cutoff two, the independent local test that every selected vertex has induced degree at most one agrees too.

The checks establish \(|F_2|=6,813\), \(|F_3|=15,197\), \(F_2\subset F_3\), and \(|F_3\setminus F_2|=8,384\). Both sets are simplicial complexes by their downward-closed definitions.

**Elementary collapses.** The accompanying certificate contains 4,192 rows, each an ordered pair of integer face masks \((a,b)\). Starting with the entire face set \(F_3\), at each row the independent verifier checks that (i) both faces are currently present and lie outside \(F_2\), (ii) \(a\subset b\) and \(b\setminus a\) is one vertex, (iii) \(b\) is the *unique* present codimension-one coface of \(a\), and (iv) \(b\) has no present coface. It then deletes precisely \(a\) and \(b\). Since any proper coface of \(a\) contains some codimension-one coface, (iii) establishes that \(b\) is its unique maximal coface. Conditions (i)–(iv) therefore prove that **each row is a legitimate elementary simplicial collapse** in the whole current complex, not just in the relative face difference.

After all rows, the verifier checks that the remaining face set is **exactly** \(F_2\), and that each of the 8,384 removed faces was deleted once and only once. An elementary simplicial collapse gives a strong deformation retraction on realizations. The composition proves the claimed relative collapse and its homotopy consequences.

## Verification

Run `python3 verify.py` with `collapse_pairs.txt` in the same directory. Only the Python standard library is used. The program both recomputes the lexicographically prioritized greedy construction of the certificate and independently replays the saved list against the **complete current** face poset. It performs two independent admissibility tests for every subset, and a third at cutoff two. The certificate has SHA-256 `f4a86667e6dd6e17b3278642a4258743bef355aa336cbf51b60cbc3abc976ff7`.

The 4,192 collapse pairs are distributed by the dimension of the removed lower face as follows: dimensions \(2,3,4,5,6,7,8\) have respectively \(48,336,1008,1512,1032,240,16\) pairs. The first mask pair is `(494,4590)` and the last is `(36880,53264)`. Both complexes have ordinary Euler characteristic 4. The recorded complete output is in `verification_output.txt`.

## Relationship to prior work

Deshpande and Singh introduce and classify higher-independence complexes for several graph families, including paths, cycles, multipartite graphs, and selected trees. Subsequent work on chordal graphs covers structurally different graph classes. The Möbius–Kantor graph is not chordal: it contains induced cycles of length greater than three. Earlier calculations of this graph's **ordinary** or **two-independence** homotopy and symmetry do not give an elementary collapse of the *ambient three-independence complex* onto the two-independence subcomplex: equality of abstract homotopy types, or knowledge of only the smaller complex, does not determine an inclusion map. Results about the graph's matching complexes, metric nerves and cut complexes use different face conditions. The present result specifies and checks the actual relative collapse sequence.

## Limitations

This is a finite theorem for the specified 16-vertex graph and the single inclusion from cutoff two to three. It does not classify larger generalized Petersen graphs, other cutoffs, or equivariant collapse sequences. The existence of an elementary collapse is stronger than equal homology, but no general criterion for such collapses is asserted. An equivalent previously unindexed description of the relative inclusion cannot be excluded by literature searching alone.

## References

1. A. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted 2020-01-15). https://arxiv.org/abs/2001.05448
2. A. Abdelmalek et al., work on higher-independence complexes of chordal graphs, arXiv:2106.10863 (2021). https://arxiv.org/abs/2106.10863
3. A. Deshpande, A. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775 (2020). https://arxiv.org/abs/2001.06775
4. E. H. Spanier, *Algebraic Topology*, 1966, standard elementary simplicial collapses and deformation retractions.
