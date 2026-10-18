# The homotopy type and affine homology character of the Paley-\(11\) tournament neighborhood complex

## Finding
Let \(Q=\{1,3,4,5,9\}\subset\mathbb F_{11}^{\times}\) be the nonzero squares and let \(T\) be the quadratic-residue tournament with \(u\to v\) precisely when \(v-u\in Q\). Let \(X=\mathcal N^+(T)\) be its out-neighborhood complex, with facets \(F_t=t+Q\), \(t\in\mathbb F_{11}\). Then
\[
X\simeq\bigvee^{21}S^2.
\]
The natural affine group \(G=\{x\mapsto ax+b:a\in Q,\ b\in\mathbb F_{11}\}\), of order \(55\), acts on \(\widetilde H_2(X;\mathbb Q)\) with character
\[
\chi(g)=\begin{cases}21,&g=1,\\-1,&g(x)=x+b\text{ for }b\ne0,\\1,&g(x)=ax+b\text{ for }a\ne1.\end{cases}
\]
Consequently \(\widetilde H_2(|X|/G;\mathbb Q)\cong\mathbb Q\), and the other reduced rational homology groups of the quotient vanish. In the standard classification of Paley-tournament automorphisms, \(G\) is the full automorphism group of \(T\).

## Assumptions and scope
All simplicial complexes are finite, faces are subsets of their declared facets, and simplicial homotopy and homology use ordinary unoriented geometric realizations with integral coefficients unless otherwise indicated. A two-element set is an edge and a three-element set is a triangle. The Euler characteristic excludes the empty face. The action of \(G\) on faces is simplicial; a quotient means the topological quotient of the geometric realization. The theorem concerns only the specified \(11\)-vertex tournament, its out-neighborhood complex, and its affine automorphisms; no statement is made for all Paley tournaments or arbitrary biplanes.

