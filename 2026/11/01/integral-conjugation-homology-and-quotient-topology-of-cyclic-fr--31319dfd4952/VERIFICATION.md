---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: Writing G=(a,h), fixed-point-free action makes 1-h invertible for all h≠1; every outside-kernel element belongs to a unique conjugate complement H_x. The equation for commutation of ((1-h)x,h) and ((1-k)y,k) simplifies to (1-h)(1-k)(x-y)=0, forcing x=y. Nonidentity kernel elements commute with no outside element, and same-prime restriction precludes within-P edges. Thus each complement forms exactly the join of prime-primary nonidentity discrete sets, with kernel isolated vertices. Integral join Künneth yields the homology and handles q_i=2 and r=1 boundaries. Conjugation gives affine permutation of complement labels with trivial internal homology action; H acts freely on nonzero kernel points, so the asserted integral modules, three-valued character and topological orbit space follow.

## originality

PASS

PASS (bounded best-of-knowledge with explicit literature risk): Bate–Everitt–Ford introduced the exact prime-power clique construction and the nilpotent complement join. The verified statement for Frobenius semidirect products, including affine integral conjugation modules and the quotient topology, was not identified in available accessible source material. The highly relevant full original paper could not be read because institutional VPN access was disconnected; this limitation ALONE is not a scientific FAIL, and the comparison is not declared exhaustive.

## value

PASS

PASS: This gives a complete family-level simplicial decomposition, homology action and geometric orbit-space classification of a recent natural group clique construction. The affine/permutation integral module and precise isolated-orbit count convey more than a standard abstract group-theoretic Frobenius partition, and can be used to analyze conjugation quotients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
