# A uniformity obstruction for equilibrium rates under arbitrary capital-supply paths

## Finding

The continuous-time overlapping-generations model in Chen, Ellingsrud, Harang, Irarrazabal, and Mayorcas admits a simple necessary regularity bound that rules out a uniform-in-capital-profile reading of Theorem 5.13. Fix a lifespan \(L>0\), a rate bound \(\|r\|_{\infty}\le M\), constant income \(\eta_0\ge 0\), initial wealth \(w_0\), and a consumption policy satisfying \(0\le c_t^b\le\kappa\). Under a stationary smooth demographic flow with age density
\[
\rho(a)=\frac{6a(L-a)}{L^3},\quad 0\le a\le L,
\]
every equilibrium aggregate-wealth path
\[
K(t)=\int_{t-L}^{t}\rho(t-b)\mathbb E[w_t^b]\,db
\]
must satisfy
\[
\|K'\|_{\infty}\le \frac{3B}{L}+MB+\eta_0+\kappa,\qquad
B=(|w_0|+L(\eta_0+\kappa))e^{ML}.
\]
The right-hand side depends on the fixed primitives, \(L\), and \(M\), but not on the target path \(K\). In contrast, for every \(\omega>0\), the positive \(C^1\) capital profile
\[
K_\omega(t)=1+\frac12\sin(\omega t)
\]
has \(\inf_t K_\omega(t)=1/2\) and \(\|K_\omega'\|_\infty=\omega/2\). Taking \(\omega\) larger than twice the bound gives a contradiction. Thus a single lifespan and a single interest-rate bound cannot work for all positive \(C^1\) capital profiles.

## Assumptions and scope

Use the cohort wealth equation from the source model,
\[
\frac{d}{dt}w_t^b=r_t w_t^b+\eta_t^b-c_t^b,\qquad t\in[b,b+L].
\]
Assume \(r\) is deterministic and continuous with \(\|r\|_\infty\le M\); each cohort starts from \(w_b^b=w_0\); income is the deterministic constant \(\eta_t^b=\eta_0\ge0\); and \(0\le c_t^b\le\kappa\). Use the stationary age-density flow \(\nu_t(db)=\rho(t-b)\,db\) on \([t-L,t]\), with \(\rho(a)=6a(L-a)/L^3\). This density is nonnegative, integrates to one, vanishes at both endpoints, and satisfies \(\|\rho'\|_{L^1(0,L)}=3/L\). Extended by zero outside \([0,L]\), it is Lipschitz and gives a regular age-density flow. These choices are a bounded-primitives special case of the model's wealth dynamics and bounded-consumption assumption.

The claim concerns only uniformity over the exogenous capital-supply profile: it does not assert that an equilibrium fails to exist for a particular fixed \(K\), nor does it disprove a version of the existence theorem whose lifespan or rate bound is allowed to depend on \(K\), for example through a bound on \(\|K'\|_\infty\).

## Proof

First, variation of constants and Grönwall's inequality give, for every cohort \(b\) and every \(t\in[b,b+L]\),
\[
|w_t^b|\le |w_0|+\int_b^t\big(M|w_s^b|+\eta_0+\kappa\big)\,ds
\le (|w_0|+L(\eta_0+\kappa))e^{ML}=B.
\]
The same bound holds for \(\mathbb E[|w_t^b|]\).

For the smooth age-density flow, differentiate under the integral. Because \(\rho(0)=\rho(L)=0\), the Leibniz boundary terms vanish, giving
\[
K'(t)=\int_{t-L}^{t}\rho'(t-b)\mathbb E[w_t^b]\,db
+\int_{t-L}^{t}\rho(t-b)\mathbb E[r_t w_t^b+\eta_0-c_t^b]\,db.
\]
The first term is bounded by \(B\|\rho'\|_{L^1(0,L)}=3B/L\). Since \(\rho\) is a probability density, the second is bounded by \(MB+\eta_0+\kappa\). Therefore
\[
|K'(t)|\le \frac{3B}{L}+MB+\eta_0+\kappa
\]
for every \(t\), proving the necessary derivative bound.

Now suppose one fixed pair \((L,M)\), determined only by the demographic flow, initial wealth, income, utility bounds, and a rate-bound parameter, worked for every positive \(C^1\) target capital profile. The preceding inequality would give the same finite upper bound for \(\|K'\|_\infty\) for all such profiles. But \(K_\omega(t)=1+\frac12\sin(\omega t)\) is positive and \(C^1\), while \(\|K_\omega'\|_\infty=\omega/2\) is unbounded as \(\omega\to\infty\). Choosing \(\omega\) above twice the proposed bound is a contradiction. The proof is exact and uses no numerical approximation.

## Verification

The inequality is obtained directly from the cohort wealth equation, a Grönwall bound, and differentiation of the smooth age-weighted aggregate. The sinusoidal family is an explicit counterexample to uniformity: positivity holds because \(K_\omega(t)\in[1/2,3/2]\), and differentiation gives \(K_\omega'(t)=(\omega/2)\cos(\omega t)\), hence \(\|K_\omega'\|_\infty=\omega/2\).

The verified conclusion is limited to the uniformity claim. It does not establish existence or uniqueness for any particular high-frequency profile, and it does not rule out a corrected theorem with \(K\)-dependent constants or additional regularity restrictions on \(K\).

## Relationship to prior work

Chen et al. state Theorem 5.13 for a positive \(C^1\) capital profile \(K\) while displaying the lifespan dependency as \(\bar L_1(\nu,w_0,\eta,\kappa,\lambda,R)\) and giving an interest-rate bound whose displayed right-hand side also omits \(K\). The source's cohort wealth equation and aggregate-wealth definition yield the derivative bound above. The result isolates a necessary dependence on the target path's time-variation; it is not a replacement for the paper's local existence proof.

Semantic literature-database searches for the paper title, overlapping-generations equilibrium, FBSDE interest-rate existence, and natural borrowing limits returned no directly equivalent result. The nearest returned finance and population-model records concern different systems and do not imply this capital-profile obstruction. Search failure alone is not a novelty proof; the mathematical comparison here is the explicit derivative inequality against the stated uniform dependency.

## Limitations

The result assumes a stationary smooth age-density flow, bounded constant income, bounded nonnegative consumption, and a uniformly bounded interest rate. These assumptions suffice to disprove a universal \(K\)-independent bound; the argument does not characterize the weakest possible regularity assumptions for a corrected equilibrium theorem. If the source's displayed parameter list was intended to include \(K\) implicitly, the result identifies the necessary missing dependence rather than establishing an authorial error.

## References

1. Cangxiong Chen, Sigmund Ellingsrud, Fabian N. Harang, Alfonso Irarrazabal, and Avi Mayorcas, “Stochastic Analysis of Overlapping Generations Models Under Incomplete Markets,” first submitted 5 September 2025, arXiv:2509.05170, version 2 dated 28 September 2026. Primary source: https://arxiv.org/abs/2509.05170. Full text: https://arxiv.org/html/2509.05170v2.