## Proof
**1. Incidence design.** Direct subtraction in \(Q\) shows that each nonzero element of \(\mathbb F_{11}\) occurs exactly twice in the ordered difference multiset \(\{q-q':q,q'\in Q,\ q\ne q'\}\). Thus every pair of distinct facets \(F_s,F_t\) intersects in exactly two vertices. Equivalently every two vertices lie in exactly two of the eleven facets. A simplex of cardinality at least three is therefore in at most one facet. The complete face counts in cardinalities one through five are
\[
(f_0,f_1,f_2,f_3,f_4)=(11,55,110,55,11).
\]
In particular, the one-skeleton is the complete graph \(K_{11}\), precisely \(55\) of its \(165\) possible triangles are absent, and \(\chi(X)=11-55+110-55+11=22\).

**2. Fundamental group.** The triangle \(A=\{0,1,3\}\) is absent: it is not contained in any \(F_t\). However, the three triangles \(\{0,1,2\},\{0,2,3\},\{1,2,3\}\) are present (in \(F_8,F_{10},F_9\), respectively). Hence the boundary of \(A\) is null-homotopic within \(X\), by the three triangular faces coned to vertex \(2\). Every affine map in \(G\) preserves \(X\). The stabilizer of \(A\) injects into the permutation group on its three vertices, and its size divides both \(55\) and \(6\), hence is trivial. Its orbit therefore has \(55\) members, exactly the number of missing triangles. Every missing triangular edge loop is therefore filled by an affine image of the same three-triangle disk. The cycles bounding all triangles of the complete one-skeleton normally generate its fundamental group (use the star at vertex \(0\) as a spanning tree). Therefore \(\pi_1(X)=0\).

**3. Dimension-reducing elementary collapses.** For each of the eleven five-vertex facets \(F\), order its vertices \(v_1<v_2<v_3<v_4<v_5\). First remove the free pair \((\{v_1,v_2,v_3,v_4\},F)\). Next, for each of the four triples \(B\subset\{v_1,v_2,v_3,v_4\}\), remove the pair \((B,B\cup\{v_5\})\). Each is elementary: after the first removal the indicated triangle \(B\) lies in a unique remaining tetrahedron, and different original facets share no triangle. All \(55\) pairs are legal. The remaining complex is connected, simply connected, and two-dimensional, with face counts \((11,55,66)\), so it has Euler characteristic \(22\). Its integral first homology vanishes, its second homology is free (a subgroup of its free cellular two-chains), and the Euler characteristic forces rank \(21\). For a simply connected two-dimensional CW complex, Hurewicz yields maps of \(21\) two-spheres representing a homology basis, and the homological Whitehead theorem makes the resulting wedge map a homotopy equivalence. Thus \(X\simeq\bigvee^{21}S^2\).

**4. Affine character and quotient.** For an affine symmetry \(g\), the signed simplicial Lefschetz number is the alternating sum of signed fixed-face contributions. If \(g\) is a nontrivial translation, all its vertex cycles have length \(11\), whereas a nonempty simplex has at most five vertices; consequently its unreduced Lefschetz number is \(0\). Its reduced Lefschetz number, and hence its trace on \(\widetilde H_2\), is \(-1\). If \(g(x)=ax+b\) with \(a\ne1\), it has one fixed vertex \(c=b/(1-a)\) and two orbits of length five, \(c+Q\) and \(c+(\mathbb F_{11}^{\times}\setminus Q)\). Its only nonempty invariant faces are the vertex \(\{c\}\) and the facet \(c+Q\): the other five-orbit is disjoint from \(c+Q\) and cannot be a facet because distinct facets meet in two vertices. A five-cycle acts with positive orientation sign on the invariant four-simplex, so the unreduced Lefschetz number is \(1+1=2\), giving reduced trace \(1\). The identity has trace \(21\). Finally finite-group transfer in characteristic zero, after barycentric subdivision if necessary, identifies the quotient's rational homology with the invariant rational homology. Averaging the character gives
\[
\dim_{\mathbb Q}\widetilde H_2(|X|/G;\mathbb Q)=\frac{21+10(-1)+44(1)}{55}=1.
\]
No other reduced rational homology is present.

## Verification
The standalone `check_structural.py` enumerates every face, confirms the incidence parameters, the orbit of all missing triangles and its common filler, and checks the precise \(55\) elementary collapses against the current face poset. The separate `check_equivariant.py` reconstructs all \(55\) affine maps and computes their signed fixed-face Lefschetz numbers directly on the nonempty simplices. Their deterministic recorded outputs are `structural_output.txt` and `equivariant_output.txt`. Run from a directory containing these files using `python3 check_structural.py` and `python3 check_equivariant.py`.

## Relationship to prior work
Dochtermann and Singh introduce the directed out-neighborhood complex (Definition 4.1), identify its homotopy type with a directed edge Hom complex (Theorem 4.3), provide general vanishing estimates (Theorem 4.12), and explicitly ask which homotopy types occur for tournaments (Section 7.1). Their general statements do not determine this particular tournament's \(21\) sphere summands or its affine homology action. Jones describes the Paley tournament and its automorphism group, but does not calculate its neighborhood-complex homology. Results on the directed *flag* complex of a Paley tournament and on neighborhood complexes of undirected Paley *graphs* concern different simplicial complexes and do not imply this theorem.

## Limitations
Only the specified \(11\)-vertex quadratic-residue tournament is classified. The quotient assertion is rational and does not determine its integral torsion or full homotopy type. The result does not establish a general theorem for all doubly regular tournaments or for all symmetric designs, nor does it claim an independently audited novelty determination.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first posted 2021-08-24; especially Definition 4.1, Theorems 4.3 and 4.12, and Sections 5 and 7.1.
2. G. A. Jones, *Paley and the Paley graphs*, arXiv:1702.00285 (2017); Section 9.7 describes automorphisms of Paley tournaments.
