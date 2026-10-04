# Two-distance \(7\)-simplices satisfy the precise center conjecture
## Finding
Let \(S\) be a nondegenerate Euclidean \(7\)-simplex. Assume that its edges have at most two distinct lengths, that \(S\) is vertex-uniform, and that its incenter equals its centroid. Then \(S\) is equifacetal.

Here vertex-uniform means that the multiset of lengths of the seven edges incident with a vertex is independent of the vertex. Equifacetal means that all eight facets, each of dimension \(6\), are mutually congruent. The theorem therefore verifies Edmonds' precise center conjecture in the first unresolved dimension on the entire two-distance subclass.

## Assumptions and scope
The simplex is Euclidean and nondegenerate. There are eight vertices. If only one edge length occurs, the simplex is regular and the conclusion is immediate, so the proof below concerns exactly two edge lengths. Let their squared lengths be \(a^2\) and \(b^2\), normalize \(b^2=1\), and put \(t=a^2/b^2>0\). Because the lengths are distinct, \(t\ne1\).

Color an edge when its squared length is \(t\), and let \(G\) be the resulting simple graph on the eight vertices. Vertex-uniformity says exactly that \(G\) is regular. Interchanging the two edge lengths replaces \(G\) by its complement, so one may assume that its degree \(k\) satisfies \(0\le k\le3\).

For vertex-uniform simplices, Edmonds proves that the centroid is the circumcenter and that equality of incenter and centroid is equivalent to equiareality, meaning equality of all facet volumes. He also proves that vertex-transitivity of the edge-labeled simplex is equivalent to equifacetality. Thus it suffices to prove: every nondegenerate equiareal two-distance vertex-uniform \(7\)-simplex has a vertex-transitive edge coloring.

## Proof
For \(k=0\) or \(k=1\), the color graph is respectively empty or a perfect matching, hence vertex-transitive. For \(k=2\), a regular graph is a disjoint union of cycles. On eight vertices the three types are \(C_8\), \(C_3\cup C_5\), and \(C_4\cup C_4\); only \(C_3\cup C_5\) is not vertex-transitive. For \(k=3\), there are six isomorphism classes of cubic graphs on eight vertices, of which exactly three are not vertex-transitive. The bundled verifier exhaustively certifies both finite classifications by enumerating every labeled regular graph and every relabeling orbit.

It remains to exclude the four non-vertex-transitive types under equiareality and nondegeneracy. For a vertex \(v\), let \(F_v(t)\) be the Cayley--Menger determinant of the six-dimensional facet opposite \(v\). A fixed nonzero dimensional constant relates \(F_v(t)\) to the square of that facet's volume, so equiareality is equivalent to equality of the eight determinants; nondegeneracy requires every \(F_v(t)\ne0\).

For the degree-two type \(C_3\cup C_5\), the two vertex classes have
\[
F_A(t)=t(9t-16)(t^2-3t+1)^2,
\]
\[
F_B(t)=-t^2(t^2-3t+1)(7t^2-5t-9),
\]
and therefore
\[
F_A(t)-F_B(t)=16t(t-1)^3(t^2-3t+1).
\]
Because \(t>0\) and \(t\ne1\), equality of the facet determinants forces \(t^2-3t+1=0\). But then both displayed determinants vanish, contradicting nondegeneracy.

For the first non-vertex-transitive cubic type, the two facet classes have
\[
F_A(t)=-t^3(t-2)(23t^2-50t+20),
\]
\[
F_B(t)=-t^3(7t^3-48t^2+72t-24),
\]
with
\[
F_A(t)-F_B(t)=-16t^3(t-1)^3.
\]
Equiareality therefore forces \(t=1\), impossible for two distinct edge lengths.

For the second non-vertex-transitive cubic type, it is enough to compare two of its three facet classes:
\[
F_A(t)=t(t-2)(t^4-34t^3+88t^2-60t+12),
\]
\[
F_B(t)=t(t^2-4t+2)(t^3-16t^2+26t-4),
\]
for which
\[
F_A(t)-F_B(t)=-16t(t-1)^4.
\]
Again equiareality forces \(t=1\), a contradiction.

