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
# Verification record

Run `python3 verify_subdivision.py` using Python 3 standard library. Its recorded deterministic output is in `verification_output.txt`.

The checker constructs adjacency from the original edge subdivision; it does not generate a graph from the candidate characterization. It tests the original blue-vertex/unique-white-neighbor rule directly on every subset of twelve graphs (\(22{,}656\) candidate initial sets), checks the count at every cardinality, and checks the proposed no-fort characterization. Four smaller parameter pairs also have every inclusion-minimal fort recomputed directly from the neighborhood condition and compared as families.

These finite tests do not certify a result for infinitely many parameter pairs. The proof in `RESULT.md` supplies the infinite argument. Independent review remains unperformed.
