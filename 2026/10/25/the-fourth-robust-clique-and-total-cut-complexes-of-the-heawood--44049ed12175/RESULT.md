# The fourth robust clique and total cut complexes of the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano projective plane. Let \(\operatorname{Cliq}_{4}(H)\) consist of all vertex sets \(W\) for which \(\alpha(H[W])\leq3\), and let \(\Delta^{t}_{4}(H)\) be the total fourth cut complex, whose facets are complements of independent four-sets. Then the following paired integral homotopy classification holds:

\[
\left|\operatorname{Cliq}_{4}(H)\right|\simeq\bigvee^{92} S^{5},
\qquad
\left|\Delta^{t}_{4}(H)\right|\simeq\bigvee^{92}S^{6}.
\]

Moreover, \(\Delta^{t}_{4}(H)\) is a pure nine-dimensional complex that is not shellable.

## Assumptions and scope

Vertices \(0,\ldots,6\) are points and vertices \(7,\ldots,13\) correspond, in order, to the seven Fano lines
\[
\{0,1,3\},\ \{0,2,5\},\ \{0,4,6\},\ \{1,2,4\},\ \{1,5,6\},\ \{2,3,6\},\ \{3,4,5\}.
\]
An edge joins a point to an incident line and no other edges exist. In particular, every two different lines meet in one point, so \(H\) has no four-cycle. The claim is for this graph and fourth robustness only; no statement is made about arbitrary bipartite or higher-girth graphs.

For a graph \(G\), \(\alpha(G[W])\) means the largest size of an independent subset of the induced subgraph on \(W\). Thus the forbidden minimal nonfaces of \(\operatorname{Cliq}_{4}(H)\) are precisely the independent vertex four-sets. The total cut complex satisfies the **combinatorial Alexander duality identity**
\[
\Delta^{t}_{4}(H)=\operatorname{Cliq}_{4}(H)^{*},\qquad
K^{*}=\{\sigma\subseteq V(H):V(H)\setminus\sigma\notin K\}.
\]

## Proof

**1. An exhaustive, checkable integral Morse model.** Encode each subset of the fourteen vertices by a fourteen-bit nonnegative integer. The included `morse_certificate.json` lists an explicit partial matching of the nonempty face poset of \(\operatorname{Cliq}_{4}(H)\), with each pair represented by its lower and upper bit masks. It also explicitly lists the unmatched face masks. The included `robust4_verify.py` reconstructs all faces independently in two ways: it tests containment of each independent four-set, and it computes maximum independent-set sizes by a separate bit-mask recurrence. Both methods yield exactly \(3032\) faces including the empty face, with \(147\) forbidden independent four-sets and nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(14,91,364,854,1092,616).
\]

The certificate contains \(1469\) disjoint pairs of incident faces differing by exactly one vertex, and exactly \(93\) unmatched nonempty faces: one vertex and \(92\) five-simplices. The verifier checks that the matched faces and the critical faces partition all \(3031\) nonempty faces. It then constructs **every** covering relation in the nonempty-face Hasse diagram and orients relations downward except that matched covering relations are oriented upward. There are exactly \(13846\) such relations. An exhaustive topological sort visits all \(3031\) faces, establishing that this oriented graph is acyclic. These finite statements can be replayed directly from the two standalone files; they do not depend on sampling or a precomputed homology table.

By the standard acyclic-matching theorem of discrete Morse theory, the geometric realization is homotopy equivalent to a CW complex with one zero-cell and exactly \(92\) five-cells, and no other cells. There is no positive-dimensional lower skeleton for the attaching maps, so this CW complex is precisely a wedge of \(92\) five-spheres. This establishes the first assertion **integrally**, independently of the ancillary mod-two boundary computations.

**2. The Alexander-dual homotopy type.** The combinatorial Alexander duality isomorphism for fourteen vertices gives, for all integers \(i\),
\[
\widetilde H_i(\Delta^{t}_{4}(H);\mathbb Z)
\cong \widetilde H^{11-i}(\operatorname{Cliq}_{4}(H);\mathbb Z).
\]
Consequently its only nonzero reduced integral homology is \(\widetilde H_6\cong\mathbb Z^{92}\). The total cut complex contains the entire two-skeleton of the simplex on fourteen vertices: removing any set of at most three vertices leaves at least four vertices in either one of the two seven-element bipartition classes, an independent set. Hence every vertex subset of size at most three is a face of \(\Delta^{t}_{4}(H)\), making the complex simply connected. Its integral homology and simple connectivity imply, by Hurewicz and the homology version of Whitehead's theorem, a homotopy equivalence with \(\bigvee^{92}S^6\). More concretely, the Hurewicz isomorphism supplies \(92\) sphere maps realizing an integral homology basis; their wedge is a homology equivalence between simply connected CW complexes.

**3. Non-shellability.** The \(147\) independent four-sets are precisely the complements of the \(147\) facets of \(\Delta^{t}_{4}(H)\); hence this dual complex is pure of dimension \(9\). A pure shellable complex has reduced homology only possibly in its top dimension. Here \(\widetilde H_6\cong\mathbb Z^{92}\) is nonzero, with \(6<9\), so the complex is not shellable.

## Verification

Execute `python robust4_verify.py morse_certificate.json` with Python 3. The program uses only the standard library. Its checks cover all \(2^{14}\) vertex subsets; all \(147\) independent four-sets; all \(3031\) nonempty faces; all \(1469\) matched pairs; all \(13846\) Hasse covers; and the dual complex's \(13352\) faces, \(147\) facets and complete two-skeleton. Independent mod-two boundary reductions give reduced Betti ranks \((0,0,0,0,0,92)\), corroborating—but not replacing—the integral discrete-Morse proof. The expected final output line is `VERIFY_OK`. See `VERIFICATION.md` for precise checks and scope.

## Relationship to prior work

Filakovský introduced the robust-clique name and analyzed \(k\)-robust clique complexes of square-sequence graphs, proving integral sphere-wedge statements at \(k=2,3\), with certain \(k\geq4\) edge-gluing cases. Every nonempty square-sequence graph contains a four-cycle; the Heawood graph does not. Thus the cited grid/square-sequence conclusions do **not** imply this fourth-level incidence-graph computation. The prior work also identifies the Alexander dual connection to total cut complexes.

Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue developed total cut complexes and computed several families, including complete bipartite graphs. Carnero Bravo established general connectivity bounds and homotopy results for powers of cycles, complete multipartite graphs, and other specified families. A Heawood incidence graph is neither complete bipartite nor a square-sequence graph, nor one of those classified graph families; the general bounds alone do not determine the claimed \(92\)-generator homotopy type.

The matched certificate, rather than any previous homotopy formula, supplies the new graph-specific fact. No priority claim beyond the comparison actually performed is intended.

## Limitations

This is an exact, finite, computer-assisted homotopy classification for the specifically labeled Heawood graph; it is **not** an infinite-family theorem and does not settle proposed square-sequence conjectures. The integer homotopy type is certified by exhaustive face-poset matching and the standard discrete-Morse theorem; merely computing mod-two ranks would not suffice. The stated Alexander-dual conclusion uses standard integral Alexander duality and a separately proved simple-connectivity condition. Literature coverage remains subject to ordinary bibliographic uncertainty. Independent mathematical review has not been performed.

## References

1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first publicly posted 2026-02-11. https://arxiv.org/html/2602.11365
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first publicly posted 2026-02-24. https://arxiv.org/pdf/2602.21427
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first publicly posted 2022-09-27. https://arxiv.org/pdf/2209.13503
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), Sections 3.3–3.4 and 4.2.
