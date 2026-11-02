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

PASS: Rebuilt both normalized MGFs M0=cosh(t), Mq=1-q+q cosh(2t), proved factorization (cosh t-1)(2q(cosh t+1)-1), and verified monotonic vq/v0=4q(1+sinh²t)/(1+2q sinh²t). For 0<q<1/4 that ratio crosses one only once, implying inverse tilts tq(v)-t0(v) change sign once, so J(v)=Iq(v)-I0(v) increases then decreases. Endpoint Legendre inversion with I0(1)=log2, Iq(2)=log(2/q) covers both finite-tilt and saturation regimes. Monotone Iq(1) determines unique qc and the cubic elimination; independently verified qc=0.1452003303264 and 56 speed-order checks. Claimed speed is only a linear-determinacy functional, not automatically nonlinear front velocity. Strict q=1/4 and q=1 are covered.

## originality

PASS

PASS best-of-knowledge for the full two-atomic-kernel q/R order, unique reversal, and secondary post-saturation threshold, excluding known general MGF variational speed and qualitative growth-dependent ranking. Kot et al. 1996 materially inspected via the accessible full PDF at pp.2029-2031. General large-deviation ordering priority remains a risk.

## value

PASS

PASS: local vs rare two-step dispersal is a motivated competing-kernel model; exact all-growth one-switch behavior, probability threshold 1/4, and the secondary saturation cutoff qc distinguish two mathematically different speed-reversal regimes. This goes beyond numerical curves or a routine substitution into the MGF speed formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
