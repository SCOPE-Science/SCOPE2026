# A four-thirds linear-partial-correlation transition in random triangle overlays

## Finding

Take \(n\ge 5\) labelled vertices and \(m\ge2\) independent, uniformly chosen three-element subsets of the vertices, with replacement. Each triple contributes all three edges of its triangle; let \(X_e\) indicate that edge \(e\) appears in their union. Write \(\Sigma=\operatorname{Cov}((X_e)_e)\) and \(Q=\Sigma^{-1}\), indexing all \(\binom n2\) edges. This covariance matrix is positive definite for every stated \(n,m\).

For distinct edges \(e,f\), define their **full-order linear partial correlation** by
\[
\rho^{\mathrm{lin}}_{ef}=-\frac{Q_{ef}}{\sqrt{Q_{ee}Q_{ff}}}.
\]
This is the Pearson correlation between the residuals obtained by separately linearly regressing \(X_e\) and \(X_f\) on the common set of edge indicators indexed by edges other than \(e\) and \(f\), with an intercept; it is not a claim of nonlinear conditional independence.

For every finite \(n\ge5,m\ge2\), adjacent distinct edges have strictly positive marginal covariance, whereas disjoint edges have strictly negative marginal covariance. If \(m=m_n\) and \(m_n/n\to\alpha\in(0,\infty)\), then for any adjacent pair and any disjoint pair, respectively,
\[
\lim_{n\to\infty}n\rho^{\mathrm{lin}}_{\mathrm{adj}}=\frac{3\alpha-4}{6\alpha},
\qquad
\lim_{n\to\infty}n\rho^{\mathrm{lin}}_{\mathrm{dis}}=-\frac{2}{3\alpha}.
\]
In contrast, their marginal Pearson correlations obey
\[
\lim_{n\to\infty}n\operatorname{Corr}(X_e,X_f)\big|_{\mathrm{adj}}=1,
\qquad
\lim_{n\to\infty}n^2\operatorname{Corr}(X_e,X_f)\big|_{\mathrm{dis}}=-6.
\]
Thus adjacent-edge *linear partial* correlations are eventually negative for \(0<\alpha<4/3\), but eventually positive for \(\alpha>4/3\), despite always-positive marginal correlations. The first-order coefficient vanishes at \(\alpha=4/3\); no claim is made about the finite-size sign at that boundary.

## Assumptions and scope

The base graph is the complete simple graph on \(n\ge5\) labelled vertices. Each of \(m\ge2\) independent layers consists of one uniformly selected triple and all its three edges. Repeated triples are permitted. There is no edge deletion or additional Bernoulli thinning. All probabilities refer to this finite probability space. For a given pair \(e,f\), each regression uses the common set of all \(X_g\) for \(g\notin\{e,f\}\) as linear covariates. Neither target variable is included among the covariates. The asymptotic assertion is along any integer sequences \(n\to\infty\) and \(m_n/n\to\alpha>0\).

## Proof

**One-layer inclusion probabilities.** Fix an edge and a pair of distinct edges. In one uniform triple, the chance of containing an edge equals
\[
p=\frac6{n(n-1)},
\qquad r=\frac{p}{n-2}
\]
where \(r\) is the chance of containing both edges when they share one vertex. A triple cannot contain two vertex-disjoint edges. Put
\[
u=1-p,\quad v=1-2p+r,\quad w=1-2p,\quad
q=u^m,\quad b=v^m,\quad c=w^m.
\]
The probability a specified edge is absent from all layers is \(q\), and the probabilities that two adjacent or two disjoint edges are simultaneously absent are \(b,c\). Writing \(E=\binom n2\), the covariance entry equals
\[
\Sigma_{ef}=\begin{cases}
q-q^2& e=f,\\
b-q^2& |e\cap f|=1,\\
c-q^2& |e\cap f|=0.
\end{cases}
\]
For \(n\ge5\), \(r>p^2\), so \(v>u^2\) and hence \(b-q^2>0\). Also \(w<u^2\), so \(c-q^2<0\). This proves the exact marginal sign assertion.

**Positive definiteness.** Suppose a deterministic linear combination \(\sum_e a_e X_e\) were constant almost surely. Every sequence of \(m\) layers has positive probability. Taking all layers equal to a fixed triangle \(T\) shows that \(\sum_{e\subset T}a_e\) is the same for every triangle. Compare triangles \(\{i,j,k\}\) and \(\{i,j,\ell\}\): for each fixed distinct \(k,\ell\), the differences \(d_i=a_{ik}-a_{i\ell}\) satisfy \(d_i+d_j=0\) for every distinct \(i,j\notin\{k,\ell\}\). There are at least three such vertices, so each \(d_i=0\). Consequently all edges meeting any fixed vertex have the same coefficient, and symmetry forces every coefficient to equal some \(a\). A sample with all layers equal to \(T\) then has edge-sum \(3a\); another with \(m-1\) copies of \(T\) and one triangle meeting \(T\) in exactly two vertices has edge-sum \(5a\). Therefore \(a=0\). No nonzero linear form has zero variance, proving \(\Sigma\) is positive definite.

