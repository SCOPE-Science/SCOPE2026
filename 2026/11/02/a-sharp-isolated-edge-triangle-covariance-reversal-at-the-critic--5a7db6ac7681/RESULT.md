# A sharp isolated-edge–triangle covariance reversal at the critical edge count

## Finding

Let \(n\ge5\), and let \(J\) count **isolated-edge components**, i.e. connected components consisting of exactly two vertices joined by one edge, in a uniformly random simple graph. Let \(T\) count its (not necessarily induced) triangles. Set \(N=\binom n2\) and \(Q=\binom{n-2}2\).

In the uniform fixed-edge model \(G(n,m)\), if \(3\le m\le Q+1\), define
\[
A_n=\frac4{3(n-1)(n^2-5n+2)},\qquad B_n=\frac4{3(n+1)(n^2-n-4)}.
\]
Then
\[
\operatorname{Cov}(J,T)=\mathbb E[J](m-1)(m-2)\bigl[A_n(m-3)-B_nm\bigr],\qquad
\mathbb E[J]=N\frac{\binom Q{m-1}}{\binom Nm}.
\]
Here \(\mathbb E[J]>0\). The exact sign transition is
\[
\operatorname{Cov}(J,T)<0\quad(3\le m\le\lceil n/2\rceil),
\qquad
\operatorname{Cov}(J,T)>0\quad(\lceil n/2\rceil+1\le m\le Q+1).
\]
For \(m\le2\) or \(m>Q+1\), the covariance is zero. There are **no** equality cases in the displayed nondegenerate interval.

By contrast, in the independent-edge model \(G(n,p)\), for \(0<p<1\),
\[
\operatorname{Cov}(J,T)=-\binom n2(n-2)^2p^4(1-p)^{2n-4}<0.
\]
Consequently fixing the edge count creates a positive-covariance regime that cannot occur with independent edges.

In the sparse window \(m=\lfloor cn/2\rfloor\), \(c>0\) fixed, the fixed-edge covariance converges to
\[
\lim_{n\to\infty}\operatorname{Cov}_{G(n,m)}(J,T)=\frac{c^3(c-1)e^{-2c}}2.
\]
For \(p=c/n\) (and sufficiently large \(n\)), the independent-edge covariance instead converges to \(-c^4e^{-2c}/2\). The positive fixed-edge regime starts immediately after \(\lceil n/2\rceil\) edges.

## Assumptions and scope

A simple graph has vertex set \(\{1,\ldots,n\}\). The model \(G(n,m)\) chooses uniformly from the \(\binom Nm\) graphs with exactly \(m\in\{0,\ldots,N\}\) edges. The model \(G(n,p)\) includes each potential edge independently with probability \(p\). An isolated-edge component has both endpoints of degree exactly one. A triangle uses three edges among a vertex triple. Covariance is with respect to the specified random-graph law, with no asymptotic assumptions unless stated.

## Proof

**1. Conditioning in the fixed-edge model.** Fix a possible edge \(e=\{u,v\}\) and let \(I_e\) indicate that \(e\) forms an isolated-edge component. If \(I_e=1\), every other edge touching \(u\) or \(v\) is absent, and the other \(m-1\) chosen edges form a uniform subset of the \(Q\) edges among the remaining \(n-2\) vertices. Thus
\[
\Pr(I_e=1)=\frac{\binom Q{m-1}}{\binom Nm},\qquad
\mathbb E[T\mid I_e=1]=\binom{n-2}3\frac{(m-1)_3}{(Q)_3},
\]
where \((a)_3=a(a-1)(a-2)\). The first expression is positive precisely when \(1\le m\le Q+1\). Unconditionally,
\[
\mathbb ET=\binom n3\frac{(m)_3}{(N)_3}.
\]
Since \(J=\sum_e I_e\) and all edge positions are exchangeable,
\[
\operatorname{Cov}(J,T)=\mathbb E[J]\left[\binom{n-2}3\frac{(m-1)_3}{(Q)_3}-\binom n3\frac{(m)_3}{(N)_3}\right].
\]
For \(n\ge5\) the denominators are positive and direct cancellation gives \(A_n\) and \(B_n\) above. Factoring \((m-1)(m-2)\) gives the exact formula. If \(m\le2\), then \(T=0\); if \(m>Q+1\), then \(J=0\). This proves the boundary cases.

