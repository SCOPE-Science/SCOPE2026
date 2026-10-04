# Exact saturation law for Gaussian residual permutation coefficient tests
## Finding
For every even integer \(n\ge 4\), one can choose a deterministic full-rank \(n\times(n-1)\) linear-regression design, including an intercept and one tested normalized column, such that the full-model residual permutation coefficient test in Toulis (arXiv:1908.04218, Eq. (17)) has an exact null rejection probability far above its nominal level even when the errors are iid Gaussian.

Let the test use \(m\ge1\) independent uniformly random observation permutations and nominal one-sided level \(\alpha\in(0,1)\). Define
\[
a_n=\sqrt{2/n},\qquad
h_n=\frac{n}{4(n-1)},\qquad
\vartheta_n=\frac{1}{\pi}\arctan(a_n),
\]
and
\[
k=\left\lceil(1-\alpha)(m+1)\right\rceil.
\]
If \(k>m\), the strict-inequality test cannot reject. If \(k\le m\), its exact null rejection probability is
\[
\Pr(\mathrm{reject})
=
\frac12-\vartheta_n
+
\vartheta_n
\left[
\Pr\!\left\{\operatorname{Bin}(m,1-h_n)\ge k\right\}
+
\Pr\!\left\{\operatorname{Bin}(m,h_n)\ge k\right\}
\right].
\]

For every fixed \(0<\alpha<1/4\),
\[
\lim_{m\to\infty}\Pr(\mathrm{reject})
=
\frac12-\frac1\pi\arctan\sqrt{2/n},
\]
and therefore
\[
\lim_{n\to\infty}\lim_{m\to\infty}\Pr(\mathrm{reject})=\frac12.
\]
At \(n=20\), \(m=1000\), and \(\alpha=0.05\), the exact size is
\[
0.40250888547893166.
\]

This is a saturation obstruction for the specific full-model observation-residual permutation procedure. It is not a statement about restricted-residual variants, Freedman--Lane tests, or the distinct projected residual-space permutation method of Wen, Wang, and Wang.

## Assumptions and scope
Take even \(n\ge4\). Let
\[
v_i=
\begin{cases}
n^{-1/2},&1\le i\le n/2,\\
-n^{-1/2},&n/2<i\le n,
\end{cases}
\qquad
q=\frac{e_1-e_2}{\sqrt2}.
\]
Then \(\|v\|=\|q\|=1\), \(v^\top q=0\), and \(v^\top\mathbf 1=0\).

Choose the design matrix \(X\) so that its column space is \(v^\perp\), its first column is the intercept \(\mathbf 1\), its tested column is \(q\), and its remaining \(n-3\) columns form an orthonormal completion inside \(\{\mathbf1,v,q\}^\perp\). Thus \(X\) has \(p=n-1\) columns and full column rank. Because the tested column is orthogonal to every other design column, the corresponding OLS coefficient statistic is \(q^\top y\).

Under the coefficient null, assume
\[
\varepsilon\sim N(0,I_n).
\]
The result uses ordinary full-model OLS residuals and independently sampled uniformly random permutation matrices, exactly as in the residual permutation construction in Eq. (17) of arXiv:1908.04218. The empirical critical value is the smallest value whose empirical cumulative proportion is at least \(1-\alpha\), matching the source definition.

## Proof
Since \(\operatorname{col}(X)=v^\perp\),
\[
I-P_X=vv^\top.
\]
Write
\[
U=q^\top\varepsilon,\qquad Z=v^\top\varepsilon.
\]
Orthogonality of \(q\) and \(v\), together with Gaussianity, gives independent \(U,Z\sim N(0,1)\). The observed coefficient statistic is
\[
T=U,
\]
while the fitted full-model residual vector is
\[
\widehat\varepsilon=Zv.
\]

Let \(P\) be a uniformly random permutation matrix. A randomized coefficient statistic is
\[
q^\top P\widehat\varepsilon
=
Z\,q^\top Pv.
\]
Because \(q=(e_1-e_2)/\sqrt2\) and \(v\) has exactly \(n/2\) positive and \(n/2\) negative coordinates,
\[
q^\top Pv\in\{-a_n,0,a_n\},
\qquad a_n=\sqrt{2/n}.
\]
The two nonzero values occur with equal probability
\[
h_n=\frac{n}{4(n-1)},
\]
and zero occurs with probability \(1-2h_n\). Conditional on \(Z\), every randomized statistic therefore has the three-point distribution
\[
-a_n|Z|,\quad 0,\quad a_n|Z|
\]
with probabilities \(h_n,1-2h_n,h_n\), respectively.

