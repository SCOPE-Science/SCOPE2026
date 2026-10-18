# The Pappus noncover complex: ten three-spheres and its full affine symmetry character

## Finding
For the classical nine-point, nine-line Pappus configuration \(\mathcal H\), let \(K=\operatorname{NC}(\mathcal H)\) consist of the point sets missing at least one configuration line. Then
\[
K\simeq \bigvee^{10}S^3.
\]
This is an integral homotopy equivalence. The full group \(G\) of automorphisms of the nine-point configuration has order \(108\). The rational third-homology character takes the trace values \(-2,-1,1,2,10\) on respectively \(21,36,32,18,1\) elements of \(G\), and is determined on every group element by the cycle formula below. Its invariant subspace is zero; its character self-inner-product is \(3\), so its complexification is multiplicity-free with precisely three distinct irreducible constituents.

## Assumptions and scope
Represent the nine points by \(\mathbf F_3^2\); label \((x,y)\) by \(3x+y\), with \(0\le x,y\le2\). The nine three-point lines are
\[
\{(x,y):x=c\},\quad\{(x,y):y=c\},\quad\{(x,y):x+y=c\},\quad c\in\mathbf F_3.
\]
This is the classical Pappus \((9_3)\) incidence structure: completing the missing fourth direction gives the twelve-line affine Hesse plane, and its eighteen-vertex incidence graph is the Pappus graph. The selected nine lines are the hyperedges of \(\mathcal H\), and \(K\) is the simplicial complex of noncovers, *not* the independence complex of the eighteen-vertex incidence graph. Every facet of \(K\) is the six-point complement of one of the nine lines. All homotopy conclusions refer to integral realizations; symmetry decomposition is rational or complex, as specified.

The complete character may be evaluated without a character table. For a point permutation \(g\in G\), write its cycles as \(C_1,\ldots,C_t\), understood as disjoint sets of points. Define
\[
\chi(g)=\sum_{J\subseteq\{1,\ldots,t\}\,:\,\bigcup_{j\in J}C_j\in K\ \mathrm{or}\ J=\varnothing}(-1)^{|J|}.
\]
This formula specifies all \(108\) traces and is invariant under relabeling of the point configuration.

## Proof
**An exact discrete-Morse reduction.** Enumerate each nonempty subset of the nine labeled points and retain a mask precisely when its point set is included in the complement of a configuration line. This gives \(297\) nonempty faces and the face vector \((9,36,81,108,54,9)\), indexed by dimensions \(0\) through \(5\).

Work in the *ordinary nonempty-face poset*. Process vertices in the fixed order \((1,3,0,6,8,5,2,7,4)\). For each pivot \(v\), traverse the currently unpaired masks in ascending order of cardinality then numerical mask. Pair each available face not containing \(v\) with its available one-vertex extension by \(v\), removing both from further consideration. The resulting matching has exactly \(143\) pairs and leaves precisely the eleven face masks
\[
2,77,85,113,165,225,300,312,329,408,456.
\]
The first is a vertex; each other mask has four set bits and is a three-simplex. For the full Hasse diagram, orient each matched covering edge upward and every other covering edge downward. The standalone verifier constructs all \(1071\) covering incidences and performs a complete directed topological sort of all \(297\) faces. It visits every face; hence the oriented Hasse diagram is acyclic. Forman's discrete-Morse theorem now yields a CW complex having one zero-cell, ten three-cells and no other cells. All attaching two-spheres map to the lone zero-cell, so this CW complex is the asserted wedge of ten three-spheres, with no additional hypotheses on attaching maps or coefficient fields.

**Full symmetry group.** A point permutation is a configuration automorphism exactly when it permutes the nine specified line triples. The verifier exhausts all \(9!=362880\) permutations and finds exactly \(108\) automorphisms. Independently it constructs the invertible affine maps \((x,y)\mapsto A(x,y)+b\) preserving the three selected line directions. Exactly \(108\) distinct such maps arise, and the two groups coincide as permutation sets.

