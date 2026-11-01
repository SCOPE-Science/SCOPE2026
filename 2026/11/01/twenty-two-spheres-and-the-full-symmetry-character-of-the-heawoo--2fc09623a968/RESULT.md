# Twenty two-spheres and the full symmetry character of the Heawood strong-matching complex

## Finding
Let \(H\) denote the incidence graph of the Fano plane. Define its **strong-matching simplicial complex** \(\mathcal S(H)\) to have as vertices the \(21\) edges of \(H\), and a set of edges is a face precisely if those edges form an **induced matching**: their endpoints are distinct and no two endpoints of different chosen edges are adjacent in \(H\). Equivalently,
\[
\mathcal S(H)=\operatorname{Ind}\bigl(L(H)^2\bigr),
\]
where \(L(H)\) is the line graph, the superscript denotes the square of a graph, and \(\operatorname{Ind}\) denotes the ordinary independence complex. Then there is an integral homotopy equivalence
\[
\boxed{\mathcal S(H)\simeq\bigvee^{20}S^2}.
\]
Moreover, the natural action of the full graph automorphism group \(G=\operatorname{Aut}(H)\), of order \(336\), on \(\widetilde H_2(\mathcal S(H);\mathbb Q)\) has the following **complete rational character**. For the subgroup \(G^+\cong\operatorname{GL}_3(\mathbb F_2)\) of order \(168\), preserving the point and line classes, the character is \(20,-4,2,0,-1\), on elements of respective orders \(1,2,3,4,7\). Every one of the other \(168\) automorphisms, exchanging point and line classes, has trace zero. The character distributions are

| Automorphism class | Number | Trace on \(\widetilde H_2\) |
|:---|---:|---:|
| Preserves the two classes, order \(1\) | 1 | 20 |
| Preserves the two classes, order \(2\) | 21 | -4 |
| Preserves the two classes, order \(3\) | 56 | 2 |
| Preserves the two classes, order \(4\) | 42 | 0 |
| Preserves the two classes, order \(7\) | 48 | -1 |
| Exchanges the two classes | 168 | 0 |

In particular,
\[
\widetilde H_2(\mathcal S(H);\mathbb Z)\cong\mathbb Z^{20},\qquad
\dim_{\mathbb Q}\widetilde H_2(\mathcal S(H);\mathbb Q)^G=0,
\]
and every other reduced integral homology group vanishes.

## Assumptions and scope
The graph is the fixed 14-vertex Heawood graph with Fano points and lines both indexed by nonzero binary vectors \(p,q\in\mathbb F_2^3\), with incidence exactly when \(p\cdot q=0\) in \(\mathbb F_2\). A graph edge is a flag \((p,q)\) with \(p\cdot q=0\); the 21 flags are listed lexicographically by integer binary encodings \(1,\ldots,7\). Two distinct flags \((p,q)\) and \((r,s)\) are compatible exactly when
\[
p\ne r,\quad q\ne s,\quad p\cdot s=1,\quad r\cdot q=1.
\]
A face is a set of pairwise compatible flags. This defines an abstract simplicial complex, including the empty face. A graph-induced matching is substantially more restrictive than an ordinary graph matching; consequently \(\mathcal S(H)\) is not the ordinary, extendible/perfect, or bounded-degree two-matching complex. Nor is it the differently defined vertex-based *induced matching complex*, in which selected graph vertices induce a subgraph of degree at most one.

## Proof
**1. Exhausting the finite complex.** The point-line rule produces \(21\) flags. Two independent complete algorithms generate faces. One checks all combinations of flags through size four by the explicit pairwise compatibility condition. The other builds a compatibility graph by demanding exactly two incidences between the four endpoints of each candidate flag pair and recursively enumerates all cliques. Both give exactly the face-count vector
\[
(f_{-1},f_0,f_1,f_2)=(1,21,84,84),
\]
with no four-flag faces. Thus \(\mathcal S(H)\) is two-dimensional. The complete finite loops and cross-checks are in `verify.py`.

**2. A graph of generators and exactly twenty free two-cells.** The `cell_certificate.json` file gives (a) a 20-edge spanning tree \(T\) in the one-skeleton, (b) an ordered sequence of 64 distinct two-simplices, and (c) the 20 complementary two-simplices. The checker verifies that the tree has 21 vertices with no cycle, and that at each stage one of the 64 listed triangles has precisely **two** boundary edges in the set of already eliminated one-cells and exactly **one** new boundary edge. At completion, all 84 one-skeleton edges have been accounted for.

Contracting \(T\) produces a homotopy-equivalent presentation CW complex with a single zero-cell, \(84-20=64\) one-cells, and 84 two-cells. Starting with the first listed triangle, its attaching word consists of one as-yet-uneliminated one-cell with exponent \(+1\) or \(-1\), because the other two boundary edges have become null in previous cancellations. Therefore a cellular change of attaching maps followed by an elementary one/two-cell cancellation eliminates that triangle together with that remaining one-cell. This step is valid even if the eliminated generator appears in other attaching words: those words are first adjusted using the triangle relation, a standard elementary Tietze/CW cancellation. Inducting over all 64 certified triangles removes every one-cell and exactly 64 two-cells without changing homotopy type. The 20 complementary two-cells then attach to a point, producing \(\bigvee^{20}S^2\). This is an integral *homotopy* statement, not an inference solely from rational or modular Betti numbers.

