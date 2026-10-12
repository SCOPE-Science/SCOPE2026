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

The standalone `checker.py` checks all coefficient tuples for \((n,q)=(1,2),(2,2),(2,3),(2,4),(3,2)\) for the cubic coordinate-cross algebra. It uses direct finite-field arithmetic, verifies the generator relations and composition-idempotence, computes ranks and compares counts against the proved closed formula. Run `python3 checker.py` from the directory containing the extracted files. Expected terminator: `VERIFY_OK`.

Exact observed distributions (rank: multiplicity) are \(\{1:1,3:1\}\), \(\{1:1,3:16,5:1\}\), \(\{1:1,3:54,5:1\}\), \(\{1:1,3:128,5:1\}\), and \(\{1:1,3:192,5:144,7:1\}\) in the listed case order. The checker does not exhaust any higher-dimensional or infinite-field case, does not establish bibliographic novelty, and provides no independent external audit. The general assertion is supported by the algebraic proof in `RESULT.md`.
