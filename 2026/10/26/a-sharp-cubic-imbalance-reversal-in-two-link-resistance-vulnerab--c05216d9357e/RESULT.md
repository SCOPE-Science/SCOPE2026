# A sharp cubic-imbalance reversal in two-link resistance vulnerability of complete bipartite networks

## Finding

Let \(G=K_{p,q}\) have unit edge conductances, with integers \(p\ge q\ge3\). For a pair \(F\) of distinct edges define its Kirchhoff-index damage by
\[
\Delta(F)=\operatorname{Kf}(G-F)-\operatorname{Kf}(G),\qquad
\operatorname{Kf}(H)=\sum_{\{u,v\}\subseteq V(H)}R_H(u,v).
\]
There are exactly three isomorphism types of unordered two-edge sets: \(A\), where the edges meet at a vertex in the \(p\)-vertex part (degree \(q\)); \(B\), where they meet in the \(q\)-vertex part (degree \(p\)); and \(D\), where they are vertex-disjoint. Their damages, denoted \(\Delta_A,\Delta_B,\Delta_D\), satisfy the **complete sharp ranking**:

* If \(p=q\), then \(\Delta_A=\Delta_B>\Delta_D\).
* If \(q<p<q(q-1)^2\), then \(\Delta_A>\Delta_B>\Delta_D\).
* If \(p\ge q(q-1)^2\), then \(\Delta_A>\Delta_D>\Delta_B\).

All inequalities are strict in the stated ranges. No integer \(p\ge q\ge3\) yields a tie between type \(B\) and type \(D\). The real crossover is the unique root greater than \(q\) of the cubic
\[
H_q(z)=z^3-\bigl(q^2(q-2)+2\bigr)z^2-q^2(q-2)^2z+q^2(q-1)(q-2),
\]
which lies strictly between \(q(q-1)^2-1\) and \(q(q-1)^2\). Thus a pair sharing a **high-degree** endpoint eventually causes **less** Kirchhoff damage than two disjoint failures, although all two-edge damage interactions are strictly superadditive.

The damage-maximizing pairs are exactly the \(p\binom q2\) type-\(A\) pairs if \(p>q\). In the balanced case all \(2p\binom p2\) incident-edge pairs maximize. For \(p>q\), the minimum-damage type is \(D\) below the cubic threshold, with exactly \(2\binom p2\binom q2\) minimizing pairs, and \(B\) at and above it, with exactly \(q\binom p2\) minimizing pairs. At the crossover no discrete tie occurs. For example, on \(K_{11,3}\) the excess of type \(B\) damage over type \(D\) damage is exactly \(3/1463\), while on \(K_{12,3}\) type \(D\) exceeds type \(B\) by \(3/3220\).

## Assumptions and scope

All graphs are finite, undirected, simple, unit-conductance complete bipartite graphs with part sizes \(p\ge q\ge3\). All effective resistances use edge resistance one. Every two-edge deletion remains connected because the edge-connectivity of \(K_{p,q}\) equals \(q\ge3\). The comparison concerns exactly two *distinct* edges, not a general number of deletions or weighted heterogeneous bipartite graphs. Vertex labels within each part are interchangeable.

For a single edge write \(S=\operatorname{Kf}(G-e)-\operatorname{Kf}(G)\). Exact closed forms for the incident classes are
\[
\Delta_A=\frac{2(p^3+p^2q-p^2+pq^2-2pq+q^3-2q^2)}{pq(p-1)(q-2)},
\]
\[
\Delta_B=\frac{2(p^3+p^2q-2p^2+pq^2-2pq+q^3-q^2)}{pq(p-2)(q-1)}.
\]
The disjoint class and all other values are given by the compact rational trace formula in the proof. No numerical approximation is needed to decide the optimal class.

## Proof

Write \(N=p+q\) and let \(L\) be the graph Laplacian. Its nonzero eigenspaces are the within-first-part contrasts (eigenvalue \(q\)), within-second-part contrasts (eigenvalue \(p\)), and the between-part contrast (eigenvalue \(N\)). Denote the orthogonal projectors by \(P_A,P_B,P_C\). Then
\[
L^+=\frac{P_A}{q}+\frac{P_B}{p}+\frac{P_C}{N},\qquad
(L^+)^2=\frac{P_A}{q^2}+\frac{P_B}{p^2}+\frac{P_C}{N^2}.
\]
Orient every edge from the first part to the second. For oriented incidence vectors \(b_e,b_f\), define \(r=b_e^TL^+b_e\), \(k=b_e^T(L^+)^2b_e\), \(c=b_e^TL^+b_f\), and \(d=b_e^T(L^+)^2b_f\). Projector evaluation gives
\[
r=\frac{p+q-1}{pq},\quad
k=\frac{p-1}{pq^2}+\frac{q-1}{qp^2}+\frac1{Npq}.
\]
For types \(A,B,D\), respectively, the remaining pair data are
\[
\begin{aligned}
(c_A,d_A)&=\left(\frac{p-1}{pq},\frac{p-1}{pq^2}-\frac1{qp^2}+\frac1{Npq}\right),\\
(c_B,d_B)&=\left(\frac{q-1}{pq},-\frac1{pq^2}+\frac{q-1}{qp^2}+\frac1{Npq}\right),\\
(c_D,d_D)&=\left(-\frac1{pq},-\frac1{pq^2}-\frac1{qp^2}+\frac1{Npq}\right).
\end{aligned}
\]
For the two incidence vectors arranged as columns of \(B\), the rank-two inverse identity on \(\mathbf1^\perp\) gives
\[
\Delta(F)=N\operatorname{tr}\left[(I-B^TL^+B)^{-1}B^T(L^+)^2B\right]
=\frac{2N\bigl(k(1-r)+cd\bigr)}{(1-r)^2-c^2}.
\]
All denominators are positive when \(p,q\ge3\), as also follows from connectedness after deleting the two edges. A single deletion has \(S=Nk/(1-r)\). Substituting the three \((c,d)\) pairs produces the displayed formulas for \(\Delta_A,\Delta_B\) and a fully explicit computable expression for \(\Delta_D\).

