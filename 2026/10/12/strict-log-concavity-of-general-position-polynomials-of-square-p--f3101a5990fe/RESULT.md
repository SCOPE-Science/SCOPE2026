# Strict log-concavity of general position polynomials of square-page book graphs
## Finding
For every integer \(r\ge2\), let \(B_r\) be the graph formed from \(r\) copies of \(C_4\) sharing the common edge \(xy\), with page \(i\) equal to
\[
x a_i b_i y x.
\]
Every general position set of cardinality at least three is exactly an independent set, and
\[
\psi(B_r;t)=(1+2t)^r+2t(1+t)^r+(3r+1)t^2.
\]

The coefficient sequence of \(\psi(B_r;t)\) is strictly log-concave, hence unimodal. In particular,
\[
\operatorname{gp}(B_r)=r+1,
\]
and the two maximum general position sets are the two bipartition classes
\[
\{x,b_1,\ldots,b_r\}
\quad\text{and}\quad
\{y,a_1,\ldots,a_r\}.
\]

## Assumptions and scope
All graphs are finite, simple, and connected. A set \(S\subseteq V(G)\) is in general position if no vertex of \(S\) lies on a shortest path between two other vertices of \(S\). The general position polynomial is
\[
\psi(G;t)=\sum_{k\ge0}a_k t^k,
\]
where \(a_k\) is the number of general position sets of cardinality \(k\).

A positive coefficient sequence \((a_0,\ldots,a_d)\) is strictly log-concave when
\[
a_k^2>a_{k-1}a_{k+1}
\]
for every \(1\le k\le d-1\).

The graph \(B_r\) is bipartite with classes
\[
X=\{x,b_1,\ldots,b_r\},
\qquad
Y=\{y,a_1,\ldots,a_r\},
\]
and has diameter \(3\).

## Proof
We first classify the general position sets of size at least three.

Let \(S\) contain an edge \(uv\) and a third vertex \(w\). Because \(B_r\) is bipartite, the distances \(d(u,w)\) and \(d(v,w)\) have opposite parity. Since \(u\) and \(v\) are adjacent, the triangle inequality gives
\[
|d(u,w)-d(v,w)|=1.
\]
Hence the farther endpoint of \(uv\) lies on a shortest path from the nearer endpoint to \(w\). Therefore no general position set of size at least three can contain an edge, so every such set is independent.

Conversely, let \(S\) be independent. Every two vertices of \(S\) are at distance at most \(3\). If a third selected vertex \(z\) lay internally on a shortest path between selected vertices \(u,v\), then independence would give
\[
d(u,z)\ge2,\qquad d(z,v)\ge2,
\]
and hence
\[
d(u,v)=d(u,z)+d(z,v)\ge4,
\]
contrary to the diameter. Thus every independent set is in general position. Therefore, for \(|S|\ge3\), general position is equivalent to independence.

Now count independent sets. If neither spine vertex is chosen, then each page independently contributes none, \(a_i\), or \(b_i\), giving
\[
(1+2t)^r.
\]
If \(x\) is chosen, then \(y\) and every \(a_i\) are forbidden, while the \(b_i\) may be chosen arbitrarily, giving
\[
t(1+t)^r.
\]
The case with \(y\) is symmetric. Hence the independence polynomial is
\[
I(B_r;t)=(1+2t)^r+2t(1+t)^r.
\]

Every set of cardinality at most two is automatically in general position. The only two-sets missing from the independence polynomial are the edges, and
\[
|E(B_r)|=3r+1.
\]
Consequently
\[
\psi(B_r;t)=I(B_r;t)+(3r+1)t^2
=(1+2t)^r+2t(1+t)^r+(3r+1)t^2.
\]

It remains to prove strict log-concavity. Write
\[
I(B_r;t)=\sum_{k=0}^{r+1}q_k t^k.
\]
With the convention that binomial coefficients outside their natural range are zero,
\[
q_k=2^k\binom{r}{k}+2\binom{r}{k-1}.
\]

