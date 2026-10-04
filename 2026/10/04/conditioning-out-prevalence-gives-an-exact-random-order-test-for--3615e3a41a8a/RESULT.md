# Conditioning out prevalence gives an exact random-order test for AP@k
## Finding
Consider independent relevance indicators \(I_1,\ldots,I_k\sim\operatorname{Bernoulli}(p)\) with fixed \(p\in(0,1)\). Put
\[
S_i=\sum_{j=1}^i I_j,
\qquad
A_k=\frac1k\sum_{i=1}^k\frac{S_i}i I_i,
\qquad
M_k=S_k,
\qquad
H_k=\sum_{i=1}^k\frac1i.
\]
The score \(A_k\) is the online AP@k random-ranking statistic studied by Manzhos, Ianevych and Melnyk.

Conditional on \(M_k=m\), every binary string with exactly \(m\) ones has the same probability. Hence \(A_k\mid M_k=m\) is independent of the unknown prevalence \(p\). For \(1\le m\le k-1\), the upper-tail conditional randomization probability
\[
\Pr\{A_k^*\ge A_k^{\rm obs}\mid M_k=m\}
\]
is therefore a finite-sample valid nuisance-free test of whether relevant items occur unusually early, conditional on the observed number of relevant items. The ordinary discrete tail probability is conservative; the usual randomized treatment of ties gives exact level.

The exact conditional mean is
\[
\eta_k(m)=\mathbb E(A_k\mid M_k=m)
=\frac{mH_k}{k^2}+
\frac{m(m-1)(k-H_k)}{k^2(k-1)}.
\]
Writing
\[
\mu_k(p)=p^2+p(1-p)\frac{H_k}k,
\]
the known-prevalence and prevalence-adjusted fluctuations have different Gaussian limits:
\[
\sqrt{k}\bigl(A_k-\mu_k(p)\bigr)
\Rightarrow N\bigl(0,5p^3(1-p)\bigr),
\]
while
\[
\sqrt{k}\bigl(A_k-\eta_k(M_k)\bigr)
\Rightarrow N\bigl(0,p^3(1-p)\bigr).
\]
Thus
\[
k\,\operatorname{Var}\!\bigl(\mathbb E[A_k\mid M_k]\bigr)
\longrightarrow 4p^3(1-p),
\qquad
k\,\mathbb E\!\left[\operatorname{Var}(A_k\mid M_k)\right]
\longrightarrow p^3(1-p).
\]
At first order, four fifths of the random-baseline variance is caused by total relevance-count fluctuation and one fifth by ordering fluctuation.

Finally, with \(\widehat p_k=M_k/k\),
\[
\frac{\sqrt{k}\,[A_k-\eta_k(M_k)]}
{\sqrt{\widehat p_k^3(1-\widehat p_k)}}
\Rightarrow N(0,1).
\]
This supplies a simple asymptotic calibration when exact conditional enumeration is inconvenient.

## Assumptions and scope
The result uses the homogeneous online null in which the \(k\) relevance indicators are iid Bernoulli with a fixed probability \(p\in(0,1)\). It tests ordering conditional on the total count \(M_k\); it intentionally removes prevalence information. An alternative that changes only the number of relevant items, without changing their conditional ordering, is therefore not targeted by this conditional test.

The finite-sample conditional statement holds for every integer \(k\ge2\). The Gaussian limits assume fixed interior \(p\); no claim is made for rare-event regimes in which \(p\) varies with \(k\).

## Proof
Given \(M_k=m\), each binary string with \(m\) ones has Bernoulli probability \(p^m(1-p)^{k-m}\). The conditional distribution is therefore uniform on the \(\binom{k}{m}\) such strings and contains no unknown parameter. This proves the exact randomization statement.

For the conditional mean, exchangeability gives
\[
\mathbb E(I_i\mid M_k=m)=\frac{m}{k},
\qquad
\mathbb E(I_jI_i\mid M_k=m)=\frac{m(m-1)}{k(k-1)}
\quad(j\ne i).
\]
Substitution into \(A_k\) gives the displayed formula for \(\eta_k(m)\). If \(r=m/k\), direct simplification also yields
\[
\eta_k(m)-\mu_k(r)
=\frac{m(k-m)(H_k-k)}{k^3(k-1)},
\]
which is uniformly \(O(k^{-1})\).

