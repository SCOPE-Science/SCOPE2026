# An exact sample-budget staircase for joint-leverage Gram approximation at stable rank one

## Finding

For every integer \(d\ge2\), form a full-column-rank matrix \(A_d\in\mathbb R^{d^2\times d}\) with rows indexed by \((j,k)\in\{1,\ldots,d\}^2\):
\[
(A_d)_{(j,k),:}=\frac{s_j}{\sqrt d}e_j^{\mathsf T},\qquad s_1=d,\quad s_2=\cdots=s_d=1.
\]
Every row is nonzero and has exactly the same leverage score \(1/d\). Moreover \(\|A_d\|_F^2/\|A_d\|_2^2=1+(d-1)/d^2\to1\). Let \(Y_{d,r}\) be the importance-rescaled product estimator from \(r\in\{1,\ldots,d^2-1\}\) independent *exact joint-leverage* row samples for the pair \((A_d,A_d)\). For \((d-1)/d^2\le\varepsilon<1\), its relative spectral-error success probability is exactly
\[
\begin{split}
 &\Pr\left\{\frac{\|Y_{d,r}-A_d^{\mathsf T}A_d\|_2}{\|A_d\|_2^2}\le\varepsilon\right\}\\
 &=\sum_{k=\lceil(r/d)(1-\varepsilon)\rceil}^{\lfloor(r/d)(1+\varepsilon)\rfloor}
 {r\choose k}\left(\frac1d\right)^k\left(1-\frac1d\right)^{r-k},
\end{split}
\]
where terms outside \(0\le k\le r\) are omitted and an empty sum is zero. In particular, the probability is strictly positive **if and only if** \(r/d\) belongs to one of the intervals
\[
\bigcup_{k\ge1}\left[\frac{k}{1+\varepsilon},\frac{k}{1-\varepsilon}\right].
\]
For \(\varepsilon<1/(2k+1)\), there is an *open, surely unsuccessful* sample-budget interval between the \(k\)-th and \((k+1)\)-st intervals. Thus adding samples can make an attainable relative spectral-error target unattainable at every realization.

As \(d\to\infty\) with \(r_d/d\to\alpha>0\), if neither \(\alpha(1-\varepsilon)\) nor \(\alpha(1+\varepsilon)\) is an integer, the success probability converges to the Poisson staircase
\[
 e^{-\alpha}\sum_{\substack{k\ge1\\|k/\alpha-1|\le\varepsilon}}\frac{\alpha^k}{k!}.
\]
The nonintegrality restriction prevents ambiguous endpoint roundings; no endpoint-uniform limit is asserted.

By contrast, for the *same matrix*, one squared-row-norm (product-norm) importance sample succeeds with the same relative spectral tolerance \(\varepsilon\) whenever \(\varepsilon\ge(d-1)/d^2\) and \(\varepsilon<1\), with exact probability
\[
\frac{d^2}{d^2+d-1}\longrightarrow1.
\]
Hence the joint-leverage sampler has a zero-success regime for every \(r<d/(1+\varepsilon)\), despite stable rank tending to one and a one-sample alternative having success probability tending to one.

## Assumptions and scope

All arithmetic is exact. Both samplers use independent draws *with replacement* and return the unbiased importance-rescaled sum of sampled row outer products. The first uses the exact joint-leverage distribution of Charalambides--Pilanci--Hero for identical inputs; the second samples row \(i\) proportionally to \(\|(A_d)_{i,:}\|_2^2\). These are different distributions and neither is claimed to dominate the other for all inputs. We assess relative *product spectral error*, not relative Frobenius error, singular-value estimates, or the stronger requirement of embedding every column-space direction. The displayed formulas require \(1\le r<d^2\) and \((d-1)/d^2\le\varepsilon<1\).

## Proof

**Geometry and probabilities.** The columns of \(A_d\) are orthogonal with respective norms \(s_j\). A reduced left orthonormal basis has \((j,k)\)-th row \(e_j^{\mathsf T}/\sqrt d\), independently of the singular values. Thus all \(d^2\) leverage scores equal \(1/d\); for identical inputs, the normalized joint score equals \(\pi_{jk}=1/d^2\). The exact Gram product is
\[
G_d=A_d^{\mathsf T}A_d=\operatorname{diag}(d^2,1,\ldots,1),\quad
\|G_d\|_2=d^2,\quad \|A_d\|_F^2=d^2+d-1.
\]

**Estimator and its limiting coordinate.** Group samples by first index \(j\), and let \(C_j\) count group \(j\). Then \((C_1,\ldots,C_d)\) is multinomial with \(r\) trials and equal group probabilities \(1/d\). Since sampling any row in group \(j\) contributes the rescaled outer product \(d s_j^2 e_je_j^{\mathsf T}/r\),
\[
Y_{d,r}=\operatorname{diag}\left(\frac{d^3C_1}{r},\frac{dC_2}{r},\ldots,\frac{dC_d}{r}\right).
\]
Therefore the exact normalized spectral error is
\[
E_{d,r}=\max\left\{\left|\frac{dC_1}{r}-1\right|,
\max_{2\le j\le d}\frac1{d^2}\left|\frac{dC_j}{r}-1\right|\right\}.
\]
Because \(0\le C_j\le r\) and \(d\ge2\), the second term is always at most \((d-1)/d^2\). Under the stated error tolerance, success is **equivalent** to \((r/d)(1-\varepsilon)\le C_1\le(r/d)(1+\varepsilon)\). As \(C_1\sim\operatorname{Binomial}(r,1/d)\), summing its point probabilities gives the first displayed formula exactly.

