# Integral homotopy of the eight-cycle four-color categorical-product independence complex

## Finding
Let \(G=C_8\times K_4\) be the categorical (tensor/direct) graph product of the eight-cycle with the complete graph on four vertices, and \(X=\operatorname{Ind}(G)\) its ordinary independence complex. There is an integral homotopy equivalence
\[
X\simeq \bigvee^{3}S^{4}\vee\bigvee^{6}S^{5}.
\]
Consequently, \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^3\) and \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^6\), and all other reduced integral homology groups vanish. In particular, no torsion or nontrivial Moore-space summands occur in this case.

## Assumptions and scope
The graph has vertex set \(V=\{(i,a):i\in\mathbb Z/8\mathbb Z,\ 0\le a<4\}\). An edge joins \((i,a)\) and \((j,b)\) if and only if \(j-i\equiv1\) or \(-1\pmod8\) and \(a\ne b\). This defines a simple 32-vertex, 96-edge graph. A face of \(X\) is any nonempty set of pairwise nonadjacent vertices. The proof is specific to the four-color, eight-cycle case; neither a different graph product nor an infinite family is claimed.

Represent \((i,a)\) by the integer \(4i+a\); represent a face by the unsigned bitmask of its vertices. In the ascending vertex order, orient each simplex with its ascending vertices and use the usual alternating boundary. These conventions completely specify the finite certificate.

## Proof
**Step 1: exhaustive independent-face enumeration.** The verifier starts from the empty mask and recursively adds higher-numbered vertices that are not adjacent to any chosen vertex. It independently reconstructs the 196,226 nonempty faces. The face counts, in vertex cardinalities 1 through 16, are
\[
(32,400,2560,9400,21440,33040,37728,34488,26336,16896,8864,3648,1120,240,32,2).
\]
Each extension uses only vertices larger than those previously chosen, so each face is enumerated exactly once. The alternating sum of the nonempty counts is \(-2\), giving reduced Euler characteristic \(-3\).

**Step 2: an acyclic matching.** Starting with all nonempty faces unmatched, for \(v=0,1,\ldots,31\) pair each still-unmatched \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided the latter is also still unmatched. Remove all pairs for that stage before proceeding. Because every pair contains exactly one lower face not containing \(v\), pairs at a given stage are disjoint. The resulting 98,087 pairs leave exactly one critical vertex, 24 critical four-dimensional simplices, and 27 critical five-dimensional simplices. To verify acyclicity, orient every unmatched codimension-one Hasse incidence downwards, and every matched incidence upwards. An exhaustive topological sort processes all 196,226 faces and all 1,457,216 nonempty codimension-one incidences, so the directed Hasse graph has no cycles. The usual acyclic-matching theorem therefore constructs a CW model with these critical cells and no others.

**Step 3: the integral Morse differential.** For each critical oriented four-simplex, use its induced ascending order. For a noncritical four-face \(\tau\) matched upward to \(\rho=\tau\cup\{v\}\), the signed gradient projection is computed recursively by solving \(\partial\rho=0\) for \(\tau\); its coefficient is the negative reciprocal of the incidence sign \([\rho:\tau]\in\{\pm1\}\). The projection of a critical four-face is itself; the projection of a noncritical four-face matched downward is zero. In acyclic order, this recursion terminates. Apply it to the oriented simplicial boundary of each of the 27 critical five-simplices. It yields a 27-by-24 signed integer boundary matrix; its full entries and critical-face identifiers are recorded in `morse_boundary.json`, and independently recomputed and compared exactly by `verify.py`.

The checker diagonalizes this matrix using integral row and column operations, swapping and adding integer multiples of rows and columns, with **only unit pivots** \(\pm1\). It finds 21 unit diagonal entries and a zero residual block. Thus the Morse cellular boundary has free kernel of rank \(27-21=6\), free cokernel of rank \(24-21=3\), and no torsion. The absence of other critical cells proves the stated reduced integral homology in every dimension.

**Step 4: upgrade from homology to homotopy.** The reduced Morse CW complex has a single 0-cell and no positive cells below dimension four. Its four-skeleton is therefore \(\bigvee^{24}S^4\). The attaching maps of its 27 five-cells lie in \(\pi_4(\bigvee^{24}S^4)\cong\mathbb Z^{24}\) by the Hurewicz theorem, and correspond exactly to the columns of the integral Morse boundary matrix. Elementary unimodular basis changes are implemented by homotopy equivalences of the four-sphere wedge and elementary five-cell slides. The 21 unit diagonal attaching maps cancel 21 pairs of four- and five-cells up to homotopy; the six zero attaching maps are null-homotopic. What remains is \(\bigvee^3S^4\vee\bigvee^6S^5\), as asserted.

## Verification
The standalone Python 3 checker `verify.py` needs no third-party dependencies. Run it alongside `morse_boundary.json` as `python verify.py`. It reconstructs graph adjacencies, all independent faces, the complete matching and acyclicity graph, all signed Morse boundary entries, and an explicit 21-unit integral diagonalization; it fails on any discrepancy. Successful execution prints `C8_TENSOR_K4_WEDGE_3S4_AND_6S5_VERIFIED`. The companion JSON is a complete, human-inspectable matrix certificate rather than a runtime log. These finite checks and the preceding mathematical arguments together support the exact homotopy claim.

## Relationship to prior work
Antolín Camarena and Carnero Bravo (2023, arXiv:2307.12401), Theorem 23, restrict possible homotopy types of \(\operatorname{Ind}(C_{3r+2}\times K_n)\) to two adjacent sphere dimensions together with possible Moore spaces, and explicitly ask whether torsion ever occurs (Question 24). They report computation for \(C_8\times K_3\), but do not determine the exact four-color case here. Their proven general three-divisible-cycle theorem concerns \(C_{3r}\), not \(C_8\). The available 2025 work of Carnero Bravo (arXiv:2505.06457) focuses on other graph-product classes, including products involving paths; its inspected statements do not settle this specific case. Goyal, Shukla and Singh (2019, arXiv:1905.06926) study different complete-graph and Mycielskian constructions. The nearest indexed finite research record, for \(C_7\times K_4\), concerns a different cycle and provides no direct equivalence to this object. The exact four-color eight-cycle classification is thus not a restatement of those inspected claims; an unindexed equivalent or a previously unrecognized implication remains possible.

## Limitations
Only this 32-vertex complex is classified. It does not establish torsion-freeness for all cycle products, classify the natural automorphism representation, or prove priority over all existing literature. Originality is qualified by the possibility of unindexed equivalent work. The integral matrix diagonalization is a complete finite computation, not an argument extending to infinite families. Independent scientific validation has not been performed.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first submitted 2023-07-23); https://arxiv.org/abs/2307.12401.
2. A. Carnero Bravo, *On Independence Complexes of Graph Products*, arXiv:2505.06457 (2025); https://arxiv.org/abs/2505.06457.
3. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019); https://arxiv.org/abs/1905.06926.
