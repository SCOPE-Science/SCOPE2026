# Diameter-conditioned degree majorization and quadratic-degree fluctuations in random permutation trees

## Finding

For each integer \(n\ge 3\), choose uniformly from the \(2^{n-2}\) labeled permutation graphs on \(n\) vertices that are trees, and write \(D_n\) for diameter and \(Z_n=\sum_{v}\deg(v)^2\) for the first Zagreb (squared-degree) index. The **single structural finding** is a diameter--degree-heterogeneity dependence law, consisting of the following compatible exact ordering and fluctuation statements.

**All-convex conditional ordering.** For each \(2\le d<n-1\), there is a coupling of the sorted degree vectors \(\boldsymbol\delta_d\sim\operatorname{Law}(\operatorname{sort}(\deg T_n)\mid D_n=d)\) and \(\boldsymbol\delta_{d+1}\sim\operatorname{Law}(\operatorname{sort}(\deg T_n)\mid D_n=d+1)\) for which
\[
\boldsymbol\delta_d\succ\boldsymbol\delta_{d+1}\quad\text{almost surely, with unequal vectors.}
\]
Here \(\succ\) is strong majorization: equal total sums and all descending partial sums weakly larger. Thus, for **every** strictly convex real function \(\phi\) on \([1,n-1]\), the conditional statistic \(\sum_v\phi(\deg v)\) strictly decreases under a common coupling as \(d\) increases, and hence decreases in strict first-order stochastic order.

**Exact quadratic dependence.** For \(2\le d\le n-1\),
\[
\mathbb E[Z_n\mid D_n=d]=2(n-1)\left(1+\frac{n-2}{d}\right),
\qquad \mathbb E Z_n=6n-14+2^{4-n},
\]
and
\[
\operatorname{Cov}(D_n,Z_n)=10-2n-\frac{n+1}{2^{n-3}}.
\]
The covariance vanishes for \(n=3\) and is strictly negative for every \(n\ge4\). Its nonvanishing dependence is quantified further by
\[
\operatorname{Var}(Z_n)=24(n-2)-120+\frac{8(n-2)^2+24(n-2)+68}{2^{n-3}}-\frac{16}{4^{n-2}}.
\]

**Joint limit and persistent correlation.** With \(N=n-2\),
\[
\frac1{\sqrt N}\begin{pmatrix}D_n-\mathbb ED_n\\Z_n-\mathbb EZ_n\end{pmatrix}
\ \Longrightarrow\ \mathcal N_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},
\begin{pmatrix}1/4&-2\\-2&24\end{pmatrix}\right),
\qquad \lim_{n\to\infty}\operatorname{Corr}(D_n,Z_n)=-\sqrt{\frac23}.
\]

## Assumptions and scope

A permutation graph has vertices \(1,\ldots,n\), with an edge between two labels precisely when they occur as an inversion in the permutation. Uniformity is over all distinct labeled graphs that arise this way and are trees; the inversion-set map is injective. Diameter is measured in edges. The degree sequence is padded to length \(n\) and rearranged in nonincreasing order before majorization. The conditional ordering applies only to successive *feasible* diameters; the variance and covariance identities include \(n=3\), when both variables are deterministic. The displayed correlation limit concerns \(n\ge4\).

## Proof

**1. Encode tree degrees and diameter as runs.** Acan and Hitczenko's bijection, justified in their Lemmas 11--12 and Eq. (3.1), associates each permutation tree on \(n\) vertices with a binary word of length \(N=n-2\). If the maximal run lengths are the positive integers \(r_1,\ldots,r_b\) summing to \(N\), the tree has exactly \(b\) non-leaf vertices of degrees \(r_i+1\), with its other \(n-b\) vertices of degree one, and \(D_n=b+1\). Consequently
\[
Z_n=3n-4+S_N,\qquad S_N=\sum_{i=1}^b r_i^2.
\]
The binary word is uniform, so all \(N-1\) adjacency-change indicators are independent \(\mathrm{Bernoulli}(1/2)\). Given \(b\) runs, their \(b-1\) cut positions form a uniformly chosen \((b-1)\)-subset of the \(N-1\) gaps; equivalently \((r_1,\ldots,r_b)\) is a uniform positive composition of \(N\) with \(b\) parts. These are the only imported combinatorial facts.

