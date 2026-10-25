# Parity and dihedral homology of the doubled cyclic four-polytope boundary

## Finding
For every integer \(n\geq5\), let \(X_n\) denote the simplicial boundary of the cyclic four-polytope \(C(n,4)\), with its vertices indexed in cyclic order by \(\mathbb Z/n\mathbb Z\). Let \(D(X_n)\) be its simplicial double: the vertices of \(D(X_n)\) are the two-element faces of \(X_n\), and two vertices span an edge precisely when they are disjoint and their union is a tetrahedral face of \(X_n\). Since \(X_n\) is three-dimensional, \(D(X_n)\) is a graph.

**Topological classification.** If \(n\) is odd, \(D(X_n)\) is connected and
\[
D(X_n)\simeq \bigvee^{\,n(n-4)+1}S^1.
\]
If \(n\) is even, its two components are characterized by whether the difference of the two indices defining a graph vertex is odd or even. The corresponding homotopy types, respectively, are
\[
\bigvee^{\,3n^2/4-3n+1}S^1
\quad\text{and}\quad
\bigvee^{\,n(n-4)/4+1}S^1.
\]
All integral homology is therefore free abelian; the only positive reduced homology is in degree one. For even \(n\), reduced degree-zero homology is a single copy of \(\mathbb Z\).

**Complete dihedral character.** The natural combinatorial \(D_n\)-action on the cyclically labeled boundary induces an action on \(H_1(D(X_n);\mathbb Q)\). Write \(R_b(i)=i+b\) and \(S_b(i)=b-i\) modulo \(n\), with \(b\in\mathbb Z/n\mathbb Z\), and let \(\chi(g)\) be the trace on first rational homology. For odd \(n\),
\[
\chi(R_0)=n(n-4)+1,\qquad
\chi(R_b)=1\ (b\not\equiv0),\qquad
\chi(S_b)=3-n.
\]
For even \(n\),
\[
\chi(R_0)=n(n-4)+2,\qquad
\chi(R_{n/2})=2-n,\qquad
\chi(R_b)=2\quad(b\not\equiv0,n/2),
\]
and
\[
\chi(S_b)=\begin{cases}4-n,&b\ \text{even}\\2-n,&b\ \text{odd}.\end{cases}
\]
Thus the topology has a sharp parity transition even though each input \(X_n\) is a simplicial three-sphere.

## Assumptions and scope
Throughout, \(C(n,4)\) means the convex hull of \(n\) points on the real moment curve in increasing parameter order; only its abstract boundary simplicial complex is used. Its facets are exactly the four-subsets obtained as unions of two vertex-disjoint edges of the cyclic polygon on \(n\) vertices, by Gale evenness for dimension four. The two-subsets are all faces because the polytope is two-neighborly. The simplicial double is as in Lesh–Schreiner–Wahl, Definition 2.1. The dihedral action here is the natural subgroup of combinatorial automorphisms preserving the cyclic vertex order, not a claim about the full automorphism group. All ranks concern ordinary integral homology; the displayed character concerns rational first homology.

## Proof
**1. Facets and graph edges.** Let \(E_i=\{i,i+1\}\) denote the \(n\) edges of the cyclic polygon, with indices modulo \(n\). Gale evenness in dimension four says that the tetrahedral facets of \(X_n\) are precisely \(E_i\cup E_j\) for distinct disjoint polygon edges. The number of facets is therefore
\[
F=\binom n2-n=\frac{n(n-3)}2.
\]
Every unordered pair of original vertices is an edge of \(X_n\), hence a vertex of the double. Each facet has exactly three partitions into complementary unordered pairs; these give three different graph edges of \(D(X_n)\). Different facets cannot give the same double edge because the union of its two pair-vertices recovers the facet. Consequently
\[
V=\binom n2=\frac{n(n-1)}2,
\qquad E=3F=\frac{3n(n-3)}2.
\]
More explicitly, any two disjoint polygon edges \(E_i,E_j\) produce the three edges connecting the complementary pairs of their four endpoints. In particular, for an arc \(i,i+1,\ldots,j\) of length \(d\geq3\), the double graph contains
\[
\{i,j\}\;\text{---}\;\{i+1,j-1\},
\]
by using the two disjoint polygon edges \(\{i,i+1\}\) and \(\{j-1,j\} \).

**2. Components.** Repeatedly apply the displayed edge to shorten any chosen arc between the two endpoints by two. If \(n\) is odd, at least one of the two arcs is odd, so every double vertex is connected to a polygon edge \(\{i,i+1\}\). All such short-edge vertices form a connected subgraph: any two disjoint polygon edges are adjacent in the double, and the disjointness graph of the polygon edges is connected for \(n\geq5\). Hence the double is connected.

If \(n\) is even, label each double vertex \(\{i,j\}\) by the parity of \(i-j\). Each tetrahedral facet has exactly two vertices of each parity, so complementary pair-vertices always have the same parity; no double edge crosses these classes. Every odd-parity pair can be shortened to a polygon edge as before. Every even-parity pair can be shortened to a length-two pair \(\{i,i+2\}\); all these are connected by the double edges
\[
\{i,i+2\}\;\text{---}\;\{i+1,i+3\},
\]
again arising from disjoint polygon edges, for \(n\geq6\). Both classes are nonempty and internally connected, so there are precisely two components.

