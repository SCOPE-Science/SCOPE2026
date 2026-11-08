# A narrow positive-covariance window for degree-one counts on the two sides of sparse bipartite graphs

## Finding
Let \(n\ge2\), \(0\le k\le n^2\), and choose uniformly a simple bipartite graph with two labeled parts of \(n\) vertices each and exactly \(k\) edges. Let \(L\) and \(R\) be the numbers of degree-one vertices in the first and second parts, respectively. Put \(N=n^2\), \(A=n^2-n\), and \(B=(n-1)^2\); define \(\binom ab=0\) for integers \(b<0\) or \(b>a\). Then
\[
P_{n,k}=\frac{n\binom A{k-1}}{\binom Nk},\qquad
J_{n,k}=\frac{\binom B{k-1}+B\binom B{k-2}}{\binom Nk},
\]
and the **exact finite-size covariance** is
\[
\boxed{\operatorname{Cov}(L,R)=n^2\bigl(J_{n,k}-P_{n,k}^2\bigr).}
\]

For every fixed \(c>0\), if integers \(k_n\) obey \(k_n/n\to c\), then
\[
\boxed{\operatorname{Cov}(L,R)\longrightarrow
-\tfrac12 c^2(c-2)^2e^{-2c}.}
\]
In particular the limiting covariance is strictly negative whenever \(c\ne2\). The vanishing at \(c=2\) hides a narrower, positive-dependence phase. For every fixed real \(x\), if integers \(k_n\) satisfy
\[
\frac{k_n-2n}{\sqrt n}\longrightarrow x,
\]
then
\[
\boxed{n\,\operatorname{Cov}(L,R)\longrightarrow
 e^{-4}\left(\frac83-2x^2\right).}
\]
Consequently, for all sufficiently large \(n\), the covariance is positive when \(|x|<2/\sqrt3\), and negative when \(|x|>2/\sqrt3\). At the two boundary values, the displayed limit is zero and does not determine the finite-size sign.

## Assumptions and scope
The sampling distribution is uniform over all \(\binom{n^2}{k}\) subsets of the edges of \(K_{n,n}\), with **a fixed exact edge count**; it is not an independent-edge graph model or a fixed-degree-sequence model. The two degree-one counts include all vertices of degree exactly one and exclude isolated vertices. The exact identity applies for every listed \(n,k\). The first limit is for fixed positive \(c\), and the critical-window limit is for a fixed real \(x\) and the specified integer sequences. The corresponding MSC2020 classification is 60C05, combinatorial probability.

## Proof
For one specified vertex on the left, exactly one of its \(n\) incident edges must be chosen; all other \(k-1\) selected edges lie among the \(A=n^2-n\) nonincident edges. Hence its degree-one probability equals \(P_{n,k}\). For a specified left vertex and specified right vertex, split into two disjoint cases. If their common edge is selected, the other \(k-1\) edges must lie in the \(B=(n-1)^2\) cells outside their row and column, contributing \(\binom B{k-1}\) graphs. If their common edge is absent, we must select one edge among the \(n-1\) other cells in that row and one among the \(n-1\) other cells in that column, then \(k-2\) from the remaining \(B\) cells; this contributes \(B\binom B{k-2}\). Their joint degree-one probability is \(J_{n,k}\). Summing the \(n^2\) exchangeable cross-part indicator covariances proves the exact identity, including the endpoint conventions.

For the limits let \(k=cn\) for an \(n\)-dependent \(c\) staying in any fixed compact subinterval of \((0,\infty)\). For large \(n\), \(P_{n,k}>0\) and \(B-k+2>0\). Direct cancellation of binomial coefficients in the preceding identity yields the exact factorization
\[
Q_{n,k}:=\frac{J_{n,k}}{P_{n,k}^2}
=\left(1+\frac{(k-1)(k-2)}{k(B-k+2)}\right)
\prod_{j=0}^{k-2}\left(1-\frac{B}{(A-j)^2}\right).
\]
The cancellation follows by factoring \((A-j)^2-B=(B-j)(N-1-j)\) in each product term and reducing the binomial coefficients. This factorization isolates the competition between a shared-cell effect (the first factor) and fixed-edge depletion (the product). Write \(c=k/n\). An expansion uniform on each such compact interval gives
\[
\begin{aligned}
\log\left(1+\frac{(k-1)(k-2)}{k(B-k+2)}\right)
&=\frac c n+\frac{c^2/2+2c-3}{n^2}
+\frac{c^3/3+2c^2+c-6+2/c}{n^3}+O(n^{-4}),\\
\sum_{j=0}^{k-2}\log\left(1-\frac{B}{(A-j)^2}\right)
&=-\frac c n+\frac{1-c^2}{n^2}
+\frac{-c^3-c^2+5c/2}{n^3}+O(n^{-4}).
\end{aligned}
\]
For completeness, put \(u_j=B/(A-j)^2\). Uniformly for \(0\le j<k=O(n)\), the elementary Taylor identity
\[
u_j=\frac1{n^2}+\frac{2j}{n^4}
+\frac{2j}{n^5}+\frac{3j^2}{n^6}
+O(n^{-5})
\]
holds. Hence
\[
\sum_{j=0}^{k-2}\log(1-u_j)=
-\frac{k-1}{n^2}-\frac{(k-1)(k-2)}{n^4}
-\frac{(k-1)(k-2)}{n^5}
-\frac{(k-1)(k-2)(2k-3)}{2n^6}
-\frac{k-1}{2n^4}+O(n^{-4}),
\]
by \(\log(1-u)=-u-u^2/2+O(u^3)\) and elementary power sums. Each total remainder is \(O(n^{-4})\), since there are \(O(n)\) summands. The first logarithm follows by expanding the rational factor in \(1/n\). This proves the displayed uniform expansions without an unproved asymptotic enumeration theorem.

