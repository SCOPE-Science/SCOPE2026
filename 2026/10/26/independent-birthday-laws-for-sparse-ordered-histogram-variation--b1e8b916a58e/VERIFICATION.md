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

# Verification of the explicit sparse-occupancy law

Run `python3 verify.py` with a standard Python 3 interpreter; it has no nonstandard dependencies. The companion `verification_output.txt` records the test results.

The checker exhaustively enumerates all \(n^N\) ordered samples for each \(2\le n\le6\) and \(2\le N\le5\), independently reconstructing the count vector, histogram variation, ordinary collisions, and adjacent-label pair collisions. It checks the exact pathwise identity, the elementary domination and triple-collision comparison, both pair kernels, the finite one-dimensional and joint Poisson total-variation bounds, and the two Stirling/binomial maximum-event formulas. The recorded run passed 75,160 assertions. It also prints 60,000 seeded simulation diagnostics at larger parameters without treating empirical agreement as proof.

The analytical argument uses the dependency-process theorem of Arratia, Goldstein and Gordon with the convention that standard total-variation distance is the supremum over events, half the two-sided norm in that paper. The finite checks do not cover arbitrary input sizes and cannot certify asymptotic or originality claims. Independent audit: not performed.
