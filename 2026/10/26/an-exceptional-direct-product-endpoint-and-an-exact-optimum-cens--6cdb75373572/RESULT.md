# An exceptional direct-product endpoint and an exact optimum census for outer-independent total Roman domination

## Finding

Write \(H_{r,s}=K_r\times K_s\) for the **direct (categorical) product** of two complete graphs, with integers \(2\le r\le s\). Its vertices are the ordered pairs \((i,j)\), and two distinct vertices are adjacent exactly when **both** coordinates differ. An outer-independent total Roman dominating function, abbreviated OITRDF, is a map \(f:V(H_{r,s})\to\{0,1,2\}\) whose zero set is independent, each zero has a neighbor labeled \(2\), and each positive vertex has a positive neighbor. Let \(\gamma_{\mathrm{oitR}}\) be its minimum weight and \(M_{r,s}\) the number of minimum-weight functions on this *labeled* graph.

**Theorem.** The corrected exact value is

\[
\gamma_{\mathrm{oitR}}(H_{r,s})=
\begin{cases}
4,&r=s=2,\\
s+3,&r=2,\ s\ge3,\\
s(r-1)+2,&3\le r\le s.
\end{cases}
\]

Every optimum is classified in the proof, and its precise census is

\[
M_{r,s}=
\begin{cases}
1,&r=s=2,\\
25,&r=2,\ s=3,\\
2s(s-1),&r=2,\ s\ge4,\\
(1+\mathbf{1}_{\{r=s\}})r\left[\binom{(r-1)s}{2}-s\binom{r-1}{2}+s(r-1)\right],&3\le r\le s.
\end{cases}
\]

The complete weight enumerator of the exceptional subfamily \(H_{2,n}\), namely the crown graph \(K_{n,n}\) with a perfect matching removed, follows from the same structural classification. If \(F_n(z)=\sum_{f\text{ OITRDF on }H_{2,n}}z^{\sum_v f(v)}\), then \(F_2(z)=z^4(1+z)^4\), and for all \(n\ge3\),

\[
\begin{aligned}
F_n(z)={}&z^{2n}(1+z)^{2n}\\
&+2z^n\sum_{t=2}^{n-1}\binom nt[z(1+z)]^t
\bigl((1+z)^n-1-(n-t)z\bigr)\\
&+nz^{2n-2}\bigl((1+z)^{n-1}-1\bigr)^2.
\end{aligned}
\]

The minimum-weight coefficient of this polynomial is \(25\) at \(n=3\), and \(2n(n-1)\) for \(n\ge4\).

## Assumptions and scope

The graph is finite, undirected, and simple. Vertices of \(K_r\) and \(K_s\) are distinguishable. We count functions, not isomorphism classes; each label \(0,1,2\) has its prescribed meaning. Set \(Z=f^{-1}(0)\), \(T=f^{-1}(2)\), \(z_0=|Z|\), and \(t_2=|T|\). Then \(\omega(f)=rs-z_0+t_2\). An OITRDF is required to satisfy all three conditions stated above, including that *every* positive vertex has a positive neighbor. The binomial coefficient \(\binom ab\) has its ordinary combinatorial meaning. The 2019 paper cited below independently gives the scalar \(\gamma_{\mathrm{oitR}}(C_6)=6\); that special numerical value is not claimed as novel.

## Proof

**1. Independent zeros in a direct product.** Two vertices of \(H_{r,s}\) are nonadjacent precisely when they share a coordinate. Any independent set of size at least two lies entirely in a single row or a single column. Indeed, if two distinct elements share a row but have different columns, a third vertex outside that row could share a column with at most one of them, so it would be adjacent to the other. Interchanging coordinates proves the column case. Thus \(|Z|\le s\) when \(r\le s\), and the size-\(s\) independent sets are full rows (and also full columns when \(r=s\)).

**2. The case \(r\ge3\).** If \(Z\ne\varnothing\), at least one vertex must have label \(2\). A labeling of weight less than \(rs-s+2\) would require \(z_0=s\) and \(t_2=1\), since \(z_0\le s\) and \(t_2\ge1\). But a single \(2\)-vertex in column \(j\) fails to defend the zero in column \(j\) of a full zero row; the same argument applies to a full zero column. Therefore \(\omega(f)\ge rs-s+2\). With no zeros, \(\omega(f)\ge rs\), which is strictly larger because \(s\ge3\).

An optimum must thus have exactly one of the profiles \((z_0,t_2)=(s-1,1)\) and \((s,2)\). For \((s-1,1)\), put the zeros in all but one column \(j\) of a row \(i\), and the sole label \(2\) at \((k,j)\) with \(k\ne i\); all remaining vertices get label \(1\). There are \(rs(r-1)\) such functions. When \(r=s\), transpose rows and columns to obtain another \(rs(s-1)\) functions. A putative size-\((s-1)\) zero set consisting of a whole column when \(r=s-1\) cannot be defended by one vertex: the defender shares a row with some zero. These exhaust the one-defender cases.

For \((s,2)\), put the zeros in a full row. Choose the two label-\(2\) vertices outside that row in *different columns*. Such pairs number

\[
\binom{(r-1)s}{2}-s\binom{r-1}{2}.
\]

Multiply by the \(r\) choices of zero row. When \(r=s\), the transposed full-column cases contribute the same number. These are all possibilities, as the two defenders must have different columns in order to defend each zero. Every constructed labeling also satisfies the total-positive condition: after deleting any allowed zero row (or column) there are at least two entire surviving rows (or columns), with no isolated vertices; if just one zero-row vertex remains positive, it too has a positive neighbor outside that row. Thus all counted functions are admissible, the bound is attained, and adding the two disjoint profiles proves both displayed formulas for \(r\ge3\).

