# 4-existentially closed graphs are super geometric dominant

## Statement

For a graph \(G\), call \(G\) **4-existentially closed** (4-e.c.) if for every two disjoint sets \(U,W\subseteq V(G)\) with \(|U|+|W|=4\), there is a vertex \(x\notin U\cup W\) adjacent to every vertex of \(U\) and to no vertex of \(W\).

Chen, Huzhang, Miao and Yang call a connected graph **super geometric dominant** if it has diameter 2 and the family consisting of all metric lines and all closed neighborhoods is an antichain: distinct generated lines are incomparable, distinct closed neighborhoods are incomparable, and every line is incomparable with every closed neighborhood.

**Theorem 1.** Every 4-e.c. graph is super geometric dominant.

This gives a direct bridge from adjacency-extension constructions to metric-line antichains.

For an explicit consequence, let \(P(p)\) be the prime-order Paley graph on \(\mathbb F_p\), where \(p\equiv1\pmod4\), with \(x\sim y\) exactly when \(x-y\) is a nonzero quadratic residue.

**Theorem 2.** If \(p\equiv1\pmod4\) is prime and \(p\ge193\), then \(P(p)\) is 4-e.c. and hence super geometric dominant.

Thus prime-order Paley graphs give an explicit deterministic infinite family of super geometric dominant graphs. This addresses the constructive-family gap explicitly noted by Chen--Huzhang--Miao--Yang in their 2015 discussion. The numerical threshold \(193\) is only a convenient sufficient bound and is not claimed optimal as a Paley adjacency bound.

There are much smaller examples outside the sufficient 4-e.c. condition:

**Proposition 3.** \(P(17)\) is super geometric dominant. It has 17 vertices, 68 edges and 136 distinct generated lines, with 68 lines of size 6 and 68 of size 10. It is not 4-e.c.; for example, no vertex outside \(\{0,1,2,3\}\) is nonadjacent to all four of these vertices.

## Proof of Theorem 1

A 4-e.c. graph also realizes every prescribed adjacency/nonadjacency pattern on any set of at most four vertices: add arbitrary extra specified vertices until four are specified, and assign the extras either adjacency status. In particular, all patterns used below are available.

First, \(G\) has diameter 2. Any two nonadjacent vertices have a common neighbor by the two-vertex extension property, while the one-vertex extension property gives a nonedge, so the diameter is exactly 2.

In a diameter-2 graph, three distinct vertices are collinear in the graph metric exactly when their induced three-vertex graph has two edges. Following Chen et al., call such a triple **tight**. Hence, for distinct \(u,v,x\),
\[
x\in\overline{uv}\quad\Longleftrightarrow\quad \{u,v,x\}\text{ is tight}.
\]

We verify the three antichain requirements in the definition of super geometric dominance.

### 1. Distinct lines are incomparable

Let \(A=\{a,b\}\) and \(B=\{c,d\}\) be distinct unordered pairs. We construct \(x\in\overline{ab}\setminus\overline{cd}\).

If the pairs are disjoint, prescribe the adjacencies of \(x\) independently on the four endpoints. For \(A\), if \(ab\notin E(G)\), make \(x\) adjacent to both \(a,b\); if \(ab\in E(G)\), make \(x\) adjacent to exactly one of them. Then \(\{a,b,x\}\) is tight. For \(B\), make \(x\) adjacent to neither \(c\) nor \(d\); this makes \(\{c,d,x\}\) non-tight whether \(cd\) is an edge or a nonedge. The 4-e.c. property supplies such an \(x\).

Suppose instead that the pairs share one endpoint, say \(A=\{s,p\}\) and \(B=\{s,q\}\). Write the three bits below as the prescribed adjacencies of \(x\) to \((s,p,q)\). According to the edge statuses of \(sp\) and \(sq\), use
\[
\begin{array}{c|c|c}
sp & sq & (xs,xp,xq)\\ \hline
0&0&(1,1,0)\\
0&1&(1,1,1)\\
1&0&(0,1,0)\\
1&1&(0,1,0).
\end{array}
\]
In every row \(\{s,p,x\}\) is tight and \(\{s,q,x\}\) is non-tight. Thus \(x\in\overline{sp}\setminus\overline{sq}\). Interchanging the two pairs gives the reverse difference, so no two distinct lines are comparable.

### 2. Closed neighborhoods are incomparable

For distinct \(a,b\), choose \(x\) adjacent to \(a\) and nonadjacent to \(b\). Then
\[
x\in N[a]\setminus N[b],
\]
and reversing \(a,b\) gives incomparability.

### 3. Every line and closed neighborhood are incomparable

Fix \(a\) and distinct \(b,c\).

First produce a point of \(N[a]\setminus\overline{bc}\). If \(a\notin\{b,c\}\), choose \(x\) adjacent to \(a\) and, according as \(bc\) is an edge or nonedge, make \(x\) adjacent to both \(b,c\) or to neither. Then \(x\in N[a]\) and \(\{b,c,x\}\) is non-tight. If \(a=b\) (the case \(a=c\) is symmetric), choose \(x\) adjacent to \(b\) and choose its adjacency to \(c\) equal to the adjacency of \(b\) to \(c\). Again \(x\in N[b]\) and the triple is non-tight.

Next produce a point of \(\overline{bc}\setminus N[a]\). If \(a\notin\{b,c\}\), require \(x\not\sim a\); if \(bc\) is a nonedge, make \(x\) adjacent to both \(b,c\), while if \(bc\) is an edge, make \(x\) adjacent to exactly one of \(b,c\). Then \(\{b,c,x\}\) is tight and \(x\notin N[a]\). If \(a=b\), then when \(bc\) is a nonedge the endpoint \(c\) itself belongs to \(\overline{bc}\setminus N[b]\); when \(bc\) is an edge, choose \(x\not\sim b\) and \(x\sim c\), which makes \(\{b,c,x\}\) tight while keeping \(x\notin N[b]\). The case \(a=c\) is symmetric.

