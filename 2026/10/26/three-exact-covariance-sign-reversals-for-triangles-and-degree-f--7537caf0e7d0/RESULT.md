# Three exact covariance sign reversals for triangles and degree frequencies in a fixed-edge random graph

## Finding
For every integer \(n\ge14\), sample a uniformly random labelled simple graph \(G\) on \(n\) vertices with exactly \(n-1\) edges. Let \(T\) count triangles and let \(D_r\) count vertices of degree \(r\). The covariance \(\operatorname{Cov}(T,D_r)\) is strictly positive at \(r=0\) and at every \(4\le r\le n-3\), and strictly negative at every \(1\le r\le3\) and \(n-2\le r\le n-1\). Consequently, the complete degree-frequency covariance profile has exactly three sign switches and no zeros. The onset is sharp for this sign profile: at \(n=13\), the covariance at \(r=11=n-2\) is positive.

## Assumptions and scope
Fix \(n\ge14\) and write \(m=n-1\), \(N=\binom n2\), and \(B=\binom{n-1}2\). All \(\binom Nm\) labelled graphs with \(m\) edges are equiprobable. Degrees use all \(n\) vertices, and \(0\le r\le n-1\). For a real number \(x\), write \((x)_j=x(x-1)\cdots(x-j+1)\), with \((x)_0=1\). An integer falling factorial vanishes when fewer than \(j\) objects exist.

Define
\[
\begin{aligned}
q_n(r)&=\frac{\binom{n-1}{r}\binom B{m-r}}{\binom Nm},\\
f_n(r)&=\binom r2\frac{m-r}{B}+\binom{n-1}3\frac{(m-r)_3}{(B)_3},\\
\mu_n&=\binom n3\frac{(m)_3}{(N)_3}
=\frac{4(n-3)(n-2)(n-1)}{3(n+1)(n^2-n-4)}.
\end{aligned}
\]
Every \(q_n(r)\) is strictly positive for \(n\ge14\) and \(0\le r\le n-1\).

## Proof
Fix a vertex \(v\). Conditional on \(\deg(v)=r\), its \(r\) neighbors are uniformly distributed over \(r\)-subsets of the other vertices, and the remaining \(m-r\) edges form an independent uniform subset of the \(B\) edges not incident to \(v\). Thus a triangle through \(v\) has expected total \(\binom r2(m-r)/B\); a triangle avoiding \(v\) has expected total \(\binom{n-1}3(m-r)_3/(B)_3\). This proves \(f_n(r)=\mathbb E[T\mid\deg(v)=r]\). The unconditional triangle expectation is \(\mu_n\), since a fixed triple of edges occurs with probability \((m)_3/(N)_3\).

Writing \(I_{v,r}=\mathbf1\{\deg(v)=r\}\), exchangeability and conditioning yield the exact identity
\[
\boxed{\operatorname{Cov}(T,D_r)=nq_n(r)g_n(r),\qquad g_n(r)=f_n(r)-\mu_n.}
\]
For fixed \(n\), \(g_n(r)\) is a *cubic polynomial* in real \(r\). Its signs at six pivotal positions are obtained by the following exact rational identities (all denominators shown are positive for \(n\ge14\)):
\[
\begin{aligned}
g_n(0)&=\frac{4(n-3)(n-2)(n-1)(3n^2-3n-4)}{3n(n+1)(n^2-3n-2)(n^2-n-4)}>0,\\
g_n(1)&=-\frac{8(n-3)(n-2)(3n^2-7n-8)}{3n(n+1)(n^2-3n-2)(n^2-n-4)}<0,\\
g_n(3)&=-\frac{2P_3(n)}{3n(n-2)(n-1)(n+1)(n^2-3n-2)(n^2-n-4)}<0,\\
g_n(4)&=\frac{8P_4(n)}{3n(n-2)(n-1)(n+1)(n^2-3n-2)(n^2-n-4)}>0,\\
g_n(n-3)&=\frac{2(n-5)(n-3)(n^3+5n^2-16n-8)}{3(n-2)(n-1)(n+1)(n^2-n-4)}>0,\\
g_n(n-2)&=-\frac{(n-3)(n^3-16n^2+35n+4)}{3(n-1)(n+1)(n^2-n-4)}<0.
\end{aligned}
\]
Here
\[
\begin{aligned}
P_3(n)&=3n^7-57n^6+275n^5-39n^4-2134n^3+2736n^2+2000n-1920,\\
P_4(n)&=15n^6-134n^5+198n^4+748n^3-1413n^2-830n+840.
\end{aligned}
\]
These inequalities hold for every \(n\ge14\): set \(t=n-14\ge0\). The coefficient lists, in descending powers of \(t\), are
\[
\begin{aligned}
P_3(t+14)&:\ (3,237,7835,139751,1440202,8450476,25402200,28166976),\\
P_4(t+14)&:\ (15,1126,34918,572396,5229491,25238118,50245776),\\
(t+14)^3-16(t+14)^2+35(t+14)+4&=t^3+26t^2+175t+102.
\end{aligned}
\]
All coefficients are strictly positive. All remaining numerator factors are manifestly positive at \(n\ge14\).

