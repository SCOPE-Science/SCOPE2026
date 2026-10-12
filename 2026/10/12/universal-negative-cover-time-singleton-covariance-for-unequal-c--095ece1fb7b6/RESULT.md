# Universal negative cover-time–singleton covariance for unequal coupon probabilities

## Finding

**Theorem.** Fix an integer \(m\ge2\) and \(p_i>0\), \(1\le i\le m\), with \(\sum_{i=1}^m p_i=1\). Draw independent coupon types with probabilities \(p_i\) until every type has appeared. Let \(N\) be the total number of draws, including the final new type, and let \(S\) count types represented exactly once among those draws. Then
\[
\operatorname{Cov}(N,S)<0.
\]
More precisely, in a rate-one Poissonized version, let \(T\) be the time of the last first arrival. For every \(t>0\), the conditional covariance \(\operatorname{Cov}(N,S\mid T=t)\) is strictly negative, \(\mathbb E[N\mid T=t]\) is strictly increasing in \(t\), and \(\mathbb E[S\mid T=t]\) is strictly decreasing in \(t\). These three properties imply the unconditional inequality.

## Assumptions and scope

All draws are independent, coupon probabilities are strictly positive and time-independent, and the number of types is finite. The stopping rule is first complete coverage (one copy of each type suffices). The count \(S\) includes the last newly appearing coupon, which necessarily occurs exactly once at stopping. The formula concerns *discrete draw count* \(N\), although the proof conditions on an auxiliary continuous cover time. Strict positivity excludes inaccessible coupon types; for one type, both statistics are constant and covariance is zero.

## Proof

**Poissonization and the conditional law.** Realize the label sequence as the marks of a rate-one Poisson process, independently marked with probabilities \(p_i\). Poisson thinning produces independent processes of rates \(p_i\); write \(T_i\) for the first event time of process \(i\), \(T=\max_iT_i\), and \(J\) for the almost surely unique index attaining the maximum. The number of all points through \(T\) is distributed exactly as the original discrete coupon count \(N\), and the number of streams containing exactly one point through \(T\) is \(S\).

For fixed \(t>0\) let
\[
 x_i=p_i t,\qquad
 q_i(t)=\frac{x_i}{e^{x_i}-1},\qquad
 a_i(t)=\frac{x_i}{1-e^{-x_i}}=x_i+q_i(t),\qquad Q(t)=\sum_iq_i(t).
\]
Conditional on \(T=t,J=j\), the \(j\)-th stream has one point, while the counts of the other streams are independent Poisson variables with means \(x_i\), each conditioned to be positive. Such a zero-truncated Poisson variable has mean \(a_i(t)\), probability \(q_i(t)\) of equaling one, and covariance with its single-appearance indicator equal to \(q_i(t)(1-a_i(t))<0\). Therefore
\[
\begin{aligned}
 \mathbb E[N\mid T=t,J=j]&=1+\sum_{i\ne j}a_i(t),\\
 \mathbb E[S\mid T=t,J=j]&=1+\sum_{i\ne j}q_i(t),\\
 \operatorname{Cov}(N,S\mid T=t,J=j)&=\sum_{i\ne j}q_i(t)(1-a_i(t))<0.
\end{aligned}
\]
Here \(m\ge2\) makes the last sum strictly negative.

**Mixing the last type.** The joint density of \(T\) and \(J=j\) is
\[
 p_j e^{-p_jt}\prod_{i\ne j}(1-e^{-p_it}).
\]
Cancelling common factors shows that the conditional weights are
\[
 w_j(t)=\mathbb P(J=j\mid T=t)=\frac{q_j(t)}{Q(t)}.
\]
For positive \(x\), the functions \(q(x)=x/(e^x-1)\) and \(a(x)=x/(1-e^{-x})\) are respectively strictly decreasing and strictly increasing. Consequently, for any weights \(w_j>0\),
\[
 \operatorname{Cov}_w(a_j(t),q_j(t))
 =\frac12\sum_{i,j}w_iw_j(a_i-a_j)(q_i-q_j)\le0.
\]
The law of total covariance over \(J\), conditional on \(T=t\), gives the explicit strictly negative decomposition
\[
 \operatorname{Cov}(N,S\mid T=t)
 =\sum_i(1-w_i)q_i(1-a_i)
   +\operatorname{Cov}_w(a_i,q_i)<0.
\]
The first term is strictly negative and the second nonpositive.