**3. The exceptional case \(r=2\).** Write the two rows as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i\sim b_j\) exactly for \(i\ne j\). For \(n\ge3\), independence implies that a nonempty zero set is either contained in one side or equals \(\{a_i,b_i\}\) for some \(i\). If the zeros are contained in \(A\), the positive vertices of \(A\) must number at least two: with zero or one positive \(a_i\), either all positive \(b_j\) are isolated or the particular positive \(b_i\) has no positive neighbor. Hence a one-sided zero set has size at most \(n-2\), and requires at least one label \(2\). Its weight is at least \(2n-(n-2)+1=n+3\). Equality forces exactly two positive vertices in that side and precisely one \(2\) on the opposite side, at one of the same two indices, so there are \(2\binom n2\cdot2=2n(n-1)\) such functions.

If the zero set is a matched cross-side pair, one label \(2\) on each side is necessary, so the weight is at least \(2n\); there are \(n(n-1)^2\) configurations attaining this weight. If there are no zeros, the minimum weight is \(2n\), attained uniquely by the all-one function. Consequently the minimum is \(n+3\) for every \(n\ge3\). At \(n=3\), the three cases tie, giving \(2n(n-1)+n(n-1)^2+1=25\); at \(n\ge4\), only the one-side configurations minimize, giving \(2n(n-1)\). For \(n=2\), the graph is two disjoint edges; the total-positive condition forces all four vertices positive, giving minimum weight \(4\) and one minimum labeling.

**4. Full crown enumerator.** Classify all valid functions by their zero set. If it is empty, every vertex is positive, contributing \(z^{2n}(1+z)^{2n}\). If the zeros lie in one side and the opposite side has no zeros, write \(t\) for the number of positive vertices in the zero-containing side. Total-positive domination requires \(2\le t\le n-1\), with \(\binom nt\) choices of these vertices and \([z(1+z)]^t\) possible weighted positive labelings on them. The other side contributes \(z^n\) times a polynomial counting its chosen label-\(2\) positions. Two or more such defenders are unrestricted, whereas a unique defender must lie at one of the \(t\) indices *not* occupied by zeros. Hence its factor is \((1+z)^n-1-(n-t)z\). There are two sides. Finally, if the zeros form the matched pair \(\{a_i,b_i\}\), then each of the two remaining sides must contain at least one defender. This contributes \(n z^{2n-2}((1+z)^{n-1}-1)^2\). The cases are disjoint and exhaustive, proving the polynomial identity. When \(n=2\), the previous paragraph gives \(F_2(z)\).

## Verification

The self-contained standard-library script `verify.py` constructs adjacency directly from the definition of \(K_r\times K_s\) and exhaustively checks all \(3^{rs}\) labelings for the pairs \((r,s)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\). The resulting minimum/count pairs are, respectively, \((4,1),(6,25),(7,24),(8,40),(9,60),(8,108),(10,96)\). The same brute-force distributions equal all coefficients of the displayed crown polynomial through \(n=6\); exact symbolic polynomial arithmetic also checks the predicted lowest-degree terms through \(n=9\). Reproduce using `python3 verify.py` in the directory containing this document and the script. These experiments are independent finite checks; the preceding argument establishes the universal quantifiers.

## Relationship to prior work

Cabrera Martínez, Kuziak, and Yero, *Relating the Outer-Independent Total Roman Domination Number with Some Classical Parameters of Graphs*, arXiv:2112.05476 (first public version, 10 December 2021), subsequently *Mediterranean Journal of Mathematics* **19**, 144 (2022), Theorem 3.5, states \(\gamma_{\mathrm{oitR}}(K_r\times K_s)=s(r-1)+2\) for all \(2\le r\le s\). For \(r=2\) and \(s\ge3\), its proposed full-zero-row witness has every remaining positive vertex in one independent row, violating the defining total-positive condition. The corrected value is therefore one larger throughout this infinite boundary family. For \(r\ge3\), the previously stated scalar is retained; the **complete optimizer classification and exact census** are the new contribution. The new all-weight crown polynomial further refines the scalar invariant. The 2019 foundational paper *Outer-independent total Roman domination in graphs* supplies the exact definition and gives \(\gamma_{\mathrm{oitR}}(C_6)=6\) as an instance of its cycle result; that pre-existing instance is explicitly not claimed as a new numerical value. Related perfect Roman and ordinary outer-independent Roman results use different feasibility constraints and do not imply the simultaneous total and outer-independent classification here.

## Limitations

The general optimizer enumeration is restricted to direct products of two complete graphs with both orders at least two. The all-weight polynomial is asserted only for the two-row (crown) subfamily. Numerical tests stop at the listed finite sizes and do not constitute an infinite proof. Although comparisons with accessible primary literature and related mathematical records found no formula that implies the new optimizer census or the corrected infinite endpoint, undiscovered or unindexed priority overlap remains possible. No independent external review has been performed.

## References

1. A. Cabrera Martínez, D. Kuziak, and I. G. Yero, *Relating the outer-independent total Roman domination number with some classical parameters of graphs*, arXiv:2112.05476v1 (2021), especially Theorem 3.5. https://arxiv.org/abs/2112.05476
2. A. Cabrera Martínez, D. Kuziak, and I. G. Yero, same article, *Mediterranean Journal of Mathematics* 19, 144 (2022). https://doi.org/10.1007/s00009-022-02061-y
3. A. Cabrera Martínez, D. Kuziak, and I. G. Yero, *Outer-independent total Roman domination in graphs*, *Discrete Applied Mathematics* 269 (2019), 107–119. https://doi.org/10.1016/j.dam.2018.12.018
