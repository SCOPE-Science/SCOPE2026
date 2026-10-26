# A universal single covariance sign switch between clique counts and induced graph patterns

## Finding

Let \(H\) be an arbitrary simple graph on \(m\ge3\) vertices; fix \(3\le r\le m\), \(n\ge m+r-2\), and \(0<p<1\). Draw \(G\sim G(n,p)\), with independent edge probabilities \(p\). Let \(K_r(G)\) count the subsets of \(r\) vertices spanning complete graphs, and let \(N_H(G)\) count the subsets of \(m\) vertices whose *induced* graph is isomorphic to \(H\). Write \(c_s(H)\) for the number of \(s\)-cliques in \(H\), \(M=\binom m2\), and \(R=\binom r2\). Then

\[
\frac{\operatorname{Cov}(K_r(G),N_H(G))}{\mathbb E[N_H(G)]p^R}
=\sum_{s=2}^{r}\binom{n-m}{r-s}\left(c_s(H)p^{-\binom s2}-\binom ms\right).
\]

If \(H\) has no edges, this covariance is strictly negative for every \(p\in(0,1)\); if \(H\) is complete, it is strictly positive. For every remaining \(H\), with \(0<c_2(H)<M\), there exists **exactly one** \(p_*(H,n,r)\in(0,1)\) where the covariance vanishes; the covariance is positive for \(p<p_*\) and negative for \(p>p_*\). Thus no nontrivial induced graph pattern can exhibit multiple covariance sign reversals against any fixed clique count as the edge probability varies.

For fixed \(H,r\) and \(n\to\infty\), letting \(\rho=c_2(H)/M\), \(B=\binom m3\), and \(t=c_3(H)\),

\[
p_*(H,n,r)=\rho+\frac{r-2}{n-m}\frac{t-B\rho^3}{M\rho^2}+O_{H,r}((n-m)^{-2}).
\]

For \(r=3\) this comparison of the critical point with \(\rho\) is exact at finite \(n\): \(\operatorname{sgn}(p_* -\rho)=\operatorname{sgn}(t-B\rho^3)\), with equality permitted. The direction of the threshold displacement is therefore determined by triangle excess relative to the independent-edge baseline.

A concrete distinction: take \(H_1=C_5\) and let \(H_2\) be the disjoint union of an isolated vertex and \(K_4\) with one edge deleted. Both have five vertices and five edges, but their triangle counts are zero and two. At \(p=1/2\), for \(n=6,r=3\), the covariances are \(-45/512\) and \(135/1024\), respectively; for \(n=7,r=4\), they are \(-1575/16384\) and \(2205/32768\). Thus motifs of the same order and edge density can have opposite associations with clique counts.

## Assumptions and scope

All graphs are finite, labelled in the random experiment, simple, undirected, and without loops. An induced copy is counted once for each eligible vertex subset, not once per embedding. The restrictions \(m\ge3\), \(3\le r\le m\), and \(n\ge m+r-2\) are essential to the stated uniform three-way sign classification: the last ensures that the two-vertex overlap contribution is present. No assertion of single crossing is made outside these parameter restrictions. \(p\) ranges over the open interval \((0,1)\); at endpoints the induced pattern's expectation can vanish.

The induced-copy expectation, always strictly positive in this domain, is
\[
\mathbb E[N_H(G)]=\binom nm\frac{m!}{|\operatorname{Aut}(H)|}
 p^{c_2(H)}(1-p)^{M-c_2(H)}.
\]

## Proof

Fix an \(m\)-vertex set \(S\) and let \(I_S\) indicate that its induced graph is isomorphic to \(H\). Conditional on \(I_S=1\), the restriction of \(G\) to \(S\) is a uniformly chosen labelled realization of \(H\); edges with at least one endpoint outside \(S\) remain independent Bernoulli\((p)\) variables. An \(r\)-subset \(A\) meeting \(S\) in exactly \(s\) vertices has conditional probability \(\mathbb P(A\text{ is a clique}\mid I_S=1)\) equal to \(p^{R-\binom s2}\) times the probability that the induced \(s\)-subset of the chosen realization is complete. Summing over all \(s\)-subsets of \(S\), that probability's numerator is exactly \(c_s(H)\). There are \(\binom{n-m}{r-s}\) choices of the external vertices. Intersections of size zero or one do not constrain any clique edge; their conditional and unconditional expectations agree. Consequently

\[
\mathbb E[K_r(G)\mid I_S=1]-\mathbb E[K_r(G)]
=\sum_{s=2}^r\binom{n-m}{r-s}
\left(c_s(H)p^{R-\binom s2}-\binom ms p^R\right).
\]

