# Cyclic normal forms for complete multipartite double-occurrence representations

## Finding

Let \(r\ge 3\), let \(n_1,\ldots,n_r\ge1\) be integers with at least one \(n_i\ge2\), and let \(G=K_{n_1,\ldots,n_r}\) be a labeled complete multipartite graph with fixed nonempty independent parts \(V_1,\ldots,V_r\). Write \(N=\sum_{i=1}^{r}n_i\). A word represents \(G\) *twice-uniformly* if it contains each vertex exactly twice and two distinct vertices alternate in the word exactly when they are adjacent in \(G\).

**Cyclic normal-form theorem.** Every twice-uniform representing word is a cyclic rotation of
\[
B_1B_2\cdots B_r\,B_1^{\mathrm{rev}}B_2^{\mathrm{rev}}\cdots B_r^{\mathrm{rev}},
\]
where the blocks \(B_i\) are permutations of the labels of the \(r\) parts in an arbitrary order, and \(B_i^{\mathrm{rev}}\) reverses the symbols of \(B_i\). Conversely, every such word represents \(G\).

For the set \(\mathcal W(G)\) of all labeled *linear* twice-uniform representing words, and the cyclic-rotation action on these words,
\[
\boxed{\lvert\mathcal W(G)\rvert=N(r-1)!\prod_{i=1}^{r}n_i!,\qquad
\lvert\mathcal W(G)/C_{2N}\rvert=\frac{(r-1)!}{2}\prod_{i=1}^{r}n_i! .}
\]
The products and quotient count labeled words; part identities and vertex labels are **not** identified by permutation or by graph automorphisms, and reversal is **not** part of the equivalence relation.

## Assumptions and scope

There are exactly \(r\ge3\) nonempty parts. At least one part contains two vertices, so \(G\) is not complete; this hypothesis is essential for the counting expression. A cyclic rotation means cutting the linear word at an arbitrary position and exchanging the two resulting segments. In a twice-uniform word, alternation of \(a\) and \(b\) means that the induced four-letter subword is \(abab\) or \(baba\). Alternation is invariant under cyclic rotation.

This is a statement about *all* twice-uniform representations, not merely concatenations of two permutations constructed from a particular orientation. The known two-part case and the all-singleton complete-graph case are **excluded from the new domain**, but are useful comparison boundaries.

## Proof

**Step 1: universal cyclic block structure.** Let \(w\) be any twice-uniform representation, choose a letter \(x\in V\) in one part \(A\), and cyclically rotate to \(w=xUxV\). Each letter \(y\notin A\) alternates with \(x\), so its two occurrences are distributed one in \(U\) and one in \(V\). If two outside letters \(y,z\) come from *different* parts, their required alternation forces the same relative order in their unique occurrences in \(U\) and \(V\): the patterns are \(y_Uz_Uy_Vz_V\) or \(z_Uy_Uz_Vy_V\). If they come from the *same* part, their required nonalternation forces opposite relative orders in \(U\) and \(V\).

The occurrences in \(U\) from each outside part are contiguous. Indeed, if two same-part labels \(y,z\) were separated in \(U\) by a label \(t\) of a different outside part, then \(y<t<z\) in \(U\) forces \(y<t<z\) in \(V\), contradicting the demanded reversal of \(y,z\) within their common part. Hence the outside-letter order in \(U\) is a concatenation \(C=C_1\cdots C_{r-1}\) of part blocks. The order of these parts is unchanged in \(V\), while the order within each block is reversed: the outside-letter projection of \(V\) is \(C^{\langle\mathrm{block}\rangle}=C_1^{\mathrm{rev}}\cdots C_{r-1}^{\mathrm{rev}}\).

Every other \(a\in A\setminus\{x\}\) does not alternate with \(x\), and therefore both occurrences of \(a\) lie in \(U\) or both lie in \(V\). Suppose they lie in \(U\). To alternate with *each* outside letter (each of which occurs once in each of \(U,V\)), the two copies of \(a\) must bracket every outside occurrence in \(U\). Thus every such first copy precedes \(C\) and every second copy follows \(C\). Since two labels in \(A\) cannot alternate, their respective first and second orders are reversed. Consequently the entire segment \(U\) is \(PCP^{\mathrm{rev}}\) for a possibly empty permutation \(P\) of the \(A\)-labels housed in \(U\). Identical reasoning gives \(V=QC^{\langle\mathrm{block}\rangle}Q^{\mathrm{rev}}\), for a permutation \(Q\) of the remaining labels of \(A\) housed in \(V\). The original cyclic word is therefore
\[
xPCP^{\mathrm{rev}}xQC^{\langle\mathrm{block}\rangle}Q^{\mathrm{rev}}.
\]
Cut immediately before \(Q^{\mathrm{rev}}\) if \(Q\) is nonempty, and before the first \(x\) otherwise. The resulting rotation is
\[
(Q^{\mathrm{rev}}xP)\,C\,(Q^{\mathrm{rev}}xP)^{\mathrm{rev}}\,C^{\langle\mathrm{block}\rangle},
\]
which is the claimed normal form with \(Q^{\mathrm{rev}}xP\) as the block for part \(A\). This argument works without presupposing any representation form or graph orientation.