All defining antichain conditions hold, proving Theorem 1. \(\square\)

## Proof of Theorem 2

Let \(\chi\) be the Legendre symbol on \(\mathbb F_p\), extended by \(\chi(0)=0\). Since \(p\equiv1\pmod4\), \(\chi(-1)=1\), so for distinct \(x,a\), adjacency in \(P(p)\) is equivalent to \(\chi(x-a)=1\).

Take four distinct prescribed vertices \(a_1,\ldots,a_4\) and desired signs \(\varepsilon_i\in\{1,-1\}\), where \(+1\) means adjacent and \(-1\) means nonadjacent. Let \(N\) be the number of vertices \(x\notin\{a_1,\ldots,a_4\}\) satisfying
\[
\chi(x-a_i)=\varepsilon_i\qquad(1\le i\le4).
\]
Set
\[
F(x)=\prod_{i=1}^4\bigl(1+\varepsilon_i\chi(x-a_i)\bigr).
\]
Away from the four roots, \(F(x)=16\) exactly for the desired pattern and is 0 otherwise. At a root \(x=a_j\), \(F(x)\) is nonnegative and at most 8. Therefore, with a root correction \(E\) satisfying \(0\le E\le32\),
\[
16N=\sum_{x\in\mathbb F_p}F(x)-E.
\]

Expanding the product, the four one-character sums vanish. Each of the six two-character sums is exactly \(-1\). For distinct shifts, the standard quadratic-character estimate
\[
\left|\sum_{x\in\mathbb F_p}\prod_{i=1}^r\chi(x-a_i)\right|\le(r-1)\sqrt p
\]
holds for \(r=3,4\). Hence the four cubic terms contribute at worst \(-8\sqrt p\), the quartic term at worst \(-3\sqrt p\), and the six quadratic terms at worst \(-6\). Consequently
\[
16N\ge p-38-11\sqrt p.
\]
For \(p\ge193\), the right-hand side is positive. Thus every prescribed four-vertex adjacency pattern has an outside realizing vertex: \(P(p)\) is 4-e.c. Theorem 1 now gives super geometric dominance. \(\square\)

## Exact finite verification of Proposition 3

The accompanying standalone script constructs \(P(17)\), computes every one of its \(\binom{17}{2}=136\) metric lines, and exhaustively checks the four defining conditions of super geometric dominance: diameter 2, pairwise line incomparability, pairwise closed-neighborhood incomparability, and line/closed-neighborhood incomparability in both directions. The expected output is included as a separate artifact. This finite check supports only Proposition 3; the general theorems above are proved analytically.

## Context and originality

Chen--Huzhang--Miao--Yang (2015) introduced super geometric dominant graphs, proved that suitable random graphs are almost surely super geometric dominant, and obtained a randomized near-complete construction. Their discussion explicitly notes that they knew no constructive family avoiding randomness and also asks about small examples.

Long before that definition, Blass--Exoo--Harary (1981) and Ananchuen--Caccetta (1993) proved that sufficiently large Paley graphs realize arbitrary fixed adjacency patterns; Cameron--Stark (2002) formulated the modern \(n\)-existentially-closed terminology and noted the Paley examples. Those results supply a natural deterministic source of 4-e.c. graphs, but they predate the super-geometric-dominance notion. Targeted searches through the current literature located no statement connecting 4-e.c. graphs or Paley graphs to super geometric dominance. Accordingly, originality is claimed only **to the best of our knowledge**.

The new content here is the transfer theorem from 4-e.c. to super geometric dominance and its metric-line application, together with the explicit sufficient Paley threshold and the exact small Paley example. The classical Paley adjacency results and character-sum estimates themselves are not claimed as new.

## Limitations

- The 4-e.c. hypothesis is sufficient, not necessary; \(P(17)\) already shows the converse fails.
- The bound \(p\ge193\) is not claimed sharp, and it is restricted here to prime-order Paley graphs to keep the character-sum argument elementary.
- No claim is made about the minimum possible order of a super geometric dominant graph.
- No improvement is claimed for the extremal edge-count problem for super geometric dominant graphs; Paley graphs have density about one half and do not compete with the near-complete constructions of Chen et al.
- The literature search can miss differently indexed later work; the originality claim is therefore explicitly to the best of our knowledge.

## References

1. X. Chen, G. Huzhang, P. Miao, K. Yang, *Graph metric with no proper inclusion between lines*, Discrete Applied Mathematics 185 (2015), 59--70. https://doi.org/10.1016/j.dam.2014.12.022
2. A. Blass, G. Exoo, F. Harary, *Paley graphs satisfy all first-order adjacency axioms*, Journal of Graph Theory 5 (1981), 435--439. https://doi.org/10.1002/jgt.3190050414
3. W. Ananchuen, L. Caccetta, *On the adjacency properties of Paley graphs*, Networks 23 (1993), 227--236. https://doi.org/10.1002/net.3230230404
4. P. J. Cameron, D. Stark, *A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property*, Electronic Journal of Combinatorics 9 (2002), R31. https://doi.org/10.37236/1647
5. D. Cizma, N. Linial, *Irreducible nonmetrizable path systems in graphs*, Journal of Graph Theory 102 (2023), 5--14. https://doi.org/10.1002/jgt.22854. Theorem 2.4 records the quadratic-character estimate used above, and Lemma 2.5 records the exact two-character sum.

**Same-model review: passed. Independent audit: not yet performed.**