**2. Construct an order-preserving conditional coupling.** Draw the cuts of a uniformly random \(b\)-part composition, then choose one of its \(N-b\) uncut gaps uniformly and add it. Every \(b\)-cut set can be obtained from exactly \(b\) different \((b-1)\)-cut sets, so the new cut set is uniform; it has the law conditional on diameter \(b+2\). If a part \(r=a+c\), with \(a,c\ge1\), is split, the tree degree list replaces \((r+1,1)\) by \((a+1,c+1)\). Their sums agree, and \((r+1,1)\) strictly majorizes \((a+1,c+1)\); every other degree is unchanged. Majorization is invariant under adjoining identical coordinates. Karamata's inequality consequently yields strict decrease of the sum of any strictly convex \(\phi\), simultaneously for all such functions under this coupling. This proves the conditional statement for each \(b=1,\ldots,N-1\).

**3. Obtain the exact conditional regression.** For a uniform positive \(b\)-part composition, a stars-and-bars second-factorial-moment calculation gives
\[
\mathbb E\sum_{i=1}^b r_i(r_i-1)=\frac{2N(N-b)}{b+1},\qquad
\mathbb ES_N=\frac{N(2N-b+1)}{b+1}.
\]
Substitute \(b=d-1\) and \(n=N+2\) into \(Z_n=3n-4+S_N\). The claimed conditional mean simplifies to \(2(n-1)(1+N/d)\), which is strictly decreasing in \(d\).

**4. Compute exact moments and covariance.** Write \(C_k\) for the independent fair cut indicator at gap \(k\), and \(B_{ij}=\prod_{k=i}^{j-1}(1-C_k)\). Counting ordered pairs within runs gives
\[
S_N=N+2\sum_{1\le i<j\le N}B_{ij},\qquad b=1+\sum_{k=1}^{N-1}C_k.
\]
Therefore \(\operatorname{Cov}(C_k,B_{ij})=-2^{-(j-i+1)}\) if \(i\le k<j\), otherwise zero. Summing the \(j-i\) cut positions inside each interval yields
\[
\operatorname{Cov}(D_n,Z_n)=-\sum_{\ell=1}^{N-1}\ell(N-\ell)2^{-\ell}
=6-2N-\frac{N+3}{2^{N-1}}.
\]
The mean follows from the same interval decomposition:
\[
\mathbb ES_N=N+2\sum_{\ell=1}^{N-1}(N-\ell)2^{-\ell}=3N-4+\frac4{2^N}.
\]
For the second moment, the ordinary generating function for compositions with marked quadratic part-weight is \(F(z,t)=(1-\sum_{r\ge1}z^r e^{tr^2})^{-1}\), interpreted formally coefficientwise in \(z\). Twice differentiating at \(t=0\) gives
\[
\partial_t^2F(z,0)=
\frac{z(1+11z+11z^2+z^3)}{(1-z)^3(1-2z)^2}
+\frac{2z^2(1+z)^2}{(1-z)^3(1-2z)^3}.
\]
Since there are \(2^{N-1}\) compositions for \(N\ge1\), extracting the coefficient of \(z^N\) and dividing by \(2^{N-1}\) yields
\[
\mathbb ES_N^2=9N^2-104+\frac{8N^2+36N+52}{2^{N-1}},
\]
which, after subtraction of \((\mathbb ES_N)^2\), is the variance stated above. The exact covariance is strictly negative for \(N\ge2\), already directly clear from the interval sum.

