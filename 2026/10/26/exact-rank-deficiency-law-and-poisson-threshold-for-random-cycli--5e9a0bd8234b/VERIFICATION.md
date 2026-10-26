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

# Reproducibility and verification

Execute `python verify.py` with Python 3. Only standard-library facilities are used: `fractions`, `collections`, `itertools`, and `math`.

The checker directly generates all binary schedules for 74 parameter triples with \(2\le n\le9\), \(1\le r<n\), \(q\in\{1,2,3\}\), and \(qn\le17\). It maps each selected actuator to the corresponding cyclically shifted basis-vector reachability column and counts distinct coordinates. Independently, it computes the polynomial recurrence for the claimed generating function in exact rational arithmetic. It verifies every coefficient of every generating polynomial against the exhaustive schedule histogram. It separately verifies exact counts at the shortest feasible horizon, compares closed-root and recurrence probabilities, and checks illustrative critical-window values.

Expected successful output begins:

`VERIFY_OK exact rank-deficiency distributions for 74 independent enumeration cases`

The universal generating-function formula, all offset/parameter boundaries, and the arbitrary-sequence Poisson limiting statements are established analytically in `RESULT.md`; the finite checker is a reproducibility test, not a substitute for their proofs or an independent external certification. In particular, its asymptotic examples do not prove convergence. No third-party publication, source code, or numerical data is bundled.
