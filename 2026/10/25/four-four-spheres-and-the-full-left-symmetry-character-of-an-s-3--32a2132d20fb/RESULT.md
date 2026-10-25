# Four four-spheres and the full left-symmetry character of an \(S_3\) directed-forest complex

## Finding
Let \(G=S_3=\langle r,s\mid r^3=s^2=1,\;srs=r^{-1}\rangle\), where \(r\) is a three-cycle and \(s\) is a transposition. Let \(D\) be the right Cayley digraph with precisely the arcs \(g\longrightarrow gr\) and \(g\longrightarrow gs\), for every \(g\in G\). Let \(K=\operatorname{DT}(D)\) be the abstract simplicial complex whose vertices are those twelve arcs and whose faces are directed forests: arc subsets with at most one incoming arc per group vertex and without directed cycles.

There is an integral homotopy equivalence
\[
K\simeq\bigvee^{4}S^4.
\]
Moreover, left multiplication by \(G\) preserves the complex. On its only nonzero reduced rational homology group, the action is
\[
\widetilde H_4(K;\mathbb Q)\cong
2\operatorname{sgn}\oplus\operatorname{Std}
\]
as a \(\mathbb Q[S_3]\)-module. Here \(\operatorname{sgn}\) denotes the one-dimensional sign representation and \(\operatorname{Std}\) the two-dimensional standard representation. In particular, no nonzero rational fourth-homology class is fixed by all left translations.

## Assumptions and scope
The generators and orientation matter. The arcs corresponding to \(s\) occur in reciprocal pairs; the arcs corresponding to \(r\) form two oppositely oriented three-cycles. This is *not* the digraph produced by taking two involutive reflection generators, nor the fully bidirected triangular-prism graph. The assertion concerns this precise twelve-arc digraph, with the convention that a directed forest admits at most one edge entering each vertex. The result is over the integers for homotopy and over the rationals for the representation statement.

For reproducible coordinates write each group element uniquely as \(r^a s^b\), with \(a\in\{0,1,2\}\), \(b\in\{0,1\}\). Order vertices by increasing \(b\), then \(a\). At \((a,b)\), list the \(r\)-arc first and the \(s\)-arc second. Then
\[
(a,b)r=(a+(-1)^b\pmod 3,b),\qquad
(a,b)s=(a,1-b).
\]
These conventions assign arc indices \(0,\ldots,11\), each representing one bit of a simplex mask. The dated reference used for the present definition is Engström's preprint of 2005-08-08; the present finite classification is not asserted for different Cayley presentations or arbitrary dihedral groups.

## Proof
**1. Complete face list.** Enumerate every integer mask \(m\in\{0,\ldots,2^{12}-1\}\). It is a face exactly when (i) no two selected arcs have the same target and (ii) the selected digraph is acyclic. Two independently coded tests, predecessor-chain detection and six-vertex topological sorting, agree for all \(4096\) masks. The resulting complex has \(432\) faces *including* the empty face, with cardinality counts
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,12,57,134,156,72).
\]

**2. An exact discrete-Morse matching.** Start with all nonempty faces unpaired. For each arc index \(e=0,1,\ldots,11\), and then in increasing order of the remaining masks \(m\) without bit \(e\), pair \(m\) with \(m\cup\{e\}\) whenever both are still unpaired faces. Never pair the empty face. This deterministic construction yields \(213\) face–coface pairs; its remaining five critical masks are \(1,1444,1620,2392,3968\), one of cardinality one and four of cardinality five.

Orient every codimension-one incidence downward, except reverse the edge belonging to each matched pair. A complete topological sort visits all \(431\) nonempty faces across \(1500\) oriented incidences. Hence the matching is acyclic, not merely cardinality-consistent. Forman's discrete Morse theorem produces a CW complex with one zero-cell and four four-cells and no other cells. All attaching maps have target the unique zero-cell, so this CW complex is a wedge of four four-spheres. This proves the integral homotopy equivalence; a finite-field rank calculation alone would not establish it.

**3. Symmetry character.** For \(g\in G\), left multiplication sends the arc \(h\to hz\) to \(gh\to ghz\), preserving its generator label and the forest condition. On the reduced simplicial chain complex, a setwise fixed face contributes the sign of the induced permutation of its ordered arc vertices to the chain trace. The exact alternating trace of the reduced chain complex is \(4\) on the identity, \(-2\) on each transposition, and \(1\) on each three-cycle. For independent reconstruction, the signed trace contributions by face cardinality \(k\) are, respectively,
\[
\begin{array}{c|rrrrrr}
&k=0&1&2&3&4&5\\\hline
1&1&12&57&134&156&72\\
\text{transposition}&1&0&-5&0&6&0\\
\text{three-cycle}&1&0&0&2&0&0
\end{array}
\]
with alternating sign \((-1)^{k-1}\), including \(k=0\). Since reduced homology is concentrated in degree four, Hopf's trace formula identifies these numbers with the fourth-homology character. Its inner products with the rational irreducible characters \((1,1,1)\), \((1,-1,1)\), and \((2,0,-1)\), in identity/transposition/three-cycle order, are \(0\), \(2\), and \(1\), respectively. This gives the stated representation decomposition.

## Verification
`verify.py` is a standalone Python 3 checker requiring no third-party packages. It reconstructs the group, arcs, all face masks, the lexicographic matching, and the full directed Hasse graph; checks acyclicity; verifies every group action preserves the face set; and computes exact signed fixed-face traces and the representation multiplicities. Independently of the Morse construction, it reduces simplicial boundary matrices over each of two finite fields and finds ranks \((1,11,46,88,68)\) in boundary degrees one through five. The recorded run in `VERIFY_OUTPUT.txt` terminates in `VERIFY_OK`. Those field ranks are a cross-check only: the integral homotopy assertion rests on the acyclic discrete-Morse certificate.

## Relationship to prior work
Engström (2005) formalizes the directed-tree complex and proves shellability for acyclic digraphs, which does not apply here because the \(r\)-arcs form directed triangles. Jojić (2011) treats complete-source digraphs and digraphs essentially supported on trees; the present strongly cyclic graph has neither property. Courtney (2020) studies Cayley directed-forest complexes; its accessible indexed description specifically discusses dihedral groups with two reflection generators, whereas the present generators have orders three and two. Its full thesis text was not accessible, so possible additional coverage remains a risk.

A separately indexed calculation of the *ordinary* discrete-Morse complex of the fully bidirected triangular prism gives a wedge of 64 four-spheres. That is a different eighteen-arc complex: the current twelve-arc complex is a proper subcomplex, so the published homotopy type of the larger complex does not determine this result or its left \(S_3\)-character. Searches for the two generator descriptions, directed-tree terminology, associated Morse complexes and equivariant homology found no theorem covering the joint claim.

## Limitations
This is one exact finite Cayley digraph, not a general formula for arbitrary generators, larger dihedral groups, or integral \(\mathbb Z[S_3]\)-module structure. The representation decomposition is rational, and it need not describe the integral module extension data. The literature comparison cannot rule out unindexed or inaccessible equivalent work; Courtney's relevant thesis was not inspected in full. Independent scientific verification is not claimed.

## References
1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, first posted 2005-08-08; definitions and acyclic-digraph homotopy results.
2. D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v1, first posted 2011-09-21; complete-source and essentially-tree results.
3. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University Master's thesis, 2020, DOI:10.18122/td/1684/boisestate; abstract and search-indexed excerpts examined, not complete full text.
4. *The triangular-prism Morse complex is a wedge of sixty-four four-spheres*, indexed public mathematical result, 2026; compared as a different, fully bidirected graph complex.
