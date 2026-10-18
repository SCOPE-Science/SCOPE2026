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

# Reproducible exact verification

This package includes standalone standard-library Python programs. From the directory containing the extracted files, run:

```
python3 verify_equivariant.py
python3 check_signed_lefschetz.py
```

The first program exhaustively enumerates 10,012 augmented matching-complex faces, constructs signed integer boundary matrices, contracts 5,002 unit entries, verifies the eight residual generators are integer cycles and project back to themselves, and evaluates each geometric symmetry as a signed simplicial chain map in that homology basis. It checks the group relations, exact character values, rational irreducible multiplicities, and quotient invariant; its final line is `VERIFIED`.

The second program generates matchings with a different graph-edge ordering and calculates signed fixed-simplex Lefschetz values directly for all eight symmetries. Its final line is `INDEPENDENT_LEFSCHETZ_VERIFIED`.

The two `.out` files contain the actually observed console output of the supplied scripts. Exact integer reductions, not finite probabilistic sampling or approximate linear algebra, support the one finite-grid claim. This is not an independent mathematical audit and does not certify other grid sizes, integral orbit-space torsion, or an equivariant homotopy equivalence.
