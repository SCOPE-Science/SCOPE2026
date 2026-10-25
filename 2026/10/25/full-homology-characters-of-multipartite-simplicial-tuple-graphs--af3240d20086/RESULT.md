# Full homology characters of multipartite simplicial tuple graphs

## Finding
For each integer \(r\ge2\), put \(q=2r+1\) and select positive integers \(a_0,\ldots,a_{q-1}\). Let \(X\) be the join of \(q\) discrete vertex sets \(A_i\) with \(|A_i|=a_i\). The simplicial \(r\)-tupling \(Y=D^r(X)\) is a connected graph; hence it has the **integral** homotopy type
\[
Y\simeq\bigvee^{E-V+1}S^1,\qquad
V=\sum_{\substack{I\subseteq[ q]\\|I|=r}}\prod_{i\in I}a_i,\quad
E=\frac12\binom{2r}{r}\sum_{\ell=0}^{q-1}\prod_{i\ne\ell}a_i.
\]
In addition, the full character on \(H_1(Y;\mathbb Q)\) of every automorphism that permutes equally sized color parts, while bijecting the elements inside parts, is computed by the explicit fixed-point formulas below. The formula includes orientation reversals of edges, which cannot be recovered from Betti numbers.

## Assumptions and scope
The vertex set of \(Y\) comprises the \(r\)-element faces of \(X\). A set of such vertices is a simplex of \(Y\) precisely when the faces are pairwise disjoint and their union is a face of \(X\). Each face of \(X\) contains at most one vertex from each \(A_i\). We require exactly \(q=2r+1\) nonempty color parts and \(r\ge2\). No restriction on the sizes other than positivity is used.

An allowed automorphism \(g\) induces a size-preserving permutation \(\pi\) of the color indices and bijections \(A_i\to A_{\pi(i)}\). For every cycle \(c\) of \(\pi\), let \(f_c\) be the number of fixed points of the composite bijection around that cycle (this is independent of the starting index in \(c\)). Define
\[
V_g=[z^r]\prod_{c\text{ a cycle of }\pi}(1+f_c z^{|c|}).
\]
For a color index \(\ell\) fixed by \(\pi\), let \(\mathcal C_\ell\) denote all cycles of \(\pi\) supported in the other \(2r\) colors, and put
\[
F_\ell=\prod_{c\in\mathcal C_\ell}f_c,\quad
h_\ell=[z^r]\prod_{c\in\mathcal C_\ell}(1+z^{|c|}),\quad
k_\ell=|\mathcal C_\ell|.
\]
Write \(\delta_\ell=1\) when every cycle in \(\mathcal C_\ell\) has even length, and \(\delta_\ell=0\) otherwise. Empty sums contribute zero. Define
\[
E_g^+=\sum_{\ell:\pi(\ell)=\ell}\frac{F_\ell h_\ell}{2},\qquad
E_g^-=\sum_{\ell:\pi(\ell)=\ell}\delta_\ell F_\ell 2^{k_\ell-1}.
\]
The fractions are integers: \(h_\ell\) is even by complementation. For \(\delta_\ell=1\), necessarily \(k_\ell\ge1\). The complete rational character is
\[
\boxed{\operatorname{tr}(g\mid H_1(Y;\mathbb Q))=1-V_g+E_g^+-E_g^-.}
\]

## Proof
**1. Dimension and face counts.** A vertex of \(Y\) chooses \(r\) distinct color classes and one vertex in each selected class. This gives \(V\). Two vertices of \(Y\) form an edge exactly when their color supports are disjoint. There cannot be three pairwise disjoint \(r\)-subsets of \(q=2r+1\) colors, since \(3r>2r+1\) for \(r\ge2\). Hence \(Y\) has dimension one. An edge uses exactly \(2r\) of the colors, leaving one omitted class \(\ell\); partitioning these colors into two unordered \(r\)-subsets gives \(\binom{2r}{r}/2\) options, and selecting one element of every used class gives \(\prod_{i\ne\ell}a_i\) options. This proves the edge formula.

**2. Connectedness and integral homotopy.** Identify each graph vertex with its color support and its selected elements. The support projection has base graph \(\mathrm{KG}(2r+1,r)\). If two \(r\)-supports differ by one color, their union has \(r+1\) colors, so the complementary \(r\)-support is adjacent to both. Therefore every pair of adjacent vertices in the Johnson graph on \(r\)-supports is joined by a two-edge walk in the Kneser graph. The Johnson graph is connected, so the Kneser graph is connected. Every vertex in each support fiber is connected to every vertex of each disjoint support fiber. In particular, two vertices in the same fiber have a common neighbor, and arbitrary base support walks lift. Thus \(Y\) is connected. Every finite connected graph deformation retracts onto a bouquet with \(E-V+1\) circles by contracting a spanning tree, proving the homotopy and integral homology statement.