We first show that \((q_k)\) is strictly log-concave. For \(1\le k\le r\), put \(n=r-k\). Direct simplification gives
\[
\frac{q_k^2-q_{k-1}q_{k+1}}{\binom{r}{k}^2}
=
\frac{N_{k,n}}{(k+1)(n+1)^2(n+2)},
\]
where
\[
\begin{aligned}
N_{k,n}={}&
2^kkn^2(2^k-k)\\
&+4^k(3kn+2k+n^3+4n^2+5n+2)\\
&+2^k(5k^2n+6k^2+7kn^2+13kn+6k)\\
&+4k^3+4k^2n+8k^2+4kn+4k.
\end{aligned}
\]
Since \(2^k>k\) for every \(k\ge1\), every displayed summand is nonnegative and the expression is positive. At the final index, \(q_{r+2}=0\), so strict log-concavity also holds there.

Let
\[
\psi(B_r;t)=\sum_{k=0}^{r+1}a_k t^k.
\]
Only the coefficient at degree two differs from \(q_k\):
\[
a_2=q_2+3r+1=(r+1)(2r+1).
\]
Thus only the inequalities centered at indices \(1,2,3\) need separate attention. At index \(1\),
\[
a_1^2-a_0a_2=(r+1)(2r+3)>0.
\]
At index \(2\), increasing \(q_2\) to \(a_2\) only increases the left side of the strict log-concavity inequality, so the already proved inequality for \((q_k)\) remains valid.

For \(r\ge3\),
\[
a_3=\frac{r(r-1)(4r-5)}{3},
\qquad
a_4=\frac{r(r-1)(r-2)(2r-5)}{3}.
\]
Writing \(s=r-3\ge0\), a direct factorization yields
\[
a_3^2-a_2a_4
=
\frac{r(r-1)}{9}
\left(
4s^4+28s^3+116s^2+284s+210
\right)>0.
\]
For \(r=2\), there is no internal index \(3\). All remaining inequalities are the strict inequalities already proved for \((q_k)\). Hence \(\psi(B_r;t)\) is strictly log-concave.

Finally, the polynomial has degree \(r+1\), and its leading coefficient is \(2\). Therefore
\[
\operatorname{gp}(B_r)=r+1
\]
and there are exactly two maximum general position sets, namely the bipartition classes.

## Verification
The included checker constructs \(B_r\), computes all-pairs shortest-path distances, and tests the general position definition directly using
\[
d(u,z)+d(z,v)=d(u,v).
\]
For every \(2\le r\le8\), it enumerates every vertex subset, verifies that every general position set of size at least three is independent, compares the complete cardinality distribution with the closed polynomial, checks the maximum-set count, and verifies every strict log-concavity inequality.

## Relationship to prior work
The structural theory of general position sets proves that, in a connected bipartite graph of diameter \(3\), the general position number equals the independence number. The argument above strengthens the specialization to \(B_r\) from a scalar maximum to a complete all-set classification.

The general position polynomial was introduced in 2024. That source derives formulas for standard graph families and several graph operations, studies Cartesian products of paths, and asks for additional unimodal families. Its full text contains no book-graph or theta-graph treatment.

A 2026 continuation develops explicit formulas and log-concavity or unimodality results for complete multipartite graphs and coronas. Its full text likewise contains no occurrence of book or theta terminology. The present theorem supplies a distinct strictly log-concave Cartesian-product family:
\[
B_r\cong K_{1,r}\square K_2.
\]

## Limitations
The theorem concerns square-page books, equivalently \(K_{1,r}\square K_2\), with \(r\ge2\). It does not cover books with longer cycle pages, arbitrary generalized theta graphs, or Cartesian products \(K_{1,r}\square H\) for larger \(H\).

The exhaustive computation is corroborative only. The all-parameter polynomial formula and strict log-concavity follow from the proof.

## References
1. B. S. Anand, U. S. V. Chandran, M. Changat, S. Klavžar, E. J. Thomas, “Characterization of general position sets and its applications to cographs and bipartite graphs,” arXiv:1812.08460v1, 20 December 2018; Applied Mathematics and Computation 359 (2019), 84–89, DOI 10.1016/j.amc.2019.04.064.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General Position Polynomials,” arXiv:2401.05696v1, 11 January 2024; Results in Mathematics 79 (2024), Article 110, DOI 10.1007/s00025-024-02133-3.
3. B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930v1, 6 March 2026.
