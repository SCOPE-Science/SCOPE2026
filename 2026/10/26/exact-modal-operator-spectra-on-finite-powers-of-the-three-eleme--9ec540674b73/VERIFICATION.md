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

# Verification details

The package includes a runnable, standard-library-only `checker.py` file. Run `python checker.py` from the directory containing this document and the checker. The program independently enumerates the full scalar truth-table spaces for \(n=1\) (\(3^3\) candidate tables) and \(n=2\) (\(3^9\) candidate tables); it applies each of the original meet-preservation, positivity, and consistency axioms, constructs the two-threshold families, and asserts equality of the accepted and constructed truth-table **sets**.

Expected scalar counts are \(5\) and \(13\), and the top-preserving scalar counts are \(3\) and \(9\), respectively. Independent selection of output coordinates gives total and normal operator counts \((5,3)\) and \((169,81)\). The execution was replayed on the packaged checker; it terminated with all assertions satisfied.

The full theorems for arbitrary \(n\ge1\) are proved in `RESULT.md`: no finite enumeration certifies them by itself. No independent audit or external formal certification is claimed. Literature priority remains subject to further human assessment.
