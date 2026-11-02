# Sharp positivity and damping frontier for an oracle Bernoulli control-variate Gram sketch

## Finding

For the balanced four-row Parseval frame and independent Bernoulli sketch defined below, the population-optimal **entrywise** control-variate Gram estimator is positive definite for **every** sampling outcome if and only if
\[
1\le K< K_{\mathrm{crit}}(\eta)=1+\frac{12\eta}{3-2\eta}.
\]
It is positive semidefinite for every outcome if and only if \(K\le K_{\mathrm{crit}}(\eta)\). For every \(K>K_{\mathrm{crit}}(\eta)\), a fixed, positive-probability sample yields an indefinite corrected matrix even though the uncorrected sampled Gram matrix is positive definite on that same event. Moreover, the least nonnegative common diagonal shift ensuring positive semidefiniteness for every outcome is exactly
\[
\rho_*(K,\eta)=\max\left\{0,(K-1)\left(\frac{1}{4\eta}-\frac16\right)-1\right\}.
\]
The elementwise variance minimization simultaneously strictly reduces total Frobenius mean-squared error for every \(K\ge1\); hence mean-square improvement does not imply samplewise positive definiteness.

## Assumptions and scope

Let \(u_1=(1/\sqrt2,0)\), \(u_2=(0,1/\sqrt2)\), \(u_3=(1/2,1/2)\), and \(u_4=(1/2,-1/2)\) be the four rows of \(U\in\mathbb R^{4\times2}\). Then \(U^{\mathsf T}U=I_2\), and each row leverage score equals \(1/2\). Fix any \(K\ge1\) and \(0<\eta<1\). Let \(P_K=\operatorname{diag}(1,1,K,1)\) and let \(T=I_4\). Sample \(\gamma_1,\ldots,\gamma_4\) independently with \(\Pr(\gamma_i=1)=\eta\). Put \(G_i=u_i^{\mathsf T}u_i\) and
\[
Y_K=U^{\mathsf T}P_KU,\qquad
\widehat Y_K=\frac1\eta\sum_{i=1}^4\gamma_i(P_K)_{ii}G_i,\qquad
\widehat Y_T=\frac1\eta\sum_{i=1}^4\gamma_iG_i.
\]
Define the deterministic population-optimal elementwise coefficient matrix by
\[
B_{jk}=\frac{\operatorname{Cov}((\widehat Y_K)_{jk},(\widehat Y_T)_{jk})}
{\operatorname{Var}((\widehat Y_T)_{jk})},\qquad j,k\in\{1,2\}.
\]
Every denominator is strictly positive. Consider the unbiased corrected estimator
\[
\widetilde Y_K=\widehat Y_K-B\circ(\widehat Y_T-I_2),
\]
with \(\circ\) denoting Hadamard multiplication. Coefficients are fixed at their population values; they are not fitted from a finite collection of sketches. The claim concerns this forward sketch, not a fused or inverted estimator. The Bernoulli family includes the equal-leverage inclusion choices of the motivating scheme, whose nominal sample budget equals \(4\eta\).

## Proof

