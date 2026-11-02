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

# Verification details

The proof rests on the permutation-invariant quadratic-form reduction, two exactly attained dual norm maxima, the signed-mass transfer inequality, and strict monotonicity on either side of the optimal interpolation scale. The parameter boundaries \(\tau=2j\) and \(\tau\ge2\lfloor n/2\rfloor\), and the exceptional cases \(n=2,3\), are included.

The companion `checker.py` is a standard-library exact-rational cross-check for the two sphere factors and a finite rational coordinate grid. Its successful run reports 310,298 grid vectors and 210 exact rational assertions. The finite grid is not an exhaustive proof over real vectors; the theorem is proved analytically in `RESULT.md`.

No independent audit or independent mathematical validation has been performed. Historical priority under all possible terminology has not been certified.