**Sample-budget classification.** Since \(\varepsilon<1\), zero cannot lie in the admissible count interval. Every count \(k\ge1\) has positive binomial mass whenever it is permitted; the inequalities for that count are equivalent to \(k/(1+\varepsilon)\le r/d\le k/(1-\varepsilon)\). Conversely no other count can succeed. All candidate counts meet \(k\le r\) because \(d\ge2>1+\varepsilon\). Consecutive intervals fail to meet precisely when \(k/(1-\varepsilon)<(k+1)/(1+\varepsilon)\), equivalently \((2k+1)\varepsilon<1\).

For instance, with \(\varepsilon=1/4\) and any \(d\ge3\) divisible by five, at \(r=d\) success requires \(C_1=1\) and has probability \((1-1/d)^{d-1}\). At the **larger** budget \(r=7d/5\), success is impossible since the permitted interval for \(C_1\) is \([21/20,7/4]\), which has no integer; at \(r=2d\) success again has positive probability (it requires \(C_1=2\)). This is a strict reentrant loss, not merely an asymptotic approximation.

**Poisson limit.** Under \(r_d/d\to\alpha\), the binomial generating function \((1+(z-1)/d)^{r_d}\) tends to \(e^{\alpha(z-1)}\). Away from integer boundaries, the finite set of accepted counts is eventually constant, so the binomial success probability converges to the stated Poisson sum. At boundaries the accepted count set may change with how \(r_d/d\) approaches \(\alpha\), and is intentionally excluded.

**Norm-product sampler.** A row in group \(j\) has squared norm \(s_j^2/d\). The group probability under squared-row-norm sampling is \(s_j^2/(d^2+d-1)\). One sample from group \(j\) therefore yields \((d^2+d-1)e_je_j^{\mathsf T}\). If \(j=1\), its normalized spectral error is \((d-1)/d^2\); if \(j\ge2\), it is at least \(1\) because the true leading \(d^2\) entry is absent. Under \((d-1)/d^2\le\varepsilon<1\), success occurs if and only if the first group is drawn, with probability \(d^2/(d^2+d-1)\). This completes every assertion.

## Verification

The standalone `verify.py` reproduces the leverage distribution and stable rank, enumerates small multinomial count vectors with exact rational arithmetic, compares the exact spectral-error event with the binomial event, verifies admissible and forbidden sample intervals, and checks the norm-sampling one-draw output. Run it using `python verify.py`. Its recorded execution passed **9,371 exact-arithmetic assertions**. Finite enumeration verifies examples and implementation; it does not substitute for the preceding proof for arbitrary \(d\).

## Relationship to prior work

Charalambides, Pilanci and Hero (arXiv:2610.29466v1, §2.2 Algorithm 1 and Remark 6) define joint-leverage sampling and explicitly identify its identical-input case with ordinary leverage sampling. Their Theorem 11 bounds a stronger full-column-space embedding at a substantially larger sufficient sample budget, whereas the present theorem gives exact finite-budget *relative Gram-product spectral-error* probabilities on a highly anisotropic all-nonzero-row family. Their §2.1 records the classical squared-row-norm alternative, which is used here as a comparator, not introduced as a new algorithm.

Cohen, Nelson and Woodruff (arXiv:1507.02268, Theorem 1 and §4) provide stable-rank spectral approximate multiplication guarantees for suitable sketch distributions and row selection. Those existence and upper-bound theorems do not give this exact probability staircase for a prescribed leverage sampler and do not imply the one-sample comparator formula. Drineas, Kannan and Mahoney (2006) establish classical importance-sampling matrix multiplication; neither unbiasedness nor product-norm sampling is claimed new. The new result is the combined sharp arithmetic feasibility law, the reentrant zero-probability intervals, and the stable-rank-one separation on this explicit family.

## Limitations

The effect exploits large singular-value anisotropy despite equal leverage scores, and it assesses only the operator-norm error normalized by the largest Gram singular value. It does **not** assert failure of full-rank subspace embedding guarantees, uniformly near-isometric approximation, or worst-case optimality of one-sample norm sampling. The reentrant intervals concern success of finite with-replacement importance-rescaled draws and are compatible with improved large-budget concentration. Exact first-publication priority for this particular example is not conclusively established by finite literature searches. Independent mathematical validation has not been performed.

## References

1. Neophytos Charalambides, Mert Pilanci and Alfred O. Hero III, *Approximate Matrix Multiplication through Joint Leverage Score Sampling*, arXiv:2610.29466v1 (first public October 21, 2026), §§2.1–2.4, especially Algorithm 1, Remark 6, Theorem 11. https://arxiv.org/abs/2610.29466
2. Michael B. Cohen, Jelani Nelson and David P. Woodruff, *Optimal Approximate Matrix Product in Terms of Stable Rank*, arXiv:1507.02268 (2015), Theorem 1 and §4. https://arxiv.org/abs/1507.02268
3. Petros Drineas, Ravi Kannan and Michael W. Mahoney, *Fast Monte Carlo Algorithms for Matrices I: Approximating Matrix Multiplication*, SIAM J. Comput. 36 (2006), 132–157, DOI:10.1137/S0097539704442684.
