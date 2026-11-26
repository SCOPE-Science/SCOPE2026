---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

After dividing by h_0², the paired traces are real polynomials. The x⁴ coefficient kills H_22; the x³ and x coefficients at 0 and δ kill H_12 and H_01 since sin δ≠0. The constant and quadratic coefficients leave H_02=t exp(−iδ), H_00=−H_11=√2 t cos δ. The kernel is exactly the indicated line with block eigenvalues tending to ±1 and remaining eigenvalue −√2 cos δ. Rank eight therefore persists at π/2, with a uniform positive least transverse singular value in a small compact neighborhood (the outputs lie in a fixed finite polynomial-Gaussian space). For H=uu*−vv*=tK_δ+R with R orthogonal to the kernel, choose a unit null vector x of H: ||R||_F≥||Rx||=|t| ||K_δx||≥|t|√2|cos δ| locally. Using ||H||_F≤|t| ||K_δ||_F+||R||_F establishes the lower multiple. For u=(e_0+i e_2)/√2 and v=(e_0−i e_2)/√2 the second trace is 2 sin(2δ)h_0h_2, the first is zero and ||H||_F=√2. The integral of h_0²h_2² is 3/(8√(2π)), obtained using the x² and x⁴ moments 1/4 and 3/16 under the normalized e^(−2x²) weight. This witness gives both the exact zero and the matching upper order, for either side of π/2.

## originality

PASS

Credit the known qualitative uniqueness and exceptional angle and known two-setting rank. The accepted contribution is specifically the sharp two-sided angular order for the global lifted pure-state ratio in the contiguous three-mode system. The strongest compared results do not already bound its angular deterioration.

## value

PASS

The Pauli pair is a natural degenerate set of observables. The exponent characterizes how the best inverse conditioning deteriorates globally over pure states as the second quadrature approaches it, separating fixed-rank ambient singular values from the tilt of the kernel relative to physically admissible differences. Exact linear order has meaning even without the optimal slope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
