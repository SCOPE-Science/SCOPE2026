---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For equal cyclic shifts an unnormalized off-diagonal overlap is 1+omega or 1+omega^2, a negative cube root of unity; for distinct shifts the supports meet at one coordinate and the overlap is a negative cube root of unity directly. Normalization divides the overlap by 2. The charge-three addition kernel then yields constant off-diagonal -a_q/8, unit diagonal, and the two orthogonal eigenspaces as stated. Harmonic dimension follows by subtracting the lower-bidegree trace dimension. I independently checked every q=0..899 by exact evaluation of the Jacobi binomial sum, not the uploaded recurrence, with /workspace/branches/audit_exact.py. For the infinite tail, writing R(e^{it})=e^{it/2} times a square root of (1+2 cos t) gives the two boundary inequalities by orthogonality on the indicated arcs. The algebraic partners give products z and -3z so there are no interior zeros of the two factors; at z=0 they are 2. The minimum modulus principle gives the interior bounds. Separation of the two branch points and Cauchy's inequality give |p_q|<30 sqrt(q+1)<q+1 for q>=900. For q=1, a_q=-5/4, neither eigenvalue vanishes. At q=0,2 the pseudoinverse gives the stated norm on the actual phased mean-zero image; rephasing changes that hyperplane by diagonal unitaries. No dependence on an uploaded executable.

## originality

PASS

The charge-three all-index equality classification, not the general kernel, the Hesse overlap geometry, or the holomorphic cubic obstruction, is the distinct part. A same-day result reproduces the q=2 matrix but in a different harmonic sector using different Jacobi parameters; this is not coverage of the charged cutoff.

## value

PASS

The same nine Hesse samples are used on a natural sequence of increasing-degree fixed-charge harmonic spaces. The result identifies exactly which spaces can interpolate arbitrary data and isolates a nonholomorphic rank defect, with conditioning and minimum-norm consequences. That exact boundary is not supplied by a positive semidefinite kernel formula or a few low-degree computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
