# Minimum quasi-total Italian functions of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency rule
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{I*}(H_n)=
\begin{cases}
3,&n=2,\\
4,&n\ge3.
\end{cases}
\]

The minimum quasi-total Italian dominating functions are completely classified. We write a labeling as
\[
(f(a_1),\ldots,f(a_n);f(b_1),\ldots,f(b_n)).
\]

For \(n=2\), the two minimum functions are
\[
(0,1;1,1),\qquad (1,1;1,0).
\]

For \(n=3\), the four minimum functions are
\[
(0,0,1;1,1,1),
\]
\[
(0,1,1;1,1,0),
\]
\[
(1,1,1;1,0,0),
\]
and
\[
(2,0,0;0,0,2).
\]

For every \(n\ge4\), the minimum function is unique:
\[
(2,0,\ldots,0;0,\ldots,0,2).
\]
Thus the two universal opposite-side vertices \(a_1\) and \(b_n\) are the unique optimal defenders once the half graph has at least eight vertices.

The published Gallai identity
\[
\gamma_{I*}(G)+\partial_s^*(G)=|V(G)|
\]
then gives
\[
\partial_s^*(H_2)=1
\]
and
\[
\partial_s^*(H_n)=2n-4\qquad(n\ge3).
\]

## Assumptions and scope
A quasi-total Italian dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2,
\]
and every vertex \(v\) with \(f(v)=2\) has a positive-labeled neighbor.

The weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{I*}(G)\) is the minimum possible weight.

In \(H_n\), the vertices \(b_1\) and \(a_n\) are leaves, adjacent only to \(a_1\) and \(b_n\), respectively.

## Proof
First assume \(n\ge3\). We prove that no quasi-total Italian dominating function has weight at most \(3\).

If \(f(b_1)=0\), then its only neighbor \(a_1\) must have label \(2\). Quasi-totality then forces some positive vertex in \(B\). If also \(f(a_n)=0\), then the only neighbor \(b_n\) must have label \(2\), already giving weight at least \(4\). Hence \(f(a_n)>0\), but then the label \(2\) at \(a_1\), a positive vertex in \(B\), and \(a_n\) again force weight at least \(4\). Therefore \(f(b_1)>0\). By symmetry, \(f(a_n)>0\).

If \(f(b_1)=2\), quasi-totality forces \(f(a_1)>0\), and together with \(f(a_n)>0\) the weight is at least \(4\). Thus a weight-at-most-\(3\) function must have
\[
f(b_1)=f(a_n)=1.
\]
Only one additional unit of weight remains. The vertex \(a_{n-1}\) cannot be zero, because its neighborhood is contained in
\[
\{b_{n-1},b_n\},
\]
which contains at most one unit of positive weight. Hence \(f(a_{n-1})=1\). Now \(b_2\) is zero, but
\[
N(b_2)=\{a_1,a_2\}
\]
contains at most one unit of positive weight, a contradiction. Therefore
\[
\gamma_{I*}(H_n)\ge4.
\]
The labeling
\[
f(a_1)=f(b_n)=2
\]
with every other label zero is feasible, because \(a_1b_n\) is an edge and every zero sees one of these two defenders. Hence
\[
\gamma_{I*}(H_n)=4
\]
for \(n\ge3\).

We now classify the weight-\(4\) functions for \(n\ge4\).

Suppose first that \(f(b_1)=0\). Then \(f(a_1)=2\). If \(f(a_n)=0\), then \(f(b_n)=2\), and the weight is exhausted, giving the displayed extreme-defender function. If instead \(f(a_n)>0\), then quasi-totality of \(a_1\) forces a positive vertex in \(B\). Weight \(4\) then forces \(f(a_n)=1\), exactly one unit label in \(B\), and all other vertices zero. Since \(n\ge4\), the zero vertex \(a_2\) sees at most one unit of weight in \(B\), contradicting the Italian condition. Thus \(f(b_1)=0\) forces the extreme-defender function. By symmetry, the same is true if \(f(a_n)=0\).

It remains to consider
\[
f(b_1)>0,\qquad f(a_n)>0.
\]
If either leaf has label \(2\), say \(f(b_1)=2\), then quasi-totality forces \(f(a_1)>0\). Weight \(4\) leaves no positive vertex in \(B\setminus\{b_1\}\), so the zero vertex \(a_2\) is undefended. Hence
\[
f(b_1)=f(a_n)=1.
\]

