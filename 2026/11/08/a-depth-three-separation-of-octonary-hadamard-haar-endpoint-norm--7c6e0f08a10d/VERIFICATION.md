---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The complete normalized real octonary Walsh–Haar basis has one constant and seven contrasts per internal node. For fixed row (recentered at the all-zero leaf by XOR), only ancestral signs contribute. With local h_y=Σ_{a≠0}σ_a(-1)^{a·y} over 128 signed contrast profiles, exact row decomposition gives F_d(t)=max_sigma[(Σ_{y≠0}|t+h_y|)/8+F_{d-1}((t+h_0)/8)], F_0(t)=|t|. Independent 128-sign enumeration yields ten distinct sorted Walsh profiles. For |t|<=1, successors stay in this invariant window and every local |t+h_y| is affine. The alleged maximizing profile (h0,S,Z)=(1,17,1) dominates all ten actions for B∈[1/7,1],t∈[0,1] by 40 exact corner inequalities on bilinear differences; it is attained by a real sign vector. The resulting A_d+B_d|t| recursion solves to U8(d)=15d/7+13/49+36/(49·8^d). The binary Haar recurrence gives U2(n)=2n/3+5/9+(4/9)(-1/2)^n. Substituting n=3d shows equality d=0,1,2 and strict octonary excess for every d>=3, via elementary closed-form difference. Finite Bellman checks d<=4 corroborate, not substitute for the invariant affine-window induction.

## originality

PASS

Full earlier Resultary theorem on b-ary predictable martingale sign transforms is NOT the same: it signs each entire (b−1)-dimensional local martingale difference by a single scalar at each parent; this result signs seven separate Hadamard contrast coefficients independently, a strictly larger different local operator family. Another prior complete theorem has independently signed Hadamard coefficients but arity 4; its binary depth-two invariance does not imply the arity-eight depth-three separation. Classical standard dyadic Haar strong/weak-type and weighted higher-rank Haar results likewise do not supply the ten-profile exact octonary law in available material. Best-of-knowledge PASS.

## value

PASS

The first depth at which three dyadic Haar generations and an eight-child Hadamard block cease sharing the same sharp endpoint unconditionality is a precise nontrivial invariant of two natural orthonormal bases; the ten-profile Bellman reduction explains a structural rather than arbitrary numerical discrepancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
