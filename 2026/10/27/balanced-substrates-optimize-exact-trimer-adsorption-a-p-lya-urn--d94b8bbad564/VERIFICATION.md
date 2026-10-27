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

# Verification notes

The analytical chain is: count all available undirected three-vertex paths of each class; condition on the first accepted deposition; prove the exact rational recurrence; subtract adjacent recurrences to obtain strict unimodality; solve the extreme-feasibility product; sum all composition coefficients; convert the normalized coefficients to a balanced two-colour urn; derive the exact second moment and every limiting even moment. The final Gaussian convergence uses moment determinacy rather than a finite simulation or an unproved local-limit assertion.

Run `python3 verify_trimers.py` in the same directory. The program uses only the standard Python library. It independently enumerates labeled vacant subsets, directly determines which of the original length-two paths can next deposit, and solves those finite hitting-probability equations using rational arithmetic; separately, it evaluates the derived two-count recurrence and exact rational identities. It passed 514 checks when packaged. Finite labeled comparisons cover total sizes \(3,6,9,12\) with every positive initial bipartition; rational profile identities cover \(t\leq60\). Illustrative Gaussian comparisons cover three larger finite sizes. None constitutes a proof for all parameter sizes.

No external or independent validation has been carried out. The unrestricted claims require the mathematical arguments in RESULT.md; the remaining limitations and potential historical overlaps are stated there.
