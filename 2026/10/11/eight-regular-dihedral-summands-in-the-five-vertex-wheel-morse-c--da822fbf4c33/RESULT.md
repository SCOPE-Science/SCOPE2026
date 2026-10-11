# Eight regular dihedral summands in the five-vertex wheel Morse complex

## Finding
Let \(W\) be the graph with vertices \(\{0,1,2,3,4\}\), rim edges \(01,12,23,30\), and hub edges \(04,14,24,34\). Its automorphism group \(D_4\) acts on the rim by the eight maps \(i\mapsto \epsilon i+k\pmod4\), for \(\epsilon\in\{1,-1\}\), \(k\in\{0,1,2,3\}\), and fixes the hub \(4\).

For the ordinary complex \(\mathcal M(W)\) of discrete gradient vector fields on this one-dimensional graph, the induced action on rational reduced homology satisfies
\[
\widetilde H_3(\mathcal M(W);\mathbb Q)\cong\mathbb Q[D_4]^{\oplus8},\qquad
\widetilde H_i(\mathcal M(W);\mathbb Q)=0\quad(i\ne3).
\]
Thus the character \(\chi_3\) is \(64\) at the identity and zero on the other seven elements. In particular, \(\dim\widetilde H_3(\mathcal M(W);\mathbb Q)^{D_4}=8\). All four rational one-dimensional irreducibles occur with multiplicity \(8\), and the rational two-dimensional irreducible occurs with multiplicity \(16\).

## Assumptions and scope
A primitive gradient arrow is a pair \((u,uv)\) consisting of a vertex and an incident edge, encoded by the oriented edge \(u\to v\). A simplex of \(\mathcal M(W)\) is a finite set of such arrows whose tails are distinct, underlying edges are distinct, and whose directed graph has no directed cycle. Because the base graph has five vertices, every simplex contains at most four arrows. Homology uses simplicial orientations obtained by ordering the sixteen primitive arrows lexicographically according to the eight underlying edges and the two orientations of each edge. All group actions are induced by permutation of the *graph vertices*, and hence by permutation of the sixteen arrows; no orientation character is inserted by hand.

## Proof
**Homology concentration.** Enumerating all subsets of the sixteen arrows directly from the preceding criterion gives the face vector \((16,94,240,225)\). On the poset of the resulting \(575\) nonempty faces, process the primitive-arrow indices in the order
`(8,12,3,9,6,11,15,14,13,0,2,4,10,7,1,5)`.
At each stage pair any still-unmatched face not containing the current index with its still-unmatched one-element extension, if available. This gives \(255\) disjoint face-coface pairs. Among the remaining \(65\) faces there is exactly one vertex and \(64\) three-simplices. For every codimension-one face incidence, orient its Hasse cover from the larger face to the smaller face unless it is matched, in which case reverse it. A complete topological sort of the resulting \(575\)-node, \(1808\)-cover digraph succeeds. Therefore the matching is acyclic, and discrete Morse theory gives \(\mathcal M(W)\simeq\bigvee^{64} S^3\). In particular \(H_0(\mathcal M(W);\mathbb Q)=\mathbb Q\), \(H_3(\mathcal M(W);\mathbb Q)=\mathbb Q^{64}\), and the other homology groups vanish.

**Equivariant Lefschetz calculation.** For each \(g\in D_4\) and each dimension \(j\in\{0,1,2,3\}\), the trace on simplicial chains \(C_j(\mathcal M(W);\mathbb Q)\) is the signed count of \(j\)-faces carried to themselves: the sign is the parity of the induced permutation of their ordered primitive-arrow vertices. Direct exhaustive counts yield, by conjugacy type, the following signed-chain trace quadruples \((\operatorname{tr}C_0,\operatorname{tr}C_1,\operatorname{tr}C_2,\operatorname{tr}C_3)\):

- Identity: \((16,94,240,225)\).
- Quarter-turns: \((0,0,0,-1)\), twice.
- Half-turn: \((0,-6,0,5)\).
- Reflections fixing two rim vertices: \((4,0,-12,-9)\), twice.
- Reflections fixing no rim vertices: \((0,-4,0,3)\), twice.

The Lefschetz alternating sums are therefore \(-63\) at the identity and \(1\) at every nonidentity element. Since the only nonzero rational homology lies in degrees zero and three, and \(H_0\) carries the trivial representation, the Hopf trace identity gives \(L(g)=1-\chi_3(g)\). Hence \(\chi_3(1)=64\) and \(\chi_3(g)=0\) for \(g\ne1\). The rational regular character of \(D_4\) has values \(8\) at the identity and \(0\) elsewhere. Maschke's theorem and character uniqueness in characteristic zero identify the module with eight copies of \(\mathbb Q[D_4]\). This also gives the asserted isotypic multiplicities.

## Verification
Run `python3 verify_wheel.py` using Python 3 without additional packages. The program independently builds all sixteen arrows, checks all subsets of sizes one through four from the acyclicity definition, verifies the \(1808\) Hasse covers, reconstructs the \(255\) Morse pairs and topologically sorts the directed Hasse graph, checks the boundary ranks \((15,79,161)\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{101}\), enumerates all eight dihedral automorphisms, and computes all thirty-two signed chain traces. It checks the exact character claimed here before printing `VERIFY_OK`. The Morse matching and Lefschetz argument, rather than finite-field sampling, establish the integral homotopy and rational representation claims.

## Relationship to prior work
Lin and Scoville determine the automorphism group of the Morse complex for finite connected simplicial complexes other than specified exceptional cases. Their theorem gives \(\operatorname{Aut}(\mathcal M(W))\cong D_4\) but not this group's action on homology. Donovan and Scoville develop homotopy calculations for graph Morse complexes and a framework for these simplicial complexes; their star-cluster results do not give this wheel representation. A previously published, fully inspected computation of \(\mathcal M(W)\) established the nonequivariant equivalence \(\bigvee^{64}S^3\) and its face vector, but did not determine any dihedral homology character. This result claims solely the **equivariant** refinement; the sphere count is already known.

## Limitations
The representation is asserted only for the five-vertex wheel, not for arbitrary wheel graphs. The homotopy equivalence produced by the acyclic matching is not claimed to be equivariant; equivariance of homology is proved instead through the chain-level Lefschetz trace calculation. Integral representation-lattice structure is not determined. The literature comparison cannot rule out unpublished or unindexed equivalent calculations.

## References
1. M. Lin and N. A. Scoville, “On the automorphism group of the Morse complex,” arXiv:1904.10907v1 (first public 2019-04-24), Section 3 and Theorem 1; primary MSC 55U05.
2. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780v1 (first public 2022-07-27), definitions and the graph-Morse results; primary MSC 57Q70.
3. “The five-vertex wheel Morse complex is a wedge of 64 three-spheres,” published mathematical record `c2f501a8-bea1-4b65-b88a-27b6a7ff118e`, complete result and reproducer available in the public published-finding corpus 2026 repository, `RESULT.md`.
