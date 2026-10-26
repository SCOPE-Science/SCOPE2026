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

# Verifiable statements and checks

The theorem is proved for all integers \(r\ge3\), \(m\ge2\), \(q\ge1\). Local forcing means a blank vertex with exactly \(q-1\) named colours on its colored neighbours takes the missing colour, and success requires a proper total assignment.

1. Reproduce finite checks with `python3 verify_windmill.py` from the same package. This Python standard-library program builds adjacency directly, enumerates all \((q+1)^N\) partial colourings in each of 12 test cases, rejects improper seeds, independently iterates the forcing rule, and compares every coefficient with the closed formula. The completed execution returned `VERIFY_OK cases=12 complete_assignments=489479`.
2. Analytic infinite check at chromatic palette: per completed proper colouring, initially seeded hub gives \(z H_r(z)^m\); initially blank hub gives \(H_r(z)^m-(r-1)z^{m(r-2)}\), because every blade needs all but at most one of its leaf vertices seeded and the missing hub needs all leaf colours present somewhere.
3. Analytic infinite check for larger palettes: degree \(r-1<q-1\) stops all leaf forces. Thus successful incomplete assignments have exactly \(N-1\) initial vertices and are counted by the explicitly derived surjective-colour inclusion-exclusion \(qU_{r,m}(q)\).
4. Boundary checks: \(q<r\) has no proper colouring; \(q>N\) has no hub-blank surjective seed, but total proper colourings exist. The one-color enlargement \(r\to r+1\) increases the minimum seed count by \(m\).

Finite enumeration does **not** establish any infinite identity. Independent audit has not been performed. The checker intentionally includes the excluded single-blade and two-vertex-clique boundary cases as stress tests, without claiming them in the theorem. No external files or third-party paper contents are required for replay.
