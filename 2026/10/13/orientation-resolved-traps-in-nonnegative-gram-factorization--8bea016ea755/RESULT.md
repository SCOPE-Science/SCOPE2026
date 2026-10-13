# Orientation-resolved traps in nonnegative Gram factorization

## Finding

Let \(m,k,r\) be integers with \(m\ge 1\), \(k\ge 1\), and \(r\ge k+1\). Write \(J_m=\mathbf 1_m\mathbf 1_m^{\mathsf T}\), \(M=\operatorname{diag}(J_m,I_k)\), and consider the fully observed symmetric nonnegative factorization objective
\[
 F(U)=\tfrac12\|UU^{\mathsf T}-M\|_F^2,\qquad U\in\mathbb R_+^{(m+k)\times r}.
\]
For every strictly positive unit vector \(a\in\mathbb R_{>0}^{r}\), let
\[
 U(a)=\begin{bmatrix}\mathbf1_m a^{\mathsf T}\\0_{k\times r}\end{bmatrix},\qquad h(a)=m\min_{1\le j\le r}a_j^2.
\]
**Complete orientation phase diagram.** All \(U(a)\) have the same fitted Gram matrix \(\operatorname{diag}(J_m,0_k)\), the same positive objective \(k/2\), and vanishing first derivative. Nonetheless:

1. If \(h(a)>1\), then \(U(a)\) is a spurious, non-strict local minimizer.
2. If \(h(a)=1\), then \(U(a)\) satisfies the constrained second-order necessary conditions but **is not** a local minimizer; arbitrarily small nonnegative perturbations lower the objective at quartic order.
3. If \(h(a)<1\), then a feasible one-sided direction has strictly negative quadratic curvature, so \(U(a)\) is not a local minimizer.

Thus local minimizers in this entire Gram-equivalent family exist precisely when \(m>r\) and \(a_j>1/\sqrt m\) for every coordinate. If \(m>r\), choosing a balanced \(a\) and a sufficiently imbalanced positive \(a\) produces a spurious local minimizer and a saddle with **identical** Gram matrices, objective values, and first derivatives. The maximum entrywise orientation margin \(\min_j a_j-1/\sqrt m\) among unit positive vectors is \(1/\sqrt r-1/\sqrt m\), uniquely attained at the balanced vector.

## Assumptions and scope

The problem is real, finite-dimensional, fully observed and noiseless; factors are elementwise nonnegative, and the loss is the squared Frobenius Gram error. The classification concerns only the explicitly defined **collapsed-block stationary family** \(U(a)\), not all stationary points or all local minima of \(F\). The strict positivity of all coordinates of \(a\) and the rank condition \(r\ge k+1\ge2\) are essential for the critical-case descent construction and for zero attainable global loss.

## Proof

Partition any feasible \(U\) as \(U=[Y;Z]\), with \(Y\in\mathbb R_+^{m\times r}\) and \(Z\in\mathbb R_+^{k\times r}\). Direct block expansion, retaining every quartic term, yields the **exact identity**
\[
 F(U)-\frac k2=\frac12\|YY^{\mathsf T}-J_m\|_F^2+\|YZ^{\mathsf T}\|_F^2-\|Z\|_F^2+\frac12\|ZZ^{\mathsf T}\|_F^2.\tag{1}
\]
At \(U(a)\), the upper block is \(Y_0=\mathbf1_m a^{\mathsf T}\). Because \(\|a\|_2=1\), \(Y_0Y_0^{\mathsf T}=J_m\) and \(F(U(a))=k/2\). The gradient \(2(UU^{\mathsf T}-M)U\) vanishes there. A global minimizer with value zero places the \(m\) identical head rows in the first factor column and the \(k\) singleton rows in distinct remaining columns; this is possible since \(r\ge k+1\). Consequently every local minimizer at \(U(a)\) is spurious.

**Positive phase.** If \(h(a)>1\), put \(a_{\min}=\min_j a_j\). Fix any \(0<\varepsilon<a_{\min}-1/\sqrt m\). For every feasible \(U=[Y;Z]\) satisfying \(|Y_{ij}-a_j|<\varepsilon\), each entry of \(Y\) is at least \(a_{\min}-\varepsilon\). For every nonnegative row vector \(z\) of \(Z\),
\[
 \|Yz^{\mathsf T}\|_2^2\ge m(a_{\min}-\varepsilon)^2\|z\|_1^2\ge m(a_{\min}-\varepsilon)^2\|z\|_2^2.
\]
Summing rows gives \(\|YZ^{\mathsf T}\|_F^2\ge m(a_{\min}-\varepsilon)^2\|Z\|_F^2\). Substitution into (1) proves the quantitative, uniform-in-\(Z\) certificate
\[
 F(U)-\frac k2\ge\frac12\|YY^{\mathsf T}-J_m\|_F^2+\bigl[m(a_{\min}-\varepsilon)^2-1\bigr]\|Z\|_F^2+\frac12\|ZZ^{\mathsf T}\|_F^2\ge0.\tag{2}
\]
This supplies a neighborhood in the full feasible factor space. It is not a strict minimum: varying \(a\) slightly along the positive unit sphere leaves the Gram matrix unchanged.

