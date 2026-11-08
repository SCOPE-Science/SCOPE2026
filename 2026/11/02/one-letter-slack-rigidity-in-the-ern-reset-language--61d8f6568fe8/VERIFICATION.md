---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reverse preimages a^-1 rotate cyclic intervals and b^-1 can grow a nonfull interval only when it is {0,...,r-1}; each growth adds n-1 and requires n-1 inverse a-rotations before the next growth. Growing a singleton to all n states requires n-1 effective b actions, yielding the minimum L and its rigid unique word. One extra a must occur before forward W (after reverse set fills Q); one extra b must be an identity inverse insertion because any shrink loses too much. In the jth internal gap the only forbidden insertion offset is t=j; summing n-2 offsets for each of n-2 gaps gives (n-2)^2 plus aW. Wa,Wb are the two already-reset extensions, giving total (n-2)^2+3. Independent bit-mask subset dynamic programming verified no earlier resets, exactly one at L and the first-next counts 1,2,5,10,17,26,37,50,65,82 for n=2..11. Algebraic proof, not finite DP, justifies all n.

## originality

PASS

PASS for exact second-layer first-synchronizing-language coefficient and full one-letter insertion classification, not for the classical shortest reset threshold. Relevant earlier algorithms analyze shortest words and avoiding/rank-compression thresholds rather than this multiplicity.

## value

PASS

A canonical extremal synchronization family permits a complete classification immediately one letter above its sharp reset threshold; the exceptional insertions and exact next-layer language coefficient expose structural rigidity of near-optimal synchronization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
