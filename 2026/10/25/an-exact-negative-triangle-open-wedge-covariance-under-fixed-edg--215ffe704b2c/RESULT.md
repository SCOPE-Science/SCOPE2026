# An exact negative triangle–open-wedge covariance under fixed-edge sampling

## Finding
Let \(G\) be uniform among all simple graphs with \(n\ge4\) labelled vertices and exactly \(0\le m\le N=\binom n2\) edges. Let \(T\) count induced triangles and \(W\) count induced three-vertex paths (open wedges), with each unordered three-vertex set counted once. For \(3\le m\le N-2\), define
\[
K_{n,m}=m(n^2-3n-8)+n^3-2n^2-3n+4.
\]
Then
\[
\boxed{\operatorname{Cov}_{G(n,m)}(T,W)=
-\binom n3\frac{(m)_3}{(N)_3}\,
\frac{6(N-m)(N-m-1)K_{n,m}}
{(n+1)(n+2)(N-5)(N-4)(N-2)}<0.}
\]
The covariance is zero if \(m\le2\) or \(m\ge N-1\). Here \((x)_j=x(x-1)\cdots(x-j+1)\) and \((x)_0=1\). Thus the sign is determined exactly for every admissible finite graph size and edge count.

In contrast, if edges are independent with probability \(0<p<1\), then
\[
\boxed{\operatorname{Cov}_{G(n,p)}(T,W)
=3\binom n3 p^4(1-p)\,[2(n-3)-(3n-8)p].}
\]
This covariance is positive for \(p<2(n-3)/(3n-8)\), zero at that threshold, and negative above it. Conditioning the graph on its precise edge count therefore changes the sign throughout the sparse-enough regime, rather than merely adjusting a numerical constant.

For any sequence of integers \(m=m_n\) with \(m/\binom n2\to p\in(0,1)\),
\[
\frac{\operatorname{Cov}_{G(n,m)}(T,W)}{n^3}
\longrightarrow -p^4(1-p)^2,
\quad
\operatorname{Corr}_{G(n,m)}(T,W)
\longrightarrow
-\frac{\sqrt{12}\,p^{3/2}}
{\sqrt{(1+2p)(1-3p+6p^2)}}.
\]

## Assumptions and scope
A triangle contributes one to \(T\) iff all three of its possible edges occur. A wedge contributes one to \(W\) iff exactly two of the three edges occur; hence an unordered triple never contributes to both. Let \(P=\sum_v\binom{d_v}{2}\) count non-induced two-edge paths by centers. The pointwise identity \(W=P-3T\) holds because a triangle contains three non-induced centered paths. All expectations use the indicated finite probability models, without any independence assumption in \(G(n,m)\).

For fixed-edge sampling put \(a_j=(m)_j/(N)_j\) for \(j=0,\ldots,6\) and interpret the probability of including \(j\) distinct edges as \(a_j\). For \(j>N\), any formal occurrence is omitted in the corresponding counting formula; equivalently terms multiplying it have zero combinatorial multiplicity. For \(n\ge4\), \(N\ge6\), so the required \(a_j\) are defined. Set \(C=\binom n3\) and \(B=3C\).

## Proof
**1. Exact moments by edge-set overlap.** Each triangle uses three distinct edges and each non-induced centered path uses two. Consequently
\[
\begin{aligned}
\mathbb ET&=Ca_3, &\mathbb EP&=Ba_2,\\
\mathbb ET^2&=C\{a_3+3(n-3)a_5+[C-1-3(n-3)]a_6\},\\
\mathbb EP^2&=B\{a_2+(4n-10)a_3+[B-4n+9]a_4\},\\
\mathbb E[TP]&=C\{3a_3+6(n-3)a_4+[B-6n+15]a_5\}.
\end{aligned}
\]
For example, a specified triangle has \(3(n-3)\) distinct triangles sharing one edge, and a specified centered path has \(4n-10\) other centered paths sharing exactly one edge. A fixed triangle contains exactly three centered paths, has \(6(n-3)\) centered paths with one of its edges and one outside edge, and has \(B-6n+15\) remaining paths whose two edges are outside the triangle. These exhaust each overlap type; disjoint sets of required edges have joint probability \(a_j\) for their union's cardinality \(j\).

Therefore
\[
\operatorname{Cov}(T,W)
=C\{3a_3+6(n-3)a_4+(B-6n+15)a_5\}-CBa_3a_2
-3\Big(C\{a_3+3(n-3)a_5+[C-1-3(n-3)]a_6\}-C^2a_3^2\Big).
\]
All identities include the boundary values of \(m\), using the usual zero falling factorial when \(m<j\).

**2. Negative factorization and finite boundaries.** Substitute \(N=n(n-1)/2\) and \(a_j=(m)_j/(N)_j\) into the last equality. Clearing products and cancelling factors gives exactly the displayed expression with \(K_{n,m}\) for \(3\le m\le N-2\); this rational-polynomial identity is also checked symbolically in the included verifier. For \(n=4\), \(K_{n,m}=24-4m>0\) whenever \(3\le m\le4\). For \(n\ge5\), both \(n^2-3n-8>0\) and \(n^3-2n^2-3n+4>0\), so \(K_{n,m}>0\). Every other factor in the numerator is positive in the stated range and every denominator factor is positive for \(n\ge4\). This proves strict negativity.

