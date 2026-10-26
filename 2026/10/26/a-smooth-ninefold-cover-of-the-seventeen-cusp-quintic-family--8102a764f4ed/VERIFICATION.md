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

Run `python3 check.py` in this directory. The standalone script requires only Python 3 and explicitly exhausts all nine codewords of the rank-two ternary model, enumerates four projective one-dimensional subspaces, checks the \(12,12,12,15\) weights and \(5,5,5,2\) block sizes, then independently verifies the arithmetic identities for the cover. This calculation is finite and does not replace the proof for arbitrary complex quintics.

The proof in `RESULT.md` checks dimension using the Griesmer inequality, verifies every nonzero local inertia column, identifies the maximal cover by localization, derives smoothness by the \(A_2\) uniformizing local model, and computes Euler, canonical and Hodge data using Tan’s four cyclic quotients. No computer algebra experiment is claimed as proof of the infinite assertions. Scientific priority is checked against source text and recorded overlaps but cannot be established absolutely by database search. Independent validation has not been performed.
