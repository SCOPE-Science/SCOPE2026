# The Paley-13 neighborhood complex is 25 two-spheres with an explicit affine homology module

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\) and let \(X=\mathcal N(P_{13})\) be its *ordinary open-neighborhood complex*. Its integral homotopy type is
\[
\boxed{X\simeq\bigvee^{25}S^2.}
\]
Write \(Q=(\mathbb F_{13}^{\times})^2\) for the six nonzero squares, and let \(G=\mathbb F_{13}\rtimes Q\) act on vertices by \(x\mapsto ax+b\). If \(W=\mathbb Q^{\mathbb F_{13}}\) is the natural thirteen-point permutation representation, its complete rational top-homology representation is
\[
\boxed{\widetilde H_2(X;\mathbb Q)\cong_{\mathbb Q[G]} W\oplus(W/\mathbb Q\mathbf1).}
\]
Equivalently, for every affine symmetry \(g(x)=ax+b\), the top-homology character is
\[
\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))=
\begin{cases}
25,&(a,b)=(1,0),\\
-1,&a=1,\ b\ne0,\\
1,&a\ne1.
\end{cases}
\]
All other reduced integral homology groups vanish. In particular, the \(G\)-invariant rational top-homology subspace is one-dimensional.

## Assumptions and scope
The vertex set is \(\mathbb Z/13\mathbb Z\). Its quadratic-residue connection set is
\[
Q=\{1,3,4,9,10,12\}.
\]
For each vertex \(v\), the **open** graph neighborhood is \(N(v)=v+Q\) and does not contain \(v\). A nonempty vertex set \(\sigma\) is a simplex of \(X\) if and only if \(\sigma\subseteq N(v)\) for at least one \(v\). This complex is neither the clique complex nor the independence complex of the same graph. Every equivalence concerns the geometric realization of finite abstract simplicial complexes. The affine group has \(13\cdot6=78\) elements; all of them preserve the stated simplex relation.

The certificate uses vertex labels \(0,\ldots,12\). An edge or simplex is an increasing list of vertex labels, and its oriented simplicial chain has that increasing order. The files `certificate.json` and `verify.py` together specify and check all finite combinatorial operations.

## Proof
**Complete face construction.** Form all nonempty subfaces of the thirteen six-vertex neighborhoods. Direct enumeration yields exactly \(598\) faces, with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(13,78,221,195,78,13).
\]
The verifier reconstructs all these faces directly from modular quadratic residues rather than trusting the stored counts.

**Actual elementary collapse.** The attached `certificate.json` lists \(227\) ordered pairs \((\sigma,\tau)\) of simplices. At each step the verifier checks, in the **current** complex, that \(\sigma\) is a codimension-one face of \(\tau\), and that \(\tau\) is its **unique** codimension-one coface. This is the elementary free-face condition: if a larger coface existed, it would produce another codimension-one coface. Delete the pair and continue. After all \(227\) elementary collapses, there are \(13\) vertices, \(59\) edges, \(72\) triangles, and no higher simplices. Thus the resulting two-dimensional complex \(Y\) is homotopy equivalent to \(X\).

**Trivial fundamental group.** The certificate next lists \(12\) graph edges. A disjoint-set reconstruction verifies that they form a spanning tree in the reduced one-skeleton. Contract that tree in the edge-path presentation of \(\pi_1(Y)\). The remaining \(59-12=47\) edges initially give \(47\) generators. The certificate lists \(47\) triangles, each of whose boundaries contains *exactly one* edge still representing a nontrivial generator at that stage; the other two edges are already trivial in the quotient presentation. Its relation therefore kills that remaining generator (or its inverse). The verifier checks these set inclusions against the complete reconstructed face list, with no numerical approximation. After \(47\) eliminations no generator remains, proving \(\pi_1(Y)=1\).

**Integral homotopy.** The connected two-dimensional complex has Euler characteristic \(13-59+72=26\). Since it is simply connected and has no cells above degree two, its only reduced integral homology is \(H_2(Y;\mathbb Z)\cong\mathbb Z^{25}\). More precisely, the integral cellular chain boundary in degree two is surjective onto the group of one-cycles because \(H_1=0\), and its kernel is free of rank \(25\). By Hurewicz each chosen basis element is represented by a map from \(S^2\); the resulting map from a wedge of \(25\) two-spheres induces an isomorphism on all integral homology. Since both spaces are simply connected CW complexes, the homological Whitehead theorem proves the asserted homotopy equivalence. This does **not** claim the collapse to be equivariant.

