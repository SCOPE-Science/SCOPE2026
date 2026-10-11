# The second all-distinct nongeneric four-length Tonnetz has \(S^1\times S^2\) homology and singular vertex links

## Finding
Let \(L=(1,2,3,5)\) and \(n=11\). For the generalized Tonnetz
\[
T=\mathrm{Tonn}^{11,4}(1,2,3,5),
\]
the face vector is \((11,55,110,66)\), and
\[
H_i(T;\mathbb Z)\cong \mathbb Z\quad\text{for }i=0,1,2,3,
\]
with \(H_i(T;\mathbb Z)=0\) for \(i>3\). Every vertex link is homotopy equivalent to \(\bigvee^3 S^2\). Hence \(T\) is not a combinatorial \(3\)-manifold, although its integral homology groups agree with those of \(S^1\times S^2\).

## Assumptions and scope
The complex is the one from Definition 1.3 of Jevtić--Živaljević: for \(x\in\mathbb Z_{11}\) and \(\sigma\in S_4\), a maximal simplex is
\[
\{x,\ x+l_{\sigma(1)},\ x+l_{\sigma(1)}+l_{\sigma(2)},\ x+l_{\sigma(1)}+l_{\sigma(2)}+l_{\sigma(3)}\}\pmod{11},
\]
where the four lengths are \(1,2,3,5\). The vector is reduced because its greatest common divisor is \(1\), but it is nongeneric because the distinct subsets \(\{1,2\}\) and \(\{3\}\) have equal sum.

Among four distinct positive integers, total length \(10\) forces \(\{1,2,3,4\}\), while total length \(11\) forces \(\{1,2,3,5\}\). Thus this is the next all-distinct total-length case after the previously recorded total-length \(10\) nongeneric example. No assertion is made for other nongeneric length vectors.

## Proof
Enumerating the maximal simplices directly from the definition gives exactly \(66\) tetrahedra and face vector \((11,55,110,66)\). With the increasing vertex order on every simplex, the integral simplicial boundary matrices \(\partial_1,\partial_2,\partial_3\) have sizes \(11\times55\), \(55\times110\), and \(110\times66\), respectively. Exact rational elimination gives ranks
\[
\operatorname{rank}\partial_1=10,\qquad
\operatorname{rank}\partial_2=44,\qquad
\operatorname{rank}\partial_3=65.
\]
The verifier also checks explicit maximal-rank minors with determinants \(1,-1,1\), respectively. Hence each corresponding cokernel is torsion-free. Since \(H_{d-1}=\ker(\partial_{d-1})/\operatorname{im}(\partial_d)\) embeds in \(C_{d-1}/\operatorname{im}(\partial_d)\), the homology is torsion-free. The rank formula then gives one copy of \(\mathbb Z\) in each degree \(0,1,2,3\).

For the link of vertex \(0\), the face vector is \((10,30,24)\). A staged vertex matching in the order \(9,10,6,5,3,2,4,7,8,1\) pairs \(30\) face incidences and leaves exactly one critical \(0\)-simplex and three critical \(2\)-simplices, with no critical \(1\)-simplices. The verifier constructs the entire directed Hasse graph after reversing matched covers and checks it is acyclic. Forman's theorem therefore gives
\[
\operatorname{Link}_T(0)\simeq\bigvee^3 S^2.
\]
Translation by any element of \(\mathbb Z_{11}\) preserves the defining facets and acts transitively on vertices, so every vertex link has the same homotopy type. In particular no vertex link is a \(2\)-sphere, so \(T\) is not a combinatorial \(3\)-manifold.

## Verification
Running `python3 verifier.py` reconstructs the complex from \(n=11\) and \(L=(1,2,3,5)\), checks \(\partial^2=0\), recomputes the exact rational boundary ranks, verifies the three determinant certificates, and independently repeats the boundary ranks modulo \(2,3,5,7,11,13\). It then reconstructs the vertex link, verifies the complete discrete-Morse matching and its acyclicity, and checks vertex-transitivity under cyclic translation.

The critical chain evidence is therefore finite and exhaustive for this specified complex. No inference from sampled simplices or from a timeout is used.

## Relationship to prior work
Jevtić--Živaljević define \(\mathrm{Tonn}^{n,k}(L)\) and prove that a reduced **generic** length vector produces a triangulated \((k-1)\)-torus. Their hypothesis does not apply here because \(1+2=3\). The same paper does not supply a classification of nongeneric four-length cases.

The closest checked database record is `2026/10/4/SCOPE-the-smallest-all-distinct-nongeneric-four-length-tonnetz-is-bigv--986e00d6ca75`, which treats the preceding all-distinct nongeneric vector \(\mathrm{Tonn}^{10,4}(1,2,3,4)\) and obtains a different mixed-dimensional sphere wedge. That result neither contains nor implies the present total-length \(11\) calculation. Catanzaro's earlier generalized-Tonnetz classification concerns triadic, two-dimensional constructions rather than this four-length complex. Related Fourier-phase-space Tonnetz work uses a different construction and is not used as a non-coverage argument.

## Limitations
The result determines the integral homology groups of the whole complex and the homotopy type of every vertex link. It does **not** determine the homotopy type, fundamental group, cohomology ring, or simple-homotopy type of the whole complex, and it does not classify all nongeneric length vectors. The literature search cannot exclude an unindexed or inaccessible duplicate. Independent audit has not been performed.

## References
1. F. D. Jevtić and R. T. Živaljević, *Generalized Tonnetz and discrete Abel-Jacobi map*, arXiv:2002.09184v1, first public 2020-02-21; Topological Methods in Nonlinear Analysis 57 (2021), DOI: 10.12775/TMNA.2020.049. The published article lists 2020 MSC Primary 57Q15 and 52B20.
2. M. J. Catanzaro, *Generalized Tonnetze*, arXiv:1612.03519; Journal of Mathematics and Music 5 (2011), 117--139.
3. J. Yust, *Generalized Tonnetze and Zeitnetze, and the topology of music concepts*, Journal of Mathematics and Music 14 (2020), 170--203, DOI: 10.1080/17459737.2020.1725667.
