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
# Reproducibility

Run the two Python 3 standard-library scripts in one directory: `python3 check.py` and `python3 check_f4.py`. Their original stdout, without postprocessing, appears in `check_output.txt`. The first enumerates all original zero-product matrix tuples in six small prime-field configurations and compares every possible prescribed rank/image/kernel combination; the second uses the extension field \(\mathbb F_4\), including field multiplication and inverses, for a seventh configuration. Both use separate brute-force matrix-product calculations from the Möbius formula.

The code uses finite enumeration; no extrapolation from it is asserted. The general result follows from the explicit bijections and finite subspace Möbius functions proved in RESULT.md. No independent audit or third-party certification has been performed.