Combining the two logarithms,
\[
\log Q_{n,k}=-\frac{(c-2)^2}{2n^2}
+\frac{a(c)}{n^3}+O(n^{-4}),\quad
 a(c)=-\frac{4c^4-6c^3-21c^2+36c-12}{6c},
\]
where notably \(a(2)=2/3\). Also the exact identity
\[
P_{n,k}=\frac{k}{n}\prod_{j=1}^{k-1}\left(1-\frac{n-1}{n^2-j}\right)
\]
implies \(P_{n,k}\to ce^{-c}\) whenever \(k/n\to c>0\), because the logarithm of the product tends to \(-c\). Since
\[
\operatorname{Cov}(L,R)=n^2P_{n,k}^2(Q_{n,k}-1),
\]
for fixed limiting \(c\ne2\) the leading \(n^{-2}\) term in \(\log Q_{n,k}\) proves the noncritical limit. The same formula yields the stated zero limit at \(c=2\) if the approach is slower than the critical scale. In the critical regime set \(c_n=k_n/n=2+x/\sqrt n+o(n^{-1/2})\). Uniformity and continuity of \(a\) imply
\[
 n^3\log Q_{n,k_n}\to\frac23-\frac{x^2}2,
 \qquad P_{n,k_n}\to2e^{-2}.
\]
Since \(Q_{n,k_n}-1\sim\log Q_{n,k_n}\) in the sense of a difference negligible after multiplication by \(n^3\), the critical limit follows. The strict sign assertions are consequences of convergence to a nonzero constant.

## Verification
Run \(\texttt{python3 verification/check.py}\) with Python 3 and no external dependencies. It independently enumerates every labeled binary matrix of sizes \(2\times2\), \(3\times3\), and \(4\times4\), checking exact rational first, mixed and covariance moments at every possible edge count. It separately checks the factorial-product identity over a larger finite range and sample sign predictions. The checker has 1,302 exact assertions. The finite checks corroborate the proof; they are not a substitute for the all-size counting argument or the Taylor remainder justification. For example, the exact expression gives positive covariance approximately \(0.00561333\) at \(n=10,k=20\), but negative covariance approximately \(-0.08829945\) at \(n=10,k=10\).

## Relationship to prior work
McKay and Skerman's *Degree sequences of random digraphs and bipartite graphs* (arXiv:1302.2446, first submitted February 11, 2013) studies this fixed-edge bipartite model among others and derives broad degree-sequence approximation theorems. Its Theorem 1(c) requires its acceptability condition, which entails edge density times its complement bounded below by a constant multiple of \(1/\log n\); the present regime has edge density asymptotic to \(c/n\) and violates that condition. The paper's independent-binomial reference model has independent left- and right-degree sequences and does not itself supply the small signed cross-part covariance in the critical window. Palka's 1984 *On the degrees of vertices in a bichromatic random graph* concerns degree counts in closely related random graph models. Its full text could not be examined, leaving an acknowledged historical-priority risk for exact cross-part moments. The stated contribution is the exact mixed degree-one covariance combined with the narrow nonzero critical-window law, not the definition of fixed-edge bipartite graphs or their marginal degree laws.

## Limitations
No exact finite-size classification of every positive and negative edge-count interval is asserted, and no boundary sign is asserted when \(|x|=2/\sqrt3\). No multivariate central limit theorem or stochastic monotonicity is claimed. The comparison with inaccessible earlier degree-count work is necessarily qualified; the scientific priority conclusion is best-knowledge, not an independence certificate.

## References
1. B. D. McKay and F. Skerman, *Degree sequences of random digraphs and bipartite graphs*, arXiv:1302.2446, first version February 11, 2013. https://arxiv.org/abs/1302.2446 ; full text https://arxiv.org/pdf/1302.2446 .
2. Z. Palka, *On the degrees of vertices in a bichromatic random graph*, Periodica Mathematica Hungarica 15 (1984), 121–126, doi:10.1007/BF01850725. Full text not inspected.
