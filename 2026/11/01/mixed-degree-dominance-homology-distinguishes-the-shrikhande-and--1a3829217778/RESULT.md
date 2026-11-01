# Mixed-degree dominance homology distinguishes the Shrikhande and rook graphs

## Finding
Let \(S\) denote the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Write \(\mathcal D(G)\) for the simplicial complex of vertex sets \(\sigma\subseteq V(G)\) for which \(V(G)\setminus\sigma\) dominates \(G\). Their complete **reduced integral homology** is
\[
\widetilde H_i(\mathcal D(S);\mathbb Z)\cong
\begin{cases}\mathbb Z^{11},&i=9,\\0,&i\ne9,\end{cases}
\qquad
\widetilde H_i(\mathcal D(R);\mathbb Z)\cong
\begin{cases}\mathbb Z,&i=9,\\\mathbb Z^2,&i=11,\\0,&\text{otherwise}.\end{cases}
\]
Both graphs are strongly regular with parameters \((16,6,2,2)\); their dominance complexes have identical face counts through dimension ten, yet the rook complex has an additional nonzero homology degree. All stated groups are torsion-free. **No homotopy-type equivalence for the dominance complexes is claimed.**

## Assumptions and scope
The graphs are simple, finite, loopless and undirected. Both have vertex set \(V=(\mathbb Z/4\mathbb Z)^2\), labeled \(4i+j\) for \(0\le i,j\le3\). Distinct pairs \((i,j),(k,l)\) are adjacent in \(R\) if \(i=k\) or \(j=l\). In \(S\), two vertices are adjacent if their difference modulo four is in
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
A set \(T\) dominates a graph if every vertex lies in \(T\) or is adjacent to a vertex in \(T\). The empty simplex is included in the abstract simplicial complexes, and reduced homology uses integral coefficients. No inference about larger strongly regular families or about equivariant representations is made.

## Proof
**1. Graphs and Alexander duality.** The displayed adjacency prescriptions give sixteen vertices each of degree six; for every pair of distinct vertices, the graph has exactly two common neighbors. Enumerating all sixteen-bit masks verifies these assertions and the graph symmetry. Let \(K_G=\mathcal N(\overline G)\), the ordinary **open-neighborhood complex** of the complement graph. Its facets are
\[
F_v=V\setminus N_G[v]\quad(v\in V),
\]
where \(N_G[v]\) is the closed neighborhood of \(v\) in the original graph. Thus each facet has nine vertices. The identity of Matsushita–Wakatsuki, or directly the definitions, gives
\[
\mathcal D(G)=K_G^\vee,
\qquad K_G^\vee=\{\sigma\subseteq V:V\setminus\sigma\notin K_G\}.
\]
Combinatorial Alexander duality for sixteen-vertex complexes yields
\[
\widetilde H_i(\mathcal D(G);\mathbb Z)
\cong\widetilde H^{13-i}(K_G;\mathbb Z).
\]
The superscript denotes cohomology. The shift \(13-i\), rather than \(14-i\), follows from the standard \(n-i-3\) formula.

**2. Entire neighborhood-complex face sets.** Iterate all nonempty submasks of each of the sixteen facet masks \(F_v\), adjoining the empty face. The resulting \(K_R\) has \(5,789\) faces including empty, with face counts in dimensions zero through eight
\[
(16,120,560,1332,1728,1296,576,144,16).
\]
The complex \(K_S\) has \(5,717\) faces including empty, with counts
\[
(16,120,528,1292,1728,1296,576,144,16).
\]
For each of the \(2^{16}\) possible masks, an independent membership test checks that it lies in \(K_G\) exactly when it is disjoint from at least one closed neighborhood \(N_G[v]\).

**3. Integral chain reductions.** Start with the unreduced, canonically oriented simplicial chain complex on the nonempty faces. Repeatedly delete a face with exactly one immediate coface together with that coface. A deterministic priority order, first by face cardinality and then by numerical mask, produces \(2,568\) elementary pairs for \(K_R\) and \(2,322\) for \(K_S\). The remaining simplicial subcomplexes contain respectively \(652\) and \(1,072\) nonempty faces. The verifier checks each face's actual immediate cofaces *before* deleting a pair; these are genuine simplicial elementary collapses.

On each remaining integral simplicial chain complex, define signed boundary coefficients using the ascending vertex order. For a coefficient \(u=\pm1\) between an upper basis cell \(x\) and a lower basis cell \(y\), eliminate this acyclic chain pair by the exact integral Schur complement
\[
\partial z\ \longmapsto\ \partial z-
\frac{[y]\partial z}{u}\,\partial x
\]
for every other generator \(z\) in the degree of \(x\), followed by removal of \(x\) and \(y\) and their adjacent incidences. This is a chain-homotopy equivalence over \(\mathbb Z\), because \(u\) is a unit. All multiplication and subtraction uses arbitrary-precision integer arithmetic; the code checks \(\partial^2=0\) and the equality of the row/column incidence dictionaries throughout. Among unit entries, choose the lexicographically least pivot by fill cost, combined incidence count, lower cardinality, lower mask and upper mask.

