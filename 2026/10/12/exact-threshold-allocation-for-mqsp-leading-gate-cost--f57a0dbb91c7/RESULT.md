# Exact threshold allocation for MQSP leading gate cost
## Finding
For the leading gate-cost allocation problem in Eq. (7.51) of Low's *Multivariate Quantum Signal Processing*, let \(m\ge 1\), let \(a_j>0\), \(G_j>0\), and \(g>0\), and define
\[
F(r)=\left(\sum_{j=1}^m a_j r_j\right)\left(g+\sum_{j=1}^m \frac{G_j}{r_j}\right),\qquad r_j\ge 1.
\]
In the source application \(a_j=\lambda_j\chi_j\), \(G_j\) is the controlled implementation cost of the corresponding component oracle, and \(g=g_{\mathrm{step}}\) bounds known-operation work per horizon step.

Set \(\rho_j=G_j/a_j\) and relabel so that
\[
\rho_{(1)}\le\rho_{(2)}\le\cdots\le\rho_{(m)}.
\]
For \(1\le k\le m\), put
\[
A_k=\sum_{i=1}^k a_{(i)},\qquad B_k=g+\sum_{i=1}^kG_{(i)},
\]
and set \(\rho_{(m+1)}=+\infty\). There is a unique index \(k\) satisfying
\[
\rho_{(k)}\le \frac{B_k}{A_k}\le \rho_{(k+1)}.
\]
With \(\tau=B_k/A_k\), the unique minimizer is
\[
r^*_{(i)}=1\quad(1\le i\le k),\qquad
r^*_{(i)}=\sqrt{\frac{\rho_{(i)}}{\tau}}\quad(k<i\le m),
\]
and
\[
\min_{r_j\ge1}F(r)=
\left(\sqrt{A_kB_k}+\sum_{i=k+1}^m\sqrt{a_{(i)}G_{(i)}}\right)^2.
\]
Thus the exact continuous solution has a water-filling-type threshold: low cost-to-weight components remain at unit delay, while only components with \(G_j/a_j>\tau\) are delayed.

If an integer schedule is needed, componentwise upward rounding satisfies
\[
\widehat r_j=\lceil r_j^*\rceil,
\qquad
F(\widehat r)\le 2F(r^*).
\]
The threshold can be located after sorting the \(m\) ratios, so the closed-form allocation requires \(O(m\log m)\) comparisons plus linear arithmetic.

## Assumptions and scope
All coefficients \(a_j\), \(G_j\), and \(g\) are strictly positive. The result solves exactly the continuous leading gate-cost objective displayed as Eq. (7.51) in arXiv:2610.01125v1. In that application \(a_j=\lambda_j\chi_j\).

The result does **not** claim an exact optimizer for the source's full precision-aware objective (7.54). In particular, it does not remove the need to check analytic-domain restrictions, the common conditioning variable, address-width feedback, finite synthesis accuracy, or the exact floor-valued oracle counts. It also does not claim that ceiling the continuous optimizer is the optimal integer schedule; only the stated factor-two guarantee for the leading objective is proved.

## Proof
Write
\[
A(r)=\sum_j a_jr_j,\qquad B(r)=g+\sum_j\frac{G_j}{r_j},
\]
so \(F=A B\). Introduce logarithmic variables \(y_j=\log r_j\ge0\). Then
\[
\log F(e^y)=\log\!\left(\sum_j a_je^{y_j}\right)
+\log\!\left(g+\sum_jG_je^{-y_j}\right).
\]
This is a convex function of \(y\). It is in fact strictly convex: a nonconstant direction has positive variance in the first log-sum-exp term, while a constant nonzero direction has positive variance in the second term because that term also contains the positive constant \(g\). Hence the Karush--Kuhn--Tucker conditions identify the unique global minimizer.

Let
\[
\tau=\frac{B(r^*)}{A(r^*)}.
\]
For a coordinate with \(r_j^*>1\), stationarity gives
\[
a_jB(r^*)-\frac{A(r^*)G_j}{(r_j^*)^2}=0,
\]
so
\[
(r_j^*)^2=\frac{G_j/a_j}{\tau}=\frac{\rho_j}{\tau}.
\]
At the lower boundary \(r_j^*=1\), the one-sided derivative must be nonnegative, which is equivalent to \(\rho_j\le\tau\). Therefore the clamped coordinates are exactly an initial segment after sorting by \(\rho_j\).

