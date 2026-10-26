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

The direct fixed-state criterion uses the closed-neighborhood sum, counting a bit's own value once. Enumerative identities and spectra are derived in the proof and can be independently reproduced with `python3 checks.py` using Python 3 without external packages.

Actual completed checks: exhaustive enumeration of extended states for \((a,b)=(1,1),(1,2),(2,2),(2,3)\); agreement of the direct double sum and exact rational spectral expression for every \(1\le a,b\le7\); numerical ratios for balanced \(n=20,80,320,1280\). The four exhaustive counts are \(10,42,324,2128\). The triangular-spectrum argument, all-size identity, and asymptotic are **analytic proofs**, not inferred from program termination or finite tests.

Scientific limits: no finite check establishes the unbounded parameter case; no claim is made about attracting basins or independent external certification. The related classical Bernstein-operator paper was not accessed in full text; this is an explicitly retained originality risk.
