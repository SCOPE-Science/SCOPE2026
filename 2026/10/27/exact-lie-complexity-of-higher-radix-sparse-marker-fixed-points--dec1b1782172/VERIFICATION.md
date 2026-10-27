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

# Verification and limits

The theorem is established by the five-step proof in `RESULT.md`: marker residues, the maximal zero run, the base classification, forbidden nondivisible lengths, and a bijective desubstitution at divisible lengths. No external completeness algorithm is needed for the infinite statement.

The self-contained Python file `verify_lie.py` uses only the standard library; run `python3 verify_lie.py` to reconstruct the substitution fixed-point prefixes and check each predicted value against a direct full-conjugate-factor census. It compares two prefix sizes independently to reduce finite-window false positives. Passing finite comparisons is supporting evidence only: it cannot certify assertions over all lengths or all radices.

Originality is supported by comparison with the cited articles and available indexed records, and is subject to the possibility of an unindexed equivalent treatment. This verification file does not represent an independent audit or external mathematical certification.
