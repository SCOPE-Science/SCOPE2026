# Branch-free cycle vertices have a mixed Gaussian quarter-power fluctuation law in random mappings

## Finding
Let \(f:[n]\to[n]\) be a uniformly selected mapping. A vertex is *cyclic* if it lies on a directed cycle. A cyclic vertex is *branch-free* if its total indegree equals one: its unique incoming edge is from its cycle predecessor, and no noncyclic tree edge ends there. Denote the number of cyclic vertices by \(R_n\) and the number of branch-free cyclic vertices by \(B_n\).

**Exact conditional distribution.** For every integer \(n\ge2\) and \(1\le r<n\), given \(R_n=r\), the variable \(B_n\) has the occupancy distribution of the number of empty boxes among \(r-1\) specified boxes following \(L=n-r-1\) independent uniform throws into \(n\) boxes. If \(r=n\), then \(B_n=n\) deterministically. Consequently, for \(0\le j\le r\) and \(r<n\),
\[
\mathbb E[(B_n)_j\mid R_n=r]=(r)_j\left(1-\frac jr\right)\left(1-\frac jn\right)^{n-r-1},
\]
with the \(j=r\) term interpreted as zero. In particular \(\mathbb E[B_n\mid R_n=r]=(r-1)(1-1/n)^{n-r-1}\).

**Finite-sample binomial approximation.** For \(1\le r<n\), let \(p_{n,r}=\exp(-(n-r-1)/n)\). Then
\[
d_{\mathrm{TV}}\big(\mathcal L(B_n\mid R_n=r),\mathrm{Bin}(r-1,p_{n,r})\big)\le\frac{r-1}{n}.
\]

**Two-scale limit.** Let \(X\) have density \(x\exp(-x^2/2)\), \(x>0\), and \(Z\sim N(0,1)\) independently. Then
\[
\left(\frac{R_n}{\sqrt n},\frac{B_n-e^{-1}R_n}{n^{1/4}}\right)\Longrightarrow\left(X,\sqrt{e^{-1}(1-e^{-1})X}\,Z\right).
\]
Thus \(B_n/\sqrt n\Rightarrow e^{-1}X\), while its residual fluctuations on the smaller quarter-power scale are a nondegenerate Gaussian mixture with random variance proportional to \(X\).

## Assumptions and scope
Every one of the \(n^n\) self-maps of the labeled set \([n]\) is equally likely. Directed loops are allowed and count as cycles of length one. All conditional finite formulas assume \(n\ge2\), \(1\le r<n\). For \(r=n\) all vertices form a permutation and are branch-free; this exceptional case is excluded from the occupancy identity and has asymptotically negligible probability. The falling factorial \((a)_j\) is \(a(a-1)\cdots(a-j+1)\), with \((a)_0=1\).

## Proof
Fix a set of \(r\) cyclic vertices and a cyclic permutation on that set. The remaining edges form a uniform labeled forest oriented toward those prescribed roots. Cayley's rooted-forest formula counts these forests as \(r n^{n-r-1}\). If \(j<r\) specified roots are required to receive no noncycle children, remove those \(j\) roots from the forest. The remaining forest has \(n-j\) vertices and \(r-j\) roots, hence \((r-j)(n-j)^{n-r-1}\) choices. For \(j=r\) and \(r<n\), no forest is possible. Thus the probability that the \(j\) specified roots are branch-free is
\[
\left(1-\frac jr\right)\left(1-\frac jn\right)^{n-r-1}.
\]
Choose one *compulsory occupied root* uniformly among the \(r\) roots and independently throw \(L=n-r-1\) balls uniformly into all \(n\) labels. For any specified \(j\) roots, the chance they avoid both the compulsory root and every ball equals the displayed probability. Since all joint zero-event probabilities of the root indicators agree, inclusion-exclusion shows equality of their joint laws. After conditioning on the compulsory root, the number of unhit roots is the number of empty boxes among the other \(r-1\) designated roots after \(L\) throws. This proves the exact law and factorial moments.

