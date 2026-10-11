# Three-cut complexes of graphs without short cycles: sphere wedges and symmetry characters

## Finding

**Theorem.** Let \(G=(V,E)\) be any finite simple graph on \(n\ge7\) vertices, not necessarily connected, with no triangle and no cycle of length four. Let \(\Delta_3(G)\) denote the ordinary three-cut complex: its facets are \(V\setminus T\) for all three-element sets \(T\subset V\) for which \(G[T]\) is disconnected. Set
\[
p(G)=\sum_{v\in V}\binom{\deg_G(v)}{2},\qquad b(G)=\binom{n-1}{2}-p(G),\qquad d=n-4.
\]
Then \(b(G)\) is a nonnegative integer and
\[
\Delta_3(G)\simeq\bigvee^{b(G)}S^d.
\]
The empty wedge is a point. In particular, \(\widetilde H_i(\Delta_3(G);\mathbb Z)=0\) for \(i\ne d\), while \(\widetilde H_d(\Delta_3(G);\mathbb Z)\cong\mathbb Z^{b(G)}\).

The entire rational homology representation of the finite group \(\operatorname{Aut}(G)\) is given explicitly. For \(g\in\operatorname{Aut}(G)\), write \(f(g)=|\{v:g(v)=v\}|\), let \(\epsilon(g)\) be the sign of its permutation of \(V\), and let \(\mathcal P(G)\) consist of unordered vertex triples inducing a two-edge path. Define
\[
\tau(g)=\sum_{T\in\mathcal P(G),\ gT=T}\operatorname{sgn}(g|_T).
\]
Every fixed path triple has its middle vertex fixed and its ends either fixed or interchanged; thus each summand is respectively \(+1\) or \(-1\). Then the character of the only potentially nonzero reduced rational homology is
\[
\boxed{\quad\chi_d(g)=\epsilon(g)\left(\frac{f(g)^2-f(g^2)}2-f(g)+1-\tau(g)\right).\quad}
\]
These character values determine the full rational \(\operatorname{Aut}(G)\)-module up to isomorphism. This is an ordinary (nonequivariant) homotopy equivalence together with an equivariant homology statement; **no equivariant wedge decomposition is asserted**.

## Assumptions and scope

Only simple graphs with \(n\ge7\) and no cycles of lengths three or four are covered; cycles of length five and longer, multiple connected components, degree-one vertices and isolated vertices are allowed. Graph automorphisms permute the same original \(n\) vertices. All reduced integral homology is computed for the ordinary, not total, three-cut complex. No shellability conclusion is asserted: a wedge-of-spheres homotopy type alone cannot establish shellability.

The graph \(G\) is combinatorial, and \(\deg_G(v)\) counts distinct adjacent vertices. No external software or unproved infinite enumeration is needed for the theorem.

## Proof

**1. Dual two-dimensional complex.** The combinatorial Alexander dual \(X=\Delta_3(G)^\vee\) comprises those sets \(S\subseteq V\) containing **no** disconnected induced triple. Every singleton and pair is therefore a face of \(X\). A triple is in \(X\) exactly when it induces a connected graph; because \(G\) is triangle-free, these are precisely the induced two-edge paths \(\mathcal P(G)\). A set of four vertices cannot be a face of \(X\): if all its four triples were connected, then each induced triple would have exactly two edges, so double-counting edges would give four edges on those four vertices. A triangle-free simple four-vertex graph with four edges contains a four-cycle, contrary to hypothesis. Thus \(X\) is the complete graph on \(V\), with precisely one triangular two-face for each induced two-edge path, and has no higher-dimensional simplices. Each two-edge path is determined by its middle vertex and an unordered pair of its neighbors, giving exactly \(p(G)\) triangular faces.

**2. Private-edge elementary collapses.** For each path \(u-v-w\), the unordered endpoint pair \(\{u,w\}\) is an edge of the one-skeleton of \(X\), but is not an edge of \(G\). It lies in no other triangular face of \(X\): another middle vertex adjacent to both \(u\) and \(w\) would create a four-cycle, while the same middle vertex gives the same triple. Hence it is a free simplicial face of the unique triangle \(\{u,v,w\}\). The endpoint pairs of different triangles are distinct. Collapse simultaneously, or in any order, each triangle against its free endpoint edge. The result is a connected one-dimensional CW complex \(Y\) with \(n\) vertices and \(\binom n2-p(G)\) edges. Consequently \(X\simeq Y\simeq\bigvee^{b(G)}S^1\), because its cycle rank is \(\binom n2-p(G)-n+1=b(G)\). In particular, \(b(G)\ge0\), and the homology of \(X\) is torsion-free, with reduced cohomology only in degree one.

**3. Duality and the homotopy conclusion.** Combinatorial Alexander duality over \(\mathbb Z\) gives
\[
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong\widetilde H^{n-i-3}(X;\mathbb Z).
\]
Thus \(\Delta_3(G)\) has exactly the reduced integral homology asserted in the theorem. Every four-vertex subset of \(V\) contains a disconnected induced triple by the same forbidden-four-vertex argument in Step 1. Therefore \(\Delta_3(G)\) contains every subset of size at most \(n-4\), i.e. the complete \((n-5)\)-skeleton; its facets have size \(n-3\), so its dimension is \(d=n-4\ge3\). This full \((d-1)\)-skeleton makes the complex \((d-2)\)-connected. The already established vanishing of \(H_{d-1}\), together with the Hurewicz theorem (also for \(d=3\)), makes it \((d-1)\)-connected. For \(b(G)>0\), choose maps \(S^d\to\Delta_3(G)\) representing an integral homology basis, using Hurewicz, and form their wedge. The resulting map from \(\bigvee^{b(G)}S^d\) is an integral homology equivalence between simply connected CW complexes, hence a homotopy equivalence by Whitehead's theorem. If \(b(G)=0\), the same homotopy-theoretic argument shows contractibility.

