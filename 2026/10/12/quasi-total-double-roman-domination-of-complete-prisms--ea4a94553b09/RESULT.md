# Quasi-total double Roman domination of complete prisms
## Finding
For every integer \(n\ge4\), let
\[
P_n^{\mathrm{cl}}=K_n\square K_2
\]
be the complete prism. Write its two clique layers as
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
with the additional matching edges \(a_i b_i\).

Then
\[
\gamma_{qtdR}(P_n^{\mathrm{cl}})=6.
\]

More strongly, every minimum quasi-total double Roman dominating function has the same form: for a unique
\[
i\in\{1,\ldots,n\},
\]
assign
\[
f(a_i)=f(b_i)=3
\]
and assign \(0\) to every other vertex. Hence \(P_n^{\mathrm{cl}}\) has exactly
\[
n
\]
minimum functions.

## Assumptions and scope
A quasi-total double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
satisfying three conditions.

First, every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\). Second, every vertex labeled \(1\) has a neighbor whose label is at least \(2\). Third, if a positive-labeled vertex is isolated in the subgraph induced by the positive support, then its label must be \(2\).

The weight is
\[
\omega(f)=\sum_{v\in V(G)} f(v),
\]
and \(\gamma_{qtdR}(G)\) is the minimum weight.

The classification theorem is stated for \(n\ge4\). The boundary \(n=2\) is the cycle \(C_4\), already covered by the published cycle formula. For \(n=3\), the minimum value is also \(6\), but additional minimum functions occur.

## Proof
For a function \(f\) on \(P_n^{\mathrm{cl}}\), let
\[
W_A=\sum_{a\in A}f(a),\qquad W_B=\sum_{b\in B}f(b).
\]

We first prove that any quasi-total double Roman dominating function of total weight at most \(6\) must satisfy
\[
W_A\ge3,\qquad W_B\ge3.
\tag{1}
\]

Suppose \(W_A\le2\). If \(A\) contains no vertex labeled \(2\), then it contains no label \(3\) either. Since \(n\ge4\), at least two vertices of \(A\) are labeled \(0\). Such a zero has no same-layer neighbor labeled \(2\) or \(3\), and its only neighbor in \(B\) is its matched vertex. Therefore each such zero requires its own matched vertex in \(B\) to carry label \(3\). If \(W_A>0\), two such forced labels already give total weight greater than \(6\); if \(W_A=0\), all \(n\) matched vertices in \(B\) would have to carry label \(3\).

The remaining possibility with \(W_A\le2\) is that \(A\) contains one vertex labeled \(2\), so \(W_A=2\). Every other vertex of \(A\) is zero. Each of those \(n-1\) zeros sees the single label \(2\) inside \(A\), and therefore its matched vertex in \(B\) must have label at least \(2\) to provide either a second label \(2\) or a label \(3\). Thus
\[
W_B\ge2(n-1)\ge6,
\]
again making total weight exceed \(6\). This proves \(W_A\ge3\), and symmetry gives \(W_B\ge3\).

Now choose any index \(i\) and set
\[
f(a_i)=f(b_i)=3,
\]
with every other label zero. Every zero in \(A\) sees \(a_i\), every zero in \(B\) sees \(b_i\), and the two positive vertices are adjacent through the matching edge. Hence this is a valid function of weight \(6\). Together with (1),
\[
\gamma_{qtdR}(P_n^{\mathrm{cl}})=6.
\]

It remains to classify equality. Let \(f\) have weight \(6\). Equation (1) forces
\[
W_A=W_B=3.
\tag{2}
\]

Consider the possible label multisets in \(A\).

If \(A\) contains labels \(2\) and \(1\), then its other \(n-2\) vertices are zero. Every such zero sees only one label \(2\) in its own clique, so its matched vertex in \(B\) must have label at least \(2\). Hence
\[
W_B\ge2(n-2)>3,
\]
contradicting (2).

