---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For A=diag(1,B), 0≼B≼qI, z tail supported on at most m-1 coordinates, the order-statistic inequality follows from B²≼qB and h≤q s/(s²+m-k), yielding |Bz|_(m)≤q sqrt(m-1)/m||z|| with equality attained by B=qJ_m/m. A leading coordinate above this bound survives arbitrary ties, with tail/leading norm ratio contracting by q; gives exact squared-overlap threshold and Rayleigh bound. The same rank-one tail at/below threshold ejects first coordinate (equality with adversarial tie) and traps subsequent iterates at q. All m and n allowed; no indefinite tail, non-sparse start or finite-precision claim.

## originality

PASS

Best-of-knowledge comparison supports a specific unclaimed mathematical increment, not a proof of absolute priority. The order-statistic constant q sqrt(m-1)/m together with rank-one extremizer gives a necessary and sufficient uniform frontier not shown in available prior statements; newer full-text unavailability leaves material originality risk.

## value

PASS

Dimension-independent sharp initialization/support-retention frontier with matching permanent-failure witness addresses a natural irreversible error mode of hard-threshold sparse eigensolvers, beyond sufficient convergence estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