**2. Sharp sign.** Explicitly,
\[
A_n-B_n=\frac{8(3n^2-6n-1)}{3(n-1)(n+1)(n^2-5n+2)(n^2-n-4)}>0.
\]
The linear factor \(A_n(m-3)-B_nm\) changes sign only at
\[
m_*=\frac{3A_n}{A_n-B_n}=\frac n2+1-\frac{n+5}{3n^2-6n-1}.
\]
For every integer \(n\ge5\), elementary inequalities give \(\lceil n/2\rceil<m_*<\lceil n/2\rceil+1\). Indeed, for even \(n\), \(0<(n+5)/(3n^2-6n-1)<1\); for odd \(n\), this fraction is strictly between \(0\) and \(1/2\). The stated sign division follows, because the prefactor is strictly positive throughout \(3\le m\le Q+1\).

**3. Independent edges.** A specified isolated-edge event has probability \(p(1-p)^{2n-4}\). Given that event, triangles can lie only among the remaining \(n-2\) vertices and appear with independent-edge probability \(p^3\). Thus
\[
\operatorname{Cov}(J,T)=\binom n2p(1-p)^{2n-4}\left[\binom{n-2}3-\binom n3\right]p^3.
\]
The binomial-coefficient difference equals \(-(n-2)^2\), establishing the strict negative formula when \(0<p<1\).

**4. Sparse limits.** With \(m=\lfloor cn/2\rfloor\), fixed \(c>0\),
\[
\mathbb E[J]\sim\frac{cn}{2}e^{-2c},\quad
A_n-B_n\sim\frac8{n^4},\quad
m-m_*\sim\frac{(c-1)n}{2}\ \ (c\ne1),
\]
while \(m-m_*=O(1)\) for \(c=1\). Substitute \(A_n(m-3)-B_nm=(A_n-B_n)(m-m_*)\) into the exact covariance to obtain the stated limit for all fixed \(c>0\), including \(c=1\). For independent edges, substitute \(p=c/n\) into the exact formula and use \((1-c/n)^{2n-4}\to e^{-2c}\).

## Verification

The included dependency-free `verify.py` enumerates all \(2^{10}=1024\) labeled graphs of order \(5\) and all \(2^{15}=32768\) labeled graphs of order \(6\), computing covariance exactly for every edge count. It also checks the independent-edge formula at two rational densities and the algebraic threshold identity and strict bounds at one hundred further sizes. Running `python3 verify.py` gives `PASS: all exact finite checks, including 327 identity/inequality assertions`. These are finite cross-checks; the proof above establishes the infinite family of formulas.

## Relationship to prior work

The classical uniform random-graph process and its edge-count scaling appear in Amir, Gurel-Gurevich, Lubetzky and Singer (2005), who study isolated **vertices**, susceptibility and giant-component emergence, not this cross-covariance of isolated-edge components with triangles. Chatterjee (2010) establishes sharp triangle-count upper-tail bounds in \(G(n,p)\), which do not determine the present joint covariance in either random-graph model. Existing published work also studies the covariance of **total connected-component count** with triangles in independent-edge percolation; that statistic is not the number of size-two components and does not imply the fixed-edge sign change. A previously obtained isolated-**vertex**/subgraph covariance formula concerns a different variable and does not cover isolated-edge components.

## Limitations

The formula concerns simple homogeneous Erdős–Rényi graphs, not degree-constrained, weighted or inhomogeneous graphs. Covariance sign alone does not imply stochastic monotonicity or causation. The sparse limit is for fixed \(c\). The apparent coincidence of the sign switch with the familiar critical edge-count scale is a mathematical location comparison, not a proof of a dynamical mechanism. Although relevant accessible sources were inspected and a semantic search for equivalents was conducted, unexamined historical mixed-moment results may contain an equivalent identity; novelty is not externally certified.

## References

1. G. Amir, O. Gurel-Gurevich, E. Lubetzky and A. Singer, *Giant Components in Biased Graph Processes*, arXiv:math/0511526, first public version 21 November 2005. Full text: https://arxiv.org/html/math/0511526v2 .
2. S. Chatterjee, *The missing log in large deviations for triangle counts*, arXiv:1003.3498, first public version 18 March 2010. Full text: https://arxiv.org/html/1003.3498v3 .
3. J. H. Kim and V. H. Vu, *Divide and conquer martingales and the number of triangles in a random graph*, Random Structures & Algorithms 24 (2004), 166–174, doi:10.1002/rsa.10113 (bibliographic record and abstract checked, not full text).
