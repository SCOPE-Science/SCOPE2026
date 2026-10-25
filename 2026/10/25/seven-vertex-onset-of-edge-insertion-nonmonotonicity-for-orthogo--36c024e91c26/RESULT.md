# Seven-vertex onset of edge-insertion nonmonotonicity for orthogonal cycle projections

## Finding
For every finite connected simple unweighted graph \(G\) with at most six vertices, and every missing edge \(e\), the Euclidean orthogonal cycle-space projections satisfy
\[
\|C_{G+e}\|_{1\to1}\ge\|C_G\|_{1\to1}.
\]
Here each norm is computed on its own real edge-coordinate space; the added edge changes that space's dimension. This statement is sharp in vertex order: there is a connected graph \(G\) on seven vertices and one added edge \(e\) for which
\[
\|C_G\|_{1\to1}=\frac{313}{153}>\frac{55}{27}=\|C_{G+e}\|_{1\to1},
\qquad \|C_G\|_{1\to1}-\|C_{G+e}\|_{1\to1}=\frac4{459}.
\]
The same statements hold for the induced real \(\ell_\infty\) operator norms because these projections are symmetric matrices. This is a sharp **finite-order** result, not a claim of monotonicity on arbitrary graphs.

## Assumptions and scope
All graphs are finite, connected, simple, unweighted and undirected; every graph edge is given an arbitrary fixed orientation. The real Euclidean structure and the \(\ell_1\) and \(\ell_\infty\) norms use unit edge coordinates. Write \(D\) for the oriented vertex-edge incidence matrix, \(Z(G)=\ker D\) for the real cycle-flow space and \(C_G\) for its Euclidean-orthogonal projection. No optimality over nonorthogonal projections is claimed. The vertex-order threshold is over **all** connected simple graphs, including those with bridges or vertices of degree one.

## Proof
Delete one row of \(D\) to obtain the \((n-1)\times m\) matrix \(B\), where \(n=|V(G)|\), \(m=|E(G)|\). Connectedness implies \(L=BB^{\mathsf T}\) is positive definite. Therefore the cut projection is
\[
Q_G=B^{\mathsf T}L^{-1}B,
\qquad C_G=I_m-Q_G.
\]
Set \(d=\det L>0\) and \(A=\operatorname{adj}(L)\). For each edge \(j\), the complete integer numerators of its cycle-projection column are
\[
 d(C_G)_{ij}=d\,\mathbf1_{i=j}-b_i^{\mathsf T}A b_j,
\qquad
 d\|C_G\|_{1\to1}=\max_j\sum_i\bigl|d\,\mathbf1_{i=j}-b_i^{\mathsf T}A b_j\bigr|,
\]
where \(b_i\) is column \(i\) of \(B\). Thus every comparison of the two rational norms for a graph and its edge augmentation reduces to a comparison of exact nonnegative integers by cross multiplication.

To certify the lower-order assertion **exhaustively**, label the vertices \(0,\ldots,n-1\), encode each of the \(\binom n2\) possible edges by a bit, and run through all \(2^{\binom n2}\) masks for each \(2\le n\le6\). The attached C99 program `verify.c` tests connectivity, forms the exact integer matrix \(L\), evaluates all cofactors by integer determinant expansions, evaluates the displayed maximum, and compares every missing-edge extension. The complete exhaustive enumeration yields:

| \(n\) | Connected labelled graphs | Checked single-edge insertions | Strict decreases in \(\|C\|_{1\to1}\) |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 4 | 3 | 0 |
| 4 | 38 | 84 | 0 |
| 5 | 728 | 3140 | 0 |
| 6 | 26704 | 186360 | 0 |
| **Total** | **27475** | **189587** | **0** |

This algorithm includes every labelled graph and every absent edge; it does not rely on a sample, graph-class restriction, or an unproved assumption that a catalogue contains every isomorphism class. For one vertex the claim is vacuous. This is a finite exhaustive proof because the domain being asserted is finite and the integer arithmetic is exact.

For the upper-order witness, take vertices \(0,1,2,3,4,5,6\) and unordered edges, in this order,
\[
\begin{split}
E(G)=\{&(0,1),(0,4),(1,2),(1,3),(1,4),(1,6),\\
 &(2,3),(3,4),(3,5),(4,5),(5,6)\}.
\end{split}
\]
Add \(e=(1,5)\) to form \(H=G+e\). In this edge order, the exact cycle-projection column-sum vector of \(G\) is
\[
\frac1{153}(233,233,233,313,313,234,233,289,275,275,234),
\]
while in the lexicographically sorted edge order of \(H\) it is
\[
\frac1{243}(369,369,369,495,495,495,369,369,459,459,459,369).
\]
These values follow by inserting the two incidence matrices into the displayed adjugate formula; the respective rooted Laplacian determinants are \(153\) and \(243\). Their maxima are \(313/153\) and \(495/243=55/27\). Direct cross multiplication gives the strict difference \(4/459\). Therefore the first permitted vertex count for a decrease is exactly seven.

Changing an orientation conjugates \(C_G\) by a diagonal sign matrix, and relabelling merely permutes coordinates; neither operation changes its endpoint norms. Symmetry of \(C_G\) also gives \(\|C_G\|_{1\to1}=\|C_G\|_{\infty\to\infty}\).

## Verification
Compile `verify.c` with `cc -O2 -std=c99 -Wall -Wextra verify.c -o verify` and execute `./verify`. It uses only the C standard library and 64-bit signed integer arithmetic. It prints the five exact enumeration counts above, reproduces both witness norms and exits successfully only if no cycle-norm decrease occurs before seven vertices and the seven-vertex strict decrease matches the stated fractions. The graph sizes here keep intermediate integer values well below signed 64-bit limits. A separate exact-rational reconstruction using symbolic graph Laplacians checked all 142 connected unlabelled graph classes through six vertices and their 821 distinct augmentation cases; this is a corroborating calculation, not the basis of exhaustiveness.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) establish the graph cycle/cut projection framework and study minimal or invariant projections, especially on discrete tori and Hamming graphs. Their general incidence setup supplies background, but their stated classifications do not give the present sharp edge-insertion onset. The present result concerns the **canonical Euclidean-orthogonal** projector, not the minimum over all projections. The known Rayleigh monotonicity of effective resistance under edge addition does not entail monotonicity of the absolute column sums of the cycle projector. Other explicit graph-family projection formulas cover special highly structured graphs but do not prove this universal small-order boundary.

## Limitations
The threshold is for unit-conductance simple connected graphs and one newly inserted edge; it does not address weighted insertions, vertex additions, deletions, or minimal nonorthogonal cycle projections. It does not enumerate or classify all seven-vertex counterexamples, or determine the maximum possible magnitude of a decrease. The negative part uses transparent exact exhaustive finite enumeration rather than a short hand-derived structural characterization. The claim has not been independently mathematically audited; bibliographic completeness cannot be guaranteed.

## References
- S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public version 2023-05-21, https://arxiv.org/abs/2305.12582.
