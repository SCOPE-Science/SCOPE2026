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

Run `python3 verify.py` beside `certificate.json`.

The first engine directly implements the least-failing-prefix greedy definition on the first \(256\) symbols and obtains exactly
\[
0,1,3,7,15,31,63,127,255.
\]

The second engine independently verifies the morphic identities used by the infinite proof and checks the attractor property of the truncated words through ten substitution levels. The third checks the exact occurrence lemma and the unique escaping factor through independent higher levels.

The computations are finite stress tests only. The infinite theorem is supplied by the induction over every dyadic prefix interval and the symbolic desubstitution proof in `RESULT.md`.

Independent audit has not been performed.
