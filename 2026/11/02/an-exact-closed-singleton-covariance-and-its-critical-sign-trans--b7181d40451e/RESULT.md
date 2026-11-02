# An exact closed–singleton covariance and its critical sign transition in site-percolated recursive trees

## Finding

For a uniformly random recursive tree on \(n\geq1\) vertices, retain each vertex independently with probability \(p\in(0,1)\). Write \(U_n\) for the number of deleted (closed) vertices and \(S_n\) for the number of open connected components having exactly one vertex. Let \(q=1-p\) and
\[
 s_p=\frac{pq}{1+p},\qquad
 \alpha_p=\frac{pq(p^2+2p-1)}{(1+p)^2},\qquad
 b_p=\frac{2p^3q}{1+p},
\]
\[
 R_n(p)=\frac{\Gamma(n-p)}{\Gamma(n)\Gamma(1-p)},\qquad
 H_{n-1}(p)=\sum_{j=1}^{n-1}\frac{1}{j-p}.
\]
(The sum is zero when \(n=1\).) Then, at **every finite size**, 
\[
 \mathbb E S_n=ns_p+(p-s_p)R_n(p),
\]
\[
 \boxed{\operatorname{Cov}(U_n,S_n)=n\alpha_p+R_n(p)\left[-pq-\alpha_p+b_pH_{n-1}(p)\right].}
\]
In particular, setting \(p_\star=\sqrt2-1\): for every fixed \(p<p_\star\), the covariance is eventually negative and asymptotic to \(n\alpha_p\); for every fixed \(p>p_\star\), it is eventually positive and asymptotic to \(n\alpha_p\). At the **unique critical probability** \(p=p_\star\), the linear term cancels, leaving the positive, vanishing asymptotic
\[
 \boxed{\operatorname{Cov}(U_n,S_n)\sim
 \frac{b_{p_\star}}{\Gamma(1-p_\star)}n^{-p_\star}\log n.}
\]

The centered vector also has a joint Gaussian limit:
\[
 \frac1{\sqrt n}\begin{pmatrix}U_n-nq\\S_n-ns_p\end{pmatrix}
 \ \Longrightarrow\ N_2(0,\Sigma_p),\qquad
 \Sigma_p=\begin{pmatrix}
 pq&\alpha_p\\
 \alpha_p&\dfrac{pq(2p^3+7p^2+1)}{(1+p)^2(1+2p)}
 \end{pmatrix}.
\]
Consequently the limiting Gaussian coordinates are independent **exactly** at \(p=p_\star\). This Gaussian limit is included to identify the meaning of the explicit covariance; general small-urn Gaussian convergence is established in earlier literature, and is not claimed as an independently novel principle.

## Assumptions and scope

Construct the random recursive tree sequentially. The first vertex is its root; for each \(j\geq2\), vertex \(j\) attaches to one uniformly chosen vertex of \(\{1,\ldots,j-1\}\), independently of previous attachments. Site states are independent Bernoulli variables of common parameter \(p\), independent of the tree. Deleted vertices are not counted as singleton open components. All formulas hold under the full (annealed) tree-and-site law. The asymptotic statements hold as \(n\to\infty\) with fixed \(p\in(0,1)\); no uniformity near the critical parameter or the endpoints is claimed.

## Proof

**1. Exact transition law.** Conditional on \((U_n,S_n)=(u,s)\), the change \((\Delta U,\Delta S)\) on adding vertex \(n+1\) is \((1,0)\) with probability \(q\), \((0,1)\) with probability \(pu/n\), and \((0,-1)\) with probability \(ps/n\). The remaining probability produces \((0,0)\). These cases are exhaustive: an open arrival adjoining a closed vertex creates a singleton, while one adjoining an existing singleton absorbs it into a two-vertex component. An arrival cannot otherwise alter the number of open singletons. Thus
\[
 \mathbb E[\Delta U\mid\mathcal F_n]=q,\quad
 \mathbb E[\Delta S\mid\mathcal F_n]=\frac{p}{n}(U_n-S_n),\quad
 \Delta U\,\Delta S=0.
\]
At \(n=1\), the vector is \((1,0)\) with probability \(q\) and \((0,1)\) with probability \(p\). In particular \(\mathbb ES_1=p\) and \(\operatorname{Cov}(U_1,S_1)=-pq\).

