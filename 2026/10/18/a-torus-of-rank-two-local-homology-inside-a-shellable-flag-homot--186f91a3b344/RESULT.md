# A torus of rank-two local homology inside a shellable flag homotopy sphere

## Finding

Let \(G=C_{16}(1,4,8)\) be the circulant graph on \(\mathbb Z/16\mathbb Z\), with two different vertices adjacent when their least cyclic distance belongs to \(\{1,4,8\}\). Set \(X=\operatorname{Ind}(G)\). The simplicial complex \(X\) is pure, three-dimensional, flag and shellable, with \(X\simeq S^3\). Nevertheless, it is **not an integral homology manifold**.

For every point \(x\in |X|\), the local integral homology satisfies

\[
H_j(|X|,|X|\setminus\{x\};\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\,m(x)},&j=3,\\
0,&j\ne 3,
\end{cases}
\]

where \(m(x)\in\{1,2\}\). The rank-two locus \(\Sigma=\{x:m(x)=2\}\) is precisely \(|T|\), where \(T\) is the subcomplex with the following 32 triangles as its facets:

\[
\{i,i+2,i+7\},\qquad \{i,i+5,i+7\},
\qquad i\in\mathbb Z/16\mathbb Z.
\]

The subcomplex \(T\) triangulates a **torus**, with face numbers \((f_0,f_1,f_2)=(16,48,32)\). Thus a shellable flag complex having the ordinary homotopy type of the three-sphere can have a two-dimensional embedded torus as its entire rank-two local-homology singular locus.

## Assumptions and scope

The abstract simplicial complex contains precisely those subsets of \(\mathbb Z/16\mathbb Z\) with no pair at cyclic distance \(1\), \(4\), or \(8\). Its geometric realization is denoted \(|X|\). All (co)homology groups, unless a coefficient field is displayed, have integral coefficients. At points in the relative interior of a simplex \(F\), local homology agrees with the shifted reduced homology of its link:

\[
H_j(|X|,|X|\setminus\{x\};\mathbb Z)
\cong\widetilde H_{j-|F|}(\operatorname{lk}_X F;\mathbb Z).
\]

Here the unique simplex corresponding to a point is nonempty, and for a facet the conventional complex consisting only of the empty face has \(\widetilde H_{-1}=\mathbb Z\). The top-dimensional local homology rank is constant along each open simplex; its support can therefore be specified simplicially.

## Proof

**1. Exact simplicial census and shelling.** Enumerate all independent subsets of the sixteen graph vertices. The cardinality distribution, including the empty face, is

\[
(f_{-1},f_0,f_1,f_2,f_3)=(1,16,80,144,80).
\]

Every maximal independent set has four vertices, hence \(X\) is pure of dimension three. The accompanying `verify_shelling.py` embeds an explicit ordered list of all 80 distinct four-vertex facets. It checks the following combinatorial shelling criterion for every \(1\le j<i\le80\): there are \(k<i\) and a vertex \(v\in F_i\setminus F_j\) such that \(F_i\setminus F_k=\{v\}\). All 3160 required ordered comparisons pass, establishing shellability independently of the published shellability assertion. Since a pure shellable complex is a wedge of top-dimensional spheres and

\[
\widetilde\chi(X)=-1+16-80+144-80=-1,
\]

there is precisely one sphere: \(X\simeq S^3\). All links of faces in a pure shellable simplicial complex are likewise pure shellable. Their reduced integral homology is therefore free and concentrated in their top degree (or zero there).

**2. Exact rank of every local link.** Reflection and cyclic translation preserve \(G\), giving a dihedral action on every face and its link. The 321 faces split into 17 orbits: one empty-face orbit, one vertex orbit, five edge orbits, six triangle orbits and four facet orbits. Representatives and orbit sizes are independently enumerated in `verify_singular_torus.py`. Exact reduced boundary ranks over the primes \(2\) and \(3\) give the same top Betti numbers in all 17 orbits. For the five edge orbits represented by \(\{0,d\}\) with \(d=2,3,5,6,7\), respectively, these ranks are \(2,1,2,1,2\). All vertex links have top rank \(2\). Of the six triangle orbits, only the 32-member orbit containing \(\{0,2,7\}\) has top rank \(2\); the other five have top rank \(1\). Each facet has link rank \(1\) in degree \(-1\). The empty-face link has top rank \(1\).

