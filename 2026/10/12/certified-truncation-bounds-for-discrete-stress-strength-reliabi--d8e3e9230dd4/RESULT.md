# Certified truncation bounds for discrete stress–strength reliability expose a DAPW stopping-rule gap
## Finding
Let \(X\) and \(Y\) be independent nonnegative-integer-valued random variables. Define
\[
R=\Pr(Y<X)=\sum_{x=0}^{\infty}p_X(x)F_Y(x-1),
\qquad F_Y(-1)=0,
\]
and truncate after index \(K\):
\[
R_K=\sum_{x=0}^{K}p_X(x)F_Y(x-1).
\]
Then the omitted remainder has the exact distribution-free bracket
\[
\boxed{
F_Y(K)\Pr(X>K)\le R-R_K\le \Pr(X>K).
}
\]
Thus any discrete stress–strength model with a computable strength survival function has an immediate certified truncation interval
\[
R\in
\left[
R_K+F_Y(K)\Pr(X>K),
\;R_K+\Pr(X>K)
\right].
\]

For the discrete Alpha-power Weibull model used by Elkalzah et al., write the strength parameters as \((\alpha,\theta_1,\beta_1)\). For \(\alpha\ne1\), its integer survival is
\[
\Pr(X\ge m)
=
\frac{\alpha}{\alpha-1}
\left[
1-\alpha^{-\theta_1^{m^{\beta_1}}}
\right],
\qquad m=0,1,2,\ldots .
\]
Therefore
\[
\Pr(X>K)
=
\frac{\alpha}{\alpha-1}
\left[
1-\alpha^{-\theta_1^{(K+1)^{\beta_1}}}
\right].
\]
At the removable Alpha-power boundary \(\alpha=1\), the same expression has the continuous limit
\[
\Pr(X>K)=\theta_1^{(K+1)^{\beta_1}}.
\]

The 2026 source instead states that its positive series is truncated when
\[
|R_K-R_{K-1}|<10^{-6}.
\]
That condition checks only the most recently added summand,
\[
R_K-R_{K-1}=p_X(K)F_Y(K-1),
\]
and does not bound the sum of all later summands.

A concrete failure occurs in the paper's own Scenario 4,
\[
(\alpha,\theta_1,\beta_1,\theta_2,\beta_2)
=(0.3,0.4,0.2,0.4,2).
\]
At \(K=4041\), direct evaluation of the exact DAPW formulas gives
\[
R_K-R_{K-1}
=
9.99890871234167\times10^{-7}<10^{-6},
\]
while
\[
\Pr(X>K)=0.00416841458563916.
\]
Moreover, monotonicity of the stress CDF gives
\[
F_Y(4041)\ge F_Y(1)=0.986585024146203.
\]
Hence the theorem certifies
\[
0.00411249540462419
< R-R_K
\le
0.00416841458563916.
\]
The omitted probability is therefore more than four thousand times the nominal last-increment threshold.

A simple rigorous replacement is: to guarantee
\[
0\le R-R_K\le\varepsilon,
\]
it is sufficient to choose \(K\) so that
\[
\Pr(X>K)\le\varepsilon.
\]
For DAPW this test is closed-form and does not require estimating a tail sum.

## Assumptions and scope
The distribution-free bracket assumes only that \(X\) and \(Y\) are independent and supported on \(\{0,1,2,\ldots\}\). It does not require DAPW structure, monotone probability masses, or an asymptotic approximation.

The DAPW specialization uses the survival-preserving discretization stated in the original DAPW article and reproduced in the 2026 stress–strength paper. The stress and strength distributions share the Alpha-power parameter \(\alpha\) in the 2026 model, while their \(\theta\) and \(\beta\) parameters may differ.

The counterexample addresses the truncation rule as printed. It does not assert that every software implementation used by the authors necessarily stopped at the first index satisfying that rule; unpublished implementation details are not inferred.

## Proof
By definition,
\[
R-R_K
=
\sum_{x=K+1}^{\infty}p_X(x)F_Y(x-1).
\]
For every \(x\ge K+1\), monotonicity of a CDF gives
\[
F_Y(K)\le F_Y(x-1)\le1.
\]
Multiplying by \(p_X(x)\ge0\) and summing yields
\[
F_Y(K)
\sum_{x=K+1}^{\infty}p_X(x)
\le
R-R_K
\le
\sum_{x=K+1}^{\infty}p_X(x).
\]
The common tail mass is
\[
\sum_{x=K+1}^{\infty}p_X(x)=\Pr(X>K),
\]
which proves the bracket.

