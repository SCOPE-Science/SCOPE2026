# Ultra-log-concavity of Poisson maxima characterizes homogeneous intensities

## Finding

**Theorem (rigidity and asymptotic curvature).** Let \(n\ge2\), let \(\lambda_1,\ldots,\lambda_n>0\), and let the variables \(X_i\sim\operatorname{Poisson}(\lambda_i)\) be independent. Define \(M=\max_{1\le i\le n}X_i\) and \(f_k=\Pr(M=k)\) for integers \(k\ge0\). Then the mass function of \(M\) is ultra-log-concave, meaning
\[
k f_k^2\ge(k+1)f_{k-1}f_{k+1}\qquad\text{for every integer }k\ge1,
\]
**if and only if** all the intensities are equal.

Indeed, if the intensities are unequal, write \(b=\max_i\lambda_i\), let \(m\) be the number of intensities equal to \(b\), let \(a<b\) be the second-largest *distinct* intensity, and let \(s\) be its multiplicity. Put \(q_b(k)=e^{-b}b^k/k!\). Then
\[
\lim_{k\to\infty}
\frac{k f_k^2-(k+1)f_{k-1}f_{k+1}}
{k q_b(k)^2(a/b)^k}
=-m s e^{b-a}\frac{(b-a)^2}{ab}<0.
\]
Consequently the ultra-log-concavity inequality is strictly reversed for **every sufficiently large integer** \(k\). The limit describes the first nonconstant curvature scale, not merely a single counterexample.

## Assumptions and scope

All intensities are fixed and strictly positive; \(n\) is finite and at least two. Independence is essential to the product formula. For any \(t>0\), write \(p_t(k)=e^{-t}t^k/k!\) and \(F_t(k)=\sum_{j=0}^k p_t(j)\) for \(k\ge0\), with \(F_t(-1)=0\). All probabilities \(f_k\) are positive. The conclusion concerns the order-two *ultra*-log-concavity comparison with the Poisson mass, not ordinary log-concavity or dispersion.

## Proof

**1. Equal intensities.** Suppose each intensity is \(b>0\) and abbreviate \(F_k=F_b(k)\) and \(p_k=p_b(k)\). Since \(F_k-F_{k-1}=p_k\), the difference of powers gives
\[
f_k=F_k^n-F_{k-1}^n=p_k H_k,
\qquad H_k=\sum_{j=0}^{n-1}F_k^j F_{k-1}^{n-1-j}.
\]
The Poisson cumulative distribution sequence is log-concave. To see this directly, for integers \(k\ge1\),
\[
\frac{F_{k-1}}{p_k}=
\sum_{j=1}^{k}\frac{k(k-1)\cdots(k-j+1)}{b^j}.
\]
Each fixed summand increases with \(k\) while a new positive summand appears, so this ratio increases strictly. Thus \(F_k/F_{k-1}=1+p_k/F_{k-1}\) is decreasing, proving \(F_k^2\ge F_{k-1}F_{k+1}\). The convention \(F_{-1}=0\) handles the boundary.

Put \(U_{j,k}=F_k^j F_{k-1}^{n-1-j}\) for \(0\le j<n\). For every such \(j,\ell\) and integer \(k\ge1\),
\[
U_{j,k}U_{\ell,k}\ge U_{j,k-1}U_{\ell,k+1}.
\]
For \(k\ge2\) this follows from decreasing consecutive logarithmic increments \(d_t=\log(F_t/F_{t-1})\): the logarithm of the left-to-right ratio is nonnegative because the left increment sum is \(j d_k+(n-1-j)d_{k-1}\ge(n-1)d_k\) and the right increment sum is \(\ell d_{k+1}+(n-1-\ell)d_k\le(n-1)d_k\). For \(k=1\), the same argument uses \(F_{-1}=0\) (the right product is zero except when \(j=n-1\), in which case \(d_2\le d_1\) suffices).

Summing over \(j,\ell\) shows \(H_k^2\ge H_{k-1}H_{k+1}\). Finally, the Poisson identity \((k+1)p_{k-1}p_{k+1}=k p_k^2\) gives
\[
k f_k^2-(k+1)f_{k-1}f_{k+1}
=k p_k^2(H_k^2-H_{k-1}H_{k+1})\ge0.
\]
Thus every homogeneous maximum is ultra-log-concave.