**3. Exhausting the full symmetry action.** Each invertible binary linear matrix \(A\in\operatorname{GL}_3(\mathbb F_2)\) induces a flag permutation
\[
(p,q)\longmapsto(Ap,A^{-T}q).
\]
Composing these with point-line duality \((p,q)\mapsto(q,p)\) generates 336 distinct graph automorphisms. They are all automorphisms: the connected bipartite Heawood graph has unique bipartition, and every bipartition-preserving automorphism induces a collineation of the Fano plane, all represented by the 168 invertible binary matrices. No additional side-interchanging automorphisms exist beyond the corresponding 168-element coset.

For each of the 336 resulting permutations \(g\) of the 21 flags, compute the exact reduced Lefschetz number from the complete simplicial chain representation:
\[
\widetilde L(g)=-1+
\sum_{\substack{\varnothing\ne\sigma\in\mathcal S(H)\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_{\sigma}).
\]
The sign is the orientation sign of the induced permutation of the ordered vertices of each fixed simplex. Because all nonzero reduced rational homology is in degree two by Step 2, the reduced Lefschetz number equals the trace on second homology. Exhausting the 336 automorphisms produces exactly the displayed six types and 336 total elements. The character-average identity gives
\[
\dim \widetilde H_2(\mathcal S(H);\mathbb Q)^G
=\frac{20+21(-4)+56(2)+42(0)+48(-1)+168(0)}{336}=0.
\]

## Verification
The complete standalone Python-standard-library verifier is `verify.py` and must be run beside `cell_certificate.json`; it needs no network access or external libraries. Execute `python3 verify.py` to reconstruct both face enumerations, check the 20-edge spanning tree and each of the 64 ordered two-cell eliminations, verify the 20 remaining two-cells, construct signed simplicial boundary matrices and verify their composition is zero, and compare exact boundary ranks over primes \(2\), \(3\), and \(5\). Those ranks are \(\operatorname{rank}\partial_1=20\) and \(\operatorname{rank}\partial_2=64\) for each of the three fields.

The verifier then enumerates all 336 Fano automorphisms, checks every transformed face is still a face, computes the complete signed trace character, and confirms that its mean is zero. The supplied `verification_output.txt` is the actual stdout from executing this exact source against this certificate, ending in `VERIFY_OK`. The certificate covers *all* faces, cancellation steps, and automorphisms for this one finite graph. It is not experimental sampling or an infinite-family assertion.

## Relationship to prior work
Joos, Rautenbach and Sasse's public 2013 paper defines induced matchings of subcubic graphs and develops extremal cardinality results. This motivates the graph-theoretic object, but its bounds do not give the topology of the complex of **all** induced matchings or its automorphism representation. Skupień's paper on the Petersen and Heawood graphs studies the strong chromatic index and the partition of Heawood's 21 edges into seven induced three-matchings; those facts do not imply the present 20-sphere homotopy classification.

The published Heawood **ordinary** matching-complex classification yields \(\bigvee^{16}S^4\), and a distinct published computation gives its 336-element ordinary-matching homology character. Both permit graph-edge subsets that are not induced matchings and thus neither statement determines this complex. The **perfect-matching** and **two-matching** complexes for the same graph have different face rules and known sphere decompositions; neither implies the present result. The edge-based complex here is also different from the vertex-based degree-at-most-one construction sometimes named the induced-matching complex. Searches for the alias \(\operatorname{Ind}(L(H)^2)\), explicit Heawood induced matchings, and their exact homotopy and characters did not identify a covering statement.

## Limitations
The calculation is specific to the Heawood graph and determines the full **rational character**, not a complete integral module decomposition or an equivariant homotopy classification. Exact enumeration supplements a finite CW cancellation proof; the standalone computer checks do not generalize to all incidence graphs without further work. Neither failed database search nor inspection of selected full texts can exclude every unindexed, inaccessible, or differently phrased earlier result; this is a residual originality risk. No independent mathematical audit has been performed.

## References
1. F. Joos, D. Rautenbach, T. Sasse, *Induced Matchings in Subcubic Graphs*, arXiv:1312.1110v1, first publicly submitted 2013-12-04, https://arxiv.org/abs/1312.1110.
2. Z. Skupień, *The Petersen and Heawood graphs make up graphical twins via induced matchings*, published in Discussiones Mathematicae Graph Theory, DOI 10.7151/dmgt.2394, publicly accessible version dated 2021-02-21, https://doi.org/10.7151/dmgt.2394.
3. *The Heawood matching complex is a wedge of sixteen 4-spheres*, published-finding corpus, identifier 7150930ba12a, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-heawood-matching-complex-is-a-wedge-of-sixteen-4-spheres--7150930ba12a.
4. *Full automorphism module of the Heawood matching complex*, published-finding corpus, identifier d7a042784870, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-full-operatorname-aut-h-module-of-the-heawood-matching-complex--d7a042784870.
5. *Perfect Morse reduction of the Heawood perfect-matching complex*, published-finding corpus, identifier 0994476b8c0d, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d.
6. *The Heawood two-matching complex is a wedge of six ten-spheres*, published-finding corpus, identifier 5bc5713358d6, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-heawood-two-matching-complex-is-a-wedge-of-six-10-spheres--5bc5713358d6.
