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
Run `python3 verify.py` using Python 3 standard library. The exact adjacent-pair closure and length-15, length-29, and length-85 factor enumerations are recalculated from the displayed morphism without external datasets. The script checks the periodic-run table for periods 1 through 14, short-period overlap absence in the four-symbol fixed point, block alignment certificates, and the factor at zero-based index 2. `verification_output.txt` holds the observed stdout.

Finite checks do not alone prove the infinite statement. The argument establishing reduction of the infinite language to those certificates, the descending-overlap step, and the exclusion of all large binary cubes are in RESULT.md. Independent scientific validation is not claimed.
