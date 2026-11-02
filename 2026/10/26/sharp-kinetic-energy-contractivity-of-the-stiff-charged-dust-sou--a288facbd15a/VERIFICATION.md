---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For invertible dissipative A with sigma_min(A)>=1/2 set B=A^-1, N=B²-B, D=B²-2B+2I. Verify the exact ORDERED noncommutative identity D*D-N*N=(4I-B*B)+(B-2I)*[-(B+B*)](B-2I)>=0, using ||B||<=2 and B+B*<=0. D is invertible because B has left-half-plane spectrum, establishing R(A)=ND^-1 contractive; strict dissipativity gives positive definiteness. In mass-weighted physical coordinates, each polarized relative generator is G^(1/2)diag(-alpha_i +/- i Omega_i)G^(1/2), where G=I+ss*>=I, so its least singular value exceeds rmin, Hermitian part is negative definite. The center-of-mass direction is fixed and relative components contract; longitudinal real drag also contracts. Scalar imaginary arguments just below 1/2 amplify, and a positive-drag rational one-species witness realizes this physically. Independent random nonnormal SOS matrices, positive-drag mass-weighted sources and the exact rational witness corroborated; no claim for nonlinear state updates.

## originality

PASS

Compared exact statements, not shared terminology. Norm contractivity for all initial vectors in a nonnormal matrix is strictly stronger than eigenvalue inclusion in the scalar stability region. The inverse-singular-gap SOS identity supplies the missing matrix implication. Previously stated scalar stability plus energy-residual bookkeeping does not automatically imply the operator-norm estimate. A general matrix-function theorem with precisely this inverse gap could subsume it but was not found. The new object is a universal operator norm inequality, not a scalar data table. The original scalar threshold is expressly acknowledged prior, while its universality for full energy is the new assertion. A spectral-radius bound does not imply contraction for nonnormal matrices. The positive-semidefinite ordered factorization and physical singular lower bound are necessary new logical steps not contained in the accessible summaries.

## value

PASS

Scalar eigenmode stability alone does not exclude nonnormal transient amplification; an all-vector kinetic-energy inequality is the physically relevant stability guarantee for mixed charged dust and gas. The theorem supplies a general exact matrix inequality and sharp switching coefficient for the published stiff source step, not merely a repetition of scalar stability region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