**Exact diagonalization and inverse.** Let \(A_1\) be the adjacency matrix of the line graph of \(K_n\) on its \(E\) edges, and let \(A_0\) be the adjacency matrix of the complementary disjoint-edge relation. Thus
\[\Sigma=qI+bA_1+cA_0-q^2J.\]
The three mutually orthogonal invariant subspaces are the constant vectors (dimension one), the vertex-incidence contrasts (dimension \(n-1\)), and the orthogonal edge residual space (dimension \(E-n\)). The eigenvalues there are, in that order,
\[
\begin{aligned}
\lambda_0&=q+2(n-2)b+\binom{n-2}{2}c-Eq^2,\\
\lambda_1&=q+(n-4)b-(n-3)c,\\
\lambda_2&=q-2b+c.
\end{aligned}
\]
For completeness, if \(B\) is the unsigned vertex-edge incidence matrix, then \(BB^{\mathsf T}=(n-2)I+J\); hence the first two orthogonal projectors are \(P_0=J/E\) and \(P_1=(B^{\mathsf T}B-2(n-1)P_0)/(n-2)\), with \(P_2=I-P_0-P_1\). Their diagonal/adjacent/disjoint entries are
\[
\begin{array}{c|ccc}
& e=f&|e\cap f|=1&|e\cap f|=0\\\hline
P_0&1/E&1/E&1/E\\
P_1&2/n&(n-4)/(n(n-2))&-4/(n(n-2))\\
P_2&(n-3)/(n-1)&-(n-3)/((n-1)(n-2))&2/((n-1)(n-2)).
\end{array}
\]
Because all eigenvalues are positive, the exact inverse is \(Q=P_0/\lambda_0+P_1/\lambda_1+P_2/\lambda_2\). In particular, every diagonal entry is equal and the other entries depend only on whether the two edges meet.

**Sparse-layer asymptotics.** Write \(t_n=m_n/n\), so \(t_n\to\alpha\in(0,\infty)\). Expanding the three powers above uniformly for \(t_n\) in a compact subset of \((0,\infty)\) gives
\[
\lambda_0=\frac{18t_n^2}{n^2}+O(n^{-3}),\quad
\lambda_1=\frac{12t_n}{n}+O(n^{-2}),\quad
\lambda_2=\frac{6t_n}{n}+O(n^{-2}).
\]
These expansions follow directly by inserting \(p=6/[n(n-1)]\), \(r=p/(n-2)\), and expanding \(m_n\log(1-z)\); cancellation in \(\lambda_0\) must be retained through order \(n^{-2}\). Applying the projector entries to the inverse formula now yields
\[
Q_{ee}=\frac{n}{6t_n}+O(1),\quad
Q_{\mathrm{adj}}=\frac1{9t_n^2}-\frac1{12t_n}+O(n^{-1}),\quad
Q_{\mathrm{dis}}=\frac1{9t_n^2}+O(n^{-1}).
\]
Dividing the off-diagonal entries by the common diagonal proves the two displayed partial-correlation limits.

For marginal correlations, direct expansions of the three covariance entries give
\[
q-q^2=\frac{6t_n}{n}+O(n^{-2}),\quad
b-q^2=\frac{6t_n}{n^2}+O(n^{-3}),\quad
c-q^2=-\frac{36t_n}{n^3}+O(n^{-4}).
\]
Dividing by the diagonal covariance gives the two marginal limits. The sign of the adjacent partial-correlation coefficient is that of \(3\alpha-4\) whenever \(\alpha\ne4/3\), completing the proof.

## Verification

The bundled standard-library script `verify_precision.py` independently enumerates all ordered triangle-layer selections for \((n,m)=(5,2),(5,3),(6,2)\), constructs exact rational covariance matrices, and independently inverts them by Gaussian elimination. It then compares every entry with the closed spectral formulas, tests many finite parameter pairs by exact fractions, and examines convergence numerically at several positive ratios. Execution reported 3,332 exact assertions and four monotone-error numerical diagnostics passing. These are reproducible consistency checks, not substitutes for the symbolic proof of positive definiteness and the limits.

Run: `python3 verify_precision.py` (no external Python packages required).

## Relationship to prior work

Bloznelis and Leskelä introduced the general model of overlapping Bernoulli-graph layers and investigated clustering and percolation [1]. Taking deterministic layer size three and full within-layer edge strength gives the present random-triangle overlay. Bloznelis, Karjalainen and Leskelä studied degree assortativity and joint degrees of adjacent nodes [2], not the inverse covariance of all edge indicators. Their later work studies normal and stable approximation of subgraph counts [3]. The exact three-eigenspace decomposition here uses standard linear algebra for the line graph of a complete graph; the specific asymptotic partial-correlation transition is the claim, not novelty of diagonalizing a Johnson-scheme matrix.

## Limitations

This concerns **linear** least-squares partial correlations, not general conditional correlations, conditional independence, or a causal graph. The phase change is asymptotic for positive limiting layer density and is not a complete finite-size classification. At the critical ratio \(\alpha=4/3\), the leading coefficient vanishes and no eventual sign is asserted. This theorem treats cliques of size three, not random heterogeneous layer sizes, thinned layers, or arbitrary overlaps. An earlier specialized calculation or stronger general inverse-covariance result could affect historical priority; independent mathematical audit has not been performed.

## References

[1] M. Bloznelis and L. Leskelä, *Clustering and percolation on superpositions of Bernoulli random graphs*, arXiv:1912.13404, first posted 2019-12-31, https://arxiv.org/abs/1912.13404.

[2] M. Bloznelis, J. Karjalainen and L. Leskelä, *Assortativity and bidegree distributions on Bernoulli random graph superpositions*, arXiv:2002.11809, first posted 2020-02-26, https://arxiv.org/abs/2002.11809.

[3] M. Bloznelis, J. Karjalainen and L. Leskelä, *Normal and stable approximation to subgraph counts in superpositions of Bernoulli random graphs*, arXiv:2107.02683, first posted 2021-07-06, https://arxiv.org/abs/2107.02683.
