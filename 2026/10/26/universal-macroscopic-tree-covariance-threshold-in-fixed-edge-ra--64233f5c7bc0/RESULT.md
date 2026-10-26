# Universal macroscopic-tree covariance threshold in fixed-edge random graphs

## Finding

Let \(G\) be uniform over simple graphs on \([n]\) with exactly \(m\) edges. Write \(L\) for its number of isolated vertices and \(X_H\) for the number of (not necessarily induced) copies of a specified tree \(H\) with \(k\) vertices. For an integer \(r\ge1\), put \((L)_{\underline r}=L(L-1)\cdots(L-r+1)\). Assume
\[
 n\ge r+3,\qquad 3\le k\le n-r,\qquad
 k-1\le m\le \binom{n-r}{2}.
\]
Set \(N=\binom n2\), \(P=\binom{n-r}{2}\), and \((a)_{\underline j}=\prod_{t=0}^{j-1}(a-t)\). Then
\[
 \frac{\mathbb E[(L)_{\underline r}X_H]}
 {\mathbb E[(L)_{\underline r}]\,\mathbb E[X_H]}
 =R_{n,r}(k):=
 \frac{(n-k)_{\underline r}}{(n)_{\underline r}}
 \frac{(N)_{\underline{k-1}}}{(P)_{\underline{k-1}}}.
\]
In particular, the sign of \(\operatorname{Cov}((L)_{\underline r},X_H)\) is exactly the sign of \(R_{n,r}(k)-1\), **independently of both the tree shape and the admissible edge count** \(m\).

The finite-size profile has \(R_{n,r}(2)=1\), \(R_{n,r}(3)>1\), and is unimodal in integer \(k\); consequently, over \(3\le k\le n-r\), its covariance signs are a nonempty initial block of positive signs, optionally one zero, then a terminal block of negative signs (possibly empty). For any admissible neighboring sizes,
\[
 \operatorname{sgn}\left(\frac{R_{n,r}(k+1)}{R_{n,r}(k)}-1\right)
 =\operatorname{sgn}\bigl(n^2-nr-2-k(2n-r-3)\bigr).
\]
Thus this finite classification can be evaluated using exact integers; it does not assume a sign switch exists for every small \(n\). For instance, at \(n=7\) and \(r=1\), the ratios at tree orders five and six are \(114/91>1\) and \(969/1001<1\), respectively, for every admissible edge budget and every tree shape.

Fix \(r\) and let \(k/n\to u\in(0,1)\). Uniformly over all admissible choices of \(m\) and all tree shapes,
\[
 R_{n,r}(k)\longrightarrow \bigl((1-u)e^{2u}\bigr)^r.
\]
Let \(\rho\in(1/2,1)\) denote the unique positive solution of
\[
 (1-\rho)e^{2\rho}=1,
 \qquad \rho=0.796812130020\ldots .
\]
The covariance is eventually positive when \(u<\rho\) and negative when \(u>\rho\). More sharply, for every fixed \(r\) and all sufficiently large \(n\), there is a unique decreasing-branch crossing \(x_{n,r}\), defined by linear interpolation of \(\log R_{n,r}(k)\) between consecutive integer values. Its location is
\[
 x_{n,r}=\rho n+\kappa_r+O_r(n^{-1}),
 \qquad
 \kappa_r=-\frac{-2+(r+1)\rho+2\rho^2-
 \dfrac{(r-1)\rho}{2(1-\rho)}}{2-\dfrac1{1-\rho}}.
\]
For example, \(\kappa_1=0.2955425\ldots\) and \(\kappa_2=-0.1028635\ldots\).

