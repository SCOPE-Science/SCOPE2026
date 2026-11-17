---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For deterministic positive dyadic weights w_{2^k}=2^{beta k}, other w_j=1, the marginal insertion depth law has Bernoulli factors p_r=w_r/W_r. The exact innovation martingale M_j=sum_{r<=j}p_r xi_r and T_n-E T_n=sum_{j=2}^n(1+(n-j)p_j)xi_j give orthogonal variance identity. If beta<1, p_j<=1/j off hubs and p_2^k<=2^{-k(1-beta)} at hubs; E v_j=O(log²j), so sum p_j² E v_j<infinity and M_j ->Z_beta a.s./L². Cesaro and Kronecker eliminate average xi_j, yield T_n/n-log n ->c_beta+Z_beta with finite positive variance (xi_3 nonzero), c_beta=gamma-1+sum(p_j-1/j) absolutely convergent. For beta>=1 every large dyadic j has p_j bounded below, and two old hubs retain positive masses with expected depths separated by at least fixed amount, giving E v_{2^k}>=c(beta)>0; positive per-hub terms force Var(T_n)/n²>=a_beta log n. Independent exact weighted enumeration n<=7 beta 0,1,2 confirms means and variances; infinite conclusions follow from martingale proof, not enumeration.

## originality

PASS

PASS best of knowledge: the 2026 primary Gałązka–Wdowicka theorem supplies innovation identity and L² convergence when p_n=O(1/n), but for every beta>0 the dyadic mass spikes violate this sufficient hypothesis. That paper explicitly raises necessity/general irregular weight limits as an open issue; it does not prove variance divergence for beta>=1. Sénizergues profile theory may cover the beta<1 convergence but not this sharp sparse-hub boundary. Distinct earlier stretched-exponential weight phase transitions concern p_n~c n^-gamma on all n and cannot be transplanted to sparse macroscopic hubs.

## value

PASS

Sharp structural threshold within a natural geometric sparse-attachment family: for beta<1 sum of hub weights negligible relative to population while at beta>=1 repeated persistent hubs generate fresh non-decaying innovation variance and log-divergent normalized total path variance. A meaningful positive/negative boundary to the existing sufficient martingale theorem, not an arbitrary finite parameter or routine renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
