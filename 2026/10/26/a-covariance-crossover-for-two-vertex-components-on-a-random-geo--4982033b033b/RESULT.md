# A covariance crossover for two-vertex components on a random geometric circle

## Finding
Let \(n\ge4\) independent uniform points lie on the circumference-one circle, and connect any two whose circular geodesic distance is at most \(r\), where \(0<r<1/2\). Write \(K_{n,r}\) for the number of connected components and \(J_{n,r}\) for the number of components containing exactly two vertices. Define
\[
p_k=(1-kr)_+^{n-1}\quad(0\le k\le n),\qquad Q_{n,r}=\sum_{k=0}^{n}(-1)^k\binom nk p_k,
\]
where \(u_+=\max(u,0)\). Then the exact finite-sample covariance is
\[
\boxed{\operatorname{Cov}(K_{n,r},J_{n,r})=n\left[2(p_2-p_3)+(n-3)(p_3-p_4)-(np_1+Q_{n,r})(p_2-p_3)\right].}
\]
Moreover, for every fixed \(c>0\), setting \(r=c/n\) for all sufficiently large \(n\) gives
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(K_{n,c/n},J_{n,c/n})}{n}
=e^{-2c}(3e^{-c}-2)\bigl((1+c^2)e^{-c}-1\bigr).}
\]
This limiting covariance is negative for \(0<c<\log(3/2)\), zero exactly at \(c=\log(3/2)\), and positive for \(c>\log(3/2)\). The crossover agrees with the unique maximizer of the limiting two-vertex-component density \(\lim_{n\to\infty}\mathbb E J_{n,c/n}/n=e^{-2c}(1-e^{-c})\), but the covariance amplitude contains an additional correction forced by the fixed total circle length.

## Assumptions and scope
All points are sampled independently from the uniform probability measure on \(\mathbb R/\mathbb Z\). Connectivity is defined using shortest circular arc length, with threshold \(r\). Ties and exact threshold equalities have probability zero. No independence of circular spacings is assumed. The finite identity holds for every integer \(n\ge4\) and every real \(0<r<1/2\), including regimes with a single connected component. The limiting sign statement is only an assertion about the scaled covariance at fixed positive \(c\); it does not claim that finite-size covariances have the same exact sign at every \(n\).

## Proof
Order the points cyclically, and let \(S_1,\ldots,S_n\) denote their successive clockwise gaps. The spacing vector has the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution, uniformly distributed on the simplex of vectors of positive entries summing to one. Set \(X_i=\mathbf1\{S_i>r\}\) and \(B=\sum_iX_i\), with cyclic indices.

A long gap prevents a connection from crossing it when at least two long gaps are present: a clockwise crossing has length greater than \(r\), and the alternate route contains another long gap greater than \(r\). If there is zero or one long gap the graph remains connected along all short consecutive gaps. Consequently
\[
K_{n,r}=B+\mathbf1\{B=0\}.
\]
A component consists of precisely two successive points exactly when the gaps bordering those two points are long and the gap between them is short. Even in the connected exceptional regimes that pattern cannot occur. Thus
\[
J_{n,r}=\sum_{i=1}^{n}X_{i-1}(1-X_i)X_{i+1}.
\]
For any \(k\) distinct specified gaps, the simplex-translation argument gives \(\Pr(S_{i_1}>r,\ldots,S_{i_k}>r)=(1-kr)_+^{n-1}=p_k\). By inclusion–exclusion, \(\Pr(B=0)=Q_{n,r}\).

Each summand of \(J_{n,r}\) has mean \(p_2-p_3\), so \(\mathbb EJ_{n,r}=n(p_2-p_3)\) and \(\mathbb EB=np_1\). Multiply a given summand by \(B\). The central gap has zero product, its two neighboring long-gap indicators each reproduce that summand, and the other \(n-3\) indicators each contribute \(p_3-p_4\). Therefore
\[
\mathbb E(BJ_{n,r})=n\left[2(p_2-p_3)+(n-3)(p_3-p_4)\right].
\]
Finally, \(J_{n,r}=0\) whenever \(B=0\), so \(\operatorname{Cov}(\mathbf1\{B=0\},J_{n,r})=-Q_{n,r}\mathbb EJ_{n,r}\). Combining these equalities proves the finite identity without approximation.

