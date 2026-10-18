---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Analytical and computational verification

The proof is self-contained: differentiating the two stated first integrals gives zero exactly; regularity of the \(H\)-levels makes the periodic annulus; the first Fourier harmonic of the forced oscillator gives the exact \(I_1\) coefficient and its positive sign. No parameter interval is justified solely by finite simulation.

The included `verify_period.py` uses Python 3, NumPy and SciPy to check five parameter cases, a sample strictly monotone period window, original-time orbit return, and numerical conservation of both first integrals. In particular, for \(a=1\), \(c=1.2\), the analytic derivative is about \(1.34713618252\), agreeing with a centered period difference. The calculations test numerical transcription, not uniqueness of the result in the literature or infinite-time behavior outside the described region.

No independent mathematical audit or independent certification has been conducted.
