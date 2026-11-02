# Exact Pareto-frontier–comparability covariance and three high-dimensional scales

## Finding

Let \(X_1,\ldots,X_n\) be independent uniform points in \([0,1]^d\), with integers \(n\ge3\) and \(d\ge2\). Count \(M_{n,d}\), the coordinatewise maximal (nondominated) observations, and \(Q_{n,d}\), the unordered comparable pairs: \(Q_{n,d}=\sum_{1\le i<j\le n}\mathbf1\{X_i\le X_j\text{ or }X_j\le X_i\}\). With probability one, every pair has distinct coordinates, so these events are disjoint.

Put
\[
\begin{aligned}
U_{n,d}&=\sum_{j=0}^{n-1}(-1)^j\binom{n-1}{j}\frac1{(j+1)^d},\\
V_{n,d}&=\sum_{j=0}^{n-2}(-1)^j\binom{n-2}{j}\frac1{((j+1)(j+2))^d},\\
W_{n,d}&=\sum_{j=0}^{n-3}(-1)^j\binom{n-3}{j}\left[\frac1{(2(j+1))^d}-\left(\frac{j+4}{2(j+2)(j+3)}\right)^d\right].
\end{aligned}
\]
The exact finite-sample mixed covariance is
\[
\boxed{\operatorname{Cov}(M_{n,d},Q_{n,d})=n(n-1)\left[V_{n,d}+(n-2)W_{n,d}-\frac{n}{2^d}U_{n,d}\right].}
\]
For each fixed \(n\ge3\), as dimension \(d\to\infty\), the three successive sharp exponential scales are
\[
\boxed{\operatorname{Cov}(M_{n,d},Q_{n,d})=-\frac{n(n-1)}{2^d}-\frac{n(n-1)(n-2)}{3^d}+\frac{n(n-1)(4n-6)}{4^d}+O_n\!\left((5/24)^d\right).}
\]
In particular the covariance is strictly negative for sufficiently large \(d\) at every fixed \(n\). At \(d=2\), the independent-rank representation gives the exact cross-check
\[\operatorname{Cov}(M_{n,2},Q_{n,2})=-\frac{n-H_n}{2},\quad H_n=\sum_{j=1}^n\frac1j.\]

## Assumptions and scope

The result is for independent observations with **independent continuous uniform coordinates**, the product order, and non-induced comparability (all order-related pairs). The high-dimensional expansion fixes \(n\); it is **not** claimed uniform in growing \(n\). The theorem does not claim covariance negativity for every pair of finite parameters. Dimensional values below \(2\) and samples below \(3\) are not included in the finite-sum statement.

## Proof

Let \(D_{ij}=\mathbf1\{X_i\ge X_j\}\), with coordinatewise order, so \(Q_{n,d}=\sum_{i\ne j}D_{ij}\) almost surely, where each comparable unordered pair contributes exactly one directed term. Let \(A_i\) indicate that \(X_i\) is maximal, so \(M_{n,d}=\sum_i A_i\). By exchangeability, \(\mathbb E Q_{n,d}=n(n-1)2^{-d}\).

For \(x\in[0,1]^d\), let \(s(x)=\prod_{k=1}^d(1-x_k)\) and \(t(x)=\prod_{k=1}^d x_k\). Conditional on \(X_1=x\), each other point avoids dominating \(x\) with probability \(1-s(x)\). Consequently,
\[\mathbb E A_1=\int(1-s(x))^{n-1}\,dx=U_{n,d}.\]
If \(X_1\) dominates \(X_2\), the second point has probability \(t(x)\), and the remaining \(n-2\) points avoid dominating \(x\). Thus
\[\mathbb E(A_1D_{12})=\int t(x)(1-s(x))^{n-2}\,dx=V_{n,d}.\]
On the other hand \(A_1D_{21}=0\) almost surely.

