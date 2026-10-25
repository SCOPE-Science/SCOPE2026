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

# Reproducibility and limits

Execute `python3 artifacts/verify_corner.py` with Python 3. The script is independent of any third-party package. It constructs the characteristic-two corner update directly by XOR-ing the four shift terms, computes the ranks of exact iterate-minus-identity maps, counts all configurations for small windows, and separately checks the half-rank identity on dyadic rectangles.

Observed output: `PASS: 405 exact matrix-rank comparisons and 60 exhaustive fixed-point counts; dyadic half-rank checks passed`.

The checks include dimensions from one through nine and iterates with exponents zero through four; exhaustive fixed-point enumeration uses windows with at most twelve cells. There is no assertion that those finite checks prove the result for arbitrary dimensions. The universal proof is algebraic and is included in `RESULT.md`. No external or independent validation was performed.
