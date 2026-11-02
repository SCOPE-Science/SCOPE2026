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

Run `python3 checker.py` using standard Python 3. The checker enumerates interleavings of identical words from their independently specified copies, collects all distinct suffix languages of all prefixes, and obtains their Myhill–Nerode count with a rejecting sink. For ten concrete cases it checks the prefix membership criterion against *all* fixed-content words and the exact state-complexity formula against direct right-quotient enumeration. Separately, 600 small parameter tuples are checked by direct enumeration of feasible count vectors.

Every computational comparison is finite; the general all-parameter theorem depends on the written proof. No external independent audit has been performed. The checker contains no imported data or third-party dependencies.