The ensemble dependence is essential. In the independent-edge graph \(G(n,p)\), for any \(0<p<1\) and \(k\ge2\), the corresponding normalized mixed moment is only
\[
 \frac{\mathbb E[(L)_{\underline r}X_H]}
 {\mathbb E[(L)_{\underline r}]\mathbb E[X_H]}
 =\frac{(n-k)_{\underline r}}{(n)_{\underline r}}<1,
\]
so the covariance is strictly negative at every admissible tree size there. Conditioning on the total edge budget creates the positive phase and the macroscopic sign transition.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by \([n]\). A copy of \(H\) is a subgraph specified by its image vertices and the \(k-1\) image edges, counted once modulo automorphisms of \(H\); other edges among those vertices may be present. Tree shapes may depend arbitrarily on \(n\). Expectations are under the uniform \(m\)-edge distribution unless explicitly stated otherwise. The restrictions \(k-1\le m\le P\) ensure both relevant expectations are strictly positive and all factorial ratios are defined. For fixed \(r\), statements as \(n\to\infty\) are conditional on an admissible edge count existing at each size; there is no density restriction beyond admissibility. At \(k=2\), the tree-copy count is the deterministic edge count, hence zero covariance.

## Proof

**Exact conditioning.** Let \(a_H\) be the automorphism-group order of the tree. For a fixed set of \(e\) possible edges, the probability that all appear in \(G(n,m)\) is \((m)_{\underline e}/(N)_{\underline e}\). Therefore
\[
 \mathbb E X_H=\frac{(n)_{\underline k}}{a_H}
 \frac{(m)_{\underline{k-1}}}{(N)_{\underline{k-1}}}.
\]
A specified ordered \(r\)-tuple of distinct vertices is isolated with probability \(\binom Pm/\binom Nm\). Conditional on this event, the restriction to the other \(n-r\) vertices is uniform over graphs with \(m\) edges, and any copy of a tree must avoid the isolated vertices. Hence
\[
 \mathbb E (L)_{\underline r}=(n)_{\underline r}
 \frac{\binom Pm}{\binom Nm},
\]
\[
 \mathbb E[(L)_{\underline r}X_H]
 =(n)_{\underline r}\frac{\binom Pm}{\binom Nm}
 \frac{(n-r)_{\underline k}}{a_H}
 \frac{(m)_{\underline{k-1}}}{(P)_{\underline{k-1}}}.
\]
Dividing the last identity by the two marginal expectations and using \((n-r)_{\underline k}/(n)_{\underline k}=(n-k)_{\underline r}/(n)_{\underline r}\) proves the displayed ratio. Positivity of the marginals under the stated inequalities proves the covariance-sign assertion.

**Finite sign structure.** The factorization
\[
 \frac{R_{n,r}(k+1)}{R_{n,r}(k)}
 =\frac{n-k-r}{n-k}\frac{N-k+1}{P-k+1}
\]
has positive denominators whenever \(k+1\le n-r\). The numerator of its difference from one is
\[
 (n-k-r)(N-k+1)-(n-k)(P-k+1)
 =\frac r2\bigl(n^2-nr-2-k(2n-r-3)\bigr).
\]
This is strictly decreasing in \(k\), since \(2n-r-3>0\). Thus the consecutive ratios change from above one to below one at most once, giving unimodality. Direct cancellation gives \(R_{n,r}(2)=1\), and the preceding numerator at \(k=2\) is \(r(n-2)(n-r-2)/2>0\). Therefore \(R_{n,r}(3)>1\). A unimodal sequence starting above one can cross level one on its decreasing branch at most once, proving the full finite sign classification.

**Macroscopic threshold.** Fix \(r\), and write \(x=k/n\) in a compact subinterval of \((0,1)\). Take logarithms of the exact product:
\[
 \log R_{n,r}(k)
 =\sum_{j=0}^{r-1}\log\frac{n-k-j}{n-j}
 +\sum_{t=0}^{k-2}\log\frac{N-t}{P-t}.
\]
Since \(N-P=rn-r(r+1)/2\), Taylor expansion with a uniform \(O_r(n^{-2})\) remainder gives
\[
 \log R_{n,r}(k)=
 r\bigl(\log(1-x)+2x\bigr)
 +\frac rn\left[-2+(r+1)x+2x^2-
 \frac{(r-1)x}{2(1-x)}\right]
 +O_r(n^{-2}).
\]
Here the first sum has \(r\) terms, while in the second sum each logarithm has argument \(1+O_r(n^{-1})\), and there are \(O(n)\) terms; retaining the quadratic logarithmic term controls the asserted remainder. The leading function \(g(x)=\log(1-x)+2x\) starts at zero, rises up to \(x=1/2\), and then decreases strictly to minus infinity. Therefore it has exactly one positive zero \(\rho>1/2\), with \(g(x)>0\) before and \(g(x)<0\) after. This proves the sign law away from \(\rho\).

