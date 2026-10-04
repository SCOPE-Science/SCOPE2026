# Sharp reserve–efficiency frontier for fractional batch conformal e-prediction

## Finding

Fix an error level \(\alpha\in(0,1)\). Suppose the current batch has \(n\ge 1\) positive calibration scores with sum \(B>0\), and suppose the e-process wealth before the batch is \(W\) with \(0<W<1/\alpha\). For a positive candidate score \(v\), use the ratio e-value
\[
e(v)=\frac{(n+1)v}{B+v},
\]
and a predictable fractional bet \(\lambda\in[0,1]\), giving candidate wealth
\[
W_\lambda(v)=W\bigl(1-\lambda+\lambda e(v)\bigr).
\]
Write \(h=(\alpha W)^{-1}>1\), and define the non-crossing score set
\[
C_\lambda=\left\{v>0:W_\lambda(v)<\frac1\alpha\right\}.
\]

The set has an exact phase transition:
\[
C_\lambda=
\begin{cases}
(0,\infty), & h\ge 1+n\lambda,\\
(0,U_\lambda), & h<1+n\lambda,
\end{cases}
\qquad
U_\lambda=
B\frac{h-1+\lambda}{1+n\lambda-h}.
\]
Thus some fractional bet gives a finite current upper endpoint if and only if
\[
W>\frac{1}{\alpha(n+1)}.
\]
On the finite branch,
\[
\frac{dU_\lambda}{d\lambda}
=
-\frac{B(h-1)(n+1)}{(1+n\lambda-h)^2}<0,
\]
so larger fractions produce nested smaller current score sets, and the all-in choice \(\lambda=1\) is pointwise smallest whenever a finite current set is possible.

There is also a sharp one-step reserve frontier. Suppose the next batch will have \(m\ge1\) calibration scores. To guarantee, uniformly over the current realized positive candidate score, a reserve
\[
R\in\left(\frac1{\alpha(m+1)},W\right],
\]
one must and may choose
\[
\lambda\le 1-\frac RW.
\]
The largest reserve-feasible choice,
\[
\lambda^\star=1-\frac RW,
\]
therefore yields a smallest current score set among all fractions that guarantee enough wealth for a bounded all-in score set at the next batch. If \(\lambda^\star>(h-1)/n\), its current endpoint is finite and strictly smaller than that from every smaller reserve-feasible fraction on the finite branch.

## Assumptions and scope

The result applies to the batch anytime-valid conformal e-prediction construction based on the ratio e-value of Gauthier, Bach, and Jordan. Scores are positive, the current calibration sum is positive, and the fractional betting fraction is chosen predictably from information available before the current test score is revealed. The result is deterministic conditional on the past and on the current calibration scores; the probabilistic validity of the e-process is inherited from the cited martingale construction.

The reserve statement is a worst-case one-step guarantee over all positive current candidate scores. It guarantees only that the next batch starts above the exact wealth threshold at which an all-in set can be bounded, provided the next batch also has a positive calibration sum. It does not claim optimality for a multi-step expected-size objective.

## Proof

Because \(B>0\),
\[
e'(v)=\frac{(n+1)B}{(B+v)^2}>0,
\]
and, for finite \(v>0\),
\[
0<e(v)<n+1.
\]
The non-crossing condition is
\[
1-\lambda+\lambda e(v)<h.
\]

If \(h\ge1+n\lambda\), then for every finite positive \(v\),
\[
1-\lambda+\lambda e(v)<1+n\lambda\le h,
\]
so \(C_\lambda=(0,\infty)\). If \(h<1+n\lambda\), solving the strict inequality gives
\[
v<
B\frac{h-1+\lambda}{1+n\lambda-h},
\]
whose numerator and denominator are both positive. This proves the displayed phase transition.