There are exactly \(324\) such integral unit cancellations for \(K_R\), leaving **one degree-zero generator, two degree-two generators and one degree-four generator**. For \(K_S\), exactly \(530\) unit cancellations leave **one degree-zero generator and eleven degree-four generators**. Every remaining differential is identically zero, and no nonunit pivot is ever required (indeed, the largest intermediate absolute coefficient is one). Therefore the full integral homology groups of \(K_R\) are \(\widetilde H_2\cong\mathbb Z^2\), \(\widetilde H_4\cong\mathbb Z\), and zero otherwise; those of \(K_S\) are \(\widetilde H_4\cong\mathbb Z^{11}\), and zero otherwise. This argument rules out any hidden integral torsion; it does not use finite-field ranks to infer torsion-freeness.

**4. Transfer to dominance homology.** The universal coefficient theorem identifies the corresponding integral cohomology groups of \(K_R\) and \(K_S\), since all their homology is free. Substituting into the sixteen-vertex Alexander-duality isomorphism in step 1 gives precisely the claimed dominance groups in degrees nine and eleven.

## Verification
Execute `python3 verify_dominance_twins.py` from the extracted package directory (Python 3 standard library only). It constructs both graphs from their definitions; tests every pair's common-neighbor count; constructs all facets and their complete downward closure; independently checks the membership of all \(65,536\) masks; and separately enumerates the dominance complexes by testing containment of every original closed neighborhood. Each elementary collapse is checked as a free pair, and each subsequent integral cancellation is implemented using explicit signed incidence dictionaries. The program verifies boundary-square-zero identities and transposed incidence data, including after every fifty algebraic eliminations and at the final step. It independently computes the entire mod-two boundary ranks of the original neighborhood complexes.

The dominance complexes contain \(59,747\) and \(59,819\) faces respectively, including empty, and have reduced Euler characteristics \(-3\) and \(-11\), consistent with the computed integral homology. Their counts of faces agree in every dimension \(\le10\); they first differ in degree eleven. The ordered cancellation-pair SHA-256 values and the complete mod-two boundary ranks are supplied by `verification_output.txt`. Every certificate is reconstructed from the graph definitions by the standalone verifier, rather than assumed from a saved log.

## Relationship to prior work
Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* (first public 2023-12-05), prove the Alexander-dual identification used here and study forests, chordal graphs and selected grid products. Their theorem alone does **not** supply either dominance Betti vector above; neither graph is chordal, and neither is their Cartesian path-grid family.

Mertens, *Domination Polynomial of the Rook Graph* (first public 2024-01-01), determines the counts of dominating sets in every rectangular rook graph. In particular the rook complex's face vector is deducible from that polynomial, so the face-count computation is **not** claimed as a novel enumerative theorem. The polynomial does not identify its homology groups, torsion or degree support. Matsushita's later *Closed neighborhood complexes of graphs* computes the complex generated by **closed neighborhoods of the rook graph**; the present chain complex is generated by **open neighborhoods of its complement**, and its Betti vector differs.

Published studies have also distinguished these same two graphs using their ordinary independence complexes and their scale-two intrinsic Čech nerves. Those complexes use different face rules and have different computed homology: the already studied independence complexes each have homology in degree two, and the Čech complexes have degree-two homology only. Neither comparison implies the new distinction between one- and two-degree **dominance** homology. The present statement is therefore a specific, stronger-than-face-enumeration topological calculation for a separately motivated graph complex, not a claim to be the first invariant distinguishing these nonisomorphic graphs.

## Limitations
The proof determines **integral homology**, not the homotopy types or cup products of the dominance complexes. Algebraic cancellations of integral chain generators alone do not yield a simplicial collapse or homotopy equivalence for the dominance spaces. The result covers exactly the two displayed sixteen-vertex graphs; a classification of arbitrary strongly regular graphs is not asserted. Indexed searches and inspected primary sources did not reveal an identical prior calculation, but an unindexed equivalent one remains possible. No independent mathematical audit has been performed.

## References
1. Takahiro Matsushita and Shun Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (2023-12-05); Theorem 1.1 and §§2–6. https://arxiv.org/abs/2312.02639
2. Stephan Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716v1 (2024-01-01); §§1–3. https://arxiv.org/abs/2401.00716
3. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, Example 3.5 (2025). https://arxiv.org/abs/2511.12608
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, publicly available research record (2026), identifier ending `41bf4d1d3187`.
5. *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, publicly available research record (2026), identifier ending `5b6e4436155e`.
6. A. Björner and M. Tancer, *Combinatorial Alexander Duality — a Short and Elementary Proof*, Discrete Comput. Geom. 42 (2009), 586–593, arXiv:0710.1172. https://arxiv.org/abs/0710.1172
