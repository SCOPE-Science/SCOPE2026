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

# Reproduction and limits

Run `python3 checker.py` using standard Python 3 (no third-party packages). It enumerates the unary operation tables of every BALFI on the two-element and four-element Boolean reducts, checks the two defining equations for each input, and separately checks the recovery and classical-negation subfamilies. It reconstructs the group action on each table and independently calculates its fixed-point counts. For Boolean reducts with one through five atoms, it computes the permutation cycles directly and compares these with the closed permutation-power formula; then it evaluates all three Burnside sums. For the two small exhaustive instances, it checks that the entire contradictory-incidence distribution is the claimed binomial law.

Expected ending: `ALL_CHECKS_OK`. The checked labelled counts are \(6\) and \(1296\); the corresponding isomorphism counts are \(6\) and \(666\). The Boolean reduct with four elements has \(666\) expansion isomorphism classes; the five and higher atom figures are computed by exact integer arithmetic without enumerating all labelled expansions.

These finite tests do not establish the general theorem. The complete mathematical proof appears in `RESULT.md`. No independent mathematical audit has been carried out.
