# Distance-edge-monitoring sets of crown graphs
## Finding
For every integer \(n\ge4\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},
\qquad
B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching.

Every vertex of \(\operatorname{Cr}_n\) monitors exactly its incident edges. Hence a vertex set is distance-edge-monitoring if and only if it is a vertex cover.

Consequently,
\[
\operatorname{dem}(\operatorname{Cr}_n)=n,
\]
and the only minimum distance-edge-monitoring sets are the two bipartition classes \(A\) and \(B\).

Define
\[
\mathcal D_n(z)
=
\sum_{\substack{S\subseteq V(\operatorname{Cr}_n)\\S\text{ distance-edge-monitoring}}}
z^{|S|}.
\]
Then
\[
\mathcal D_n(z)
=
2z^n(1+z)^n-z^{2n}+nz^{2n-2}.
\]

The threshold \(n\ge4\) is sharp. Since \(\operatorname{Cr}_3\cong C_6\), one has
\[
\operatorname{dem}(\operatorname{Cr}_3)=2,
\]
so the incident-edge-only property fails at \(n=3\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected.

For a vertex \(x\) and edge \(e\), say that \(x\) monitors \(e\) if there is a vertex \(y\) such that deleting \(e\) increases the distance from \(x\) to \(y\). Equivalently, \(e\) lies on every shortest \(x,y\)-path. A set is distance-edge-monitoring when every edge is monitored by at least one selected vertex.

The result concerns crown graphs with \(n\ge4\). The six-cycle boundary \(n=3\) is explicitly excluded from the main equivalence and treated separately.

## Proof
Fix \(n\ge4\). Every vertex monitors each incident edge: if \(e=xy\), then deleting \(e\) changes the distance from \(x\) to \(y\), which is initially \(1\).

We prove that no vertex monitors a nonincident edge. By symmetry it suffices to take the probe
\[
x=a_p
\]
and a nonincident edge
\[
e=a_r b_s,
\qquad r\ne p.
\]
We show that, for every target vertex \(y\), there remains a shortest \(x,y\)-path avoiding \(e\).

If \(y=b_j\) with \(j\ne p\), then \(x b_j\) is an edge. Since \(e\) is not incident with \(x\), this one-edge geodesic survives.

If \(y=a_q\) with \(q\ne p\), then
\[
d(x,y)=2.
\]
The common neighbors of \(a_p\) and \(a_q\) are precisely
\[
\{b_k:k\notin\{p,q\}\}.
\]
There are \(n-2\ge2\) such vertices. The deleted edge \(e\) can destroy at most one of the corresponding two-edge paths
\[
a_p-b_k-a_q,
\]
because it cannot be the first edge and can equal the second edge for at most one value of \(k\). Thus a length-two geodesic survives.

The remaining target is \(y=b_p\). Here
\[
d(a_p,b_p)=3.
\]
Every ordered pair of distinct indices \(i,j\in[n]\setminus\{p\}\) gives a length-three path
\[
a_p-b_j-a_i-b_p.
\tag{1}
\]
If \(s\ne p\), the edge \(e=a_r b_s\) can occur in (1) only as the middle edge, and only for the single ordered pair
\[
(j,i)=(s,r).
\]
Since \((n-1)(n-2)\ge6\), another length-three path survives.

If \(s=p\), then \(e=a_r b_p\) can occur only as the last edge in paths with \(i=r\). Choose any
\[
i\in[n]\setminus\{p,r\}
\]
and then choose
\[
j\in[n]\setminus\{p,i\}.
\]
Such choices exist because \(n\ge4\), and the resulting path (1) avoids \(e\).

Therefore deleting any nonincident edge leaves every distance from \(a_p\) unchanged. By symmetry, the same holds for probes in \(B\). Hence every probe monitors exactly its incident edges.

It follows immediately that a set monitors all edges exactly when it contains an endpoint of every edge, that is, exactly when it is a vertex cover.

To count these sets, take complements. An independent set in \(\operatorname{Cr}_n\) is either an arbitrary subset of \(A\), an arbitrary subset of \(B\), or one of the \(n\) deleted matched pairs
\[
\{a_i,b_i\}.
\]
Thus its independence polynomial is
\[
I_n(z)=2(1+z)^n-1+nz^2.
\]
Complementation converts independent sets of size \(k\) into vertex covers of size \(2n-k\), so
\[
\mathcal D_n(z)
=z^{2n}I_n(z^{-1})
=2z^n(1+z)^n-z^{2n}+nz^{2n-2}.
\]
The maximum independent sets have size \(n\) and are exactly \(A\) and \(B\), proving
\[
\operatorname{dem}(\operatorname{Cr}_n)=n
\]
and the two-basis statement.

For \(n=3\), direct evaluation gives \(\operatorname{Cr}_3\cong C_6\) and distance-edge-monitoring number \(2\), so the threshold cannot be lowered.

## Verification
The included verifier constructs \(\operatorname{Cr}_n\) directly. For every edge \(e\) and every probe \(x\), it recomputes all distances after deleting \(e\) and thereby determines the monitored-edge set from the definition.

For each
\[
4\le n\le7,
\]
it confirms that every edge is monitored exactly by its two endpoints, exhaustively enumerates every vertex subset, checks that the distance-edge-monitoring sets are exactly the vertex covers, and compares every coefficient with the stated polynomial. It also checks the exceptional graph \(\operatorname{Cr}_3\).

## Relationship to prior work
Distance-edge monitoring was introduced in the CALDAM 2020 proceedings. The expanded journal version proves that every vertex cover is distance-edge-monitoring and records a sufficient condition for the converse: when every probe monitors exactly its incident edges, the distance-edge-monitoring sets are precisely the vertex covers. Complete bipartite graphs and hypercubes are given there as examples.

The crown graph is obtained from \(K_{n,n}\) by deleting a perfect matching. The theorem above shows that, for every \(n\ge4\), this deletion preserves the incident-edge-only monitoring property and hence preserves the minimum value
\[
\operatorname{dem}=n.
\]
It also determines every monitoring set. Relative to \(K_{n,n}\), the deleted matching creates exactly \(n\) additional vertex covers whose complements are the deleted matched pairs, which accounts for the term
\[
nz^{2n-2}.
\]

Later work develops general bounds, small-value characterizations, graph-product formulas, girth bounds, and perturbation results for the same invariant. Targeted searches using the standard crown name, the description \(K_{n,n}\) minus a perfect matching, and distance-edge-monitoring terminology did not locate the all-set crown theorem or its polynomial.

## Limitations
The theorem does not classify distance-edge-monitoring sets for arbitrary matching-deleted complete bipartite graphs with unequal sides or with a nonperfect deleted matching.

The threshold \(n\ge4\) is essential: \(\operatorname{Cr}_3\cong C_6\) behaves differently.

The exhaustive computation is corroborative only. The arbitrary-parameter claim is proved by the surviving-geodesic argument above.

A differently phrased or non-indexed treatment of the same crown family may exist despite the targeted searches.

## References
1. F. Foucaud, R. Klasing, M. Miller, J. Ryan, “Monitoring the Edges of a Graph Using Distances,” Algorithms and Discrete Applied Mathematics, CALDAM 2020, Lecture Notes in Computer Science 12016, 28–40, DOI 10.1007/978-3-030-39219-2_3.
2. F. Foucaud, S.-S. Kao, R. Klasing, M. Miller, J. Ryan, “Monitoring the edges of a graph using distances,” Discrete Applied Mathematics 319 (2022), 424–438, DOI 10.1016/j.dam.2021.07.002.
3. C. Yang, R. Klasing, Y. Mao, X. Deng, “On the distance-edge-monitoring numbers of graphs,” Discrete Applied Mathematics 342 (2024), 153–167, DOI 10.1016/j.dam.2023.09.012.
4. C. Yang, R. Klasing, C. He, Y. Mao, “Perturbation Results for Distance-edge-monitoring Numbers,” Fundamenta Informaticae 191 (2024), DOI 10.3233/FI-242176.
