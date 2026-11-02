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

Run `python verify.py` with a standard Python 3 interpreter. The program uses no external packages and constructs all open-neighborhood bitmasks directly from the deleted-matching adjacency condition. It enumerates **every** vertex subset of each crown graph for \(2\le n\le9\), checks the original locating-domination predicate (nonempty and distinct signatures among unselected vertices), then compares full cardinality counts with both an independent pair-occupancy test and integer binomial coefficients.

The first checked total counts, for \(n=2,3,4,5,6,7,8,9\), are respectively \(9,36,149,588,2103,7178,23913,78552\). The corresponding minimum sizes are \(2,3,4,4,5,6,7,8\). Integer coefficient checks additionally verify the minimum-count expression and total count for all \(5\le n\le200\). Successful execution prints `VERIFY_OK`.

These are exhaustive checks **only** for the enumerated finite graphs and exact algebraic evaluations at finite parameter values. The all-parameter proof and the Poisson limit require the symbolic arguments in `RESULT.md`; the program does not certify them independently. Independent audit has not been performed.
