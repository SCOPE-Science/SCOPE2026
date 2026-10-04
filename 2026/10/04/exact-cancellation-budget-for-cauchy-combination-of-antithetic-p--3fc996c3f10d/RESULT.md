# Exact cancellation budget for Cauchy combination of antithetic p-value pairs
## Finding
Let \(U_1,\ldots,U_m\) be independent \(\mathrm{Uniform}(0,1)\) variables. For each \(j\), form the antithetic pair of exact null p-values
\[
P_{j,+}=U_j,
\qquad
P_{j,-}=1-U_j.
\]
Assign deterministic nonnegative weights \(w_{j,+},w_{j,-}\) satisfying
\[
\sum_{j=1}^m (w_{j,+}+w_{j,-})=1,
\]
and apply the usual weighted Cauchy combination statistic
\[
T=\sum_{j=1}^m\left[
w_{j,+}\tan\{\pi(1/2-P_{j,+})\}
+w_{j,-}\tan\{\pi(1/2-P_{j,-})\}
\right].
\]
Define the cancellation budget
\[
A=\sum_{j=1}^m |w_{j,+}-w_{j,-}|.
\]
Because the weights are nonnegative and sum to one,
\[
A=1-2\sum_{j=1}^m\min(w_{j,+},w_{j,-}),
\qquad 0\le A\le1.
\]
Then the null law is exactly
\[
T\sim\mathrm{Cauchy}(0,A),
\]
with the convention that \(A=0\) means the point mass at zero.

For the usual reported standard-Cauchy p-value
\[
P_C=\frac12-\frac1\pi\arctan(T),
\]
if \(A>0\), then for every \(0<c<1\),
\[
\Pr(P_C\le c)=
\frac12-\frac1\pi
\arctan\!\left(\frac{\cot(\pi c)}{A}\right).
\]
If \(A=0\), then \(P_C=1/2\) almost surely.

Hence, for every nominal level \(0<\alpha<1/2\), the exact rejection probability is
\[
s_A(\alpha)=
\begin{cases}
0, & A=0,\\
\displaystyle
\frac12-\frac1\pi
\arctan\!\left(\frac{\cot(\pi\alpha)}{A}\right), & 0<A\le1.
\end{cases}
\]
It is strictly increasing in \(A\). Thus the usual Cauchy calibration is exact exactly when \(A=1\), which occurs exactly when every antithetic pair has at most one positive weight. It is strictly conservative whenever \(0<A<1\), and it is completely nonrejecting when every pair is internally balanced, so \(A=0\). In the extreme tail,
\[
\frac{s_A(\alpha)}{\alpha}\longrightarrow A
\qquad\text{as}\qquad \alpha\downarrow0.
\]
The scalar \(A\) is therefore an exact cancellation budget: every unit of weight simultaneously placed on both sides of the same antithetic pair reduces the small-level rejection rate by the corresponding amount.

A natural realization uses independent Gaussian contrasts. If \(Z_1,\ldots,Z_m\) are independent standard normal variables and both one-sided directions are included, then
\[
P_{j,+}=1-\Phi(Z_j),
\qquad
P_{j,-}=1-\Phi(-Z_j)=1-P_{j,+}.
\]
Thus the theorem describes a singular but ordinary Gaussian dependence architecture rather than an artificial coupling of p-values.

For a single pair with weights \(w\) and \(1-w\), one has \(A=|2w-1|\). At nominal level \(\alpha=0.05\), the rejection probability is \(0\) for \(w=1/2\), approximately \(0.025155168137137\) for \(w=3/4\), approximately \(0.040118479962686\) for \(w=0.9\), and exactly \(0.05\) at an endpoint weight.

## Assumptions and scope
The theorem assumes independent latent uniforms across pairs, exact complementarity within each pair, deterministic nonnegative weights, and the standard Cauchy transform and standard-Cauchy reference cdf. It is a finite-sample statement for this antithetic-block dependence model. It does not assert an analogous formula for imperfect negative correlations, dependence across the latent pairs, random weights, or truncated/positive Cauchy variants.

The primary method source introduced the weighted Cauchy statistic and standard-Cauchy p-value calculation. Later work broadened dependence theory and explicitly documented that negatively correlated one-sided p-values can make the Cauchy method unusually conservative. The claim here isolates a natural exact dependence architecture and classifies its calibration completely through one weight functional \(A\).

## Proof
For each \(j\), define
\[
C_j=\tan\{\pi(1/2-U_j)\}.
\]
The variables \(C_1,\ldots,C_m\) are independent standard Cauchy variables. Complementarity gives
\[
\tan\{\pi(1/2-P_{j,-})\}
=\tan\{\pi(U_j-1/2)\}
=-C_j.
\]
Therefore
\[
T=\sum_{j=1}^m d_j C_j,
\qquad
 d_j=w_{j,+}-w_{j,-}.
\]
The characteristic function of a standard Cauchy variable is \(\exp(-|t|)\). Independence therefore gives
\[
\mathbb E\,e^{itT}
=
\prod_{j=1}^m e^{-|d_jt|}
=
\exp\!\left(-|t|\sum_{j=1}^m|d_j|\right)
=e^{-A|t|}.
\]
This is the characteristic function of \(\mathrm{Cauchy}(0,A)\), proving the exact null law, including degeneracy when \(A=0\).

