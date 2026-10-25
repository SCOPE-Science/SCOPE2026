# Exact negative covariance of two- and three-cycle counts in uniform attachment multigraphs

## Finding

Fix arbitrary integers \(n\ge 2\) and \(m\ge 2\). In the uniform attachment multigraph on vertices \(1,\ldots,n\), each newly arrived vertex has \(m\) independently sampled, labelled outgoing edges, each choosing a uniformly random older endpoint. Let \(P_{n,m}\) count unordered pairs of parallel edges (the two-cycles), and let \(T_{n,m}\) count edge-distinguished triangles (the three-cycles, including multiplicity). Then

\[
\boxed{\operatorname{Cov}(P_{n,m},T_{n,m})=-m^2(m-1)\sum_{q=2}^{n-1}\frac{q-1}{q^3}.}
\]

The covariance is zero for \(n=2\), strictly negative for every \(n\ge3\), and decreases strictly as \(n\) increases with \(m\) fixed. In particular, for every fixed \(m\ge2\),

\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}(P_{n,m},T_{n,m})=-m^2(m-1)[\zeta(2)-\zeta(3)]<0.}
\]

The finite identity is also valid when \(m=m(n)\) varies arbitrarily with \(n\): no fixed-outdegree hypothesis is needed. For fixed \(m\), the exact variance of the two-cycle count is

\[
\operatorname{Var}(P_{n,m})=\binom m2\left(H_{n-1}-H_{n-1}^{(2)}\right),
\]

so the known order \(\operatorname{Var}(T_{n,m})=\Theta(\log n)\) implies \(\operatorname{Corr}(P_{n,m},T_{n,m})=-\Theta(1/\log n)\) as \(n\to\infty\) for fixed \(m\). This latter statement invokes the variance-order theorem of Björklund et al., not an independent determination of the three-cycle variance constant.

## Assumptions and scope

Write \(X_{j,a}\in\{1,\ldots,j-1\}\) for the endpoint of edge label \(a\in\{1,\ldots,m\}\) born with vertex \(j\), for every \(2\le j\le n\). All the \(X_{j,a}\) are mutually independent and each \(X_{j,a}\) is uniform on its declared set. Edges retain their labels, and parallel copies are distinct edges.

Define the number of parallel-edge pairs at arrival \(j\) by

\[
Q_j=\sum_{1\le a<b\le m}{\bf1}\{X_{j,a}=X_{j,b}\},\qquad P_{n,m}=\sum_{j=2}^n Q_j.
\]

Define triangles as copies with three distinct vertices and a choice of one edge along each of their three sides. Their count is

\[
T_{n,m}=\sum_{1\le i<j<k\le n}\sum_{a=1}^m\sum_{\substack{b,c=1\\b\ne c}}^m {\bf1}\{X_{j,a}=i\}\,{\bf1}\{X_{k,b}=i,\ X_{k,c}=j\}.
\]

The restriction \(b\ne c\) is necessary because a single outgoing edge from \(k\) cannot end at both \(i\) and \(j\). The formula is for multigraph counts, not for counts of distinct triples that support at least one edge of each type. Vertices are birth-labelled; no conditioning on simple graphs is imposed.

## Proof

For each triangle summand with fixed \(i<j<k\), edge labels \(a,b,c\) and \(b\ne c\), write \(A={\bf1}\{X_{j,a}=i\}\) and \(B={\bf1}\{X_{k,b}=i,X_{k,c}=j\}\). The random variables \(A\) and \(B\) are independent, and \(\mathbb E A=1/(j-1)\). Because \(Q_\ell\) uses only the edges born at \(\ell\), its covariance with \(AB\) is zero for \(\ell\notin\{j,k\}\).

For \(\ell=j\), consider one equality indicator \({\bf1}\{X_{j,r}=X_{j,s}\}\) within \(Q_j\). It is independent of \({\bf1}\{X_{j,a}=i\}\) when \(a\notin\{r,s\}\); when \(a\in\{r,s\}\), their joint probability is \(1/(j-1)^2\), again the product of their means. Consequently \(\operatorname{Cov}(Q_j,A)=0\) and \(\operatorname{Cov}(Q_j,AB)=0\).

For \(\ell=k\), put \(q=k-1\). Consider one term \(I_{rs}={\bf1}\{X_{k,r}=X_{k,s}\}\) in \(Q_k\). For \(\{r,s\}\ne\{b,c\}\), either it is independent of \(B\), or it shares exactly one sampled coordinate with \(B\); in the latter case its joint probability with \(B\) is \(q^{-3}\), equal to \(\mathbb E I_{rs}\,\mathbb E B\). For the unique term with \(\{r,s\}=\{b,c\}\), the events \(I_{bc}=1\) and \(B=1\) are incompatible because \(i\ne j\); their product has expectation zero, whereas \(\mathbb E I_{bc}\,\mathbb E B=q^{-3}\). Thus

