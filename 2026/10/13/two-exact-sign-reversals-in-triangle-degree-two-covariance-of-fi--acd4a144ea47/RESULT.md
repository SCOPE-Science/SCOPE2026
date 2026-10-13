# Two exact sign reversals in triangle–degree-two covariance of fixed-edge random graphs

## Finding

Let \(V_2\) be the number of degree-two vertices and \(T\) the number of triangles in a uniform random graph with a prescribed edge count. There are **two** exact changes of sign in their covariance as that edge count increases, even though the corresponding independent-edge model has at most one. The full domain, exact covariance, and asymptotic locations of both transitions are specified below.

For integers \(n\ge6\), put \(N=\binom{n}{2}\) and \(B=\binom{n-1}{2}\). Define the quadratic on all real \(z\) by
\[
Q_n(z)=\frac1B
+\binom{n-1}{3}\frac{(z-3)(z-4)}{B(B-1)(B-2)}
-\binom n3\frac{z(z-1)}{N(N-1)(N-2)}.
\]
For \(3\le m\le B+2\),
\[
\boxed{\operatorname{Cov}(V_2,T)
=n\binom{n-1}{2}\frac{\binom B{m-2}}{\binom Nm}(m-2)Q_n(m).}
\]
For all other \(m\in\{0,\ldots,N\}\) this covariance is zero. The two distinct zeros satisfy
\[
\boxed{3<r_{n,-}<n<r_{n,+}<B+2.}
\]
Consequently, at admissible integers \(3\le m\le B+2\), the covariance is positive for \(m<r_{n,-}\) or \(m>r_{n,+}\), negative for \(r_{n,-}<m<r_{n,+}\), and zero if an integer equals a root.

For every positive \(c\), as \(n\to\infty\) with integer \(m_n/n\to c\),
\[
\boxed{\operatorname{Cov}(V_2,T)\to4c^3e^{-2c}(2c^2-4c+1),\qquad\frac{r_{n,\pm}}n\to1\pm\frac1{\sqrt2}.}
\]
The limiting signs are positive for \(0<c<1-1/\sqrt2\) and \(c>1+1/\sqrt2\), and negative between. The formula alone makes no eventual strict-sign assertion when \(c\) equals one of these two critical values.

## Assumptions and scope

The graph \(G\sim G(n,m)\) is uniformly sampled from all labeled simple undirected graphs on \(\{1,\ldots,n\}\) with exactly \(m\) edges. Here \(n\ge6\), \(0\le m\le N\), and a triangle is a three-element vertex set with all three edges present. The degree-two count is \(V_2=\sum_{v=1}^n\mathbf1\{\deg_G(v)=2\}\). The exact formula is not an assertion about the random-regular or fixed-degree-sequence models. A binomial coefficient whose bottom argument exceeds its top is zero. All denominators defining \(Q_n\) are nonzero for \(n\ge6\).

## Proof

Fix a labeled vertex \(v\), and write \(D_v=\deg_G(v)\). The \(n-1\) candidate incident edges are uniformly sampled subject to \(D_v=2\). The other \(m-2\) selected edges, conditional on \(D_v=2\) and on the two neighbors of \(v\), form a uniform sample from the \(B\) possible edges not incident to \(v\). Therefore the number of triangles **avoiding** \(v\) has conditional mean
\[
\binom{n-1}3\frac{(m-2)(m-3)(m-4)}{B(B-1)(B-2)},
\]
while the number **containing** \(v\) is exactly the indicator that its two neighbors are adjacent, with conditional expectation \((m-2)/B\). Hence
\[
\mathbb E[T\mid D_v=2]=
\binom{n-1}3\frac{(m-2)(m-3)(m-4)}{B(B-1)(B-2)}+\frac{m-2}B.
\]
An unconditional triangle occurs with probability \((m)(m-1)(m-2)/(N(N-1)(N-2))\), so
\[
\mathbb ET=\binom n3\frac{m(m-1)(m-2)}{N(N-1)(N-2)}.
\]
The degree-two probability equals \(\binom{n-1}2\binom B{m-2}/\binom Nm\). Using exchangeability and \(\operatorname{Cov}(V_2,T)=n\Pr(D_v=2)\bigl(\mathbb E[T\mid D_v=2]-\mathbb ET\bigr)\) yields the exact expression with factor \((m-2)Q_n(m)\). For \(m<3\), every triangle count is zero; for \(m>B+2\), every vertex has degree at least three, so the covariance is also zero.

