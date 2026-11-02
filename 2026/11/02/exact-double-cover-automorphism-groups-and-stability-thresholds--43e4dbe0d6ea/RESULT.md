# Exact double-cover automorphism groups and stability thresholds for clique bouquets

## Finding

For a finitely supported sequence of nonnegative integers \( (t_r)_{r\ge2} \) with \(t=\sum_{r\ge2}t_r\ge1\), form the *clique bouquet*
\[
X=K_1\vee\biggl(\bigsqcup_{r\ge2}t_r K_r\biggr),
\]
where \(\vee\) denotes graph join and \(K_1\) is the common hub. Let \(k=t_2\) be the number of triangular blades (the cliques comprising two peripheral vertices and the hub). Let \(BX=X\times K_2\) be its canonical bipartite double cover.

If \(t\ge2\), then, as abstract groups,
\[
\operatorname{Aut}(X)\cong\prod_{r\ge2}(S_r\wr S_{t_r}),
\qquad
\operatorname{Aut}(BX)\cong
\biggl(S_{2k}\times\prod_{r\ge3}(S_r\wr S_{t_r})\biggr)\times C_2,
\]
with empty factors trivial. The natural embedded subgroup \(\operatorname{Aut}(X)\times C_2\) has exact index
\[
[\operatorname{Aut}(BX):\operatorname{Aut}(X)\times C_2]
=\frac{(2k)!}{2^k k!}=(2k-1)!!,
\]
where the value at \(k=0\) is \(1\). In particular, for *all* \(t\ge1\), the bouquet is stable if and only if \(k\le1\). For \(k\ge2\), the graph is nontrivially unstable (connected, nonbipartite and twin-free).

The index equals the number of ways to re-pair the \(2k\) indistinguishable peripheral-edge atoms occurring after the two lifted hubs are deleted. Thus even when the sizes and numbers of larger blades vary arbitrarily, the full instability index depends only on the number of triangular blades. For a pure friendship graph \(K_1\vee kK_2\) with \(k\ge2\), its cover has automorphism group \(S_{2k}\times C_2\) and instability index \((2k-1)!!\).

## Assumptions and scope

Every graph is finite, simple and undirected. The parameter \(t_r\) counts distinguishable vertex sets of size \(r\), not ordered blades; graph automorphisms are allowed to permute blades of equal size. The product \(S_r\wr S_{t_r}\) is the standard imprimitive wreath product \(S_r^{t_r}\rtimes S_{t_r}\). The group descriptions are abstract isomorphisms; the designated expected subgroup need not be normal. *Stable* means that every automorphism of \(BX\) is induced by an automorphism of \(X\) and possibly simultaneous interchange of the two covering layers. The single-blade case \(t=1\) is \(K_{r+1}\), handled separately.

## Proof

**Step 1 (the original graph).** Suppose \(t\ge2\). The hub has degree \(N=\sum_{r\ge2}rt_r\), strictly larger than the peripheral degree \(r\) of any vertex in an \(r\)-blade: at least one other blade contributes at least two vertices. Hence every graph automorphism fixes the hub. Removing it leaves disjoint complete graphs, so permutations within equal-size blades and permutations of those blades give precisely \(\prod_{r\ge2}(S_r\wr S_{t_r})\).

**Step 2 (recognizing the two lifted hubs).** The two lifts \(h_0,h_1\) of the hub each have degree \(N\); all other lifted vertices have degree \(r<N\). Thus \(\{h_0,h_1\}\) is characteristic under all cover automorphisms, and the automorphisms fixing both lifts form a subgroup of index two. Every edge of the cover joins opposite bipartition classes.

**Step 3 (deleting both lifted hubs).** Removing \(h_0,h_1\) leaves a disjoint union of the covers \(B(K_r)\), one per original peripheral blade. For \(r=2\), \(B(K_2)\) is the union of two independent edges: altogether the \(k\) triangular blades produce exactly \(2k\) indistinguishable edge components. Each edge has one endpoint adjacent to \(h_0\), and its other endpoint adjacent to \(h_1\). Consequently a cover automorphism fixing both hubs permutes these \(2k\) edges arbitrarily and must take the endpoints with the same prescribed hub adjacency to each other. The induced action is exactly \(S_{2k}\).

For \(r\ge3\), \(B(K_r)\) is the connected graph \(K_{r,r}\) with a perfect matching removed; for \(r=3\) it is a six-cycle. Its vertices on one shore are exactly the neighbors of \(h_0\) among the component vertices, and those on the other shore are the neighbors of \(h_1\). Distinct sizes \(r\) have distinct component orders, so cannot mix. Any side-preserving automorphism of \(B(K_r)\) must permute the \(r\) missing opposite-shore pairs simultaneously, and hence is uniquely determined by an arbitrary permutation of \(r\) labels. Thus the side-preserving component group is \(S_r\), not two independent symmetric groups. Permuting equal-size components yields exactly \(S_r\wr S_{t_r}\). This proves that the pointwise stabilizer of \(h_0,h_1\) is
\[
H\cong S_{2k}\times\prod_{r\ge3}(S_r\wr S_{t_r}).
\]

