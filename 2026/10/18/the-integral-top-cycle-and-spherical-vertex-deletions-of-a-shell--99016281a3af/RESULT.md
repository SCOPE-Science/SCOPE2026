# The integral top cycle and spherical vertex deletions of a shellable non-vertex-decomposable circulant

## Finding
Let \(G=C_{16}(1,4,8)\) and \(K=\operatorname{Ind}(G)\). This is the classical smallest known well-covered circulant with a shellable, non-vertex-decomposable independence complex. The following sharper topological and chain-level description holds.

For **every** vertex \(v\), the induced deletion \(K-v\) simplicially collapses onto a triangulated two-sphere with \(10\) vertices, \(24\) edges, and \(16\) triangles; its link satisfies
\[
K-v\simeq S^2,\qquad \operatorname{lk}_K(v)\simeq S^2\vee S^2.
\]
The rank-one integral group \(H_3(K;\mathbb Z)\) has a unique primitive cycle up to sign, supported on **all 80 tetrahedral facets**. Its coefficients have absolute value one on 64 facets and two on 16 facets. It is fixed by all rotations and reflections of the labeled circulant. The exact simplicial \(\ell_1\)-norm of the primitive generator is therefore \(96\), whereas its nonzero mod-two reduction has support on only \(64\) tetrahedra. In particular,
\[
H_3(K[W];\mathbb Z)=0\quad\text{for all proper }W\subsetneq\mathbb Z/16\mathbb Z.
\]
Thus every vertex is necessary to support a nonzero ambient integral third-homology class. The previously known shellability implies \(K\simeq S^3\); the novelty here is the local deletion/link topology and the fully supported, nonuniform, integral fundamental cycle.

## Assumptions and scope
The finite simple graph has vertex set \(\mathbb Z/16\mathbb Z\); distinct vertices \(a,b\) are adjacent precisely when \(\min\{(a-b)\bmod16,(b-a)\bmod16\}\in\{1,4,8\}\). An independent vertex subset is a face of \(K\). A tetrahedron \([a,b,c,d]\) is oriented by its increasing vertex order. Simplicial integral boundary operators have the usual alternating signs. The simplex \(\ell_1\)-norm is the sum of absolute coefficients in this oriented basis. A primitive cycle means a generator of \(\ker(\partial_3)\) over \(\mathbb Z\), not a normalized real cycle.

Write \(r(a)=a+1\bmod16\) and \(s(a)=-a\bmod16\). These graph symmetries generate the natural dihedral action of order \(32\). On oriented faces they act with the sign of the permutation required to restore increasing vertex order.

## Proof
**The top cycle.** Direct enumeration gives the face vector (excluding the empty simplex)
\[
(f_0,f_1,f_2,f_3)=(16,80,144,80).
\]
The tetrahedra form four dihedral orbits, of respective sizes \(16,32,16,16\). For a representative \(\tau\), let \(\mathcal O(\tau)\) denote the *signed* orbit sum whose coefficient on the increasing orientation of \(\tau\) is \(+1\). The stabilizers preserve this orientation, so these sums are unambiguously defined. In order, take the representatives
\[
(0,2,5,7),\ (0,2,5,11),\ (0,2,7,9),\ (0,3,6,9).
\]
The following integral chain is central:
\[
z=\mathcal O(0,2,5,7)-\mathcal O(0,2,5,11)
   +2\mathcal O(0,2,7,9)+\mathcal O(0,3,6,9).
\]
There are six dihedral orbits of triangles. For representatives of those orbits, the coefficients in the four orbit boundaries are, respectively,
\[
\begin{array}{c|r|rrrr}
\text{triangle}&\text{orbit size}&\partial\mathcal O_1&\partial\mathcal O_2&\partial\mathcal O_3&\partial\mathcal O_4\\\hline
(0,2,5)&32&-1&-1&0&0\\
(0,2,7)&32&1&-1&-1&0\\
(0,2,9)&16&0&0&0&0\\
(0,3,6)&16&0&0&0&0\\
(0,3,9)&32&0&1&0&1\\
(0,5,10)&16&0&0&0&0
\end{array}
\]
Each row annihilates the weight vector \((1,-1,2,1)\). Dihedral equivariance therefore gives \(\partial_3z=0\) over the integers. Every tetrahedron occurs. The numbers of coefficients of absolute values \(1\) and \(2\) are \(64\) and \(16\), giving \(\|z\|_1=96\). The two generators \(r,s\) preserve each signed orbit sum, so they fix \(z\).

