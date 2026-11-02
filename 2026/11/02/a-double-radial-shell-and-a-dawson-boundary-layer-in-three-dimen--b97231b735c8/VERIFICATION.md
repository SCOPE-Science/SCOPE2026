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

# Reproduction and limits

The argument is analytic. It independently checks the physical Gaussian variance normalization, Bessel integral representation, small-radius endpoint expansion, and Dawson inner scaling. The critical asymptotic implication is a local \(C^2\) limit followed by persistence of the nondegenerate maximizer of \(F\). The outer maximum is obtained from fixed positive comparison radii; no asserted global mode count relies on numerical peak finding.

Run `python verify.py` using Python 3, NumPy, SciPy; it evaluates a phase integral, the Bessel expression, the Dawson profile and finite high-amplitude shell diagnostics. A passed run is a reproducible finite numerical consistency check, not interval certification of every \(q\) or proof of an infinite limit. The complete mathematical proof and its parameter restrictions are in `RESULT.md`.

Scientific and literature limitations: only strictly positive harmonic Gaussian variances with \(0\le q<1\), dimension three, independent uniform physical phase; no finite-density damping, explicit onset threshold, or exact count of maxima. The numerical value of the unique Dawson maximum is approximate. The primary-source comparison is finite and cannot exclude all mathematical literature; independent scientific audit has not been performed.
