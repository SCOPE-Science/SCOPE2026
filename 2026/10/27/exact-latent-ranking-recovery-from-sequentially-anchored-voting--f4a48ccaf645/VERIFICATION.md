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

# Verification procedures and limits

The general claim follows from the constructive six-part proof in RESULT.md. The verifier is an exact finite-domain cross-check, not an infinite certificate.

Run `python3 verify.py` with a standard Python 3 interpreter. The script enumerates every strict intrinsic ranking and every nonzero acceptability cutoff for a fixed known presentation order with 3–7 alternatives. It computes all realized ballot fibers and compares each with the proposed tree linear extensions, the claimed hook count, and every forced ordered pair. It also verifies the exact random-permutation mean and variance. Across 3–7 alternatives this covers 7+15+31+63+127=243 nonempty record ballots.

For 3–5 alternatives, it separately enumerates every presentation order, intrinsic ranking, and cutoff and checks the no-order compatible-ranking set on all 15, 64, and 325 possible observed ranked ballots, respectively. The source checker uses Python integer, `Fraction`, and exhaustive permutations, not numerical approximate equalities.

Observed successful output includes `ALL EXACT FINITE CHECKS PASSED`. The universal theorem's proof remains the necessary-and-sufficient tree construction, finite-poset extension count, and characterization of all comparable pairs. The Dickman limit is a standard record-position limit noted in the prior literature. No external validation is claimed.
