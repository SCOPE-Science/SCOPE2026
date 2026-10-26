# Sharp triangle–open-triad covariance reversal under edge-count conditioning

## Finding

Let \(T\) count complete three-vertex subgraphs and \(P\) count vertex triples inducing exactly two edges (open triads). For every integer \(n\ge 4\), write \(M=\binom n2\). Under the uniform fixed-edge model \(G(n,m)\), the covariance is **strictly negative** for every integer \(3\le m\le M-2\), and it vanishes at every other allowable \(m\). Throughout its nonzero range the exact formula is

\[\operatorname{Cov}(T,P)=-\frac{4m(m-1)(m-2)(M-m)(M-m-1)\bigl[(n-1)(n^2-n-4)+m(n^2-3n-8)\bigr]}{(n+1)^2(n+2)(M-5)(M-4)(M-2)^2}.\]

This contrasts sharply with the independent-edge model \(G(n,p)\), where for every real \(0<p<1\),

\[\operatorname{Cov}(T,P)=3\binom n3 p^4(1-p)\bigl[2(n-3)-(3n-8)p\bigr].\]

Consequently \(\operatorname{Cov}(T,P)\) in \(G(n,p)\) is positive, zero, and negative according as \(p\) is below, equal to, or above \(p_*(n)=2(n-3)/(3n-8)\). In particular \(p_*(4)=1/2\), and \(p_*(n)\to2/3\). Conditioning on an exact edge count thus changes positive covariance to strict negative covariance throughout the low-density regime.

## Assumptions and scope

The graphs are undirected, labeled, simple graphs on \(n\) vertices. The count \(P\) includes each **induced** three-vertex path once, rather than counting all noninduced two-edge walks. The fixed-edge model assigns equal probability to every graph having exactly \(m\) edges, with \(0\le m\le M\). The independent-edge model includes each of the \(M\) possible edges independently with probability \(p\). All covariance statements refer to the unnormalized integer motif counts \(T\) and \(P\).

## Proof

Write \(A=\binom n3\) and let \(W=\sum_v\binom{\deg(v)}2\), the noninduced two-edge path count. On any simple graph, \(W=P+3T\); thus \(\operatorname{Cov}(T,P)=\operatorname{Cov}(T,W)-3\operatorname{Var}(T)\).

For a fixed potential triangle, among the \(3A\) potential (unoriented) two-edge paths, exactly three use two of its edges, exactly \(6(n-3)\) use exactly one of its edges, and the remaining \(3A-3-6(n-3)\) use neither. These cases require respectively three, four and five distinct present edges. For a fixed triangle, among the \(A\) possible triangles, exactly one is itself, \(3(n-3)\) share one edge, and \(A-1-3(n-3)\) share no edges; the corresponding union sizes are three, five and six.

For \(G(n,m)\) set \(q_r=(m)_r/(M)_r\) for \(r\le m\), and \(q_r=0\) for \(r>m\). Because the probability that any prescribed \(r\) distinct edges all occur is \(q_r\), the classifications give

\[\begin{aligned}
\operatorname{Cov}(T,W)&=A\bigl[3q_3+6(n-3)q_4+(3A-3-6(n-3))q_5-3Aq_3q_2\bigr],\\
\operatorname{Var}(T)&=A\bigl[q_3+3(n-3)q_5+(A-1-3(n-3))q_6-Aq_3^2\bigr].
\end{aligned}\]

Substitute these two expressions in the identity for \(\operatorname{Cov}(T,P)\), clear the nonzero denominators when \(3\le m\le M-2\), and factor the resulting polynomial: the outcome is precisely the displayed fixed-edge formula. The factorization is an identity of rational functions in the integer parameters and was also checked symbolically and by an exact-independent implementation.

The factors \(m(m-1)(m-2)(M-m)(M-m-1)\) and the denominator are positive on that range. For \(n\ge5\), both terms in the square bracket are positive because \(n^2-3n-8\ge2\) and \(n^2-n-4>0\). For \(n=4\), the bracket reduces to \(24-4m>0\) for the only allowed values \(m=3,4\). Thus the covariance is strictly negative. If \(m\le2\), then \(T\equiv0\); if \(m\ge M-1\), then \(P\) is deterministic (\(n-2\) when one edge is missing, zero when none is missing). These prove all boundary cases.

For \(G(n,p)\), the same classification is exact with \(q_r=p^r\). Substitution and cancellation now yield the second displayed formula. For \(n\ge4\), the threshold \(2(n-3)/(3n-8)\) lies strictly between zero and one, so the strict sign trichotomy follows.

## Verification

The standalone program `CHECK.py` independently implements the overlap-based rational expectations and the factored fixed-edge expression. It checks their equality for all integers \(4\le n\le19\) and all \(0\le m\le\binom n2\), and exhaustively enumerates all graphs on four, five and six vertices to calculate covariance by direct moment averaging. Separate symbolic rational-factorization calculations verified both displayed identities. These finite checks corroborate the preceding parameter-uniform proof; they are not substituted for it.

## Relationship to prior work

Berkowitz (arXiv:1610.01281) studies a quantitative local limit theorem for triangle counts in \(G(n,p)\). Goldschmidt, Griffiths and Scott (arXiv:1902.06830) develop martingale decompositions for the noninduced two-edge-path and triangle counts in \(G(n,m)\) and related conditional covariance approximations, notably Section 7, Proposition 7.1; their Lemma 2.7 also gives a general induced-subgraph inclusion–exclusion identity. Alvarado, de Oliveira and Griffiths (arXiv:2305.04326) develop moderate deviations and also examine noninduced two-edge paths. Those statements provide relevant general techniques and overlapping objects. The checked portions do not state the universal finite-parameter strict negative sign of the **induced** triad covariance nor the exact contrasting \(G(n,p)\) sign transition. Such general techniques may nevertheless give alternative derivations.

## Limitations

The theorem concerns covariance, not negative association, negative regression or stochastic ordering. It does not address vertex sampling, heterogeneous edge probabilities, random regular graphs or larger induced motifs. Broad general subgraph covariance methods are available in earlier literature, so no assertion is made that every algebraic ingredient or every consequence is historically new. The closest foundational literature, including Janson's 1990/1994 random-graph-statistic theory, was not available in full for exhaustive historical-priority comparison.

## References

- R. Berkowitz, *A Quantitative Local Limit Theorem for Triangles in Random Graphs*, arXiv:1610.01281 (first submitted 2016-10-05), https://arxiv.org/abs/1610.01281.
- C. Goldschmidt, S. Griffiths, and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs G(n,m) and G(n,p)*, arXiv:1902.06830 (2019), https://arxiv.org/abs/1902.06830.
- J. D. Alvarado, L. G. de Oliveira, and S. Griffiths, *Moderate deviations of triangle counts in sparse Erdős–Rényi random graphs G(n,m) and G(n,p)*, arXiv:2305.04326 (2023), https://arxiv.org/abs/2305.04326.
- S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms 1 (1990), 15–37, DOI:10.1002/rsa.3240010103.
