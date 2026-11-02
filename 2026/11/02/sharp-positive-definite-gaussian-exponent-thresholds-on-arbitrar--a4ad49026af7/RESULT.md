# Sharp positive-definite Gaussian exponent thresholds on arbitrary complete multipartite path metrics

## Finding
Let \(G=K_{n_1,\ldots,n_k}\) be a connected complete multipartite graph with \(k\ge2\), positive integer part sizes \(n_1\ge\cdots\ge n_k\), \(N=\sum_j n_j\), and shortest-path distance \(d\). The kernel \(K_{\lambda,p}(u,v)=\exp(-\lambda d(u,v)^p)\), \(\lambda>0\), is positive definite for **every** \(\lambda>0\) exactly when \(0\le p\le p_*\), with the threshold \(p_*\) determined explicitly below. Beyond it the kernel is indefinite for all sufficiently small positive \(\lambda\). Here all diagonal powered distances are defined to be zero, including at \(p=0\).

If \(n_1=1\) (a complete graph), then \(p_*=\infty\). Otherwise put \(t=1-2^{-p}\) and define \(t_*\) by the following two exclusive cases:

1. If \(n_1=n_2=m\ge2\), then \(t_*=1/m\).
2. If \(n_1>n_2\), then \(t_*\) is the unique solution in \((1/n_1,1/n_2)\) of
\[
 t-\frac1{n_1}=\left(\sum_{j=2}^k \frac1{1/n_j-t}\right)^{-1}.
\]

In either noncomplete case, \(p_*=-\log_2(1-t_*)\). The strict conditional-negative-type interval is exactly \(0\le p<p_*\). At \(p=p_*\), the centered distance-power form has a radical of dimension \(r-1\) if the maximum part size occurs \(r\ge2\) times, and dimension one if the largest part is unique. The corresponding minimal Euclidean embedding dimension for squared distances \(d(u,v)^{p_*}\) is \(N-r\) or \(N-2\), respectively; below threshold it is \(N-1\).

For noncomplete members, \(p_*=2\) occurs only for the three-vertex star \(K_{2,1}\). Every other noncomplete complete multipartite graph satisfies the sharp bound \(p_*\le \log_2 3\), with equality exactly for \(K_{3,1}\) and \(K_{2,1,1}\). An unbalanced three-part example is \(K_{3,2,1}\), with \(t_*=(11-\sqrt{13})/18\); the threshold need not be rational in \(t\).

## Assumptions and scope
A complete multipartite graph has all edges between distinct vertex parts and no edges within a part. Distinct vertices in different parts have distance one; distinct vertices in the same part have distance two. Positive definiteness means the matrix of kernel values on **all distinct vertices** is strictly positive definite (positive eigenvalues); nonnegative definiteness would suffice for the universal-\(\lambda\) characterization. Conditional negative type at exponent \(p\) means \(\sum_{u,v}\alpha_u\alpha_v d(u,v)^p\le0\) for every real vector \(\alpha\) with \(\sum_u\alpha_u=0\). We use the convention \(d(u,u)^p=0\) also when \(p=0\). If \(p>p_*\), failure is asserted for sufficiently small positive \(\lambda\), not for every \(\lambda\).

## Proof
**Exact decomposition.** For each vertex part \(V_j\), write \(S_j=\sum_{u\in V_j}\alpha_u\), where \(\sum_j S_j=0\). Directly grouping pairs at distances one and two gives
\[
 Q_p(\alpha):=\sum_{u,v}\alpha_u\alpha_v d(u,v)^p
 =2^p\left[t\sum_{j=1}^k S_j^2-\sum_{j=1}^k\sum_{u\in V_j}\alpha_u^2\right],\quad t=1-2^{-p}.
\]
Cauchy--Schwarz within each part yields
\[
 Q_p(\alpha)\le 2^p\sum_{j=1}^k\left(t-\frac1{n_j}\right)S_j^2,
\]
with equality exactly when \(\alpha\) is constant on every part. Therefore the entire conditional-negative-type decision reduces, without loss, to a diagonal quadratic form in \(k\) part masses constrained by \(\sum_jS_j=0\).

**Repeated largest size.** If exactly \(r\ge2\) parts attain the largest size \(m\), then for \(t<1/m\) the compressed form is negative definite. At \(t=1/m\), it vanishes precisely when \(S_j=0\) on smaller parts and the \(r\) largest part masses sum to zero, a space of dimension \(r-1\). For \(t>1/m\), assigning masses \(+1,-1\) to two maximal parts makes the form positive. This proves the first threshold and its radical.

