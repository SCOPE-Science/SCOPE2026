# Exact VC and Littlestone dimensions of seven-label circular orders

## Finding

Let \(\mathcal C_n\) be all cyclic orders of the distinct labels \(0,\ldots,n-1\), with a Boolean query for each triple \(a<b<c\) recording whether these appear clockwise in that cyclic order. For \(n=7\), the exact static and adaptive dimensions are
\[
\operatorname{VCdim}(\mathcal C_7)=7,\qquad \operatorname{Ldim}(\mathcal C_7)=9.
\]
The first strict separation in this family occurs at seven labels: for \(n=3,4,5,6\) the corresponding pairs are \((1,1),(2,2),(4,4),(6,6)\), respectively. Equivalently, the seven-label class has an adaptive-minus-static gap of two. This finite result resolves the seven-label static threshold left between seven and nine in the closest identified published public calculations.

## Assumptions and scope

A cyclic order is a permutation of the seven distinct labels modulo cyclic rotation, **not** modulo reversal. Normalize its representative to start with label zero, giving exactly \(6!=720\) possibilities. Queries are all \(\binom{7}{3}=35\) increasing triples \((a,b,c)\). The answer is one precisely when, moving clockwise from \(a\), one encounters \(b\) before \(c\). The VC dimension is the largest number of fixed triple queries jointly realizing all Boolean patterns. The Littlestone dimension is the maximum depth of a *complete*, adaptively queried binary decision tree, in which each binary response sequence is witnessed by at least one cyclic order. All statements concern these distinct definitions, not arbitrary binary strings or linear comparisons.

## Proof

**Seven fixed queries shatter.** Set
\[
Q=\{(0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,1,6),(2,3,4),(2,5,6)\}.
\]
The standalone file `vc7_witnesses.json` contains, for each of the \(128\) binary words on \(Q\), an index of a cyclic order in the lexicographic enumeration of permutations \((0,p_1,\ldots,p_6)\). The independent `verify_circular.py` enumerates the 720 permutations anew and checks every response bit of each of the 128 witnesses. This is a complete finite lower-bound certificate, giving \(\operatorname{VCdim}\ge7\).

**Eight fixed queries cannot shatter.** Relabeling the seven labels permutes the 35 possible triple queries and preserves each answer word up to coordinate complements. Thus if any eight-query set shattered, one could choose a shattered eight-query set containing the triple \((0,1,2)\). The verifier exhaustively lists all increasing extensions of this fixed query. For each partial selection of \(k\) queries to be extendible to eight shattered queries, each of the \(2^k\) answer cells must contain at least \(2^{8-k}\) cyclic orders: these are the distinct witnesses required for their eventual descendant words. Therefore an extension is safely pruned when any refined cell has fewer than the necessary orders. The exact branch-and-bound counts of visited viable prefixes at sizes zero through eight are
\[
(0,1,28,290,1572,3669,2903,711,0).
\]
No size-eight support survives. The checker uses bitmask intersections on all 720 enumerated concepts, visits all eligible query indices in ascending order and uses only this necessary safe pruning test. This is exhaustive finite verification, not sampling. Hence \(\operatorname{VCdim}\le7\).

**Depth nine is realizable.** `ldim9_tree.json` provides a recursive full binary tree with \(511\) internal nodes, each labeled by one of the \(35\) possible queries, and \(512\) distinct leaf witnesses. The checker reconstructs each path and verifies that its witness cyclic order obeys every one of the nine preceding answers. Consequently \(\operatorname{Ldim}\ge9\).

**Depth ten is impossible.** A complete depth-ten tree would require at least \(2^{10}=1024\) distinct concepts, since no fixed concept can follow two different answer paths after their first split. There are only 720, hence \(\operatorname{Ldim}\le9\).

**First separation.** For sizes three through six the verifier gives fixed shattered supports of sizes \(1,2,4,6\), matching the respective cardinality upper bounds \(\lfloor\log_2((n-1)!)\rfloor\). As \(\operatorname{VCdim}\le\operatorname{Ldim}\), both dimensions equal those bounds. Their equality at smaller sizes and the displayed seven-label values prove the first strict gap.

## Verification

Run with Python 3 standard library only:

```sh
python3 verify_circular.py vc7_witnesses.json ldim9_tree.json
```

The expected final line is `CYCLIC_ORDER_ALL_CHECKS_PASS`. Separate assertions check the seven-query witness mapping, the symmetry-reduced exhaustive eight-query obstruction, every internal node and leaf of the depth-nine tree, cardinality of the family and small-size witness supports. There is no randomization, optimization tolerance, unrecorded dataset or non-stdlib dependency. The full source and all certificates are distributed as standalone files.

## Relationship to prior work

The online-learning dimension and VC dimension are developed in the 2021 papers of Guingona et al. and Malliaris–Moran, where the exact families studied are different. García-Colín et al. identify cyclic permutations with transitive-oriented ternary structures, giving an equivalent representation of our clockwise queries. Ramassamy treats more restricted cyclic-order extensions. The closest public exact shattering computation identified in the literature, the P39-MATH-G document, established values through six labels and explicitly left the seven-label dimension between seven and nine. Its lower bound and the general concept-count upper bound do not imply this paper's exact seven-label VC dimension, nor its separate Littlestone result. Historical priority should not be inferred solely from unsuccessful database searches.

## Limitations

The seven-label impossibility claim rests on a small exhaustive finite algorithm with source code suitable for independent reimplementation. No result for larger label counts, asymptotic behavior, or unrestricted partial cyclic orders is claimed. This work has received self-review and automated reproducibility checks only; independent mathematical audit remains outstanding. Priority against older literature on cyclic order extensions and online comparisons is not fully certified.

## References

1. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first public 2021-09-10), https://arxiv.org/abs/2109.04805.
2. M. Malliaris, S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569 (first public 2021-08-12), https://arxiv.org/abs/2108.05569.
3. N. García-Colín, A. Montejano, L. Montejano, D. Oliveros, *Transitive oriented 3-Hypergraphs of cyclic orders*, arXiv:1210.6828 (2012), https://arxiv.org/abs/1210.6828.
4. S. Ramassamy, *Extensions of Partial Cyclic Orders, Euler Numbers and Multidimensional Boustrophedons*, arXiv:1706.03386 (2017), https://arxiv.org/abs/1706.03386.
5. *P39 Mathematical Track: Acyclic Hypergraph Gluing, Invariant Separators and Shattering*, public research document, sections G5–G9, https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p39/P39_MATH_G_ACYCLIC_HYPERGRAPH_GLUING_INVARIANT_SEPARATORS_AND_SHATTERING.md.