Two units of weight remain. If they form a single label \(2\), then that label lies in one bipartition class. The opposite class has no positive vertex except the leaf already labeled \(1\). Because \(n\ge4\), one can choose an internal zero vertex whose neighborhood avoids that leaf, so the Italian condition fails.

The final possibility is two additional labels \(1\). If \(a_{n-1}=0\), then both \(b_{n-1}\) and \(b_n\) must receive those two labels, after which \(b_2\) has insufficient positive weight in its neighborhood. Therefore \(a_{n-1}=1\). Symmetrically \(b_2=1\). These are the two remaining unit labels. Now \(a_{n-2}\) has neighborhood weight at most \(1\): for \(n=4\) it sees \(b_2\) but no second positive vertex, and for \(n>4\) it does not even see \(b_2\). This is again impossible. Hence the extreme-defender function is unique for every \(n\ge4\).

For \(n=3\), the same argument reduces weight \(4\) to the following finite cases. If a leaf is zero, the extreme-defender function is forced. If both leaves are positive, neither can have label \(2\), so both have label \(1\). A remaining label \(2\) is impossible because its opposite-side support pattern leaves an internal zero insufficiently defended. Thus the remaining weight consists of two labels \(1\). If \(a_2=0\), both \(b_2,b_3\) must be labeled \(1\); if \(a_2=1\) and \(b_2=0\), then \(a_1=1\); and if \(a_2=b_2=1\), no weight remains. These are exactly the three all-\(1\) patterns displayed above, together with the extreme-defender function.

Finally, \(H_2\cong P_4\). A weight-\(2\) quasi-total Italian function is impossible. At weight \(3\), any label \(2\) would require positive support and leave one of the two leaves or its neighbor insufficiently defended. Hence all three units must be labels \(1\), and the unique zero must be one of the two degree-\(2\) vertices. This gives exactly the two displayed functions.

The quasi-total strong differential formulas follow immediately from the published Gallai identity and \(|V(H_n)|=2n\).

## Verification
The included checker constructs \(H_n\) directly for
\[
2\le n\le7
\]
and enumerates every map to \(\{0,1,2\}\). It tests both the Italian neighborhood-sum condition at every zero and the quasi-total positive-neighbor condition at every label-\(2\) vertex.

It independently compares the minimum weight and the complete minimum-function list with the theorem.

## Relationship to prior work
Quasi-total Italian domination was introduced in 2021 through the quasi-total strong differential. The introducing paper proves the Gallai identity
\[
\gamma_{I*}(G)+\partial_s^*(G)=|V(G)|
\]
and general bounds, but it does not give a half-graph or chain-graph computation in the inspected text.

A later \(w\)-domination treatment identifies quasi-total Italian domination with the vector
\[
(2,0,1)
\]
and places it in Mathematics Subject Classification \(05C69\). That paper studies lexicographic-product reductions and contains no half-graph or chain-graph occurrence in the inspected full text.

The 2020 chain-graph algorithm for Roman \(\{2\}\)-domination concerns ordinary Italian domination, without the requirement that every label-\(2\) vertex have a positive neighbor. It therefore does not classify the quasi-total Italian optima above.

The new content is the exact quasi-total Italian minimum-function classification on the canonical twin-free chain family, including the uniqueness threshold at \(n=4\), together with the resulting exact quasi-total strong differential.

## Limitations
The theorem classifies minimum quasi-total Italian functions, not all feasible functions of higher weight.

The boundary cases \(n=2\) and \(n=3\) have exceptional optimizer multiplicities; uniqueness begins at \(n=4\).

The exhaustive computation through \(n=7\) is corroborative only. The arbitrary-\(n\) uniqueness statement follows from the leaf and nested-neighborhood argument in the proof.

A differently phrased or non-indexed half-graph result may exist despite the targeted searches.

## References
1. A. Cabrera Martínez, A. Estrada-Moreno, J. A. Rodríguez-Velázquez, “From the Quasi-Total Strong Differential to Quasi-Total Italian Domination in Graphs,” Symmetry 13 (2021), 1036, DOI 10.3390/sym13061036, published 8 June 2021.
2. A. Cabrera-Martínez, L. P. Montejano, J. A. Rodríguez-Velázquez, “From \(w\)-Domination in Graphs to Domination Parameters in Lexicographic Product Graphs,” Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), 109, DOI 10.1007/s40840-023-01502-5.
3. H. Jiang, Z. Shao, “Complexity of Roman \(\{2\}\)-domination and the double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 777–782, DOI 10.1016/j.akcej.2020.01.005.
