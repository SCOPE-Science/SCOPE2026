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
# Verification and limits

Run `python3 verify.py` in the same directory. Exact integer tests verify the vertex exposure, candidate-edge exposure, parallelogram obstruction, local-degree polynomial, edge counts, simple-vertex counts, and graph diameter for each integer \(3\le n\le12\). Independent LP feasibility tests use SciPy when installed and compare *every pair* of candidates in sizes \(3\le n\le8\). Each LP fixes a supporting functional to have equal value at the candidate pair and at least one unit less at all remaining roots, which is equivalent by scaling to exact two-point face exposure. Running the supplied checker produced `VERIFY_OK`.

The exact checks and LP tests are finite, not a proof at arbitrary parameter. The proof is the covering combinatorial case split with constructive integer supporting functionals and explicit impossible-case identities in `RESULT.md`. The positivity of the origin-adjoined supports and negativity of the extra unit-chain supports are explicitly checked there. No independent audit has been performed.
