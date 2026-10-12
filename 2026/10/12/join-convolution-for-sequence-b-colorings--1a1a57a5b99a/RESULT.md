# Join convolution for sequence b-colorings

## Finding

Let \(G\) and \(H\) be finite simple connected graphs. For a finite non-increasing sequence
\[
S=(s_1,\ldots,s_k)
\]
of positive integers and a set
\[
I=\{i_1<\cdots<i_p\}\subseteq[k],
\]
write
\[
S_I=(s_{i_1},\ldots,s_{i_p}).
\]

Then
\[
\boxed{
G\vee H\text{ realizes }S
\iff
\exists\,\emptyset\ne I\subsetneq[k]
\text{ such that }
G\text{ realizes }S_I
\text{ and }
H\text{ realizes }S_{[k]\setminus I}.
}
\]

This is an exact shuffle law for realized sequences under graph join.

There is also an exact counting convolution. Let \(B_G(S)\) denote the number of surjective labeled b-colorings
\[
c:V(G)\to[k]
\]
that realize \(S\). Then
\[
\boxed{
B_{G\vee H}(S)
=
\sum_{\emptyset\ne I\subsetneq[k]}
B_G(S_I)\,B_H(S_{[k]\setminus I}).
}
\]

For a connected complete multipartite graph
\[
K_{n_1,\ldots,n_r},
\]
let
\[
m_1\ge m_2\ge\cdots\ge m_r
\]
be the part sizes in non-increasing order. A finite sequence
\[
S=(s_1,\ldots,s_k)
\]
is realized if and only if
\[
k=r
\]
and
\[
s_i\le m_i
\qquad
\text{for every }1\le i\le r.
\]
Hence
\[
\boxed{
(m_1,\ldots,m_r)
}
\]
is the unique maximal realized sequence.

If \(k=r\), define
\[
c_i=\bigl|\{j:n_j\ge s_i\}\bigr|.
\]
Then the exact number of labeled realizing b-colorings is
\[
\boxed{
B_{K_{n_1,\ldots,n_r}}(S)
=
\prod_{i=1}^r(c_i-i+1),
}
\]
where the product is interpreted as \(0\) when some factor is nonpositive.

For an infinite non-increasing sequence
\[
S=(s_1,s_2,\ldots),
\]
the \(S\)-spectrum of \(K_{n_1,\ldots,n_r}\) is
\[
\boxed{
\{r\}
}
\]
exactly when
\[
s_i\le m_i
\qquad
(1\le i\le r),
\]
and is empty otherwise. Whenever the spectrum is nonempty,
\[
\chi_S(K_{n_1,\ldots,n_r})
=
\phi_S(K_{n_1,\ldots,n_r})
=
r.
\]

## Assumptions and scope

A b-coloring is a proper coloring in which every color class contains at least one color-dominating vertex. A vertex is color-dominating when its closed neighborhood contains every color used by the coloring.

For a finite non-increasing sequence
\[
S=(s_1,\ldots,s_k),
\]
a b-coloring with exactly \(k\) colors realizes \(S\) when color class \(i\) contains at least \(s_i\) color-dominating vertices.

The join
\[
G\vee H
\]
is obtained from vertex-disjoint copies of \(G\) and \(H\) by adding every edge between the two copies.

The join theorem is stated for nonempty connected factors, matching the graph scope used in the initiating sequence-b-coloring paper. The complete multipartite corollary is proved directly rather than by treating independent partite classes as disconnected factors.

## Proof

Consider a proper coloring of
\[
G\vee H.
\]
No color can occur on both sides of the join, because every vertex of \(G\) is adjacent to every vertex of \(H\). Thus the color set partitions uniquely into the colors used on \(G\) and the colors used on \(H\).

Fix a vertex
\[
v\in V(G).
\]
Every color used on \(H\) automatically occurs in the open neighborhood of \(v\). Therefore \(v\) is color-dominating in the join if and only if its closed neighborhood inside \(G\) contains every color used on \(G\). In other words,
\[
v\text{ is a CDV in }G\vee H
\iff
v\text{ is a CDV in the restricted coloring of }G.
\]
The same statement holds with \(G\) and \(H\) interchanged.

Suppose first that a b-coloring of \(G\vee H\) realizes
\[
S=(s_1,\ldots,s_k).
\]
Let \(I\subset[k]\) be the set of color labels used on \(G\). Since both factors are nonempty, \(I\) is nonempty and proper. Restricting the coloring to \(G\) produces a b-coloring that realizes \(S_I\), because the number of CDVs in every \(G\)-color class is unchanged by restriction. Similarly, the restriction to \(H\) realizes \(S_{[k]\setminus I}\).

Conversely, suppose \(G\) realizes \(S_I\) and \(H\) realizes \(S_{[k]\setminus I}\) for a nonempty proper \(I\). Relabel the colors of the two realizing colorings by the corresponding global labels in \([k]\) and combine them. Properness holds because the two color sets are disjoint and all cross edges are present. Every factor-CDV remains a join-CDV because it additionally sees every color on the opposite factor. The combined coloring therefore realizes \(S\).