**Exact frame, target and oracle coefficients.** The four outer products are
\[
G_1=\frac12\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
G_2=\frac12\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
G_3=\frac14\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
G_4=\frac14\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Their sum is \(I_2\). Writing \(d=K-1\),
\[
Y_K=\begin{pmatrix}(K+3)/4&(K-1)/4\\(K-1)/4&(K+3)/4\end{pmatrix},
\quad
B=\begin{pmatrix}(K+5)/6&(K+1)/2\\(K+1)/2&(K+5)/6\end{pmatrix}.
\]
Indeed independent Bernoulli sampling gives
\[
\operatorname{Cov}((\widehat Y_K)_{jk},(\widehat Y_T)_{jk})
=\frac{1-\eta}{\eta}\sum_i (P_K)_{ii}(G_i)_{jk}^2,
\quad
\operatorname{Var}((\widehat Y_T)_{jk})
=\frac{1-\eta}{\eta}\sum_i (G_i)_{jk}^2.
\]
The target has eigenvalues \(1\) and \((K+1)/2\), and is positive definite for every allowed \(K\).

**Sharp all-outcome eigenvalue.** Direct substitution, without statistical approximation, gives
\[
\widetilde Y_K=I_2+dC(\gamma,\eta),\quad
C=\frac16I_2+\frac{1}{24\eta}
\begin{pmatrix}
-2\gamma_1+5\gamma_3-\gamma_4&3(\gamma_3+\gamma_4)\\
3(\gamma_3+\gamma_4)&-2\gamma_2+5\gamma_3-\gamma_4
\end{pmatrix}.
\]
Set \(\mu_\eta=1/6-1/(4\eta)\). For every binary outcome,
\[
24\eta(C-\mu_\eta I_2)=
\begin{pmatrix}4+5\gamma_3-\gamma_4&3(\gamma_3+\gamma_4)\\3(\gamma_3+\gamma_4)&4+5\gamma_3-\gamma_4\end{pmatrix}
+\operatorname{diag}(2(1-\gamma_1),2(1-\gamma_2)).
\]
The first summand has eigenvalues \(4+8\gamma_3+2\gamma_4\) and \(4+2\gamma_3-4\gamma_4\), both nonnegative for all binary \(\gamma_3,\gamma_4\); the second is diagonal positive semidefinite. Thus \(C\succeq\mu_\eta I_2\). Equality is attained at \(\gamma=(1,1,0,1)\), where \(C\) has eigenvalues \(1/6\) and \(\mu_\eta\), with the smaller eigenvalue in the \((1,-1)\) direction. Because \(d\ge0\),
\[
\min_{\gamma\in\{0,1\}^4}\lambda_{\min}(\widetilde Y_K)
=1+(K-1)\left(\frac16-\frac1{4\eta}\right).
\]
This quantity is strictly positive exactly below \(K_{\mathrm{crit}}(\eta)\), zero at the threshold, and negative above it. Adding \(\rho I_2\) changes each eigenvalue by precisely \(\rho\), yielding the stated sharp shift. At the extremal event the raw sketch includes \(G_1,G_2,G_4\) with positive coefficients, so its two-by-two Gram matrix is strictly positive definite. The extremal event occurs with probability \(\eta^3(1-\eta)>0\).

**Exact variance trade-off.** The variables are independent, so
\[
\mathbb E\|\widehat Y_K-Y_K\|_F^2
=\frac{1-\eta}{\eta}\sum_i (P_K)_{ii}^2\|G_i\|_F^2
=\frac{1-\eta}{\eta}\frac{K^2+3}{4}.
\]
Using the displayed optimal coefficients in the four scalar entrywise variance identities, summing diagonal and twice off-diagonal contributions gives
\[
\mathbb E\|\widetilde Y_K-Y_K\|_F^2
=\frac{1-\eta}{\eta}\frac{(K-1)^2}{6}.
\]
Both estimators are unbiased. Their MSE ratio is \(2(K-1)^2/[3(K^2+3)]<2/3\). In particular at \((\eta,K)=(1/2,5)\), the corrected mean-squared error is \(8/3\), versus \(7\) for the uncorrected estimator; nevertheless an event of probability \(1/16\) yields corrected minimum eigenvalue \(-1/3\). The necessary and sufficient common semidefinite shift is then \(1/3\). Finally, for any fixed \(c>4\), setting \(K=1+c\eta\) and letting \(\eta\downarrow0\) makes the target condition number tend to one and the corrected MSE tend to zero while retaining a positive-probability indefinite event for every sufficiently small \(\eta\).

## Verification

The independent, exact-rational enumeration in `verify_cv_frontier.py` reconstructs all four rank-one outer products and all sixteen Bernoulli outcomes without floating-point arithmetic. It checks the population covariance coefficients, the all-outcome Loewner bound, attainment on the specified event, unbiasedness, exact MSE identities and positivity thresholds for multiple rational choices including threshold equality. The theorem's universal quantifiers follow from the explicit matrix decomposition above, not from finite enumeration. Run with `python verify_cv_frontier.py` using the standard library.

## Relationship to prior work

Polydorides, Wu, Noori, Vandierendonck and Woods introduce leverage-score Bernoulli sampling and entrywise control-variate correction for a projected finite-element matrix; their discussion explicitly warns that the corrected forward sketch may not be positive definite. Thus neither the scheme nor the qualitative loss-of-positivity possibility is new here. The additional assertion is an exact, attained, all-sampling-outcome positivity frontier and minimal common diagonal repair for a balanced equal-leverage Parseval frame, accompanied by a closed MSE comparison. Maurais, Alsup, Peherstorfer and Marzouk propose positive-definite-by-construction multifidelity covariance regression on a different matrix manifold; that distinct estimator does not by its stated construction imply this entrywise Bernoulli forward-sketch frontier. Historical coverage beyond inspected accessible material is not excluded.

## Limitations

The exact classification applies to four specified rows, a two-dimensional projection, one positive diagonal parameter contrast, independent common-rate Bernoulli samples, exact arithmetic and population-known coefficients. It is not a claim about coefficients estimated from finite data, inverse or fused sketches, nonlinear finite-element solvers, or the global accuracy of a full implementation. A worst-case all-outcome scalar shift generally introduces bias; no optimal biased-estimator claim is made. The rare negative-eigenvalue event has positive but vanishing probability as \(\eta\downarrow0\). Historical priority and independent mathematical validation remain open.

## References

1. N. Polydorides, Y. Wu, H. Noori, H. Vandierendonck, and R. Woods, *Low-Variance Randomised Numerical Linear Algebra for Finite Element Simulation*, arXiv:2606.08817v1 (2026-06-07), https://arxiv.org/abs/2606.08817.
2. A. Maurais, T. Alsup, B. Peherstorfer, and Y. M. Marzouk, *Multifidelity Covariance Estimation via Regression on the Manifold of Symmetric Positive Definite Matrices*, SIAM Journal on Mathematics of Data Science 7 (2025), 189–223; arXiv:2307.12438, https://doi.org/10.1137/23M159247X.
