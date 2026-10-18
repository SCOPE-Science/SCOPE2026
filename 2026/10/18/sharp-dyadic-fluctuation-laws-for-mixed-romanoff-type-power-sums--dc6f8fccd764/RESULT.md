# Sharp dyadic fluctuation laws for mixed Romanoff-type power sums

## Finding
Fix an integer \(r\ge2\), and define the mixed restricted-power set
\[
\mathcal A_r=\{2^a+2^{b^r}:a,b\in\mathbb Z_{\ge1}\}.
\]
For each integer \(N\ge2\), write \(t=N-1\), \(s=\lfloor t^{1/r}\rfloor\), and \(F_r(N)=\#\{u\in\mathcal A_r:u\le2^N\}\). Then the exact dyadic count is
\[
\boxed{F_r(N)=ts-\binom{s}{2}.}
\]
Exactly \(\binom{s}{2}\) such values have two representations as \(2^a+2^{b^r}\); every other value has exactly one, and none has more than two. Define the normalized secondary remainder
\[
Z_r(N)=\frac{F_r(N)-(N-1)^{1+1/r}}{N-1}.
\]
As \(K\to\infty\), the empirical distribution of \(Z_r(N)\), for integer \(2\le N\le K+1\), converges to the uniform distribution on \([-3/2,-1/2]\) if \(r=2\), and to the uniform distribution on \([-1,0]\) if \(r\ge3\). More precisely, the Kolmogorov distance between these empirical and limiting distributions is \(O_r(K^{-1/r})\). Consequently, the error in the leading-term asymptotic has the sharp scale \(N\) along dyadic cutoffs: for no real constant \(c\) does \(F_r(N)=(N-1)^{1+1/r}+c(N-1)+o(N)\) hold.

## Assumptions and scope
The exponent \(r\) is a fixed ordinary integer at least two; \(a,b\) are strictly positive integers; the base is two; the cutoff is exactly \(2^N\) with integer \(N\ge2\). The representation count retains the roles of \(a\) and \(b\), including when their exponents coincide. The uniform-distribution statement samples integer cutoffs \(N\) equally, rather than weighting values of \(u\) or arbitrary real cutoffs. All asymptotic constants may depend on fixed \(r\).

## Proof
**1. Exact cutoff and collisions.** If \(2^a+2^{b^r}\le2^N\), then both exponents are at most \(N-1=t\), since both summands are positive. Conversely, any \(1\le a\le t\), \(1\le b\le s\) gives a sum at most \(2^N\): if the exponents differ, their sum is at most \(2^{N-1}+2^{N-2}<2^N\), and if they coincide, their sum is \(2^{a+1}\le2^N\). Thus there are \(ts\) labeled parameter pairs.

When \(a\ne b^r\), the integer has exactly two nonzero binary digits, at positions \(a\) and \(b^r\). Its unordered exponent pair is unique by binary expansion. Two labeled parameter pairs can represent the same integer precisely when both distinct positions are positive \(r\)-th powers: either one can be assigned to \(b^r\). Such values correspond bijectively to unordered pairs of distinct members of \(\{1^r,\ldots,s^r\}\) and number \(\binom{s}{2}\). When \(a=b^r\), the integer is the one-bit number \(2^{b^r+1}\); these are distinct as \(b\) varies and cannot coincide with a two-bit value. Therefore exactly \(\binom{s}{2}\) duplicated values exist, each with multiplicity two, giving \(F_r(N)=ts-\binom{s}{2}\).

**2. Reduction of the second-order error to a fractional power.** Let \(t=N-1\), \(s=\lfloor t^{1/r}\rfloor\), and \(\theta_t=\{t^{1/r}\}\in[0,1)\). Then \(s=t^{1/r}-\theta_t\) and the exact formula gives
\[
Z_r(N)=-\theta_t-\frac{s(s-1)}{2t}.
\]
For \(r=2\), \(s(s-1)/(2t)=1/2+O(t^{-1/2})\), so \(Z_2(N)=-\theta_t-1/2+O(t^{-1/2})\). For fixed \(r\ge3\), \(s(s-1)/(2t)=O_r(t^{-(r-2)/r})=O_r(t^{-1/r})\), hence \(Z_r(N)=-\theta_t+O_r(t^{-1/r})\). In both cases there is a fixed shift \(c_r\), equal to \(1/2\) for \(r=2\) and \(0\) for \(r\ge3\), such that
\[
Z_r(t+1)=-\theta_t-c_r+O_r(t^{-1/r}).
\]

**3. Uniform fractional-root distribution with a quantitative error.** For any fixed interval \([\alpha,\beta)\subseteq[0,1)\) and integer \(k\ge1\), the number of integers \(t\) in \([k^r,(k+1)^r)\) with \(\{t^{1/r}\}\in[\alpha,\beta)\) differs from \((k+\beta)^r-(k+\alpha)^r\) by at most two. The latter equals \((\beta-\alpha)((k+1)^r-k^r)+O_r(k^{r-2}+1)\), uniformly in \(\alpha,\beta\), by the binomial theorem. Summing complete blocks and bounding the final partial block proves, uniformly for intervals \(I\subseteq[0,1)\),
\[
\#\{1\le t\le K:\theta_t\in I\}=K|I|+O_r(K^{1-1/r}).
\]
Therefore \(\theta_t\) has uniform limiting distribution, with discrepancy \(O_r(K^{-1/r})\).

**4. Quantitative limiting law.** For a threshold \(z\), the indicators \(\mathbf1_{Z_r(t+1)\le z}\) and \(\mathbf1_{-\theta_t-c_r\le z}\) can differ only when \(\theta_t\) lies within \(O_r(t^{-1/r})\) of a fixed point of \([0,1]\), with the obvious one-sided interpretation at endpoints. Split \(1\le t\le K\) into dyadic index blocks \(T\le t<2T\). For each block, this exceptional set lies in at most two intervals of total length \(O_r(T^{-1/r})\). The preceding interval-discrepancy estimate, applied to two prefixes, bounds the number of exceptional indices in that block by \(O_r(T^{1-1/r})\). Summing the geometric series over dyadic blocks gives \(O_r(K^{1-1/r})\) exceptions. Combined with step 3, this proves uniform-in-\(z\) Kolmogorov error \(O_r(K^{-1/r})\) and the two asserted uniform laws.

The nondegenerate limiting distributions also rule out convergence of \(Z_r(N)\) to any constant. This proves that subtracting any fixed linear term cannot leave an \(o(N)\) remainder.

## Verification
A standalone exact-integer enumerator in `check_representations.py` reconstructs every labeled value \(2^a+2^{b^r}\) for \(2\le r\le7\) and \(2\le N\le50\). It checks cardinality, exact number of two-representation values, and absence of multiplicity above two in 294 parameter cases. The enumerator is supplementary evidence for the finite identities, not an infinite proof. The asymptotic law and rate follow from the analytic block estimates above, not from finite sampling.

To run the check from this package, execute `python3 check_representations.py` in the directory containing this file and the accompanying script. No external dependencies are required.

## Relationship to prior work
Xiao-Hui Yan, *On a conjecture on Romanoff type representations*, arXiv:2610.13691v1 (9 October 2026), considers general sets \(\{\sum_i2^{k_i^{r_i}}\}\) and proves a positive-density prime-plus-set representation theorem. Yan's Lemma 2.1 cites a general first-order counting asymptotic by Y.-G. Chen. Specializing it to the exponents \((1,r)\) gives only \(F_r(N)\sim N^{1+1/r}\). The present statement concerns the distinct subset invariant (exact dyadic cardinality and internal representation multiplicity) and its sharp second-order distribution, not prime-plus-set representation counts. The accessible full text of Yan's work does not supply the finite formula or limiting law. Ding and Li's arXiv:2606.06118 studies moments of prime-plus-set representation functions, not the stated dyadic secondary distribution. The publisher full text of Chen's 2026 article was not accessible during comparison; its cited first-order lemma does not logically imply the exact formula or limit law. Standard equidistribution of fractional powers supplies a proof ingredient but not the mixed-Romanoff arithmetic conclusion.

## Limitations
This is an unconditional dyadic-cutoff theorem for the fixed restricted family \((1,r)\). It does not establish an asymptotic for arbitrary real cutoffs, distributions of prime representations, or any uniform-in-\(r\) estimate. The fact that relevant full texts may contain an equivalent implicit consequence, particularly the full text of Chen's 2026 article, is an originality risk. The quantitative Kolmogorov upper bound is proved but is not claimed optimal. No independent external validation has been performed.

## References
1. Xiao-Hui Yan, *On a conjecture on Romanoff type representations*, arXiv:2610.13691v1, first posted 9 October 2026, https://arxiv.org/html/2610.13691v1 .
2. Y.-G. Chen, *On Integers of the Form \(p+2^{k_1^{r_1}}+\cdots+2^{k_t^{r_t}}\), II*, Frontiers of Mathematics (2026), DOI:10.1007/s11464-026-0057-0; cited Lemma 2.1 in reference 1. Full text not available in this comparison.
3. Yuchen Ding and Liangxun Li, *On a conjecture on Romanoff type sumsets*, arXiv:2606.06118v2 (2026), https://arxiv.org/abs/2606.06118 . Abstract and accessible synopsis examined; full text inaccessible.