These modular computations give **integral**, not merely modular, ranks because the independently verified pure shelling makes every link a wedge of spheres and hence torsion-free. Thus for every nonempty simplex \(F\) the link is free of rank \(1\) or \(2\) in degree \(3-|F|\), with zero reduced homology in every other degree. The local-homology shift above proves the asserted complete pointwise local-homology formula.

**3. Identification and topology of the rank-two locus.** The triangle orbit of \(\{0,2,7\}\) consists of exactly the 32 triangles \(\{i,i+2,i+7\}\) and \(\{i,i+5,i+7\}\), with arithmetic modulo 16. Its edges are exactly the 48 edges having cyclic distance \(2\), \(5\) or \(7\). Its vertices are all sixteen vertices. The orbit computation in part 2 therefore shows that the rank-two locus is the realization of the downward closure \(T\) of these triangles; no other open simplices occur in it.

Each edge of \(T\) belongs to exactly two triangles. Each vertex belongs to six triangles, and its link within \(T\) is a **single connected six-cycle**. These two verified incidence properties make \(T\) a closed combinatorial surface. It is connected because edges of cyclic distance \(7\) alone connect all sixteen vertices, as \(\gcd(7,16)=1\).

More strongly, orient every triangle by the ordered triples \((i,i+2,i+7)\) and \((i,i+7,i+5)\). The integer simplicial boundary of the sum of these 32 oriented triangles is exactly zero, by cancellation on every one of the 48 edges; the accompanying checker verifies the oriented edge coefficients without reducing modulo a prime. Hence the closed connected surface \(T\) is orientable. Its Euler characteristic is

\[
\chi(T)=16-48+32=0.
\]

The classification of closed connected orientable surfaces now identifies \(|T|\cong S^1\times S^1\). The established pointwise rank classification proves that this torus is precisely \(\Sigma\).

## Verification

Run, using standard Python 3 and no third-party dependencies, `python3 verify_shelling.py` and `python3 verify_singular_torus.py`. Both programs reconstruct the graph directly. The first embeds and exhaustively validates an 80-facet shelling order and every face. The second reconstructs all 17 face orbits and their link homology, with exact matrix arithmetic over \(\mathbb F_2\) and \(\mathbb F_3\), and independently checks the surface-incidence, connectedness and integer-orientation certificates. The checkers are supplied as complete source files, not referenced to an external computation.

The finite enumeration is exhaustive because the graph has exactly sixteen vertices and each possible face has at most four vertices. The field calculations alone would not establish integral torsion-freeness; the verified pure shellability supplies the required mathematical theorem about links.

## Relationship to prior work

Earl, Vander Meulen and Van Tuyl [1, Theorem 6.1(iii) and its proof] identified \(C_{16}(1,4,8)\) as a shellable but not vertex-decomposable independence-complex example and printed a shelling order. The current finding does **not** claim priority for shellability, the graph, or its facet enumeration. Its new claim concerns local homology at every point and the unexpected topological type of the complete rank-two singular locus. Neither local rank classification nor a toroidal subcomplex identification is contained in the inspected theorem and proof.

Vander Meulen and Van Tuyl [2, Theorems 1.1 and 4.4] extend the shellable/nonvertex-decomposable phenomenon to graph expansions and lexicographic products. Those structural properties do not force the specific pointwise local-homology profile or the embedded torus exhibited here. Full-text comparisons and searches for alternate graph notation, links, local homology, singular loci and cyclic torus triangulations did not identify a stronger covering statement.

## Limitations

This theorem concerns the specified sixteen-vertex graph and its integral local homology. It does not determine homeomorphism type of the ambient three-dimensional complex, its PL singular neighborhoods, or analogous singular loci for other circulants and lexicographic products. An equivalent description in unindexed literature remains possible.

## References

[1] J. Earl, K. N. Vander Meulen, and A. Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837v1 (first public posting 2015-05-11), especially Theorem 6.1 and pp. 12–13; https://arxiv.org/pdf/1505.02837.

[2] K. N. Vander Meulen and A. Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, arXiv:1505.02838v1 (first public posting 2015-05-12), especially Theorems 1.1 and 4.4; https://arxiv.org/pdf/1505.02838.
