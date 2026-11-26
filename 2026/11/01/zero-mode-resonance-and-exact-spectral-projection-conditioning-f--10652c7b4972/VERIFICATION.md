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

The Fourier characters are eigenvectors of U with dense eigenvalues on the circle. For a≠b, conjugation of diag(aU,bU) by the upper shear S with off-diagonal M_h gives coupling b h−a h∘R_α=c. The Fourier denominator b−a exp(inα) is nonzero and the finite sum defines a bounded multiplier; this fixes the sign of the conjugated Riesz projection, whose row is (1,−h) pointwise and whose norm is sqrt(1+||h||∞²). The known ergodic component bound for a two-dimensional fiber applies; this operator attains it. Near a=b=r the nonzero-frequency part of h converges uniformly, while the constant term is exactly c_0/(b−a). Its norm differs from that term's modulus by a bounded amount even for either sign of b−a. This proves the scaled gap limit and the bounded norm limit for c_0=0. The two-mode norm follows by exact phase alignment, including when either coefficient vanishes. At collision, write c=c_0+r(h−h∘R_α) using the nonzero harmonics. Directly raising the triangular factorization to the N-th power and removing diag(U^N,U^N) leaves unit diagonal and off-diagonal multiplication by Nc_0/r+h−h∘R_α^N. The last two terms are uniformly bounded; the diagonal contributes norm one, so dividing by N yields |c_0|/r and the power-boundedness criterion for r^(−N)T^N. Off the circle the triangular resolvent is invertible, and the invariant first-coordinate subspace supplies the dense eigenvalues on the circle, so no further spectral issue arises at collision. The proof's 'rank-one upper-block' terminology refers to fiber rank, not rank on the whole L² space; only its norm is used.

## originality

PASS

The supported distinction is the sharp quantitative calculation for fixed irrational rotation and finite Fourier coupling: explicit Fourier dependence of the exact norm, the residue at a closing gap, and the collision dichotomy with an exact power-growth coefficient. Prior decomposability, the fiber-dimension component ceiling, triangular norm identities, and classical shear/cohomological methods are credited rather than claimed as new.

## value

PASS

The known component bound addresses how many spectral pieces can occur, not whether the splitting stays well conditioned as two pieces meet. This exact two-fiber model is a useful benchmark: the same scalar harmonic controls sharp reciprocal-gap conditioning and quantitative amplification after collision, while a mean-zero near-resonant harmonic shows a different, large but finite conditioning scale at fixed angle. The general norm identity plus explicit two-frequency evaluation make these regimes distinguishable without spectral discretization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
