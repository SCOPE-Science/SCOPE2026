---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The derivation was replayed from the stated stochastic recurrences.

For stochastic Dual-OHM, each terminal iterate is represented as a rational linear combination of the initial point and formal independent noise symbols. The script checks the claimed reflected-map coefficients for every horizon \(2\le N\le24\). It separately reconstructs stochastic OHM and checks its terminal coefficient \((j+1)/N\) in magnitude.

The script then checks the finite variance identities obtained by summing squared coefficients. It reports `VERIFY_OK` when all exact-rational comparisons pass.

The replay is finite and therefore does not prove the all-horizon theorem or the infinite-series limit; those are established by the algebraic argument in `RESULT.md`.
