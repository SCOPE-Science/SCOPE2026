# Complete furtherness barcodes of Steiner incidence spaces

## Finding
Let \((V,\mathcal B)\) be a nontrivial Steiner \(2\!\!-\!\!(v,k,1)\) design: \(2\le k<v\), every block has \(k\) points, and every unordered pair of distinct points lies in exactly one block. Put \(r=(v-1)/(k-1)\), \(b=vr/k\), \(\beta=(k-1)b-v+1\), and \(\alpha=(k-1)(v-k)\). Construct the finite \(T_0\) Alexandrov space \(P\) from the height-two incidence poset whose minimal elements are points, maximal elements are blocks, and \(p<B\) exactly when \(p\in B\).

For every root \(x\in P\), use the furtherness filtration \(F_x(t)=\Delta(\{y\in P:|\downarrow y\setminus\downarrow x|\le t\})\), where \(\Delta\) denotes the order complex and \(t\in\mathbb R\). Over **every** coefficient field, the complete nonzero barcodes, with interval multiplicities, are:

For a point root \(p\):
\[
\mathrm{Dgm}_0(F_p)=\{[0,\infty)\}\sqcup(v-1)\{[1,k)\},\qquad
\mathrm{Dgm}_1(F_p)=\beta\{[k+1,\infty)\}.
\]
For a block root \(B\):
\[
\begin{split}
\mathrm{Dgm}_0(F_B)&=\{[0,\infty)\}\sqcup(v-k)\{[1,k)\},\\
\mathrm{Dgm}_1(F_B)&=\alpha\{[k,\infty)\}\sqcup(\beta-\alpha)\{[k+1,\infty)\}.
\end{split}
\]
All barcodes in degrees at least two are empty. Moreover \(\beta-\alpha=(k-1)[b-1-k(r-1)]\), counting an exact number of cycles associated with blocks disjoint from \(B\), and every positive-degree class persists forever. In degree one, point and block roots have bottleneck distance exactly \(1\).

Thus the unordered collection of **all rooted barcodes in all homological degrees**, with roots counted with multiplicities, depends only on \((v,k)\), not on the isomorphism type of the design. In particular, the 80 nonisomorphic Steiner triple systems on 15 points give 80 pairwise **nonhomotopy-equivalent finite spaces** with identical complete rooted furtherness-persistence profiles. This last assertion concerns ordinary homotopy of finite Alexandrov spaces, not merely weak homotopy of their order complexes.

## Assumptions and scope
The design is simple and nontrivial, with \(v>k\ge2\). Each unordered pair belongs to one block. The parameters \(r,b\) are necessarily integral; \(r\ge2\). The topology has principal opens \(\downarrow x\). Furtherness is the asymmetric function \(\Psi(x,y)=|\downarrow y\setminus\downarrow x|\) from Badra and Singh. The filtration uses inclusive sublevels, begins empty for \(t<0\), and is constant between its integer critical values. Ordinary unreduced homology is used in degree zero, over any field; interval endpoints follow the half-open convention. In fact, all positive-dimensional integral homology groups at each stage are free, and the inclusion maps in degree one are injective.

## Proof
**1. Furtherness weights.** For a point \(a\), \(\downarrow a=\{a\}\); for a block \(C\), \(\downarrow C=\{C\}\cup C\). Consequently, if the root is a point \(p\), all other points enter at time \(1\), each block through \(p\) at \(k\), and each block not through \(p\) at \(k+1\). The root itself enters at \(0\). If the root is a block \(B\), its \(k\) points and the block enter at \(0\), every other point at \(1\), every other block meeting \(B\) at \(k\), and every disjoint block at \(k+1\). Distinct blocks of a Steiner two-design intersect in at most one point, so there are no other weights.

**2. Point-root topology.** The order complex of this height-two poset is exactly its bipartite incidence graph (no chains have length three). At time \(1\), all \(v\) point vertices are isolated. The \(r\) blocks through \(p\) enter at time \(k\). They form a tree: every point other than \(p\) belongs to exactly one such block, by uniqueness of the block through the pair \(\{p,a\}\). The tree is connected, has \(v+r\) vertices and \(kr=v+r-1\) edges. Hence the \(v-1\) components born at time \(1\) die at \(k\) and no cycle is yet present. Adding all remaining blocks at \(k+1\) gives the full connected incidence graph, with \(v+b\) vertices and \(kb\) edges. Its first Betti number is \(kb-(v+b)+1=\beta\), so precisely \(\beta\) essential first-homology bars begin at \(k+1\).