**4. Integral path submodule and automorphism character.** Let \(P=\mathbb Q^V\) be the vertex permutation module and \(A=\ker(\sum:P\to\mathbb Q)\) the augmentation module. The first homology of the complete graph on \(V\), with its natural \(\operatorname{Aut}(G)\)-action, is \(\bigwedge^2 A\): indeed its oriented one-chains identify with \(\bigwedge^2P\), and the boundary kills exactly \(\bigwedge^2 A\) under \(P=\mathbb Q\mathbf1\oplus A\). Because each path triangle has a private boundary edge, its boundary is nonzero and the boundaries of all path triangles are linearly independent. The cellular exact sequence is therefore
\[
0\longrightarrow C_2(X;\mathbb Q)\xrightarrow{\ \partial_2\ }\bigwedge^2A\longrightarrow H_1(X;\mathbb Q)\longrightarrow0.
\]
The action on \(C_2(X;\mathbb Q)\) is the **signed path-permutation action** (orientations of triangle faces), whose trace is \(\tau(g)\). The standard exterior-power identity yields
\[
\operatorname{tr}\!\left(g\middle|\bigwedge^2A\right)
=\frac{f(g)^2-f(g^2)}2-f(g)+1.
\]
In the equivariant Alexander-duality isomorphism, the orientation of the ambient sphere (the boundary of the simplex on \(V\)) transforms by \(\epsilon(g)\); hence \(\widetilde H_d(\Delta_3(G);\mathbb Q)\cong\mathbb Q_{\epsilon}\otimes H^1(X;\mathbb Q)\). The trace of a finite-order rational linear transformation equals the trace of its dual. Taking traces of the exact sequence and applying the orientation twist proves the displayed formula. At the identity it equals \(b(G)\), as required. Since \(\operatorname{Aut}(G)\) is finite, its characteristic-zero rational representation is determined up to isomorphism by its rational character.

## Verification

Run `python3 verify.py` using a Python 3.10+ interpreter and only the standard library. The source code constructs the graphs, constructs every facet of their ordinary three-cut complexes directly from disconnected triples, enumerates their faces, computes their signed simplicial Lefschetz traces, checks the claimed traces elementwise against the formula, and independently computes mod-two boundary ranks for the examples of up to ten vertices. It also checks for forbidden triangles/four-cycles and that every connected triple has a private opposite edge.

The checked examples include a seven-cycle, a seven-vertex path, the Petersen graph, the Heawood graph, a seven-vertex star, two disjoint five-cycles and a five-cycle with two isolated vertices. The script verifies respectively \(14,2,120,14,4,200,20\) explicit automorphisms, a total of \(374\) symmetry actions, and concludes `VERIFY_OK`. Its Heawood boundary ranks are not reconstructed owing to size; all claimed homology ranks for arbitrary graphs follow from the integral proof rather than from these experiments. The Petersen example supplies a six-dimensional consistency check of the signed character formula.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the ordinary cut complex in *Topology of Cut Complexes of Graphs* (arXiv:2304.13675). In their Theorem 6.1 and Proposition 6.2, forbidding cycles of length at most four gives a complete codimension-one skeleton, torsion-free homology in at most two adjacent degrees and the Euler characteristic; hence **the numerical expression** \(\binom{n-1}{2}-p(G)\) as an Euler difference is already implied by those statements. Their cycle and tree results also cover special cases of the present homotopy formula. The present claim is the all-graph concentration of homology in the top degree, its resulting uniform wedge homotopy type and the complete signed automorphism-character formula—not a new derivation of the known Euler characteristic. The contrast with the original connected triangle-free two-cut theorem is already visible on the seven-cycle: the three-cut sphere count here is \(8\), whereas the two-cut sphere count is its graph cycle rank, \(1\).

*Topology of Cut Complexes II* (arXiv:2407.08158) gives further families and selected group representations but not this all-graphs short-cycle-free module. The later paper *On Shellability of 3-Cut Complexes of Hexagonal Grid Graphs* (arXiv:2512.21755) gives shellability and a wedge for its particular hexagonal grid family; the present theorem does not assert a new hexagonal-grid homotopy result. Its representation formula extends beyond those families, including graphs with highly transitive automorphism groups and disconnected examples.

## Limitations

The hypothesis forbidding both triangles and four-cycles is essential to the private-edge argument. No claim is made when either is allowed, or for fewer than seven vertices, or for other cut parameters. There is no claim of shellability or of an equivariant homotopy equivalence. The character formula does not constitute a decomposition into individually named irreducible modules without the particular group's character table. The supplied finite verifier checks consistency on the stated graphs only; the mathematical proof covers the infinite class. Published coverage could exist in an alternate formulation not identified in the literature examined; independent validation remains outstanding.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first submitted 26 April 2023, especially Definition 2.7, Theorem 6.1, Proposition 6.2, Theorem 6.4 and §7. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first submitted 11 July 2024, especially §§3–6. https://arxiv.org/abs/2407.08158
3. H. Chandrakar, *On Shellability of 3-Cut Complexes of Hexagonal Grid Graphs*, arXiv:2512.21755, first submitted 25 December 2025, especially Theorems 1.1–1.2 and introductory comparison. https://arxiv.org/abs/2512.21755