**3. Fixed vertices.** An \(r\)-face is fixed by \(g\) if and only if its chosen colors are a union of full cycles of \(\pi\), and its chosen elements along each selected cycle form a fixed orbit under the composite return map. Hence the number of fixed vertices is \(V_g\).

**4. Fixed oriented edges.** Each unordered edge has a unique omitted color \(\ell\). If it is setwise fixed by \(g\), then \(\pi(\ell)=\ell\). Within the \(2r\) remaining colors, \(g\) must preserve or swap its endpoint support classes. To preserve each endpoint, every cycle in \(\mathcal C_\ell\) must lie entirely in one support. Exactly \(h_\ell\) labeled choices of the first support have size \(r\), with complementary choices representing the same unordered edge; the selected elements must be fixed around every color cycle, giving \(F_\ell\). The count of pointwise-fixed edges is \(E_g^+\).

To exchange the two endpoints, the support class must alternate along each color-permutation cycle; this is possible exactly when all its cycle lengths are even. Each such cycle has two alternating assignments, independently; swapping the endpoints identifies the two global complementary assignments. There are \(2^{k_\ell-1}\) unoriented support assignments, and again \(F_\ell\) compatible element selections. Thus the number of endpoint-reversing edges is \(E_g^-\). This proves both signed formulas without double counting.

**5. Rational first homology.** Orient each graph edge once and form the cellular chain sequence \(C_1(Y;\mathbb Q)\to C_0(Y;\mathbb Q)\). The trace of \(g\) on \(C_0\) is \(V_g\); its trace on \(C_1\) is \(E_g^+-E_g^-\) because endpoint exchange changes orientation. The Lefschetz trace identity, with \(H_0(Y;\mathbb Q)\) the trivial one-dimensional representation, gives \(V_g-(E_g^+-E_g^-)=1-\operatorname{tr}(g\mid H_1)\). Rearrangement proves the formula.

## Verification
A standalone standard-library Python program, `verify.py`, constructs every graph vertex and edge and checks signed permutation traces against the closed formula. Test families include \(r=2\) with class sizes \((2,2,2,2,2)\), \((2,3,2,3,1)\), and \((1,1,1,1,1)\), and \(r=3\) with seven size-two parts, totaling 495 independently enumerated automorphism tests. The graph sizes and first homology ranks include \((V,E,E-V+1)=(40,240,201)\) and \((280,4480,4201)\). As a nontrivial sign check, the color permutation \((0\ 1)(2\ 3)\), with trivial internal bijections and all part sizes two, has trace \(-7\) on \(H_1\): its fixed counts are \((V_g,E_g^+,E_g^-)=(4,4,8)\). These finite checks support, but do not replace, the proof of the uniform theorem.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial \(r\)-tupling and proved a general connectivity theorem for \(D^r(X)\) in *The double of a simplicial complex* (2025), Definition 2.1 and Theorem A. Their results motivate the specific near-threshold \(2r+1\)-color case, but do not state the present graph identification, arbitrary part-size Euler characteristic, or full color-permutation-and-fiber character. Shareshian and Wachs study symmetric-group representations on homology of complete hypergraph matching complexes rather than these colored, vertex-inflated odd Kneser graphs. The ordinary cycle-space identity for graphs is used explicitly as a standard ingredient, not claimed as novel. The combination yields a character formula with two genuinely distinct fixed-edge contributions.

## Limitations
This is an exact family-specific calculation, not a classification of simplicial \(r\)-tuplings in general. Only automorphisms induced by color-preserving or size-preserving color-relabeling bijections are addressed; this is a natural large symmetry group but need not equal the entire abstract graph automorphism group in every degenerate size case. Rational representation characters, not an integral decomposition into indecomposable lattices, are determined. Independent novelty review has not been conducted; equivalent formulations in unindexed literature remain a residual risk.

## References
1. Kathryn Lesh, Bridget Schreiner and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1, 12 June 2025. https://arxiv.org/abs/2506.10436.
2. John Shareshian and Michelle Wachs, *Top homology of hypergraph matching complexes, p-cycle complexes and Quillen complexes of symmetric groups*, arXiv:0808.3114; author-hosted text https://www.math.miami.edu/~wachs/papers/tophom.pdf.
