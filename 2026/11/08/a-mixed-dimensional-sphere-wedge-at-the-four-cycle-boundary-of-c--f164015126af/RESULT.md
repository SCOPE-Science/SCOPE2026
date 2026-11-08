# A mixed-dimensional sphere wedge at the four-cycle boundary of clique-fiber neighborhood complexes

## Finding
Let \(G=K_5\mathbin{\square}C_4\) be the Cartesian product of a five-vertex complete graph and a four-cycle. The open Lovász neighborhood complex of \(G\) has the **integral homotopy type**
\[
\boxed{\mathcal N(G)\simeq\bigvee^{53}S^2\vee\bigvee^{4}S^3.}
\]
In particular it is simply connected, with \(\widetilde H_2(\mathcal N(G);\mathbb Z)\cong\mathbb Z^{53}\), \(\widetilde H_3(\mathcal N(G);\mathbb Z)\cong\mathbb Z^4\), and all other reduced integral homology zero. This resolves a mixed-dimensional short-cycle boundary instance beyond the previously classified regime of cycle lengths at least five. It is a **single exact finite graph computation**, not a theorem about all complete-graph factors or all cycle lengths.

## Assumptions and scope
The graph has vertices \(v_{i,a}\) for \(i\in\mathbb Z/4\mathbb Z\) and \(a\in\{0,1,2,3,4\}\). Vertices \(v_{i,a}\) and \(v_{j,b}\) are adjacent precisely when \(i=j\) and \(a\ne b\), or when \(a=b\) and \(i-j\equiv\pm1\pmod4\). Thus \(G\) is a simple, 20-vertex, 6-regular graph. The **open** neighborhood of \(v_{i,a}\) is
\[
F_{i,a}=\{v_{i,b}:b\ne a\}\cup\{v_{i-1,a},v_{i+1,a}\}.
\]
A nonempty vertex subset is a face of \(\mathcal N(G)\) exactly when it lies in one of these twenty six-element sets. No closed-neighborhood, cut-complex, or graph-metric thickening convention is used.

## Proof
**Step 1: Complete face model.** Label \(v_{i,a}\) by the bit position \(5i+a\), ordered from zero to nineteen. A face is represented by its positive 20-bit mask. Enumerating all nonempty submasks of the twenty explicit \(F_{i,a}\) gives 950 distinct faces, with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(20,130,360,300,120,20).
\]
A separate procedure examines all \(2^{20}\) vertex subsets and tests common-neighbor intersections using graph adjacency; both produce exactly the same face set. In particular the enumeration is exhaustive, not a sample.

**Step 2: Full acyclic matching.** In increasing order of vertex labels \(p=0,1,\dots,19\), on the set of faces not yet matched, pair each \(\sigma\) without \(p\) to \(\sigma\cup\{p\}\) whenever both are then unmatched faces. Process the candidate faces in ascending integer-mask order. This unambiguous construction produces 446 pairs and precisely 58 unmatched faces: one vertex, 53 triangles, and four tetrahedra. Every pair consists of a face and an immediate coface. Construct the directed Hasse diagram on **all** 950 nonempty faces, orienting every unmatched cover from coface to face and every matched cover from face to coface. There are 3,260 cover incidences. A complete topological sort consumes every node, proving that there are no directed cycles. Forman's acyclic-matching theorem therefore gives a CW model with exactly the indicated cells.

**Step 3: Integral cellular attaching maps.** Order each simplex's vertices increasingly, with the usual signed simplicial boundary. For a matched pair \(\sigma\subset\tau\), the incidence number is \(+1\) or \(-1\), so algebraic cancellation is integral. The included verifier computes the resulting cellular boundary from the four critical three-cells to all 53 critical two-cells **in two ways**: (i) exact signed recursive gradient-path substitution; and (ii) direct unit-pivot cancellation of the 446 matched pairs in the original integral chain complex. In both computations all residual boundary coefficients are exactly zero. No floating-point, finite-field, numerical rank, or presumed zero differential is involved.

**Step 4: Homotopy upgrade.** Since the Morse CW complex has one zero-cell and no one-cells, its two-skeleton is a wedge of 53 two-spheres. In a simply connected two-complex the Hurewicz map \(\pi_2\to H_2(-;\mathbb Z)\) is an isomorphism. The vanishing integral cellular boundary of each three-cell means that its attaching map has zero Hurewicz image, hence is null-homotopic. Attaching the four three-cells therefore wedges on four three-spheres. This proves the stated integral homotopy equivalence. As a consistency check, \(\chi=1+53-4=50\), which equals the alternating sum of the exact face vector.

## Verification
Run `python3 verify_k5c4.py` using Python 3 and its standard library. It independently enumerates the open-neighborhood face set by direct common-neighbor testing on all \(1,048,576\) vertex subsets, verifies the 950 face masks from the twenty facet masks, constructs all matching pairs and all 3,260 directed cover incidences, and topologically sorts the entire oriented Hasse diagram. It then computes the signed Morse boundary by gradient recursion and checks the same zero boundary by independent integral unit-pivot cancellations. The program prints `ALL_CHECKS_PASS` only after all assertions succeed. The exact corresponding output is embedded in `verification_output.txt`. The finite program provides a complete proof certificate for this single finite complex; it does **not** establish a family theorem.

## Relationship to prior work
Kozlov [1] supplies general simple-homotopy relationships among Lovász neighborhood complexes, Lovász complexes, and graph Hom-complexes, but does not calculate this graph's homotopy type. Matsushita [2] relates fundamental groups of neighborhood complexes to graph-theoretic groups, without giving these higher integral homology groups.

A closest published calculation [3] classifies \(\mathcal N(K_m\mathbin\square C_n)\) only under the **explicit restriction** \(m\ge4\), \(n\ge5\), and explicitly excludes the present short-cycle boundary \(n=4\). Its generic result has an \(S^1\) summand, whereas the present boundary complex is simply connected: the excluded parameter cannot be supplied by naive substitution. Shukla's paper [4] addresses maximum degree at most three or four-regular circulant graphs; the present Cartesian product has degree six. Chauhan–Shukla–Vinayak [5] study **total two-cut complexes** of the same product graph family, but those facets are complements of independent pairs, not common-neighbor faces; their theorem does not imply this neighborhood-complex classification. Targeted available research-record and literature searches found no equivalent calculation, although this is not proof of publication priority.

## Limitations
The conclusion is confined to \(K_5\mathbin\square C_4\), with the open Lovász neighborhood convention. There is no claim for other clique sizes, for cycles of lengths three or at least five, for equivariant homotopy types, or for geometric homeomorphism. An unindexed equivalent computation may exist. The finite proof relies on the reproducible executable certificate, including its exhaustive face membership and directed-acyclicity checks. Independent mathematical audit has not been performed.

## References
[1] D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first public 2005-03-28, especially Sections 4 and 7. https://arxiv.org/html/math/0503613v3

[2] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public 2012-10-10, especially the fundamental-group correspondence. https://arxiv.org/html/1210.2803v4

[3] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, published-finding corpus published research record, 2026-10-11, especially its Finding, Proof, and stated \(n\ge5\) boundary. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c/RESULT.md

[4] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13. https://arxiv.org/abs/1802.04526

[5] P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486, first public 2025-12-04, especially Theorem 1.5. https://arxiv.org/abs/2512.04486
