# Exact domination polynomial of chain graphs
## Finding
Let \(G\) be a finite connected chain graph. Use its canonical twin-class bipartition
\[
A=A_1\cup\cdots\cup A_p,\qquad B=B_1\cup\cdots\cup B_p,
\]
where every class is nonempty and
\[
N(a)=B_1\cup\cdots\cup B_i\quad(a\in A_i),
\qquad
N(b)=A_j\cup\cdots\cup A_p\quad(b\in B_j).
\]
Put \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\),
\[
a_i=\sum_{t=1}^i\alpha_t,\qquad b_i=\sum_{t=1}^i\beta_t,
\]
with \(a_0=b_0=0\), and write \(n=b_p\). Then the ordinary domination polynomial
\[
D(G;x)=\sum_{S\text{ dominating}}x^{|S|}
\]
is
\[
D(G;x)=\sum_{i=0}^{p}x^{a_i+n-b_i}
+\sum_{1\le j\le i\le p}
 x^{a_{j-1}+n-b_i}
 \big((1+x)^{\alpha_i}-1\big)
 \big((1+x)^{\beta_j}-1\big)
 \prod_{t=j}^{i-1}(1+x)^{\alpha_t}
 \prod_{t=j+1}^{i}(1+x)^{\beta_t}.
\]
Thus the total number of dominating sets is
\[
D(G;1)=p+1+\sum_{1\le j\le i\le p}
2^{a_{i-1}-a_{j-1}+b_i-b_j}
(2^{\alpha_i}-1)(2^{\beta_j}-1).
\]
The domination number satisfies \(\gamma(G)=1\) exactly when \(\min\{|A|,|B|\}=1\), and \(\gamma(G)=2\) otherwise.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A dominating set \(S\subseteq V(G)\) means that every vertex outside \(S\) has a neighbor in \(S\). The canonical chain-graph form above fixes the orientation of the nested neighborhoods; reversing the two sides only reindexes the same theorem. The claim concerns the ordinary domination polynomial, not total domination or independent domination.

For \(0\le i\le p\), define the cut set
\[
C_i=A_1\cup\cdots\cup A_i\cup B_{i+1}\cup\cdots\cup B_p.
\]
Empty prefixes or suffixes are allowed, so \(C_0=B\) and \(C_p=A\).

## Proof
First suppose that a dominating set \(S\) meets both bipartition sides. Define
\[
i=\max\{t:S\cap A_t\ne\varnothing\},\qquad
j=\min\{t:S\cap B_t\ne\varnothing\}.
\]
If \(t<j\), then no selected vertex lies in \(B_1\cup\cdots\cup B_t=N(A_t)\). Hence every vertex of \(A_t\) must itself belong to \(S\); otherwise such an omitted vertex would be undominated. Therefore \(A_t\subseteq S\) for every \(t<j\). Dually, if \(t>i\), then \(N(B_t)=A_t\cup\cdots\cup A_p\) contains no selected vertex, so \(B_t\subseteq S\).

These forced inclusions imply \(j\le i+1\). Indeed, if \(j\ge i+2\), then \(A_{i+1}\subseteq S\), contradicting maximality of \(i\).

Conversely, fix indices with \(j\le i+1\), require all \(A_t\) with \(t<j\) and all \(B_t\) with \(t>i\), and choose boundary vertices so that \(S\cap A_i\ne\varnothing\) and \(S\cap B_j\ne\varnothing\) when \(j\le i\). Any omitted vertex in \(A_t\) has \(t\ge j\), hence is adjacent to every selected vertex of \(B_j\). Any omitted vertex in \(B_t\) has \(t\le i\), hence is adjacent to every selected vertex of \(A_i\). Thus the stated conditions are sufficient.

When \(j=i+1\), the forced inclusions leave exactly the single set \(C_i\). This also includes the one-sided possibilities at the endpoints \(C_0=B\) and \(C_p=A\); no proper subset of one bipartition side can dominate omitted vertices on that same independent side.

