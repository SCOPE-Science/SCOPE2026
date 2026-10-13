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
# Reproducible checks
The analytical calculation is in `RESULT.md`. A separate finite-dimensional verification program is in `artifacts/verify.py` and requires NumPy (`requirements.txt`). Run `python3 artifacts/verify.py`. The expected successful summary is:

```
VERIFY_OK full_spectrum_axis_cases=270 Kraus_outputs=30 N=2..6 p=9 both_channels
```

The code calculates matrices on the entire \(2^N\)-dimensional Hilbert space, retains zero-eigenvalue transitions in the spectral Fisher formula, verifies all three spin directions for both channels and nine strengths at each size from two through six, and compares both exact output density matrices with direct Kraus tensor products for sizes two to four and five strengths. The checks include \(p=0\) and \(p=1\). Small finite matrices are corroboration, **not** a proof for arbitrary \(N\), nor publication-priority evidence. The algebraic proof covers all \(N\ge2\) and \(p\in[0,1]\). Independent evaluation is not reported.
