# Proper conflict-free colorings of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), and \(n_i=|V_i|\). A proper vertex coloring of \(G\) is proper conflict-free exactly when at least two partite classes contain a color class of size one.

If
\[
t=\bigl|\{i:n_i=1\}\bigr|,\qquad N=\sum_{i=1}^r n_i,
\]
then
\[
\chi_{\mathrm{pcf}}(G)=r+\max\{0,2-t\}.
\]
Moreover every integer \(q\) in the interval
\[
\chi_{\mathrm{pcf}}(G)\le q\le N
\]
is realized by a proper conflict-free coloring.

There is also an exact enumeration. Let \(S(n,c)\) denote a Stirling number of the second kind and define
\[
A(n,c)=c!S(n,c).
\]
Thus \(A(n,c)\) is the number of surjections from an \(n\)-element labeled set onto a fixed \(c\)-element labeled color set. Let \(H(n,c)\) count those surjections having at least one singleton fiber. Inclusion-exclusion gives
\[
H(n,c)=
\sum_{j=1}^c
(-1)^{j+1}
\binom{c}{j}
(n)_j
(c-j)!
S(n-j,c-j),
\]
where \((n)_j=n(n-1)\cdots(n-j+1)\). Put
\[
U(n,c)=A(n,c)-H(n,c).
\]
For a fixed labeled set of \(q\) colors, the number of surjective proper conflict-free colorings is
\[
C_{\mathrm{pcf}}^{\mathrm{onto}}(G,q)
=
q!
\sum_{\substack{1\le c_i\le n_i\\c_1+\cdots+c_r=q}}
\frac{
\prod_i A(n_i,c_i)
-
\prod_i U(n_i,c_i)
-
\sum_{j=1}^r H(n_j,c_j)\prod_{i\ne j}U(n_i,c_i)
}{\prod_i c_i!}.
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. The graph is connected, so \(r\ge2\) and every part size \(n_i\) is positive. A proper conflict-free coloring is a proper vertex coloring in which every vertex has some color occurring exactly once in its open neighborhood. The counting formula counts colorings that use every color in a fixed labeled \(q\)-color palette.

The theorem concerns ordinary proper conflict-free coloring, not list coloring, odd coloring, or the stronger \(h\)-conflict-free variants.

## Proof

In a proper coloring of a complete multipartite graph, one color cannot occur in two different partite classes, because every two vertices in different parts are adjacent. Hence every color class lies entirely inside one \(V_i\).

Fix \(v\in V_i\). Its open neighborhood is
\[
N(v)=V(G)\setminus V_i.
\]
Because each color class lies in a single part, a color occurs exactly once in \(N(v)\) precisely when that color class is a singleton contained in some \(V_j\) with \(j\ne i\).

Let \(W\subseteq\{1,\ldots,r\}\) be the set of indices of parts containing at least one singleton color class. The proper coloring is conflict-free exactly when, for every \(i\), the set \(W\setminus\{i\}\) is nonempty. Since \(r\ge2\), this is equivalent to
\[
|W|\ge2.
\]
This proves the structural characterization.

Every part needs at least one color. A part of order one is automatically in \(W\) at no extra cost. A part of order at least two can be put in \(W\) using exactly two colors, by giving one vertex a singleton color and all remaining vertices another color. Therefore two witness parts are necessary and sufficient, so if \(t\) parts already have order one,
\[
\chi_{\mathrm{pcf}}(G)=r+\max\{0,2-t\}.
\]

For the spectrum, start from a minimum coloring constructed as above. If a part of order \(n_i\) currently uses \(c_i\) colors and \(c_i<n_i\), refine one of its nonsingleton color classes, increasing the number of colors by one. A witness part can always retain a singleton color while being refined. Repeating this operation reaches every color count up to \(N\), where all vertices have distinct colors. Hence the spectrum is the entire integer interval from \(\chi_{\mathrm{pcf}}(G)\) to \(N\).

For the enumeration, fix integers \(c_i\) with \(1\le c_i\le n_i\) and \(\sum_i c_i=q\). First allocate the \(q\) labeled colors among the parts; this can be done in
\[
\frac{q!}{\prod_i c_i!}
\]
ways. For a fixed allocation, part \(i\) has \(A(n_i,c_i)\) surjective colorings, of which \(H(n_i,c_i)\) have at least one singleton fiber and \(U(n_i,c_i)\) have none.

The number of fixed-allocation colorings with at least two witness parts is the total number
\[
\prod_i A(n_i,c_i)
\]
minus the colorings with no witness part,
\[
\prod_i U(n_i,c_i),
\]
minus the colorings with exactly one witness part,
\[
\sum_{j=1}^r
H(n_j,c_j)\prod_{i\ne j}U(n_i,c_i).
\]
Multiplying by the palette-allocation factor and summing over all admissible \((c_1,\ldots,c_r)\) proves the formula.

Finally, the inclusion-exclusion formula for \(H(n,c)\) follows by declaring, for each color, the event that its fiber has size one. If a specified set of \(j\) colors are singleton fibers, choose their distinct vertices in \((n)_j\) ways and surject the remaining \(n-j\) vertices onto the remaining \(c-j\) colors in \((c-j)!S(n-j,c-j)\) ways.

## Verification

The accompanying script `artifacts/verify.py` independently constructs complete multipartite graphs and exhaustively checks every nondecreasing part-size profile of total order \(2\) through \(6\). For every profile and every possible number of used colors, it compares three quantities: the direct neighborhood definition of proper conflict-free coloring, the singleton-witness characterization, and the exact Stirling-number formula.

The replay checks \(23\) multipartite profiles, \(114\) profile/color-count pairs, \(699753\) labeled colorings in the direct search space, and \(50405\) surjective colorings relevant to the exact counting comparison. The finite computation is corroborative only; the proof above establishes the theorem for all positive part sizes.

## Relationship to prior work

Qi, Song, and Cao recently study proper conflict-free choosability for sparse graphs and list primary MSC \(05C15\). Their first public version was submitted on September 10, 2026. Their results concern sparse high-girth graphs and degree-based list sizes, not complete multipartite exact colorings.

Pradhan and Sharma give a full classification for chain graphs. In particular, their chain-graph theorem implies the complete-bipartite endpoint: a complete bipartite graph with both shores of order at least two has proper conflict-free chromatic number \(4\), while stars have value \(3\) and a single edge has value \(2\). The theorem here agrees with that endpoint but extends to every number of partite classes, gives a structural characterization of every proper conflict-free coloring, determines the full color-count spectrum, and supplies an exact surjective-coloring enumeration.

Caro, Petruševski, and Škrekovski determine the parameter for several basic graph classes and establish general bounds, but their announced classes are trees, cycles, hypercubes, and subdivisions of complete graphs. No complete-multipartite structural or counting formula was located in the inspected sources or in targeted database searches.

A nearby published-finding corpus record gives an exact odd-coloring formula for complete multipartite graphs. Odd coloring only requires some neighborhood color to have odd multiplicity, whereas proper conflict-free coloring requires multiplicity exactly one. Neither statement implies the other exact characterization or enumeration used here.

## Limitations

The theorem is restricted to connected complete multipartite graphs and ordinary proper conflict-free coloring. It does not address list assignments, arbitrary cographs, general perfect graphs, or \(h\)-conflict-free colorings with \(h>1\).

The originality assessment is literature-based rather than a proof of global uniqueness. The closest directly relevant full-text result is the chain-graph classification, which covers only the bipartite endpoint and only the minimum number of colors. Poorly indexed or concurrent work could still contain an equivalent multipartite counting statement.

## References

1. X. Qi, H. Song, and Z. Cao, “Proper conflict-free choosability of sparse graphs with girth at least seven,” arXiv:2609.11249v1, first public September 10, 2026. Primary MSC \(05C15\).
2. D. Pradhan and V. Sharma, “Complexity and algorithms for proper conflict-free coloring in graphs,” arXiv:2608.10874v1, August 11, 2026.
3. Y. Caro, M. Petruševski, and R. Škrekovski, “Remarks on proper conflict-free colorings of graphs,” arXiv:2203.01088v1; Discrete Mathematics 346 (2023), 113221.
4. J. Ahn, S. Im, and S.-i. Oum, “The proper conflict-free \(k\)-coloring problem and the odd \(k\)-coloring problem are NP-complete on bipartite graphs,” arXiv:2208.08330v1; Discrete Applied Mathematics 377 (2025), 10–17.