For the DAPW distribution, the defining survival is
\[
S_X(m)=
\frac{\alpha}{\alpha-1}
\left[
1-\alpha^{-\theta_1^{m^{\beta_1}}}
\right]
\]
for \(\alpha\ne1\), so the upper bound follows by substituting \(m=K+1\). The \(\alpha=1\) formula follows from the standard Alpha-power limit
\[
\frac{\alpha}{\alpha-1}
\left(1-\alpha^{-a}\right)
\longrightarrow a
\qquad(\alpha\to1)
\]
with \(a=\theta_1^{m^{\beta_1}}\).

For Scenario 4, substitution into the exact PMF and CDF gives the displayed increment and survival values. Since \(F_Y\) is nondecreasing,
\[
F_Y(4041)\ge F_Y(1),
\]
so the lower remainder bound can be certified using only the modest-index value \(F_Y(1)\); no approximation of the far stress tail is required.

## Verification
The included checker implements the DAPW survival using numerically stable logarithmic/exponential formulas, reconstructs the PMF by survival differences, and verifies normalization on large finite windows together with the exact remainder inequalities.

For Scenario 4 it recomputes the index \(K=4041\) quantities from the model parameters, verifies that the printed \(10^{-6}\) successive-increment condition is satisfied, and checks that the certified lower remainder bound exceeds \(0.0041\).

It also checks that direct summation to a much larger index lies inside the certified interval. That finite replay is supplementary; the theorem itself is the exact inequality proved above.

## Relationship to prior work
Elkalzah et al. derive the DAPW stress–strength series and explicitly state that numerical evaluation is required because they do not have a closed form for \(R\). They say that the infinite series is truncated adaptively until the absolute difference between successive partial sums is below \(10^{-6}\), and that this is used to ensure numerical stability and accuracy. The paper does not provide a remainder theorem connecting that last increment to the omitted probability.

Mohamed, Hassan, and Abdelrahman introduced the DAPW discretization and also express stress–strength reliability as an infinite positive series. Their article supplies the closed-form survival that makes the present remainder certificate possible, but the inspected full text does not state the two-sided truncation bracket or a certified stopping rule.

Related discrete stress–strength work often obtains exact closed forms when the chosen model permits geometric summation. For example, a recent discrete-exponential model derives its reliability parameter by summing a geometric series explicitly. That does not cover DAPW's slowly decaying Scenario 4 or supply a general survival-based remainder certificate.

Focused searches for DAPW truncation errors, last-term stopping rules, stress–strength remainder certificates, and survival-tail bounds did not locate the displayed theorem or the Scenario 4 discrepancy.

## Limitations
The theorem certifies truncation error in \(R\) for fixed model parameters. It does not address parameter-estimation error, posterior Monte Carlo error, optimization error, or bootstrap error.

The Scenario 4 calculation demonstrates that the printed stopping condition can be insufficient; it does not reconstruct the authors' private software or establish which truncation index was used in every table.

The upper survival bound is intentionally simple and distribution-free. Tighter model-specific bounds may be possible, but are not needed to obtain a rigorous tolerance certificate.

## References
1. B. Elkalzah, M. O. Mohamed, K. Elsharkawy, E. S. Osman, A. Aldukeel, and G. A. Marei, “Classical and Bayesian estimation of stress–strength reliability under the discrete Alpha-power Weibull distribution with incomplete and record data: Application to high-voltage capacitors,” AIMS Mathematics 11 (2026), 6374–6399. DOI: 10.3934/math.2026263.
2. M. O. Mohamed, N. A. Hassan, and N. Abdelrahman, “Discrete alpha-power Weibull distribution: Properties and application,” International Journal of Nonlinear Analysis and Applications 13 (2022), 1305–1317. DOI: 10.22075/ijnaa.2022.6301.
3. A. Barbiero, “A new discrete exponential distribution: properties and applications,” Journal of Statistical Theory and Practice 19 (2025). DOI: 10.1007/s42519-025-00447-1.
