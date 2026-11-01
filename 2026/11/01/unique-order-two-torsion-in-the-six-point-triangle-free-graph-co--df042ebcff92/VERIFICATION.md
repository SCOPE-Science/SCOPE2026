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

Execute `python3 check_tri6.py` with NumPy installed. The script checks all face patterns, computes the complete integral boundary matrices, tests \(\partial_6\partial_7=0\), performs independent finite-field eliminations, and applies invertible modulo-four row/column elimination. Its terminal assertions check the exact ranks and the presence of a residual two after 564 unit pivots.

The recorded completed output is stored separately in `verification_output.txt`. This verifies only the specified two-primary summand, not every homology group or the whole Smith form at odd primes. A standalone integer torsion cycle is not provided because the direct Smith-rank argument is sufficient.
