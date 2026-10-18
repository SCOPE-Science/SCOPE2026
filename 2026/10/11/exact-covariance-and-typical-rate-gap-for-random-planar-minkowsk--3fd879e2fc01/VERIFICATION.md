---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The planar support-function area formula gives D_0=(π/2)Σ_{m>=2}(m²−1)(a_m²+b_m²); it is valid for nonsmooth convex bodies via W^{1,2} approximation. Independent Haar-uniform reflection axes become i.i.d. first-angle/successive-difference variables. Each m-th Fourier weight is multiplied by cos² of its projected angle, giving mean 1/2, fourth moment 3/8 and cross-mode second moment 1/4. Tonelli justifies summing countably many nonnegative finite-total weights; thus Var(D_t)=((3/8)^t−4^{-t})Q and Cov(D_s,D_t)=2^{-(t−s)}Var(D_s). Q<=D0² with equality exactly one active higher harmonic. M_t=2^tD_t is a nonnegative martingale; for each fixed mode E log(2cos²(mU))=−log2, so it decays almost surely; the limit of all remaining tail martingales has mean at most the initial discarded Fourier-tail sum and hence tends to zero. Independent 256x256 angle quadrature on three Fourier modes matched two-step mean and variance exactly to numerical tolerance, but the general statement is analytic.

## originality

PASS

Best-of-knowledge: Coupier--Davydov prove expected squared centered-support contraction and general convergence of random symmetrizations, but do not state an exact Fourier-weighted intrinsic area-deficit covariance, fourth-moment equality classification or mean-normalized martingale degeneracy. These additions do not follow just from their first-moment theorem.

## value

PASS

PASS: Exact time-covariance of a natural intrinsic isoperimetric statistic, sharp geometric single-harmonic variance extremizers and an almost-sure decay vastly faster than mean are distinct useful mathematical conclusions. This refines known expected contraction in a highly interpretable stochastic-geometric model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
