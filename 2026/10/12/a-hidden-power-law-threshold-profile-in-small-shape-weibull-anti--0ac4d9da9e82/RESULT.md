# A hidden power-law threshold profile in small-shape Weibull anti-concentration
## Finding
Fix \(y>0\). Let \(X_{\alpha,\lambda}\) have Weibull density \(f_{\alpha,\lambda}(x)=\alpha\lambda x^{\alpha-1}e^{-\lambda x^\alpha}\) on \(x>0\), and put
\[
T_\alpha(y)=\Pr\!\left\{\left|X_{\alpha,\lambda}-\mathbb E X_{\alpha,\lambda}\right|\ge y\sqrt{\operatorname{Var}(X_{\alpha,\lambda})}\right\}.
\]
The quantity \(T_\alpha(y)\) is independent of \(\lambda\), and as \(\alpha\downarrow0\),
\[
T_\alpha(y)\sim
\left(\frac{\alpha}{4\pi}\right)^{1/(2e)}y^{-2/e}
\exp\!\left(-\frac{2}{e\alpha}\right).
\]
The convergence is locally uniform for \(y\) in compact subsets of \((0,\infty)\). Consequently, for every fixed \(y_1,y_2>0\),
\[
\frac{T_\alpha(y_1)}{T_\alpha(y_2)}\longrightarrow
\left(\frac{y_2}{y_1}\right)^{2/e}.
\]
Thus the essential-exponential collapse of Weibull standardized anti-concentration has a nontrivial power-law threshold profile that is invisible at the leading logarithmic-rate scale.

Equivalently,
\[
-\log T_\alpha(y)=\frac{2}{e\alpha}+\frac{1}{2e}\log\frac{4\pi}{\alpha}+\frac{2}{e}\log y+o(1),
\]
locally uniformly for \(y\) bounded away from zero and infinity. The last display explains why all fixed thresholds have the same essential-exponential rate while their probability ratios retain the explicit power \(2/e\).

## Assumptions and scope
The shape parameter satisfies \(\alpha>0\), the Weibull rate parameter satisfies \(\lambda>0\), and \(y>0\) is fixed. Local uniformity means uniformity for \(y\in[a,b]\) for every fixed \(0<a<b<\infty\). Scaling by \(\lambda^{1/\alpha}\) removes \(\lambda\), so it suffices to take \(\lambda=1\). No statement is made for thresholds that themselves vanish or diverge with \(\alpha\).

## Proof
Set \(r=1/\alpha\),
\[
m_r=\Gamma(r+1),\qquad q_r=\Gamma(2r+1),\qquad s_r=\sqrt{q_r-m_r^2}.
\]
For unit rate, \(m_r\) and \(s_r\) are the mean and standard deviation. Stirling's expansion gives
\[
\delta_r:=\frac{m_r^2}{q_r}=\sqrt{\pi r}\,4^{-r}\left(1+O(r^{-1})\right).
\]
Hence \(m_r/s_r\to0\) exponentially. For every compact \([a,b]\subset(0,\infty)\), the lower endpoint \(m_r-y s_r\) is therefore negative for all sufficiently large \(r\), uniformly for \(y\in[a,b]\). The exact Weibull survival function then gives
\[
T_\alpha(y)=\exp\!\left(-(m_r+y s_r)^{1/r}\right).
\]

Now
\[
(m_r+y s_r)^{1/r}
=y^{1/r}q_r^{1/(2r)}(1-\delta_r)^{1/(2r)}
\left(1+\frac{m_r}{y s_r}\right)^{1/r}.
\]
The last two factors equal \(1+o(r^{-N})\) for every fixed \(N\), uniformly on \(y\in[a,b]\). The logarithmic Stirling expansion yields
\[
\frac{1}{2r}\log\Gamma(2r+1)
=\log(2r)-1+\frac{\log(4\pi r)}{4r}+\frac{1}{48r^2}+O(r^{-4}).
\]
Therefore
\[
(m_r+y s_r)^{1/r}
=\frac{2r}e+\frac{1}{2e}\log(4\pi r)+\frac{2}e\log y
+O\!\left(\frac{(\log r)^2}r\right),
\]
again locally uniformly in \(y\). Substituting \(r=1/\alpha\) gives an \(o(1)\) error in \(-\log T_\alpha(y)\). Exponentiating that additive \(o(1)\) proves the stated multiplicative equivalent. Dividing the equivalents at \(y_1\) and \(y_2\) gives the ratio law.

## Verification
The accompanying script `verify_weibull_profile.py` evaluates the exact probability in logarithmic arithmetic from the Gamma-function moment formulas and compares it with the displayed multiplicative asymptotic for several small shapes and three fixed thresholds. It also checks the predicted ratio law between two thresholds. The script returns `VERIFY_OK alpha_min=0.00625 max_terminal_log_error=0.0156609494975 ratio_rel_error=0.012273215192`. These finite computations are regression checks only; the proof above establishes the asymptotic statement.

## Relationship to prior work
Hu, Song and Tan prove that the Weibull anti-concentration function is identically zero. In Proposition 3.7 they record the exact Weibull mean and variance, show that the lower standardized endpoint eventually leaves the positive support, and upper-bound the remaining tail by replacing the true threshold with the mean. Their argument is sufficient for convergence to zero but does not identify a multiplicative equivalent, a threshold-dependent prefactor, local uniformity in the threshold, or a limiting ratio profile.

The present result retains the exact standardized threshold and uses a second-order logarithmic Stirling expansion. The resulting limit \(y^{-2/e}\) is a recovered threshold profile after the unrenormalized anti-concentration function has collapsed to zero. Targeted searches for this prefactor, the ratio law, the \(y^{-2/e}\) profile, and equivalent small-shape standardized-Weibull formulations found no covering published statement. Standard Gamma-function asymptotics supply the analytic tool but do not themselves state this probability theorem.

## Limitations
The theorem concerns the small-shape path \(\alpha\downarrow0\) and fixed standardized thresholds. It does not optimize a convergence rate over all Weibull shapes, and it does not assert uniformity when \(y\) approaches zero or infinity with \(\alpha\). An equivalent calculation could exist in older reliability or asymptotic-distribution literature under different terminology; the literature search did not eliminate that possibility.

## References
1. Z.-C. Hu, R. Song and Y. Tan, *On the anti-concentration functions of some familiar families of distributions*, arXiv:2401.09998, first posted 2024-01-18; *Mathematical Theory and Applications* 44 (2024), 1--15, DOI: 10.3969/j.issn.1006-8074.2024.01.001.
2. NIST Digital Library of Mathematical Functions, §5.11, especially the logarithmic Stirling expansion in Eq. 5.11.1.
