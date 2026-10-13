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

# Reproducibility and scope

Run `python3 verify.py` using Python 3 and only its standard library. A successful execution prints `VERIFY_OK exhaustive_n=3..5 labelings= 59805 independent_2supports_n=3..6 exact_minimum_and_multiplicity_n=3..18`.

The direct enumerator checks the Roman neighborhood condition on each individual three-valued labeling of \(T_n\) for \(3\le n\le5\). A logically different enumerator ranges over all possible label-two edge subsets and independently counts free zero/one choices for \(3\le n\le6\). Their coefficients agree with the inclusion-exclusion expression. Further exact integer computations compare minima, optimal counts, and highest-degree coefficients through \(n=18\).

These are finite regression tests and not a substitute for the proof over all integers \(n\ge3\). The proof is the forced-label bijection, inclusion-exclusion of isolated vertices, and a sharp edge-cover equality argument in `RESULT.md`. The previously published minimum weight \(n-1\) is credited there; no claim of third-party validation is made.
