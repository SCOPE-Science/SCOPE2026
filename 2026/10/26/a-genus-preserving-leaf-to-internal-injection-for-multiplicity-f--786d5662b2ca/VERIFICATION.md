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

The standalone `VERIFY.py` uses an independent semigroup-membership predicate from Apéry residues to compute minimal generators and compare the actual leaf condition against the four algebraic classes. It also checks target Kunz admissibility, genus preservation, internality, absence of collisions, and the closed counts for every genus \(3\) through \(80\). It produced `VERIFY_OK` when executed against the delivered package.

Proof-based checks: the four Kunz inequalities, exhaustive residue-compatible Apéry decompositions, six pairwise-disjoint image-region comparisons, and the four integer interval counts are presented in `RESULT.md`. The asymptotic denominator uses the cited 2018 partition formula. Finite exhaustive tests are not a substitute for the general proof.

Limitations: no formal proof assistant or independent audit has been used. The complete text of the 2026 motivating paper was inaccessible; originality retains the resulting residual risk.
