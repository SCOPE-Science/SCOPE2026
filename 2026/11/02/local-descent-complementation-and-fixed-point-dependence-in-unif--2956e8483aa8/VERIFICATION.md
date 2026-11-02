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

The standalone file `verify.py` is executable with Python 3 and only the standard library. Run `python verify.py` after extracting it from the same package.

It enumerates all involutions for each \(2\le n\le10\) and checks their counts against the recurrence. For every eligible descent position it verifies the exact probability \(1/2\), the predicted pairwise covariance against every fixed-site indicator, the full fixed-point-count/descent covariance, and every conditional descent probability in every realized pattern of **all remote fixed-site bits**. It checks the global fixed-point-count/total-descent covariance as well. For every involution and adjacent site pair it also checks that the explicit map is an involution, reverses the descent and preserves the entire remote fixed-site pattern. The final run reported `PASS: 345599 exact assertions` and enumerated 9,496 involutions at \(n=10\).

The proof of the all-size assertion is the explicitly defined local involution and the exact conditioning/counting argument in `RESULT.md`. Finite checks do not establish infinite statements. There was no computer-assisted infinite certification or independent audit.