For the counting formula, every labeled realizing coloring of \(G\vee H\) has a unique label set \(I\) on \(G\). For a fixed \(I\), restriction gives a bijection between such join colorings and ordered pairs consisting of a labeled realizing coloring of \(G\) for \(S_I\) and one of \(H\) for \(S_{[k]\setminus I}\). Summing over \(I\) yields
\[
B_{G\vee H}(S)
=
\sum_{\emptyset\ne I\subsetneq[k]}
B_G(S_I)B_H(S_{[k]\setminus I}).
\]

Now let
\[
G=K_{n_1,\ldots,n_r}.
\]
In any proper coloring, a color class is contained in a single partite class. Suppose some part \(V_j\) uses at least two colors. A vertex of \(V_j\) is adjacent to every vertex outside \(V_j\) and to no other vertex of \(V_j\). Hence it misses every color appearing elsewhere in \(V_j\), so no vertex in that part is color-dominating. Consequently no b-coloring may split a part into two or more colors.

Every proper b-coloring therefore uses exactly one color on each part and exactly \(r\) colors. Conversely, every assignment of distinct colors to the \(r\) parts is a b-coloring, and every vertex is color-dominating. Thus, if color \(i\) is assigned to a part of size \(n_j\), the sequence requirement at that color is precisely
\[
s_i\le n_j.
\]

After sorting part sizes as
\[
m_1\ge\cdots\ge m_r
\]
and recalling that \(S\) is non-increasing, a feasible bijection between requirements and parts exists exactly when
\[
s_i\le m_i
\qquad
(1\le i\le r).
\]
This proves the realization criterion and the unique maximal sequence.

For the count, let
\[
E_i=\{j:n_j\ge s_i\},
\qquad
c_i=|E_i|.
\]
Since \(s_1\ge\cdots\ge s_r\),
\[
E_1\subseteq E_2\subseteq\cdots\subseteq E_r.
\]
Assign colors in the order \(1,2,\ldots,r\). There are \(c_1\) choices for color \(1\). At step \(i\), all \(i-1\) previously chosen parts lie in \(E_i\), so exactly
\[
c_i-(i-1)
\]
eligible parts remain. Multiplication gives
\[
B_G(S)=\prod_{i=1}^r(c_i-i+1).
\]
The infinite-sequence statement follows because the only possible b-color count is \(r\).

## Verification

The accompanying script `artifacts/verify.py` checks both parts of the theorem by direct enumeration.

For the join law, it enumerates every labeled connected graph on one, two, or three vertices, forms every ordered pair of such graphs, and computes every b-coloring of the join by testing properness and the closed-neighborhood CDV condition from scratch. It compares the exact CDV-count profiles of the join with the predicted shuffle product of the exact profiles of the two factors.

For complete multipartite graphs, it enumerates every nondecreasing part-size profile of total order at most six. It brute-forces every possible color assignment for every color count, identifies b-colorings directly, checks that only the number of partite classes can occur, and then compares the exact number of labeled colorings realizing every non-increasing requirement sequence with the product formula.

The finite computation is corroborative only. The proof above establishes the theorem for all finite connected factors and all complete multipartite part sizes.

## Relationship to prior work

Jakovac and Lang introduced sequence b-colorings in 2026. Their paper defines realization, the \(S\)-spectrum, and the parameters \(\chi_S\) and \(\phi_S\), proves general bounds and realizability results, characterizes sequences realized by cycles, studies regular graphs with girth conditions, and analyzes colorings requiring one additional CDV.

The searchable full text of that paper contains no occurrence of “join,” “complete multipartite,” or “complete bipartite.” Its stated graph-class results concern cycles and regular graphs rather than join decompositions. The theorem here gives an exact structural operation law for the new invariant and an exact family classification with enumeration.

Classical b-coloring literature already studies graph operations and cographs, and the ordinary b-chromatic number is a much older invariant. Those results correspond only to the constant requirement of at least one CDV per color class. They do not encode the full CDV multiplicity sequence or the labeled convolution
\[
B_{G\vee H}(S).
\]
The complete-multipartite corollary also determines the unique maximal realized sequence and every realization count, not merely the ordinary b-chromatic number.

## Limitations

The join law does not by itself give a closed form for arbitrary graph classes because one still needs the sequence-realization data of the factors.

The complete multipartite formula depends crucially on the fact that each part is an independent false-twin class with all possible cross edges. It does not directly extend to arbitrary cographs or complete multipartite graphs with internal edges added to the parts.

The originality assessment is literature-based rather than an absolute uniqueness proof. Classical b-coloring has a large literature on graph operations, so a differently phrased CDV-count factorization could exist in poorly indexed work. No covering sequence-b-coloring statement was located in the initiating paper, targeted web searches, or published-finding corpus searches.

## References

1. M. Jakovac and M. S. Lang, “Sequence b-colorings in graphs,” arXiv:2609.08484v1, first public September 8, 2026, MSC \(05C15\).
2. M. Jakovac and I. Peterin, “The b-chromatic number and related topics—A survey,” Discrete Applied Mathematics 235 (2018), 184–201, DOI 10.1016/j.dam.2017.08.008.
3. F. Bonomo, G. Durán, F. Maffray, J. Marenco, and M. Valencia-Pabon, “On the b-coloring of cographs and \(P_4\)-sparse graphs,” Graphs and Combinatorics 25 (2009), 153–167, DOI 10.1007/s00373-008-0829-1.
