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

# Verification and scope

Run with `python verify_clique_bouquets.py` using Python 3 and the standard library. The checker constructs adjacency sets afresh, simulates the ordinary blue-only forcing rule to a fixed point, and compares it with the claimed initial-set characterization for each candidate subset. It separately calculates every predicted polynomial coefficient and executes a polynomial-division reconstruction of the peripheral size profile. Its observed output is preserved in `verification_output.txt`.

The exhaustive run covers 38 peripheral-size profiles, at most three cliques with sizes in \(\{2,3,4\}\), and 37,336 starting subsets. Three finite numerical critical-window sequences with homogeneous clique size \(2\), \(3\), and \(5\) are diagnostic only. The infinite polynomial and probabilistic limit require their analytic arguments in RESULT.md; finite checks cannot prove them. No independent audit has occurred.
