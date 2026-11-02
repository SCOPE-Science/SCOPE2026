# Universal fixed-edge anticorrelation and a binomial sign transition for triangle–open-wedge counts

## Finding
For every integer \(n\ge4\), let \(N=\binom n2\) and \(B=\binom n3\). Given a graph \(G\) on \(n\) labeled vertices, let \(T\) count triangles and \(W\) count induced three-vertex paths (unordered triples having **exactly two** of their three possible edges). In the uniform fixed-edge random graph \(G(n,m)\), the covariance obeys the strict law
\[
\operatorname{Cov}(T,W)<0\quad\Longleftrightarrow\quad 3\le m\le N-2,
\]
and is zero at the five edge levels \(m\in\{0,1,2,N-1,N\}\), understood as a set, so coincident boundary values count only once.

More precisely, write \(q_j=(m)_{\underline j}/(N)_{\underline j}\) for \(0\le j\le N\), with \(q_j=0\) if \(m<j\). Then
\[
\operatorname{Cov}_{G(n,m)}(T,W)
=-\frac{48Bq_3(N-m)(N-m-1)\,[m(n^2-3n-8)+(n-1)(n^2-n-4)]}
{(n+1)(n+2)(n^2-n-10)(n^2-n-8)(n^2-n-4)}.
\]

By contrast, for the independent-edge graph \(G(n,p)\), for every \(0\le p\le1\),
\[
\operatorname{Cov}_{G(n,p)}(T,W)
=3Bp^4(1-p)\big[(n-3)(2-3p)-p\big].
\]
For \(0<p<1\) this covariance is positive precisely when \(p<2(n-3)/(3n-8)\), zero at that single interior threshold, and negative above it. Consequently, fixing the edge total reverses the sparse-regime positive covariance into strict negative covariance at every nondegenerate fixed-edge level.

## Assumptions and scope
The vertex set is \([n]\); all induced paths are counted by their unordered three-vertex support, not by orientations or choices of center. A triangle contributes one to \(T\) and zero to \(W\) on its own triple. The fixed-edge law selects each of the \(\binom{N}{m}\) graphs with \(m\) edges equally. The independent-edge law makes the \(N\) edges independent Bernoulli variables of common parameter \(p\). No sparsity, large-order limit, or connectivity hypothesis is imposed.

## Proof
Put \(B=\binom n3\) and let \(I_A\) and \(J_A\) be the triangle and induced-open-wedge indicators of a three-vertex subset \(A\). Under \(G(n,m)\), every prescribed collection of \(j\) present edges has probability \(q_j=(m)_{\underline j}/(N)_{\underline j}\), and a set of \(j\) required present edges with one further edge required absent has probability \(q_j-q_{j+1}\). In particular, \(\mathbb EI_A=q_3\) and \(\mathbb EJ_A=3(q_2-q_3)\).

For ordered pairs \((A,C)\) of triples, if \(A=C\), then \(I_AJ_C=0\). If \(A\) and \(C\) have exactly two vertices in common, their edge sets overlap in one edge. Conditional on the triangle at \(A\), that shared edge is present; for \(C\) to be an induced open wedge exactly one of its two other edges must be present. Hence \(\mathbb E[I_AJ_C]=2(q_4-q_5)\), and each \(A\) has exactly \(3(n-3)\) such \(C\). If the triples share at most one vertex, their three-edge sets are disjoint, and \(\mathbb E[I_AJ_C]=3(q_5-q_6)\); there are \(L=B-1-3(n-3)\) such \(C\). When a falling-factorial index exceeds \(N\), its contribution has zero coefficient in this enumeration; the formula below is still well-defined for every \(n\ge4\) because \(N\ge6\).

Summation and subtraction of the product of means give
\[
\operatorname{Cov}(T,W)=B\{6(n-3)(q_4-q_5)+3L(q_5-q_6)-3Bq_3(q_2-q_3)\}.
\]
For \(m\ge3\), set \(q_3=(m)_3/(N)_3\). The ratio identities imply
\[
q_4-q_5=q_3\,\frac{(m-3)(N-m)}{(N-3)(N-4)},\qquad
q_5-q_6=q_3\,\frac{(m-3)(m-4)(N-m)}{(N-3)(N-4)(N-5)},
\]
and
\[
q_2-q_3=\frac{m(m-1)(N-m)}{N(N-1)(N-2)}.
\]
Factoring the common positive terms yields the expression displayed in Finding. Its polynomial identity can also be verified by common-denominator expansion of the preceding exact covariance formula.

