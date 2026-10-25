---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Independent block sign flips and uniqueness force John and Loewner quadratic forms to be block diagonal. For John containment the exact scalar problem is max_{sum r_i^2<=1}sum_i(a_i r_i)^p<=1; p<2 gives sum a_i^{2p/(2-p)}<=1 and strict weighted AM-GM optimum a_i=w_i^{1/p-1/2}; p>=2 has a_i=1. Loewner containment is max_{sum s_i^p<=1}sum_i(c_i s_i)^2<=1; p<=2 gives max c_i<=1, while p>2 yields sum c_i^{2p/(p-2)}<=1, including p=infty exponent 2, leading w_i^{1/p-1/2} L_i block radii. Equality in Holder identifies all multi-block vs single-block John and Loewner contacts, and arbitrary unit Euclidean radius allocations at p=2. Cancelling common ellipsoid-volume constants yields exp[N H(w)|1/p-1/2|], strictly minimized at p=2. Independently recomputed entropy identity for dimensions (1,2),(3,2,1),(1,3,5) across p=1,1.25,1.8,2,2.5,4,infinity. Source code was read; finite norm samples are corroboration only.

## originality

PASS

Grundbacher-Kobos arXiv:2603.18268 Theorem 1.1 gives a different Banach-Mazur distance to Euclidean space and optimal single simultaneous position, not separately volume-maximal inscribed/minimal-volume enclosing ellipsoid or their complete block-contact sets. Classical John-Lowner conditions supply ingredients, but combining them with arbitrary symmetric summands yields a quantitative dimension-entropy formula and p=2 opposite contact transition not supplied by a cited theorem. Classical direct-sum norm literature is broad, preserving priority risk.

## value

PASS

Canonical ellipsoid and contact decomposition for arbitrary symmetric blocks is a reusable structural lemma on direct-sum geometry; the sharp entropy factor exposes how block dimensions govern volume separation and an exact switch in support geometry across p=2. Not merely a numerical special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
