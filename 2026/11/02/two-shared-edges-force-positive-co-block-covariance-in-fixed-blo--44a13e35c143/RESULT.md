# Two shared edges force positive co-block covariance in fixed-block random partitions

## Finding
Let \(n\ge3\), let \(2\le k\le n-1\), and choose uniformly among the \(S(n,k)\) partitions \(\Pi\) of \([n]\) into exactly \(k\) nonempty blocks. For a fixed spanning tree \(T\) on \([n]\), set
\[
X_T=\sum_{uv\in E(T)}\mathbf1\{u,v\text{ belong to the same block of }\Pi\}.
\]
For arbitrary fixed spanning trees \(T,U\), put \(t=|E(T)\cap E(U)|\) and
\[
p=\frac{S(n-1,k)}{S(n,k)},\qquad q=\frac{S(n-2,k)}{S(n,k)}.
\]
Then the **complete pairwise covariance formula** is
\[
\operatorname{Cov}(X_T,X_U)=t(p-q)-(n-1)^2(p^2-q).
\]
Moreover \(p^2>q\), and the sign is universally classified as follows: \(t=0\) gives strictly negative covariance, whereas \(t\ge2\) gives strictly positive covariance. For \(t=1\), the exact sign is the sign of \(1-\tau_{n,k}\), where
\[
0<\tau_{n,k}:=\frac{(n-1)^2(p^2-q)}{p-q}\le\frac{2(n-1)}n<2.
\]
Equality in the upper bound holds precisely when \(k=n-1\). Thus two common edges are always sufficient, and this universal threshold cannot be lowered to one: at \(k=n-1\), one common edge yields negative covariance. Conversely, one common edge yields positive covariance for \(k=2\) and \(n\ge6\). The result is independent of the shapes of the two trees apart from their edge overlap.

## Assumptions and scope
The trees are deterministic, simple, undirected, spanning trees on the same labeled vertex set; no randomness is imposed on either tree. All randomness is in one common uniformly selected set partition, not independent partitions for the two trees. Here \(S(a,b)\) denotes a Stirling number of the second kind, with \(S(a,b)=0\) if \(b>a\). Feasibility of a particular overlap \(t\) depends on \(n\) and the chosen trees. The excluded cases \(k=1\) and \(k=n\) produce deterministic \(X_T\), hence covariance zero.

## Proof
**Edge-event contractions.** For an unordered pair \(e=uv\), write \(I_e=\mathbf1\{u,v\text{ lie in the same block}\}\). Identifying \(u\) and \(v\) bijects partitions with \(I_e=1\) with \(k\)-block partitions of \(n-1\) symbols, so \(\mathbb E I_e=p\). For any two *distinct* edges \(e,f\) of the complete graph, their equality constraints have rank two: if adjacent they identify three vertices; if disjoint they identify two separate vertex pairs. Hence \(\mathbb E(I_eI_f)=q\) regardless of adjacency. The \((n-1)^2\) ordered pairs in \(E(T)\times E(U)\) consist of \(t\) identical pairs and the remainder distinct. Consequently
\[
\operatorname{Cov}(X_T,X_U)
=t(p-p^2)+((n-1)^2-t)(q-p^2)
=t(p-q)-(n-1)^2(p^2-q).
\]

**Strict sign of distinct-edge covariance.** For fixed \(k\ge2\), the ordinary generating series satisfies
\[
\sum_{m\ge0}S(k+m,k)z^m=\prod_{j=1}^k(1-jz)^{-1}.
\]
The coefficient sequence is the convolution of positive geometric sequences \((j^m)_{m\ge0}\). Geometric sequences are log-concave with no internal zeros, and convolution preserves that property: equivalently, the nonnegative order-two Toeplitz minors multiply under Cauchy convolution. Strictness at every interior index follows already from the first two distinct factors, whose convolution has terms \(2^{m+1}-1\), with
\[
(2^{m+1}-1)^2-(2^m-1)(2^{m+2}-1)=2^m>0
\]
for \(m\ge1\); convolution with the remaining positive geometric factors preserves strictness by the Cauchy–Binet formula for adjacent Toeplitz minors. Thus \(S(n-1,k)^2>S(n-2,k)S(n,k)\) for \(2\le k<n\), including the boundary \(n=k+1\) by \(S(k-1,k)=0\). Hence \(c:=p^2-q>0\).

