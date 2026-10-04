# Quadratic reversal distance in the bipermutahedron
## Finding
For every integer \(n\ge 3\), let \(\Pi_{n,n}\) be the bipermutahedron and let
\[
B_n=1\mid2\mid2\mid3\mid3\mid\cdots\mid n\mid n
\]
be the bipermutation whose unique non-repeated letter is \(1\). In the one-skeleton of \(\Pi_{n,n}\),
\[
d\bigl(B_n,\operatorname{rev}(B_n)\bigr)=n^2-1.
\]
For \(n=2\), the corresponding distance is \(2\). Consequently, for every \(n\ge3\),
\[
\operatorname{diam}\bigl(\Pi_{n,n}^{(1)}\bigr)\ge n^2-1.
\]

## Assumptions and scope
A bipermutation of \([n]\) is a word of length \(2n-1\) in which one letter occurs once and every other letter occurs twice. The graph is the one-skeleton determined by Ardila's bipermutahedral adjacency rule: one edge either swaps two adjacent distinct letters, or, when a doubled letter \(i\mid i\) is present and \(k\) is the unique singleton, replaces one copy of \(i\) by a second copy of \(k\), thereby transferring singleton status from \(k\) to \(i\). The result concerns only the displayed canonical reversal pair and the resulting diameter lower bound; it does not assert that \(n^2-1\) is the full diameter.

## Proof
Given a bipermutation \(B\) with singleton \(k\), form its expansion \(E(B)\) by duplicating \(k\) next to itself. Thus \(E(B)\) has length \(2n\) and every letter occurs twice. Under an adjacent-distinct-letter edge, if the swapped pair does not involve the singleton then \(E(B)\) changes by one adjacent swap. If the swap involves the singleton, the adjacent doubled block \(k k\) crosses one copy of the other letter, so \(E(B)\) changes by two adjacent swaps. Under a singleton-transfer edge, \(E(B)\) is unchanged.

Compare expansions with the reversed target. Between \(E(B_n)=11\,22\cdots nn\) and \(E(\operatorname{rev}(B_n))=nn\cdots22\,11\), every pair of distinct labels reverses all four cross-copy orders. Hence the required change in the copy-level inversion count is
\[
4\binom n2=2n(n-1).
\]
Along any path, let \(A_2\) be the number of adjacent-swap edges involving the current singleton, \(A_1\) the number of the other adjacent-swap edges, and \(T\) the number of singleton-transfer edges. Since such edges can change the copy-level inversion count by at most \(2\), \(1\), and \(0\), respectively,
\[
2A_2+A_1\ge2n(n-1),
\]
so the path length \(L=A_1+A_2+T\) satisfies
\[
L\ge n(n-1)+\frac{A_1}{2}+T.
\]

Let \(r\) be the number of labels that are ever singletons on the path and put \(t=n-r\). Every unordered pair of labels that is never a singleton must reverse its four cross-copy orders using ordinary adjacent swaps, so
\[
A_1\ge4\binom t2=2t(t-1).
\]
The singleton starts and ends at label \(1\). If \(r=1\), then \(t=n-1\) and, for \(n\ge3\),
\[
\frac{A_1}{2}\ge(n-1)(n-2)\ge n-1.
\]
If \(r\ge2\), the singleton-label walk starts and ends at \(1\) and visits \(r\) distinct labels, hence \(T\ge r=n-t\). Therefore
\[
\frac{A_1}{2}+T\ge t(t-1)+n-t=n-1+(t-1)^2\ge n-1.
\]
In all cases \(L\ge n^2-1\).

For the matching upper bound, stay inside the words whose doubled labels occur as adjacent blocks. Starting with singleton \(1\), move it right across the blocks \(22,33,\ldots,nn\); crossing one doubled block uses two adjacent-swap edges. Transfer singleton status from \(1\) to \(2\). Next move singleton \(2\) right across \(33,\ldots,nn\), transfer to \(3\), and continue. After moving singleton \(n-1\) across \(nn\), transfer singleton status back to \(1\), using the terminal block \(11\). The block crossings use
\[
2\sum_{j=1}^{n-1}(n-j)=n(n-1)
\]
edges, and for \(n\ge3\) the singleton transfers use \(n-1\) edges. The endpoint is \(nn\mid(n-1)(n-1)\mid\cdots\mid22\mid1=\operatorname{rev}(B_n)\), so the total length is \(n^2-1\). For \(n=2\), two adjacent swaps already reach the reversal.

## Verification
A standalone checker implements the published local edge rule and performs breadth-first search from \(B_n\) to its reversal for \(n=2,3,4,5\), obtaining distances \(2,8,15,24\). It also checks the finite algebraic cases in the lower-bound estimate. These computations corroborate the proof; the infinite statement rests on the argument above, not on finite enumeration.

## Relationship to prior work
Ardila introduced the bipermutahedron, identified its vertices with bipermutations, and gave the exact local one-skeleton adjacency rule used here. The same paper notes that reversal exchanges descents and ascents, but uses this symmetry for the \(h\)-vector rather than for graph distance. Targeted searches for bipermutahedron diameter, shortest paths, reversal distance, and antipodal vertex distance did not locate a statement implying the exact distance above. Nabijou's later work gives a modular interpretation of the bipermutahedral variety; its full text contains no occurrence of “diameter” or “shortest”.

## Limitations
The result determines one natural family of pairwise distances and yields a quadratic diameter lower bound. It does not prove an upper bound for the diameter of the full graph, classify all diametral pairs, or give a general all-pairs distance formula. The literature search cannot exclude terminology not captured by the inspected sources and targeted aliases.

## References
1. Federico Ardila, “The bipermutahedron”, arXiv:2008.02295, first version 5 August 2020; Combinatorial Theory 2(3), 2022, DOI 10.5070/C62359149.
2. Navid Nabijou, “Toric configuration spaces: the bipermutahedron and beyond”, arXiv:2306.03215, first version 5 June 2023; Mathematische Zeitschrift 308 (2024), 57.
