# Exact all-window noise threshold and correlation reversal in stochastic moving-average feedback

## Finding

**Theorem.** Fix an integer \(m\ge2\), a real mean multiplier \(a\), variance \(v\ge0\), and admissible within-step coefficient correlation \(-1/(m-1)\le\rho\le1\). Let
\[
 x_{n+1}=\frac1m\sum_{j=0}^{m-1}(a+\xi_{n,j})x_{n-j}+\epsilon_n.
\]
The random coefficient vectors are independent and identically distributed over \(n\), independent of the initial state and innovations, have zero mean, covariance \(\operatorname{Cov}(\xi_{n,i},\xi_{n,j})=v\) for \(i=j\) and \(v\rho\) otherwise. The independent, identically distributed innovations have mean zero and variance \(\tau^2>0\). Only these finite second moments are assumed; Gaussianity is unnecessary.

The homogeneous iteration (innovations set to zero) is mean-square asymptotically stable for every deterministic initial state **if and only if**
\[
 -m<a<1,\qquad 0\le v<v_*(m,a,\rho)
 :=\frac{m(1-a)(m+a)}{m-(m-1)a(1-\rho)}.
\]
In that regime a unique causal square-integrable stationary solution exists, whose state-vector covariance has constant diagonal \(u\), and common off-diagonal \(ur\), where
\[
 r=\frac{a}{m-(m-1)a},\qquad
 u=\frac{\tau^2m\,[m-(m-1)a]}{m(1-a)(m+a)-v\,[m-(m-1)a+(m-1)\rho a]}.
\]
In particular, every stationary autocorrelation at lags \(1,\ldots,m-1\) equals the *same* value \(r\), independent of \(v\) and \(\rho\). If \(a>0\), minimum stationary variance and maximum admissible coefficient-noise variance occur at \(\rho=-1/(m-1)\), when \(v_*=m+a\); if \(a<0\), both occur at \(\rho=1\), when \(v_*=(1-a)(m+a)\). When \(a=0\), all correlations give the same stability threshold and stationary variance.

## Assumptions and scope

The indexed initial values \(x_0,x_{-1},\ldots,x_{1-m}\) are any deterministic real numbers with finite magnitude. The entire collection of time-slice random coefficient vectors is independent over time, and each slice is independent of the new innovation and of the past. The coefficient vector need not have independent coordinates: their equicorrelation is prescribed, including singular endpoint covariance matrices. The innovations need only a finite positive variance. Mean-square stability means \(\mathbb E\Vert Z_n\Vert_2^2\to0\) for every deterministic initial vector, with \(Z_n=(x_n,\ldots,x_{n-m+1})^\top\) and with innovations suppressed. Stability at either boundary is **excluded**.

All inequalities and equalities above refer to exact arithmetic and scalar random maps; matrix-valued multipliers, temporally correlated noise, non-equal averaging weights, and higher moments are not covered.

## Proof

Let \(e_1=(1,0,\ldots,0)^\top\) and write \(Z_{n+1}=B_nZ_n+e_1\epsilon_n\), where the first row of the companion matrix \(B_n\) equals \((a+\xi_{n,j})/m\) and the subdiagonal entries equal one. Define the positive linear second-moment map \(\mathcal K(P)=\mathbb E[B_nPB_n^\top]\) on symmetric \(m\times m\) matrices.

**Deterministic first-moment interval.** The mean companion matrix has characteristic polynomial
\[
 p_a(z)=z^m-\frac{a}{m}\sum_{j=0}^{m-1}z^j.
\]
If \(0\le a<1\) and \(|z|\ge1\), the root equation yields \(|z|^m\le a|z|^m\), a contradiction. If \(-m<a<0\), write \(q=-a/m\in(0,1)\). Every root of \(p_a\) satisfies \(z^{m+1}=(1-q)z^m+q\). Taking absolute values rules out \(|z|>1\); equality \(|z|=1\) forces \(z=1\), which is not a root of \(p_a\). Conversely, \(a\ge1\) yields a real root of modulus at least one by \(p_a(1)=1-a\le0\), and \(a\le-m\) gives a root of modulus at least one from the product of the root moduli \(|a|/m\ge1\). Thus the mean system is asymptotically stable exactly for \(-m<a<1\). Because the magnitude squared of the mean is bounded by the second moment, this interval is necessary for mean-square stability.

**A single equicorrelation Lyapunov matrix.** Assume \(-m<a<1\). Put \(d=m-(m-1)a\), \(r=a/d\) and let \(P_0\) be the matrix with diagonal entries one and all off-diagonal entries \(r\). Since \(-1/(m-1)<r<1\), \(P_0\) is positive definite. A direct second-moment calculation using \(1+(m-1)r=m/d\) gives
\[
 \mathcal K(P_0)=P_0+(F-1)e_1e_1^\top,
 \qquad F=\frac{a^2}{d}+\frac vm\left(1+(m-1)\rho r\right).
\]
The shifted off-diagonal entries agree with \(P_0\), because the mean of the new leading component paired with each old component equals \(a[1+(m-1)r]/m=r\). Algebra gives \(F<1\) exactly when \(v<v_*(m,a,\rho)\). The denominator of \(v_*\) is positive: \(d+(m-1)a\rho=m+(m-1)a(\rho-1)>0\) for the whole stated parameter domain, equivalently \(m[1+(m-1)\rho r]>0\).

If \(F\ge1\), then \(\mathcal K(P_0)\succeq P_0\), and positivity yields \(\mathcal K^n(P_0)\succeq P_0\) for all \(n\). A decomposition of \(P_0\) into deterministic rank-one outer products shows that mean-square decay cannot hold for all deterministic starting states. This proves necessity, including equality.

