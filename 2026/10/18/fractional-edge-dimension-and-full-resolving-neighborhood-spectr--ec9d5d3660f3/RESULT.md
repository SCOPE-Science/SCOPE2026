# Fractional edge dimension and full resolving-neighborhood spectrum of two-subset Kneser graphs

## Finding
For each integer \(n\ge5\), let \(G_n=\mathrm{KG}(n,2)\) be the graph on the two-element subsets of \([n]\), with two vertices adjacent precisely when the subsets are disjoint. For two distinct graph edges \(e,f\), write \(R(e,f)\) for the vertices having unequal shortest-path distances to the two edges, where distance to an edge is minimum distance to an endpoint. Let \(\mathcal R_n(z)=\sum_{\{e,f\}\in\binom{E(G_n)}2}z^{|R(e,f)|}\).

**Theorem.** For every integer \(n\ge5\),
\[
\mathcal R_n(z)=3\binom n4z^4+30\binom n5z^6+60\binom n5z^8+225\binom n6z^{10}+180\binom n6z^{11}+(630\binom n7+315\binom n8)z^{12}.
\]
Consequently, the minimum edge-resolving neighborhood size is four, and the fractional edge dimension is
\[
\operatorname{edim}_f(G_n)=\frac{\binom n2}{4}=\frac{n(n-1)}8.
\]
Here \(\binom nt=0\) when \(t>n\). The six displayed powers describe the possible sizes in the union over all admissible orders; for an individual order, terms with zero coefficients are absent.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected. A graph edge of \(G_n\) is an unordered pair \(e=\{A,B\}\) of disjoint doubletons in \([n]\); its *ground support* \(U_e=A\cup B\) has four elements. The *endpoint matching* \(M_e=\{A,B\}\) is one of the three perfect matchings of the ground complete graph on \(U_e\). The distance of a probe vertex \(S\) to \(e\) is \(\delta_e(S)=\min\{d_{G_n}(S,A),d_{G_n}(S,B)\}\), and \(R(e,f)=\{S:\delta_e(S)\ne\delta_f(S)\}\). A fractional edge-resolving function is \(w:V(G_n)\to[0,1]\) with \(\sum_{S\in R(e,f)}w(S)\ge1\) for all distinct edges; \(\operatorname{edim}_f\) minimizes \(\sum_Sw(S)\).

## Proof
**Distances and the local support identity.** For \(n\ge5\), two different overlapping doubletons have distance two: a doubleton disjoint from their three-element union exists. Distinct disjoint doubletons are adjacent. Therefore, for any graph edge \(e=\{A,B\}\),
\[
\delta_e(S)=\begin{cases}
0,&S\in\{A,B\},\\
2,&S\subseteq U_e\ \text{and}\ S\notin\{A,B\},\\
1,&S\not\subseteq U_e.
\end{cases}
\]
In the last case, a doubleton not contained in \(U_e\) cannot meet both disjoint endpoint doubletons, so it is adjacent to at least one of them.

For different edges \(e,f\), put \(h=|U_e\cap U_f|\), and define \(q\) as the number of doubletons \(S\subseteq U_e\cap U_f\) that are members of exactly one of the two endpoint matchings. If \(S\) lies in exactly one ground support, its two edge distances differ; if it is in neither, the distances coincide; if in both, they differ exactly when it belongs to one matching but not the other. Thus
\[
|R(e,f)|=\left|\binom{U_e}{2}\triangle\binom{U_f}{2}\right|+q=12-2\binom h2+q.\tag{1}
\]

**Exact pair census.** Put \(t=|U_e\cup U_f|=8-h\). Count the unordered distinct graph-edge pairs with union support equal to a *prescribed* \(t\)-element set. The full list, justified below, is

| \(t\) | \(h\) | \(q\) | \(|R(e,f)|\) | Pairs per prescribed support |
|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 4 | 3 |
| 5 | 3 | 0 | 6 | 30 |
| 5 | 3 | 2 | 8 | 60 |
| 6 | 2 | 0 | 10 | 225 |
| 6 | 2 | 1 | 11 | 180 |
| 7 | 1 | 0 | 12 | 630 |
| 8 | 0 | 0 | 12 | 315 |

