# A sharp short-cycle covariance transition in biregular pairing multigraphs

## Finding
Let \(n,m\ge2\), \(d,e\ge1\), and \(L=nd=me\). Take a uniformly random perfect pairing between the \(L\) labelled left and \(L\) labelled right half-edges of the bipartite configuration model. Write \(M_{ij}\) for the number of resulting edges joining left vertex \(i\) to right vertex \(j\). Define
\[
X=\sum_{i=1}^{n}\sum_{j=1}^{m}\binom{M_{ij}}2,\qquad
Y=\sum_{i<i'}\sum_{j<j'}M_{ij}M_{ij'}M_{i'j}M_{i'j'}.
\]
Thus \(X\) counts two-edge parallel bundles, and \(Y\) counts four-cycles with distinct edge choices, without discarding multiedges.

If \(\min(d,e)=1\), both counts vanish. For \(d,e\ge2\) and \(L\ge6\), set \([t]_k=t(t-1)\cdots(t-k+1)\),
\[
B=\binom n2\binom m2\frac{[d]_2^2[e]_2^2}{[L]_4},\quad
P_{d,e}(L)=(d+e-4)L^2-(3de-11)L+6de-4d-4e-4.
\]
Then the exact finite-size covariance is
\[
\boxed{\operatorname{Cov}(X,Y)=-\frac{2B P_{d,e}(L)}{(L-5)(L-4)(L-1)}}.
\]
It is positive exactly for \(d=e=2\), \(n=m\ge3\), and negative for all other degrees at least two with \(L\ge6\). The unique small-size exception \(n=m=d=e=2\) has covariance \(-4/9\). For fixed degrees and admissible \(L\to\infty\),
\[
\operatorname{Cov}(X,Y)\sim
\begin{cases}
\frac{1}{2L^2},&d=e=2,\\[3pt]
-\frac{(d-1)^2(e-1)^2(d+e-4)}{2L},&d,e\ge2,\ \max(d,e)>2.
\end{cases}
\]

## Assumptions and scope
All \(n,m,d,e\) are positive integers satisfying \(n,m\ge2\) and \(nd=me\). Every bijection of labelled half-edges has probability \(1/L!\); this is not the uniform law on unlabelled multigraphs and is not the uniform simple biregular graph model. Parallel-edge pairs count as \(\binom{k}2\) when multiplicity is \(k\). A square with multiplicities on its four cells contributes their product. The asymptotic limits hold with \(d,e\) fixed and \(L\) increasing through common multiples of \(d,e\) for which \(n=L/d,m=L/e\ge2\).

## Proof
First, by selecting two distinct stubs at each of one left and one right vertex, and summing the probability of their two prescribed pairings,
\[
\mathbb E X=\frac{L(d-1)(e-1)}{2(L-1)}.
\]
For a square on four distinct vertices, choose two left and two right half-edges at each vertex, assign the edges to the four corresponding vertex pairs, and divide by the ordered matching denominator. Linearity gives
\[
\mathbb E Y=B=\binom n2\binom m2\frac{[d]_2^2[e]_2^2}{[L]_4}.
\]
For \(L\ge6\), fix any one of the labelled four-edge square occurrences contributing to \(Y\). Conditional on the occurrence, the other \(L-4\) stubs on each side are uniformly paired. Each of its two used left vertices has residual degree \(d-2\), and each of its two used right vertices residual degree \(e-2\). Therefore \(X\) comprises two types of pairs: a specified square edge plus a residual parallel edge, and two residual edges. The first has conditional expectation \(4(d-2)(e-2)/(L-4)\), while the second has expectation \(A_dA_e/[2(L-4)(L-5)]\), where
\[
A_d=2[d-2]_2+(n-2)[d]_2=L(d-1)-8d+12,\\
A_e=2[e-2]_2+(m-2)[e]_2=L(e-1)-8e+12.
\]
Consequently every distinguished square occurrence gives the same conditional expectation
\[
Q=\frac{4(d-2)(e-2)}{L-4}+
\frac{[L(d-1)-8d+12][L(e-1)-8e+12]}{2(L-4)(L-5)}.
\]
The conditional matching remains uniform, so \(\mathbb E(XY)=B Q\), not merely an asymptotic factorization. Expanding the rational expression and canceling gives
\[
Q-\mathbb E X=-\frac{2P_{d,e}(L)}{(L-5)(L-4)(L-1)}.
\]
Multiplying by \(B\) proves the exact covariance identity.

