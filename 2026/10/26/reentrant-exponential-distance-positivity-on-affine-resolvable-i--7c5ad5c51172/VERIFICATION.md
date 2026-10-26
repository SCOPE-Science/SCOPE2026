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

# Reproduction and proof checks

The included `affine_distance_kernel_verifier.py` is a standalone Python 3 program requiring SymPy and NumPy. Run `python affine_distance_kernel_verifier.py` in the directory containing the script. It prints four geometry checks and ends with `PASSED all symbolic, geometry, spectral and rank assertions` on success.

**Exact symbolic checks.** The script verifies the general identities
\[
\det B_1=(1-w)^2(1-(k-1)w),\qquad
\det B_0=\frac{1-w}{n-1}\bigl((n-1)+\beta w+\gamma w^2\bigr),
\]
verifies the scalar-sector factorization, and checks that the constant-sector determinant in the \(\mathrm{AG}(3,3)\) case equals \((1-w)(1-54w+416w^2)\). It verifies the exact radicals \(w_\pm=(27\pm\sqrt{313})/416\) and the strict ordering \(0<w_-<w_+<1/8\).

**Graph and spectral checks.** Finite-field arithmetic constructs incidence graphs for \(\mathrm{AG}(2,2)\), \(\mathrm{AG}(3,2)\), \(\mathrm{AG}(2,3)\), and \(\mathrm{AG}(3,3)\), with \(10\), \(22\), \(21\), and \(66\) vertices. Breadth-first search confirms graph distances and parallel-class distance four. Direct symmetric eigenvalue computation agrees with the predicted two scalar-sector multiplicities and block-sector eigenvalues at five values of \(e^{-a}\). Separate checks verify the signs in and outside the admissible intervals and the endpoint nullities \(1,1,26\) for the three positive thresholds.

**Limits.** Floating-point diagonalization at selected small orders does not certify a universal theorem, and numerical rank comparisons use an absolute threshold of \(10^{-8}\). The all-design proof is the symbolic orthogonal decomposition in `RESULT.md`. The algebraic endpoint identities are checked exactly; existence of every possible integer-parameter design is not claimed. No independent audit has yet been performed.