The cubic \(g_n\) therefore has at least one real root in each of the three pairwise disjoint open intervals \((0,1)\), \((3,4)\), and \((n-3,n-2)\). A nonzero cubic has at most three distinct roots, so it has exactly one in each and no others. The endpoint signs determine all integer signs; \(g_n(n-1)=-\mu_n<0\) is consistent with the same conclusion. Since \(nq_n(r)>0\), the asserted covariance pattern follows, with no zero covariance for any integer degree.

Sharpness of the onset follows by direct substitution at \(n=13\): the factor \(n^3-16n^2+35n+4=-48\) is negative, and all other factors in the displayed formula for \(g_n(n-2)\) are positive, so \(\operatorname{Cov}(T,D_{11})>0\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It exhaustively enumerates all fixed-edge graphs for \(n=4,5,6,7\), checking all \(22\) degree-index covariance identities against direct averaging. It also verifies the claimed complete sign patterns for each \(14\le n\le120\), together with the \(n=13\) boundary. These tests corroborate the derivation; the cubic-root argument and sign certificates above prove the unbounded assertion.

Run with `python verify.py` using standard Python 3, with no dependencies.

## Relationship to prior work
Fixed-edge Erdős–Rényi random graphs and triangle counts are standard. Goldschmidt, Griffiths, and Scott investigate moderate deviations of subgraph counts in both fixed-edge and independent-edge models [1]. Their abstract concerns asymptotic deviation rates and the linkage of subgraph deviations; this finite-degree-frequency covariance sign theorem is not stated in the accessible abstract. McKay and Wormald study the random-graph degree sequence [2], but the reviewed abstract does not discuss covariance with triangles. The classical exact expectation of triangles is used, not asserted as new. A key conceptual distinction is that, in an independent-edge random graph, conditional expected triangle count is monotone nondecreasing with a given vertex's degree; fixing the number of edges creates a competing depletion term, allowing three covariance reversals.

## Limitations
This is an exact theorem specifically for a *uniform graph with \(n-1\) edges* and \(n\ge14\); it makes no analogous universal sign assertion for other fixed edge counts or for independent-edge models. No limit law or causal interpretation is claimed. Complete historical priority remains uncertain: only bibliographic information and abstracts were accessible for the most relevant broad publications, not their full contents. Independent validation has not been performed.

## References
[1] C. Goldschmidt, S. Griffiths, A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*, arXiv:1902.06830, publicly posted 2019-02-18, later published in *Transactions of the American Mathematical Society* 373 (2020), 5517–5585; https://arxiv.org/abs/1902.06830.

[2] B. D. McKay, N. C. Wormald, *The degree sequence of a random graph. I. The models*, *Random Structures & Algorithms* 11 (1997), 97–117; https://research.monash.edu/en/publications/the-degree-sequence-of-a-random-graph-i-the-models/.