**2. Mean and finite covariance.** The closed sites are i.i.d., hence \(\mathbb E U_n=nq\) and \(\operatorname{Var}(U_n)=npq\). Writing \(m_n=\mathbb E S_n\) gives
\[
 m_{n+1}=\left(1-\frac pn\right)m_n+pq,
 \qquad m_1=p.
\]
Since \(R_1=1\) and \(R_{n+1}=(1-p/n)R_n\), this solves to \(m_n=ns_p+(p-s_p)R_n\).

For \(c_n=\operatorname{Cov}(U_n,S_n)\), total covariance and the disjointness \(\Delta U\Delta S=0\) yield
\[
 c_{n+1}=\left(1-\frac pn\right)c_n+\frac pn\operatorname{Var}(U_n)
 -\frac{pq}{n}\left(\mathbb EU_n-\mathbb ES_n\right).
\]
Substitution of the preceding mean formulas simplifies this exactly to
\[
 c_{n+1}=\left(1-\frac pn\right)c_n+(1+p)\alpha_p+\frac{b_p}{n}R_n.
\]
The affine function \(\alpha_p n\) is a particular solution. For \(d_n=c_n-n\alpha_p\), divide the homogeneous remainder equation by \(R_{n+1}\):
\[
 \frac{d_{n+1}}{R_{n+1}}-\frac{d_n}{R_n}=\frac{b_p}{n-p}.
\]
Summing from \(1\) to \(n-1\), using \(d_1=-pq-\alpha_p\), proves the claimed exact finite covariance, including \(n=1\).

**3. The sign transition.** The Gamma-ratio asymptotic and a harmonic-sum estimate give
\[
 R_n(p)\sim\frac{n^{-p}}{\Gamma(1-p)},\qquad
 H_{n-1}(p)=\log n+O_p(1).
\]
Because \(\alpha_p\) has the sign of \(p^2+2p-1\), it changes sign exactly once in \((0,1)\), at \(p_\star\). Away from this root, the correction is \(O_p(n^{-p}\log n)\), and at the root the \(b_pH_{n-1}\) term dominates the constant in brackets. Since \(b_p>0\), the critical asymptotic is positive and tends to zero. Note that this is an **eventual** sign statement; the finite-size sign need not agree with the limiting sign for every \(n\).

**4. Joint central limit theorem and covariance matrix.** Define \(Z_n=(U_n-nq,S_n-ns_p)^\mathsf T\) and the bounded martingale difference \(\xi_{n+1}=(\Delta U,\Delta S)^\mathsf T-\mathbb E[(\Delta U,\Delta S)^\mathsf T\mid\mathcal F_n]\). The exact drift becomes
\[
 Z_{n+1}=\left(I+\frac{B}{n}\right)Z_n+\xi_{n+1},\qquad
 B=\begin{pmatrix}0&0\\p&-p\end{pmatrix}.
\]
Its deterministic propagator over times \(k+1,\ldots,n-1\) is
\[
 M_{n,k}=\begin{pmatrix}1&0\\1-w_{n,k}&w_{n,k}\end{pmatrix},\quad
 w_{n,k}=\prod_{j=k+1}^{n-1}\left(1-\frac pj\right),
\]
with the initial \(Z_1\) propagated using the analogous product beginning at \(j=1\). Every propagator is bounded, so martingale orthogonality implies \(\mathbb E\|Z_n\|^2=O_p(n)\), whence \(U_n/n\to q\) and \(S_n/n\to s_p\) in probability. By the finite transition law, the conditional covariance of \(\xi_{n+1}\) converges in probability to
\[
 G_p=\begin{pmatrix}pq&-qs_p\\-qs_p&p(q+s_p)-s_p^2\end{pmatrix}.
\]
For \(k/n\to t\in(0,1]\), \(M_{n,k}\to M(t)=\bigl(\begin{smallmatrix}1&0\\1-t^p&t^p\end{smallmatrix}\bigr)\). Boundedness of \(\xi_{n+1}\), the deterministic propagators, and the preceding law of large numbers verify the multivariate martingale triangular-array Lindeberg condition and its conditional variance convergence. The finitely early arrivals contribute negligibly after division by \(\sqrt n\), while the remaining conditional variance sums converge to
\[
 \Sigma_p=\int_0^1M(t)G_pM(t)^\mathsf T\,dt.
\]
Integrating \(t^p\) and \(t^{2p}\) gives exactly the matrix displayed in the finding. For \(p\in(0,1)\), \(G_p\) is positive definite (there are three noncollinear outcomes with positive limiting probabilities), so is \(\Sigma_p\). The martingale central limit theorem proves the asserted joint convergence. Its off-diagonal integral agrees with \(\alpha_p\), as also follows independently from the exact finite covariance.

