# A 34-three-sphere wedge and full dihedral character for the hexagonal antiprism

## Finding

Let \(A\) be the twelve-vertex hexagonal-antiprism graph, realized on \(\mathbb Z/12\mathbb Z\) by joining residues of cyclic difference \(\pm1\) or \(\pm2\). Let \(X=\operatorname{Ind}_2(A)\) comprise vertex sets whose induced connected components have at most two vertices. Then the **integral homotopy type** is

\[
X\simeq\bigvee^{34}S^3.
\]

The full graph automorphism group is the dihedral group \(D_{12}=\langle r,s:r^{12}=s^2=1,\ srs=r^{-1}\rangle\), acting by \(r(i)=i+1\) and \(s(i)=-i\). Its rational character on \(\widetilde H_3(X;\mathbb Q)\), in the order \(r^k\) for \(0\leq k<12\), is

\[
\chi(r^k)=(34,1,1,-2,1,1,10,1,1,-2,1,1),\qquad
\chi(sr^k)=4\quad(0\leq k<12).
\]

Thus the fixed subspace under the entire automorphism group has dimension \(4\). The antipodal half-turn \(r^6\) has positive and negative rational eigenspaces of dimensions \(22\) and \(12\), respectively.

## Assumptions and scope

The graph is finite, simple, and undirected. Its vertex set is exactly the twelve residues \(0,1,\ldots,11\), with the stated adjacency, and it is regarded as a one-dimensional graph, not as a filled triangulation of a polyhedral surface. The complex contains the empty face and every nonempty subset \(S\) for which no selected vertex has two selected neighbors in \(A\). Equivalently, each induced connected component of \(A[S]\) is either one vertex or one edge. All homotopy and integral-homology assertions refer to the geometric realization of this finite abstract simplicial complex. Rational characters refer to the natural action of graph automorphisms on oriented simplicial chains and hence on homology.

## Proof

**Exact face criterion and exhaustive range.** For any simple graph, each induced component has at most two vertices if and only if the induced maximum degree is at most one. In this graph every vertex \(i\) has precisely the four neighbors \(i\pm1,i\pm2\), with arithmetic modulo \(12\). Hence for each of the \(2^{12}-1=4095\) nonempty masks \(m\), one tests that every selected \(i\) satisfies

\[
\left|\{j\in\{i-2,i-1,i+1,i+2\}:j\text{ is selected}\}\right|\leq1.
\]

The resulting complete face counts in dimensions \(0,1,2,3,4,5\) are respectively \((12,66,172,207,60,4)\), totalling \(521\) nonempty faces. This is a finite exhaustive enumeration, not a sample.

**Acyclic discrete-Morse certificate.** The file `matching_pairs.json` records \(243\) disjoint pairs \((a,b)\) of nonempty face masks, with \(a\subset b\) and \(|b\setminus a|=1\). Reconstruct all \(1800\) cover relations in the nonempty face poset. Orient every unpaired relation from the smaller face to the larger face, and every paired relation in the opposite direction. The checker `verify_morse.py` verifies each of the \(243\) incidences, checks that every face occurs at most once in the matching, reconstructs the full oriented graph, and certifies its acyclicity by a topological sort visiting all \(521\) vertices. Precisely \(35\) faces remain unpaired: one vertex and \(34\) tetrahedra (dimension-three faces). Thus the finite discrete-Morse theorem provides a CW complex with exactly one \(0\)-cell, \(34\) cells of dimension \(3\), and no other cells. Every attaching map of a \(3\)-cell has domain \(S^2\) and targets a point. The CW complex is the stated wedge of \(34\) three-spheres. In particular, all integral homology is torsion-free and \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{34}\), with all other reduced groups zero.

**Automorphisms.** Edges at cyclic distance one have exactly two common graph neighbors; edges at cyclic distance two have exactly one. Hence the twelve distance-one edges are intrinsically characterized, and every graph automorphism preserves the underlying twelve-cycle. Conversely every rotation and reflection of that cycle preserves distances one and two. Therefore \(\operatorname{Aut}(A)=D_{12}\), of order \(24\).