When \(1\le j\le i\le p\), the classes \(A_1,\ldots,A_{j-1}\) and \(B_{i+1},\ldots,B_p\) are forced in; \(A_i\) and \(B_j\) contribute nonempty-subset factors; the intervening classes \(A_j,\ldots,A_{i-1}\) and \(B_{j+1},\ldots,B_i\) are arbitrary; and all classes beyond the boundary indices are absent. Their generating function is therefore
\[
x^{a_{j-1}+n-b_i}
\big((1+x)^{\alpha_i}-1\big)
\big((1+x)^{\beta_j}-1\big)
\prod_{t=j}^{i-1}(1+x)^{\alpha_t}
\prod_{t=j+1}^{i}(1+x)^{\beta_t}.
\]
The boundary indices are unique, so these contributions are disjoint. Adding the \(p+1\) cut sets proves the polynomial formula. Evaluating at \(x=1\) gives the stated total count.

If one bipartition side has one vertex, its unique vertex is adjacent to the entire other side and hence dominates the graph. If both sides have size at least two, no single vertex can dominate the other vertices in its own independent side. On the other hand, any vertex of \(A_p\) together with any vertex of \(B_1\) dominates both sides, proving \(\gamma(G)=2\).

## Verification
The accompanying `verify.py` constructs canonical chain graphs directly from the class sizes, exhaustively enumerates all vertex subsets, tests the definition of domination, and compares every coefficient with the displayed formula. It checks all \(540\) class-size instances with \(1\le p\le4\), every \(\alpha_i,\beta_i\in\{1,2,3\}\), and total order at most \(11\). It also checks the closed total-count formula and explicit \(K_2\) and star boundary cases. A successful replay prints
`VERIFY_OK graph_types=540 subset_checks=687124 coefficient_checks=5836 max_order=11`.

This finite computation is a regression check, not the proof of the unrestricted theorem; the symbolic boundary-index argument above proves all finite connected chain graphs.

## Relationship to prior work
Kotek, Preen, Simon, Tittmann, and Trinks introduced general recurrence and splitting machinery for the domination polynomial and emphasized exact computations on special graph classes. Their paper gives the standard generating-function definition and general-purpose reductions, but the inspected full text does not state the chain-graph boundary-index formula above. The complete-bipartite case \(p=1\) is not claimed as new: the formula specializes to
\[
D(K_{m,n};x)=x^m+x^n+\big((1+x)^m-1\big)\big((1+x)^n-1\big).
\]

Rather, Wang, and Belardo study **independent** domination polynomials of chain and threshold graphs. Independent dominating sets are a strict subfamily of ordinary dominating sets in general, so that invariant does not determine the ordinary domination polynomial here. Likewise, total-domination formulas do not imply the present result because ordinary domination allows selected vertices to have no selected neighbor and includes the cut sets \(C_i\).

## Limitations
The theorem is restricted to connected chain graphs in the stated canonical form. It does not claim analogous formulas for arbitrary bipartite graphs, threshold graphs, or disconnected graphs. Exhaustive verification stops at order \(11\); larger orders rely on the symbolic proof. Targeted searches did not locate an earlier equivalent chain-graph ordinary-domination formula, but absence from the searched indexes is not a proof of novelty, and older special-class literature can use different terminology such as Ferrers or difference graphs.

## References
1. T. Kotek, J. Preen, F. Simon, P. Tittmann, M. Trinks, “Recurrence relations and splitting formulas for the domination polynomial,” *Electronic Journal of Combinatorics* 19(3) (2012), P47. arXiv:1206.5926. DOI:10.37236/2475.
2. B. A. Rather, J. Wang, F. Belardo, “Independent domination polynomials of binary sequence graphs,” *Journal of Algebraic Combinatorics* 63 (2026), article 57. DOI:10.1007/s10801-026-01514-x.
