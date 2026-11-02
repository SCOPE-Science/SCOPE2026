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

Run `python checker.py` in a normal Python 3 installation. The script verifies binary-code non-overlap for denominator sizes through 16, exact first-hit equinumerosity on explicit finite words, two-letter swap involutions, and the equivalence of cut encoding and 231/312 pattern avoidance for carriers through seven elements. A successful run prints `ALL_CHECKS_OK`.

Those finite tests do not prove claims for unbounded denominator or word length. The proof in `RESULT.md` establishes the general cases through explicit cross-bifix analysis, a finite-size bijection, a disjoint-block probability bound, explicit quantifier-rank accounting, and the classical aperiodic-automaton/rational-Markov-chain theorem. Independent auditing has not been performed.
