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

# Reproducibility and scope of the checks

Run `python3 code/verify_cubic_nets.py` from the extracted package directory. It builds each derivative as a six-bit quadratic coefficient vector, constructs all 18 degree-four multiples by quadratic monomials, and computes the rank of their span in the 15-dimensional degree-four space over the binary field. The algebraic proof that rank 15 is equivalent to geometric smoothness appears in `RESULT.md`; it is essential to interpreting this computation.

The program asserts 336 smooth cubics among the 1,023 nonzero coefficient vectors, 5,544 smooth two-dimensional vector spaces, 864 three-dimensional spaces, no extendible four-dimensional space, five seven-member rational-point spectra and eight projective orbits. The group-action check explicitly iterates all 168 invertible binary matrices. All loops are over specified finite exhaustive spaces.

Run `python3 code/check_smooth_by_extensions.py` for a separately implemented differentiation and extension-field test. It retains 336 cubics after testing geometric singular points of degrees at most four. This independent corroboration is not used in place of the exact Macaulay criterion: absence of zeros over only finitely many extensions does not by itself imply geometric smoothness.

The reproducibility checks were run successfully with standard Python. The enumeration is reproducible but has no independent external audit. Orbit classification is projective, not birational. The rational-base-point conclusion does not exclude nonrational geometric base points. Bibliographic searches do not prove uniqueness in the literature.
