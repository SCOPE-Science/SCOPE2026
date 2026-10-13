# The two-summand case of the variance-equalization concentration conjecture
## Finding
Let \(\nu^m\) be uniform on \(\{-m+1,-m+3,\ldots,m-1\}\). For \(\alpha\in(0,1]\), put
\[
k(\alpha)=\lfloor 1/\alpha\rfloor,
\qquad
\tau(\alpha)=k(\alpha)(k(\alpha)+1)\alpha-k(\alpha),
\]
and let \(T(\alpha)\) have law
\[
\tau(\alpha)\nu^{k(\alpha)}+(1-\tau(\alpha))\nu^{k(\alpha)+1}.
\]
For a real random variable \(Z\), define
\[
\mathcal Q_2(Z)=\sup_{x\in\mathbb R}\Pr\{Z\in(x,x+2]\}.
\]
If \(T(\alpha)\) and \(T(\beta)\) are independent, then
\[
\mathcal Q_2(T(\alpha)+T(\beta))=
\begin{cases}
\displaystyle \frac1{k+1}+\frac{\tau(\alpha)\tau(\beta)}{k(k+1)},&k(\alpha)=k(\beta)=k,\\[6pt]
\min\{\alpha,\beta\},&k(\alpha)\ne k(\beta).
\end{cases}
\]
Consequently, if \(\alpha_1,\alpha_2\in(0,1]\) and \(\alpha_*\) is the unique value satisfying
\[
2\operatorname{Var}(T(\alpha_*))
=
\operatorname{Var}(T(\alpha_1))+
\operatorname{Var}(T(\alpha_2)),
\]
then, for independent copies,
\[
\mathcal Q_2(T(\alpha_1)+T(\alpha_2))
\le
\mathcal Q_2(T(\alpha_*)+T(\alpha_*)).
\]
Equality holds if and only if \(\alpha_1=\alpha_2\). Thus Conjecture 6.1 of Juškevičius holds for two summands throughout the positive parameter range.

## Assumptions and scope
The variables are real, independent, and use the extremal family \(T(\alpha)\) defined above. The parameter range is \((0,1]\); no assertion is made at the limiting parameter \(\alpha=0\), where the finite-support description leaves every fixed canonical cell. The concentration length is exactly \(2\), matching the normalization in the motivating source.

The proof uses the published fact that for sums of these extremal variables the central half-open interval \((-1,1]\) attains \(\mathcal Q_2\). All new algebra below is elementary and finite.

## Proof
For independent \(U_r\sim\nu^r\) and \(U_s\sim\nu^s\), the support of \(U_r+U_s\) lies on one parity class. Its central support point is \(0\) when the parities agree and \(1\) when they disagree. Exactly \(\min\{r,s\}\) of the \(rs\) ordered pairs hit that central point. Hence
\[
\Pr\{U_r+U_s\in(-1,1]\}=\frac1{\max\{r,s\}}.
\]
Mixing the four pairs of uniform components gives the displayed two-summand formula. If both parameters lie in the same canonical cell \((1/(k+1),1/k]\), all component pairs except \((\nu^k,\nu^k)\) contribute \(1/(k+1)\), while that pair contributes \(1/k\). If the cells differ, every component size from the smaller-parameter variable is at least every component size from the larger-parameter variable, so the mixture collapses to the smaller parameter.

The variance is
\[
v(\alpha):=\operatorname{Var}(T(\alpha))
=k(k+1)\left(1-\frac{2k+1}{3}\alpha\right),
\qquad k=k(\alpha).
\]
It is continuous and strictly decreasing from \(+\infty\) to \(0\) as \(\alpha\) runs from \(0\) to \(1\). Thus \(\alpha_*\) exists uniquely and lies between \(\alpha_1\) and \(\alpha_2\).

Assume \(\alpha_1\ge\alpha_2\). If both parameters have the same cell index \(k\), linearity of \(v\) on that cell gives \(\alpha_*=(\alpha_1+\alpha_2)/2\), hence \(\tau_*=(\tau_1+\tau_2)/2\). Therefore
\[
\mathcal Q_2(T(\alpha_*)+T(\alpha_*))
-
\mathcal Q_2(T(\alpha_1)+T(\alpha_2))
=
\frac{(\tau_1-\tau_2)^2}{4k(k+1)}.
\]
This is nonnegative, and vanishes exactly when \(\alpha_1=\alpha_2\).