**2. Unequal intensities.** By telescoping the product of CDFs,
\[
f_k=\sum_{i=1}^n p_{\lambda_i}(k)
\left(\prod_{j<i}F_{\lambda_j}(k)\right)
\left(\prod_{j>i}F_{\lambda_j}(k-1)\right).
\]
All these CDF factors lie in \([0,1]\). Their deviation from one is at most \(\Pr(\operatorname{Poisson}(b)\ge k)\) for the \(k-1\) argument, hence \(O(b^k/k!)\) as \(k\to\infty\); this last bound follows from the Poisson tail ratio \(b/(k+1)\to0\). Therefore, after division by the positive \(p_b(k)\),
\[
h_k:=\frac{f_k}{p_b(k)}
=\sum_{i=1}^n e^{b-\lambda_i}
\left(\frac{\lambda_i}{b}\right)^k
+O\left(\frac{b^k}{k!}\right).
\]
Let \(r=a/b\in(0,1)\) and \(\gamma=s e^{b-a}>0\). Finite summation and the factorial bound imply
\[
h_k=m+\gamma r^k+o(r^k).
\]
The expansion also holds when the index is shifted by one. Consequently
\[
\frac{h_k^2-h_{k-1}h_{k+1}}{r^k}
\longrightarrow m\gamma(2-r-r^{-1})
=-m\gamma\frac{(1-r)^2}{r}<0.
\]
Using the same Poisson identity as above,
\[
k f_k^2-(k+1)f_{k-1}f_{k+1}
=k p_b(k)^2(h_k^2-h_{k-1}h_{k+1}).
\]
Since \((1-r)^2/r=(b-a)^2/(ab)\), the displayed limit in the theorem follows. Its strict negative sign proves the eventual reversed inequality and completes the classification.

## Verification

The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. From the finite sums \(G_k=\prod_i\sum_{j=0}^k\lambda_i^j/j!\), \(G_{-1}=0\), the scaled probability is \(G_k-G_{k-1}=e^{\sum_i\lambda_i}f_k\) for integer parameters. The script checks homogeneous nonnegative defects and determines the first negative defect in five heterogeneous examples, including \((\lambda_1,\lambda_2)=(1,2)\): the first failure occurs at \(k=4\), with the exactly scaled defect \(-17/360\). These are independently repeatable diagnostic calculations. They do **not** prove the infinite classification or asymptotic limit; the proof above supplies those arguments. Run `python3 verify.py` in the directory containing this file.

## Relationship to prior work

Badiella, del Castillo, and Puig (2023), *Ultra log-concavity of discrete order statistics*, Theorem 2, establishes preservation of ultra-log-concavity for independent **identically distributed** order statistics, which includes the homogeneous half of this theorem. Its theorem does not cover unequal parent intensities, and it gives no necessity or heterogeneity-sensitive negative curvature asymptotic. The proof above reconstructs that half directly for Poisson maxima.

Chowdhury, Kundu, and Mishra (2021), *Comparisons of Order Statistics from Some Heterogeneous Discrete Distributions*, specifically studies Poisson extrema with unequal parameters. Its principal comparisons use usual stochastic ordering and majorization, not ultra-log-concavity of a single maximum or the stated necessary-and-sufficient classification. Yu (2009), *Stochastic Ordering of Exponential Family Distributions and Their Mixtures*, develops relative log-concavity to establish distributional order comparisons and studies genuine mixtures, not this maximum's pmf curvature. The explicit Poisson-telescoping argument is not a corollary of those cited comparisons.

## Limitations

The theorem assumes independent Poisson variables, a finite number of coordinates, and strictly positive fixed intensities. It makes no claim about ordinary log-concavity of heterogeneous maxima, their dispersion, the precise first violating index, or families of rates that vary with \(k\) or the sample size. The asymptotic provides eventual strict reversal but no universal finite cutoff. A literature comparison and self-review have been performed; independent priority confirmation and independent proof audit have not.

## References

1. L. Badiella, J. del Castillo, P. Puig (2023). *Ultra log-concavity of discrete order statistics*. Statistics & Probability Letters **201**, 109900. DOI: 10.1016/j.spl.2023.109900. First online 26 June 2023. Open full text: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf.
2. S. Chowdhury, A. Kundu, A. Mishra (2021). *Comparisons of Order Statistics from Some Heterogeneous Discrete Distributions*. arXiv:2103.00763v1. https://arxiv.org/abs/2103.00763.
3. Y. Yu (2009). *Stochastic Ordering of Exponential Family Distributions and Their Mixtures*. Journal of Applied Probability **46**, 244–254. DOI: 10.1239/jap/1238592127. https://arxiv.org/abs/0909.4570.
4. Y. Yu (2010). *Relative log-concavity and a pair of triangle inequalities*. Bernoulli **16**(2), 459–470. arXiv:1010.2043.
