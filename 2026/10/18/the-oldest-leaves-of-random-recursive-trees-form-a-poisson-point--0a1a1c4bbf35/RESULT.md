# The oldest leaves of random recursive trees form a Poisson point process

## Finding

The earliest-born leaves in a uniform random recursive tree survive on a square-root scale and, after rescaling their birth labels, form an inhomogeneous Poisson point process. More precisely,
\[
\Xi_n:=\sum_{i=2}^{n}\mathbf1\{i\text{ is a leaf of }T_n\}\,\delta_{(i-1)/\sqrt{n-1}}
\quad\xRightarrow[n\to\infty]{\mathrm{vague}}\quad
\operatorname{PPP}(x\,dx)
\]
on \([0,\infty)\). The limit has mean measure \(\Lambda([0,z])=z^2/2\).

For every fixed positive integer \(k\), let \(J_{n,k}\) denote the \(k\)-th smallest label among the leaves, with \(+\infty\) used if fewer than \(k\) leaves exist. Then
\[
\frac{J_{n,k}-1}{\sqrt{n-1}}\ \xRightarrow[n\to\infty]{}\ \sqrt{2G_k},
\qquad G_k\sim\operatorname{Gamma}(k,1).
\]
Jointly for any fixed number of ranks, the squared limiting locations divided by two are consecutive arrival times of a unit-rate Poisson process. In particular, the first leaf label has the Rayleigh tail
\[
\lim_{n\to\infty}\Pr\left\{\frac{J_{n,1}-1}{\sqrt{n-1}}>z\right\}=e^{-z^2/2}
\qquad(z\ge0).
\]

The exact finite-size input is itself a multivariate identity: for every \(n\ge2\), every \(1\le r\le n-1\), and all \(2\le i_1<\cdots<i_r\le n\),
\[
\Pr\{i_1,\ldots,i_r\text{ are all leaves}\}
=\prod_{j=1}^{r}\frac{i_j-j}{n-j}.
\tag{1}
\]

## Assumptions and scope

At time \(t\in\{2,\ldots,n\}\), vertex \(t\) selects one parent uniformly from the older vertices \(\{1,\ldots,t-1\}\), independently of all other arrivals. The root is vertex \(1\). A leaf means a vertex of outdegree zero; the root is excluded from \(\Xi_n\). Point-process convergence is vague weak convergence on the locally compact space \([0,\infty)\). The limit statement concerns fixed bounded windows in the rescaled label coordinate. The order-statistic result holds for each fixed rank; it does not claim uniformity when the rank increases with \(n\).

## Proof

**1. Exact joint leaf probabilities.** The choices of parents made at distinct arrival times are independent. A specified vertex \(i\ge2\) is still a leaf at time \(n\) exactly when none of \(i+1,\ldots,n\) chose \(i\) as its parent; hence \(\Pr\{i\text{ is a leaf}\}=(i-1)/(n-1)\). To obtain (1), order the specified labels increasingly. First require that vertex \(i_1\) has no later children. At each later arrival, its parent is thereby chosen uniformly among the other available older vertices. Conditional on the first \(j-1\) specified vertices having no children, every parent choice after time \(i_j\) is uniform among the \(t-j\) older vertices not among those \(j-1\) forbidden labels. The conditional probability that no arrival attaches to vertex \(i_j\) is the telescoping product
\[
\prod_{t=i_j+1}^n\frac{t-j-1}{t-j}
=\frac{i_j-j}{n-j}.
\]
The constraints at times up to \(i_j\) do not affect this product. Multiplying the conditional probabilities gives (1). This includes the boundary case \(r=n-1\).

**2. Domination and factorial sums.** Put \(q_{n,i}:=(i-1)/(n-1)\). Because
\[
\frac{i_j-j}{n-j}\le\frac{i_j-1}{n-1}
\quad\text{for }i_j\le n,
\]
the exact identity gives for any set \(S\) of distinct nonroot labels the bound \(\Pr\{S\text{ consists of leaves}\}\le\prod_{i\in S}q_{n,i}\). Fix a continuous function \(f\ge0\) supported on \([0,R]\), and define \(b_{n,i}:=1-e^{-f((i-1)/\sqrt{n-1})}\). The discrete weighted intensity satisfies
\[
A_n:=\sum_{i=2}^n b_{n,i}q_{n,i}
\longrightarrow A:=\int_0^\infty(1-e^{-f(x)})x\,dx.
\tag{2}
\]
For each fixed \(r\ge1\), (1), uniformly over labels in this compact window, differs from \(\prod_{j=1}^r q_{n,i_j}\) by \(O_{r,R}(n^{-(r+1)/2})\). Indeed each numerator differs from \(i_j-1\) by at most \(r-1\), while each denominator equals \(n+O_r(1)\), and the labels are \(O_R(\sqrt n)\). There are \(O_{r,R}(n^{r/2})\) possible \(r\)-subsets in the window. Thus
\[
\sum_{2\le i_1<\cdots<i_r\le n}
\left(\prod_{j=1}^r b_{n,i_j}\right)
\Pr\{i_1,\ldots,i_r\text{ all leaves}\}
\longrightarrow\frac{A^r}{r!}.
\tag{3}
\]
The last step also uses that omitting coincident indices from the \(r\)-fold product of the sum in (2) has vanishing effect, since \(\max_i b_{n,i}q_{n,i}=O_R(n^{-1/2})\). Moreover, the left side of (3) is at most \(A_n^r/r!\) by the domination inequality. For sufficiently large \(n\), these terms are bounded by \(C_R^r/r!\) for a constant independent of \(r\).

