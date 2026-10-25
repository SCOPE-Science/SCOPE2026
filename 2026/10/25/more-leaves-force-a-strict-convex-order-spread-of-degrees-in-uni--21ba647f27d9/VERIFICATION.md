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

# Reproducible exact checks and scope

Run `python3 check.py` in this directory. The program uses standard-library `fractions.Fraction`, `itertools.product`, and `math.comb`; it requires no third-party data, network, or dependency. The output from an actual successful invocation is copied verbatim into `CHECK_OUTPUT.txt`.

It checks 989 complete analytical probability laws (normalization, constant mean, and size-bias), 461175 two-by-two likelihood-ratio inequalities, and 27434 integer-hinge convex inequalities. It also independently enumerates all Prüfer words at orders \(4\le n\le8\), checking 20 complete conditioned distributions, and checks 1953 strict Stirling-ratio comparisons. These computations are finite diagnostics, not an exhaustive proof for arbitrary order. The universal proof is the real-rooted Bell-polynomial induction, strict Stirling-ratio comparison and size-bias identity in `RESULT.md`.

No independent mathematical assessment is asserted.
