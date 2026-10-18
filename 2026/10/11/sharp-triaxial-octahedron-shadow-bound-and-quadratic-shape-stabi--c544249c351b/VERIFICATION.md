---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a Haar-uniform plane normal u, failure of projected antipodal vertex pair i is exactly |u_i|/a_i >= sum of the other two scaled absolute coordinates; the six-vertex event is a strict triangle-inequality cone in each octant. The standard trihedral solid-angle formula gives p=(4/pi)atan(2abc/D). AM--GM gives L_ab L_ac L_bc/(abc)>=2sqrt(2) and (a^2 L_bc+...)/(abc)>=3sqrt(2), with simultaneous equality iff a=b=c. Thus sharp global bound and strict equality follow. On centered log-axis line (t,-t,0), independently differentiated exact radicals give D/(abc)=5sqrt(2)+(27sqrt(2)/4)t^2+O(t^4) and p difference sqrt(2)t^2/pi; permutation symmetry makes Hessian isotropic, giving coefficient 1/(sqrt(2)pi). Scale and strict positivity hypotheses handled; no nonorthogonal claim.

## originality

PASS

Best-of-knowledge novelty is the sharp full two-modulus octahedron shape optimization and isotropic centered-log Hessian; prior axial theorem and regular value do not logically imply it. Historical hidden equivalence remains a risk.

## value

PASS

Random-shadow vertex counts of a natural triaxial orthogonal cross-polytope depend on two shape moduli; the result identifies the unique optimally balanced shape globally and an exact Hessian on that two-dimensional moduli space. The local rigidity supplies quantitative sensitivity not contained in knowing only the regular value. This is a motivated structural extremal statement, not a one-parameter interpolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
