# The PTS-XL survival coefficient is wrong and the printed hazard can exceed one
## Finding
Let \(X\) have the 2026 Poisson two-sum XLindley (PTS-XL) distribution with parameter
\[
\theta>0.
\]
Its PMF in Eq. (2.9) is
\[
p_x
=
\frac{\theta^4(x+1)}{6(1+\theta)^{x+8}}
\left[
x^2+x\{17+6\theta(\theta+3)\}
+6\{3+\theta(\theta+3)\}^2
\right],
\qquad x=0,1,2,\ldots.
\]

The source defines the strict survival
\[
S(x)=\Pr(X>x)=\sum_{t=x+1}^{\infty}p_t
\]
and gives Eq. (2.10) in the form
\[
S_{\mathrm{pub}}(x)
=
\frac{
\omega_0(\theta)+\omega_1^{\mathrm{pub}}(\theta)x+
\omega_2(\theta)x^2+\theta^3x^3
}{6(1+\theta)^{x+8}}.
\]
The printed coefficient of \(x\) is
\[
\omega_1^{\mathrm{pub}}(\theta)
=
\theta^7+6\theta^6+18\theta^5+87\theta^4
+146\theta^3+45\theta^2+6\theta.
\]

The exact tail sum instead has
\[
\boxed{
\widetilde\omega_1(\theta)
=
6\theta^7+36\theta^6+108\theta^5+174\theta^4
+146\theta^3+45\theta^2+6\theta.
}
\]
The other three polynomial coefficients in Eq. (2.10) are unchanged. Thus
\[
\boxed{
S(x)
=
\frac{
\omega_0(\theta)+\widetilde\omega_1(\theta)x+
\omega_2(\theta)x^2+\theta^3x^3
}{6(1+\theta)^{x+8}}.
}
\]

The exact discrepancy is
\[
\boxed{
S(x)-S_{\mathrm{pub}}(x)
=
\frac{x\theta^4(5\theta^3+30\theta^2+90\theta+87)}
{6(1+\theta)^{x+8}},
\qquad x\ge1.
}
\]
It is strictly positive for every \(\theta>0\). Therefore Eq. (2.10) underestimates the strict survival and Eq. (2.11) overestimates the CDF for every positive lattice point.

The printed hazard Eq. (2.13) uses the erroneous survival in its denominator. At
\[
\theta=5,
\qquad
x=2,
\]
it gives
\[
\boxed{
h_{\mathrm{pub}}(2)
=
\frac{1814375}{1739338}
=
1.043141126106599\ldots,
}
\]
which cannot be a conditional failure probability. The correct value is
\[
\boxed{
h(2)
=
\frac{p_2}{\Pr(X\ge2)}
=
\frac{1814375}{2336838}
=
0.776423098220758\ldots.
}
\]

The source's log-concavity theorem and the resulting increasing-failure-rate classification need not be discarded: that argument is based directly on the PMF. The correction is that the closed survival, CDF, and hazard formulas must use \(\widetilde\omega_1\), not \(\omega_1^{\mathrm{pub}}\).

Section 3.6 derives stress-strength reliability by explicitly substituting Eq. (2.11). It therefore inherits the same coefficient error. For instance, with
\[
\theta_1=1,
\qquad
\theta_2=2,
\]
direct summation from the PMF and corrected survival gives
\[
\boxed{
R=\Pr(X<Y)=0.2122721975308641975\ldots,
}
\]
whereas substituting the printed survival gives
\[
0.1886554074074074074\ldots.
\]

## Assumptions and scope
The parameter domain is exactly
\[
\theta>0,
\]
and the count support is
\[
\{0,1,2,\ldots\}.
\]

The survival convention follows the source:
\[
S(x)=\Pr(X>x).
\]
Accordingly,
\[
\Pr(X\ge x)=S(x-1)
\]
for integer \(x\ge1\).

The finding corrects the closed forms derived after the PMF. It does not challenge the PMF in Eq. (2.9), the PGF in Eq. (3.15), the MGF in Eq. (3.16), or the log-concavity proof in Theorem 3.1.

No claim is made about which formula was used in unpublished numerical software. The analytic formulas printed in the article are the objects assessed here.

## Proof
Write
\[
q=\frac1{1+\theta},
\]
and define
\[
A=17+6\theta(\theta+3),
\qquad
B=6\{3+\theta(\theta+3)\}^2.
\]
Then Eq. (2.9) is
\[
p_t
=
\frac{\theta^4}{6(1+\theta)^8}
q^t(t+1)(t^2+At+B).
\]
The polynomial factor expands to
\[
(t+1)(t^2+At+B)
=
t^3+(A+1)t^2+(A+B)t+B.
\]
Hence the strict survival requires tail sums through cubic order:
\[
S(x)
=
\frac{\theta^4}{6(1+\theta)^8}
\sum_{t=x+1}^{\infty}
q^t\{t^3+(A+1)t^2+(A+B)t+B\}.
\]

