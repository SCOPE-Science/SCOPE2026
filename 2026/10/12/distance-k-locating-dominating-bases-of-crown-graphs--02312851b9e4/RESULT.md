# Distance-\(k\) locating-dominating bases of crown graphs
## Finding
For every integer \(n\ge5\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},
\qquad
B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching consists of the nonedges
\[
a_i b_i,
\qquad 1\le i\le n.
\]
Write \(P_i=\{a_i,b_i\}\). For every integer \(k\ge1\),
\[
\gamma_L^k(\operatorname{Cr}_n)=n-1.
\]

For \(k\ge2\), the minimum distance-\(k\) locating-dominating sets are exactly the sets that omit one matched pair \(P_j\) and choose exactly one vertex from every other \(P_i\). Hence there are
\[
n2^{n-1}
\]
minimum sets.

For \(k=1\), a minimum set has the same transversal form, but it is locating-dominating exactly when it contains at least two vertices from \(A\) and at least two vertices from \(B\). Hence there are
\[
n\bigl(2^{n-1}-2n\bigr)
\]
minimum sets.

Thus the minimum cardinality is independent of the sensor range \(k\), while the family of minimum configurations has a sharp transition between \(k=1\) and \(k\ge2\).

## Assumptions and scope
All graphs are finite, simple, and connected. For a positive integer \(k\), define
\[
d_k(x,y)=\min\{d(x,y),k+1\}.
\]
A set \(S\subseteq V(G)\) is distance-\(k\) resolving when the vectors
\[
\bigl(d_k(v,s):s\in S\bigr)
\]
are distinct for all vertices \(v\). It is distance-\(k\) dominating when every vertex outside \(S\) is at ordinary graph distance at most \(k\) from \(S\). A distance-\(k\) locating-dominating set satisfies both conditions.

In \(\operatorname{Cr}_n\), vertices \(a_i\) and \(b_j\) are adjacent exactly when \(i\ne j\). For \(n\ge3\), the graph has diameter \(3\):
\[
d(a_i,a_j)=d(b_i,b_j)=2
\]
for distinct same-side vertices,
\[
d(a_i,b_j)=1
\]
when \(i\ne j\), and
\[
d(a_i,b_i)=3.
\]

## Proof
Fix distinct indices \(i,j\). For every \(k\ge1\), the only vertices that distinguish the same-side pair \(a_i,a_j\) under \(d_k\) are the four vertices in
\[
P_i\cup P_j.
\]
A vertex outside these two matched pairs has equal distance to \(a_i\) and \(a_j\), while every vertex in \(P_i\cup P_j\) distinguishes them. The same holds for \(b_i,b_j\).

Therefore a distance-\(k\) resolving set \(S\) must meet \(P_i\cup P_j\) for every \(i\ne j\). Hence at most one matched pair can be disjoint from \(S\), and
\[
|S|\ge n-1.
\]
If equality holds, exactly one pair \(P_j\) is omitted and \(S\) contains exactly one endpoint of every other pair.

Conversely, assume \(n\ge4\) and \(S\) has this transversal form. Two same-side vertices are distinguished by the selected vertex in at least one of their matched pairs. A matched pair \(a_i,b_i\) is distinguished by the selected vertex in \(P_i\), when \(i\ne j\), or by any selected vertex from another pair when \(i=j\). If \(a_i,b_\ell\) are adjacent with \(i\ne\ell\), choose an index \(h\notin\{i,\ell\}\) whose pair is not omitted. Such \(h\) exists because \(n\ge4\). The selected vertex from \(P_h\) has truncated distances \(2\) and \(1\), in some order, to \(a_i\) and \(b_\ell\). Thus every pair is resolved.

If \(k\ge2\), every minimum resolving transversal is already distance-\(k\) dominating because every omitted vertex is within distance at most \(2\) of some selected vertex. Hence
\[
\gamma_L^k(\operatorname{Cr}_n)=n-1
\]
for \(k\ge2\), with
\[
n2^{n-1}
\]
minimum sets.

For \(k=1\), fix a minimum resolving transversal with omitted pair \(P_j\), and put
\[
p=|S\cap A|,
\qquad
q=|S\cap B|,
\]
so \(p+q=n-1\). The omitted vertices \(a_j,b_j\) require \(q\ge1\) and \(p\ge1\), respectively. If \(a_i\in S\), then its unselected mate \(b_i\) has a selected neighbor exactly when there is another selected \(A\)-vertex, so all such mates require \(p\ge2\). Symmetrically, all mates of selected \(B\)-vertices require \(q\ge2\). Hence the transversal is distance-\(1\) dominating exactly when
\[
p\ge2
\qquad\text{and}\qquad
q\ge2.
\]

For \(n\ge5\), the number of valid orientations for a fixed omitted pair is
\[
\sum_{p=2}^{n-3}\binom{n-1}{p}
=
2^{n-1}-2n.
\]
Multiplying by the \(n\) choices of omitted pair gives
\[
n\bigl(2^{n-1}-2n\bigr).
\]
This proves the theorem.

## Verification
The included checker constructs \(\operatorname{Cr}_n\), computes all-pairs distances by breadth-first search, evaluates distance-\(k\) metric codes, and tests distance-\(k\) domination directly. For every \(5\le n\le8\) and \(k\in\{1,2,3\}\), it rejects every set smaller than \(n-1\), enumerates every candidate of size \(n-1\), and compares the complete minimum family with the theorem.

## Relationship to prior work
Distance-\(k\) location-domination was introduced in 2021 as the simultaneous requirement of distance-\(k\) domination and distance-\(k\) resolution. The foundational paper proves general bounds, extremal characterizations, and exact results for several standard classes. Its accessible full text contains no occurrence of “crown” and no specialization to \(K_{n,n}\) with a deleted perfect matching.

The same paper proves
\[
0\le \gamma_L^k(G)-\dim_k(G)\le1.
\]
The present crown result determines the lower endpoint and, more strongly, classifies and counts every minimum set.

The companion distance-\(k\) dimension literature identifies \(k=1\) with adjacency dimension and proves general monotonicity and diameter facts. Those results do not determine the crown bases or the one-step domination filter.

Targeted searches under crown graph, \(K_{n,n}\) minus a perfect matching, bipartite double cover of \(K_n\), bipartite Kneser graph, adjacency dimension, and locating-dominating terminology did not locate the minimum-set classification or basis counts proved here.

## Limitations
The theorem is stated for \(n\ge5\). The small crowns \(n=3,4\) have exceptional distance-\(1\) behavior because a size-\(n-1\) transversal cannot contain two selected vertices in each bipartition class.

No claim is made for identifying codes, locating-total domination, or other stronger code variants. The exhaustive computation is corroborative only; the all-parameter conclusion follows from the proof.

## References
1. C. X. Kang, E. Yi, “Distance-\(k\) locating-dominating sets in graphs,” arXiv:2106.14848v1, 28 June 2021; Bulletin of the Institute of Combinatorics and its Applications 95 (2022), 38–56.
2. J. Geneson, E. Yi, “The distance-\(k\) dimension of graphs,” arXiv:2106.08303v1, 15 June 2021.
3. P. J. Slater, “Dominating and reference sets in a graph,” Journal of Mathematical and Physical Sciences 22 (1988), 445–455.
