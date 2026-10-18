# Exact Italian domination polynomial of connected non-complete-bipartite chain graphs

## Finding

An **Italian dominating function** on a finite simple graph \(G\) is a labeling \(f:V(G)\to\{0,1,2\}\) in which every vertex with label zero has neighbors whose labels sum to at least two. Its weight polynomial is
\[
D_I(G;x)=\sum_{f\text{ Italian dominating}}x^{\sum_{v\in V(G)}f(v)}.
\]

**Theorem.** Let \(p\ge2\). Take nonempty, pairwise disjoint vertex classes \(A_1,\ldots,A_p,B_1,\ldots,B_p\) with positive sizes \(a_i=|A_i|\) and \(b_j=|B_j|\). Form the connected bipartite chain graph \(G\) by making every vertex of \(A_i\) adjacent to every vertex of \(B_j\) exactly when \(j\le i\). The following explicit sum determines **every coefficient** of \(D_I(G;x)\), for arbitrary positive class sizes.

Set
\[
U_m(x)=(1+x+x^2)^m,\qquad
V_m(x)=(x+x^2)^m,\qquad
W_m(x)=U_m(x)-V_m(x)
\]
and, for any polynomial \(F\), define the low-weight truncation
\[
\mathcal T_2(F)(x)=F(x)-F(0)-xF'(0).
\]
For \(1\le\alpha\le p+1\) and \(0\le\beta\le p\), define
\[
P_i^{(\alpha)}(x)=
\begin{cases}
V_{a_i}(x),&i<\alpha,\\
W_{a_i}(x),&i=\alpha,\\
U_{a_i}(x),&i>\alpha,
\end{cases}
\]
where the middle case never occurs when \(\alpha=p+1\), and
\[
Q_j^{(\beta)}(x)=
\begin{cases}
U_{b_j}(x),&j<\beta,\\
W_{b_j}(x),&j=\beta,\\
V_{b_j}(x),&j>\beta,
\end{cases}
\]
where the middle case never occurs when \(\beta=0\). Empty products are one. Put
\[
\mathcal A_{\alpha\beta}(x)=
\begin{cases}
\displaystyle\prod_{i=1}^{p}P_i^{(\alpha)}(x),&\beta=0,\\[2mm]
\displaystyle\left(\prod_{i<\beta}P_i^{(\alpha)}(x)\right)
\mathcal T_2\!\left(\prod_{i\ge\beta}P_i^{(\alpha)}(x)\right),&1\le\beta\le p,
\end{cases}
\]
\[
\mathcal B_{\beta\alpha}(x)=
\begin{cases}
\displaystyle\prod_{j=1}^{p}Q_j^{(\beta)}(x),&\alpha=p+1,\\[2mm]
\displaystyle\mathcal T_2\!\left(\prod_{j\le\alpha}Q_j^{(\beta)}(x)\right)
\left(\prod_{j>\alpha}Q_j^{(\beta)}(x)\right),&1\le\alpha\le p.
\end{cases}
\]
Then
\[
\boxed{D_I(G;x)=\sum_{\alpha=1}^{p+1}\sum_{\beta=0}^{p}
\mathcal A_{\alpha\beta}(x)\,\mathcal B_{\beta\alpha}(x).}
\]
This is a sum of \(p(p+1)\) explicitly factored polynomial contributions with only weight-zero and weight-one truncations; no enumeration of the \(3^{|V(G)|}\) labelings is required.

## Assumptions and scope

All graphs are finite, undirected, simple and connected. Each class size is a positive integer, so the class orderings are strict canonical open-neighborhood twin-class orderings. Each vertex receives one of the three numeric labels, and labels on distinct named vertices are counted separately. The variable \(x\) records total numeric weight, not the size of the positive support. The theorem concerns the genuinely non-complete-bipartite chain graphs \(p\ge2\). The same formula also makes sense when \(p=1\), the complete-bipartite boundary already treated by broader previous enumeration.

## Proof

For a labeling \(f\), let \(\alpha\) be the **smallest** class index containing a zero-labeled vertex on the \(A\)-side, or \(p+1\) when that side has no zero. Let \(\beta\) be the **largest** class index containing a zero-labeled vertex on the \(B\)-side, or zero when that side has no zero. These two indices are uniquely determined by \(f\).

For fixed \(\alpha\), all labels on \(A_i\) with \(i<\alpha\) are positive, the class \(A_\alpha\) (if it exists) contains at least one zero, and later classes have unrestricted labels. Their classwise weight polynomials are precisely \(P_i^{(\alpha)}\): the choices are respectively counted by \(V\), \(W\) and \(U\). For fixed \(\beta\), the corresponding assertions on the \(B\)-side are reversed in order, and are counted by \(Q_j^{(\beta)}\).

