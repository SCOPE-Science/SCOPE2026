# Signed total Roman domination of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n,
\]
where the bipartition is \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and the deleted perfect matching is \(M_n=\{a_i b_i:1\le i\le n\}\). Then
\[
\gamma_{stR}(\operatorname{Cr}_n)=6.
\]

More precisely, every minimum signed total Roman dominating function has total label sum \(3\) on each shore. If one shore contains \(a\) vertices labeled \(-1\), \(b\) labeled \(1\), and \(c\) labeled \(2\), then
\[
a=\frac{n+c-3}{2},\qquad b=\frac{n+3-3c}{2},
\]
so only nonnegative integral triples arising from these formulas occur. The two shore labelings are compatible exactly when the label-\(-1\) vertices can see a label \(2\) across the deleted matching: if the opposite shore has at least two labels \(2\), compatibility is automatic; if it has exactly one label \(2\) at index \(j\), the first shore cannot put \(-1\) at index \(j\); and if it has no label \(2\), the first shore cannot contain a label \(-1\).

Writing
\[
T_n(c)=\frac{n!}{a_n(c)!\,b_n(c)!\,c!},\quad
a_n(c)=\frac{n+c-3}{2},\quad
b_n(c)=\frac{n+3-3c}{2},
\]
and letting \(C_n\) be the set of \(c\) for which \(a_n(c)\) and \(b_n(c)\) are nonnegative integers, the number \(M_n\) of minimum functions is as follows. For odd \(n\),
\[
M_3=10,
\]
and for odd \(n\ge5\),
\[
M_n=\left(\sum_{c\in C_n,\ c\ge2}T_n(c)\right)^2.
\]
For even \(n\), put \(a_1=(n-2)/2\), \(b_1=n/2\), \(T_1=T_n(1)\),
\[
S_n=\sum_{c\in C_n,\ c\ge3}T_n(c),\qquad
Q_n=\sum_{c\in C_n,\ c\ge3}T_n(c)\frac{n-a_n(c)}{n}.
\]
Then
\[
M_n=S_n^2+2T_1Q_n+T_1\left(\binom{n-1}{a_1}+b_1\binom{n-2}{a_1}\right).
\]
For example,
\[
(M_3,M_4,M_5,M_6,M_7,M_8)=(10,84,900,3280,44100,189000).
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. A signed total Roman dominating function on a graph \(G\) is a function \(f:V(G)\to\{-1,1,2\}\) such that every open-neighborhood sum satisfies
\[
\sum_{u\in N(v)}f(u)\ge1,
\]
and every vertex labeled \(-1\) has a neighbor labeled \(2\). The signed total Roman domination number is the minimum possible total weight \(\sum_{v\in V(G)}f(v)\).

The theorem is restricted to connected crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\). The case \(n=2\) is excluded because \(K_{2,2}-M_2\) is disconnected.

## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), and
\[
X=\sum_{i=1}^n x_i,\qquad Y=\sum_{i=1}^n y_i.
\]
Since \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), and symmetrically for \(b_i\), the open-neighborhood inequalities are exactly
\[
Y-y_i\ge1,\qquad X-x_i\ge1\qquad(1\le i\le n).
\]
The rescue condition is also index-explicit: if \(x_i=-1\), then some \(y_j=2\) must occur with \(j\ne i\); if \(y_i=-1\), then some \(x_j=2\) must occur with \(j\ne i\).

Consider any shore vector \(z=(z_1,\ldots,z_n)\in\{-1,1,2\}^n\) with sum \(Z\) satisfying \(Z-z_i\ge1\) for every \(i\). If some \(z_i=2\), then \(Z\ge3\). If no label \(2\) occurs, then the labels are \(\pm1\); applying the inequality at a vertex labeled \(1\) gives \(Z\ge2\). Thus \(X,Y\ge2\).

Suppose a feasible function had weight at most \(5\). Then one shore sum, say \(X\), would equal \(2\). That shore contains no label \(2\). For \(n=3\), a \(\pm1\)-sum of \(2\) is impossible by parity. For \(n\ge4\), the equality \(X=2\) forces \(n\) even and forces at least one label \(-1\) on \(A\). Therefore \(B\) must contain a label \(2\) to rescue it. Conversely, because \(A\) has no label \(2\), \(B\) cannot contain any label \(-1\). Hence every label on \(B\) is \(1\) or \(2\), with at least one \(2\), so \(Y\ge n+1\ge5\). Then \(X+Y\ge7\), a contradiction. Therefore every feasible function has weight at least \(6\).

The bound is attained. If \(n\) is odd, label two vertices on each shore by \(2\), label \((n-1)/2\) vertices by \(-1\), and label the remaining \((n-3)/2\) vertices by \(1\). Each shore has sum \(3\), and two opposite-shore labels \(2\) guarantee every label \(-1\) a rescuing neighbor despite one deleted cross-edge. If \(n\) is even, choose the same index on both shores for the unique label \(2\), put \(-1\) on \((n-2)/2\) other indices, and put \(1\) on the remaining \(n/2\) indices. Again each shore has sum \(3\), and no label \(-1\) is matched to the unique opposite label \(2\). Thus \(\gamma_{stR}(\operatorname{Cr}_n)=6\).

