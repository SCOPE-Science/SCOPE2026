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
# Finite verification and theoretical boundaries

Execute `python verify.py` using the Python 3 standard library. Actual replay: **PASS: 602 exact identities, 12854 weak compositions enumerated.** The program checks the exact support-size formula, zero-count first and second factorial moments, uniform support-to-gap correspondence for all enumerated parameters, the expectation of equal-positive-gap pairs given occupied support, and the positive-pair coefficient formula for general uniform weak compositions at small parameters. It raises an assertion error on any discrepancy.

The proof's asymptotic local-limit lemma is verified analytically by conditioning independent geometric terms and applying Stirling's formula to explicit negative-binomial masses. Higher-order collision diagrams, isolated-zero second moments, and factorial-moment convergence are supplied in `RESULT.md`. The verifier does not certify an infinite-domain theorem. Exploratory simulation at three increasing sizes agrees with the first-window mean but is supporting evidence only.

The terminal Poisson law arises from the exact displayed factorial moments; adjacent-zero rarity is bounded by an exact probability and is not inferred from a simulation. All claims concern uniform weak compositions of a fixed integer into a specified number of terms. The first Poisson window overlaps the published spacing theory identified in the references. Independent audit has not been performed.
