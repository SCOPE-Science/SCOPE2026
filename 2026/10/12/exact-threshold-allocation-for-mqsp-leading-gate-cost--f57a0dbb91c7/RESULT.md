# Exact threshold allocation for MQSP leading gate cost (tie-corrected)

## Finding

Fix an integer \(m\ge1\) and positive real coefficients \(a_j,G_j,g\). The leading gate-cost allocation objective from Eq. (7.51) of Low's *Multivariate Quantum Signal Processing* is
\[
 F(r)=\left(\sum_{j=1}^m a_j r_j\right)\left(g+\sum_{j=1}^m\frac{G_j}{r_j}\right),\qquad r_j\ge1.
\]
In that application \(a_j=\lambda_j\chi_j\), the \(G_j\) are component-oracle implementation costs, and \(g\) represents known-operation work per horizon step. Put \(\rho_j=G_j/a_j\), relabel so \(\rho_{(1)}\le\cdots\le\rho_{(m)}\), and define
\[
 A_k=\sum_{i\le k}a_{(i)},\quad B_k=g+\sum_{i\le k}G_{(i)},\quad \rho_{(m+1)}=+\infty.
\]
There exists at least one \(k\in\{1,\ldots,m\}\) with
\[
 \rho_{(k)}\le \tau_k:=B_k/A_k\le\rho_{(k+1)}.
\]
**Select the smallest such \(k\)** to make the threshold index unambiguous. (The inequality can hold for more than one index at an exact tie; uniqueness of an eligible index is not asserted.) With \(\tau=\tau_k\), the **unique continuous minimizer** is
\[
 r^*_{(i)}=\begin{cases}1,&i\le k,\\ \sqrt{\rho_{(i)}/\tau},&i>k,\end{cases}
\]
and its exact cost is
\[
 \min_{r_j\ge1}F(r)=\left(\sqrt{A_kB_k}+\sum_{i>k}\sqrt{a_{(i)}G_{(i)}}\right)^2.
\]
Every eligible index represents this same optimizer and minimum; the canonical first-crossing convention merely removes ambiguity in its description. Low cost-to-weight components remain at unit delay, while those strictly above the endogenous threshold receive larger delays. Sorting costs \(O(m\log m)\) comparisons and the threshold scan is linear.

For an integer schedule the componentwise ceiling \(\widehat r_j=\lceil r^*_j\rceil\) satisfies
\[
 F(\widehat r)\le2F(r^*).
\]
The ceiling need not be the integer optimum.

## Proof

Put \(y_j=\log r_j\ge0\). Then
\[
 \log F(e^y)=\log\sum_j a_je^{y_j}+\log\left(g+\sum_jG_je^{-y_j}\right).
\]
Both summands are log-sum-exp functions, hence convex. The second is strictly convex because the exponent vectors \(0,-e_1,\ldots,-e_m\) affinely span \(\mathbb R^m\) and all associated weights are strictly positive (in particular \(g>0\)). Thus the logarithmic objective is strictly convex. It is coercive on \(y\ge0\): if any \(y_j\to+\infty\), then \(\sum_i a_i e^{y_i}\to\infty\) while the other factor stays at least \(g\). A unique minimizing vector exists, and the KKT conditions are necessary and sufficient.

Writing \(A=\sum_j a_jr_j\), \(B=g+\sum_jG_j/r_j\), and \(\tau=B/A\), the derivative in coordinate \(r_j\) is
\[
 \partial_{r_j}F=a_jB-AG_j/r_j^2.
\]
If \(r_j>1\), stationarity gives \(r_j^2=\rho_j/\tau\). If \(r_j=1\), the one-sided derivative is nonnegative precisely when \(\rho_j\le\tau\). Therefore the clamped coordinates form an initial segment of the sorted ratios; coordinates at equality \(\rho_j=\tau\) necessarily have \(r_j=1\) and may be placed on either side of the formal index.

Assume the initial segment is indexed through \(k\), and set \(S_k=\sum_{i>k}\sqrt{a_{(i)}G_{(i)}}\). At the KKT point,
\[
 A=A_k+S_k/\sqrt\tau,\qquad B=B_k+\sqrt\tau\,S_k.
\]
Substitution into \(\tau=B/A\) cancels the common free-coordinate term and gives \(\tau=B_k/A_k\). The KKT inequalities are exactly \(\rho_{(k)}\le\tau\le\rho_{(k+1)}\).

