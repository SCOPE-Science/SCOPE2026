---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For K=Ind(C_{3r}×K_n), the oriented fixed-face trace counts rows invariant under a rotation with d=gcd(3r,t), including short quotients d=1,2. The augmented-chain Lefschetz sign is minus the signed row enumerator. The exact transfer matrix splits into q colour-difference eigenvalues -1 and a 3×3 block satisfying B^3=qI; the resulting signed character is q(-1)^d+3*1_{3|d}q^{d/3}. Published Theorem 22 gives concentration of homology in degree 2r-1, enabling character and induced-necklace module reconstruction and quotient rational invariants. Direct independent oriented-simplex finite checks agree; they do not prove all orders.

## originality

PASS

The published wedge-of-spheres homotopy theorem for exactly C_{3r}×K_n specifies non-equivariant homology only and cannot determine rotation character traces. Published 3-cut and matching-complex cyclic character theorems analyze different simplicial complexes; no valid implication was identified.

## value

PASS

The cyclic representation and rotational quotient Betti number distinguish equivariant topological information that a non-equivariant wedge decomposition cannot determine. The theorem treats every cycle length divisible by three and all complete-clique sizes, with a natural necklace classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