**Unique largest size.** If \(n_1>n_2\), for \(1/n_1<t<1/n_2\) let \(w_j=(1/n_j-t)^{-1}>0\) for \(j\ge2\), and \(H=\sum_{j=2}^k w_j\). Weighted Cauchy--Schwarz gives
\[
 \sum_{j=2}^k(1/n_j-t)S_j^2\ge \frac{S_1^2}{H},
\]
with equality precisely at \(S_j=-w_j S_1/H\). Consequently nonpositivity holds exactly when \(t-1/n_1\le1/H\). The difference \(t-1/n_1-1/H(t)\) is strictly increasing: \(H(t)\) strictly increases, so \(1/H(t)\) strictly decreases. At the left endpoint the difference is negative and as \(t\uparrow1/n_2\) it is strictly positive. Hence it has exactly one root, with the asserted unique equality direction. For \(t>t_*\) inside that interval the equality vector witnesses positivity; for \(t\ge1/n_2\), masses \(S_1=1,S_2=-1\) yield a positive value. When \(t\le1/n_1\), negative definiteness is immediate except at the boundary, where the unique-largest constraint \(\sum S_j=0\) also forces strictness. Thus the interval and radical classification hold for every \(t\in[0,1)\).

**Positive-definite kernels and embedding ranks.** By the finite Schoenberg equivalence, a distance power is conditionally negative semidefinite if and only if \(\exp(-\lambda d^p)\) is positive semidefinite for every \(\lambda>0\). It is in fact strictly positive definite for every \(\lambda>0\) here: a conditionally negative power is the squared Euclidean distance on an injective finite configuration, and the Euclidean Gaussian is strictly positive definite on distinct points. Conversely, if \(Q_p(\alpha)>0\) with \(\sum\alpha=0\), then \(\alpha^{\mathsf T}K_{\lambda,p}\alpha=-\lambda Q_p(\alpha)+O(\lambda^2)<0\) for sufficiently small \(\lambda>0\). For the embedding dimension, double-centering shows that the squared Euclidean distance Gram matrix has rank \((N-1)-\dim\ker(Q_p\vert_{\sum\alpha=0})\), giving the claimed values.

**Sharp simple bound.** The star \(K_{2,1}\) has \(t_*=3/4\), hence \(p_*=2\). Every noncomplete multipartite graph other than this star either contains an isometric induced \(K_{3,1}\), an isometric induced \(K_{2,1,1}\), or equals \(K_{2,2}\); the corresponding thresholds are \(2/3,2/3,1/2\). Negative type passes to metric subspaces, so \(p_*\le\log_2 3\). Equality for the first two small witnesses holds directly. Adding vertices or parts to either witness strictly lowers the threshold: compare the repeated-maximum case, or observe that increasing a part strictly increases its reciprocal contribution \(1/(1/n_j-t)\) in the unique-maximum secular equation, which strictly moves its root downward. This proves the equality classification.

## Verification
The accompanying standalone `check_multipartite.py` uses standard-library exact fractions and exact rank elimination for a zero-sum basis. It checks strict definiteness just below and an explicit violation just above the computed threshold for 119 distinct noncomplete multipartite part profiles of total order at most ten, plus 32 exact rational endpoint rank cases with repeated maxima. The algebraic \(K_{3,2,1}\) identity is independently checked. Numerical threshold root finding and finite tests are corroborative; the proof above establishes all positive integer part sizes and all real exponents.

## Relationship to prior work
Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (first posted 2 August 2011), gives a general finite-distance-matrix test and computes the full bipartite family \(K_{n,m}\). The two-part specialization here reproduces his Theorem 3.1; neither that case nor Schoenberg's positive-kernel equivalence is claimed new. The proposed refinement is the explicit arbitrary-part profile, the exact endpoint-radical/embedding-rank classification, and the sharp distinguished-subfamily gap. Deza and Maehara's earlier metric-transform work provides a general graph spectral framework, not independently inspected in full in this review. These broader matrix procedures can compute instances without implying that a closed multipartite secular law or its complete equality spaces has already been stated.

## Limitations
The novelty comparison is bounded: an equivalent multiparameter formula may appear in older distance-matrix or metric-transform literature, particularly work not inspected in full. This statement concerns finite complete multipartite shortest-path metrics only. It does not determine the positivity threshold for any single fixed \(\lambda\) above the universal exponent, nor any infinite-graph limit or independently validated theorem.

## References
1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, posted 2011-08-02, Theorem 3.1 and Section 2. https://arxiv.org/abs/1108.0451
2. M. Deza and H. Maehara, *Metric Transforms and Euclidean Embeddings*, Transactions of the American Mathematical Society 317 (1990), 661–671, DOI:10.2307/2001482.
3. I. J. Schoenberg, classical equivalence between conditional negative type and Gaussian positive-definite kernels, 1938. The equivalence is recalled in Sánchez's introduction.