**Opposite conditional regressions in cover time.** Put \(R(t)=\sum_iq_i(t)^2\). The conditional expectations are
\[
 s(t):=\mathbb E[S\mid T=t]=1+Q(t)-\frac{R(t)}{Q(t)},
\quad
 n(t):=\mathbb E[N\mid T=t]=1+\sum_i a_i(t)-\sum_iw_i(t)a_i(t).
\]
For every \(k\),
\[
 \frac{\partial}{\partial q_k}\left(Q-\frac{R}{Q}\right)
 =\frac{(Q-q_k)^2+\sum_{i\ne k}q_i^2}{Q^2}>0.
\]
Each \(q_k'(t)<0\), hence \(s'(t)<0\). Also \(a_i'(t)>0\), and direct logarithmic differentiation gives
\[
 \frac{q_i'(t)}{q_i(t)}=\frac{1-a_i(t)}{t},
 \qquad
 w_i'(t)=\frac{w_i(t)}t\left(\sum_jw_j(t)a_j(t)-a_i(t)\right).
\]
It follows that
\[
 n'(t)=\sum_i(1-w_i(t))a_i'(t)
   +\frac{\operatorname{Var}_{w(t)}(a_i(t))}{t}>0,
\]
since \(m\ge2\) gives \(0<w_i(t)<1\).

Finally, \(T\) has a nondegenerate continuous distribution and finite moments of all orders because all rates are positive. If \(T'\) is an independent copy, the opposite strict monotonicities imply
\[
 \operatorname{Cov}(n(T),s(T))
 =\frac12\mathbb E[(n(T)-n(T'))(s(T)-s(T'))]<0.
\]
The full law of total covariance now yields
\[
 \operatorname{Cov}(N,S)
 =\mathbb E[\operatorname{Cov}(N,S\mid T)]
   +\operatorname{Cov}(n(T),s(T))<0,
\]
proving the theorem for every positive probability vector.

## Verification

The independent finite-state program `verify_unequal_coupon.py` solves first-step equations over coupon-count states truncated at \(0,1,2\), using exact rational arithmetic. Run `python3 verify_unequal_coupon.py` from the directory containing this result. It exhaustively checks symmetric representatives of three-level integer weight vectors for \(2\le m\le5\), additional strongly unequal vectors, and the known uniform benchmark. It reports **59** exact covariance comparisons with no failures. The analytic proof above, not this finite census, establishes the theorem for arbitrary real weights and arbitrary finite \(m\).

For uniform probabilities only, the independent calculation gives
\[
 \mathbb E[N]=m H_m,\qquad \mathbb E[S]=H_m,\qquad
 \operatorname{Cov}(N,S)=m\bigl(H_m^{(2)}-H_m\bigr),
\]
where \(H_m=\sum_{k=1}^m k^{-1}\) and \(H_m^{(2)}=\sum_{k=1}^m k^{-2}\). This is a **known-joint-distribution corollary**, not a claimed novel part of the theorem: Myers and Wilf (2003) give the complete joint law of \(N\) and \(S\) in the uniform case.

## Relationship to prior work

Myers and Wilf (2003, arXiv:math/0304229v1, Section 4, equation (44)) explicitly derive the joint distribution of cover length and singleton count when every coupon is equally likely; that statement covers every uniform-case moment, including the uniform covariance above. It does **not** cover nonuniform probability vectors. Brown, Peköz, and Ross (2008, Proposition 1) work with unequal sampling probabilities and give cover-time laws, last-type laws, and marginal terminal counts for each coupon, but not the joint mixed moment of \(N\) with the total singleton count or its universal strict sign. Anceaume, Busnel, and Sericola (2014, arXiv:1402.5245v1) give arbitrary-probability cover-time distributions and moments, without this terminal singleton covariance. Zoroa et al. (2016, arXiv:1608.00155v1) study fixed-draw occupancy and unequal-probability coverage speed, not this stopping-time mixed dependence.

These are comparisons of the **statements and information implied**, not titles alone. In particular, separate marginal laws do not determine this covariance, whereas the uniform joint law does determine it for the uniform subcase. Historical coverage by a different broader nonuniform joint-law theorem is possible and has not been excluded by exhaustive global literature review.

## Limitations

No explicit closed form or optimal quantitative lower bound is claimed for arbitrary \(p\). The conditional monotonicity concerns the **auxiliary continuous cover time**, not conditional expectations at each *discrete* value of \(N\); no discrete regression theorem is claimed. The result does not address unequal probabilities changing over time, dependent draws, coupon quotas above one, zero-probability types, or infinite alphabets. The finite tests do not establish the theorem outside their finite parameter sets.

## References

- N. Zoroa, E. Lesigne, M.-J. Fernández-Sáez, P. Zoroa, and J. Casas, *The coupon collector urn model with unequal probabilities in ecology and evolution*, arXiv:1608.00155v1, first posted 2016-07-30; primary MSC 60C05.
- E. Anceaume, Y. Busnel, and B. Sericola, *New results on a generalized coupon collector problem using Markov chains*, arXiv:1402.5245v1, first posted 2014-02-21; Journal of Applied Probability 52 (2015), 405–418.
- M. Brown, E. A. Peköz, and S. M. Ross, *Coupon Collecting*, Probability in the Engineering and Informational Sciences 22 (2008), 221–229, DOI:10.1017/S0269964808000132.
- A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1, first posted 2003-04-16; SIAM Journal on Discrete Mathematics 17 (2003), 1–17.
