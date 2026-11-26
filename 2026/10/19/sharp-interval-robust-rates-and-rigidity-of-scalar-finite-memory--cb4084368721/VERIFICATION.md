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

For one tap, the maximum of |a+k0| on the interval is t+|c+k0|. With at least two taps, k0=-c and k1=-t²/4 yield the characteristic factor z²-(a-c)z+t²/4; its roots have modulus t/2 throughout, including the double roots ±t/2 at the endpoints. For arbitrary gains, let r be their maximum spectral radius and L(z)=z−Σ k_j z^(−j). For positive R≥r the open exterior |z|>R omits the entire uncertainty interval under L, by p_a(z)=z^(H−1)(L(z)−a). Applying the inverse Joukowski map Φ of that slit and the reciprocal gives a disk self-map g(ζ)=1/Φ(L(R/ζ)), removable at zero with g(0)=0 and g′(0)=t/(2R). If r<t/2 take positive r<R<t/2 to contradict Schwarz. At r=t/2 take R=r; the derivative is positive one, hence g is the identity. Inverting yields L(z)=c+z+t²/(4z), fixing every Laurent coefficient. Continuity of the companion spectral radius on the compact interval makes pointwise strict Schur stability equivalent to a maximum <1; the thresholds are strict. At t=0 exact cancellation puts all poles at zero. Read the proof and support; no numerical test is used to establish the continuum bound or rigidity. The result is for fixed drift and fixed real taps, not switching, general compensators, or an endpoint power estimate at repeated poles.

## originality

PASS

The closest inspected comparisons do not establish the sharp all-length full-interval radius and its rigidity for the fixed FIR state-feedback class. This finding is supported as distinct to the extent of available evidence, not a priority certification for robust Schur theory or for the classical slit map.

## value

PASS

The prior two-plant example motivates a concrete memory question. Quantifying the greatest benefit of any finite number of taps for a full drift interval and proving that only one lag is needed, with a unique optimum and exact thresholds, converts it into a useful sharp design theorem. The nonattainment of strict stability at the critical widths is meaningful; the claim is not merely a familiar existence test or an empirical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
