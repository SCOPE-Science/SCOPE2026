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

The fixed-reset process has an invariant renewal mixture over exponentially distributed age; coupling with common resets and common driving noises gives uniqueness. Finite stationary moments follow from exponential age, bounded speed and the Brownian moment bounds. An independent check uses ordered times s≤t in a reset-free interval. For the sum of angles, the Fourier factor is exp[−(4D_r−2iΩ)s]exp[−(D_r−iΩ)(t−s)]; for their difference it is just the second factor. Weighting by the survival probability exp(−rt) and integrating the two ordered-time integrals yields E Z²=2v²/[(A−iΩ)(B−2iΩ)] and E|Z|²=4D_t/r+(2v²/r)Re[1/(A−iΩ)]. The mean is v/(A−iΩ). Subtracting the squared mean in each case gives the stated centered tensor, with the factor 2A−B=r−2D_r in Q. The denominators cannot vanish and v>0, so both traceless components vanish precisely at that rate. The eigenvalue gap is |Q|; reversing Ω conjugates Q, and at Ω=0 its real sign determines the principal-axis exchange. Even centered full-law symmetry need not follow: the ordered third-moment integral gives E Z³=6v³/(L₁L₂L₃) with L_j=r+j²D_r−ijΩ; at isotropy L₂=2L₁ and the centered third complex moment is −2D_r v³/(L₁³L₃)≠0. The scope requires independent noises, isotropic translational noise and Poisson resetting of both position and heading. Frozen RESULT.md lines 27–66 provide the generator proof. The uploaded quadrature code was inspected, not executed; the independent integral calculation is analytical, not a rerun of the reported 84 finite checks.

## originality

PASS

The supported distinct claim is the complete centered tensor and universal exact crossing for nonzero angular drift in the overdamped model with fixed position–orientation Poisson resetting. The match on scalar radial moments in the identical chiral model and the known achiral variance specialization are not new here. Neither determines the two independent traceless entries as functions of nonzero chirality. The strongest indexed matches alter the dynamics or the resetting protocol and observable; no equivalent or stronger covering statement was established in the bounded comparison.

## value

PASS

The fixed reset heading selects an axis and chirality permits off-diagonal covariance. The complete centered tensor therefore tests whether both forms of anisotropy can vanish together at an exact, useful calibration point. The chirality-independent rate identifies that degeneracy despite the generally nonisotropic stationary distribution and is not a restatement of a scalar spread or the known achiral crossing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