**Negative phase.** If \(h(a)<1\), select a coordinate \(j\) satisfying \(ma_j^2<1\). Hold \(Y=Y_0\) and set one row of \(Z\) to \(t e_j^{\mathsf T}\), all other rows to zero. Equation (1) gives
\[
 F([Y_0;Z])-F(U(a))=(ma_j^2-1)t^2+\tfrac12t^4<0
\]
for all sufficiently small positive \(t\). The quadratic coefficient is negative, establishing a feasible negative-curvature direction.

**Critical phase.** Suppose \(h(a)=1\), and choose \(j\) with \(ma_j^2=1\). For every feasible first-order direction \(H=[P;Q]\) at \(U(a)\), the rows of \(Q\) must be nonnegative, while \(P\) is unrestricted. The exact second-variation coefficient is
\[
 \tfrac12D^2F(U(a))[H,H]=\tfrac12\|Y_0P^{\mathsf T}+PY_0^{\mathsf T}\|_F^2+\|Y_0Q^{\mathsf T}\|_F^2-\|Q\|_F^2\ge0,
\]
since \(\|Y_0Q^{\mathsf T}\|_F^2\ge m a_{\min}^2\|Q\|_F^2=\|Q\|_F^2\). Thus the constrained first- and second-order necessary conditions hold. To exhibit genuine higher-order descent, choose \(\ell\ne j\) and a small \(\delta>0\). Construct a positive unit vector \(a'\) by setting
\[
 (a'_j)^2=a_j^2-\delta/m,\qquad (a'_{\ell})^2=a_{\ell}^2+\delta/m,
\]
and retaining the other squared coordinates. Set \(Y=\mathbf1_m(a')^{\mathsf T}\), and give one row of \(Z\) the value \(\sqrt\delta\,e_j^{\mathsf T}\), keeping all other rows zero. Then \(U=[Y;Z]\to U(a)\), whereas (1) gives the exact strict decrease
\[
 F(U)-F(U(a))=\bigl(m(a'_j)^2-1\bigr)\delta+\tfrac12\delta^2=-\tfrac12\delta^2<0.
\]
This proves failure of local minimality despite second-order stationarity.

**Existence and sharp margin.** For every positive unit vector \(a\), \(\min_j a_j^2\le1/r\), with equality only at \(a=\mathbf1_r/\sqrt r\). Hence \(h(a)>1\) is possible exactly when \(m>r\), and the balanced vector uniquely maximizes the entrywise certificate margin \(a_{\min}-1/\sqrt m\). For \(m>r\), the positive sphere also contains profiles with \(h(a)<1\), establishing distinct stationary types on a single Gram fiber.

## Verification

The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. Execute `python verify.py`. It verifies (1) on 420 randomly generated small rational block matrices, the exact one-row perturbation law on 120 rational cases, the critical quartic identity, and the lower-bound certificate on 600 further nonnegative instances (1141 exact-rational checks total). The analytic arguments above, not finite tests, prove the statement for all permitted sizes and every positive unit orientation.

## Relationship to prior work

Zhang's full-text Theorem 4 and Lemma 12 (2025 arXiv preprint, 2026 journal article) prove existence of a spurious local minimum for the special **balanced** vector \(a=\mathbf1_r/\sqrt r\) when \(m>r\). This special case is fully credited. The present statement classifies *every* strictly positive unit orientation on that collapsed Gram fiber, supplies the necessary and sufficient orientation threshold, distinguishes the semidefinite-Hessian yet non-minimizing critical boundary, and gives a quantitative perturbation certificate. Neither the balanced example nor its sufficient condition implies that other Gram-equivalent stationary factorizations are saddles. General analyses of symmetric nonnegative factorization algorithms and unconstrained low-rank landscapes address different results and do not supply this classification in their inspected statements.

## Limitations

This is a family-specific landscape classification and does not imply all nonnegative factorizations share the same threshold. The orientation margin is for the explicit entrywise **certificate** (2), not a computed maximal Euclidean basin radius. No claim is made about asymptotic behavior of a particular optimization algorithm or about robustness under partial observation or noise. Unindexed equivalent formulations or extensions of the earlier block proof remain possible; no independent review has been performed.

## References

1. Richard Y. Zhang, *Nonnegative Low-rank Matrix Recovery Can Have Spurious Local Minima*, arXiv:2505.03717 (first posted 2025-05-06), especially Theorem 4 and Lemma 12; *Optimization Letters* **20** (2026), 683–704, DOI:10.1007/s11590-026-02290-0.
2. Koby Hayashi, Sinan G. Aksoy, Grey Ballard and Haesun Park, *Randomized Algorithms for Symmetric Nonnegative Matrix Factorization*, *SIAM Journal on Matrix Analysis and Applications* **46** (2025), 584–625, DOI:10.1137/24M1638355 (related numerical setting, not a landscape theorem).
3. Srinadh Bhojanapalli, Behnam Neyshabur and Nathan Srebro, *Global Optimality of Local Search for Low Rank Matrix Recovery*, arXiv:1605.07221 (unconstrained landscape context).
