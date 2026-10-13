# Weighted Roman domination of crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) for \(n\ge3\), with bipartition \(A_0=\{a_1,\ldots,a_n\}\), \(B_0=\{b_1,\ldots,b_n\}\), and deleted matching \(a_i b_i\). Give the vertices arbitrary positive real weights \(\alpha_i=w(a_i)\) and \(\beta_i=w(b_i)\). Write
\[
A=\sum_i\alpha_i,\qquad B=\sum_i\beta_i,
\]
\[
P_A=\min_{i<j}(\alpha_i+\alpha_j),\qquad P_B=\min_{i<j}(\beta_i+\beta_j).
\]
Define
\[
C_{20}=A+P_A,\qquad C_{02}=B+P_B,
\]
\[
C_{11}=\min_{i,j}\left(2\alpha_i+2\beta_j+\mathbf 1_{i\ne j}(\alpha_j+\beta_i)\right),
\]
\[
C_{21}=\min_{i<j,\,k}\left(2\alpha_i+2\alpha_j+2\beta_k+\mathbf 1_{k\notin\{i,j\}}\alpha_k\right),
\]
\[
C_{12}=\min_{i<j,\,k}\left(2\beta_i+2\beta_j+2\alpha_k+\mathbf 1_{k\notin\{i,j\}}\beta_k\right),
\]
\[
C_{22}=2(P_A+P_B).
\]
Then
\[
\gamma_{wR}(\operatorname{Cr}_n;w)=\min\{C_{20},C_{02},C_{11},C_{21},C_{12},C_{22}\}.
\]
Here \(\gamma_{wR}\) minimizes \(\sum_v f(v)w(v)\) over Roman dominating functions \(f:V\to\{0,1,2\}\), where every vertex labeled \(0\) has a neighbor labeled \(2\).

## Assumptions and scope
The graph is finite and simple, \(n\ge3\), and every vertex weight is a positive real number. No symmetry, integrality, normalization, or equality of weights is assumed. The formula concerns ordinary weighted Roman domination, not Roman \(\{2\}\)-domination, strong Roman domination, or signed variants.

## Proof
Let \(T_A=\{i:f(a_i)=2\}\) and \(T_B=\{i:f(b_i)=2\}\), and put \(p=|T_A|\), \(q=|T_B|\). Once \(T_A,T_B\) are fixed, positivity of the vertex weights forces every remaining label to be as small as feasibility permits.

For a vertex \(a_i\), a label \(0\) is feasible exactly when there is a \(j\in T_B\) with \(j\ne i\). Hence if \(q=0\), every \(a_i\notin T_A\) must carry label \(1\); if \(q=1\), say \(T_B=\{j\}\), then only \(a_j\) is forced to be nonzero; and if \(q\ge2\), every \(a_i\notin T_A\) may be labeled \(0\). The symmetric statement holds on \(B_0\) with \(p\) in place of \(q\).

An optimum has \(p,q\le2\). Indeed, if \(p\ge3\), changing any one label \(2\) on \(A_0\) to the smallest label allowed by the preceding rule preserves feasibility: at least two label-\(2\) vertices remain on \(A_0\), so every zero on \(B_0\) still has a label-\(2\) neighbor. Because weights are positive, the cost strictly decreases. The same argument applies to \(q\).

The types \((0,0)\), \((1,0)\), and \((0,1)\) cannot be optimal. Type \((0,0)\) has cost \(A+B\), while choosing a matched pair \(a_i,b_i\) and labeling both by \(2\) gives a feasible function of cost \(2(\alpha_i+\beta_i)\). Since \(n\ge3\), some \(i\) satisfies \(2(\alpha_i+\beta_i)<A+B\). For type \((1,0)\) with the sole label \(2\) at \(a_i\), the forced cost is \(A+\alpha_i+\beta_i\). If \(\alpha_i+\beta_i\le A\), the matched-pair construction at index \(i\) costs at most this much; if \(\alpha_i+\beta_i>A\), then \(P_A<A\) and the type \((2,0)\) construction costs \(A+P_A<A+\alpha_i+\beta_i\). The type \((0,1)\) case is symmetric.

It remains to evaluate the six possible optimum types. For \((2,0)\), two vertices on \(A_0\) carry label \(2\), all other vertices of \(A_0\) carry label \(1\), and all vertices of \(B_0\) carry label \(0\), giving \(C_{20}\); \((0,2)\) gives \(C_{02}\). For \((1,1)\), label \(2\) at \(a_i\) and \(b_j\) forces the extra labels \(1\) at \(a_j\) and \(b_i\) exactly when \(i\ne j\), giving \(C_{11}\). For \((2,1)\), label \(2\) at \(a_i,a_j,b_k\); the only possible extra label \(1\) is at \(a_k\), and it is needed exactly when \(k\notin\{i,j\}\), giving \(C_{21}\). The case \((1,2)\) is symmetric and gives \(C_{12}\). Finally, type \((2,2)\) needs no label \(1\), so independent cheapest pairs on the two shores give \(C_{22}\). Taking the minimum proves the formula.

## Verification
The bundled checker evaluates the six-term formula and independently enumerates every labeling in \(\{0,1,2\}^{2n}\). It exhausts every weight assignment in \(\{1,2,3\}^6\) for \(n=3\), then checks fixed-seed integer-weight profiles for \(n=4,5\), including profiles chosen so that each nontrivial type can be optimal. This computation is a stress test only; the theorem for arbitrary positive real weights and all \(n\ge3\) follows from the proof above.

## Relationship to prior work
Cera, García-Vázquez, and Valenzuela-Tripodoro introduced the weighted Roman domination number for positive real vertex weights and, in Proposition 4.2 of their 2025 preprint, obtained an exact formula for weighted complete bipartite graphs. Their inspected paper explicitly states that its exact-family section treats complete graphs and complete bipartite graphs and gives cycle bounds; searches of the full text found no occurrence of “crown” or “matching”. The present result treats the canonical matching-deleted biclique \(K_{n,n}-M_n\), where the missing matched neighbor creates six genuinely competing support types rather than the three strategies of the complete-bipartite formula.

Earlier weighted \((a,b)\)-Roman domination algorithms on strongly chordal graphs do not subsume this family: every \(\operatorname{Cr}_n\) with \(n\ge3\) contains the induced subgraph \(\operatorname{Cr}_3=C_6\), and therefore is not chordal. Unweighted Roman-domination formulas or enumerators likewise do not determine the minimum under arbitrary nonuniform vertex costs.

## Limitations
The formula is specific to crowns and positive vertex weights. It does not claim an analogous six-type reduction for arbitrary matching-deleted unbalanced bicliques, for zero or negative vertex weights, or for other Roman variants. The finite checker does not certify the infinite statement; it only corroborates the analytic case split. A poorly indexed exact weighted-crown result under another graph-family name remains a residual literature risk.

## References
1. M. Cera, P. García-Vázquez, J. C. Valenzuela-Tripodoro, “Roman domination in weighted graphs,” arXiv:2512.22622v1, first posted 2025-12-27; later published in *Mathematics* 14 (2026), 466, DOI:10.3390/math14030466.
2. C.-H. Liu, G. J. Chang, “Roman domination on strongly chordal graphs,” *Journal of Combinatorial Optimization* 26 (2013), 608–619, DOI:10.1007/s10878-012-9482-y.
3. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, S. T. Hedetniemi, “Roman domination in graphs,” *Discrete Mathematics* 278 (2004), 11–22, DOI:10.1016/j.disc.2003.06.004.