**Primitivity and uniqueness.** The explicit mod-two \(144\times80\) third-boundary matrix has rank \(79\), verified by reproducible bit-exact Gaussian elimination in `verify.py`. Hence its rational rank is at least \(79\). The nonzero integral cycle \(z\) bounds the rational rank above by \(79\). Thus \(\ker(\partial_3;\mathbb Q)\) is one-dimensional. Because some coefficient of \(z\) is \(1\) or \(-1\), it is primitive, so \(\ker(\partial_3;\mathbb Z)=\mathbb Z z\). There are no four-simplices. Consequently \(H_3(K;\mathbb Z)=\mathbb Z[z]\), with only \(\pm z\) as primitive representatives. Modulo two, the 16 coefficients of magnitude two disappear and the unique nonzero top cycle has 64 facets. Any proper induced subcomplex has third-cycle module zero, since its cycles embed into \(\mathbb Z z\) but omit at least one facet in \(z\).

**Vertex deletions.** The accompanying `deletion_collapse.json` lists \(106\) successive free-face/coface pairs in \(K-0\). Each pair is checked against the *current* simplicial complex in `verify.py`. Removing the pairs leaves a two-dimensional complex with face vector \((10,24,16)\); each edge is in exactly two triangles, each vertex link is a single cycle, and the complex is connected. Its Euler characteristic is \(2\), so it is a triangulated \(S^2\). Rotation gives the same simplicial collapse for each of the sixteen vertex deletions.

**Vertex links.** The link of \(0\) has face vector \((10,27,20)\). In `link_spheres.json`, its triangles are partitioned into two closed subcomplexes \(A\) and \(B\), each a connected triangulated sphere, with face vectors \((10,24,16)\) and \((6,12,8)\). Their intersection has face vector \((6,9,4)\) and is a collapsible four-triangle disk. Thus \(\operatorname{lk}_K(0)=A\cup B\simeq S^2\vee S^2\) by the homotopy-pushout property for simplicial subcomplexes. Translation gives the same result for every link.

The published shelling of \(K\), combined with its reduced Euler characteristic \(-1\), yields the previously known equivalence \(K\simeq S^3\), consistent with the chain calculation above.

## Verification
Run `python3 verify.py` beside `deletion_collapse.json` and `link_spheres.json` using Python 3 with no external dependencies. The program reconstructs all independent subsets, computes the four signed facet orbits, checks the integral boundary, performs exact mod-two elimination, verifies the dihedral action, replays each elementary collapse, tests every remaining surface vertex link and global connectivity, checks the two link spheres, and collapses their intersection. It prints `VERIFY_OK` only after all assertions succeed. No floating-point arithmetic, random trials, or extrapolation from smaller graphs is used.

## Relationship to prior work
Earl, Vander Meulen and Van Tuyl prove shellability and non-vertex-decomposability of this circulant and provide an explicit shelling order of its \(80\) facets. The initial public description appeared in a 2014 mathematical discussion. Vander Meulen and Van Tuyl later construct lexicographic families from this graph; Mafi, Naderi and Soufivand reuse it as a shellability counterexample. Those results give the classical status of the graph but not the sphere-collapse type of each deletion, the two-sphere-wedge link type, or a primitive integral top-cycle coefficient/orbit classification. The general implication from pure shellability to a sphere wedge already determines the ambient \(S^3\) homotopy type from the known shelling and face vector; that implication is not asserted as new.

## Limitations
The result concerns this exact 16-vertex graph and its ordinary independence complex, not all shellable non-vertex-decomposable complexes, other circulants, or their lexicographic expansions. The theorem is an exact finite calculation and a finite topological certificate, not a general family classification. Publication priority beyond the inspected literature is not certified; an equivalent calculation under different terminology might exist. No independent external scientific audit has been performed.

## References
1. Adam Van Tuyl, *Flag complexes that are shellable but not vertex decomposable*, MathOverflow question, first posted 11 September 2014. https://mathoverflow.net/questions/180666/flag-complexes-that-are-shellable-but-not-vertex-decomposable
2. Jonathan Earl, Kevin N. Vander Meulen and Adam Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837v1, 11 May 2015; especially Theorem 6.1, its proof, and Remark 6.2. https://arxiv.org/abs/1505.02837
3. Kevin N. Vander Meulen and Adam Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, arXiv:1505.02838v1, 12 May 2015; especially Theorem 4.4. https://arxiv.org/abs/1505.02838
4. Amir Mafi, Dler Naderi and Parasto Soufivand, *On vertex decomposability and regularity of graphs*, International Electronic Journal of Algebra 33 (2023), 205–212, DOI:10.24330/ieja.1217285; especially Theorem 2.4 and Example 2.5.