The exact interaction terms \(\Delta_X-2S\) are
\[
\begin{aligned}
\Delta_A-2S&=\frac{2p(N-1)}{q(p-1)(q-2)(q-1)},\\
\Delta_B-2S&=\frac{2q(N-1)}{p(p-2)(p-1)(q-1)},\\
\Delta_D-2S&=\frac{2(p^2+pq-p+q^2-q)}{(p-1)(q-1)(pq-p-q)(pq-p-q+2)}.
\end{aligned}
\]
Each is strictly positive. Direct cancellation gives
\[
\Delta_A-\Delta_B=\frac{2(p-q)(N-1)(p^2+pq-2p+q^2-2q)}{pq(p-2)(p-1)(q-2)(q-1)}.
\]
Thus \(\Delta_A>\Delta_B\) if \(p>q\), with equality if and only if \(p=q\).

For \(\Delta_A-\Delta_D\), put \(u=p-q\ge0\). Its denominator is the strictly positive expression \(q(p-1)(q-2)(pq-p-q)(pq-p-q+2)\), and its numerator equals
\[
2\bigl[(q-1)u^4+(q-1)(5q-3)u^3+(q-1)^2(9q-2)u^2
+q(q-1)(7q^2-13q+4)u+q^3(q-2)(2q-3)\bigr].
\]
All coefficients are strictly positive for \(q\ge3\); hence \(\Delta_A>\Delta_D\).

Finally,
\[
\Delta_B-\Delta_D=
-\frac{2H_q(p)}{p(p-2)(q-1)(pq-p-q)(pq-p-q+2)}.
\]
The cubic has signs \(+,-,-,+\) for its coefficients in descending degree, so it has at most two positive roots by Descartes' rule. Since \(H_q(0)>0\), \(H_q(q)=-q^3(q-2)(2q-3)<0\), and \(H_q(z)\to+\infty\), there is exactly one positive root below \(q\) and one above \(q\), both simple. Put \(T=q(q-1)^2\). Then
\[
H_q(T)=q^3(q-2)(q-1)>0.
\]
Writing \(v=q-3\ge0\), exact substitution yields
\[
-H_q(T-1)=v^6+13v^5+70v^4+198v^3+308v^2+248v+81>0.
\]
The sole root above \(q\) is therefore in \((T-1,T)\). As \(p\) is integer, \(H_q(p)<0\) for \(q\le p\le T-1\) and \(H_q(p)>0\) for \(p\ge T\). Together with the first two strict comparisons this proves the complete ranking and counts.

## Verification

The standalone `verification/check.py` script requires SymPy (`verification/requirements.txt`). From the package root run `python verification/check.py`. It checks every displayed rational identity symbolically, the positive-coefficient expression and cubic bracketing identities, 100 direct rational Kirchhoff-index computations on complete bipartite graphs with both part sizes from three to seven (each comparison independently inverts \(L+\mathbf1\mathbf1^T/N\)), and 52 exact large-imbalance sign checks. These finite checks corroborate, but do not replace, the all-integer proof above.

## Relationship to prior work

Yang's open-access 2012 paper proves that \(K_{p,q}\) has minimal Kirchhoff index among bipartite graphs with its fixed part sizes; that global fact alone does not distinguish which two missing edges cause greater resistance damage. Ge and Dong's 2019 complete-bipartite resistance paper computes the Kirchhoff index after deleting an arbitrary *matching* and therefore covers the disjoint-pair damage as a special case, not the incident-pair formulas or the size-dependent reversal between an incident and a disjoint pair. The 2020 Jiang–He–Liu–Li work considers diameter-restricted global extrema; available source descriptions do not resolve these fixed-part-size pairwise comparisons, although its inaccessible complete text is a residual coverage risk.

The mathematical contribution claimed here is the **sharp three-class two-link damage ordering, strictly positive interactions, and exact cubic-to-integer phase boundary**, not the known Kirchhoff index of \(K_{p,q}\), the known disjoint-pair case, or the rank-two inverse identity by itself.

## Limitations

The classification requires both parts to have at least three vertices and all conductances to equal one. No claim is made for edge failures of size three or more, arbitrary bipartite graphs, or edge-weight heterogeneity. The disjoint-pair Kirchhoff expression is already covered by the matching-deletion literature; the strict ordering and incident-versus-disjoint reversal are the distinct conclusions assessed here. Historical mathematical-literature coverage may be incomplete; independent review has not been performed.

## References

1. Y. Yang, “Bounds for the Kirchhoff Index of Bipartite Graphs,” *Journal of Applied Mathematics* (first published 23 April 2012), DOI: `10.1155/2012/195242`.
2. J. Ge and F. Dong, “Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs,” arXiv:`1904.07766` (first posted 16 April 2019), especially §5.3 on matching deletion.
3. X. Jiang, W. He, Q. Liu, and J. Li, “On the Kirchhoff index of bipartite graphs with given diameters,” *Discrete Applied Mathematics* **283** (2020), 512–521, DOI: `10.1016/j.dam.2020.01.035` (full text not inspected).
