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

The overlap integrals give the stated piecewise sine form; for delay at least 1 the remaining sinc zeros are simple. In the lower strip set r=(2−τ)/τ and T=πτν. At nonzero Doppler a multiple zero of F=sin(rT)−2sin T must satisfy 4(sin² T+r⁻² cos² T)=1. This excludes 1<r<2. At r=2 the factorization 2sin T(cos T−1) gives simple odd multiples, cubic nonzero even multiples, and a quadratic zero at ν=0 after division by πν. For r>2 the multiple zeros have F_TT=−2(r²−1)sin T≠0 and F_r=T cos(rT)≠0, giving regular nodal points, nondegenerate folds, and an isolated simultaneous-zero set of (F,F_T). At ν=0 the sole nodal point has A_τ=−3. The density step is valid: the rescaled maps near the irrational-flow recurrence converge in C¹ and have an invertible limiting Jacobian. Independently, choose first-quadrant phases θ(r),φ(r) with sin²θ=(r²−4)/(4(r²−1)), sinφ=2sinθ and cosφ=2cosθ/r. Then T=2πn+θ is a double-zero frequency whenever 2πnr+rθ−φ is a multiple of 2π. Its derivative in r is 2πn+θ, so on every fixed open r-interval inside (2,∞) the image contains such a multiple for large n. The frozen CHECKER.py and CHECKER_OUTPUT.txt were inspected but not executed. A separate high-precision solve recovered the three logged delays (approximately 0.51108368717, 0.60125992786, 0.50581267973) with |F|, |F_T| and |A| below 3×10⁻⁶⁰ and nonzero F_r and F_TT. Those spot checks corroborate folds, not density or completeness. Joint analyticity is only asserted for 0<τ<1; density is not a fixed-band statement.

## originality

PASS

The overlap formula and the classical ambiguity transform are not credited as original. The supported distinct claim is the full Doppler multiplicity threshold together with the dense nondegenerate delay folds, the exceptional cubic resonance lattice, and joint nodal regularity. The closest indexed Fourier-zero result and the inspected pulse-ambiguity theorem do not cover this combination or imply its density step.

## value

PASS

For the elementary signed two-pulse waveform the result identifies a sharp boundary between simple and multiple directional zeros and explains how dense critical delays coexist with a regular joint nodal curve. This is useful for interpreting sections and projections of a basic time-frequency example; the high-frequency restriction is substantive and prevents a misleading finite-band conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
