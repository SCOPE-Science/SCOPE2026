# Poisson clocks for consecutive missing part sizes in random partitions

## Finding
Let \(\lambda_N\) be uniformly sampled from the ordinary, unrestricted integer partitions of \(N\). For each fixed integer \(r\ge 2\), mark every positive integer \(j\) for which **all** sizes \(j,j+1,\ldots,j+r-1\) are absent from \(\lambda_N\). Put
\[
a_N=N^{r/(2(r+1))},\qquad c=\pi/\sqrt{6},\qquad
\Xi_{r,N}=\sum_{j\ge1}\mathbf 1_{\{j,\ldots,j+r-1\}\cap\lambda_N=\varnothing}\,\delta_{j/a_N}.
\]
As \(N\to\infty\), the locally finite random point measures \(\Xi_{r,N}\) converge in distribution (vaguely on \([0,\infty)\)) to an inhomogeneous Poisson point process of intensity
\[
\boxed{\rho_r(x)\,dx=c^r x^r\,dx\quad (x\ge0).}
\]
Here \(\{j,\ldots,j+r-1\}\cap\lambda_N=\varnothing\) means that none of these integers occurs as a part, regardless of multiplicity. In particular, if \(M_{r,k}\) is the starting index of the \(k\)-th marked run (ordered by index, and \(M_{r,1}\) is the \(r\)-chain minimal excludant), then for every fixed positive integer \(k\) and every real \(x\ge0\),
\[
\boxed{\lim_{N\to\infty}\Pr\left\{M_{r,k}>x a_N\right\}
=e^{-\Lambda_r(x)}\sum_{\ell=0}^{k-1}\frac{\Lambda_r(x)^\ell}{\ell!},\qquad
\Lambda_r(x)=\frac{\pi^r x^{r+1}}{6^{r/2}(r+1)}.}
\]
For the first run, the limit is Weibull with shape \(r+1\). At \(r=2\), for example, \(\Pr\{M_{2,1}>xN^{1/3}\}\to\exp(-\pi^2x^3/18)\).

## Assumptions and scope
An unrestricted partition is an unordered multiset of positive integers with sum \(N\), sampled uniformly among the \(p(N)\) possible multisets. All occurrences of an integer count as the same part size for purposes of absence. The run length \(r\) and the order index \(k\) are fixed as \(N\) tends to infinity; there is no uniform assertion for growing \(r\) or \(k\). A marked run at \(j\) does not require a present part at \(j-1\) or \(j+r\); overlapping marked runs are counted at their distinct starting indices. The point process is tested on compact subsets of \([0,\infty)\).

## Proof
**1. Transfer of the small-part multiplicities.** For fixed \(N\), let \(Z_{j,N}\), \(j\ge1\), be independent geometric random variables with
\[
\Pr\{Z_{j,N}=h\}=(1-q_N^j)(q_N^j)^h,\quad h\ge0,\qquad
q_N=\exp(-c/\sqrt N).
\]
By Theorems 4.13(1) and 4.14 of DeSalvo--Menz [3], specialized to unrestricted ordinary partitions (allowed size set all positive integers; their part-growth parameters are \(B=r_{\mathrm{source}}=1\)), for every \(m_N=o(\sqrt N)\) the total variation distance between \((m_1(\lambda_N),\ldots,m_{m_N}(\lambda_N))\) and \((Z_{1,N},\ldots,Z_{m_N,N})\) tends to zero. Here the specialization of their constant is \(c=\sqrt{\zeta(2)}=\pi/\sqrt6\). Since \(a_N=o(\sqrt N)\) for fixed \(r\), this applies to every window of size \(\lfloor K a_N\rfloor+r\), for any fixed finite \(K>0\). Any event or measurable statistic based only on these coordinates inherits the same total variation bound.

**2. The independent rare-run model.** Define \(Y_{j,N}=\mathbf1_{\{Z_{j,N}=0\}}\) and \(I_{j,N}=\prod_{t=0}^{r-1}Y_{j+t,N}\). Put \(\varepsilon_N=a_N/\sqrt N=N^{-1/(2(r+1))}\). Then the \(Y_{j,N}\) are independent and
\[
\theta_{j,N}:=\Pr(Y_{j,N}=1)=1-e^{-cj/\sqrt N},\qquad
a_N\varepsilon_N^r=1.
\]
On each fixed scaled window \(1\le j\le Ka_N\), Taylor's theorem, with \(r,K\) fixed, implies uniformly
\[
\Pr(I_{j,N}=1)=\prod_{t=0}^{r-1}\theta_{j+t,N}
=c^r\varepsilon_N^r(j/a_N)^r+O_{r,K}(\varepsilon_N^{r+1}+\varepsilon_N^r/a_N).
\]
Consequently, for every interval \(B\subset[0,K]\) with endpoints fixed,
\[
\sum_{j:\,j/a_N\in B}\Pr(I_{j,N}=1)
\longrightarrow \int_B c^r x^r\,dx.
\]