**3. Laplace-functional limit.** Expand the finite product exactly:
\[
\begin{aligned}
\mathbb E[e^{-\langle f,\Xi_n\rangle}]
&=\mathbb E\prod_{i=2}^{n}(1-b_{n,i}\mathbf1\{i\text{ leaf}\})\\
&=\sum_{r=0}^{n-1}(-1)^r
\sum_{i_1<\cdots<i_r}
\left(\prod_{j=1}^r b_{n,i_j}\right)
\Pr\{i_1,\ldots,i_r\text{ all leaves}\}.
\end{aligned}
\]
Equation (3) and the uniformly summable \(C_R^r/r!\) majorant justify interchanging the limit and infinite alternating sum. The result is
\[
\lim_{n\to\infty}\mathbb E[e^{-\langle f,\Xi_n\rangle}]
=e^{-A}
=\exp\left[-\int_0^\infty(1-e^{-f(x)})x\,dx\right],
\]
the Laplace functional of \(\operatorname{PPP}(x\,dx)\). Convergence of Laplace functionals of locally finite point measures proves the claimed point-process convergence.

**4. The ordered leaves.** On each bounded interval the limiting process is simple and puts no mass on its boundary. Its count in \([0,z]\) has distribution \(\operatorname{Poisson}(z^2/2)\). Therefore, for each fixed \(k\ge1\),
\[
\Pr\{(J_{n,k}-1)/\sqrt{n-1}>z\}
\longrightarrow e^{-z^2/2}
\sum_{j=0}^{k-1}\frac{(z^2/2)^j}{j!}.
\]
The limiting process almost surely has infinitely many points on \([0,\infty)\), so the \(+\infty\) convention has vanishing probability for each fixed rank. The deterministic transformation \(x\mapsto x^2/2\) sends its intensity to unit Lebesgue measure, proving the Gamma arrival-time statement and its joint version.

## Verification

The standalone standard-library script `verify.py` exhaustively enumerates all uniform recursive trees with up to eight vertices, compares every subset's exact empirical joint leaf probability with (1), and checks the independent attachment product. For sizes \(15,25,45\) it separately checks all singleton, pair and triple leaf probabilities by exact rational arithmetic. For three larger sizes it verifies convergence of the first two factorial moments in a unit rescaled window. Its completed run reported 17,287 passing exact/computational consistency assertions. These finite checks do not prove the point-process limit; Steps 1–4 above do.

## Relationship to prior work

Janson's 2004/2005 degree-profile results give asymptotic Gaussian behavior for global outdegree counts in recursive trees, including leaves, not the distribution of the earliest leaf birth indices [1]. Kuba and Panholzer obtain exact laws for the outdegree of one label and limit regimes according to the label's size; their Theorems 1–4 treat a prescribed vertex, not the joint rare-event configuration over \(O(\sqrt n)\) early labels [2]. Mahmoud and Smythe consider leaf counts within a subtree rooted at a *fixed* label [3], whereas the present statistic orders globally surviving zero-outdegree vertices by their birth labels. Dobrow and Smythe's Poisson approximation concerns binary-search comparisons and internode distances [4], not a point process of surviving leaves. Later joint-degree results for a fixed number of labels also do not give this growing rare-label configuration [5]. The natural structural distinction is between one-label marginal degree information or global leaf totals and a complete extreme-label point process.

## Limitations

No quantitative convergence rate is asserted, and the result is not extended to weighted-attachment or plane-oriented recursive trees. The explicit multivariate leaf probability is derived here rather than attributed as an established priority claim; earlier equivalent identities or general-purpose limit theorems might implicitly imply the result. Some older relevant full texts were not accessible for complete inspection; this is a priority risk, not evidence of absence. Verification is mathematical and computational as described, not independent expert validation.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. First publicly posted version of record: 16 November 2004. DOI: 10.1002/rsa.20046.
2. M. Kuba and A. Panholzer, *On the degree distribution of the nodes in increasing trees*, Journal of Combinatorial Theory, Series A 114 (2007), 597–618. DOI: 10.1016/j.jcta.2006.08.003. Publicly readable author's manuscript: https://www.dmg.tuwien.ac.at/kuba/nodedegree3.pdf.
3. H. M. Mahmoud and R. T. Smythe, *On the distribution of leaves in rooted subtrees of recursive trees*, Annals of Applied Probability 1 (1991), 406–418. DOI: 10.1214/aoap/1177005874.
4. R. P. Dobrow and R. T. Smythe, *Poisson approximations for functionals of random trees*, Random Structures & Algorithms 9 (1996), 79–92.
5. B. Lodewijks, *Joint degree and depth distributions of vertices in random recursive trees*, arXiv:2204.09032 (2022).