If \(F<1\), telescope the identity to obtain
\[
 \mathcal K^m(P_0)=P_0-(1-F)\sum_{j=0}^{m-1}\mathcal K^j(e_1e_1^\top).
\]
The sum is **positive definite**: for each particular sequence of companion matrices, the vectors \(e_1,B_1e_1,B_2B_1e_1,\ldots,B_{m-1}\cdots B_1e_1\) have a lower-triangular column arrangement with unit diagonal (the \(j\)-th vector has coordinate \(j+1\) equal to one and no later nonzero coordinates). Their outer products therefore sum to a positive-definite matrix; expectation preserves positive definiteness. Consequently \(\mathcal K^m(P_0)\prec P_0\). Positivity and finite dimensionality imply geometric decay of iterated second moments: choose \(0<c<1\) with \(\mathcal K^m(P_0)\preceq cP_0\), dominate any initial rank-one covariance by a multiple of \(P_0\), and iterate. This proves sufficiency.

**Stationarity.** For additive innovation variance \(\tau^2\), the discrete Lyapunov equation is \(P=\mathcal K(P)+\tau^2e_1e_1^\top\). Because \(\mathcal K(P_0)-P_0=(F-1)e_1e_1^\top\), the unique solution is \(P=uP_0\) with \(u=\tau^2/(1-F)\), which simplifies to the formula in the finding. Existence of a causal stationary solution follows by summing independent innovations from the infinite past; the geometric second-moment decay makes the sum converge in \(L^2\). Uniqueness among causal square-integrable stationary solutions follows from mean-square contraction.

**Correlation reversal.** Write \(v_*=m(1-a)(m+a)/[d+(m-1)a\rho]\). At fixed admissible \(m,a\) it decreases strictly with \(\rho\) for \(a>0\) and increases strictly for \(a<0\). The inverse stationary variance has the same monotonicity when \(v>0\) and the chosen correlations are in the stable regime. Evaluating at the two permissible endpoints proves all optimality claims. For \(v=0\) the stationary variance is correlation-independent, so the word *minimum* need not mean a unique minimizer.

## Verification

The accompanying standalone `CHECK.py` tests exact rational matrix identities for \(m=2,\ldots,7\), six mean multipliers per window, five permissible correlation values and six noise levels relative to the sharp threshold: 1080 exact checks, together with exact stationary Lyapunov identities in stable cases and 14 endpoint threshold checks. Its finite spectral computations provide additional diagnostics only; the proof establishes the assertions for all real admissible parameters.

Illustrations: with \(m=2\), \(a=1/2\), \(v=1\), \(\tau^2=1\), the variance is \(3/(1-\rho/2)\), hence it rises from \(2\) at \(\rho=-1\) to \(6\) at \(\rho=1\). With \(m=2\), \(a=-1\), \(v=1\), \(\tau^2=1\), it equals \(6/(1+\rho)\) for \(-1<\rho\le1\), hence *decreases* with \(\rho\); \(\rho=-1\) is precisely the instability boundary.

## Relationship to prior work

Epperlein and Wirth (arXiv:2609.21442, first publicly dated 2026-09-18) investigate deterministic moving-average iterations and spectral stability for fixed complex linear maps. Our mean multiplier \(a\) reproduces their scalar equal-window update at \(v=0\), but the within-step random coefficient covariance and its exact mean-square effects are not addressed in the available abstract. The full preprint could not be inspected, leaving a bounded bibliographic risk.

The stochastic recurrence also belongs to the long-established random-coefficient autoregression class (RCA). In particular, the Nicholls–Quinn / Andel general second-order stationarity criterion, recalled in Benmoumen, Allal, and Salhi (2019, Section 2, Theorem 1), gives an implicit Kronecker-matrix inequality for arbitrary random-coefficient autoregressions, and their Theorem 2 gives the established AR-like autocorrelation relationship. **Neither an RCA model class nor a generic spectral-radius criterion is claimed as new.** The content evaluated here is the all-window *explicit* threshold, a one-matrix sharp Lyapunov certificate, the correlation-invariant flat lag law in this structured setting, and the exact sign-dependent optimum at maximally negative versus fully reused noise. These are nontrivial evaluations of the general criterion, rather than a new general criterion. General random-coefficient AR references remain potential sources of equivalent explicit specializations.

## Limitations

The correlated stochastic model is a separate extension of the cited deterministic method; it is not asserted to be that paper's own stochastic algorithm. Results are for equal scalar averaging weights and independent coefficient *vectors over time*, with equicorrelated entries within each vector. Gaussian distribution assumptions are unnecessary, but mean-square stability does not imply pathwise almost-sure contraction at each step or uniform higher-moment bounds. The stationary formula requires strictly positive innovation variance and strictly subcritical coefficient variance. The relevant 2026 preprint's full text was unavailable; an exact previously published specialization cannot be categorically ruled out. Independent mathematical validation has not been performed.

## References

1. J. Epperlein and F. Wirth, *Moving-Average Iteration of Linear Maps*, arXiv:2609.21442, first public release 2026-09-18, https://arxiv.org/abs/2609.21442.
2. M. Benmoumen, J. Allal, and I. Salhi, *Parameter Estimation for p-Order Random Coefficient Autoregressive (RCA) Models Based on Kalman Filter*, Journal of Applied Mathematics (2019), article 8479086, https://doi.org/10.1155/2019/8479086.
3. D. F. Nicholls and B. G. Quinn, *Random Coefficient Autoregressive Models: An Introduction*, Springer, 1982 (cited for existing general RCA theory, not independently read here).