Exchangeability makes the right side independent of \(S\). Using
\(\operatorname{Cov}(K_r,I_S)=\mathbb E[I_S](\mathbb E[K_r\mid I_S=1]-\mathbb E[K_r])\), summing over \(S\), and dividing by the strictly positive expectation proves the exact identity.

Define the right-hand normalized covariance as \(F(p)\). If \(H\) is empty, all \(c_s(H)=0\), and every bracket is negative; if \(H\) is complete, \(c_s(H)=\binom ms\), and every bracket is positive because \(p^{-\binom s2}>1\). The coefficients \(\binom{n-m}{r-s}\) are strictly positive under the scope conditions. If \(0<c_2(H)<M\), direct differentiation gives

\[
F'(p)=-\sum_{s=2}^r\binom{n-m}{r-s}
\binom s2\,c_s(H)p^{-\binom s2-1}<0,
\]

because the \(s=2\) term is strictly negative. Moreover \(F(p)\to+\infty\) as \(p\downarrow0\) and
\(F(1)=\sum_{s=2}^r\binom{n-m}{r-s}(c_s(H)-\binom ms)<0\), since the \(s=2\) deficit is strict. Continuity and strict decrease prove a unique zero with the stated sign pattern.

For the asymptotics, put \(q=n-m\) and \(\rho=c_2(H)/M\in(0,1)\). Dividing \(F\) by \(\binom q{r-2}\) gives

\[
0=\frac{c_2(H)}{p}-M+
\frac{r-2}{q-r+3}\left(\frac{c_3(H)}{p^3}-B\right)+O_{H,r}(q^{-2}),
\]

uniformly for \(p\) in a fixed neighbourhood of \(\rho\). The terms \(s\ge4\) have coefficient ratios \(O_{H,r}(q^{-2})\). Strict monotonicity shows \(p_*\to\rho\). Substituting \(p_* =\rho+O(q^{-1})\) and expanding the first term to first order yields the displayed expansion. For \(r=3\) every term beyond \(s=3\) vanishes, and evaluating the exact \(F\) at \(p=\rho\) gives \(F(\rho)=c_3(H)\rho^{-3}-B\). Because \(F\) is decreasing, this proves the exact sign comparison. The two example covariances follow by counting induced-copy labelings and substituting into the same identity.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter. The file uses only the standard library. It independently enumerates all graphs on up to six labelled vertices, computes the covariance directly with rational weights at three probabilities, and compares it against the claimed overlap formula for 168 cases. It also calculates the contrasting order-five motif covariances stated above. The finite checks are not relied upon for the infinite-family theorem, which is proved above.

## Relationship to prior work

Graph-factor expansions and dependence among random subgraph counts are established methods. In particular Sah and Sawhney (arXiv:2006.11369, first posted June 19, 2020) develop induced-count expansions and study exceptional edge densities for local limit theorems, while Goldschmidt, Griffiths, and Scott (arXiv:1902.06830, first posted February 18, 2019) analyze subgraph-count deviations through graph overlaps. Bhattacharya, Das, and Mukherjee (arXiv:2011.03026, first posted November 5, 2020) develop statistical motif-count estimation under vertex sampling. These general techniques and the elementary overlap calculation are not claimed as new. The result isolated here is the **universal unique covariance sign crossing** for arbitrary induced \(H\) against every clique size \(r\), together with its critical-location hierarchy and equal-edge-density, opposite-sign examples. The inspected material does not explicitly give this all-pattern sign classification; priority remains provisional.

## Limitations

The result concerns covariance, not stochastic ordering, independence, higher moments, or statistical identifiability. The expansion is for fixed \(H,r\) and growing \(n\), not for a growing motif. The theorem applies to independent-edge binomial random graphs, not fixed-edge graphs; the latter can have different covariance signs. Established general graph Fourier and subgraph-overlap methods may imply further specializations, so exhaustive priority is not certified. The verification enumerates finitely many graphs and is not an independent infinite proof. No independent audit has been performed.

## References

1. A. Sah and M. Sawhney, *Local limit theorems for subgraph counts*, arXiv:2006.11369 (first posted 2020-06-19), Sections 2.5 and 6; published J. London Math. Soc. 105 (2022), 950–1011.
2. C. Goldschmidt, S. Griffiths, and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs G(n,m) and G(n,p)*, arXiv:1902.06830 (first posted 2019-02-18), Sections 1–2 and 7.
3. B. B. Bhattacharya, S. Das, and S. Mukherjee, *Motif Estimation via Subgraph Sampling: The Fourth Moment Phenomenon*, arXiv:2011.03026 (first posted 2020-11-05), Sections 1–2.
