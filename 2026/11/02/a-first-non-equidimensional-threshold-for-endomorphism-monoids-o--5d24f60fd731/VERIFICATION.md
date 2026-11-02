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

Use Python 3 without third-party packages, from this directory:

```sh
python3 verify_coordinate_cross.py
```

The script constructs the polynomial product in \(t\mathbb F_q[t]/(t^d)\) over prime fields and the explicit extension \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), and checks every tuple of coefficient values in 13 target-row cases. It compares the original annihilation equations against the proposed component cover and exact point formula. Three small full endomorphism enumerations also check the independent matrix-rank unit criterion, while five larger global cases use seeded sampling, not exhaustive verification. See `coordinate_cross_check_output.txt` for the recorded checker output and final success marker.

Mathematical proof, not finite enumeration, establishes claims for arbitrary \(n\ge2\) and every field. The original scheme's possible nilpotents, higher truncation lengths, and external independent mathematical validation have **not** been checked or claimed.