At \(\rho\), \(g'(\rho)=2-1/(1-\rho)\ne0\). The finite unimodality and the preceding uniform expansion imply that for large \(n\), consecutive values of \(\log R\) on the decreasing branch bracket zero uniquely. Interpolation changes the displayed expansion by at most \(O_r(n^{-2})\) near \(\rho n\), because its second differences there are \(O_r(n^{-2})\). Solving the interpolated equation by the mean-value theorem yields the stated \(\rho n+\kappa_r+O_r(n^{-1})\), with \(\kappa_r\) determined by cancellation of its \(n^{-1}\) coefficient.

**Independent-edge comparison.** In \(G(n,p)\), conditioning on any specified vertices being isolated leaves all edges on the remaining vertices mutually independent with probability \(p\). The expected copies of \(H\) are therefore scaled by only \((n-r)_{\underline k}/(n)_{\underline k}<1\). The equality of the two normalizations and the strict negative covariance follow without a fixed-edge hypergeometric correction.

## Verification

The standalone `verify.py` uses rational arithmetic and exhaustive graph enumeration rather than the preceding conditioning argument. It counted all \(33{,}856\) labeled graphs on four through six vertices, testing path and star tree shapes across admissible edge counts and isolated-vertex factorial orders. It made \(69\) independently computed mixed-moment comparisons. Separate exact-rational checks tested \(39{,}711\) adjacent-ratio and unimodality cases for graph orders up to \(64\); eight numerical checks tested the sharp crossing approximation for four factorial orders at graph orders \(1000\) and \(10000\). All \(39{,}788\) checks passed. Run `python3 verify.py` using Python's standard library; the analytic proof, not the finite checks, establishes statements for all orders.

## Relationship to prior work

The factorial edge-inclusion probability and the distinction between the independent-edge and fixed-edge random-graph ensembles are standard. Janson and Ruciński (2009), examined in full, analyze upper-tail bounds for edge-generated count statistics and rooted subgraph counts, not the joint factorial isolate–macroscopic-tree sign profile here. Janson (1990) studies random-graph subgraph-count fluctuations with fixed graph type and discusses the difference between fixed-edge and independent-edge ensembles; only its abstract and references could be inspected. Tomescu (1994) studies overlapping random subtrees of a complete graph, a distinct random quantity; only its abstract was accessible. These works motivate the question and provide related techniques but do not, in the material inspected, state the universal threshold, finite unimodality classification, or order-one correction above. Historical priority is not conclusively established.

## Limitations

The result concerns **non-induced** copies of trees and falling factorials of the isolated-vertex count; it does not establish the same threshold for induced tree counts, connected-component trees, or other vertex-degree statistics. The finite formulas require the specified admissible edge interval. No sign is asserted for sequences with \(k/n\to\rho\) without use of the finer crossing-location information. The asymptotic factor and thresholds describe normalized mixed moments and covariance signs, **not** a nonzero limit of the raw covariance for every edge-density sequence. The verification program tests finitely many cases and does not constitute an infinite proof. The 1990 and 1994 primary full texts were unavailable; a mathematically equivalent result in older literature remains a residual priority risk.

## References

1. Svante Janson and Andrzej Ruciński (2009), *Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs*, arXiv:0905.0972v1, first public 2009-05-07. https://arxiv.org/html/0905.0972v1
2. Svante Janson (1990), *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms **1**, 15–37. https://doi.org/10.1002/rsa.3240010103
3. Ioan Tomescu (1994), *On the number of subtrees for almost all graphs*, Random Structures & Algorithms **5**, 205–213. https://doi.org/10.1002/rsa.3240050119
