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

# Computational verification

Run `python3 verify.py` in the same directory; its UTF-8 JSON output should equal the embedded `certificate.json` byte for byte. All arithmetic uses Python standard-library exact fractions. The tests independently enumerate all patterns of failed and functional sites on multiple small cycles, and compare the enumerated connectivity and reachable-site distribution with the independent gap formula. Other loops check finite rational instances of the symbolic balancing, stochastic extremality and connectivity reversal.

The mathematical proof in `RESULT.md` is the only justification for the full infinite family of integer sizes and all real survival probabilities. The computations cannot establish novelty, independent validation, or general-case correctness on their own.