**Step 2: converse.** In a displayed normal form, two distinct labels from different blocks have their occurrences in the same relative order in both halves; hence they alternate. Two labels from the same block have their relative order reversed in the second half; hence they are nested and do not alternate. Therefore every displayed word represents precisely \(G\).

**Step 3: count cyclic forms.** Choose the ordering of \(r\) labeled parts in \(r!\) ways and the internal orders of all blocks in \(\prod_i n_i!\) ways. These choices create distinct linear normal-form words beginning at a part boundary, so the total number of such words is \(r!\prod_i n_i!\).

Because some part has at least two vertices, \(G\) is not complete. The word has no nontrivial rotational period: a length-\(2N\) word in which each distinct label occurs exactly twice can have only a possible nontrivial period \(N\), but period \(N\) would make the two length-\(N\) halves identical permutations; every pair would alternate, contrary to the nonedge within a larger part. Thus a cyclic class has exactly \(2N\) linear rotations.

Among the rotations of any normal form, precisely \(2r\) start at a boundary between adjacent part blocks, counting the boundaries in both halves. Each of these is again a normal form with its first half a permutation containing every vertex exactly once. A cut strictly inside any part block cannot be such a normal form: the first \(N\) letters would contain a duplicate label from the suffix of that block, whose copy from the reversed block is also captured in that length-\(N\) segment. Therefore each cyclic class is counted exactly \(2r\) times by the \(r!\prod_i n_i!\) constructions. The cyclic-class count is \(r!\prod_i n_i!/(2r)\); multiplying by \(2N\) yields the linear count.

## Verification

The independent, self-contained `verify.py` enumerates every restricted-growth canonical twice-occurrence word on \(2,3,4,5,6,7\) labels (respectively \(3,15,105,945,10395,135135\) words). It reconstructs pair alternation directly from occurrence positions, detects exactly the cases whose nonadjacency is a complete multipartite equivalence relation, and independently finds a cyclic block normal form for every such case. It also enumerates *all labeled words* for eight graph profiles with up to five vertices, comparing the exact word counts with the formula. Run with `python3 verify.py` from the directory containing this document and the checker. A successful run ends with `VERIFY_OK complete_multipartite_cyclic_normal_form`.

These checks are finite consistency tests only. The universal statement is proved by Steps 1–3, not inferred by extrapolating the census.

## Relationship to prior work

Mozhui and Krishna, *Words for the Graphs with Permutation-Representation Number at most Three* (arXiv:2307.00301, first publicly posted 2023-07-01), study representability by concatenations of permutations and several graph families. Their classification of two-permutation representability does not enumerate **all** twice-uniform words for arbitrary multipartite graphs or supply the cyclic block-converse. Mozhui and Krishna's *On the Representation Number of Bipartite Graphs* (arXiv:2109.03458, 2021) gives constructions and bounds for bipartite graphs; the bipartite complete two-part normal form is already known and is **not** claimed anew here. Fleischmann, Haschke, Löck, and Nowotka, *Word-representable graphs from a word's perspective* (Acta Informatica 61, 2024, DOI:10.1007/s00236-024-00462-y), investigate graph changes under word rotations and local word restrictions; their inspected analysis does not give this explicit multipartite classification and labeled enumeration.

Nakamigawa and Sakuma's *The expansion of a chord diagram and the Tutte polynomial* (Discrete Mathematics 341, 2018, DOI:10.1016/j.disc.2018.02.015) considers a different enumerand: sequences of chord expansions and a Tutte-polynomial specialization, including complete multipartite intersection graphs. The accessible abstract does not establish whether an equivalent diagram-class enumeration occurs elsewhere in the inaccessible full text; this remains a priority risk.

## Limitations

The theorem is restricted to two occurrences per label, a fixed labeled complete multipartite graph with at least three parts and at least one nonsingleton part, and equivalence under rotations alone. It does not count words modulo reflection, vertex relabeling, or general graph isomorphism, nor words with more than two copies of each letter. It makes no claim to the novelty of the bipartite case, the complete-graph case, or the general fact that permutation graphs have two-permutation representations. A possible unpublished, unindexed, or inaccessible equivalent statement is not excluded by literature searches. The scientific review is not independent validation.

## References

1. K. Mozhui and K. V. Krishna, *Words for the Graphs with Permutation-Representation Number at most Three*, arXiv:2307.00301v1 (2023-07-01), https://arxiv.org/abs/2307.00301.
2. K. Mozhui and K. V. Krishna, *On the Representation Number of Bipartite Graphs*, arXiv:2109.03458v1 (2021-09-08), https://arxiv.org/abs/2109.03458.
3. P. Fleischmann, L. Haschke, T. Löck, and D. Nowotka, *Word-representable graphs from a word's perspective*, Acta Informatica 61 (2024), 383–400, DOI:10.1007/s00236-024-00462-y.
4. T. Nakamigawa and T. Sakuma, *The expansion of a chord diagram and the Tutte polynomial*, Discrete Mathematics 341 (2018), 1573–1581, DOI:10.1016/j.disc.2018.02.015.