**3. Block-root topology.** At time \(0\), the root block and its incident \(k\) points form a tree. At \(1\), the remaining \(v-k\) points appear as isolated vertices. A block meeting \(B\) in exactly one point appears at \(k\). Because each of the \(k\) points of \(B\) lies on exactly \(r\) blocks, and two distinct points of \(B\) cannot lie together on another block, the number of blocks present at \(k\) is \(b_*=1+k(r-1)\). Every point outside \(B\) is joined to a point inside \(B\) via its unique block through that point and any fixed point of \(B\). Therefore the intermediate incidence graph is connected and has \(v+b_*\) vertices and \(kb_*\) edges. Its cycle rank is
\[
(k-1)b_*-v+1=(k-1)(v-k)=\alpha,
\]
where \(r(k-1)=v-1\) was used. The final graph has cycle rank \(\beta\). All further blocks are disjoint from \(B\), so exactly \(\beta-\alpha=(k-1)(b-b_*)\) more independent cycles are created at \(k+1\).

**4. Persistence and homotopy separation.** An inclusion of graphs induces an injection on integral first homology, because there are no two-cells and every first cycle in a subgraph remains a cycle in the larger graph. Thus the cycle-rank increments in parts 2–3 are exactly the persistent first-homology birth multiplicities, with no finite bars. All complexes are graphs, proving absence of higher-dimensional homology. The degree-zero barcodes follow from the explicitly identified component merges. The two first-homology barcodes have equal numbers of essential intervals, with \(\alpha>0\) intervals born at consecutive integer times, so their bottleneck distance is \(1\); infinite intervals cannot be matched to the diagonal.

Finally, each minimal point lies below \(r\ge2\) incomparable maximal blocks, and each maximal block lies above \(k\ge2\) incomparable minimal points. Therefore the incidence poset has no up or down beat point. Stong's finite-space core theorem says that homotopy-equivalent beat-point-free finite \(T_0\) spaces must be homeomorphic. A homeomorphism of these posets is precisely a design isomorphism, because it preserves the minimal and maximal elements and their order incidences. There are 80 nonisomorphic Steiner triple systems of order \(15\) by the established classification. They therefore give the asserted 80 distinct finite-space homotopy types despite identical per-root barcodes.

## Verification
A standalone verifier, `verify.py`, constructs four finite Steiner designs from scratch: all pairs on five points, the Fano plane, the affine plane of order three, and the 15-point binary projective-space triple system. It checks the pair-coverage axioms, reconstructs the principal opens and furtherness weights, and independently computes the complete graph-persistence barcodes by an elder-rule component-merger and cycle-creation algorithm for **every root**. The resulting examples have \((v,k,b,\alpha,\beta)=(5,2,10,3,6),(7,3,7,8,8),(9,3,12,12,16),(15,3,35,24,56)\), respectively; all match the formulas. Successful execution prints `VERIFY_OK`. This exhaustive finite test is auxiliary evidence; the general proof is the design-incidence argument above and does not rely on enumerating all designs.

## Relationship to prior work
Badra and Singh (2026, arXiv:2610.16386v1) define the rooted furtherness filtration and analyze its **zeroth** persistent homology, including a general birth and death framework. Their earlier article (arXiv:2603.18580v1, Corollary 2.17) establishes the cardinality formula for furtherness. The contribution here is the complete all-degree barcode classification for arbitrary Steiner \(2\)-design incidence spaces, especially the two distinct first-homology birth stages and the finite-space homotopy nonseparation for 80 examples. Generic persistence algorithms and graph cycle-rank formulas are used, but the explicit design-wide profile is not supplied by those general methods without the incidence-geometry analysis.

Related results for Lovász neighborhood complexes and graph-metric Vietoris–Rips complexes of Steiner/projective-plane incidence graphs concern **different simplicial complexes and different filtrations**. Their aggregate circle multiplicities can coincide with the final cycle rank \(\beta\), but this does not imply the root-dependent birth multiplicities here. The classification of 80 Steiner triple systems is previously known and is used only to establish the cardinality of the indistinguishable family; it is not claimed as new.

## Limitations
The theorem applies to Steiner \(2\)-designs with pair multiplicity one, not to arbitrary block designs or hypergraphs. It does not claim that the individual finite-space homotopy types are indistinguishable by all conceivable invariants: only the specified rooted homological persistence barcodes are universal. Homotopy equivalence of the finite Alexandrov spaces must not be confused with weak homotopy equivalence of their order complexes. No classification of all nonisomorphic designs is proved here. No independent audit or priority certification has been performed; unpublished or unindexed equivalent calculations cannot be excluded.

## References
1. A. Badra and H. K. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1, first posted 12 October 2026, especially Sections 2–5 and 7. https://arxiv.org/abs/2610.16386
2. A. Badra and H. K. Singh, *Furtherness in finite topological spaces*, arXiv:2603.18580v1, 19 March 2026, Corollary 2.17. https://arxiv.org/abs/2603.18580
3. R. E. Stong, *Finite topological spaces*, Transactions of the AMS **123** (1966), 325–340; finite-space core uniqueness also reviewed by J. A. Barmak and E. G. Minian, *Simple homotopy types and finite spaces*. https://mate.dm.uba.ar/~jbarmak/simplerevisedversion.pdf
4. D. Heinlein et al., *Enumerating Steiner triple systems*, Journal of Combinatorial Designs **31** (2023), 479–495; classification count \(80\) for order \(15\). https://doi.org/10.1002/jcd.21906