For the quantitative approximation, let \(m=r-1\), and let \(N\) be the total number of the \(L\) throws entering those \(m\) marked boxes. Then \(N\sim\mathrm{Bin}(L,m/n)\), and conditional on \(N\) the marked allocations are uniform multinomial. Replace \(N\) by \(N'\sim\mathrm{Pois}(Lm/n)\). The same conditional multinomial kernel then makes the marked occupancies independent Poisson variables, each of mean \(L/n\). The elementary Poisson-approximation bound
\[
d_{\mathrm{TV}}(\mathrm{Bin}(L,p),\mathrm{Pois}(Lp))\le p
\]
for independent Bernoulli indicators gives a joint total-variation error at most \(m/n\); applying the empty-box-count map cannot increase total variation. The independent Poisson emptiness indicators form \(\mathrm{Bin}(m,e^{-L/n})\), proving the finite bound.

Counting mappings by their cyclic roots gives
\[
\Pr(R_n=r)=\frac{r(n)_r}{n^{r+1}},\qquad 1\le r\le n.
\]
In particular, \(\Pr(R_n\ge r)=(n)_r/n^r\), so \(R_n/\sqrt n\) converges to a unit-scale Rayleigh variable \(X\) and is tight. For any deterministic sequence \(r_n/\sqrt n\to x>0\), we have \(m=r_n-1\to\infty\) and \(p_{n,r_n}\to e^{-1}\), while the preceding total-variation error is \(O(r_n/n)=o(1)\). The classical triangular binomial central limit theorem therefore gives
\[
\frac{B_n-(r_n-1)p_{n,r_n}}{n^{1/4}}\ \Big|\ (R_n=r_n)
\Longrightarrow N\big(0,x e^{-1}(1-e^{-1})\big).
\]
The centering difference \((r_n-1)p_{n,r_n}-e^{-1}r_n\) is \(O(1+r_n^2/n)\) for \(r_n=O(\sqrt n)\), hence negligible on the \(n^{1/4}\) scale. This conditional convergence holds uniformly for \(r/\sqrt n\) in compact subsets of \((0,\infty)\). Combining it with Rayleigh convergence by conditioning and tightness, then letting the compact lower and upper cutoffs tend to zero and infinity, yields the stated joint mixture limit with \(X,Z\) independent. The first-order corollary follows by dividing the residual term by \(n^{1/4}\).

## Verification
The standalone `verify.py` enumerates all maps exactly through six vertices, independently constructs the cyclic set and counts indegree-one cyclic vertices, checks the full conditional occupancy law and its joint avoidance factorial moments, and performs independent exact occupancy comparisons and finite-regime scale sanity checks. It passed 1,682 assertions. Finite checks are corroboration, not proofs of the infinite limits. The finite bound and limit follow analytically above.

## Relationship to prior work
Hansen and Jaworski (2010) give the uniform rooted-forest construction conditional on cyclic vertices; that construction is the enumeration input, not a claimed new theorem. Arney and Bender (1982) analyze origins and indegree counts of random mappings; their asymptotic tables do not state a conditional law for cyclic indegree-one vertices or the two-scale mixed limit. Mutafchiev and Finch (2023) analyze deepest-cycle lengths and motivate separate local structural statistics, without the branch-free cyclic-vertex statistic. The present result targets the *cycle roots*, unlike the noncyclic zero-indegree vertices appearing in other occupancy identities. The distinguishing contribution is the compulsory-root correction, a uniform conditional binomial approximation, and the Rayleigh-mixed quarter-power limit. The Poisson and binomial central limit statements used are standard tools rather than new contributions.

## Limitations
The mapping is uniform. The limit is weak convergence for \(n\to\infty\), not a Berry–Esseen or local limit theorem for the mixture, and no uniform normal approximation is claimed for sequences with bounded cyclic count. Literature priority remains best-knowledge; the possibility of an equivalent formulation in older enumeration/occupancy literature has not been eliminated. There is no independent mathematical audit.

## References
- L. Mutafchiev and S. Finch, *On the Deepest Cycle of a Random Mapping*, arXiv:2301.13829, first submitted 2023-01-31, MSC2020 60C05. https://arxiv.org/abs/2301.13829
- J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
- J. Arney and E. A. Bender, *Random Mappings with Constraints on Coalescence and Number of Origins*, Pacific Journal of Mathematics 103 (1982), 269–297. https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-s.pdf
- H.-K. Hwang and S. Janson, *Local Limit Theorems for Finite and Infinite Urn Models*, Annals of Probability 36 (2008), 992–1022, arXiv:math/0604397. https://arxiv.org/abs/math/0604397
