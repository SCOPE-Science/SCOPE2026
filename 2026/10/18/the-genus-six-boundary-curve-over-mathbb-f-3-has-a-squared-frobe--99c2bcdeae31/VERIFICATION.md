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

# Arithmetic verification

Run `python3 verify.py` from a directory containing this file and the standalone program. The script checks every degree-\(1\) through degree-\(6\) field by exact integer arithmetic, including irreducibility of the defining moduli and equality of two fibre-count tests; its final line is `ALL EXACT CHECKS PASSED`.

The expected rational point counts are \((4,10,76,82,244,670)\). Integer Newton recurrences and the genus-six functional equation reconstruct the complete numerator, and convolution proves the displayed square factorization. The elliptic partner is checked directly over \(\mathbb F_3\). The infinite point-count identity and the isogeny interpretation additionally require the mathematical arguments recorded in RESULT.md. No external independent audit was performed.