**3. Integral homotopy and ranks.** Every connected finite graph is homotopy equivalent, by collapsing a spanning tree, to a wedge of \(E-V+1\) circles. For odd \(n\) this yields \(n(n-4)+1\). For even \(n\), the odd-parity pair-vertices are the \(n^2/4\) pairs with opposite parity, and even-parity pair-vertices are the \(n(n-2)/4\) pairs with equal parity. Each tetrahedral facet supplies two double edges joining opposite-parity pairs and one joining same-parity pairs. Thus the corresponding edge numbers are \(n(n-3)\) and \(n(n-3)/2\), and subtracting the respective vertex counts and adding one yields the displayed componentwise circle multiplicities. The integral homology assertions follow.

**4. Dihedral character.** Give each graph edge an arbitrary but fixed orientation. The equivariant graph chain exact sequence
\[
0\longrightarrow H_1(D(X_n);\mathbb Q)\longrightarrow C_1\xrightarrow{\partial}C_0\longrightarrow H_0\longrightarrow0
\]
shows that
\[
\chi(g)=\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid H_0).
\]
Every dihedral element fixes each of the two parity components when \(n\) is even, and the unique component when \(n\) is odd, so the last trace is \(2\) or \(1\), respectively. The trace on \(C_0\) equals the number of invariant unordered original-vertex pairs: it is \(V\) for the identity, \(n/2\) for a half-turn (when \(n\) is even), zero for other nonidentity rotations, \((n-1)/2\) for reflections when \(n\) is odd, and \(n/2\) for reflections when \(n\) is even.

For \(C_1\), a double edge fixed with its two endpoints in place contributes \(+1\), one with endpoints interchanged contributes \(-1\). An invariant tetrahedral facet on which the symmetry acts as two transpositions contributes \(-1\) in total from its three complementary-pair partitions: one partition has both double-graph endpoints individually fixed and contributes \(+1\), while the other two partitions each have their endpoints swapped and contribute \(-1\) apiece. The total signed trace is therefore \(+1-1-1=-1\). The identity contributes \(3F\). For a nonidentity rotation other than the half-turn, no facet is fixed (a possible four-cycle orbit would have no two neighboring polygon vertices); hence the trace is zero. A half-turn fixes exactly \(n/2\) facets, each assembled from a polygon-edge orbit of size two, so its trace is \(-n/2\).

For a reflection of an odd polygon, exactly one polygon edge is fixed and one of the \((n-1)/2\) other edge orbits comprises two incident edges. Thus exactly \((n-3)/2\) disjoint swapped-edge orbits produce fixed facets. For a reflection across opposite vertices of an even polygon, exactly two of the \(n/2\) edge orbits comprise incident edges, leaving \(n/2-2\) fixed facets. For reflection across opposite edges of an even polygon, the two fixed polygon edges form one facet, and the other \((n-2)/2\) two-element edge orbits are disjoint, making \(n/2\) fixed facets in total. In each case the reflection acts by two transpositions on the four facet vertices. The three respective \(C_1\) traces are therefore \(-(n-3)/2\), \(2-n/2\), and \(-n/2\). Substituting these and the \(C_0,H_0\) traces into the chain formula gives exactly the stated character table. This argument applies to every integer \(n\geq5\).

## Verification
The accompanying `verify_cyclic_double.py` builds facets independently from Gale evenness and from disjoint cyclic polygon edges, then builds every double edge from complementary pair partitions. For each \(5\leq n\leq24\), it checks all component sizes, integral first Betti ranks, and signed chain traces for every element of the natural dihedral action, totaling 580 symmetry calculations. It establishes finite consistency of the two facet descriptions and character formulas; the universal assertions follow from the proofs above rather than finite enumeration.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced doubling of arbitrary simplicial complexes and proved a general weak Cohen–Macaulay connectivity theorem [1]; their definition is used literally here. Their theorem concerns connectivity bounds, not the exact doubled graph of cyclic four-polytope boundaries or its integral homology and symmetry. Gale's classical facet-evenness criterion for cyclic polytopes [2] supplies the combinatorial input and is not claimed as new. The separate combinatorial-component, sphere-multiplicity, and complete dihedral-character conclusions are the proposed contribution.

## Limitations
The formula concerns dimension-four cyclic polytopes and their **first** simplicial double, not higher-dimensional polytopes or iterated doubling. Only the natural labeled dihedral subgroup is analyzed. The rational character does not classify the integral dihedral module up to isomorphism. Searches cannot exclude equivalent results under different terminology, and independent assessment of novelty and proof is outstanding.

## References
[1] Kathryn Lesh, Bridget Schreiner and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1, publicly submitted 2025-06-12, https://arxiv.org/html/2506.10436v1 (Definition 2.1; Sections 2–4).

[2] Gale's evenness criterion for cyclic polytopes; see M. M. Bayer and T. Bisztriczky, *On Gale and braxial polytopes*, arXiv:math/0610940, https://arxiv.org/abs/math/0610940, and standard treatments of the four-dimensional evenness characterization.
