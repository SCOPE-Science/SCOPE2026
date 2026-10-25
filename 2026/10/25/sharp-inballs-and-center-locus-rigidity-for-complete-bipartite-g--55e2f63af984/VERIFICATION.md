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

# Computational verification

The standalone `verify.py` uses Python 3 standard-library arithmetic only. Replay by running `python3 verify.py` from this directory.

The exact-rational phase enumerates all nontrivial cut-size types \((a,b)\) for \(345\) complete-bipartite parameters with \(2\le p\le24\) and \(p\le q\le27\). It compares each squared facet-support distance with the proposed exact squared radius and identifies every minimizing cut type. It checks \(79{,}994\) cut-size types without floating-point thresholds.

A separate Decimal phase at precision \(75\) checks the center-interval inequalities for all two-row graphs with \(3\le q\le70\), plus the exceptional four-cycle, totaling \(7{,}521\) constraints. It also checks that a nearest-middle cut attains the two-row endpoint bound. Tolerances are explicitly confined to this corroborative Decimal phase.

Observed local replay output:

`EXACT_OK bipartite_pairs=345 cut_types=79994; CENTER_OK high_precision_constraints=7521; q=3..70 and C4`

These tests do not prove any universal statement outside the tested ranges. The general theorem uses the analytic Laplacian bound, strict finite-order exceptions, and exact supporting inequalities in `RESULT.md`; no sampling or linear-program termination claim replaces proof.
