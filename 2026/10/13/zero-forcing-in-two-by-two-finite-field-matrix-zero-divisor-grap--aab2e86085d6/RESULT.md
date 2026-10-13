# Zero forcing in two-by-two finite-field matrix zero-divisor graphs

## Finding

Let \(q\) be a prime power, and let \(G_q\) be the underlying simple graph of the standard directed zero-divisor graph of \(M_2(\mathbb F_q)\): its vertices are the nonzero singular matrices, and distinct \(A,B\) are adjacent when \(AB=0\) or \(BA=0\). Put \(N=(q-1)(q+1)^2\). Then \[Z(G_q)=N-2q=q^3+q^2-3q-1.\] More structurally, if \(T_{I,K}\) denotes the \(q-1\) matrices with image line \(I\) and kernel line \(K\), then a set is zero forcing exactly when its white complement contains at most one matrix from every \(T_{I,K}\) and the corresponding bipartite image-kernel edge set can be completely eliminated by repeatedly choosing a source type \(T_{I,K}\) that contains a blue representative and deleting the unique white edge in image-row \(K\) union kernel-column \(I\). Consequently every such white type graph is a forest with at most \(2q\) edges, and this bound is sharp.

Thus a graph on
\[
N=(q-1)(q+1)^2
\]
vertices has a minimum zero forcing set of size
\[
(q-1)(q+1)^2-2q.
\]
The sharp obstruction is not merely a twin-class count: after passing to image-kernel types, zero forcing becomes a leaf-elimination process on a bipartite graph with two copies of the projective line.

## Assumptions and scope

Let \\(q\\) be a prime power and let
\[
R=M_2(\mathbb F_q).
\]
The directed zero-divisor graph of \\(R\\) has the nonzero zero-divisors as vertices and an arc \\(A\to B\\) when \\(AB=0\\). We use its underlying simple graph \\(G_q\\): distinct vertices \\(A,B\\) are adjacent exactly when
\[
AB=0\quad\text{or}\quad BA=0.
\]
Since a nonzero singular \\(2\times2\\) matrix has rank one, the vertices are precisely the rank-one endomorphisms of \\(\mathbb F_q^2\\).

For projective lines \\(I,K\in\mathbb P^1(\mathbb F_q)\\), define
\[
T_{I,K}=\{A:\operatorname{im}A=I,\ \ker A=K\}.
\]
There are \\(q+1\\) choices for each line.

## Proof

For fixed \\(I,K\\), a rank-one map with image \\(I\\) and kernel \\(K\\) is a nonzero map
\[
\mathbb F_q^2/K\longrightarrow I,
\]
between one-dimensional spaces. Hence
\[
|T_{I,K}|=q-1.
\tag{1}
\]
Therefore
\[
|V(G_q)|=(q+1)^2(q-1)=N.
\tag{2}
\]

If \\(A\in T_{I,K}\\) and \\(B\in T_{J,L}\\), then
\[
AB=0\iff J=K,
\qquad
BA=0\iff I=L.
\tag{3}
\]
Thus two distinct type classes are completely joined exactly when
\[
J=K\quad\text{or}\quad L=I.
\tag{4}
\]
Within \\(T_{I,K}\\), the class is a clique when \\(I=K\\) and an independent set when \\(I\ne K\\).

When \\(q\ge3\\), two white vertices in one type class can never be separated by a first force: off the diagonal they are false twins, and on the diagonal they are true twins. Thus a zero forcing complement contains at most one white vertex per type. For \\(q=2\\), every type class is already a singleton, so the same statement is automatic.

Assume now that at most one white vertex remains in every type. Encode the white types as edges of a bipartite graph \\(H_W\\). Its left vertices are a copy of \\(\mathbb P^1(\mathbb F_q)\\) indexing image lines, its right vertices are a second copy indexing kernel lines, and a white type \\(T_{J,L}\\) is the edge \\(J-L\\).

A blue vertex in type \\(T_{I,K}\\) is adjacent to exactly the white types lying in image-row \\(K\\) or kernel-column \\(I\\), by (4). Therefore it performs a force exactly when that row-column union contains one white edge. Equivalently, the white edge set can be reduced by repeatedly choosing a source type that currently contains a blue representative and deleting the unique white edge in its associated row-column union. For \\(q\\ge3\\), the blue-representative condition is automatic once there is at most one white matrix per type; for \\(q=2\\), it is an essential part of the rule. This proves the structural characterization in the finding.

Every such deletion removes a leaf edge of the current bipartite graph. Hence a completely reducible \\(H_W\\) cannot contain a cycle: after all pendant trees attached to a cycle are deleted, the cycle itself has no leaf edge. Therefore \\(H_W\\) is a forest on
\[
2(q+1)
\]
vertices, so initially
\[
|W|\le 2q+1.
\tag{5}
\]

Equality in (5) would make \\(H_W\\) a spanning tree. A spanning tree has no isolated row or column. If a row-column union contained exactly one edge, then both the chosen row and chosen column would have degree one and would meet in that edge; the edge would therefore be an isolated \\(K_2\\) component. This is impossible in a spanning tree on at least six vertices. Consequently a completely reducible white graph satisfies
\[
|W|\le2q.
\tag{6}
\]
Thus every zero forcing set has size at least
\[
N-2q.
\tag{7}
\]

