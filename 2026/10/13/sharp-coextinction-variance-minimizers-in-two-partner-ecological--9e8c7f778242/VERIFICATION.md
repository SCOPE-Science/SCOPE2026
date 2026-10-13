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

# Verification of the coextinction-variance classification

Run `python3 verify_degree_two_extinction.py` from a folder containing that file. It uses only Python's standard library, exact integer counts and `fractions.Fraction`; there is no internet or data dependency.

Expected and observed successful output:

`VERIFY_OK profiles=7132 exact_event_contributions=1362496 equality_cases=25081`

The checker generates 7,132 multisets of unordered distinct-primary pairs for parameter ranges \((n,m)=(4,2\ldots5),(5,3\ldots5),(6,3\ldots4)\), computes every exact fixed-number primary-loss survivor state, verifies the variance formula and its equality cases against the explicit lower bound at each deletion count, and checks independent-loss laws at \(q=1/4,1/2,3/4\). The checker also verifies two connected six-primary examples, including their exact rational variances. Its search covers some test profiles with isolated primaries, for which the covariance identity remains valid; the theorem's network feasibility and optimizer statements only concern networks with no isolated primaries.

The unrestricted statements in RESULT.md are mathematical proofs based on indicator covariances, primary-degree convexity, and a terminating degree-balancing edge shift. Finite verification is corroboration, not a claim to an exhaustive search over unbounded network sizes or to independent certification.
