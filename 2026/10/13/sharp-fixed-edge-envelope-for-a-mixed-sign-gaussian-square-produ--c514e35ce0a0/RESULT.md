# Sharp fixed-edge envelope for a mixed-sign Gaussian square product
## Finding
Let \((X_1,X_2,X_3)\) be a centered Gaussian vector with unit variances, let \(0<\alpha<1\), and fix
\[
a=\operatorname{Corr}(X_1,X_2),\qquad b=\operatorname{Corr}(X_1,X_3).
\]
Set
\[
s=\sqrt{(1-a^2)(1-b^2)}
\]
and
\[
B=1-\alpha(a^2+b^2)+(\alpha^2-2\alpha+2)a^2b^2.
\]
Then, over every admissible value \(c=\operatorname{Corr}(X_2,X_3)\),
\[
\inf_c\frac{\mathbb E[|X_1|^{-\alpha}X_2^2X_3^2]}{\mathbb E|X_1|^{-\alpha}}
=B-2(1-\alpha)^2a^2b^2+2\bigl((1-\alpha)|ab|-s\bigr)_+^2.
\]
An optimizer is
\[
c_*=ab-\operatorname{sgn}(ab)\min\{(1-\alpha)|ab|,s\},
\]
where \(\operatorname{sgn}(0)=0\). Thus the optimizer is interior exactly when
\[
(1-\alpha)|ab|\le \sqrt{(1-a^2)(1-b^2)},
\]
in which case \(c_*=\alpha ab\). Beyond that phase boundary, the optimizer lies at a positive-semidefinite boundary where the residual covariance of \((X_2,X_3)\) conditional on \(X_1\) is singular.

The resulting sharp fixed-edge bound is strictly stronger than
\[
(1-a^2)(1-b^2)
\]
for every \((a,b)\ne(0,0)\). For example, when \(\alpha=1/2\) and \(a=b=1/2\), the minimizing correlation is \(c_*=1/8\) and the exact normalized minimum is \(51/64\), whereas the earlier factor is \(9/16\).

## Assumptions and scope
The Gaussian vector is allowed to be singular. The coordinates have mean zero and unit variance. The exponent satisfies \(0<\alpha<1\), which is exactly the integrability range for \(\mathbb E|X_1|^{-\alpha}\). The pair \((a,b)\) is fixed, and only the remaining correlation \(c\) is optimized. The statement concerns the mixed-sign moment with one negative absolute exponent and two quadratic factors; it does not assert a corresponding envelope for arbitrary positive exponents or higher dimension.

## Proof
Write
\[
d=c-ab.
\]
The Schur complement of the \(X_1\) coordinate shows that the correlation matrix is positive semidefinite exactly when
\[
|d|\le s=\sqrt{(1-a^2)(1-b^2)}.
\]
Conditionally on \(X_1=x\), write
\[
X_2=ax+U,\qquad X_3=bx+V,
\]
where \((U,V)\) is centered Gaussian with
\[
\operatorname{Var}(U)=1-a^2,\qquad
\operatorname{Var}(V)=1-b^2,\qquad
\operatorname{Cov}(U,V)=d.
\]
Isserlis' formula gives
\[
\begin{aligned}
\mathbb E[X_2^2X_3^2\mid X_1=x]
={}&a^2b^2x^4\\
&+\bigl(a^2(1-b^2)+b^2(1-a^2)+4abd\bigr)x^2\\
&+(1-a^2)(1-b^2)+2d^2.
\end{aligned}
\]
For a standard normal \(G\), the gamma recurrence yields
\[
\frac{\mathbb E|G|^{2-\alpha}}{\mathbb E|G|^{-\alpha}}=1-\alpha,
\qquad
\frac{\mathbb E|G|^{4-\alpha}}{\mathbb E|G|^{-\alpha}}=(1-\alpha)(3-\alpha).
\]
After averaging the conditional formula against \(|X_1|^{-\alpha}\), the normalized moment becomes the quadratic
\[
R(d)=B+4ab(1-\alpha)d+2d^2.
\]
Completing the square,
\[
R(d)=B-2(1-\alpha)^2a^2b^2+2\bigl(d+ab(1-\alpha)\bigr)^2.
\]
Minimizing this convex quadratic on \([-s,s]\) is projection of \(-ab(1-\alpha)\) onto that interval. This gives the displayed formula and optimizer, including both the interior and boundary regimes.

For comparison with the previously available factor, first minimize the same quadratic without the interval constraint. The resulting value is
\[
1-\alpha(a^2+b^2)+\alpha(2-\alpha)a^2b^2.
\]
Subtracting \((1-a^2)(1-b^2)\) gives
\[
(1-\alpha)\bigl(a^2+b^2-(1-\alpha)a^2b^2\bigr).
\]
This is positive whenever \((a,b)\ne(0,0)\). The constrained minimum is at least the unconstrained minimum, proving the strict improvement for every nontrivial fixed pair.

## Verification
The proof is analytic and exhaustive: the Schur-complement interval is the full admissible set of the remaining correlation, and a strictly convex one-variable quadratic is minimized exactly by projection. A companion exact-rational script independently evaluates the conditional-moment formula and the proposed minimum on a finite grid of Pythagorean correlation values in both the interior and boundary regimes. Those finite checks are consistency tests only and are not used as a substitute for the universal proof.

## Relationship to prior work
Zhou, Zhao, Hu and Song prove, for one negative exponent and quadratic remaining coordinates, the lower factor obtained by multiplying the residual variances \((1-\rho_{1i}^2)\). In three standardized dimensions their theorem yields \((1-a^2)(1-b^2)\). Their statement does not optimize the moment over the remaining correlation when \(a\) and \(b\) are fixed.

Lan, Ouimet and Sun later treat broader mixed-sign Gaussian product inequalities and explicitly recover the earlier one-negative, quadratic-positive bound as a specialization. Their result likewise does not give this fixed-edge constrained minimum or the optimizer phase transition. Later series-formula work for mixed-sign absolute moments evaluates structured correlation families but does not supply the arbitrary fixed-\((a,b)\) envelope established here.

## Limitations
The result is specialized to three standardized Gaussian coordinates, one exponent in \((-1,0)\) written as \(-\alpha\), and two square factors. It does not determine analogous envelopes for nonquadratic positive exponents, more than three coordinates, or non-Gaussian vectors. A differently phrased equivalent fixed-edge optimization could exist in poorly indexed literature; targeted searches and inspection of the most relevant primary and follow-up sources did not find one.

## References
1. Y. Zhou, B. Zhao, Z.-C. Hu, and B.-Q. Song, *Some New Results on Gaussian Product Inequalities*, arXiv:2308.13740v1, 2023; Journal of Mathematical Analysis and Applications, DOI:10.1016/j.jmaa.2023.127907.
2. G. Lan, F. Ouimet, and Y. Sun, *Results related to the Gaussian product inequality conjecture for mixed-sign exponents in arbitrary dimension*, arXiv:2505.09976v2, 2025.
3. H. Ogasawara, *Gaussian product inequalities for absolute moments of mixed-sign orders using a series formula*, DOI:10.1080/03610926.2025.2560040.