**3. Clusters of overlapping starts vanish.** Fix an integer \(s\ge1\) and finitely many disjoint bounded scaled intervals. In the joint factorial-moment sum of their marked-start counts, consider an ordered tuple of \(s\) distinct start indices. Connect indices whose difference is less than \(r\). Distinct connected components use disjoint sets of \(Y_{j,N}\)'s and are independent. A component of size \(t\) has at least \(r+t-1\) different missing part sizes, so its simultaneous occurrence probability is at most \(O_{r,K,s}(\varepsilon_N^{r+t-1})\). There are at most \(O_{r,K,s}(a_N)\) placements of each component: after selecting its least index, every subsequent connected index lies within at most \(s(r-1)\) places. Summing the contribution of a component therefore gives
\[
O_{r,K,s}\left(a_N\varepsilon_N^{r+t-1}\right)
=O_{r,K,s}(\varepsilon_N^{t-1}).
\]
Thus every configuration involving a component of size \(t\ge2\) contributes \(o(1)\) to the total factorial moment; singleton components contribute \(O(1)\). If all starts are separated by at least \(r\), the indicators are independent. Their factorial-moment sums converge to the products of the limiting intensity integrals from Step 2, because deleting the \(O(a_N^{s-1})\) tuples with a nearby pair changes the product sum by \(O(a_N^{-1})\). Therefore the joint factorial moments of counts in every finite collection of disjoint bounded intervals converge to those of independent Poisson random variables with means \(\int_B c^r x^r dx\). These limiting joint laws are moment-determinate and their first moments give tightness. Hence the point processes of \(I_{j,N}\) converge to the claimed Poisson point process.

**4. Return to fixed-size partitions and order statistics.** The random process restricted to \([0,K]\) depends on multiplicities only through \(\lfloor Ka_N\rfloor+r\). Step 1 transfers the just-proved weak convergence from the independent model to the uniformly sampled partition, for every finite \(K\). These restrictions determine vague convergence on \([0,\infty)\). For fixed \(x\ge0\), the limiting process has no point at \(x\). The exact event \(M_{r,k}>xa_N\) is that there are at most \(k-1\) marked starts at indices not exceeding \(\lfloor xa_N\rfloor\). Its limiting probability is the displayed Poisson lower tail. At \(x=0\), both sides equal one. This proves every assertion.

## Verification
A self-contained Python 3 verifier, `verify.py`, enumerates all ordinary partitions for \(0\le N\le28\), and compares exact forbidden-part counts with the coefficient identity
\[
\#\{\lambda\vdash N:S\cap\lambda=\varnothing\}
=[z^N]\,\frac{\prod_{j\in S}(1-z^j)}{\prod_{h\ge1}(1-z^h)}
=\sum_{T\subseteq S}(-1)^{|T|}\,p\left(N-\sum_{t\in T}t\right),
\]
where \(p(u)=0\) for \(u<0\). It passes 754 exact integer comparisons for single and overlapping runs of lengths 2 and 3 and their accumulated counts. Separate numerical checks for fixed lengths 2, 3, 4 verify decreasing Boltzmann mean error and overlapping-pair mass as the model parameter increases. These finite checks test definitions and algebra only; they do not certify the infinite theorem, whose proof rests on the cited total-variation theorem and the cluster estimates above. Run: `python3 verify.py` with the standard library.

## Relationship to prior work
Bhoria, Eyyunni and Maji [1, Definition 1] introduced the \(r\)-chain mex; their Theorem 2.6 gives the generating function of its **sum over partitions**, while their Problem 6 asks for an asymptotic formula for that sum. The later bijective paper of Bhoria, Eyyunni and Li [2, Theorems 1.5--1.7] develops exact enumeration. Neither inspected text gives the **point-process limit, the \(r\)-dependent scaling exponent, or the distributions of successive runs**. The classical case \(r=1\), including smallest-gap asymptotics, is treated in DeSalvo--Menz [3, Example 4.6]; their Theorem 4.14 supplies the general small-part comparison used here. The 2025 overpartition extension [4] has a different underlying sample space. The 2026 study [5] counts missing integers below the largest part rather than consecutive-run locations. The limiting process is obtained by combining a known approximation with a new explicit overlapping-run analysis; no novelty is claimed for the approximation theorem or standard Poisson factorial-moment criterion. The result is not, by itself, an asymptotic formula for the expected \(r\)-chain mex or for the sum in Problem 6.

## Limitations
Only fixed \(r\ge2\) is covered, and convergence of the distribution does **not** by itself justify convergence of expectations or other unbounded moments; no mean-asymptotic or resolution of Problem 6 is asserted. No rate of convergence, uniformity in growing \(r\), or statement about overpartitions is proved. General Poisson approximation theorems or an unindexed study of the same partition statistic could implicitly contain this specialization; independent priority has not been established.

## References
[1] S. C. Bhoria, P. Eyyunni, and B. Maji, *A New Generalization of the Minimal Excludant Arising from an Analogue of Franklin's Identity*, arXiv:2208.03658, initial version 2022-08-07, Definition 1, Theorem 2.6, Problem 6. https://arxiv.org/pdf/2208.03658

[2] S. C. Bhoria, P. Eyyunni, and R. Li, *On the Combinatorics of r-Chain Minimal and Maximal Excludants*, arXiv:2312.02620, initial version 2023-12-05, Theorems 1.5--1.7. https://arxiv.org/pdf/2312.02620

[3] S. DeSalvo and G. Menz, *A Robust Quantitative Local Central Limit Theorem with Applications to Enumerative Combinatorics and Random Combinatorial Structures*, arXiv:1610.07664, Theorems 4.13--4.14 and Example 4.6. https://arxiv.org/pdf/1610.07664

[4] T. Y. He, C. S. Huang, H. X. Li, and X. Zhang, *The r-Chain Minimal and Maximal Excludant Sizes of an Overpartition*, arXiv:2501.12864. https://arxiv.org/pdf/2501.12864

[5] S. C. Bhoria, P. Eyyunni, and S. Santra, *On the Number of Missing Integers in Partitions*, arXiv:2604.12557, 2026. https://arxiv.org/html/2604.12557