**Universal sharp threshold from a variance.** Let \(N=\binom n2\) and \(R=\sum_{e\in E(K_n)}I_e=\sum_{B\in\Pi}\binom{|B|}{2}\). Pair-event exchangeability proved above yields
\[
0\le\operatorname{Var}(R)=Np(1-p)-N(N-1)c.
\]
Writing \(v=p(1-p)>0\), we obtain \(c\le v/(N-1)\), whence
\[
\tau_{n,k}=\frac{(n-1)^2c}{v+c}
\le \frac{(n-1)^2}{N}=\frac{2(n-1)}n<2.
\]
Because the covariance is \((p-q)(t-\tau_{n,k})\) and \(p-q=v+c>0\), this proves both strict sign statements and the exact one-overlap criterion.

**Sharpness and the two one-overlap regimes.** If \(k=n-1\), precisely one block has size two and all other blocks are singletons, so \(R=1\) surely. The variance bound is an equality, giving \(\tau_{n,n-1}=2(n-1)/n>1\). If \(2\le k\le n-2\), one can make \(R\) take different values by comparing a block of size \(n-k+1\) with the configuration having one block of size \(n-k\) and another of size two; thus the variance bound is strict. If \(k=2\), substitution of \(S(n,2)=2^{n-1}-1\) gives
\[
\tau_{n,2}=\frac{(n-1)^2}{2^{n-1}-1}<1\quad\text{for }n\ge6.
\]
Thus an overlap of one edge can have either covariance sign, while the best possible all-parameter positive-overlap guarantee is two edges.

**Additional marginal law.** For a single tree \(T\), requiring exactly \(j\) monochromatic edges and contracting them leaves a tree with \(n-j\) vertices whose remaining edges must connect *different* blocks. The number of proper \(k\)-block partitions of a tree with \(r\) vertices is \(S(r-1,k-1)\), by its chromatic polynomial. Therefore
\[
\Pr(X_T=j)=\frac{\binom{n-1}{j}S(n-j-1,k-1)}{S(n,k)}
\quad(0\le j\le n-1).
\]
This confirms that the marginal distribution also does not depend on tree shape; its counting ingredient is classical and is not separately asserted as new.

## Verification
Running `python verify_overlap.py` with Python 3 standard library reproduces 134 exact-rational tests: it enumerates all set partitions through \(n=6\) and checks the covariance for a representative of every feasible tree-overlap class, checks the strict Stirling inequalities through \(n=7\), and verifies both sharp-threshold boundary formulas for \(n<35\). The code checks only finite cases; the proof above establishes the assertions for every allowed \(n,k,T,U\).

## Relationship to prior work
Galvin and Thanh (arXiv:1206.3591v1, publicly posted June 15, 2012), especially Section 2 and Eq. (10), give the classical graphical Stirling numbers of forests: a tree on \(r\) vertices has \(S(r-1,k-1)\) proper \(k\)-block partitions. That result underlies the marginal law above but does not state the covariance of **two** different tree-edge statistics or the uniform sharp two-edge positivity criterion. The present covariance proof instead exploits the exchangeability of all two-edge equality events and a global variance bound. Published mathematical research was checked for equivalent edge-overlap or co-block-covariance formulations; no stronger encompassing statement was located in the inspected material.

## Limitations
Only first and second mixed moments are classified; the complete joint distribution of \((X_T,X_U)\) may depend on the union of the trees beyond their edge overlap. The sign for one shared edge depends on the explicitly supplied finite Stirling ratio, not only on the fact that it is one. Search coverage does not establish historical priority, and uninspected literature may contain an equivalent formulation. An independent mathematical audit has not been performed.

## References
1. David Galvin and Do Trong Thanh, “Stirling numbers of forests and cycles,” arXiv:1206.3591v1, June 15, 2012, https://arxiv.org/abs/1206.3591 . Sections 1–2 and Eq. (10).
2. William M. Y. Goh and Eric Schmutz, “Random Set Partitions,” SIAM Journal on Discrete Mathematics, 1994, DOI:10.1137/S0895480190186974. General background on uniformly random set partitions; only bibliographic details and abstract consulted.
