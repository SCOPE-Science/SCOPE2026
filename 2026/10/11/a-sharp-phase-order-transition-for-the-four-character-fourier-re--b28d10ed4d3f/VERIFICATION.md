---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For positive A,B,C,D, scalar and independent torus rotations fix three coefficient phases and leave theta=arg(ad/bc). Haar integration in z yields Phi_s(X(t),Y_theta(t)) with X=A^2+C^2+2AC cos t and Y=B^2+D^2+2BD cos(t+theta), s=p/2. Generalized binomial coefficient recurrence gives hypergeometric ODE and the exact off-diagonal Phi_XY = s^2/sqrt(XY) E[cos t (X+Y+2sqrt(XY)cos t)^(s-1)], with strict sign of s-1 by monotone covariance; s=1 gives Phi=X+Y. At X=Y, continuity and integrable local diagonal singularity permit finite four-corner super/submodular inequalities without an unwarranted global C2 assertion. Two centered cosine superlevel arcs have overlap L(u)=(alpha+beta-u)_+-(abs(alpha-beta)-u)_+ +(alpha+beta+u-2pi)_+, nonincreasing with phase separation, strictly decreasing at alpha=beta=pi/2 on [0,pi]. Applying finite grid mixed differences and refining yields strict moment ordering for every two distinct separations, and opposite extrema for p below/above 2. Zero coefficient removes essential phase; p=2 is orthogonality. The independent arithmetic and quadrature checks corroborate identities but do not replace the analytic proof.

## originality

PASS

Best-of-knowledge pass for the precise all-positive-real-exponent fixed-modulus rectangle theorem: neither the inspected global UMP results nor the fully inspected finite-support publications furnish the exact strict phase-distance order for every p>0 and every strictly positive quadruple. Classical supermodular rearrangement is directly relevant to the endpoint optimizers, but the case-specific signed mixed derivative, strict intermediate angular order and sharp reversal across p=2 still require a nontrivial implication not located in an inspected primary statement. Full Gressman and Burchard texts were not available in this run; treat them as explicit priority risks, not decisive whole-document exclusions.

## value

PASS

The frequency rectangle {(0,0),(1,0),(0,1),(1,1)} is a canonical minimal non-affinely-independent two-variable Fourier support. For arbitrary prescribed positive amplitudes, the theorem resolves the exact sharp cross-phase optimizer at every positive real Lp exponent, proves strict monotonicity for all intermediate phase shifts, pinpoints universal sign change at p=2 and classifies equality and zero-amplitude boundaries. This motivated structural phase-selection law is a nontrivial all-exponent sharpening of routine even-moment convolution and of general existence-of-failure theorems; it can serve as a quantitative benchmark in the majorant problem without requiring downstream conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
