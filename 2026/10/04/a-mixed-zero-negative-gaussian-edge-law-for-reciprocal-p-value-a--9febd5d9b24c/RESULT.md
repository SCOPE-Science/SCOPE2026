# A mixed zero–negative Gaussian edge law for reciprocal p-value aggregation
## Finding
Let \(Z=(Z_1,Z_2,Z_3)\) be a centered Gaussian vector with unit variances and positive-definite correlation matrix \(R\). Assume
\[
\rho_{12}=0,\qquad \rho_{13}<0,\qquad \rho_{23}<0.
\]
Set \(U_i=1-\Phi(Z_i)\), choose fixed weights \(w_i>0\) with \(w_1+w_2+w_3=1\), and define the reciprocal aggregate
\[
T=\sum_{i=1}^3 \frac{w_i}{U_i}.
\]
Then
\[
\Pr(T>t)=\frac1t+2w_1w_2\frac{\log t}{t^2}+O(t^{-2}),\qquad t\to\infty.
\]
Hence the unique exactly zero-correlated Gaussian pair is the unique source of the independence-critical logarithm. The two strictly negative pairs and the genuine three-coordinate interaction contribute only \(O(t^{-2})\).

Let \(q_R(\alpha)\) be the upper \(\alpha\)-quantile under this mixed zero-negative Gaussian law and let \(q_\Pi(\alpha)\) be the upper \(\alpha\)-quantile under full independence. Then
\[
q_R(\alpha)-q_\Pi(\alpha)=-2(w_1w_3+w_2w_3)\log(1/\alpha)+O(1),
\]
and
\[
\Pr\{T>q_\Pi(\alpha)\}=\alpha-2(w_1w_3+w_2w_3)\alpha^2\log(1/\alpha)+O(\alpha^2).
\]
Thus replacing two independent edges by strict negative Gaussian dependence removes exactly their logarithmic second-order inflation while leaving the independent edge \((1,2)\) intact.

## Assumptions and scope
The correlations are fixed as \(t\to\infty\), all three weights are strictly positive, and \(R\) is positive definite. The result concerns one-sided exact-uniform Gaussian \(p\)-values and reciprocal aggregation only. It does not cover correlations tending to zero with the threshold, positive correlations, two-sided \(p\)-values, or positive Half-Cauchy scores.

The primary classification is MSC2020 62G32, matching the motivating work on tail behavior and extreme-value calibration of \(p\)-value aggregates.

## Proof
Write \(X_i=w_i/U_i\). Each \(X_i\) has the exact scaled-Pareto tail
\[
\Pr(X_i>x)=\frac{w_i}x,\qquad x\ge w_i.
\]
For nonempty \(I\subseteq\{1,2,3\}\), let
\[
g_I(x_I)=\mathbf 1\!\left\{\sum_{i\in I}x_i>t\right\}
\]
and define the Möbius increment \(G_I=\sum_{J\subseteq I}(-1)^{|I|-|J|}g_J\), with \(g_\varnothing=0\). Exact inclusion-exclusion on the coordinate-face lattice gives
\[
\mathbf 1\{X_1+X_2+X_3>t\}=\sum_i G_{\{i\}}+\sum_{i<j}G_{\{i,j\}}+G_{\{1,2,3\}}.
\]
Taking expectations reduces the tail to one-coordinate, pair, and triple-face terms.

The singleton contribution is exact:
\[
\sum_i\Pr(X_i>t)=\frac{w_1+w_2+w_3}t=\frac1t.
\]

Because \(\rho_{12}=0\), \(U_1\) and \(U_2\) are independent. The exact two-Pareto convolution identity gives
\[
\mathbb E G_{\{1,2\}}=
\frac{w_1w_2}{t^2}\log\!\frac{(t-w_1)(t-w_2)}{w_1w_2}
=2w_1w_2\frac{\log t}{t^2}+O(t^{-2}).
\]

For a strictly negative Gaussian pair, say \((i,j)\), put \(a=w_i\), \(b=w_j\), \(X=a/U_i\), and \(Y=b/U_j\). The simultaneous exceedance \(\Pr(X>t,Y>t)\) is \(o(t^{-2})\): for every sufficiently small \(\varepsilon>0\), both Gaussian thresholds exceed \(\sqrt{2(1-\varepsilon)\log t}\), so the event forces \(Z_i+Z_j\) above twice that level; since \(\operatorname{Var}(Z_i+Z_j)=2(1+\rho_{ij})<2\), a Gaussian tail bound yields exponent strictly larger than two.

For the cooperative event \(X\le t\), \(Y\le t\), \(X+Y>t\), the strips \(t-b<X\le t\) and \(t-a<Y\le t\) each have probability \(ab t^{-2}+O(t^{-3})\). Outside those strips, split according as \(X\ge t/2\) or \(Y\ge t/2\). For the first part set \(s=t-X\). Conditional on \(U_i=a/(t-s)\),
\[
\Pr(Y>s\mid U_i=a/(t-s))
=\overline\Phi\!\left(\frac{z_{b/s}-\rho_{ij}z_{a/(t-s)}}{\sqrt{1-\rho_{ij}^2}}\right),
\]
where \(z_q=\Phi^{-1}(1-q)\). For fixed \(s\) this tends to zero. On \(s\ge2b\), Mills-ratio comparison gives an integrable envelope \(C(b/s)^p\) for some \(p>1\), while on \([b,2b]\) the bound \(1\) suffices. Dominated convergence therefore makes the core \(o(t^{-2})\). Hence
\[
\mathbb E G_{\{1,3\}}=O(t^{-2}),\qquad
\mathbb E G_{\{2,3\}}=O(t^{-2}).
\]
The same argument also yields an \(O(t^{-2})\) bound for probabilities that either negative-pair sum lies in a fixed-width shell around \(t\).