If \(A\) contains three labels \(1\), then for \(n\ge5\) at least two zeros in \(A\) each require their distinct matched vertices in \(B\) to have label \(3\), impossible because \(W_B=3\). When \(n=4\), the unique zero in \(A\) forces its matched vertex in \(B\) to have label \(3\), so that vertex is the only positive vertex in \(B\). Each of the three vertices labeled \(1\) in \(A\) then has no neighbor with label at least \(2\), again impossible.

Therefore \(A\) consists of one label \(3\) and \(n-1\) zeros. By symmetry, the same is true of \(B\). The positive support thus consists of one vertex of \(A\) and one vertex of \(B\), both labeled \(3\). A positive isolated vertex may not carry label \(3\), so these two vertices must be adjacent. Across the two clique layers, adjacency occurs exactly along the matching. Hence the two labels \(3\) must be \(a_i\) and \(b_i\) for the same unique index \(i\).

Conversely, each of these \(n\) matched choices is valid, completing the classification.

## Verification
The included checker constructs \(K_n\square K_2\) directly and evaluates the three defining conditions without using the theorem.

It exhaustively checks every labeling for \(n=3,4,5\), totaling
\[
4^6+4^8+4^{10}=1{,}118{,}208
\]
labelings. It obtains minimum value \(6\) in all three cases. For \(n=4\) and \(n=5\), every minimum function is exactly a matched pair of labels \(3\), giving \(4\) and \(5\) minima respectively. The checker also confirms that \(n=3\) has \(15\) minima, which is why the structural classification is stated from \(n=4\).

As an additional construction check, all \(n\) claimed minimum functions are tested directly for every
\[
4\le n\le50.
\]

## Relationship to prior work
Kosari, Babaei, Amjadi, Chellali, and Sheikholeslami introduced quasi-total double Roman domination and determined exact values for paths and cycles, characterized graphs with values \(3\), \(4\), and \(5\), obtained an exact complete-multipartite result, and proved general upper bounds. Their complete-multipartite theorem does not apply to \(K_n\square K_2\): for \(n\ge3\), nonadjacency across the two layers is not an equivalence relation, so the graph is not complete multipartite.

The small-value characterization is consistent with the lower bound here but does not give the equality structure at value \(6\). The general maximum-degree bound applied to the complete prism gives only
\[
\gamma_{qtdR}(K_n\square K_2)\le 2n+2,
\]
and the connected-graph bound gives a quantity growing linearly with \(n\); neither implies the constant value \(6\) or the exact optimizer count.

A later paper studies stability of the same parameter and reuses the known path, cycle, and values-\(3\)-through-\(5\) results. Targeted searches using “complete prism”, “prism graph”, “Cartesian product”, and \(K_n\square K_2\) formulations did not locate a published exact quasi-total double Roman theorem for this family.

## Limitations
The optimizer classification begins at \(n=4\). For \(n=3\), the value remains \(6\) but there are additional optimal label patterns; for \(n=2\), the graph is \(C_4\) and belongs to the previously solved cycle family.

The theorem concerns the complete prism \(K_n\square K_2\), not arbitrary prism graphs \(C_n\square K_2\) or arbitrary Cartesian products.

Finite exhaustive computation is corroborative only. The all-\(n\) value and optimizer classification follow from the layer-weight proof.

Search coverage cannot rule out a differently phrased or non-indexed treatment of the same family.

## References
1. S. Kosari, S. Babaei, J. Amjadi, M. Chellali, S. M. Sheikholeslami, “Quasi total double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 21(2) (2024), 171–180, DOI 10.1080/09728600.2024.2315275; published online 26 February 2024.
2. S. Kosari, H. Jiang, M. Esmaeili, “Quasi total double Roman domination stability in graphs,” AKCE International Journal of Graphs and Combinatorics (2026), DOI 10.1080/09728600.2025.2604085; published online 9 January 2026.
