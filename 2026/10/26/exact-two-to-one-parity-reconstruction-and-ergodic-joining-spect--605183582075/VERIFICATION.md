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

Run `python3 verify.py` (Python 3 standard library). It exactly enumerates all unordered phase pairs on two rational rotation grids, checks distinct parity words outside the diagonal, and independently evaluates 701 lower/upper golden-slope coding coordinates using 90-digit decimal arithmetic. It tests singular pulse locations at four shifts. Successful output begins `VERIFY_OK`.

These finite checks corroborate symbolic conventions. The proof for every irrational slope uses equidistribution, the absence of finite cycles of irrational rotation (for the jump-parity operator), and uniqueness of invariant Haar measures on circle orbits. Finite rational grids neither establish irrational injectivity nor prove completeness of invariant measures.