\[
\operatorname{Cov}(Q_k,B)=-\frac{1}{(k-1)^3},\qquad
\operatorname{Cov}(Q_k,AB)=-\frac{1}{(j-1)(k-1)^3}.
\]

There are exactly \(m\) choices for \(a\) and \(m(m-1)\) ordered choices for \((b,c)\). Summing over \(1\le i<j<k\le n\), then over the unique contributing arrival \(k\), gives

\[
\begin{aligned}
\operatorname{Cov}(P_{n,m},T_{n,m})
&=-m^2(m-1)\sum_{k=3}^n\sum_{j=2}^{k-1}\sum_{i=1}^{j-1}\frac{1}{(j-1)(k-1)^3}\\
&=-m^2(m-1)\sum_{k=3}^n\frac{k-2}{(k-1)^3}.
\end{aligned}
\]

The sign and strict decrease are immediate. The limit exists because the summand is \(q^{-2}-q^{-3}\) with \(q=k-1\), so the infinite sum is \(\zeta(2)-\zeta(3)>0\). No limiting interchange is needed for the finite identity.

To derive the two-cycle variance, note that equality indicators \({\bf1}\{X_{j,r}=X_{j,s}\}\) for distinct unordered index pairs are pairwise uncorrelated, including when they share one index: the probability that three independent uniform draws are equal is \((j-1)^{-2}\). Hence

\[
\operatorname{Var}(Q_j)=\binom m2\left(\frac{1}{j-1}-\frac{1}{(j-1)^2}\right).
\]

Different arrivals are independent, and summation gives the stated variance. For fixed \(m\), Theorem 3.5 of the cited primary source applies to the three-cycle as a unicyclic graph with no attached tree edges and yields \(\operatorname{Var}(T_{n,m})=\Theta(\log n)\). The correlation-rate consequence follows, since the covariance tends to a finite strictly negative limit and \(\operatorname{Var}(P_{n,m})=\Theta(\log n)\).

## Verification

The included `verify.py` uses only the Python standard library. It independently enumerates every attachment choice for several small \((n,m)\), counts parallel pairs directly from the sampled parent tuples, and counts triangles by the product of unordered vertex-pair edge multiplicities. It then computes exact rational covariances and compares them to the claimed formula. Invocation: `python verify.py`. It checks 30,377 attachment configurations across ten test instances and prints `VERIFY_OK` on success. These finite checks detect normalization and multiplicity mistakes; they are not the unrestricted proof.

## Relationship to prior work

Björklund, Holmgren, Janson and Lo introduce this exact edge-labelled multigraph convention in their arXiv preprint, Example 2.1 and the model specification; their Example 3.4 gives separate means of the two- and three-cycle counts. Their Theorem 3.3 gives a multivariate approximation by *independent* Poisson laws for distinct cycle lengths when \(m\) is fixed, and Theorem 3.5 gives the variance order of a cycle count. These results neither state nor numerically determine the signed finite covariance or its nonzero limiting constant; convergence in total variation of varying integer-valued count laws does not itself yield this mixed unbounded moment. Their covariance-based coupling estimates bound errors without evaluating the mixed pair at this precision. The exact negative finite covariance here supplies an additional second-order description beyond the first-order asymptotic independence.

The calculation also applies uniformly to each finite choice of \(m\), including sequences of outdegrees varying with \(n\); this should not be confused with a proof of multivariate Poisson approximation when \(m\) grows.

## Limitations

The statement depends on independently and uniformly chosen **labelled** outgoing edges, retaining multiplicities. It does not assert negative association of the entire vector of cycle counts, analogous covariance signs for longer cycles, or the same identity after conditioning on simplicity or changing the attachment rule. No exact leading constant for \(\operatorname{Var}(T_{n,m})\) is claimed. Although full-text comparison with the closest identified primary article and a targeted literature search found no previously stated equivalent formula, an uncatalogued earlier computation remains a priority risk. Independent validation has not been performed.

## References

1. J. Björklund, C. Holmgren, S. Janson, T. Y. Y. Lo, *Approximation of Subgraph Counts in the Uniform Attachment Model*, arXiv:2311.04184v1 (7 November 2023), https://arxiv.org/pdf/2311.04184 . Relevant material: Sections 1–3 (construction, Examples 2.1/3.4, Theorems 3.3/3.5), Section 5 (cycle indicator coupling), and Section 7 (cycle overlap estimates).
2. J. Björklund, C. Holmgren, S. Janson, T. Y. Y. Lo, *Approximation of subgraph counts in the uniform attachment model*, *Combinatorics, Probability and Computing* **34** (2025), 90–114, first published online 10 October 2024, https://doi.org/10.1017/S0963548324000294 . This is the journal version of [1], not an independent source.
