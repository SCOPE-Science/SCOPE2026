---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The scalar impulse response g(t) has precisely one maximum at t0=log(kappa/lambda)/(kappa-lambda), with equal-rate limit t0=1/lambda. On t>d the derivative of g(t)+m g(t-d) is a difference of two positive exponentials (equal-rate: an affine times exponential), giving at most one post-input maximum. For d>t0, the pre-input maximum exists and the right derivative at d is m+g'(d)=m-Q(d): it is positive exactly in the two-peak regime. At equality the post-input profile immediately decreases, so it remains one maximum. Q=-g' is strictly increasing then decreasing with unique max at d=2t0, m*=r^{-(r+1)/(r-1)} or e^-2 for coincident rates; this gives two delay cutoffs and full reentrant intervals. I independently verified peak-time/derivative identities and exact m*=1/9 at lambda=1,kappa=3, plus both equal/unequal rate boundaries; the all-real-parameter claim follows analytically.

## originality

PASS

Comparison by actual mathematical hypotheses, conclusions and implications, including the closest primary works and structured equivalent/general/table checks; best-of-knowledge acceptance with explicit historical-priority risks.

## value

PASS

The exact if-and-only-if two-peak criterion for a physical two-depot first-order absorption/elimination response determines a genuinely counterintuitive reentrant window as the delay increases. The mathematical notion of local modes and its equality boundaries are naturally motivated for delayed release, and distinct from simple waveform plots. It is a model theorem, not a patient-specific dosing recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
