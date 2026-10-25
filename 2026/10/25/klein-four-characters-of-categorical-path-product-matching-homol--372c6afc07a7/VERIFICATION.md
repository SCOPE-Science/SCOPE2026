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
# Verification of path-product reflection characters

The identity-character Betti ranks and the unique odd homology degree are exactly those of the published nonequivariant homotopy classification. Their use is explicitly attributed.

The proof checks the augmented Lefschetz normalization, the parity of the unique homological degree, all three nonidentity involution orbit structures, and the exact transfer matrix on eight boundary states. The transfer matrix and its characteristic polynomial provide a finite algebraic certificate of the closed forms for the auxiliary matching sums, rather than relying on sampled widths. The four character values yield nonnegative integral multiplicities by the Klein-four character projector.

The supplied `verify.py` was executed with Python 3. It reconstructs the matrix independently from the four cross-column edges and tests the signed orbit sums by a separate matching enumeration. Its successful output was:

```
TRANSFER_MATRIX_EXACT_27_OK
GROUP_ACTION_ORBIT_SUMS_VERIFIED 47 MAX_STATES 743476
```

The first test covers auxiliary lengths 1–27; the latter covers all four transformations for long-path widths 2–9 and all nonidentity transformations at widths 10–14. Exhaustive finite tests do not replace the infinite proof. The full character uses a published homotopy result and therefore does not independently re-prove that theorem; an independent audit of the new argument has not been performed.
