# Outer multiset bases of square-page book graphs
## Finding
For every integer \(r\ge3\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing a common edge \(xy\), with page \(i\) equal to \(x a_i b_i y x\). Then
\[
\operatorname{odim}(B_r)=2r-3=|V(B_r)|-5.
\]

Every outer multiset basis has a five-vertex complement. One complement type, valid for every \(r\ge3\), consists of both spine vertices, one complete internal page pair, and one internal vertex from a different page. A second type, valid exactly for \(r\ge4\), consists of exactly one spine vertex, one complete internal page pair, one \(a\)-vertex from a second page, and one \(b\)-vertex from a third page.

Thus \(B_3\) has exactly \(12\) outer multiset bases, while for every \(r\ge4\) the number of bases is
\[
2r(r-1)^2.
\]

## Assumptions and scope
All graphs are finite, simple, and connected. For \(S\subseteq V(G)\), the multiset representation of a vertex \(v\notin S\) is the multiset of distances from \(v\) to the vertices of \(S\). An outer multiset resolving set is a set \(S\) for which all vertices in \(V(G)\setminus S\) have pairwise distinct multiset representations. The minimum cardinality of such a set is denoted by \(\operatorname{odim}(G)\).

For \(B_r\), put
\[
X=\mathbf 1_{\{x\in S\}},\qquad Y=\mathbf 1_{\{y\in S\}},
\]
and let
\[
A=|\{i:a_i\in S\}|,\qquad B=|\{i:b_i\in S\}|.
\]
For a vertex outside \(S\), record its multiset representation by the triple
\[
\sigma_S(v)=(m_1(v),m_2(v),m_3(v)),
\]
where \(m_j(v)\) is the number of landmarks at distance \(j\).

## Proof
The distance structure of \(B_r\) gives the following exact signatures whenever the displayed vertex lies outside \(S\):
\[
\sigma_S(x)=(Y+A,B,0),
\]
\[
\sigma_S(y)=(X+B,A,0),
\]
\[
\sigma_S(a_i)=
\left(
X+\mathbf 1_{\{b_i\in S\}},
Y+A,
B-\mathbf 1_{\{b_i\in S\}}
\right),
\]
and
\[
\sigma_S(b_i)=
\left(
Y+\mathbf 1_{\{a_i\in S\}},
X+B,
A-\mathbf 1_{\{a_i\in S\}}
\right).
\]

Hence two vertices \(a_i,a_j\notin S\) can have distinct signatures only if exactly one of \(b_i,b_j\) lies in \(S\). Therefore at most two \(a\)-vertices can lie outside an outer multiset resolving set. Similarly, at most two \(b\)-vertices can lie outside.

Suppose six vertices lay outside \(S\). Then both spine vertices would have to lie outside, together with exactly two \(a\)-vertices and two \(b\)-vertices. This forces
\[
A=B=r-2,
\]
and therefore
\[
\sigma_S(x)=\sigma_S(y)=(r-2,r-2,0),
\]
a contradiction. Thus every outer multiset resolving set satisfies
\[
|V(B_r)\setminus S|\le5,
\]
so
\[
|S|\ge 2r-3.
\]

For the matching construction, let
\[
V(B_r)\setminus S=\{x,y,a_1,b_1,a_2\}.
\]
Then \(A=r-2\) and \(B=r-1\), and the five outside signatures are
\[
(r-2,r-1,0),\quad
(r-1,r-2,0),\quad
(0,r-2,r-1),\quad
(0,r-1,r-2),\quad
(1,r-2,r-2),
\]
which are pairwise distinct for every \(r\ge3\). Hence
\[
\operatorname{odim}(B_r)=2r-3.
\]

It remains to classify the bases. Let \(U=V(B_r)\setminus S\) for a basis \(S\), so \(|U|=5\). Write
\[
\alpha=|\{i:a_i\in U\}|,\qquad
\beta=|\{i:b_i\in U\}|.
\]
The previous argument gives \(\alpha,\beta\le2\).

If both \(x\) and \(y\) lie in \(U\), then \(\alpha+\beta=3\), so \(\{\alpha,\beta\}=\{1,2\}\). If, for example, \(\alpha=2\), the two outside \(a\)-vertices must have different mate-selection states, so exactly one lies on the unique page whose \(b\)-vertex is also outside. Thus \(U\) consists of both spine vertices, one complete internal page pair, and one internal vertex from another page. The case \(\beta=2\) is symmetric. Every such complement resolves: after relabeling, its five signatures are exactly the five signatures displayed in the construction above. The number of complements of this type is
\[
2r(r-1).
\]

If exactly one spine vertex lies in \(U\), then \(\alpha+\beta=4\), so \(\alpha=\beta=2\). Distinguishing the two outside \(a\)-vertices forces exactly one of their \(b\)-mates outside, and distinguishing the two outside \(b\)-vertices forces exactly one of their \(a\)-mates outside. Therefore \(U\) consists of the omitted spine vertex, one complete page pair, one \(a\)-vertex from a second page, and one \(b\)-vertex from a third page.

Assume, by symmetry, that \(x\in U\) and \(y\in S\). The five signatures are then
\[
(r-1,r-2,0),\quad
(0,r-1,r-2),\quad
(1,r-2,r-2),\quad
(1,r-1,r-3),\quad
(2,r-2,r-3).
\]
They are pairwise distinct exactly when \(r\ge4\). For \(r=3\), the first and last signatures both equal
\[
(2,1,0),
\]
so this second type is invalid. For \(r\ge4\), its number of complements is
\[
2r(r-1)(r-2).
\]

No basis can omit neither spine vertex, because that would require five outside internal vertices although at most four are possible. Hence the preceding two types are complete. Therefore the number of bases is
\[
2r(r-1)=12
\]
when \(r=3\), and for \(r\ge4\) it is
\[
2r(r-1)+2r(r-1)(r-2)
=
2r(r-1)^2.
\]

## Verification
The included verifier independently constructs each book graph, computes all-pairs shortest-path distances, and evaluates outer multiset representations directly from the definition.

For every \(3\le r\le9\), it checks every landmark set smaller than \(2r-3\), confirms that none resolves, enumerates every set of size \(2r-3\), and compares the exact basis family with the two complement types in the theorem.

## Relationship to prior work
The 2019 paper introducing outer multiset dimension establishes the parameter, general bounds, computational hardness, and exact values for several basic graph families such as paths and cycles. Targeted inspection of its accessible full text found no book-graph or generalized-theta treatment.

A 2022 continuation proves, among other results, that graphs of order \(n\) have outer multiset dimension \(n-1\) exactly when they are regular of diameter at most two, characterizes the value two, studies lexicographic products, and determines rectangular-grid values. It lists AMS 2020 classes \(05C12\) and \(05C76\). Book graphs with at least three pages are nonregular and have diameter three, so the order-minus-one theorem does not apply. Targeted full-text searches found no book or theta occurrence.

The present result gives a different stable high-dimensional regime:
\[
\operatorname{odim}(B_r)=|V(B_r)|-5.
\]
It also determines every minimum resolving set and its exact multiplicity.

## Limitations
The theorem covers square-page books with \(r\ge3\). The two-page book \(B_2\) is exceptional and is not included. No claim is made for triangular books, books with longer cycle pages, or arbitrary generalized theta graphs. The exhaustive computation is corroborative only; the proof above establishes the result for all claimed parameters.

## References
1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, I. G. Yero, “Distance-based vertex identification in graphs: the outer multiset dimension,” arXiv:1902.03017v1, 8 February 2019; Applied Mathematics and Computation 363 (2019), Article 124612, DOI 10.1016/j.amc.2019.124612.
2. S. Klavžar, D. Kuziak, I. G. Yero, “Further contributions on the outer multiset dimension of graphs,” arXiv:2207.06834v1, 14 July 2022; Results in Mathematics 78 (2023), Article 50, DOI 10.1007/s00025-022-01829-8.