**Step 4 (splitting off the hub exchange).** Define an involution \(\sigma\) on \(BX\) interchanging \(h_0,h_1\); on each peripheral two-vertex edge component it exchanges its endpoints, and on each larger \(B(K_r)\) component it exchanges the two shores while keeping the underlying vertex label fixed. These operations preserve all cover edges. The involution commutes with every element of \(H\): on an edge component endpoint exchange is canonical, and on a larger component labelwise shore exchange centralizes diagonal label permutations and blade permutations. Every cover automorphism either lies in \(H\) or is the product of an element of \(H\) with \(\sigma\). Hence \(\operatorname{Aut}(BX)\cong H\times\langle\sigma\rangle\), proving the asserted full-group decomposition.

**Step 5 (index and exceptional one-blade case).** The canonical expected subgroup is generated by graph automorphisms lifted to both layers and the global layer swap. Within \(H\), it preserves precisely the original pairing of the \(2k\) edge components into \(k\) pairs (one pair per triangular blade), acting on them by \(S_2\wr S_k\); on all larger components it gives the full wreath groups already identified. Because the global layer swap lies in \(H\sigma\) and its product with \(\sigma\) preserves the original pairs, the expected subgroup has order
\[
2\,(2!)^k k!\prod_{r\ge3}(r!)^{t_r}t_r!,
\]
whereas the full cover group has order
\[
2\,(2k)!\prod_{r\ge3}(r!)^{t_r}t_r!.
\]
The ratio is \((2k)!/(2^kk!)\). It equals one for \(k=0,1\) and exceeds one for \(k\ge2\). If \(t=1\), the graph is \(K_{r+1}\) and its double cover is the crown \(K_{r+1,r+1}\) with a perfect matching removed. Here \(r+1\ge3\); its two shore-preserving and shore-exchanging automorphisms give precisely \(S_{r+1}\times C_2\). This is the expected subgroup, so the single-blade graph is stable.

Finally all bouquets are connected and contain triangles. No two different peripheral vertices have the same open neighborhood: within a blade each vertex omits itself but sees all its distinct blade-mates, and vertices in different blades have differing sets of peripheral neighbors. The hub also has a different open neighborhood. Hence each graph with \(k\ge2\) is twin-free and its instability is nontrivial. \(\square\)

## Verification

The standalone program `verify_double_cover.py` constructs each bouquet and its canonical double cover, enumerates all graph automorphisms independently using graph isomorphism search, and compares the results against the structural group-order formulas. It covers eleven parameter lists, including mixed blade sizes, the stable/unstable transition, and the first three-factorial-index values. Running `python verify_double_cover.py` prints `VERIFY_OK cases= 11` when all checks pass. This finite check is not relied on for the proof for arbitrary blade counts and orders.

## Relationship to prior work

The 2026 work of Bychawski, Hujdurović, Mitrović and Verret establishes an asymptotic hierarchy for double-cover instability and studies a four-added-vertex construction. The 2023/2024 work of Hujdurović and Mitrović already proves that graphs from that construction can be nontrivially unstable. In particular, the existence of instability for bouquets with at least two triangular blades is **not claimed as new**: choosing pairs of peripheral vertices gives instances of this construction. The present theorem determines the *entire* automorphism group for arbitrary mixed clique bouquets, gives the exact growing index, and establishes a sharp stability criterion. Mizzi's 2026 two-fold-automorphism framework provides an alternative viewpoint on cover symmetries but does not state this mixed-bouquet group formula in the inspected material. Literature searches under friendship, windmill, Kronecker cover, bipartite double cover, two-fold automorphisms, and clique bouquet did not identify an equivalent group decomposition; this does not prove absolute historical novelty.

## Limitations

The theorem applies only to a join of one hub with a disjoint union of cliques of peripheral order at least two, and does not classify covers of arbitrary block graphs or all windmill-like joins. The group isomorphism is not an assertion that the expected subgroup is normal. Relevant historical literature may contain a stronger general automorphism classification from which this special case follows. The finite software check explores only named small inputs, with the infinite family established by the mathematical argument.

## References

1. Bartłomiej Bychawski, Ademir Hujdurović, Đorđe Mitrović and Gabriel Verret, *Asymptotical results on the automorphism groups of canonical double cover of graphs*, arXiv:2610.30373v1 (2026-10-21). https://arxiv.org/html/2610.30373v1
2. Ademir Hujdurović and Đorđe Mitrović, *Some conditions implying stability of graphs*, Journal of Graph Theory **105** (2024), 98–109, DOI:10.1002/jgt.23018. https://onlinelibrary.wiley.com/doi/10.1002/jgt.23018
3. Russell Mizzi, *Lifting and Folding: A Framework for Unstable Graphs and TF-Cousins*, arXiv:2603.27559 (2026). https://arxiv.org/abs/2603.27559
