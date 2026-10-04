# Locating-total domination polynomial of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\) and \(N=\sum_i n_i\). A set \(S\subseteq V(G)\) is a locating-total dominating set if and only if all three conditions hold:

1. \(S\) meets at least two partite sets.
2. \(V(G)\setminus S\) contains at most one vertex from each partite set.
3. At most one singleton partite set has its unique vertex outside \(S\).

Write
\[
p=\left|\{i:n_i\ge2\}\right|,\qquad
s=\left|\{i:n_i=1\}\right|,
\]
and
\[
P(x)=\prod_{n_i\ge2}x^{n_i-1}(x+n_i).
\]
For the locating-total domination size enumerator
\[
\mathcal L_t(G;x)=\sum_{S\text{ locating-total dominating}}x^{|S|},
\]
one has
\[
\mathcal L_t(G;x)=
\begin{cases}
P(x)\bigl(x^s+s x^{s-1}\bigr),& p\ge2,\\
P(x)\bigl(x^s+s x^{s-1}\bigr),& p=1,\ s\ge2,\\
xP(x),& p=1,\ s=1,\\
x^s+s x^{s-1},& p=0,\ s\ge3,\\
x^2,& p=0,\ s=2.
\end{cases}
\]
Here the factor \(x^s+s x^{s-1}\) is interpreted only when \(s\ge1\).

Thus, whenever \(p\ge2\), or \(p=1\) and \(s\ge2\),
\[
\gamma_t^L(G)=N-p-\min\{1,s\},
\]
and the number of minimum locating-total dominating sets is
\[
\left(\prod_{n_i\ge2}n_i\right)\max\{1,s\}.
\]
For the star \(K_{1,n}\) with \(n\ge2\) and for the complete graph \(K_s\) with \(s\ge3\), \(\gamma_t^L(G)=N-1\); for \(K_2\), \(\gamma_t^L(K_2)=2\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The complete multipartite representation has \(r\ge2\) nonempty partite sets. A locating-total dominating set \(S\) is a total dominating set for which distinct vertices outside \(S\) have distinct open-neighborhood traces on \(S\).

The result is an all-set classification and size enumerator, not only a formula for the minimum cardinality.

## Proof
Let the partite sets be \(V_1,\ldots,V_r\), with \(|V_i|=n_i\).

First, \(S\) is a total dominating set exactly when it meets at least two partite sets. If \(S\) meets only one part, then vertices of \(S\) have no neighbor in \(S\). If it meets at least two parts, every vertex has a neighbor in \(S\) lying in a different part.

Now suppose \(S\) is locating-total dominating. Two vertices in the same part have identical open neighborhoods, so two such vertices cannot both lie outside \(S\). Hence \(V(G)\setminus S\) contains at most one vertex from each part.

Consider distinct outside vertices \(u\in V_i\) and \(v\in V_j\) with \(i\ne j\). Since
\[
N(u)\cap S=S\setminus V_i,\qquad N(v)\cap S=S\setminus V_j,
\]
these two traces are equal if and only if
\[
S\cap V_i=S\cap V_j=\varnothing.
\]
Because at most one vertex is omitted from each part, an empty trace contribution \(S\cap V_i=\varnothing\) can occur only when \(n_i=1\) and the singleton vertex of \(V_i\) is omitted. Therefore distinct outside vertices from different parts fail to be located exactly when two singleton parts are both omitted. This proves the necessity of conditions 1--3.

Conversely, assume conditions 1--3. Condition 1 gives total domination. Outside vertices from the same part do not occur by condition 2. For outside vertices from different parts, equality of their traces would force both corresponding parts to be empty in \(S\), hence would force two omitted singleton parts, contrary to condition 3. Therefore \(S\) is locating-total dominating.

It remains to enumerate such sets. In a non-singleton part \(V_i\), either no vertex is omitted, contributing \(x^{n_i}\), or one vertex is omitted in \(n_i\) ways, contributing \(n_i x^{n_i-1}\). Thus each non-singleton part contributes
\[
x^{n_i-1}(x+n_i),
\]
and their product is \(P(x)\). Across all \(s\) singleton parts, condition 3 allows either no omission or one omission, contributing
\[
x^s+s x^{s-1}.
\]
These independent choices already satisfy total domination except when there is only one non-singleton part and exactly one singleton part, where omitting the singleton would leave \(S\) supported in one part, and when all parts are singleton and \(r=2\), where omitting either vertex would do the same. Removing precisely those invalid terms gives the displayed case formula. The minimum degrees and their leading coefficients give the formulas for \(\gamma_t^L(G)\) and the number of minimum sets.

## Verification
An exact checker exhaustively enumerates every complete multipartite isomorphism type of order at most \(9\), tests every vertex subset directly against the locating-total domination definition, and compares the resulting coefficient table with the closed formula above. The replay checks \(87\) multipartite types and reports no discrepancy.

This finite computation is a regression check only; the proof above establishes the result for arbitrary part sizes and arbitrary order.

## Relationship to prior work
Haynes, Henning, and Howard introduced locating-total domination and studied it for trees. Henning and Jafari Rad later developed general bounds and structural observations, including the standard twin obstruction, proved that connected graphs of order at least \(3\) have locating-total domination number at most \(N-1\) with equality exactly for stars and complete graphs, and explicitly noted \(\gamma_t^L(K_{3,3})=4\). Those results recover boundary or special cases of the formulas above but do not state the all-complete-multipartite classification or enumerator.

Foucaud and Henning subsequently emphasized twin structure in locating-total domination. The present classification exploits the especially rigid open-neighborhood traces of complete multipartite graphs: within each part all vertices are open twins, while traces of vertices from different parts can coincide only when both corresponding parts are absent from the locating set.

## Limitations
The result is specific to complete multipartite graphs. It does not claim an analogous factorization for arbitrary cographs, complete multipartite graphs with added internal edges, or other graph products. The literature comparison found no exact all-set formula for this class, but terminology and indexing differences can hide older special-case results; this remains a residual bibliographic risk.

## References
1. T. W. Haynes, M. A. Henning, J. Howard, “Locating and total dominating sets in trees,” *Discrete Applied Mathematics* 154 (2006), 1293–1300. DOI: 10.1016/j.dam.2006.01.002.
2. M. A. Henning, N. Jafari Rad, “Locating-total domination in graphs,” *Discrete Applied Mathematics* 160 (2012), 1986–1993. DOI: 10.1016/j.dam.2012.04.004.
3. F. Foucaud, M. A. Henning, “Locating-Total Dominating Sets in Twin-Free Graphs: a Conjecture,” *Electronic Journal of Combinatorics* 23(3) (2016), P3.9. DOI: 10.37236/5147.
