# Strictly negative triangle–open-triad covariance under a fixed edge count

## Finding

Let \(T\) count unordered triangles and \(W\) count **induced open three-vertex paths**, that is, unordered triples spanning exactly two edges. In a uniformly sampled fixed-edge graph \(G(n,m)\), their covariance has a universal sign. For every integer \(n\ge4\), \(N=\binom n2\), and \(0\le m\le N\), put \(t=\binom n3\) and \(q_3=(m)_3/(N)_3\). Then

\[
\operatorname{Cov}(T,W)=-\frac{6tq_3(N-m)(N-m-1)\big[(n^2-3n-8)m+(n-1)(n^2-n-4)\big]}{(n+1)(n+2)(N-5)(N-4)(N-2)}.
\]

In particular,

\[
\operatorname{Cov}(T,W)<0\quad\Longleftrightarrow\quad 3\le m\le N-2,
\]

and it is zero for all other admissible edge counts. If \(m/N\to p\in(0,1)\), then

\[
\lim_{n\to\infty}n^{-3}\operatorname{Cov}(T,W)=-p^4(1-p)^2.
\]

The fixed-edge sign sharply contrasts with the independent-edge model: for \(G(n,p)\), with fixed \(n\ge4\) and \(0<p<1\),

\[
\operatorname{Cov}_{G(n,p)}(T,W)=3t p^4(1-p)\big[2(n-3)-(3n-8)p\big].
\]

Thus the covariance in \(G(n,p)\) is positive below \(p=2(n-3)/(3n-8)\), zero at that threshold, and negative above. The statement concerns **induced** open paths; for ordinary, non-induced two-edge paths the covariance is a different quantity.

## Assumptions and scope

All graphs are undirected, simple, labeled, and loop-free. The fixed-edge probability law assigns the same probability to each of the \(\binom Nm\) graphs. A triangle is a three-vertex subset with all three possible edges. An induced open path is a three-vertex subset with exactly two edges. Define the ordinary two-star count \(S=\sum_v\binom{\deg(v)}2\); a triangle contributes three ordinary two-stars, so \(W=S-3T\). For nonnegative integer \(j\), \((a)_j=a(a-1)\cdots(a-j+1)\), with \((a)_0=1\). Write \(q_j=(m)_j/(N)_j\) for \(j=2,3,4,5,6\); this is exactly the probability that a specified set of \(j\) distinct potential edges is present. These ratios are well defined for \(n\ge4\), and automatically vanish when \(j>m\).

## Proof

There are \(t=\binom n3\) possible triangles and \(3t\) possible centered two-stars. Consequently \(\mathbb E T=tq_3\) and \(\mathbb E S=3tq_2\). To compute mixed moments, fix a particular triangle. Among the \(3t\) possible two-stars, exactly three have both their edges inside that triangle; exactly \(6(n-3)\) have exactly one edge in the triangle; all remaining \(3t-3-6(n-3)\) share no edge with it. The joint occurrence of a triangle and such a two-star therefore requires respectively three, four, or five distinct edges, giving

\[
\mathbb E(TS)=t\Big[3q_3+6(n-3)q_4+\big(3t-3-6(n-3)\big)q_5\Big].
\]

Similarly, for a fixed triangle, there is one coincident triangle, \(3(n-3)\) triangles sharing exactly one edge, and \(t-1-3(n-3)\) triangles sharing no edge. Therefore

\[
\mathbb E(T^2)=t\Big[q_3+3(n-3)q_5+\big(t-1-3(n-3)\big)q_6\Big].
\]

Since \(W=S-3T\), subtracting the products of expectations gives

\[
\operatorname{Cov}(T,W)=\mathbb E(TS)-3\mathbb E(T^2)-3t^2q_3q_2+3t^2q_3^2.
\]

Substitution of \(q_j=(m)_j/(N)_j\), elimination of denominators, and \(N=n(n-1)/2\) reduce this rational expression to the factored formula in the Finding. No limiting or independence approximation is used in this simplification.

All factors outside the overall minus sign are nonnegative. For \(n\ge5\), the factor \(n^2-3n-8\) is strictly positive and the constant term \((n-1)(n^2-n-4)\) is strictly positive. For \(n=4\), the bracket becomes \(24-4m\), which is positive whenever \(3\le m\le N-2=4\). As the denominator is positive for all \(n\ge4\), the covariance is strictly negative for all and only the stated integer edge counts, and otherwise vanishes by \(q_3=0\) or \((N-m)(N-m-1)=0\).

For the dense limit, \(t\sim n^3/6\), \(N\sim n^2/2\), \(q_3\to p^3\), and the bracket is asymptotic to \(pn^4/2\). Substitution yields \(-p^4(1-p)^2\) after division by \(n^3\). For the independent-edge comparison, replace each \(q_j\) in the two mixed-moment formulas above by \(p^j\), use the same relation \(W=S-3T\), and simplify to the stated expression. The factor \(2(n-3)-(3n-8)p\) has one interior zero for every \(n\ge4\), proving the contrast.

## Verification

The included standalone `verify.py` uses only Python's standard library. It checks the moment formula against the factored formula exactly for thousands of parameter pairs; enumerates every graph on four, five, and six vertices, conditioning on its edge count; and evaluates exact rational independent-edge mixtures to check the second formula. It checks signs at all admissible integer edge counts for sample sizes up to 36. These finite computations corroborate, but do not establish, the unbounded analytic theorem. Reproduce with `python3 verify.py`.

## Relationship to prior work

Reinert and Röllin [1] analyze the joint behavior of ordinary two-star and triangle counts in independent-edge random graphs, including normal approximation; they do not give this induced-triad, fixed-edge, all-sample-size sign theorem. Janson [2] develops broader asymptotic theory for both ordinary and induced subgraph counts in fixed-edge and independent-edge random graphs; that framework may imply moments of the present statistics without explicitly isolating the sign. Dey and Terlov [3] analyze conditional joint wedge and triangle counts and asymptotic Gaussian behavior after fixing the edge count; their general framework is an important potential route to the covariance but does not explicitly state the complete finite-sample sign classification. Goldschmidt, Griffiths, and Scott [4] connect fixed-edge subgraph fluctuations to wedge and triangle statistics, and likewise provide relevant general coverage. The claimed contribution is the exact **all-edge-count negative-sign classification** and **explicit contrast between ensembles**, not the basic mixed-moment technique.

## Limitations

The statement assumes uniform random graphs with a deterministic number of edges. It does not extend unchanged to degree-constrained graph ensembles, directed motifs, or heterogeneous edge probabilities. No new asymptotic central limit theorem is claimed. General orthogonal-decomposition identities might imply the exact covariance and sign after specialized calculations; some older relevant full texts, especially Janson's 1990 article and subsequent monograph, were not available for complete comparison. Historical priority therefore requires independent literature review. The independent-edge contrast is proved for the same induced open-triad statistic, not for non-induced wedges.

## References

1. G. Reinert and A. Röllin, *U-statistics and random subgraph counts: Multivariate normal approximation via exchangeable pairs and embedding*, arXiv:0912.3425 (first public 2009-12-17), *Journal of Applied Probability* **47** (2010), 378–393.
2. S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, *Random Structures & Algorithms* **1** (1990), 15–37, DOI:10.1002/rsa.3240010103.
3. P. S. Dey and G. Terlov, *Stein's method for Conditional Central Limit Theorem*, arXiv:2109.09274 (2021).
4. C. Goldschmidt, S. Griffiths, and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs G(n,m) and G(n,p)*, arXiv:1902.06830 (2019).