A finite set is possible for some \(\lambda\in[0,1]\) exactly when \(h<1+n\), equivalently
\[
W>\frac1{\alpha(n+1)}.
\]
Differentiating the finite endpoint gives
\[
\frac{dU_\lambda}{d\lambda}
=
-\frac{B(h-1)(n+1)}{(1+n\lambda-h)^2}<0,
\]
because \(h>1\). This proves the nesting and current-set optimality of the all-in fraction.

For the reserve statement, since \(e(v)>0\) and \(e(v)\downarrow0\) as \(v\downarrow0\),
\[
\inf_{v>0}W_\lambda(v)=W(1-\lambda).
\]
Therefore \(W_\lambda(v)\ge R\) for every positive \(v\) if and only if
\[
W(1-\lambda)\ge R,
\]
which is equivalent to \(\lambda\le1-R/W\). The condition \(R>1/[\alpha(m+1)]\) places every allowed realized post-batch wealth strictly above the next-batch boundedness threshold. Since current sets shrink monotonically as \(\lambda\) grows, the largest reserve-feasible fraction yields a smallest current set. Strict endpoint improvement holds once the frontier lies on the finite branch.

## Verification

The proof is symbolic and does not depend on numerical experimentation. A standalone checker in `artifacts/verify.py` verifies the algebraic classification on exact rational grids, checks nestedness on deterministic pseudo-random positive instances, and checks both directions of the reserve frontier. Running `python artifacts/verify.py` prints `VERIFY_OK`.

The checker is supplementary: the infinite-domain statements follow from the monotonicity and exact algebra above, not from finite enumeration.

## Relationship to prior work

Gauthier, Bach, and Jordan introduce the batch anytime-valid conformal e-prediction process and, in their Remark 2.7, explicitly note the fractional product
\[
\prod_s(1-\lambda_s+\lambda_s E_s)
\]
for predictable \(\lambda_s\in[0,1]\), while focusing on the all-in choice for simplicity and identifying alternatives as worth exploring. Their paper does not state the phase transition for bounded score sets or the sharp wealth-reserve frontier proved here.

Koning and van Meer study e-values as fuzzy prediction sets and utility-based notions of prediction-set optimality, including the ratio form of conformal e-values, but their treatment is primarily a single-batch decision framework rather than the fractional batch-wealth geometry above. Waudby-Smith and Ramdas develop predictable betting fractions for confidence sequences and provide the broader betting interpretation behind the fractional update, but not this conformal ratio-score endpoint calculation.

A recent set-preserving p-to-e calibration paper studies efficiency of conformal p-to-e conversion; its objective and construction are different from the fractional sequential reserve tradeoff here. These comparisons support non-implication by the inspected sources, while not constituting an exhaustive proof of historical priority.

## Limitations

The result is one-step and conditional on the current calibration scores and past wealth. It does not optimize an expected cumulative loss, adapt \(\lambda\) to a stochastic model for future scores, or compare empirical prediction-set sizes across datasets. The reserve guarantee is deliberately worst-case over the current score and can be conservative when score distributions are known. Literature searches cannot rule out every equivalent statement in unindexed or unpublished work.

## References

1. E. Gauthier, F. Bach, and M. I. Jordan, “E-Values Expand the Scope of Conformal Prediction,” arXiv:2503.13050, first submitted 17 March 2025. https://arxiv.org/abs/2503.13050
2. N. W. Koning and S. van Meer, “Fuzzy Prediction Sets: Conformal Prediction with E-values,” arXiv:2509.13130, first submitted 16 September 2025. https://arxiv.org/abs/2509.13130
3. I. Waudby-Smith and A. Ramdas, “Estimating means of bounded random variables by betting,” Journal of the Royal Statistical Society: Series B 86(1), 1–27. https://doi.org/10.1093/jrsssb/qkad009
4. N. Alami, J. Zakharia, and S. Ben Taieb, “Set-Preserving Calibration from Conformal P-Values to E-Values,” arXiv:2606.03600, first submitted 2 June 2026. https://arxiv.org/abs/2606.03600