Suppose this initial segment has size \(k\), and define
\[
S_k=\sum_{i=k+1}^m\sqrt{a_{(i)}G_{(i)}}.
\]
For the free coordinates,
\[
r^*_{(i)}=\sqrt{\rho_{(i)}/\tau}.
\]
Consequently
\[
A(r^*)=A_k+\frac{S_k}{\sqrt\tau},
\qquad
B(r^*)=B_k+\sqrt\tau\,S_k.
\]
The definition \(\tau=B(r^*)/A(r^*)\) cancels the common \(\sqrt\tau S_k\) term and gives
\[
\tau=\frac{B_k}{A_k}.
\]
The KKT boundary conditions are therefore exactly
\[
\rho_{(k)}\le\frac{B_k}{A_k}\le\rho_{(k+1)}.
\]
Existence and uniqueness of \(k\) follow directly from the recurrence
\[
\frac{B_{k+1}}{A_{k+1}}
=\frac{A_k(B_k/A_k)+a_{(k+1)}\rho_{(k+1)}}{A_k+a_{(k+1)}}.
\]
Starting from \(B_1/A_1>\rho_{(1)}\), take the first \(k\) for which \(B_k/A_k\le\rho_{(k+1)}\); before that point the recurrence keeps \(B_k/A_k>\rho_{(k)}\), and after the crossing the full two-sided condition cannot recur at a later index.

Finally,
\[
A(r^*)B(r^*)=
\left(\sqrt{A_kB_k}+S_k\right)^2,
\]
which proves the minimum formula.

For integerization, \(r_j^*\ge1\) implies
\[
\lceil r_j^*\rceil\le r_j^*+1\le2r_j^*.
\]
Hence the first factor in \(F\) increases by at most a factor two, while the second factor cannot increase under upward rounding. Thus
\[
F(\lceil r^*\rceil)\le2F(r^*).
\]

## Verification
The accompanying `artifacts/verify.py` reconstructs the threshold solution for deterministic positive test families. It checks the threshold inequalities, evaluates the closed-form minimum against the product at the reconstructed optimizer, verifies the KKT signs, and checks the factor-two ceiling bound. Its finite tests are corroborative only; the proof above establishes the statement for all positive coefficients.

## Relationship to prior work
Low, arXiv:2610.01125v1, Eq. (7.51), isolates exactly this leading gate-cost tradeoff. The paper then gives a constructive schedule whose cost is within a universal constant of the proxy in Eq. (7.52), using Eq. (7.53), and treats the precision-aware extension (7.54) as a geometric program. The paper does not state the threshold index, the exact minimum of (7.51), or the factor-two ceiling guarantee obtained by rounding its exact continuous optimizer.

The same paper's Lemma 3.12 gives a different unconstrained weighted-delay allocation and explicitly notes that integer delays require scaling and rounding. The present result addresses the lower-bounded gate-cost objective appearing later in the downfolding resource analysis, where the additive known-operation cost \(g\) breaks the common-scale invariance and creates the threshold.

Jing, Wang, Yu, and Zhang, arXiv:2610.03393v1, study optimal per-variable query counts for multivariate polynomial transformations, including commuting unitaries. Their query model does not contain Eq. (7.51)'s delay-versus-known-gate tradeoff and does not imply the threshold allocation above. Earlier multivariable-QSP characterization work likewise concerns realizable polynomial transformations rather than this resource-allocation objective.

## Limitations
The exact formula applies only to the leading positive objective (7.51). The source's full objective (7.54) contains additional precision and conditioning variables and remains a genuine geometric program; the present threshold need not solve it. Address width depends on the resulting schedule in the full circuit accounting. Exact floor-valued oracle counts can also make a different integer schedule preferable. No claim of information-theoretic optimality for total circuit cost is made.

## References
1. G. H. Low, *Multivariate Quantum Signal Processing*, arXiv:2610.01125v1 (first public 2026-10-01), especially Lemma 3.12 and Eqs. (7.51)--(7.54).
2. M. Jing, X. Wang, Z. Yu, and L. Zhang, *Multivariate quantum signal processing with optimal query complexity*, arXiv:2610.03393v1 (2026).
3. Y. Ito, H. Mori, K. Sakamoto, and K. Fujii, *Polynomial time constructive decision algorithm for multivariable quantum signal processing*, Quantum 10, 2102 (2026), doi:10.22331/q-2026-05-12-2102.
