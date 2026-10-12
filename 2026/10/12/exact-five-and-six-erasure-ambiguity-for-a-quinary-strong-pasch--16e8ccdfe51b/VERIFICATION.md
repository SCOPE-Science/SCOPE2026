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

# Reproducible checks and limits

Extract `verify.py` and `artifacts/circuits.json` into the same directory, preserving the `artifacts/` subdirectory, and run `python3 verify.py`. Only Python's standard library is used. The checker reconstructs the six-by-twelve matrix over \(\mathbb F_5\) directly from the three published vector triples and computes its rank six. It enumerates every \(5^6=15{,}625\) kernel codeword, deriving the complete weight distribution and support multiplicities.

A separate implementation of six point-difference versus four triple-line projective incidences per ordered group pair gives exactly 16 five-circuits. The program checks all \(\binom{12}{5}=792\) and \(\binom{12}{6}=924\) erased-column sets by modular Gaussian elimination and counts deficiencies zero and one. It verifies every support in the companion complete circuit manifest against both enumerated codewords and the erasure ranks, including the 112 extensions and 69 independent six-circuits. A successful run ends in `VERIFY_OK`.

These checks are complete only for the explicit finite code. They do not imply an analogous count over other fields or for all strong-Pasch configurations. No external independent audit is represented by this document.
