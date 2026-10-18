---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Actual Git RESULT.md blob fee87c8b67241f09e9fa8a599c66ace652d53bbe uses Grinberg signed-cycle Frobenius maps. On tuple containing n_j copies of idempotent e_j, mixed-label cycles vanish and contributing permutations are ∏ S_nj, so f_m=∏_j (c_j)_nj. Mod p, (c_j)_s≠0 precisely when 0≤s≤the canonical lift a_j∈{0,...,p−1}. Existence of multiplicity vectors of sum m is equivalent to m≤∑a_j, and multilinearity extends this to the entire A^m. Hence minimal normalization-free degree w and distribution [t^d](1+...+t^(p−1))^r, including zero map, p=2 and r=1. Independent exhaustive bounded combinatorics for p=2,3,5, r≤3, m≤6 agreed; infinite assertion follows from the integral signed-cycle identity, not enumeration.

## originality

PASS

Best-of-knowledge PASS: Grinberg defines the normalization-free Frobenius maps and proves sum/composition theorems, but an exact minimal degree and generating distribution for all coefficient vectors in the split characteristic-p algebra are not stated in inspected material. The lower bound comes from explicit mixed-idempotent nonvanishing, not from the published sum upper bound.

## value

PASS

This is a natural complete classification of ALL additive maps on the basic split finite F_p-algebra for a newly generalized Frobenius notion, with exact degree spectrum and multiplicities. It clarifies a genuine small-characteristic limitation of normalized trace-like interpretations and yields an explicit sharp bound r(p−1), rather than an arbitrary coefficient slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