Now include \(T=U\) together with the \(m\) randomized values, as in Eq. (17). The empirical \(1-\alpha\) critical value is the \(k\)-th order statistic, where
\[
k=\left\lceil(1-\alpha)(m+1)\right\rceil.
\]
Because rejection is strict, \(U\) exceeds that order statistic exactly when at least \(k\) of the \(m\) randomized values are strictly below \(U\). If \(k>m\), this is impossible.

Assume \(k\le m\). Conditional on \(U,Z\), the number of randomized values below \(U\) is binomial. Its success probability is \(0\), \(h_n\), \(1-h_n\), or \(1\) according as
\[
U\le-a_n|Z|,\quad
-a_n|Z|<U\le0,\quad
0<U\le a_n|Z|,\quad
U>a_n|Z|.
\]
The rotational symmetry of the independent standard-normal pair \((U,Z)\) gives
\[
\Pr\{U>a_n|Z|\}
=
\frac12-\frac1\pi\arctan(a_n),
\]
and each of the two middle wedges has probability
\[
\frac1\pi\arctan(a_n).
\]
Integrating the appropriate binomial tail over these four wedges gives the displayed exact formula.

For fixed \(\alpha<1/4\), one has \(\alpha<h_n\) for every \(n\ge4\). Hence
\[
1-\alpha>1-h_n>h_n.
\]
By the law of large numbers, both binomial-tail terms in the exact formula vanish as \(m\to\infty\). This proves the fixed-\(n\) limit. Finally, \(\arctan\sqrt{2/n}\to0\), so the limiting size tends to \(1/2\).

## Verification
The accompanying `verify.py` checks the permutation multiplicities exactly for \(n=6\), verifies the finite-\(m\) formula against exhaustive enumeration of the three-point randomization outcomes in a small case, and evaluates the \(n=20\), \(m=1000\), \(\alpha=0.05\) value using direct binomial-tail summation. It also checks the asymptotic trend numerically at several \(n\).

Run:

`python3 verify.py`

The expected first line is `VERIFY_OK`.

## Relationship to prior work
Toulis, arXiv:1908.04218, defines the full-model residual randomization test by comparing an observed OLS coefficient statistic with the same coefficient functional applied to randomly transformed full-model residuals. For observation permutations, Theorem 4 gives a sufficient exchangeability regime based on a residual-proxy error ratio and notes that \(p/n=o(1)\) suffices; the paper's simulations study dimensions up to order \(n^{1/2}\). The source does not state the rank-one saturation construction, the three-point permutation law, or the exact finite-\(m\) null-size formula above.

Wen, Wang, and Wang, arXiv:2211.16182, later study coefficient testing when the covariate dimension is a constant fraction of the sample size. Their numerical appendix includes the Toulis residual-randomization procedure and reports substantial over-rejection in several proportional-dimensional settings, including Gaussian settings. Their proposed RPT is different: it projects residual information using spaces determined by original and permuted designs and proves finite-sample validity in a \(p<n/2\) regime. The paper also analyzes a separate “naive RPT” that permutes coordinates after a residual-space basis transformation. Neither inspected formulation yields the exact saturation law above.

Classical residual-permutation and residual-bootstrap work motivates the broader resampling setting, but those procedures use differing residual constructions and test statistics. The claim here is only for the explicitly defined full-model residual permutation coefficient test.

## Limitations
The construction is deliberately extreme: the regression has \(p=n-1\), so the full-model residual space is one-dimensional. It demonstrates a sharp boundary failure and does not imply similar inflation for every near-saturated design. The formula is for the unstudentized one-sided coefficient statistic and the source's empirical-quantile convention. Other statistics, restricted residuals, or other permutation schemes require separate analysis.

The exact Gaussian calculation does not establish a minimax worst-case size over all saturated designs. It supplies an explicit family whose size tends to \(1/2\), which is enough to show that the low-dimensional validity condition cannot in general be extrapolated to saturation.

## References
1. Panos Toulis, *Asymptotic Validity and Finite-Sample Properties of Approximate Randomization Tests*, arXiv:1908.04218. First public version: 2019-08-12. Later published in *Biometrika*, DOI 10.1093/biomet/asaf085.
2. Kaiyue Wen, Tengyao Wang, and Yuhao Wang, *Residual permutation test for regression coefficient testing*, arXiv:2211.16182. First public version: 2022-11-29.
3. David A. Freedman, *Bootstrapping regression models*, *Annals of Statistics* 9 (1981), 1218--1228.
