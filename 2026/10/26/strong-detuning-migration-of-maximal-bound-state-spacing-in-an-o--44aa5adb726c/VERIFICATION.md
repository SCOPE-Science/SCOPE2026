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
# Verification record

The proof verifies the original exact spectral equation, both Airy root parity phases, positivity and uniqueness of the scaling inverse, the interior critical point, and the argument controlling maximizing indices over an unbounded set. In particular, fixed-index tests are not used as proof of the global maximum.

The supplied Python script requires NumPy and SciPy and checks six representative detunings by reconstructing the Airy zeros and solving the exact scalar eigenvalue equation. The reproducible diagnostic output for detunings \(20,30,40\) is respectively \((n_*,\Omega\Delta_*)=(93,1.070872814),(211,1.070443378),(373,1.070297302)\). The limiting coefficient is \(1.070105058314\), and the predicted index coefficient is \(0.233621921565\).

The finite-range script does not certify the infinite-index optimizer; the analytic argument in `RESULT.md` does. Independent audit or validation has not been performed.