To classify signs, let \(a=d-2\) and \(b=e-2\). Algebra yields
\[
P_{d,e}(L)=4-L+(L-2)((a+b)(L-4)-3ab).
\]
If \(a=b=0\), this equals \(4-L<0\) for \(L\ge6\). If, say, \(b=0<a\), it becomes \((L-4)(a(L-2)-1)>0\). If both \(a,b\ge1\), the vertex-count assumptions imply \(L\ge2\max(d,e)=2\max(a,b)+4\); hence \((a+b)(L-4)-3ab\ge ab\), and therefore \(P\ge4-L+ab(L-2)\ge2>0\). Positivity of \(B\) and the denominator proves the dichotomy.

When \(L=4\), \(n=m=d=e=2\) is the only case with degrees at least two. With probability \(2/3\) the multigraph is the simple square \((X,Y)=(0,1)\); with probability \(1/3\) it consists of two doubled opposite edges \((X,Y)=(2,0)\). Direct computation gives covariance \(-4/9\). If either degree is one, no square or parallel pair exists, regardless of size.

Finally \(B\to(d-1)^2(e-1)^2/4\) for fixed degrees. If \(d=e=2\), then \(P=4-L\), giving \(\operatorname{Cov}(X,Y)=2B/((L-5)(L-1))\sim1/(2L^2)\). Otherwise \(P\sim(d+e-4)L^2\), giving the stated negative \(L^{-1}\) asymptotic.

## Verification
All quantities in the proof are rational for finite parameters; the identities can be checked algebraically. The standalone accompanying `verify_cycles.py` enumerates every labelled half-edge matching for seven small admissible models with \(L\le8\), using exact rational arithmetic. The resulting values agree with the exact mean and covariance formulas for the nonexceptional cases, and give \(-4/9\) for the exceptional case. These finite checks corroborate, but are not a substitute for, the all-parameter counting argument and sign proof.

## Relationship to prior work
Dumitriu and Zhu (first posted 2020) study Poisson approximations for short cycles of uniformly random **simple** biregular bipartite graphs, where parallel pairs cannot occur. Angel, van der Hofstad and Holmgren (2016) derive Poisson approximations for self-loops and multiple edges, including the bipartite configuration model, but do not present this exact covariance with edge-distinguished squares. McKay, Wormald and Wysocka analyze asymptotic short-cycle counts in random regular **simple** graphs and discuss the bipartite extension. The present statement concerns finite, uniform stub pairings and a mixed covariance of two distinct short-cycle sizes, including a sharp degree-two sign and decay-rate transition; it does not follow from the cited simple-graph Poisson approximation bounds or the cited marginal multiple-edge estimates.

## Limitations
This theorem concerns the pairing law, not the uniform distribution on simple graphs or equally weighted unlabelled multigraphs. The definition of \(Y\) counts edge-distinguished cycles; the corresponding statistic in the underlying simple support graph has a different law. The fixed-degree asymptotic does not assert uniformity when degrees grow. No assertion of historical priority or independent external certification is made; the related literature may contain an equivalent finite mixed-moment identity not located here.

## References
1. I. Dumitriu and Y. Zhu, *Global eigenvalue fluctuations of random biregular bipartite graphs*, arXiv:2008.11760, first posted 26 August 2020; Section 2, Theorem 2.10.
2. O. Angel, R. van der Hofstad and C. Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172, 2016; Section 1.4, especially the bipartite configuration model.
3. B. D. McKay, N. C. Wormald and B. Wysocka, *Short cycles in random regular graphs*, Electronic Journal of Combinatorics 11 (2004), R66, DOI:10.37236/1819; bipartite extension.
