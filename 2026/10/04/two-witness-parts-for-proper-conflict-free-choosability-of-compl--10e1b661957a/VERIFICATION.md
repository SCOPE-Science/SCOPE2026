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

The proof is symbolic and constructive. Its critical inequalities are:

1. In the first part, every non-witness vertex has at least two listed colors, so it can avoid the first witness color.
2. For the second part, offset two always gives at least \(n_1+2\) listed colors. With offset one and at least three parts, the nonempty third part gives the same lower bound.
3. For every later part \(P_i\), the number of colors already used is at most the number of previously colored vertices, which is at most \(N-n_i\). A list of size at least \(N-n_i+1\) therefore has an unused color.
4. Because no later part reuses an earlier palette, the two designated witness colors remain unique in their respective parts and hence unique in the required open neighborhoods.

`verify.py` implements exactly this construction. It exhaustively checks exact-size list assignments for five small complete multipartite graphs and deterministically stress-tests larger profiles. `verification_output.txt` records a replay ending with `ALL CHECKS PASSED`.

These computations are finite implementation checks only. They do not replace the general proof and make no claim about optimality of the offsets.
