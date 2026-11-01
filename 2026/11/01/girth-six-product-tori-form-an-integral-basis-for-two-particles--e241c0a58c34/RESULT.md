# Girth-six product tori form an integral basis for two particles on the Möbius–Kantor graph

## Finding
For the Möbius–Kantor graph \(G=GP(8,3)\), let \(X=\operatorname{UConf}_2(|G|)\) be the space of two distinct **unordered** points on its geometric realization. There are exactly \(24\) simple six-cycles and exactly \(60\) unordered pairs of vertex-disjoint six-cycles. Every such pair determines an embedded product torus in \(X\). Their integral fundamental classes generate all of \(H_2(X;\mathbb Z)\), and twenty explicitly indexed classes are an integral basis. More precisely,
\[
H_0(X;\mathbb Z)\cong\mathbb Z,\quad
H_1(X;\mathbb Z)\cong\mathbb Z^9\oplus\mathbb Z/2,\quad
H_2(X;\mathbb Z)\cong\mathbb Z^{20},
\]
and \(H_i(X;\mathbb Z)=0\) for \(i>2\). The full graph automorphism group of order \(96\) has exactly two orbits, of sizes \(12\) and \(48\), on these sixty minimum-length torus constructions.

## Assumptions and scope
Write vertices as \(u_i=i\) and \(v_i=8+i\), where \(i\in\mathbb Z/8\mathbb Z\), and let the edges be \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\). Orient each edge from its smaller numerical endpoint to its larger endpoint. Let \(\gamma_0,\ldots,\gamma_{23}\) denote the twenty-four simple six-cycles, with each cycle written beginning at its numerically least vertex and with second vertex less than last, then ordered lexicographically. List pairs \((a,b)\), with \(a<b\), for which \(\gamma_a\) and \(\gamma_b\) are vertex-disjoint, again lexicographically. This gives sixty pairs \(P_0,\ldots,P_{59}\).

For definiteness, the following pairs of six-cycle *indices* give an integral basis of twenty product tori:

`(0,18), (0,19), (0,20), (1,15), (1,17), (1,18), (2,15), (2,16), (2,17), (3,12), (3,14), (3,15), (4,12), (4,13), (5,12), (5,13), (5,18), (6,9), (6,10), (6,11)`.

Indices here are zero-based; the verification program reconstructs every cycle and pair directly from the edge definition. The torus orientations are the product orientations of the canonical oriented cycles. The claim concerns the integral homology of the usual continuous configuration space, not merely its rationalization or a graph-theoretic cycle-vector space.

## Proof
**Cubical model.** The Abrams unordered discrete configuration complex for two particles has cells consisting of two vertices, one vertex and a nonincident edge, or two edges with no common endpoint. Its inclusion is a homotopy equivalence for this graph: every path joining essential vertices has at least one edge and every simple cycle has more than two edges. There are exactly \(120\), \(336\), and \(228\) cells in degrees zero, one, and two.

A one-cell \((v,e)\), with \(e=(a,b)\) oriented from \(a\) to \(b\), has boundary \([(v,b)]-[(v,a)]\), where vertex pairs are unordered. For a two-cell \((e,f)\), with \(e=(a,b)<f=(c,d)\) in lexicographic edge order, take its boundary to be
\[
[(b,f)]-[(a,f)]-[(d,e)]+[(c,e)].
\]
The formulas define integer matrices \(\partial_1\) and \(\partial_2\); direct substitution gives \(\partial_1\partial_2=0\).

**Short product tori.** Exact enumeration of all simple cycles of lengths three through six shows that the girth is six and that there are exactly twenty-four six-cycles. Exactly sixty unordered pairs of them have disjoint vertex sets. The two cycles in such a pair give an embedded torus in the unordered two-particle space. Its fundamental two-chain has coefficient \(\epsilon_e\epsilon_f\) at the square associated with edges \(e<f\), with a sign reversal when the order of the two cycle factors is swapped. Applying the displayed boundary proves that each torus two-chain is a cycle.

**Rank and primitivity.** Exact elimination over \(\mathbb F_3\) gives \(\operatorname{rank}\partial_2=208\) modulo three and therefore at least \(208\) over \(\mathbb Q\). The twenty torus chains indexed above have a \(20\)-by-\(20\) coordinate minor of determinant \(-1\), using the square-cell indices

`0, 2, 4, 6, 8, 11, 19, 21, 23, 25, 27, 57, 59, 61, 63, 91, 93, 95, 121, 123`

in the lexicographically ordered list of vertex-disjoint edge pairs. Thus twenty integral cycles are linearly independent, forcing \(\operatorname{rank}_{\mathbb Q}\partial_2\le208\). Equality follows. The unimodular minor shows that their span is a *primitive* direct summand of the free ambient group of two-chains. Since \(\ker\partial_2\) is also primitive in that group (its quotient is a subgroup of the free group of one-chains), and both subgroups have rank twenty, the two subgroups agree. Consequently those twenty torus cycles form an integral basis of \(H_2\), hence all sixty hexagon-pair tori generate.

**Remaining homology.** The cubical one-skeleton is connected; its incidence boundary has rank \(119\). The exact integral Smith form of \(\partial_2\) has \(207\) unit invariant factors and one invariant factor \(2\) (the remaining entries are zero). Therefore \(H_1\) has free rank \(336-119-208=9\) and one order-two torsion factor; there is no higher cellular degree. Enumeration of all graph automorphisms and their induced permutations of the sixty disjoint hexagon pairs gives a full group of order \(96\) and orbit sizes \(12\) and \(48\).

## Verification
Run `python verify.py` and `python symmetry.py` in the same directory, with Python 3, `sympy`, and `networkx` installed. The first script independently constructs all cubical boundary columns from edges, checks the chain identity, enumerates short cycles, verifies every torus boundary, checks modular ranks, computes the exact Smith form, and recomputes the specified unimodular determinant. The second exhaustively enumerates graph automorphisms and determines the pair-orbit partition. Their recorded outputs are `verify.out` and `symmetry.out`. All counts and integer assertions are finite, exhaustive computations; no experimental extrapolation is used.

## Relationship to prior work
Barnett and Farber [1] give the ordered deleted-product complex, the intersection method, and planar graph results. Farber and Hanbury [2] study ordered configurations and mature nonplanar graphs; their rank framework does not imply an integral basis arising specifically from shortest disjoint cycles on this graph. Ko and Park [3] determine general first-homology invariants and already account for the possibility of order-two torsion; the order-two observation is not claimed as a new general phenomenon. An and Knudsen [4] ask for combinatorial bases in second graph-braid homology and prove planar-generation theorems that do not apply to this nonplanar graph. Knill [5] studies the same Möbius–Kantor graph as a symmetric toroidal graph, but its geodesics, graph Lefschetz invariants and group structures are different objects from this two-particle homology theorem. The contribution here is the *integral girth-six torus basis* and its sixty-carrier, two-orbit description, not the configuration-space cubical construction or the existence of two-torsion alone.

## Limitations
No claim is made about more than two particles, the integral action on the full homology lattice, or homotopy equivalence to a product of surfaces. The computation uses the specified model and fixed finite graph only. Publication-priority checks may miss equivalent unindexed or unpublished material. This is not an independently audited mathematical result.

## References
[1] K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, originally submitted 2009-03-12.

[2] M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, originally submitted 2010-05-13.

[3] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, originally submitted 2011-01-13.

[4] B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, originally submitted 2020-08-24.

[5] O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799, originally submitted 2026-05-29.
