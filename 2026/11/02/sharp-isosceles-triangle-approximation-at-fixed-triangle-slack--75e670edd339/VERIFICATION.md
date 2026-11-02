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

The proof in RESULT.md is analytic and applies to all Euclidean triangles of positive area. The published pointwise three-candidate reduction is explicitly used. The following checks support the *new* constrained-minimax algebra:

- `python checker.py` with SymPy installed as stated in `requirements.txt`.
- Exact symbolic verification of the four-positive-coefficient stability identity, the quartic factor at the three-way tie, and the one-sided derivative identities.
- Direct coordinate construction of two inscribed isosceles candidates, cross-checking their relative areas against side-length expressions.
- Deterministic numerical stress tests on 12,000 admissible normalized side triples and on the unique fixed-slack extremizers at representative parameters.

These numerical tests do not prove the universal bound or uniqueness; those follow from the monotonicity and explicit positivity arguments. The endpoint of zero slack is a limiting collinear host and is not itself in the domain. Independent mathematical audit has not been performed.