For nonnegative numbers \(x,y\), \(|x-y|=x+y-2\min(x,y)\). Summing this identity over the pairs and using total weight one yields the second expression for \(A\). It also shows that \(A=1\) exactly when \(\min(w_{j,+},w_{j,-})=0\) for every \(j\), and \(A=0\) exactly when \(w_{j,+}=w_{j,-}\) for every \(j\).

If \(A>0\), the map \(t\mapsto 1/2-\arctan(t)/\pi\) is decreasing, so
\[
P_C\le c
\quad\Longleftrightarrow\quad
T\ge\cot(\pi c).
\]
The upper tail of \(\mathrm{Cauchy}(0,A)\) is
\[
\Pr(T\ge x)
=
\frac12-\frac1\pi\arctan(x/A),
\]
which proves the displayed p-value cdf. For \(0<\alpha<1/2\), the threshold \(\cot(\pi\alpha)\) is positive, so the rejection probability is strictly increasing in \(A\). At \(A=1\), the identity \(\arctan(\cot(\pi\alpha))=\pi/2-\pi\alpha\) gives exact size \(\alpha\); for \(0<A<1\), the size is strictly smaller.

Finally, \(\cot(\pi\alpha)\sim1/(\pi\alpha)\) and \(\pi/2-\arctan x\sim1/x\) as \(\alpha\downarrow0\), yielding \(s_A(\alpha)\sim A\alpha\).

## Verification
The proof uses exact transformation identities, independence across latent pairs, and the characteristic function of the Cauchy law. The accompanying checker recomputes the cancellation budget from arbitrary weight vectors, verifies the one-pair numerical examples, checks endpoint/degenerate cases, and checks the small-level ratio. Those computations are consistency checks only; the finite-sample theorem follows analytically from the characteristic-function calculation.

For the Gaussian realization, the probability-integral transform makes \(1-\Phi(Z_j)\) uniform, and symmetry gives \(1-\Phi(-Z_j)=1-(1-\Phi(Z_j))\). Independence of the Gaussian contrasts supplies independence across antithetic pairs.

## Relationship to prior work
Liu and Xie introduced the weighted Cauchy statistic and the standard-Cauchy reference calculation. Their paper explicitly notes exact standard-Cauchy behavior under independence and under perfect positive dependence, and develops a broad small-tail approximation under dependence. The inspected full text does not state the antithetic-block cancellation budget \(A\), the scaled-Cauchy law, or the exact calibration classification above.

Long, Li, Zhang, and Li broadened Cauchy tail-approximation theory under p-value dependence. The inspected material does not provide the exact blockwise-antithetic weighted law.

Gui, Jiang, and Wang provide the closest substantive comparison. Their analysis covers one-sided p-values, explicitly observes that negative correlation can make the Cauchy combination test more conservative than Bonferroni, and discusses perfect-correlation boundaries asymptotically. The exact scaled-Cauchy law for independent antithetic blocks, the complete weight criterion for exactness, and the tail attenuation factor \(A\) are not stated in the inspected main text. Their qualitative observation is therefore sharpened here into a finite-level classification for a natural singular dependence model.

Ota studies fixed-level calibration when the number of p-values grows in a one-factor equicorrelated Gaussian model. That regime is distinct from finitely many independent contrasts with perfect negative dependence inside each pair.

## Limitations
The result is exact only for independent latent blocks with perfect complementarity inside each block. It should not be extrapolated to near-antithetic Gaussian correlations or arbitrary dependence across blocks. The original CCT Gaussian theorem is formulated for two-sided p-values, whereas the Gaussian realization here uses one-sided p-values; later heavy-tailed-combination theory explicitly treats one-sided p-values and negative correlations.

The stable-law calculation is elementary once the dependence architecture is exposed. An equivalent statement could therefore exist in unindexed notes, software discussions, or supplementary material; targeted searches and inspection of the closest primary texts did not locate one, but this remains the principal originality risk.

The theorem concerns null calibration. It does not itself establish power optimality or prescribe weighting outside this singular antithetic architecture.

## References
1. Liu, Y. and Xie, J. “Cauchy combination test: a powerful test with analytic p-value calculation under arbitrary dependency structures.” arXiv:1808.09011; Journal of the American Statistical Association 115 (2020), 393–402. DOI: 10.1080/01621459.2018.1554485.
2. Long, M., Li, Z., Zhang, W., and Li, Q. “The Cauchy Combination Test under Arbitrary Dependence Structures.” arXiv:2107.06040; The American Statistician 77 (2023), 134–142. DOI: 10.1080/00031305.2022.2116109.
3. Gui, L., Jiang, Y., and Wang, J. “Aggregating dependent signals with heavy-tailed combination tests.” arXiv:2310.20460; Biometrika 112 (2025), asaf038. DOI: 10.1093/biomet/asaf038.
4. Ota, H. “Fixed-level calibration of the Cauchy combination test.” arXiv:2603.22668.
