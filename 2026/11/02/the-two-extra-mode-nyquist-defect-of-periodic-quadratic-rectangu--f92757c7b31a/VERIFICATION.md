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

# Verification

The proof is a closed six-equation Fourier-fiber calculation for every integer \(m,n\ge2\); no finite experiment is used to extrapolate to infinite mesh families. Inspect the exact formulas in `RESULT.md` and run `python3 check.py` to reproduce independent direct interface-matrix rank tests, which use integer row operations and require only the Python standard library.

Observed direct nullities: \(2\times2:6\), \(2\times3:6\), \(3\times3:9\), \(2\times4:10\), \(3\times4:12\), \(4\times4:18\). The script also checks that all three displayed double-Nyquist local shapes exactly satisfy periodic vertex and averaged-normal-derivative conditions. It does not verify arbitrary mesh sizes computationally; that is supplied by the exhaustive Fourier proof. No independent mathematical audit was performed.