It remains to control \(G_{\{1,2,3\}}\). Choose \(u_0=1/2\) and first restrict to \(U_1,U_2,U_3\le u_0\). A positive-definite correlation matrix with nonpositive off-diagonal entries is a Stieltjes matrix, so \(R^{-1}\) is entrywise nonnegative and its diagonal entries are at least one. For \(z_i=\Phi^{-1}(1-U_i)\ge0\), the Gaussian copula density therefore satisfies
\[
c_R(U_1,U_2,U_3)
=\frac1{\sqrt{\det R}}\exp\!\left[-\frac12 z^\mathsf T(R^{-1}-I)z\right]
\le \frac1{\sqrt{\det R}}.
\]
After the reciprocal change of variables, the joint density is thus bounded by a constant times \(\prod_i x_i^{-2}\). The standard product-corner bound for the three-coordinate Möbius increment gives
\[
\int_{[u_0^{-1}/t,\infty)^3}|G_{\{1,2,3\}}(t y)|\prod_i y_i^{-2}\,dy=O(t),
\]
so this all-lower-corner region contributes \(O(t^{-2})\).

On the complementary region at least one \(U_k>u_0\), hence \(X_k\le 2w_k\). Adding or removing this bounded coordinate can change a threshold indicator only if either a singleton or the opposite pair sum lies in a fixed-width shell around \(t\). Singleton shell probabilities are \(O(t^{-2})\); the pair \((1,2)\) has an exact convolution density of order \(t^{-2}\) near \(t\), and the two negative pairs have the fixed-width shell bound from the preceding paragraph. Therefore the complement also contributes \(O(t^{-2})\), proving
\[
\mathbb E G_{\{1,2,3\}}=O(t^{-2}).
\]
Adding the four face levels proves the tail expansion.

For quantiles, a tail of the form
\[
\overline F(t)=t^{-1}+A(\log t)t^{-2}+O(t^{-2})
\]
implies by direct substitution
\[
q(\alpha)=\alpha^{-1}+A\log(1/\alpha)+O(1).
\]
Here \(A=2w_1w_2\). Under full independence the known coefficient is \(2(w_1w_2+w_1w_3+w_2w_3)\). Subtraction gives the quantile formula, and substituting the independent quantile into the mixed-Gaussian tail gives the stated size expansion.

## Verification
The proof uses exact marginal Pareto tails, an exact Möbius decomposition, the exact independent two-Pareto convolution, elementary Gaussian tail bounds, a dominated-convergence estimate for each negative pair, and an explicit lower-corner bound on the trivariate Gaussian copula density. No finite experiment is used as proof of an infinite asymptotic statement.

The bundled checker verifies the face-decomposition identity on a dense rational grid, the algebraic coefficient subtraction, and positive definiteness of a representative mixed correlation matrix. These checks are sanity tests only; the asymptotic proof is analytic.

## Relationship to prior work
Liu, arXiv:2609.29658v1, proves the independent reciprocal coefficient and develops a face-calculus framework. Its Appendix A.11 notes that for one-sided negative Gaussian correlation the comparable joint-extreme exponent exceeds two but explicitly says this does not identify the leading weighted-sum remainder. Open Problem A.12 asks for one-sided nonpositive Gaussian dependence and specifically identifies mixed zero and negative correlations as unresolved. The present result settles the minimal genuinely mixed trivariate reciprocal case with one zero edge and two negative edges.

Kortschak's 2012 Gaussian-copula second-order theorem covers regularly varying risks under conditions that, at Pareto index one, include fixed strictly negative correlations. Its Gaussian condition is strict and becomes \(\alpha>1\) at a zero correlation, so it does not cover the critical zero-correlation pair responsible for the logarithm here. Yang and Zhang's bivariate copula-sum theory explicitly states that negative tail orders beyond the near-independence range are not its focus and does not address the trivariate mixed face. Chen, Wang, Wang, and Zhu establish finite-level subuniformity under negative dependence but not this small-level second-order coefficient. Chakraborty, Guo, Shedden, and Stoev establish first-order universal calibration for the Pareto/harmonic-mean class rather than the mixed Gaussian second term.

## Limitations
The theorem is deliberately trivariate and assumes exactly one zero pair and two strictly negative pairs. It does not establish a general arbitrary-dimensional theorem, a correlation-to-zero transition law, or a positive-Half-Cauchy analogue. The comparison with older risk-aggregation literature substantially lowers but does not eliminate the possibility that an equivalent special-case expansion appears under different terminology.

## References
1. T. Liu, *Copula Geometry and Second-Order Calibration of Heavily Right Aggregation*, arXiv:2609.29658v1, first public 2026-08-30.
2. D. Kortschak, *Second order tail asymptotics for the sum of dependent, tail-independent regularly varying risks*, Extremes 15 (2012), 353–388, DOI 10.1007/s10687-011-0142-x.
3. F. Yang and Y. Zhang, *Asymptotics of Sum of Heavy-tailed Risks with Copulas*, Methodology and Computing in Applied Probability 25 (2023), article 88; arXiv:2411.09657.
4. Y. Chen, R. Wang, Y. Wang, and W. Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics 54 (2026), e70017, DOI 10.1002/cjs.70017.
5. P. Chakraborty, F. R. Guo, K. Shedden, and S. Stoev, *On the universal calibration of heavy-tailed combination tests*, arXiv:2509.12066.