For the **disjoint** directed relation \(D_{23}\), conditioned on \(X_1=x\), both points \(2\) and \(3\) must avoid the upper orthant of \(x\). Under \(D_{23}\), the event that \(X_3\) dominates \(x\) is contained in the event that \(X_2\) dominates \(x\). Therefore the probability of \(D_{23}\) with neither point dominating \(x\) is
\[
2^{-d}-\int_{y\ge x}\prod_{k=1}^d y_k\,dy
=2^{-d}\left[1-\prod_{k=1}^d(1-x_k^2)\right].
\]
All other \(n-3\) points must avoid the upper orthant, so
\[
\mathbb E(A_1D_{23})=\int 2^{-d}\left[1-\prod_k(1-x_k^2)\right](1-s(x))^{n-3}\,dx=W_{n,d}.
\]
The three finite sums are obtained by binomial expansion and coordinatewise integration, including \(\int_0^1 x(1-x)^j dx=1/((j+1)(j+2))\) and \(\int_0^1 (1-x^2)(1-x)^j dx=(j+4)/((j+2)(j+3))\).

Counting ordered index incidences gives \(\mathbb E(MQ)=n(n-1)V+n(n-1)(n-2)W\). Subtracting \(\mathbb EM\,\mathbb EQ=nU\cdot n(n-1)2^{-d}\) proves the exact covariance formula.

For fixed \(n\), the leading terms of the three sums as \(d\to\infty\) are
\[
\begin{aligned}
U_{n,d}&=1-(n-1)2^{-d}+O_n(3^{-d}),\\
V_{n,d}&=2^{-d}+O_n(6^{-d}),\\
W_{n,d}&=2^{-d}-3^{-d}-(n-3)4^{-d}+O_n((5/24)^d).
\end{aligned}
\]
Every omitted term has base at most \(5/24\) in the last line (the \(j=1\) correction to the upper-orthant exclusion); the other two displayed errors become at most this size after multiplication by \(2^{-d}\) when required. Substitution yields the three-scale expansion and eventual negativity.

For \(d=2\), order points by decreasing first coordinate. The second-coordinate ranks form a uniform random permutation. The maximal-point count is its number of left-to-right upper records, and \(Q\) is its inversion count. At insertion \(j\), the rank among the first \(j\) observations is uniform on \(\{1,\ldots,j\}\), independently over \(j\). It contributes an upper-record indicator and \(j-\text{rank}\) inversions. Their covariance is \(-(j-1)/(2j)\). Summing gives \(-(n-H_n)/2\).

## Verification

The standalone standard-library script `check.py` derives the rational finite sums independently of exhaustive rank-permutation enumeration. It checks all \((n,d)=(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\), tests the planar harmonic specialization and large-dimensional three-scale remainders, and uses exact fractions throughout. The script's finite checks are not a substitute for the all-parameter integration and finite-asymptotic proof above.

## Relationship to prior work

Bai–Devroye–Hwang–Tsai, *Maxima in hypercubes* (2005), establishes detailed **marginal variance and limit theory** for the number of maxima in the same cube model. Its equations for the mean and variance involve nondominance probabilities but do not give a joint moment with the **total number of comparable pairs**. Bollobás–Brightwell, *Random high-dimensional orders* (1995), treats the same product-order model, focusing in the available abstract on height, maximum degree and dimension thresholds, rather than the present cross-covariance. The contribution here is the explicit mixed moment and its three successive fixed-sample high-dimensional coefficients, not the general model or the known marginal laws.

## Limitations

Strict covariance negativity for every finite \((n,d)\) is **not** established. A previously derived identity in random-order or skyline-algorithm literature could overlap the result; historical priority is not independently certified. The full 1995 paper was not accessible for complete theorem-by-theorem comparison, while the 2005 paper was inspected substantially in its full author-hosted text. The finite-sample result holds only under the uniform product model; no statement is made for correlated coordinates or nonrectangular regions.

## References

1. Z.-D. Bai, L. Devroye, H.-K. Hwang and T.-H. Tsai, *Maxima in hypercubes*, Random Structures & Algorithms **27** (2005), 290–309. DOI: https://doi.org/10.1002/rsa.20053. Author-hosted complete paper: https://luc.devroye.org/max-d-cube.pdf. First published February 28, 2005.
2. B. Bollobás and G. Brightwell, *Random high-dimensional orders*, Advances in Applied Probability **27** (1995), 161–184. DOI: https://doi.org/10.2307/1428102. https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/random-high-dimensional-orders/DD0F2E931DEE90622F444BC565C0CFAD.
