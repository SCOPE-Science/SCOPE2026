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

Run `python3 check_congruences.py` with a standard Python 3 installation in the same directory as this document. It exhaustively enumerates admissible lower-word ideals in finite instances, cross-checks an independently evaluated de Bruijn subset sum at lengths two and three, and directly tests all ideal candidates in feasible small cases. It also enumerates every unordered two-vertex set for seven small directed de Bruijn graphs and compares weighted overlap counts with the theorem's formula. The saved output `check_output.txt` ends in `VERIFY_OK` and gives detailed counts and histograms.

The proof's universal fixed-length asymptotic is not inferred from these finite checks. The necessary nonstandard steps—the two-arc classification and the tail bounds—are written explicitly in `RESULT.md`. No outside computation or independent mathematical assessment has been performed.