Suppose \(\alpha\le p\). Every zero-labeled vertex in \(A_i\) has \(i\ge\alpha\) and neighborhood \(B_1\cup\cdots\cup B_i\). Since labels are nonnegative, all these zero vertices satisfy the defense requirement **if and only if** the total label weight on \(B_1\cup\cdots\cup B_\alpha\) is at least two: necessity follows from the zero in \(A_\alpha\), and sufficiency from neighborhood nesting. If \(\alpha=p+1\), no \(A\)-side defense condition is needed. Because the polynomial of a set of labelings records their nonnegative integral weight, \(\mathcal T_2\) removes exactly those labelings for which the relevant prefix has weight zero or one. This gives \(\mathcal B_{\beta\alpha}\).

Dually, when \(\beta\ge1\), every zero-labeled vertex in \(B_j\) has \(j\le\beta\) and neighborhood \(A_j\cup\cdots\cup A_p\). All such vertices are defended if and only if the label weight on \(A_\beta\cup\cdots\cup A_p\) is at least two. The condition is vacuous for \(\beta=0\). Truncation on this suffix gives \(\mathcal A_{\alpha\beta}\).

For fixed \((\alpha,\beta)\), the constraints on labels in the \(A\)-classes and \(B\)-classes are independent, so multiplication of their weight polynomials counts exactly the Italian dominating functions having those two zero frontiers. Every valid function has exactly one pair of frontiers, and the pairs are disjoint. Adding the \(p(p+1)\) products proves the identity for all allowed sizes and weights. In particular the formula has no unproved infinite-step or asymptotic premise. \(\square\)

## Verification

The standalone Python 3 script `verify.py` evaluates every frontier-cell polynomial from the formula and independently enumerates labelings from the graph's explicitly generated edges and the local defense test. On 76 class-size profiles (including complete-bipartite baseline tests), it evaluated 793620 labeled assignments and compared 1143 separately counted frontier cells; all comparisons agreed. A fixed pair of connected chain graphs with \(3\) vertices on each side, both of Italian domination number \(4\), illustrates the additional information: for \((a_1,a_2)=(2,1)\), \((b_1,b_2)=(1,2)\), the coefficient of \(x^4\) is \(4\); for \((a_1,a_2,a_3)=(b_1,b_2,b_3)=(1,1,1)\), it is \(6\). The script checks these figures independently. Execute `python3 verify.py` in the directory containing the script. Finite enumeration is a consistency test, not the proof for arbitrary sizes.

## Relationship to prior work

Shao and Zhao introduced the all-weight Italian-domination counting program for paths, trees and cycles, with dynamic programs and selected explicit cycle coefficients [1]. The present identity gives every coefficient, in a closed zero-frontier sum, for non-complete-bipartite connected chain graphs, a different infinite class containing cyclic examples. Padamutham and Palagiri previously obtained the **minimum** Roman \(\{2\}\) (equivalently Italian) domination number of chain graphs [2]; knowing that minimum does not determine the weight polynomial. Published formulas for the ordinary Roman-domination polynomial of chain graphs [3] impose the stronger requirement that every zero have a label-two neighbor, and therefore count a different collection. The existing all-weight Roman \(\{2\}\) formula on complete multipartite graphs [4] includes the complete-bipartite boundary \(p=1\) but not general chain graphs with \(p\ge2\).

## Limitations

The theorem does not cover arbitrary convex bipartite graphs, general chordal bipartite graphs, or disconnected graphs with isolated vertices without further decomposition. It does not assert real-rootedness, coefficient log-concavity, or any asymptotic property of the polynomial. The exhaustive tests cover only the finite profiles and assignments listed above; the unrestricted statement rests on the frontier proof. Bibliographic uniqueness outside the identified sources remains open to further investigation.

## References

[1] P. Shao and C. Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, first posted 2026-09-09. https://arxiv.org/abs/2610.00108

[2] C. Padamutham and V. S. R. Palagiri, *Complexity of Roman {2}-domination and the double Roman domination in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 1081–1086, DOI:10.1016/j.akcej.2020.01.005.

[3] *Roman domination polynomial of chain graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-roman-domination-polynomial-of-chain-graphs--e846e0fa619b.

[4] *Weight enumerator of all Roman {2}-dominating functions on complete multipartite graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-weight-enumerator-of-all-roman-2-dominating-functions-on-complet--4a62f97e627e.