The source lists only the standard tail identities for powers \(t^0,t^1,t^2\) immediately before Eq. (2.10). The missing cubic contribution is exactly what changes the linear coefficient after simplification.

Using
\[
\sum_{t=x+1}^{\infty}t^3q^t
=
\frac{q^{x+1}}{(1-q)^4}
\left[
(x+1)^3+(-3x^3-6x^2+4)q
+(3x^3+3x^2-3x+1)q^2-x^3q^3
\right],
\]
and the corresponding lower-power tail identities gives
\[
S(x)
=
\frac{
\omega_0(\theta)+\widetilde\omega_1(\theta)x+
\omega_2(\theta)x^2+\theta^3x^3
}{6(1+\theta)^{x+8}},
\]
with the corrected coefficient displayed above.

Subtracting the printed coefficient gives
\[
\widetilde\omega_1(\theta)-\omega_1^{\mathrm{pub}}(\theta)
=
\theta^4(5\theta^3+30\theta^2+90\theta+87),
\]
which proves the survival discrepancy formula.

A second exact certificate is the one-step tail recurrence. Any valid strict survival must satisfy
\[
S(x-1)-S(x)=p_x.
\]
The corrected formula satisfies this identity identically. The printed formula instead gives
\[
S_{\mathrm{pub}}(x-1)-S_{\mathrm{pub}}(x)-p_x
=
-\frac{\theta^4(\theta x-\theta-1)
(5\theta^3+30\theta^2+90\theta+87)}
{6(1+\theta)^{x+8}},
\]
which is not identically zero.

The hazard and stress-strength consequences follow by substitution into their definitions.

## Verification
The included checker performs four independent consistency checks.

First, it numerically sums the PMF tail and compares it with the corrected closed survival for several values of \(\theta\) and \(x\).

Second, it verifies the exact recurrence
\[
S(x-1)-S(x)=p_x
\]
for the corrected formula and exhibits the nonzero residual of the printed formula.

Third, it evaluates the printed and corrected hazards at
\[
(\theta,x)=(5,2),
\]
recovering the exact rational values stated above.

Fourth, it evaluates
\[
R=\sum_{x\ge0}p_X(x)\Pr(Y>x)
\]
for \((\theta_1,\theta_2)=(1,2)\), comparing direct tail summation with the corrected and printed closed survivals.

Finite numerical checks support reproducibility; the coefficient correction and recurrence failure are proved algebraically.

## Relationship to prior work
Haj Ahmad and El-Awady introduce the PTS-XL distribution by mixing a Poisson count with the sum of two independent XLindley variables. Their Proposition 1 gives the PMF used here. Immediately after the PMF, the article derives the strict survival in Eq. (2.10), the CDF in Eq. (2.11), and the hazard in Eq. (2.13). The displayed derivation lists tail sums only through the quadratic term even though the PMF polynomial is cubic after multiplication by \(x+1\).

The same article later proves strict log-concavity directly from successive PMF ratios. That argument is independent of the erroneous survival coefficient, so the increasing-failure-rate classification can survive the correction even though the printed hazard closed form does not.

Ahsan-ul-Haq et al. study the earlier Poisson-XLindley model and derive survival and hazard functions for that one-summand mixed-Poisson law. It provides relevant reliability background but does not contain the PTS-XL two-sum coefficient or correct the 2026 formula.

Focused searches using the exact DOI, full model name, survival/CDF/hazard terminology, the printed coefficient, and tail-sum aliases did not locate a corrigendum or a published PTS-XL correction.

## Limitations
The result corrects printed analytic formulas. The article's figures may have been generated by separate numerical code, so no claim is made that every plotted value used Eq. (2.13) literally.

The stress-strength example demonstrates the downstream numerical effect of the wrong CDF coefficient, but a fully re-expanded replacement for every coefficient in Eq. (3.17) is not needed for the accepted claim.

A very recent unindexed correction could exist outside the sources examined.

## References
1. H. Haj Ahmad and M. M. El-Awady, “The Poisson two-sum XLindley distribution: Statistical properties, estimation, regression modeling, and applications,” AIMS Mathematics 11 (2026), 28121–28160. DOI: 10.3934/math.20261122.
2. M. Ahsan-ul-Haq, A. Al-Bossly, M. El-Morshedy, and M. S. Eliwa, “Poisson XLindley Distribution for Count Data: Statistical and Reliability Properties with Estimation Techniques and Inference,” Computational Intelligence and Neuroscience 2022, 6503670. DOI: 10.1155/2022/6503670.