For \(t=4\) there are three matchings of the same four-set, hence three unordered pairs, and two different matchings disagree on four doubletons. For \(t=5\), the first ground edge has \(5\cdot3=15\) choices. The second has four choices for the omitted element of the first support and three choices for its matching, so there are \(15\cdot4\cdot3/2=90\) unordered pairs. In the three-element intersection, each endpoint matching has precisely one contained pair. For each first edge, exactly four choices of the second edge retain the same contained pair, giving \(15\cdot4/2=30\) with \(q=0\); the other 60 have \(q=2\).

For \(t=6\), the first edge has \(\binom64\cdot3=45\) choices. Choose two common ground elements in six ways and the matching of the other edge in three ways, giving \(45\cdot6\cdot3/2=405\) unordered pairs. With a prescribed first edge, \(q=1\) precisely if exactly one of the matchings includes the common doubleton: there are \(2\cdot2=4\) cases where the first includes it and the second does not, and \(4\cdot1=4\) cases with the roles reversed. Hence \(45\cdot8/2=180\) with \(q=1\), leaving 225 with \(q=0\). For \(t=7\), the first edge has \(\binom74\cdot3=105\) choices, the second shares one of its four ground elements and has three matchings: \(105\cdot4\cdot3/2=630\) pairs. For \(t=8\), choose the first four-set and matching in \(\binom84\cdot3=210\) ways; the second four-set is the complement and admits three matchings, yielding \(210\cdot3/2=315\) pairs. Multiplying each fixed-support count by \(\binom nt\) yields the claimed polynomial through (1), without double counting (each pair has a unique union support).

**Exact fractional optimum.** Every resolving neighborhood has at least four vertices, so the constant weight \(w(S)=1/4\) is feasible, proving \(\operatorname{edim}_f(G_n)\le\binom n2/4\). Conversely, fix any four-element ground set \(U\). Its three perfect matchings are three graph edges; any two have resolving neighborhood consisting of the four endpoint doubletons belonging to their two matchings. Thus each \(U\) furnishes three constraints, each requiring total weight at least one. As the three pairs of matchings run through these constraints, each of the six doubletons contained in \(U\) occurs in exactly two resolving neighborhoods. Summing for every four-set gives
\[
2\binom{n-2}{2}\sum_{S\in\binom{[n]}2}w(S)\ge3\binom n4.
\]
Since \(3\binom n4/(2\binom{n-2}{2})=\binom n2/4\), this matches the uniform upper bound and proves optimality for every \(n\ge5\). \(\square\)

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3.9 or later. This standalone program builds each \(G_n\) for \(5\le n\le9\), independently obtains all vertex distances by breadth-first search, enumerates all unordered pairs of graph edges, computes exact edge-distance profiles, checks formula (1), and compares the size histogram with the theorem. It checks 99,753 pairs. The output is supplied in \(\texttt{verification-output.txt}\). Finite computations corroborate but do not replace the proof of the infinite result.

## Relationship to prior work
Yi introduced and studied the fractional edge dimension and explicitly calculated the Petersen graph case (Proposition 3.5 in [1]); \(G_5\) is the Petersen graph, so the \(n=5\) scalar value \(5/2\) is **previously known**. Goshi et al. [2] supplied a symmetry-based general expression for vertex- and edge-transitive graphs, which can provide the scalar value once the minimum resolving-neighborhood size is independently known. Thus the general symmetry reduction is also **not new**. The contribution here is the explicit all-parameter ground-support classification, the exact polynomial recording every distinct-edge-pair neighborhood size, and an elementary matching tight primal–dual bound for every \(n\ge5\). Neither inspected source states this six-term KG-family census or carries out the needed minimal-support calculation.

## Limitations
The result is restricted to two-element Kneser graphs and fractional **edge** resolving, not arbitrary Kneser graphs or integral edge dimension. It does not claim uniqueness of the minimizing weights. The \(n=5\) scalar instance and the general transitivity approach precede this result. Computational verification is finite, and bibliographic priority cannot exclude unindexed or inaccessible equivalent work; independent scientific evaluation has not been performed.

## References
[1] E. Yi, *On the edge dimension and fractional edge dimension of graphs*, arXiv:2103.07375v1 (first submitted 2021-03-12), subsequently *Discrete Applied Mathematics*, DOI:10.1016/j.dam.2022.07.014. https://arxiv.org/abs/2103.07375

[2] N. Goshi, S. Zafar, T. Rashid and J. L. G. Guirao, *A Combinatorial Approach to the Computation of the Fractional Edge Dimension of Graphs*, *Mathematics* **9** (2021), article 2364, DOI:10.3390/math9192364. https://doi.org/10.3390/math9192364
