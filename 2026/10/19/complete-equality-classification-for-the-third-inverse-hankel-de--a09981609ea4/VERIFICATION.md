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

The corrected RESULT.md retains the equality theorem and closes a gap in the cited majorant argument. In Allu–Kumar's Eq. (2.6), the constant Schur group's g² coefficient is p²(4−p²)(172−49p²), negative for 172/49<p²<4; a termwise triangle bound cannot retain that sign. The upper bound itself survives: grouping the constant, linear and quadratic terms in −g gives A+Bexp(iψ)−Cexp(2iψ), where C/B≤2/17 and C/A≤4/27 in this regime, hence B(A−C)>4AC. Subtracting the absolute square from (A+B−C)² gives the nonnegative factorization in repaired Step 2. All other groups have valid separate absolute bounds. Consequently exactly the same Bernstein certificate proves strictness for p<2 and |g|<1. Independently reconstructed inverse coefficients by Lagrange inversion and Schur recursion; reconstructed the source majorant's Phi (Bernstein minima 0 and 160 in the first p-slice) and the reduced unimodular defect by exact Chebyshev substitution (Bernstein minima 78336, 78848 on the half-boxes). Thus equality forces p=2, or |g|=1 and either p=0 or g=−1. For the boundary cases the Schur transform terminates: p=2 gives Koebe, g=−1 gives z/(1−pz+z²), and p=0 gives z/(1−gz²). Rotations recover precisely the two-pole family. Substitution in w(1−az+bz²)=z gives the stated inverse coefficients and determinant b³; its starlikeness follows by averaging the two positive-real-part Cayley kernels.

## originality

PASS

The sharp constant and Koebe example are prior. The same excerpted primary proof controls the envelope but does not fully classify its sharp maps. The repaired proof adds the missing signed phase bound for the envelope and retains the separate phase-defect rigidity theorem for the actual determinant. The complete rational two-unit-pole family in the ordinary starlike class is not covered by the verified prior statements.

## value

PASS

A complete necessity-and-sufficiency theorem reveals a genuine continuous set of sharp maps missed by pointing to Koebe, distinguishes phase rigidity from saturation of a numerical upper envelope, and supplies exact proof rather than sampling. The proof repair is needed to support that structural conclusion; it does not rely on claiming a stronger bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