To find one eligible index, start at \(k=1\). Since \(B_1/A_1=\rho_{(1)}+g/a_{(1)}>\rho_{(1)}\), either the first upper inequality holds or \(\tau_1>\rho_{(2)}\). In the latter case, the recurrence
\[
 \tau_{k+1}=\frac{A_k\tau_k+a_{(k+1)}\rho_{(k+1)}}{A_k+a_{(k+1)}}
\]
shows that \(\tau_{k+1}\) lies strictly between \(\rho_{(k+1)}\) and \(\tau_k\). Hence at the first index with \(\tau_k\le\rho_{(k+1)}\) the lower inequality also holds. Such an index exists no later than \(m\), because \(\rho_{(m+1)}=\infty\). Taking the first index defines a canonical \(k\). The KKT conditions and strict convexity prove uniqueness of \(r^*\), **not uniqueness of every admissible index**. At a tie \(\tau_k=\rho_{(k+1)}\), consecutive eligible indices can describe the same optimizer. For instance \(m=2\), \(a=(1,1)\), \(G=(1,3)\), \(g=2\) gives \(\tau_1=\tau_2=3\) and both \(k=1\) and \(k=2\) satisfy the inequalities; the unique optimizer is \((1,1)\).

Using the expressions for \(A\) and \(B\), and \(B_k=\tau A_k\), gives
\[
 AB=\left(\sqrt{A_kB_k}+S_k\right)^2.
\]
For rounding, \(r_j^*\ge1\) implies \(\lceil r_j^*\rceil\le r_j^*+1\le2r_j^*\). The linear factor in \(F\) increases by at most two; the reciprocal factor cannot increase, so the asserted factor-two bound follows.

## Scope, verification and limitations

This solves only the positive, lower-bounded continuous leading gate-cost proxy in Low's Eq. (7.51). It neither optimizes the full precision-aware geometric program (7.54) nor resolves analytic-domain restrictions, address-width feedback, conditioning variables, finite synthesis precision, floor-valued oracle counts, or total circuit-cost optimality. Positivity of all \(a_j,G_j,g\) is essential to strict convexity. Exact equality of a cost-to-weight ratio and the threshold is the boundary at which multiple formal indices may be eligible; the actual delays remain unique.

A finite deterministic verifier checks threshold construction, KKT signs, product identity, and ceiling inequality at selected input coefficients. These checks are corroborative; the above proof establishes the all-positive-coefficient theorem. The analytic tie example independently detects the former erroneous claim that the eligible index must always be unique.

## Relationship to prior work

Low, arXiv:2610.01125v1, Eq. (7.51), isolates the same leading gate-cost tradeoff and offers a universal-constant allocation in Eq. (7.53) related to Eq. (7.52); the source treats the richer Eq. (7.54) as a geometric program and has a different earlier weighted-delay lemma (Lemma 3.12). The present statement gives an exact optimizer, cost, and explicit ceiling guarantee for the lower-bounded leading objective, not a claim to optimize (7.54). Jing, Wang, Yu, and Zhang, arXiv:2610.03393v1, address optimal per-variable query counts in a different multivariate-polynomial access model without this delay/known-gate tradeoff. Ito, Mori, Sakamoto, and Fujii, *Quantum* 10 (2026), 2102, study multivariate-QSP polynomial realizability instead. A generic convex resource-allocation or water-filling treatment under different terminology could independently imply this closed form; originality remains best-of-knowledge.

## References

1. G. H. Low, *Multivariate Quantum Signal Processing*, arXiv:2610.01125v1 (2026), especially Lemma 3.12 and Eqs. (7.51)–(7.54).
2. M. Jing, X. Wang, Z. Yu, and L. Zhang, *Multivariate quantum signal processing with optimal query complexity*, arXiv:2610.03393v1 (2026).
3. Y. Ito, H. Mori, K. Sakamoto, and K. Fujii, *Polynomial time constructive decision algorithm for multivariable quantum signal processing*, *Quantum* 10 (2026), 2102.
