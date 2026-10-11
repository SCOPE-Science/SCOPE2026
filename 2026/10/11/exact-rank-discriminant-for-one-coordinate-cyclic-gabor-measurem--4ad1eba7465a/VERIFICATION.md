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

# Reproducibility and scientific limits

The proof gives the full all-dimensional result algebraically; it does not rely on a finite census. For a separate computational cross-check **within the proof package**, execute `python3 CHECK.py` using Python 3 and its standard library. The checker directly assembles the \(n^2\) Gabor orbit vectors and their vectorized rank-one projectors, computes the matrix rank by complex Gaussian elimination, and compares against the claimed rank formula for \(3\le n\le10\) at six specified parameter values. It also enumerates all pairs of nonzero residue classes to verify the divisor-count identity at each residue in these dimensions.

The executed package-path check returned:

```
PASS: 48 direct projector-span ranks and 52 congruence counts
PASS: prime/composite phase-line distinction and universal rational generator for n=3..10
```

The finite computations involve floating-point arithmetic and a tolerance for matrix-rank decisions. They are checks, not error-free exhaustive certifications of all \(z\) or \(n\). Exact validity follows instead from the explicitly established four-case ambiguity identity, elementary congruence-count formula, and root-of-unity trace argument in `RESULT.md`. The underlying Weyl/Gram eigenvalue relation was also reconstructed and compared against the original published theorem. An external independent audit has not been performed.
