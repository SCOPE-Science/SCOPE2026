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

Checked the continuous transform in the specified 2π Fourier convention and reconstructed the Gaussian integral. The two phase-space Jacobians cancel. For fixed horizontal translation v the shear is confined to the span of j(v) and the central axis, a two-by-two block with determinant 4+ε²|v|²/4. Thus det M=2^d H, H=1+ε²|v|²/16. Since v is orthogonal to j(v), completing the square gives |v|²/2+c²/(2H). The modulation and central-translation Gaussian integrals leave the power H^(1−p/2) and the horizontal radial law πp|v|²/2 ∼ Gamma(n,1). At p=2 the joint spectrogram has mass one; direct expectation of its negative log gives E log H+n+1/2+d/2=d+E log H. The finite Gamma moments justify both quadratic expansions; dominated convergence gives sharpness. In the cited upper bound, the Young step acts on the nonzero functions |f̂|^(p′), |ĝ|^(p′) (with inversion of the first) with input exponents 2/p′ and output p−1, all strictly interior for p>2. Strict Young at those exponents rules out STFT equality. The entropy assertion is an infimum, not a global equality classification. The uploaded numerical support was inspected, not executed, and is not used as proof. In RESULT.md's intermediate Gaussian modulation integral, the differential is understood in the rescaled modulation coordinates (the reciprocal Jacobian belongs to the central translation).

## originality

PASS

The universal inequalities and the Young nonextremizer result are prior work, not credited here. The exact normalized Heisenberg-STFT Gaussian moment and entropy curves and their deficits supply a sharpness proof for a specific question explicitly left by the primary STFT paper. The one-step deduction of STFT nonattainment from interior Young nonattainment is not independently credited as an original mechanism. No checked source covers the distinct quantitative claim.

## value

PASS

Resolves whether the known continuous Heisenberg-STFT bounds can be approached, despite the absence of maximizing pairs for p>2. The complete finite-width curve and leading defects quantify the effect of the noncommutative shear in every dimension, beyond an existence proof for a saturating sequence. No general stability or all-extremizing-sequences assertion is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
