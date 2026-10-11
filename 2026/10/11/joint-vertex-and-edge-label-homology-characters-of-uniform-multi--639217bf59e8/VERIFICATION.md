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

# Verification of the joint character

Run `python3 verify.py` with Python 3 and only the standard library. The script constructs every relevant face and all of its boundary incidences for eight small \((n,q)\) pairs, computes cellular ranks over \(\mathbb F_2\), and compares the resulting Betti vectors with the identity-character specialization. It separately compares the closed cycle formula against the signed fixed-cell count obtained by literal permutation of unordered pairs for all listed vertex and color conjugacy types. Finally it verifies the three-vertex quotient formula against the exterior-cube character.

Expected output:

```
VERIFY_OK direct_signed_character_checks= 170 exact_mod2_homology_cases= 8 exterior_cube_character_checks= 41
```

The proof is mathematical and all-parameter; the computational cases are consistency checks, not an exhaustive search over arbitrary \(n\) or \(q\). Integral equivariant representation structures and quotient homotopy types are not established.
