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

The proof is self-contained in `RESULT.md` apart from standard Fourier diagonalization, two-projection principal angles, and complex interpolation. The standard-library `check.py` constructs separate exact-rational common-refinement matrices and verifies 750 finite cases, and independently checks the Fourier expression. Testing does not establish statements for untested integer depths or irrational translations; those follow from the symbolic proof. The exact formula includes its two-bin exception, half-step cancellation, and strict-interior \(L^p\) boundary. Historical equivalence risk remains despite specific primary-literature comparisons.