For the limit, fix \(c>0\) and put \(r=c/n\). For each fixed \(k\in\{1,2,3,4\}\), direct expansion gives
\[
p_k=e^{-kc}\left[1+\frac{kc-k^2c^2/2}{n}+O_c(n^{-2})\right].
\]
Substitute into the covariance formula, omit the \(Q_{n,c/n}\) term provisionally, and divide by \(n\). The order-\(n\) terms cancel identically. Writing \(t=e^{-c}\), the remaining constant factors as
\[
t^2(3t-2)\bigl((1+c^2)t-1\bigr).
\]
To control the omitted term, write \(S_i=E_i/\sum_jE_j\) with independent unit exponential variables \(E_i\). If every spacing is at most \(c/n\) and \(\sum E_i\le2n\), then every \(E_i\le2c\). The Chernoff estimate gives
\[
Q_{n,c/n}\le(2/e)^n+(1-e^{-2c})^n,
\]
so the omitted term vanishes exponentially. This proves the limit.

For \(c>0\), \(e^c>1+c^2\): indeed the Taylor lower bound \(e^c\ge 1+c+c^2/2+c^3/6\) exceeds \(1+c^2\), because \(1-c/2+c^2/6>0\). Hence \((1+c^2)e^{-c}-1<0\), so the sign is opposite to that of \(3e^{-c}-2\), with unique zero \(c=\log(3/2)\). The density formula follows from \(\mathbb EJ_{n,c/n}/n=p_2-p_3\) and is maximized at the same \(c\) by elementary differentiation.

## Verification
A standalone Python 3 script, `verify.py`, uses exact rational inclusion–exclusion to reconstruct the probability of every possible cyclic binary long-gap mask. It independently computes the covariance directly from those mask probabilities and compares it with the stated formula across twenty parameter strata and 1,984 mask states. It also checks numerical convergence of the sparse-limit formula on four fixed positive densities and its sign at the crossover. Run with `python3 verify.py`. Its expected final output is `VERIFY_OK`. These checks validate finite computations and examples; the all-parameter result rests on the analytical proof above.

## Relationship to prior work
The classical equal-length random arc model on the circle and its component counts are developed by Huillet (2003), whose Theorem 7 characterizes joint **physical lengths** of connected arc components, while the present statistic \(J_{n,r}\) counts components containing exactly **two sampled vertices**. Huillet's formula does not state the displayed mixed covariance or its sharp sparse sign crossover. Decreusefond–Ferraz (2011) compute the number-of-components distribution for a Poisson process on an interval, not the joint count on a binomial circle. Badiu–Coon (2021) study structural entropy of interval random geometric graphs. Wilsher–Dettmann–Ganesh (2022) study isolated nodes in a different soft-connection Poisson circle model. All four are important background but do not explicitly supply this finite fixed-sample covariance. The exact Dirichlet spacing joint-exceedance formula and classical inclusion–exclusion are prior tools, not claimed as original.

## Limitations
The result is specific to uniform independent points, one-dimensional circular geometry, hard distance-threshold connectivity, and components of order exactly two. The finite identity is not a complete joint distribution of all component counts; the theorem does not prove a joint central limit theorem, does not assert finite-sample uniqueness of a covariance sign crossing, and does not apply to unequal sampling densities or soft edges without further analysis. No claim of independent historical-priority certification is made. General unexamined higher-dimensional and marked-renewal covariance theorems remain possible sources of implicit coverage.

## References
1. T. Huillet, “Random covering of the circle: the size of the connected components,” *Advances in Applied Probability* **35** (2003), 563–582, DOI 10.1239/aap/1059486818. Full author-shared manuscript at https://www.researchgate.net/publication/38349613_Random_covering_of_the_circle_the_size_of_the_connected_components .
2. L. Decreusefond and E. Ferraz, “On the One Dimensional Poisson Random Geometric Graph,” arXiv:1008.5140 (2010), https://arxiv.org/abs/1008.5140 .
3. M.-A. Badiu and J. P. Coon, “Structural Complexity of One-Dimensional Random Geometric Graphs,” arXiv:2107.13495 (first posted 2021-07-28), https://arxiv.org/abs/2107.13495 .
4. M. Wilsher, C. P. Dettmann, and A. Ganesh, “The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph,” arXiv:2202.08044 (first posted 2022-02-16), https://arxiv.org/abs/2202.08044 .