**5. Prove the two-dimensional limit.** Regard the runs as successive iid geometric lengths \(R_j\), with \(\mathbb P(R_j=r)=2^{-r}\) for \(r\ge1\). The last run is censored by the finite word; its length has a geometric tail uniformly in \(N\), so its effects on both the number of runs and the quadratic reward are \(o_{\mathbb P}(\sqrt N)\). The standard random-time-change/renewal-reward central limit argument applies to the iid centered rewards
\[
U_j=\left(1-\frac{R_j}{2},\ R_j^2-3R_j\right).
\]
With \(\mathbb ER_j=2\), \(\mathbb ER_j^2=6\), \(\mathbb ER_j^3=26\), and \(\mathbb ER_j^4=150\), one has
\[
\frac{\mathbb E(U_jU_j^{\mathsf T})}{\mathbb ER_j}=
\begin{pmatrix}1/4&-2\\-2&24\end{pmatrix}.
\]
The iid vector CLT, law of large numbers for the number of completed runs, and negligible censoring remainder prove the joint limit. Exact means differ from the corresponding linear centering by \(O(1)\). The exact moment formulas imply convergence of the component variances and covariance on scale \(N\), completing the correlation limit.

## Verification

The standalone `verify.py` constructs each permutation from its binary insertion word, independently builds the entire inversion graph, and computes diameters and squared-degree sums from graph edges. It exhausts all \(2^{n-2}\) words for \(3\le n\le12\), checking the run encoding, exact conditional means, exact mean/variance/covariance, and their finite-domain boundaries. It also checks **every** consecutive-cut insertion for \(3\le n\le10\) and each sorted degree partial-sum inequality. Execution: `python3 verify.py`. A recorded execution passed **14,234 exact assertions**. This finite enumeration is a reproducibility check, not a proof for all \(n\); the algebraic and probabilistic arguments above supply the infinite proof.

## Relationship to prior work

Acan and Hitczenko (2014 preprint; subsequently published 2016) establish the permutation-tree run encoding, the marginal diameter distribution, maximum-degree behavior, and joint asymptotic normality of any *fixed finite collection* of degree counts. Their result is the basis of Step 1 and is not presented as new here. The assertions assessed here are the entire conditional degree-sequence majorization, the exact diameter--Zagreb covariance and variance, and the nonzero limiting two-statistic correlation. The fixed-coordinate degree-count CLT alone does not justify the unbounded quadratic weighted sum. Bender and Canfield (2005) provide general composition asymptotic background rather than this permutation-tree dependence law. A related recorded result about uniform compositions establishes stochastic ordering of the *maximum part* by part count; this is a weaker projection of the all-convex ordering and is explicitly excluded from independent novelty claims.

## Limitations

Historical priority is not established conclusively by the literature comparisons. The exact claims concern uniformly sampled *permutation-graph trees*, not all Cayley trees, all random caterpillars, or arbitrary nonuniform binary words. Literature searches cannot rule out equivalent formulations in earlier composition or degree-index work. A relevant previous result proves a cut-insertion coupling and conditional maximum-part stochastic ordering; its complete accessible result was compared. Our all-degree-vector majorization follows by strengthening that basic coupling with a strict majorization inequality, so it is not claimed as a novel coupling mechanism. Historical precedence for the additional quadratic and joint-limit formulas is not completely resolved. The source's run encoding implies the complete finite combinatorial law in principle; this work isolates and proves specific dependence consequences rather than claiming a new representation of that law. The Gaussian limit applies to the stated pair, without a functional CLT or a rate of convergence.

## References

- H. Acan and P. Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958, publicly available 2014-06-16; subsequently *Discrete Mathematics* 339 (2016), 2871--2883. https://arxiv.org/abs/1406.3958
- E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, *Electronic Journal of Combinatorics* 12 (2005), R57. https://doi.org/10.37236/1954
- *Rigorous decorrelation of part count and maximum in uniform compositions*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31 (full result text inspected for overlap; its maximum-part ordering is acknowledged).