Now suppose the cell indices differ, with \(k(\alpha_2)=k\). The exact formula gives
\[
\mathcal Q_2(T(\alpha_1)+T(\alpha_2))=\alpha_2.
\]
If \(k(\alpha_*)\le k-1\), then
\[
\mathcal Q_2(T(\alpha_*)+T(\alpha_*))\ge \frac1{k}>\alpha_2,
\]
except that when \(\alpha_2=1/k\) the first inequality is still strict because \(\alpha_*>1/k\).

It remains to consider \(k(\alpha_*)=k\). Write \(\tau_2=\tau(\alpha_2)\) and \(\tau_*=\tau(\alpha_*)\). Because \(\alpha_1>1/k\), strict monotonicity gives \(v(\alpha_1)<v(1/k)\). Affinity of \(v\) in \(\tau\) on the \(k\)-th cell therefore implies
\[
\tau_*>\frac{1+\tau_2}{2}.
\]
Consequently,
\[
\begin{aligned}
\mathcal Q_2(T(\alpha_*)+T(\alpha_*))-
\alpha_2
&>
\frac1{k+1}
+
\frac{(1+\tau_2)^2}{4k(k+1)}
-
\frac{k+\tau_2}{k(k+1)}\\
&=
\frac{(1-\tau_2)^2}{4k(k+1)}\ge0.
\end{aligned}
\]
In this subcase \(\tau_2<1\), so the final inequality is strict. This completes the proof and the equality classification.

## Verification
The standalone exact-arithmetic checker `verify.py` reconstructs \(\nu^m\), the mixtures \(T(\alpha)\), their convolutions, concentration functions, and variances using rational arithmetic. It verifies the uniform-pair identity for \(1\le r,s<25\), the closed two-summand formula, variance identity, variance-matching parameter, inequality, and strictness on \(8001\) rational parameter pairs sampled across canonical cells through index \(18\).

Its replay output is:

`VERIFY_OK`

`pairs_checked 8001`

As a concrete case below the previously covered \(\alpha_i\ge1/2\) region, \((\alpha_1,\alpha_2)=(1/3,1/5)\) gives \(\alpha_*=11/45\), left side \(1/5\), and equalized right side \(97/405\). These finite checks are supplementary; the proof above is universal.

## Relationship to prior work
Juškevičius proves the sharp Kolmogorov--Rogozin extremal theorem for the family \(T(\alpha)\) and then poses Conjecture 6.1: replacing arbitrary parameters by a common parameter with the same total variance should not decrease concentration. The same paper states that Kanter's earlier concentration comparison proves this equalization phenomenon when all parameters satisfy \(\alpha_i\ge1/2\), for arbitrary numbers of summands. The present result instead proves the complete two-summand case for every positive parameter, including the lower-concentration cells not covered by that condition, and gives the exact two-summand concentration formula and equality case.

Targeted searches for the conjecture number, the two-summand specialization, the exact \(\mathcal Q_2\) formula, variance equalization, and arithmetic-progression extremizers did not locate a published statement implying this theorem. The closest retrieved work concerns different concentration objects or different distribution families.

## Limitations
No claim is made for three or more summands outside the already known parameter regime, nor for \(\alpha=0\). The originality comparison is necessarily limited by indexing: an equivalent short proof could exist in poorly indexed literature. The exact finite checker does not certify the infinite parameter domain; universality comes from the analytic proof.

## References
1. T. Juškevičius, *The sharp form of the Kolmogorov--Rogozin inequality and a conjecture of Leader--Radcliffe*, arXiv:2201.09861v1 (2022); Bulletin of the London Mathematical Society 56 (2024), 3289--3299, DOI 10.1112/blms.13132.
2. M. Kanter, *Probability inequalities for convex sets and multidimensional concentration functions*, Journal of Multivariate Analysis 6 (1976), 222--236.
3. L. Mattner and B. Roos, *A shorter proof of Kanter's Bessel function concentration bound*, Probability Theory and Related Fields 139 (2007), 191--205; arXiv:math/0603522.
