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

The main proof is the exhaustive geometric classification of one-point extensions of an ordered pair, followed by a cap argument for an arbitrary first node. The proof works for all heights and all branching values in the stated domain; numerical tests are supporting evidence, not extrapolation.

Reproduction from this directory: `sh reproduce.sh`. Requires Python 3 and a C++17 compiler. The symbolic and word-orbit implementations checked 7,098 pair configurations; the direct program checks actual ordered vertex triples without orbit reduction. The reproduction output is in `verification_output.txt`.

The 32 capped pointed types are the combinations of two capped depth variables with the binary-versus-at-least-ternary branching parameter. Some pointed types across the two branching classes can coincide; only the root-type classification is asserted to be pairwise distinct, and the rank-three branching sentence supplies the separation.

Limits: finite stress through height 44 does not by itself prove stabilization; Steps 1–3 of `RESULT.md` do. No independent human or external audit is claimed.
