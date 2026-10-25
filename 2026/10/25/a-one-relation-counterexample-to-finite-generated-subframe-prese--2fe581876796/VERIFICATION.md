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

The new theorem is supported by the full mathematical proof in `RESULT.md`. Its critical steps are: forward locality of the deterministic-chain tag formulas; compatibility of interpretation with successor-closed restrictions; exact recovery of all source relations by the graph encoding; and a structural induction translating every allowed \(\exists\)-bounded formula back to the original all-binary signature. The published Theorem 8 (arXiv:2603.12171v1) supplies the four-relation obstruction.

The supplementary standalone checker `check_generated_coding.py` is executable with Python 3 standard library. Run `python check_generated_coding.py`; observed output: `FORWARD_GADGET_FINITE_SANITY_OK 2133`. This checks every source graph up to the code's finite source limits and every successor-closed induced subgraph of every directed graph on up to three vertices. The asserted exact finite identities follow from the code's enumeration and the mathematical construction. These finite checks do not prove equivalence for arbitrary formulas, general model sizes, or historical originality; the proof and documented literature comparisons address those obligations.

No external/independent audit has been performed, and the full text of one broad FO-transduction comparison was unavailable. The result is restricted to directed frames with loops permitted.
