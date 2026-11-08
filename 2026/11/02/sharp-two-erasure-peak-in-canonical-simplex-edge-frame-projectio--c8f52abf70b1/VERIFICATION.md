---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=9 the Parseval vectors v_{ij}=(e_i+e_j-2/n 1)/sqrt(n-2) form the stated edge-indexed frame; their full Gram is (|e∩f|-4/n)/(n-2). A matching M of t erased edges has H=2/(n-2)I-4/[n(n-2)]J. The Woodbury identity yields Q=P_EE+P_EM(I-H)^(-1)P_ME and the explicit entry formula in RESULT.md. Its sign is determined by whether retained edges intersect; orbit-wise row sums depend on erased-incidence s_e=0,1,2. The maximal incidence row gives the three rational branches of Lambda_{n,t}. Exact differences have the common n²-12n+24 factor, negative at n=9 and positive at all integer n>=10, and derivative in t is strictly negative after t=2. I built and inverted exact rational deletion Grams independently for every matching size at n=9,10,11,12; resulting max-row norms agree. This concerns canonical Parseval renormalization only, not the best possible complement projection.

## originality

PASS

Deregowska–Lewandowska use exactly the unerased simplex-edge midpoint frame and obtain the 4(n-3)/n base row norm; their accessible abstract and secondary review focus on relative projection constants and conjectural maximal constants. Renormalization after a matching deletion is an additional constrained deterministic problem, not a logical consequence of the unerased case. General frame-erasure moment results address different observables.

## value

PASS

Canonical projection after data loss is a natural finite-frame conditioning invariant. The exact row norms show a nonmonotone effect: two matching deletions, not zero or one and not three, produce the worst canonical projection for every n>=10. The completely classified peak and special n=9 reversal have a clear robust-frame motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