## Verification

The standalone Python 3 program `verify_singleton.py` independently enumerates every recursive-tree parent sequence and every site configuration through six vertices at five rational values of \(p\), compares the exact formula against rational moments, and checks the integrated covariance matrix by rational arithmetic. It also checks large-size second-moment recurrences numerically. Running `python3 verify_singleton.py` produces `PASS: 180 independent exact/limit assertions; all n <= 6, five rational retention parameters; n=3001 moment recurrences.` These checks corroborate the proof; finite enumerations cannot establish the infinite-size limits.

## Relationship to prior work

Gu and Yuan [1], publicly posted August 22, 2024, establish the site-percolation model's complete cluster-frequency law of large numbers, including the singleton proportion \(s_p\), and give the Markov transition mechanism from which the present two-dimensional reduction starts. Kalay and Ben-Naim [2] derive related cluster-size averages in a fixed-number deletion variant. Janson [3] proves general Gaussian and covariance theory for small balanced generalized Pólya urns; such theory covers the abstract Gaussian mechanism, and is not claimed as new here. The distinct mathematical assertion investigated here is the **specialized finite-size closed–singleton covariance identity**, its cancellation to order \(n^{-p}\log n\) at the unique threshold, and the explicit resulting sign phase diagram. Janson [4] concerns graph-uncovering edge counts and connected-component totals, not this singleton-versus-deletion covariance. These comparisons leave a residual possibility of an equivalent calculation in less easily indexed urn or occupancy literature.

## Limitations

The formulas assume a uniform recursive tree, independent site retention and fixed \(p\). They do not classify signs at every finite \(n\), imply independence of the actual closed/singleton counts at the threshold, extend automatically to bond percolation, or address larger component-size coordinates. The Gaussian theorem is not asserted to supersede general balanced-urn central limit results. Full historical priority and independent validation remain unresolved.

## References

[1] C. Gu and L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515v1 (publicly posted 2024-08-22), https://arxiv.org/abs/2408.12515 . Relevant: Definition 1, (1.3)–(1.8), Theorem 1.

[2] Z. Kalay and E. Ben-Naim, *Fragmentation of random trees*, Journal of Physics A 48 (2015), preprint available at https://cnls.lanl.gov/~ebn/pubs/treefrag/treefrag.pdf . Relevant: recursive-tree fragmentation cluster frequency discussion.

[3] S. Janson, *Mean and variance of balanced Pólya urns*, arXiv:1602.06203 (original 2016 posting), https://arxiv.org/abs/1602.06203 . Relevant: abstract normality, variance convergence, general small-urn framework.

[4] S. Janson, *Uncovering a graph*, Probability Theory and Related Fields (2025), https://doi.org/10.1007/s00440-025-01401-9 . Relevant: Sections 8–9 on component totals and small subgraphs.