**Full homology character.** For an automorphism \(g\), let \(F_g\) be the nonempty faces invariant as sets under \(g\). Each such face contributes its induced orientation sign \(\epsilon(g,S)\in\{\pm1\}\) to the simplicial Lefschetz number. Since the preceding Morse proof leaves reduced rational homology only in degree three, the exact trace is

\[
\operatorname{tr}\big(g\mid\widetilde H_3(X;\mathbb Q)\big)
=1-\sum_{S\in F_g}(-1)^{|S|-1}\epsilon(g,S).
\]

A separate checker `verify_equivariant.py` enumerates the complex from all forbidden three-vertex path supports and evaluates this signed sum for each of the \(24\) dihedral automorphisms. It returns the \(12\) rotation traces and \(12\) reflection traces displayed above. The average of these character values is \(4\), giving the invariant dimension by the fixed-space projection formula. Since \(r^6\) is an involution with trace \(10\) on a \(34\)-dimensional space, its \(\pm1\) eigenspace dimensions are \((34\pm10)/2=(22,12)\).

## Verification

The standalone files `verify_morse.py`, `verify_equivariant.py`, and `matching_pairs.json` form an exact finite certificate without third-party packages. Run both scripts using Python 3 with all three files in the same directory. Their exact recorded standard outputs are included in `morse_output.txt` and `equivariant_output.txt`.

The first checker verifies the entire \(521\)-face poset, all \(243\) matched covering pairs, \(1800\) oriented covers, a complete topological order, and the stated critical-cell profile. The second constructs the faces by a different characterization (forbidden triples), computes the complete mod-two simplicial boundary ranks \((0,11,55,117,56,4)\) in degrees \(0\) through \(5\), and checks the resulting mod-two Betti numbers independently. It also evaluates all signed fixed-simplex traces, the invariant dimension, and the half-turn eigenspace dimensions. Integer homotopy follows from the first check, not from mod-two homology.

## Relationship to prior work

Higher-independence complexes of graphs were defined and studied by Deshpande, Shukla, and Singh; their 2020 paper develops connectivity bounds and determines wedge-of-spheres behavior for chordal graphs, without giving this twelve-vertex nonchordal example. Sawant's May 2026 work proves vertex decomposability for higher-independence complexes of all trees; the antiprism graph is not a tree. Deshpande, Goyal, and Sawant's July 2026 paper determines path-free complexes for complete multipartite graphs, including their three-path-free case; the cyclic antiprism is not complete multipartite. Thus the present exact homotopy and full dihedral character are not consequences of those stated family classifications.

The terminology \(\operatorname{Ind}_2(A)\) and three-path-free complex describes the same object here: no induced vertex subset may contain a three-vertex path as a subgraph, whether or not that path is itself induced. In particular, triangles are forbidden as well. The graph is also the square of the twelve-cycle, so literature phrased in terms of cycle powers and their circulant representations is directly relevant. Targeted comparisons did not locate a prior exact result for this combination of graph, forbidden induced components, and full symmetry character; that negative search is not a proof of global uniqueness.

## Limitations

This establishes the exact finite twelve-vertex result. It neither asserts a uniform formula for all antiprism sizes nor establishes shellability or vertex decomposability. Although the homotopy type is a wedge of spheres, an acyclic Morse matching does not by itself prove a simplicial collapse directly onto a wedge subcomplex. Bibliographic searches can miss inaccessible or unindexed results.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, initially publicly posted 2026-05-24. https://arxiv.org/abs/2605.25150
2. Priyavrat Deshpande, Shuchita Goyal, and Rutuja Sawant, *On a Complete Characterization of Path-Free Complexes Associated with Complete Multipartite Graphs*, arXiv:2607.05358 (2026). https://arxiv.org/abs/2607.05358
3. Priyavrat Deshpande, Samir Shukla, and Anurag Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775 (2020). https://arxiv.org/abs/2001.06775