At weight \(6\), the preceding argument also rules out shore sums \((2,4)\) and \((4,2)\), so necessarily \(X=Y=3\). Solving
\[
a+b+c=n,\qquad -a+b+2c=3
\]
gives the displayed formulas for \(a_n(c)\) and \(b_n(c)\). The stated compatibility rule is exactly the rescue condition translated into the number and positions of opposite-shore labels \(2\). Counting multinomial shore labelings under this rule gives the formulas for \(M_n\). For odd \(n\ge5\), every feasible minimum shore has at least two labels \(2\), so compatibility is automatic. For even \(n\), the only nonautomatic case is a shore with exactly one label \(2\); separating the \((1,1)\), \((1,c)\), and \((c,d)\) cases with \(c,d\ge3\) yields the displayed expression.

## Verification
The proof above is symbolic for every \(n\ge3\). The included `VERIFY.py` independently evaluates the graph definition and all labelings for \(3\le n\le8\). It confirms minimum weight \(6\) and the exact minimum-function counts \(10,84,900,3280,44100,189000\). It also evaluates the closed counting formula and explicit constructions through \(n=40\).

A replay from the packaged verifier returned:

`ALL CHECKS PASSED; exhaustive_orders=[3,4,5,6,7,8]; minimum_counts=[10,84,900,3280,44100,189000]; formula_range=3..40`

The finite computation is corroborative only; it is not used to justify the unrestricted theorem.

## Relationship to prior work
Koster, Volkmann, and Wehrmann introduced a recent study of signed total Roman domination and domatic numbers for cubic and complete multipartite graphs. Its public record was first posted on 2026-06-25 and lists MSC 05C69. The accessible abstract defines the same invariant and states that the paper determines the parameters on complete multipartite graphs while relating the cubic case to other invariants. A crown graph is not complete multipartite for \(n\ge3\), though \(\operatorname{Cr}_4\) is cubic. No crown-graph or perfect-matching-deletion theorem appeared in the accessible abstract and detailed public summary. The full article text was not retrievable during this review, so a hidden same-family statement remains an explicit originality risk rather than being treated as disproved.

Zhao and Miao computed exact signed total Roman domination numbers for complete bipartite graphs. In particular, the published survey statement gives
\[
\gamma_{stR}(K_{p,p})=2
\]
for \(p\ge1\) except \(p=3\), where the value is \(4\). Hence the crown result is not a restatement of the complete-bipartite formula: deleting one perfect matching raises the value to \(6\) for every \(n\ge3\). The 2025 edge-modification paper on signed total Roman domination explicitly studies graph modification by deleting or subdividing an edge, but the accessible abstract does not state an exact theorem for deletion of a whole perfect matching. That full text was also not retrievable here and is retained as a residual comparison risk.

Focused searches for the standard crown name, the form \(K_{n,n}-M_n\), the bipartite-Kneser alias \(H(n,1)\), and signed-total-Roman terminology did not locate an equivalent exact crown theorem or minimum-function census.

## Limitations
The theorem concerns crown graphs only and does not classify arbitrary bipartite graphs obtained by deleting a nonperfect matching from \(K_{m,n}\). The minimum-function count is exact, but its finite replay checks only orders through \(8\); the unrestricted count follows from the symbolic case analysis. The full text of two highly relevant recent sources was unavailable during this review, so an equivalent result hidden in those texts cannot be excluded solely from the accessible material. Search noncoverage is evidence, not a proof of absolute novelty.

## References
1. A. M. C. A. Koster, L. Volkmann, M. Wehrmann, “Signed Total Roman Domination and Domatic Numbers: Degree Three and Complete Multipartite Graphs,” arXiv:2606.27175v1, 2026.
2. Y. Zhao, L. Miao, “Signed Roman (Total) Domination Numbers of Complete Bipartite Graphs and Wheels,” Communications in Mathematical Research 33(4) (2017), 318–326, DOI 10.13447/j.1674-5647.2017.04.04.
3. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, L. Volkmann, “Varieties of Roman domination II,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 966–984, DOI 10.1016/j.akcej.2019.12.001.
4. A. Guo, L. Volkmann, Y. Wang, “Signed total Roman domination and domatic numbers in graphs,” Applied Mathematics and Computation 487 (2025), 129074, DOI 10.1016/j.amc.2024.129074.
5. S. Kosari, Y. Rao, Z. Shao, J. Amjadi, R. Khoeilar, “Complexity of signed total \(k\)-Roman domination problem in graphs,” AIMS Mathematics 6(1) (2021), 952–961, DOI 10.3934/math.2021057.