**Character.** Because the reduced homology is concentrated in degree three, the ordinary Lefschetz number satisfies \(L(g)=1-\operatorname{tr}(g\mid\widetilde H_3(K;\mathbf Q))\). For each setwise-fixed simplex with ordered vertices, its trace on its oriented chain is the sign of the induced vertex permutation, multiplied by the usual alternating simplicial degree sign in the Lefschetz sum. The second, independent calculation groups fixed simplices into unions of cycles of \(g\): selecting \(j\) vertex cycles contributes \((-1)^j\) to the **third-homology trace**, including the empty selection. This gives the stated cycle formula. Evaluating both exact expressions independently for every one of the \(108\) permutations yields identical traces and the distribution in the Finding. Their sum is \(0\) and the sum of squared traces is \(324\). Dividing by the group order gives, respectively, zero invariant multiplicity and character inner product \(3\). Maschke's theorem and character orthogonality imply precisely three distinct irreducible complex constituents, each of multiplicity one.

## Verification
Execute `python3 verify_pappus_noncover.py` using Python 3 and only its standard library. The verifier independently reconstructs the point-line incidence data, all simplices, all \(143\) matching pairs, the full directed Hasse diagram, binary simplicial boundary ranks, all point automorphisms by brute-force \(9!\) enumeration and independently by affine coordinate maps, and two complete signed Lefschetz character computations. The replay output is included as `verification_pappus_output.txt`. Checks are exhaustive for the nine-point configuration; no finite sampling is extrapolated to an infinite family.

## Relationship to prior work
Kim and Kim define the noncover complex of a hypergraph and prove general vanishing/collapsibility bounds; their complete preprint treats explicit homotopy classifications for *tight paths and tight cycles*. The Pappus line hypergraph is neither: its distinct lines meet in at most one point, whereas tight three-uniform consecutive triples overlap in two points. Neither their general bounds nor their special-family formulas imply this wedge decomposition or symmetry character.

Tsukuda's Theorem 4.10 and Corollary 4.11 give a suspension equivalence between the independence complex of a hypergraph's incidence graph and the Alexander dual of its hypergraph independence complex. Applied here, they relate the Pappus graph's ordinary independence complex to the suspension of this noncover complex. A previously published specific Pappus-graph calculation identifies that independence complex as a wedge of ten four-spheres, with a cyclic-subgroup character in another study. Its suspension information recovers the **ranks** but does not on its own supply an unsuspended homotopy equivalence for this five-dimensional noncover complex, nor the complete \(108\)-automorphism homology character. The matching certificate and complete group-character calculation are the new portions of the finding.

A separate published Pappus-graph Čech-nerve classification concerns \(18\) graph vertices and has homotopy type a wedge of \(44\) two-spheres, not this nine-vertex noncover complex. The complete twelve-line affine Hesse hypergraph is another related but different incidence configuration: adding the missing fourth parallel class changes the noncover complex and its homotopy type. These comparisons distinguish objects as well as numerical invariants.

## Limitations
The claim concerns one natural nine-point configuration and the complete symmetry group preserving its **point** labels, not the larger group of the eighteen-vertex Levi graph including point-line dualities. The integral homotopy type does not give an integral decomposition of the homology lattice as a symmetry module, nor an equivariant homotopy equivalence. Finite exhaustive computations require replay of the attached code; the source material and exact enumeration recipe are sufficient to reproduce them. The literature comparison cannot rule out unindexed equivalent calculations.

## References
1. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1, first publicly submitted 2021-01-06, subsequently J. Combin. Theory A 180 (2021), 105408.
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277; especially Corollary 4.11.
3. *The Pappus graph independence complex is a wedge of ten four-spheres*, published mathematical report, identifier ff7e4637c061 (2026).
4. *The scale-three graph Čech nerve of the Pappus graph is a wedge of forty-four two-spheres*, published mathematical report, identifier 2ff2beca323b (2026).
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
