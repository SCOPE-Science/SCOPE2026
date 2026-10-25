---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The event T_r<k<=T_{r+1} has exactly one previously earliest r-occupancy winner that remains at r; the next iid uniform mark hits it with probability 1/m, proving the exact joint mass [S_{r+1}(k)-S_r(k)]/m including endpoint k. Summing gives P(B_r)=(ET_{r+1}-ET_r)/m, and rate-m Poissonization with m independent rate-one clocks gives its absolutely convergent integral. For fixed r, Taylor expansion Q_s(x)=1-x^s/s!+O(x^{s+1}), integrated with an exponential dominating envelope, gives E Z_s=c_s m^{-1/s}+O_s(m^{-2/s}); the difference yields the displayed two-scale expansion. The joint kernel, T_{r+1}/m^{r/(r+1)} Weibull limit and negligible ET_r at this scale yield an integrated-tail conditional Weibull density via Riemann sums and tightness. Independent exact enumeration of all finite uniform sequences until threshold for (m,r)=(2,2),(3,2),(2,3), including every conditional k and total probability 13/16, 175/243, 27/32, reproduces the identity. Finite cases are not asymptotic proof.

## originality

PASS

Best-of-knowledge priority judgment: close primary sources and published indexed findings are compared by mathematical statement, not just titles. Known general/ingredient results are credited; the precise asserted complete result is not shown to be covered by the material actually examined. Explicit source-access and possible stronger-result residual risks remain and do not become fabricated negative bibliographic claims.

## value

PASS

The marked question asks whether a particular category retains leadership at successive collision thresholds; marginal birthday waiting-time theory does not record that event. The exact survival-difference kernel, rare selection probability and distinct equilibrium-Weibull limiting law characterize a motivated survivor-bias phenomenon in random occupancy processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
