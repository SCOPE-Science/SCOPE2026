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

# Verification record

Execute `python verify.py` in the directory containing the submitted files, with NumPy, SciPy and SymPy installed. Compare the program's standard output with `VERIFY_OUTPUT.txt`. The checker computes the exact closed-form candidate and direct extremal eigenvalues for 145 real test vectors in dimensions two through twelve, compares 5,800 arbitrary asymmetric positive diagonal alternatives, and performs 23 separate continuous numerical optimizations. Maximum observed closed-form-versus-eigenvalue absolute deviation was 5.12e-13, and maximum observed numerical optimizer discrepancy was 4.44e-14.

Exact symbolic checks verify: (a) a positive-semidefinite polygonal dual \(H\) for a three-coordinate nondominant vector; (b) the complete spectrum at an asymmetric dominant-coordinate instance; and (c) exact rational/surd eigenvalues in the example where Jacobi scaling is worse. The code uses a fixed pseudorandom seed and fails on assertion errors. Positive margins in sampled comparisons are observational and cannot establish universal optimality by themselves.

For the general theorem, the verification target is the full proof in `RESULT.md`: the polygonal zero-sum Gram construction supplies a matching minimax lower certificate; in the dominant regime every diagonal preconditioner inherits a two-plane spectral lower bound and the exhibited one-coordinate scaling attains it, with other eigenvalues located between the two planar extremes. Boundary cases are checked analytically.

Limitations: No numerical test exhausts the continuum of possible vectors or positive diagonal scalings. The analytic proof, rather than the software, supports the quantified claim. Independent external mathematical audit has not been performed.