The denominator in that factorization is strictly positive for \(n\ge4\). Its last bracket \(H=m(n^2-3n-8)+(n-1)(n^2-n-4)\) is strictly positive throughout the claimed range: for \(n\ge5\), both terms are nonnegative and the second is positive; for \(n=4\), \(H=24-4m>0\) at \(3\le m\le4\). Thus the factorization is strictly negative exactly when \(3\le m\le N-2\). At \(m\le2\), triangles are impossible; at \(m=N-1\), every graph is a complete graph with one omitted edge, so both \(T\) and \(W\) are deterministic; at \(m=N\), \(W=0\).

For \(G(n,p)\), disjoint edge sets are independent. For \(A=C\), \(\operatorname{Cov}(I_A,J_C)=-3p^5(1-p)\). For \(|A\cap C|=2\), the covariance is \(p^4(1-p)(2-3p)\), since \(\mathbb E I_AJ_C=2p^4(1-p)\). All other triple pairs have zero covariance. Counting gives the displayed binomial expression, with a unique interior zero \(p=2(n-3)/(3n-8)\). Its endpoints are \(0\) and \(1\), where both statistics are deterministic. At the interior zero the statistics need not be independent: \(T=B\) forces \(W=0\), whereas \(W>0\) occurs with positive probability.

## Verification
Run the bundled standalone Python 3 script \(`verify.py`\) without nonstandard dependencies. It enumerates all \(2^{\binom n2}\) labeled graphs for \(n\in\{4,5,6\}\) and calculates all fixed-edge covariances using rational arithmetic, testing the orbit enumeration, factorization, boundary cases, and strict sign. It separately tests the independent-edge formula for three rational values of \(p\) per dimension. Finally it checks the equality of the two exact fixed-edge formulas and the sign law for every \(4\le n\le40\) and every possible \(m\). The recorded execution passed over 33,856 enumerated graphs and 21,497 exact identities. These finite checks are not used as a substitute for the symbolic proof.

## Relationship to prior work
Random-graph triangle counts, wedge and clustering statistics, and motif enumeration are established objects. Chatterjee and Varadhan (2010) investigate independent-edge triangle large deviations; Seshadhri, Pinar and Kolda (2013) analyze wedge sampling for triangle/clustering estimation; Bubeck, Ding, Eldan and Rácz (2014) use signed triangles for graph testing; and Klusowski and Wu (2018) analyze motif estimators from subsampled fixed graphs. These bodies of work provide motivations and comparison points, but the inspected text did not supply the joint fixed-edge triangle/induced-open-wedge covariance law or the strict all-level sign comparison with \(G(n,p)\). An open wedge here excludes closed triangles, whereas some prior work calls every two-edge path a wedge even within a triangle. The distinction affects both the statement and the covariance.

## Limitations
The result is confined to homogeneous independent-edge \(G(n,p)\) and uniform fixed-size \(G(n,m)\) models; it does not assert analogous signs for inhomogeneous graphs, dependent-edge random graphs, or conditioned-degree models. The covariance zero at the interior binomial threshold is not independence. Exact precedence in the broader subgraph-count and network-motif moment literature cannot be guaranteed from the inspected sources. Independent mathematical validation has not been performed.

## References
- Chatterjee, S., and Varadhan, S. R. S. (2010), *The large deviation principle for the Erdős–Rényi random graph*, arXiv:1008.1946, first posted 2010-08-11, https://arxiv.org/abs/1008.1946.
- Seshadhri, C., Pinar, A., and Kolda, T. G. (2013), *Wedge Sampling for Computing Clustering Coefficients and Triangle Counts on Large Graphs*, arXiv:1309.3321, first posted 2013-09-12, https://arxiv.org/abs/1309.3321.
- Bubeck, S., Ding, J., Eldan, R., and Rácz, M. (2014), *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713, first posted 2014-11-20, https://arxiv.org/abs/1411.5713.
- Klusowski, J. M., and Wu, Y. (2018), *Counting Motifs with Graph Sampling*, PMLR 75, https://proceedings.mlr.press/v75/klusowski18a.html.
