# Sharp second-moment inflation for expanding circle-map pair correlations

## Finding
Let \(b\geq2\) be any integer. Write \(\mathbb T=\mathbb R/\mathbb Z\), let \(U\) be Haar-uniform on \(\mathbb T\), and let \(T_b(x)=bx\pmod1\). For each fixed \(s>0\) and integer \(N>2s\), put
\[
R_N(s;U)=\frac1N\#\bigl\{(i,j):0\le i\ne j<N,\ \|T_b^iU-T_b^jU\|_{\mathbb T}\le s/N\bigr\}.
\]
Then
\[
\mathbb ER_N(s;U)=2s(1-N^{-1}),\qquad
\lim_{N\to\infty}N\operatorname{Var}(R_N(s;U))
=4s\frac{b+1}{b-1}.
\]
For each fixed \(b,s\) the variance limit admits the stronger error estimate
\[
N\operatorname{Var}(R_N(s;U))=4s\frac{b+1}{b-1}
+O_{b,s}\!\left(\frac{\log N}{N}\right).
\]
For comparison, if the \(N\) orbit points are replaced by \(N\) independent Haar-uniform circle points, with the same ordered-pair convention, then their normalized count has asymptotic variance \(4s/N\). Thus the expanding deterministic orbit has a sharp inflation factor \((b+1)/(b-1)>1\) even though its almost-sure pair-correlation limit is Poissonian.

## Assumptions and scope
All limits hold with \(b\) and \(s\) fixed; \(N\to\infty\) through all positive integers. Distance \(\|x\|_{\mathbb T}=\min_{k\in\mathbb Z}|x-k|\) is the circular distance, not the interval absolute distance. Variance is over the single uniform initial point \(U\), not over an independently resampled orbit. Pairs are ordered and exclude the diagonal. The result is an exact leading **variance**, not a central limit theorem nor a distributional fluctuation law. For finite \(N\), the formulas assume \(s/N<1/2\).

## Proof
**1. The exact two-frequency covariance kernel.** Fix \(0<r<1/2\) and let \(\chi_r(x)={\bf1}_{\{\|x\|_{\mathbb T}\le r\}}\). For positive integers \(m,n\), write \(g=\gcd(m,n)\), \(a=m/g\), \(c=n/g\), so \(\gcd(a,c)=1\). Since \(mU\) is Haar-uniform, \(\mathbb E\chi_r(mU)=2r\). The Fourier coefficients of \(\chi_r\) are \(\widehat\chi_r(0)=2r\) and \(\widehat\chi_r(k)=\sin(2\pi kr)/(\pi k)\) for nonzero integral \(k\). Integrating the product of the two Fourier expansions, only frequency pairs \((ct,-at)\) with nonzero integral \(t\) survive. The absolutely convergent resulting series and the Fourier expansion of the periodic Bernoulli polynomial give
\[
\begin{split}
C_r(a,c)&:=\operatorname{Cov}(\chi_r(mU),\chi_r(nU))\\
&=\frac{B_2(\{(a-c)r\})-B_2(\{(a+c)r\})}{ac},\\
B_2(t)&=t^2-t+\frac16\quad(0\le t<1).
\end{split}
\]
Here braces mean fractional part. Because the periodic extension of \(B_2\) is even and globally \(1\)-Lipschitz, the kernel satisfies the uniform bound
\[
|C_r(a,c)|\le \frac{2r}{\max(a,c)}.
\]
For every fixed integer \(h\geq0\), once \((b^h+1)r<1\), the polynomial expression simplifies exactly to
\[
C_r(1,b^h)=\frac{2r}{b^h}-4r^2.
\]

**2. Covariance decomposition by orbital lag.** Write \(M_{i,d}=b^i(b^d-1)\), where \(1\le d<N\) and \(0\le i<N-d\). Since \(T_b^{i+d}U-T_b^iU\equiv M_{i,d}U\pmod1\), the normalized pair count is twice the unordered sum:
\[
R_N(s;U)=\frac2N\sum_{d=1}^{N-1}\sum_{i=0}^{N-d-1}\chi_{s/N}(M_{i,d}U).
\]
Each summand has mean \(2s/N\), proving the expectation formula. Split the variance of the unordered sum into equal-lag contributions \(d=e\) and unequal-lag contributions \(d\ne e\).

**3. Unequal lags contribute only bounded unnormalized variance.** For \(d\ne e\), put \(h_0=\gcd(d,e)\), \(A=(b^d-1)/(b^{h_0}-1)\), \(E=(b^e-1)/(b^{h_0}-1)\), and \(M=\max(d,e)\). The elementary identity \(\gcd(b^d-1,b^e-1)=b^{h_0}-1\), combined with coprimality of \(b\) and \(b^d-1\), shows that after dividing \(M_{i,d}\) and \(M_{k,e}\) by their gcd the multipliers are \((A,b^{k-i}E)\) if \(i\le k\), and \((b^{i-k}A,E)\) if \(k<i\). Since \(h_0\) is a proper divisor of \(M\), it is at most \(M/2\). Therefore \(Q:=\max(A,E)\ge b^{M-h_0}\ge b^{M/2}\).