For \(m\le2\), no triangle can occur, so \(T=0\) identically. For \(m\ge N-1\), the graph is complete or misses exactly one edge: the triangle count and open-wedge count depend only on \(m\), and hence are both deterministic. The covariance therefore vanishes at precisely the claimed boundary values.

**3. Independent-edge comparison.** In \(G(n,p)\), two disjoint edge-functionals are independent. For a given triangle's three vertices, the same triple contributes covariance \(-3p^5(1-p)\) with its induced-wedge indicator. There are \(3(n-3)\) other triples sharing exactly one edge with it. Each such pair contributes \(p^4(1-p)(2-3p)\), found by enumerating which of the wedge's three edges is absent. All other pairs of triples have disjoint required edge sets and covariance zero. Summing gives
\[
C\bigl[-3p^5(1-p)+3(n-3)p^4(1-p)(2-3p)\bigr]
=3Cp^4(1-p)[2(n-3)-(3n-8)p],
\]
as asserted. Because \(0<2(n-3)/(3n-8)<1\), the claimed sign transition is strict.

**4. Dense fixed-edge limit.** The exact factorization yields \(n^{-3}\operatorname{Cov}(T,W)\to-p^4(1-p)^2\) by substitution and leading powers of \(n\). For the correlation, use the exact moments in Step 1 and \(W=P-3T\), whence
\[
\operatorname{Var}(W)=\operatorname{Var}(P)+9\operatorname{Var}(T)-6\operatorname{Cov}(T,P).
\]
Cancelling leading terms in these rational expressions gives
\[
\begin{aligned}
\operatorname{Var}(T)/n^3&\to p^3(1-p)^2(1+2p)/6,\\
\operatorname{Var}(W)/n^3&\to p^2(1-p)^2(1-3p+6p^2)/2.
\end{aligned}
\]
Both constants are positive for \(p\in(0,1)\). Division by the geometric mean of the two standard deviations proves the limiting correlation.

## Verification
`verify.py` uses exact rational arithmetic to enumerate **all** graphs on four, five, and six labelled vertices, separately at every possible number of edges (34 edge-count strata). It checks five moments/covariances against independent enumerations, the closed covariance factorization, and the strict-sign/boundary claim. It also checks the independent-edge covariance polynomial for five vertices by exact summation over fixed-edge strata. Symbolic verification checks the factorization for arbitrary symbolic size and edge count and the three leading fixed-density limits. Run `python verify.py` with Python 3 and SymPy installed. Exact enumeration does not prove the unlimited statement; the overlap count, rational factorization, and positivity argument above do.

## Relationship to prior work
Goldschmidt, Griffiths and Scott (2019; subsequently published 2020) develop martingale decompositions and moderate-deviation estimates for non-induced cherry and triangle counts in \(G(n,m)\); Section 7 concerns covariances of **increments**, not the finite induced-open-wedge count's universal negative covariance. Alvarado, Gonçalves de Oliveira and Griffiths (2023) also treat triangles and (non-induced) cherries separately in both Erdős–Rényi models; their inspected Section 1.3 describes marginal cherry deviations and does not state the displayed mixed finite-size sign result. The induced versus non-induced distinction is essential: \(W=P-3T\). Janson (1990, 1994) developed general finite-graph-statistic limit methods, a plausible antecedent for the asymptotic part. The novelty claim concerns the explicit **all-parameter finite sign and model-reversal comparison**, not the elementary fact that subgraph counts admit moment expansions or that they have limiting distributions.

## Limitations
The claim addresses the two standard Erdős–Rényi models only, with \(n\ge4\). It does not assert stochastic negative association or a sign for other graph statistics. The general finite-sign theorem is proved directly here; historical priority may still depend on an equivalent calculation in older graph-statistics literature, particularly detailed treatments of joint induced subgraph counts. The symbolically checked identities are supplementary to the stated proof.

## References
1. C. Goldschmidt, S. Griffiths, A. Scott, “Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\),” arXiv:1902.06830 (first public 2019-02-18); Transactions of the American Mathematical Society 373 (2020), 5517–5585. https://arxiv.org/abs/1902.06830
2. J. D. Alvarado, L. Gonçalves de Oliveira, S. Griffiths, “Moderate deviations of triangle counts in sparse Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\),” arXiv:2305.04326 (first public 2023-05-07). https://arxiv.org/abs/2305.04326
3. S. Janson, “A functional limit theorem for random graphs with applications to subgraph count statistics,” Random Structures & Algorithms 1 (1990), 15–37, DOI:10.1002/rsa.3240010103.
4. S. Janson, “Orthogonal decompositions and functional limit theorems for random graph statistics,” Memoirs of the American Mathematical Society 534 (1994).