The coefficient of \(z^2\) in \(Q_n(z)\) is
\[
a_n=\frac{4(3n^2-3n-4)}{3n(n+1)(n^2-3n-2)(n^2-n-4)}>0
\]
for \(n\ge6\). Direct substitution and simplification give
\[
Q_n(3)=\frac{2(n-3)(n^2-n+4)}{(n-2)(n-1)(n+1)(n^2-n-4)}>0,
\]
\[
Q_n(n)=-\frac{2(n-3)P_n}{3n(n-2)(n-1)(n+1)(n^2-3n-2)(n^2-n-4)}<0,
\]
where
\[
P_n=3n^5-12n^4-25n^3+106n^2+40n-64.
\]
Indeed, writing \(t=n-6\ge0\) yields \(P_n=3t^5+78t^4+767t^3+3544t^2+7684t+6368>0\). At the final possible degree-two edge count,
\[
Q_n(B+2)=\frac{(n-4)(n-3)S_n}{3(n-2)(n-1)(n+1)(n^2-n-4)}>0,
\]
where \(S_n=3n^3-12n^2+5n-4=3t^3+42t^2+185t+242>0\). The quadratic is strictly convex and negative at \(n\), so it has precisely two distinct real roots, one inside \((3,n)\) and one inside \((n,B+2)\). The strictly positive prefactor for \(3\le m\le B+2\) transfers the quadratic's signs to the covariance. This proves the all-integer classification, without assuming that the roots are integral.

For the sparse scaling, the degree of a fixed vertex is hypergeometric and satisfies \(\Pr(D_v=2)\to 2c^2e^{-2c}\) when \(m/n\to c>0\). Expansion of the explicit polynomial uniformly on compact positive \(c\)-intervals gives
\[
n^2Q_n(cn)\longrightarrow 2(2c^2-4c+1).
\]
The preceding exact covariance identity consequently converges to \(4c^3e^{-2c}(2c^2-4c+1)\). The two simple real roots of the limiting quadratic are \(1\pm1/\sqrt2\). Convergence of the coefficients of the rescaled quadratics therefore gives the asserted asymptotics for \(r_{n,\pm}/n\).

Finally, in the independent-edge model \(G(n,p)\), conditioning on \(D_v=2\) leaves the edges among all other vertices independently Bernoulli with parameter \(p\). Accordingly \(\mathbb E[T\mid D_v=2]-\mathbb ET=p-Bp^3\), which yields \(\operatorname{Cov}(V_2,T)=\mathbb EV_2\,p(1-Bp^2)\). For \(0<p<1\), the sign has at most one transition; unlike the fixed-edge result there is no second positive regime after a negative interval.

## Verification

Run the self-contained, standard-library-only checker `python check.py`. It exhaustively enumerates every labeled simple graph for \(n=4,5,6\), comparing the exact covariance computed by graph enumeration at every admissible edge count against the conditional-expectation formula. It also checks \(Q_n(3)>0\), \(Q_n(n)<0\), \(Q_n(B+2)>0\), strict convexity, and selected exact-rational values for \(6\le n\le200\). An observed successful run reported 34 exact enumeration cells and 2,136 exact quadratic evaluations. These finite checks support arithmetic reproducibility; only the displayed derivation establishes the universal results.

## Relationship to prior work

Goldstein (2010) studies degree-count marginals in the independent-edge model using normal approximation. Gilmer and Kopparty (2014) give a local limit theorem for triangle counts in the independent-edge model. Stark and Wormald (2016) develop subgraph-count methods and triangle-free probabilities in the fixed-edge model; Goldschmidt, Griffiths, and Scott (2019) study moderate deviations and covariances of **subgraph-count increments**. None of the inspected results states the finite-\(n\) two-root sign classification for the degree-two count versus triangle count.

The single model-specific mixed-moment identity is also algebraically obtainable by expressing the independent-edge mixed moment as a Bernstein polynomial in \(p\) and extracting the fixed-edge coefficients. No novelty is claimed for coefficient extraction itself, the conditional hypergeometric law, or the independent-edge comparator. The substantive result claimed is the **complete two-transition sign classification** and its sharp sparse-edge limits, which require the separate convexity and polynomial-sign argument above.

## Limitations

The scope is simple labeled graphs, degree exactly two, triangles, and \(n\ge6\). The covariance is zero on the stated degenerate edge ranges. The asymptotic formula gives a zero limit at critical scaling but does not determine finite-sample signs for arbitrary sequences converging to a critical constant. Broad historical mixed-moment and generating-function methods may implicitly contain the classification; independent historical priority confirmation has not been performed. Code enumeration is not a proof for unbounded \(n\).

## References

1. L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390, first publicly submitted 2010-05-24, https://arxiv.org/abs/1005.4390.
2. J. Gilmer and S. Kopparty, *A local central limit theorem for triangles in a random graph*, arXiv:1412.0257, https://arxiv.org/abs/1412.0257.
3. D. Stark and N. Wormald, *The probability of nonexistence of a subgraph in a moderately sparse random graph*, arXiv:1608.05193, https://arxiv.org/abs/1608.05193.
4. C. Goldschmidt, S. Griffiths, and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*, arXiv:1902.06830, https://arxiv.org/abs/1902.06830.
