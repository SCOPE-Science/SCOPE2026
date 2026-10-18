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

## Reproducible checks

Run `python3 verify_critical_gl.py` with Python 3 and no third-party packages. The script checks 45 exact rational identities at \(q=1/4,1/2,3/4\) and \(1\le M\le15\); tests positivity and the weighted-potential drift on six numerical trajectories; compares finite-time critical amplitudes with their closed forms; and tests gamma-ratio memory scaling for three fractional orders with \(M=10000\).

## Logical scope and limits

The full proof is contained in RESULT.md. The exact tests establish the identities only for the enumerated rational instances, while the analytic proof covers all \(M\ge1\) and \(0<q\le1\). Forward numerical tests never establish convergence by themselves, and no finite truncation is used as an infinite-memory approximation. The bound on initial histories is essential to the claimed global-in-time positivity. Independent scientific audit has not been performed.