For the limit law, put \(X_i=I_i-p\). Exact expansion gives
\[
k\bigl(A_k-\mathbb EA_k\bigr)
=\sum_{i=1}^k c_{i,k}X_i
+\sum_{1\le j<i\le k}\frac{X_jX_i}i,
\]
where
\[
c_{i,k}=p+\frac{1-p}i+p(H_k-H_i).
\]
The quadratic remainder divided by \(k\) has variance
\[
\frac{p^2(1-p)^2}{k^2}
\sum_{i=2}^k\frac{i-1}{i^2}
=O\!\left(\frac{\log k}{k^2}\right),
\]
so it is negligible after multiplication by \(\sqrt{k}\). Moreover,
\[
\frac1k\sum_{i=1}^k c_{i,k}^2
\longrightarrow
p^2\int_0^1\bigl(1+\log(1/x)\bigr)^2\,dx
=5p^2.
\]
Because the \(X_i\) are bounded and \(\max_i|c_{i,k}|=O(\log k)=o(\sqrt{k})\), the triangular-array Lindeberg theorem gives the first Gaussian limit.

Now expand the plug-in centering \(\mu_k(\widehat p_k)\) around \(p\). Its derivative at \(p\) is
\[
d_k=2p+(1-2p)\frac{H_k}k,
\]
and the Taylor remainder is \(o_p(k^{-1/2})\). Hence
\[
\sqrt{k}\bigl(A_k-\mu_k(\widehat p_k)\bigr)
=\frac1{\sqrt{k}\sum_{i=1}^k(c_{i,k}-d_k)X_i+o_p(1).
\]
Since
\[
\frac1k\sum_{i=1}^k(c_{i,k}-d_k)^2
\longrightarrow
p^2\int_0^1\bigl(\log(1/x)-1\bigr)^2\,dx
=p^2,
\]
the same Lindeberg argument gives variance \(p^3(1-p)\). The uniform \(O(k^{-1})\) difference between \(\eta_k(M_k)\) and \(\mu_k(\widehat p_k)\) transfers the limit to exact conditional centering. Slutsky's theorem gives the studentized version. Combining this limit with the source's exact asymptotic variance \(5p^3(1-p)/k\) and the law of total variance yields the \(4+1\) variance split.

## Verification
A standalone checker exhaustively enumerates all binary strings for \(2\le k\le8\) to verify the conditional-mean formula, verifies the source mean and variance formulas for several prevalence values, checks the exact linear-plus-degenerate-quadratic decomposition, checks the identity between exact conditional and plug-in centering, and numerically confirms the coefficient limits \(5\) and \(1\). Running `python verify.py` returns `VERIFY_OK`.

## Relationship to prior work
Manzhos, Ianevych and Melnyk derive exact expectation and variance formulas for AP@k under both fixed-count random rankings and the iid Bernoulli online model. In the online model they explicitly assume \(p\) known and leave construction of a statistical test against random ranking for future work. Their two randomization models make the conditional reduction natural, but the inspected article does not state the nuisance-free conditional test, the Gaussian limits above, or the \(4+1\) variance decomposition.

Bestgen studies exact expected AP under a fixed number of relevant documents in a uniformly random ranking. This supports the fixed-count random-baseline connection, but does not supply the online Bernoulli conditional testing statement or the factor-five asymptotic decomposition.

Su, Yuan and Zhu derive asymptotic variance for a different AP object built from multinomial score strata in diagnostic classification. Their delta-method calculation does not specialize to the top-\(k\) iid-Bernoulli random-ranking statistic with the constants \(5\) and \(1\). Smucker, Allan and Carterette compare generic significance tests for differences in mean average precision across retrieval systems; that testing problem is different from an exact one-sample random-ranking null conditional on relevance count.

## Limitations
The exact conditional test answers an ordering question only after fixing the observed total number of relevant items. It should not be interpreted as a test for improved prevalence. The asymptotic normal calibration is not established for \(p\) approaching \(0\) or \(1\), heterogeneous item-specific relevance probabilities, dependence between relevance indicators, or user-to-user mixtures. Exact conditional tails may require combinatorial enumeration or dynamic programming for large \(k\); no computational-complexity claim is made here. A specialized information-retrieval paper not surfaced by the searches could contain an equivalent conditional calibration, so the originality claim is limited to the specific AP@k theorem and variance split stated above.

## References
1. T. Manzhos, T. Ianevych, O. Melnyk, “Average Precision at Cutoff k under Random Rankings: Expectation and Variance,” arXiv:2511.02571v1, 2025; DOI 10.15559/26-VMSTA298.
2. Y. Bestgen, “Exact Expected Average Precision of the Random Baseline for System Evaluation,” The Prague Bulletin of Mathematical Linguistics 103 (2015), 131–138; DOI 10.1515/pralin-2015-0007.
3. W. Su, Y. Yuan, M. Zhu, “Threshold-free Evaluation of Medical Tests for Classification and Prediction: Average Precision versus Area Under the ROC Curve,” arXiv:1310.5103, 2013.
4. M. D. Smucker, J. Allan, B. Carterette, “A comparison of statistical significance tests for information retrieval evaluation,” CIKM 2007, 623–632; DOI 10.1145/1321440.1321528.