For fixed \((d,e)\) and fixed displacement \(h=|i-k|\), there are at most \(N\) starting-index pairs of either orientation. By the covariance bound, the total absolute contribution of all starting indices for that lag pair is at most a constant times
\[
Nr\sum_{h\ge0}\left(\frac1{\max(A,b^hE)}+\frac1{\max(b^hA,E)}\right).
\]
For \(0\le h\le M\), each summand is at most \(b^{-M/2}\); for \(h>M\), each is at most \(b^{-h}\). Hence the displayed series is at most \(2(M+1)b^{-M/2}+2b^{-M}/(b-1)\). There are at most \(2M\) choices of distinct positive \((d,e)\) with maximum \(M\), and their sum is finite uniformly in \(N\). Since \(Nr=s\), the full unequal-lag variance contribution is \(O_{b,s}(1)\).

**4. Equal lags give the sharp limit.** If \(d=e\), the two multipliers after gcd reduction are \(1\) and \(b^{|i-k|}\). Grouping the pairs by \(h=|i-k|\) yields the exact equal-lag contribution to the variance of the unordered sum:
\[
D_N=\frac{N(N-1)}2C_r(1,1)+
\sum_{h=1}^{N-2}(N-h-1)(N-h)C_r(1,b^h),\quad r=s/N.
\]
The bound \(|C_r(1,b^h)|\le2r b^{-h}\) justifies dominated convergence after multiplying by \(4/N\). For each fixed \(h\), the exact small-radius expression from Step 1 gives
\[
\lim_{N\to\infty}\frac4N D_N
=4s+8s\sum_{h\ge1}b^{-h}
=4s\frac{b+1}{b-1}.
\]
The unequal-lag term contributes \(O_{b,s}(N^{-1})\) after multiplication by \(4/N\), proving the limit. For the stated error, split the equal-lag sum at \(H=\lfloor\log_b(N/(2s))\rfloor\). On \(h\le H\), use the exact difference \(-4r^2\), whose contribution is \(O_{b,s}(\log N/N)\). On \(h>H\), use the geometric bound; its contribution is \(O_{b,s}(N^{-1})\). Replacing finite lag weights by their leading terms also costs \(O_{b,s}(N^{-1})\).

**5. The independent benchmark.** For \(N\) independent uniform circle points, each unordered collision event has probability \(2r\). Distinct unordered collision events are pairwise uncorrelated, including those sharing one endpoint, by conditioning on that endpoint and rotation invariance. Thus
\[
\operatorname{Var}(R_N^{\mathrm{iid}}(s))
=\frac4{N^2}\binom N2(2r)(1-2r)
=\frac{4s}{N}(1-N^{-1})(1-2s/N).
\]
Comparison with Step 4 gives the asserted strict inflation factor.

## Verification
The accompanying `CHECK.py` independently recomputes the covariance kernel by exact rational integration of intersecting preimage arcs, and independently recomputes entire finite-sample variances by partitioning the circle at every event boundary. It passed 153 rational-arithmetic checks, covering small multipliers, expansion factors \(2,3\), and sample sizes up to \(5\). Additional floating-point finite-sample evaluations produced \(N\operatorname{Var}(R_N(1))\approx 10.3605\) for \(b=2,N=50\) and \(11.44596\) for \(b=2,N=120\), approaching the proved limit \(12\). Finite checks are diagnostics only; Steps 1–5 prove the infinite statement.

## Relationship to prior work
Baker and Todd (2026) study pair correlations for typical interval-map orbits and obtain normalized almost-sure convergence using second-moment bounds; they explicitly cite the earlier Poissonian pair-correlation result for expanding integer circle maps. Rudnick and Zaharescu (1999/2002) prove Poissonian local correlations for lacunary integer sequences and give decay bounds for the variances of smooth correlation sums, but do not state the unsmoothed leading variance constant above. Rudnick and Technau (2020) and Chaubey and Yesha (2021/2022) obtain further lacunary correlation results and nonsharp variance bounds. These convergence results do not determine the leading variance for the sharp collision window, which is the focus here. The normalization here uses circular distance and variance over initial points.

## Limitations
No asymptotic normality or compound-Poisson law is established. The theorem does not extend without proof to nonintegral expansion factors, arbitrary lacunary sequences, irregular shrinking radii, or interval distance. The error constant can depend on the fixed expansion factor and collision radius. The literature comparison cannot rule out an unindexed older calculation of the same explicit variance constant.

## References
1. S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880, initial public submission 16 June 2026, particularly Introduction and Sections 3–4. https://arxiv.org/abs/2606.17880
2. Z. Rudnick and A. Zaharescu, *The distribution of spacings between fractional parts of lacunary sequences*, arXiv:math/9912103, especially Section 4 (variance upper bound). https://arxiv.org/abs/math/9912103
3. Z. Rudnick and N. Technau, *The metric theory of the pair correlation function of real-valued lacunary sequences*, arXiv:2001.08820, especially Section 2.2. https://arxiv.org/abs/2001.08820
4. S. Chaubey and N. Yesha, *The distribution of spacings of real-valued lacunary sequences modulo one*, arXiv:2108.00431, especially Section 3.1. https://arxiv.org/abs/2108.00431
