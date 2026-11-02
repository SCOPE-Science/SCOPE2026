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
The symbolic proof in RESULT.md is the universal correctness argument. The standalone standard-library checker `check_median.py` compares the proposed arithmetic criterion with independent exhaustive binary-window computations for all 60 permitted pairs in its bounded check range, independently tests the exact exceptional family and the \((10,3)\) example, and verifies 100 arithmetic edge-case families. These are finite consistency checks, not a computational proof for arbitrarily many sites. The real-data witness is obtained by replacing sign classes with pairwise distinct values on each side of zero, then perturbing only the zero coordinate.