**Complete affine rational character.** For a simplicial symmetry, the alternating trace on oriented simplicial chains is the sum over preserved faces, each weighted by its orientation sign and alternating dimension. Subtracting the trace \(1\) on unreduced degree-zero homology gives the trace on \(H_2(X;\mathbb Q)\), because all other reduced rational homology groups vanish. The independent finite Lefschetz calculation evaluates all \(598\) faces for all \(78\) affine symmetries and confirms the displayed values. A nontrivial translation has no stabilized nonempty face, as its nonempty orbits have size \(13\) but every face has at most \(6\) vertices; its reduced Lefschetz number is consequently \(-1\). Each element with multiplier \(a\ne1\) is conjugate by a translation to pure multiplication by \(a\). Direct exact signed face sums for the six multipliers are \(25\) at \(a=1\), and \(1\) at each of \(a=3,4,9,10,12\). These are exhaustive finite computations, validated by `verify.py`.

The permutation character of \(W\) is the number of affine-fixed vertices. The character of \(W\oplus(W/\mathbb Q\mathbf1)\) is twice that number minus one: \(25\) for the identity, \(-1\) for nontrivial translations, and \(1\) for other affine elements (which each have exactly one fixed vertex). This matches the fully computed homology character. Rational representations of finite groups are semisimple and are determined by their ordinary characters; hence the displayed rational module isomorphism follows. The quotient augmentation module has no affine invariants, whereas \(W\) has exactly one invariant line.

## Verification
In a directory containing `certificate.json` and `verify.py`, execute `python3 verify.py` with Python's standard library. The program independently reconstructs the Paley graph, the initial \(598\) simplices, every free-face condition for all \(227\) elementary collapses, the reduced face vector, the proposed connected acyclic spanning tree, all \(47\) unit-generator triangle-relator eliminations, the Euler characteristic, and the exact signed Lefschetz character on all \(78\) affine elements. The companion `verification_output.txt` records a completed execution terminating in `VERIFY_OK`. Every finite claim in the argument is checked from those two supplied files. No external computation or historical file is required.

## Relationship to prior work
Kahle's work on random-graph neighborhood complexes supplies the standard topological setting and studies probabilistic connectivity; it makes no exact assertion about this deterministic \(13\)-vertex graph. Elsawy's account determines the Paley graph and its affine symmetries, but not the neighborhood complex's homotopy type or its homology action. Shukla classifies neighborhood complexes of graphs with maximum degree at most three and of four-regular circulants; the present Paley graph is six-regular, so that theorem does not specialize to this case.

For statement-level overlap, a published record concerning the ordinary neighborhood complex of the \(17\)-vertex Paley graph computes a different complex with nontrivial three-torsion and a different homotopy type. Another published record determines the neighborhood complex of the \(5\)-regular Clebsch graph; those vertices and adjacencies differ from the six-regular \(P_{13}\). Results about the clique complex of \(P_{13}\), which is a torus, are distinct: here the same graph is used in the **common-open-neighbor** construction, whose dimension and homology differ. None of those statements supplies a homotopy equivalence or rational affine character for \(\mathcal N(P_{13})\). Literature coverage is necessarily nonexhaustive.

## Limitations
The homotopy equivalence was established nonequivariantly; no equivariant collapsing sequence, equivariant homotopy equivalence, or integral \(\mathbb Z[G]\)-lattice decomposition is claimed. The representation is determined **over \(\mathbb Q\)**, not integrally. The exact certificate covers this single graph order only and proves no uniform result for all Paley graphs. A differently named treatment of \(\operatorname{Hom}(K_2,P_{13})\), a Dowker complex, or another unindexed equivalent formulation could cover some or all of the result; no exhaustive priority claim is asserted.

## References
1. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first public 2005-12-04. https://arxiv.org/abs/math/0512077 .
2. A. N. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818, first public 2012-03-07. https://arxiv.org/abs/1203.1818 .
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13. https://arxiv.org/abs/1802.04526 .
4. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, published research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
5. *The 5-regular Clebsch neighborhood complex is a wedge of 31 two-spheres*, published research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a .
