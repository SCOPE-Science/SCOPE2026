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

Use the translate-incidence Gram A=T*T for Tf=f_P*1_H. Each diagonal is q−1. For ordered u≠v in F× the collision equations force s−t=u−v and s+t=−1/(uv), with exactly one solution because 2 is invertible. Equal hyperbola parameters force equal parabola parameters. Thus S=1*A1=2(q−1)^2 and Q(1)=S/[q(q−1)]. Since S≡2 (mod q), the integral row sums are unequal, so the constant vector is nonstationary on the normalized sphere and not a local maximum. Balancing integer row sums gives ||A1||²≥S²/q+2(q−2)/q (the balanced floor/ceiling counts are q−2 and 2). Applying A²≤λ_max(A)A to 1 and dividing the resulting eigenvalue bound by q−1 gives the claimed gap. This includes characteristic three for q≥9, and claims neither the sharp value nor a two-variable norm. The frozen checker tests only prime fields; independent replay /workspace/branches/frozen-review-replay.py directly groups pairs by their output and checks exact Gram sums/variance in q=5,7,9,25, with numerical top-eigenvalue corroboration only.

## originality

PASS

The reviewed contribution is the mixed Gram collision count and its uniform quantitative obstruction to flat-input extremality. The closest inspected records and primary theorems apply to self-convolution or single-surface extension, not to this mixed operator. The integer-variance and spectral inequalities used thereafter are standard, not claims of originality.

## value

PASS

This is not an improvement of a sharp numerical constant by a tiny amount alone. It establishes that constants are not even stationary throughout a natural mixed problem juxtaposed with single-surface flat extremizers, with an exact count and a size-uniform arithmetic certificate valid even in characteristic three. The small explicit lower bound certifies that qualitative separation; the theorem does not claim to optimize the gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
