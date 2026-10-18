# Exact sign transitions between isolated clique components and embedded cliques

## Finding
Let \(I_r\) count connected components isomorphic to \(K_r\), and \(T_s\) count all labeled-vertex-set copies of \(K_s\) as subgraphs, whether or not maximal or isolated, in \(G(n,p)\). For \(n>r\ge2\), \(2\le s\le n\), \(0<p<1\), write
\[
A_{r,s}=\binom rs,\quad B_{n;r,s}=\binom ns-\binom{n-r}s,\quad b_s=\binom s2.
\]
Then the exact cross-covariance is
\[
\boxed{\operatorname{Cov}(I_r,T_s)=\binom nr p^{\binom r2}(1-p)^{r(n-r)}\bigl(A_{r,s}-B_{n;r,s}p^{b_s}\bigr).}
\]
If \(2\le s\le r\), there is exactly one sign reversal at
\[
\boxed{p_{n;r,s}=\left(\frac{\binom rs}{\binom ns-\binom{n-r}s}\right)^{1/\binom s2}.}
\]
The covariance is strictly positive below this value and strictly negative above it. If \(s>r\), the covariance is strictly negative throughout \(0<p<1\). For fixed \(r\) and \(s\le r\),
\[
\boxed{p_{n;r,s}\sim \left(\frac{(s-1)!\binom rs}{r}\right)^{2/[s(s-1)]}n^{-2/s}.}
\]
Consequently, for any fixed \(r\ge3\), the thresholds for \(s=2,3,\ldots,r\) eventually increase strictly with \(s\). This hierarchy can reverse at finite size: when \(n=7,r=6\), the \(s=6\) threshold is smaller than the \(s=5\) threshold.

## Assumptions and scope
The graph is a labeled, undirected, simple Erdős–Rényi graph on \(n\) vertices; its distinct edges are independent Bernoulli random variables with common parameter \(p\). A component is *isolated* if it has no edge to the rest of the graph. The parameter \(r\) satisfies \(2\le r<n\), while \(2\le s\le n\). Binomial coefficients vanish when the lower entry exceeds a nonnegative upper entry. The theorem concerns **component-count versus unconditioned subgraph-count** covariance, not covariance between two component counts or between two unconditioned subgraph counts. All equalities and strict signs are finite-sample statements on \(0<p<1\).

## Proof
For each \(r\)-subset \(U\), let \(J_U\) be the indicator that \(U\) induces an entire connected component isomorphic to \(K_r\). Then \(I_r=\sum_U J_U\), and
\[
q:=\mathbb E[J_U]=p^{\binom r2}(1-p)^{r(n-r)}>0.
\]
Conditioning on \(J_U=1\) fixes all edges inside \(U\) present and all cross-edges from \(U\) to its complement absent. Edges entirely inside the complement remain independent Bernoulli \(p\). Every \(s\)-clique is therefore either inside \(U\), in the complement, or straddles the two parts; the latter case is impossible. Thus
\[
\mathbb E[T_s\mid J_U=1]=\binom rs+\binom{n-r}s p^{\binom s2},
\]
while \(\mathbb E[T_s]=\binom ns p^{\binom s2}\). Subtracting and multiplying by \(q\) gives
\[
\operatorname{Cov}(J_U,T_s)=q\left[\binom rs-\left(\binom ns-\binom{n-r}s\right)p^{\binom s2}\right].
\]
Summing over all \(\binom nr\) choices of \(U\) proves the formula.

If \(s\le r\), the coefficient \(A_{r,s}\) is positive, and \(B_{n;r,s}>A_{r,s}\): there is an \(s\)-subset of the \(n\) vertices meeting \(U\) that is not wholly contained in \(U\), because \(r<n\) and \(s\ge2\). Therefore \(0<A/B<1\), and the bracket is strictly decreasing in \(p\), crossing zero once. If \(s>r\), then \(A=0\), whereas \(B>0\), proving strict negativity.

For fixed \(r,s\), the exact identity
\[
\binom ns-\binom{n-r}s=\sum_{j=0}^{r-1}\binom{n-j-1}{s-1}
\]
gives \(B\sim r n^{s-1}/(s-1)!\). Taking the \(1/\binom s2\) power yields the claimed asymptotic. Since \(n^{-2/s}/n^{-2/(s+1)}=n^{-2/[s(s+1)]}\to0\), thresholds increase strictly by \(s\) for sufficiently large \(n\) at any fixed \(r\).

For the finite-size reversal, with \(n=7,r=6\), the ratios \(A/B\) are \(2/7\) for \(s=5\) and \(1/7\) for \(s=6\). Hence
\[
p_{7;6,5}^{30}=\left(\frac27\right)^3=\frac8{343},\qquad p_{7;6,6}^{30}=\left(\frac17\right)^2=\frac7{343},
\]
which implies \(p_{7;6,6}<p_{7;6,5}\).

## Verification
The standalone standard-library Python script `check.py` independently enumerates every simple graph through six vertices and computes exact rational covariances for two choices of \(p\), comparing the numerical definitions with the formula. It also checks the strict threshold inequalities for \(3\le n\le69\) and the seven-vertex reversal by integer arithmetic. Execution returned `PASS: 52475 exact checks; full graph enumeration through six vertices.` The general conclusions, including the asymptotic order and the seven-vertex reversal, are proved above; finite enumeration is supplementary.

## Relationship to prior work
Janson, Knuth, Łuczak, and Pittel (1993) analyze component structure near the giant-component threshold via generating functions. Bhamidi, Budhiraja, and Wang (2012) analyze bounded-size random-graph evolution and its barely subcritical component regime. Neither inspected primary text states this covariance between the number of *isolated complete components* and the number of *unconditioned clique subgraphs*, nor its all-size sign transitions. Barbour, Janson, Karoński, and Ruciński (1990) study maximal cliques, whose definition is distinct from isolated complete components. Gösgens and collaborators (2024) condition the *entire graph* to be a disjoint union of cliques; that is a different probability law. The conditioning calculation here is elementary and could be implicit in broader earlier component/subgraph generating-function methods; no independent priority conclusion is asserted.

## Limitations
The result applies to the independent-edge homogeneous model and clique subgraphs, not arbitrary heterogeneous graphs or arbitrary motifs. The exact threshold hierarchy is only eventually ordered for fixed component size; it has finite-size reversals. The comparison to prior work is not exhaustive, so a general previously published joint generating function might already imply the formula. No independent historical-priority or mathematical audit has occurred.

## References
1. S. Janson, D. E. Knuth, T. Łuczak, and B. Pittel, *The Birth of the Giant Component*, arXiv:math/9310236v1 (public version 1993-10-01), https://arxiv.org/abs/math/9310236 .
2. S. Bhamidi, A. Budhiraja, and X. Wang, *Bounded-size rules: The barely subcritical regime*, arXiv:1212.5480v1 (public version 2012-12-21), https://arxiv.org/abs/1212.5480 .
3. A. D. Barbour, S. Janson, M. Karoński, and A. Ruciński, *Small cliques in random graphs*, Random Structures & Algorithms **1** (1990), 403–434, https://doi.org/10.1002/rsa.3240010403 .
4. M. Gösgens, L. Lüchtrath, E. Magnanini, M. Noy, and É. de Panafieu, *The Erdős–Rényi Random Graph Conditioned on Every Component Being a Clique*, arXiv:2405.13454 (2024), https://arxiv.org/abs/2405.13454 .
