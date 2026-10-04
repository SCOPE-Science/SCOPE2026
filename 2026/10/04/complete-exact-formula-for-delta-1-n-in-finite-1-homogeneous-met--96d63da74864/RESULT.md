# Complete exact formula for \(\Delta_1(n)\)

## Finding
Let \(\Delta_1(n)\) be the largest possible number of distinct distance values, including \(0\), in a finite \(1\)-homogeneous metric space with \(n\) points. For even \(n\), write \(n_2\) for the largest power of \(2\) dividing \(n\). Then

\[
\Delta_1(n)=
\begin{cases}
(n+1)/2, & n \text{ odd},\\
(3n+n_2)/4, & n \text{ even}.
\end{cases}
\]

The odd case is already established by Bargetz, Bartoš, Kubiś and Luggin. The new part is the even formula, which proves that their lower bound is always sharp and settles the remaining cases in their Question 1.

## Assumptions and scope
A metric space is \(1\)-homogeneous when its isometry group is transitive on points. The distance count includes \(0\), as in the definition \(\delta(X)=|\operatorname{Dist}(X)|\) used by Bargetz et al. A positive distance is singleton when from every point there is exactly one point at that distance. For a vertex-transitive edge-coloring, the valency of a color is the number of incident edges of that color at each vertex.

## Proof
Let \(X\) be an even \(n\)-point \(1\)-homogeneous metric space. Regard each positive distance as an edge color on the complete graph \(K_n\). Bargetz et al. explicitly note that \(1\)-homogeneity is exactly vertex-transitivity of this colored complete graph. Hence the numbers of neighbors of each positive distance form the partition associated with a vertex-transitive edge-coloring in the sense of Edmonds.

Every positive singleton distance has color valency \(1\), hence contributes an odd part to that partition. Edmonds' Theorem 1.4 says that for a vertex-transitive coloring on even \(n\) vertices, the number of odd parts is at most \(\iota(n)\), the maximum possible number of involutions in a group of order \(n\). His Theorem 1.2 gives

\[
\iota(n)=\frac n2+\frac{n_2}2-1.
\]

If \(S_X\) is the set of singleton distances including \(0\), then the preceding paragraph yields

\[
|S_X|-1\le \iota(n),
\qquad
|S_X|\le \frac n2+\frac{n_2}2.
\]

Observation 6.2 of Bargetz et al. gives \(\delta(X)\le (|S_X|+n)/2\). Therefore

\[
\delta(X)\le
\frac12\left(n+\frac n2+\frac{n_2}2\right)
=\frac{3n+n_2}4.
\]

It remains to match the upper bound. Write \(n=2^a(2k+1)\) with \(a\ge1\). Example 6.10 of Bargetz et al., applied with their parameter \(m=a-1\), gives a \(1\)-homogeneous space with

\[
2^{a-1}(3k+2)
=\frac{3\cdot 2^a(2k+1)+2^a}4
=\frac{3n+n_2}4
\]

distances. Thus equality holds for every even \(n\). For odd \(n\), Proposition 6.7 and the matching construction in the same paper give \(\Delta_1(n)=(n+1)/2\).

## Verification
The proof was checked against the full text of both source papers. In Edmonds, Theorem 1.2 gives the exact involution maximum and Theorem 1.4 applies that maximum to the odd valencies of every vertex-transitive complete-graph coloring. In Bargetz et al., Observation 6.2 converts the number of singleton distances into a distance-count upper bound, Example 6.10 supplies the matching lower construction, and Remark 6.14 identifies the metric problem with vertex-transitive complete-graph colorings. The bundled arithmetic checker verifies the parameter conversion and the closed formula for a finite range of \(n\); it is a sanity check, not a substitute for the proof.

## Relationship to prior work
Bargetz et al. obtained the exact odd and power-of-two cases, proved the even lower bound used above, and asked for the remaining exact values. Their Proposition 6.11 handled \(n=2q\) when the odd factor \(q\) is prime. A previous calculation also removes that primality restriction for \(n=2q\). The present argument is strictly broader: Edmonds' older bound on odd valencies applies for every even \(n\), including all higher \(2\)-adic valuations, and closes the full question.

Edmonds' 2009 paper proves the relevant finite-group and vertex-transitive-coloring bounds but does not formulate the metric invariant \(\Delta_1\). Conversely, the 2024 metric-space paper formulates the invariant and the open question but does not cite or use Edmonds' partition theorem. The result here is the cross-application of those two ingredients.

## Limitations
The result concerns finite \(1\)-homogeneous metric spaces and the number of distinct attained distances. It does not classify all extremal spaces. The proof relies on Edmonds' published theorem on the maximum number of involutions and odd valencies rather than reproducing its finite-group proof. A targeted literature and database search found no prior statement of the closed formula above, but an unindexed independent observation remains possible because the argument is short once the two literatures are connected.

## References
1. C. Bargetz, A. Bartoš, W. Kubiś, F. Luggin, “Homogeneous isosceles-free spaces,” arXiv:2305.03163; Rev. Real Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. 118 (2024), Paper 118, DOI 10.1007/s13398-024-01587-y.
2. A. L. Edmonds, “The Partition Problem for Equifacetal Simplices,” Beiträge zur Algebra und Geometrie 50 (2009), 195–213.