For the third non-vertex-transitive cubic type, two facet classes have
\[
F_A(t)=-(t^2-3t+1)(4t^3+7t^2-37t+19),
\]
\[
F_B(t)=-(t^2-3t+1)(20t^3-41t^2+11t+3),
\]
so
\[
F_A(t)-F_B(t)=16(t-1)^3(t^2-3t+1).
\]
With \(t\ne1\), equiareality again forces \(t^2-3t+1=0\). Every facet determinant in this graph type contains that factor, so the simplex is degenerate, again impossible.

Hence every nondegenerate equiareal two-distance vertex-uniform \(7\)-simplex is vertex-transitive. Edmonds' characterization of equifacetal simplices by vertex-transitivity yields the conclusion.

## Verification
The standalone file `verify.py` uses only the Python standard library. It performs two exact checks.

First, it enumerates all labeled regular graphs on eight vertices. It certifies that the degree-two family consists of exactly \(3507\) labeled graphs in three relabeling orbits of sizes \(2520,672,315\), with only the \(672\)-element orbit non-vertex-transitive. It likewise certifies that the cubic family consists of exactly \(19355\) labeled graphs in six relabeling orbits of sizes \(35,2520,10080,3360,840,2520\), of which exactly three are non-vertex-transitive.

Second, it computes the Cayley--Menger determinants by fraction-free Bareiss elimination in exact integer arithmetic. Each six-dimensional facet determinant is a polynomial in \(t\) of degree at most \(6\): after the first row and column of the Cayley--Menger matrix contribute their required unit entries, a determinant monomial contains at most six squared-distance entries. Consequently, agreement at seven distinct integer values of \(t\) proves each displayed polynomial identity exactly. The verifier checks all facet classes and all four determinant-difference factorizations and prints `VERIFY_OK`.

These finite computations certify the exhaustive graph case split and polynomial identities. The quantified conclusion for every real \(t>0\) follows from the displayed algebraic factorizations and the nondegeneracy condition, not from numerical sampling.

## Relationship to prior work
Edmonds' 2009 paper formulates three versions of the center conjecture for equifacetal simplices. Its precise version states that a vertex-uniform simplex whose incenter and centroid coincide should be equifacetal. The paper proves the strong version through dimension \(6\) and leaves higher dimensions open; it also supplies the two structural equivalences used here: vertex-transitivity characterizes equifacetality, and for a vertex-uniform simplex coincidence of centroid and incenter is equivalent to equiareality.

Prieto-Martínez's 2023 paper proves an analogue for a different, non-continuous notion of center and explicitly records that both the original continuous-center conjecture and the strong conjecture remain open. That result does not imply the present two-distance dimension-\(7\) theorem.

The present theorem is a restricted advance rather than a solution of the full conjecture: it closes all possibilities with at most two edge lengths in dimension \(7\), using the natural regular-graph encoding of a two-distance vertex-uniform simplex.

## Limitations
No claim is made for vertex-uniform \(7\)-simplices with three or more edge lengths, for arbitrary \(7\)-simplices without vertex-uniformity, or for dimensions above \(7\). No claim is made about Edmonds' all-centers version. The literature comparison did not identify an earlier statement equivalent to this two-distance theorem, but absence from the inspected sources and searches is not a proof that no obscure or unindexed special-case treatment exists.

## References
1. Allan L. Edmonds, “The center conjecture for equifacetal simplices,” *Advances in Geometry* 9 (2009), 563–576, DOI 10.1515/ADVGEOM.2009.027. Earliest verified public issue date used here: 2009-07-06.
2. Luis Felipe Prieto-Martínez, “The concept of center as an equivariant map and a proof of an analogue of the center conjecture for equifacetal simplices,” arXiv:2301.09945 (2023).
