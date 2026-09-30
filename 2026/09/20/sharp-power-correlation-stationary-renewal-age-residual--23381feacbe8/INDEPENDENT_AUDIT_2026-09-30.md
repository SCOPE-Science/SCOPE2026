# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-power-correlation-stationary-renewal-age-residual--23381feacbe8`  
**Audited source tree:** `e85b78e048ced8b443dc48a3460a3c95c3a5e300`  
**Disposition:** passed

## Correctness — PASS

PASS. At stationarity the containing interval L has the size-biased interarrival law and (A,R)=(UL,(1-U)L) with U uniform and independent. This gives E A^r=m_{r+1}/((r+1)m_1), E A^{2r}=m_{2r+1}/((2r+1)m_1), and E(A^rR^r)=B(r+1,r+1)m_{2r+1}/m_1, from which the displayed correlation formula follows. Cauchy--Schwarz gives 0<Q_r<=1 with equality only for deterministic X. Because B(r+1,r+1)<1/(r+1)^2<1/(2r+1), the correlation is strictly decreasing in Q_r, giving the stated endpoints. The two-point size-biased construction genuinely realizes every Q in (0,1): choosing P(L=M)=M^{-r} sends Q to zero as M grows, while continuity from a point mass covers intermediate values, and inverse size-biasing produces a valid positive interarrival law. I numerically rechecked the endpoint formulas for several noninteger and integer r and the asymptotics are consistent.

## Originality — PASS

PASS, narrowly scoped. The radial-uniform Schur-constant representation and raw stationary recurrence-time moment identities are prior theory and are not new here. The inspected renewal-covariance and Schur-constant papers study ordinary covariance, dependence measures, and joint moments, but I found no statement of the all-r Pearson power-correlation identification interval, its exact endpoint/extremizer classification, or the two-point attainability theorem. Because the result is a short synthesis of standard representation plus a moment-ratio extremum, older Schur-constant or l1-symmetric literature under different terminology remains a real but nondecisive originality risk.

## Scientific value — PASS

PASS. The contribution is a clean distribution-free identification region valid for every positive power, with exact attainment, sign threshold, and high-power asymptotics. It packages standard renewal structure into a reusable sharp dependence statement rather than merely reporting another raw moment formula.

## Independent checks

- Re-derived all stationary moments from the size-biased interval/uniform-location representation.
- Differentiated the correlation as a Möbius function of Q_r and checked the ordering of beta-function constants.
- Verified the two-point attainability and inverse size-biasing construction.
- Numerically checked integer and noninteger endpoint formulas and the r→infinity asymptotic signs.

## Literature evidence

- https://doi.org/10.1080/07362999408809372 — Gakis and Sivazlian (1994), classical backward/forward recurrence correlation.
- https://doi.org/10.1007/s40300-014-0045-0 — Nair and Sankaran (2014), bivariate Schur-constant equilibrium distributions from renewal theory.
- https://doi.org/10.1080/15326349.2019.1575752 — Losidis and Politis (2019), stationary covariance of recurrence times.
- https://doi.org/10.1007/s11009-020-09787-w — Losidis, Politis and Psarrakos (2021), exact results and bounds for joint tails and moments.

## Limitations

- The theorem concerns stationary recurrence times, equal positive powers, and Pearson correlation only.
- The upper endpoint is a supremum, not a maximum.
- An equivalent envelope could be implicit in older Schur-constant or l1-symmetric literature under different terminology.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
