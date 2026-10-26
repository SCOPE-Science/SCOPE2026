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

# Verification record

The proof uses a finite Poisson neighbourhood expansion and an exact insertion formula. The required analytic identities are \(T(( -\sigma,\sigma))=3\sigma^2\) and \(T(B_\sigma)=\sigma^4(\pi^2-3\sqrt3\pi/4)\). The first follows from elementary planar area; the second follows from an explicitly stated radial disk-overlap integral. The non-overlapping two-centre witness shows that two admissible three-event colour histories have different total acceptance counts.

Run `python verify.py` with Python 3 and `mpmath`; its archived output is `CHECK_OUTPUT.txt`. The checker passed 12 assertions: four exact rational one-dimensional identities, four high-precision two-dimensional identities, two explicit three-event tests, and two seeded independent Monte Carlo tests of exclusion-region geometry. The Monte Carlo tests check integrals, not infinite-volume correctness or scholarly priority. No independent audit or expert verification has been performed.

Limitations: the checker is not a symbolic proof assistant, not a formal certificate, and does not test arbitrarily late dynamics. The statement in `RESULT.md` and the analytic proof, rather than numerical extrapolation, establish the fixed-parameter small-time expansion.
