---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Rooting the tree gives an integer inverse to the edge differences modulo common phase by signed path summation, so normalized Haar in these coordinates is as stated. The edge Gram matrix K is positive definite and the connected line graph with bipartite orientation makes the top weighted eigenvector full-support and simple (also true for the one-edge matrix). From K^{-1}−A/Λ positive semidefinite, the scalar strict monotonicity of t+sin t gives strict monotonicity of the lift in the K^{-1} metric. Lattice equivariance gives torus injectivity and invariance of domain gives surjectivity. The symmetric matrix K^{-1}DF is the sum of K^{-1}−A/Λ and diag(a_i(1+cos z_i))/Λ; their kernels intersect nontrivially precisely when all z_i=π. At this point the kernel is one-dimensional. Conjugate DF by A^{1/2} and diagonalize its constant term at π. The zero-mode diagonal entry of the quadratic perturbation is (1/2)∑a_i v_i² x_i², and cofactor expansion multiplies it by the product c of the other diagonal entries. All higher terms are O(|x|⁴), giving the asserted positive definite H. The punctured-torus change of variables yields an absolutely continuous pushforward (both exceptional singletons are null), with the q-norm pullback integrand (det DF)^{1−q}. Radial integration gives cutoff 1+d/2 and excludes L∞ as well. For the specified source-coordinate annulus the angular integral is |S^{d−1}|/sqrt(det H), by the volume of the unit H-ellipsoid, and the uniform O(r²) relative error integrates to O(1). The factor (2π)^{−d} and path value 3/π agree; in d=1 the empty product gives H=1/2 and cutoff 3/2. The independent symbolic two-edge check, including unequal weights, is replayable via python /workspace/branches/independent_checks.py; it is not the universal proof.

## originality

PASS

Prior exact criticality and narrower critical-map behavior must be credited. The supported distinction is the all-positive-weight quadratic determinant with its spectral coefficients, and the resulting sharp one-step density exponent and logarithmic constant; neither prior invertibility statements nor a cubic inverse modulus give that volume-distortion result.

## value

PASS

At the natural critical step, topological reversibility does not predict the distribution of uniform phases after one step. The sharp dimension-dependent threshold and spectral logarithmic coefficient give a usable, weight-sensitive volume-distortion benchmark, including a precise endpoint divergence. This is not a claim about invariant or long-time densities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