To attain the bound, label the projective lines
\[
L_0,L_1,\ldots,L_q.
\]
Choose one white matrix from each type
\[
T_{L_0,L_k}\quad(0\le k\le q)
\]
and from each type
\[
T_{L_i,L_0}\quad(1\le i\le q-1).
\]
There are exactly
\[
(q+1)+(q-1)=2q
\]
white vertices.

At the type level, the following chronological sequence forces all of them:
\[
T_{L_1,L_q}\to T_{L_0,L_1},
\]
then
\[
T_{L_1,L_i}\to T_{L_i,L_0}
\qquad(1\le i\le q-1),
\]
then
\[
T_{L_0,L_1}\to T_{L_0,L_0},
\]
then
\[
T_{L_i,L_1}\to T_{L_0,L_i}
\qquad(2\le i\le q-1),
\]
and finally
\[
T_{L_0,L_0}\to T_{L_0,L_q}.
\]
For \\(q>2\\), every initially white type still contains a blue representative because its size is \\(q-1\\); for \\(q=2\\), the displayed source types are blue at the moment they are used. Hence the sequence is valid for every prime power \\(q\ge2\\).

Combining with (7) gives
\[
Z(G_q)=N-2q=q^3+q^2-3q-1.
\]

## Verification

The accompanying `verify.py` was inspected from its packaged path before replay.

It checks the displayed forcing sequence for every integer \\(2\le q\le9\\) in the abstract image-kernel graph and confirms the predicted value \\(N-2q\\). It exhaustively enumerates all white type profiles for \\(q=2\\) and \\(q=3\\), obtaining maximum reducible white sizes \\(4\\) and \\(6\\), respectively, and verifies that every reducible profile is acyclic.

As an independent algebra-to-graph check, it constructs every nonzero singular matrix over the prime fields \\(\mathbb F_2\\), \\(\mathbb F_3\\), and \\(\mathbb F_5\\), computes products directly, recovers image and kernel lines, and verifies every pairwise adjacency against (4). The resulting vertex counts are \\(9\\), \\(32\\), and \\(144\\).

For \\(q\ge3\\), the checker also verifies an auxiliary \\(K_{2q+1}\\)-minor certificate in the graph; this is not needed for the zero forcing lower bound.

Exact replay output:

```text
q=2: N=9, explicit forcing set size=5, omitted=4
q=3: N=32, explicit forcing set size=26, omitted=6
q=4: N=75, explicit forcing set size=67, omitted=8
q=5: N=144, explicit forcing set size=134, omitted=10
q=6: N=245, explicit forcing set size=233, omitted=12
q=7: N=384, explicit forcing set size=370, omitted=14
q=8: N=567, explicit forcing set size=551, omitted=16
q=9: N=800, explicit forcing set size=782, omitted=18
q=2: exhaustive type profiles max omitted=4, profile_count=108
q=3: exhaustive type profiles max omitted=6, profile_count=4752
F_2: direct M2 multiplication matches image-kernel graph on 9 vertices
F_3: direct M2 multiplication matches image-kernel graph on 32 vertices
F_5: direct M2 multiplication matches image-kernel graph on 144 vertices
q=3: explicit K_7 minor certificate OK
q=4: explicit K_9 minor certificate OK
q=5: explicit K_11 minor certificate OK
q=7: explicit K_15 minor certificate OK
q=9: explicit K_19 minor certificate OK
VERIFY_OK
```

The finite checks corroborate the arbitrary-prime-power proof. They do not replace the rank-one image-kernel argument or the forest obstruction.

## Relationship to prior work

Božić and Petrović study directed zero-divisor graphs of matrix rings over commutative rings and, in particular, establish connectivity and diameter results for matrix-ring zero-divisor graphs. The indexed record classifies the work under matrix rings, including MSC \\(16S50\\).

A later survey devoted to graphs from matrices lists \\(16S50\\) first in its 2020 Mathematics Subject Classification and reviews the matrix zero-divisor graph literature through properties such as connectivity, diameter, girth, Hamiltonicity, Eulerian behavior, and domination. Searches of the accessible article text found no occurrence of “zero forcing” or “pathwidth.”

Earlier work on the same underlying graph \\(G_q\\) determines its ordinary domination number by the image-kernel decomposition. That statement neither bounds the size of a zero forcing complement nor yields the bipartite forest obstruction proved here.

General zero forcing theory supplies the color-change rule and its relationship to matrix nullity; no general theorem located in the checked sources gives the formula above for this matrix-ring graph.

## Limitations

The theorem is for \\(2\times2\\) full matrix rings over finite fields and for the underlying simple graph of the standard directed zero-divisor graph.

It does not determine the full zero forcing polynomial or count all minimum zero forcing sets. The elimination criterion characterizes them structurally but is not converted here into a closed enumeration formula.

No equality with real maximum nullity or minimum rank is claimed.

## References

1. I. Božić and Z. Petrović, “Zero-Divisor Graphs of Matrices Over Commutative Rings,” *Communications in Algebra* 37 (2009), 1186–1192. DOI: 10.1080/00927870802465951.
2. “Graphs from matrices - a survey,” *AKCE International Journal of Graphs and Combinatorics* (2024). DOI: 10.1080/09728600.2024.2332780.
3. A. Mahmoodi, “Nilpotent Graphs of Matrix Algebras,” *Algebraic Structures and Their Applications* 1 (2014), 123–132. Primary MSC \\(16S50\\).
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
