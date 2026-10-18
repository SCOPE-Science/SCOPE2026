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

Execute `python3 verify.py` with Python 3 and its standard library. The program constructs directed adjacency lists from each literal edge orientation of \(F_n\), computes indegree parities and uses topological deletion to decide acyclicity without using the transfer's directed-triangle criterion. It independently compares all \(699{,}048\) orientations for \(2\le n\le10\) with the four-state formula across all \(2{,}044\) globally feasible parity fibres. It also confirms the exact unrestricted parity-fibre size, the obstruction criterion, and the total count in each order.

For \(11\le n\le16\), it enumerates all parity inputs to the transfer (not all graph orientations), checking every predicted zero pattern and the sum of counts. A successful run prints `VERIFIED` after the individual case summaries.

The proof for all \(n\ge2\) is in `RESULT.md`. These finite tests are not an infinite certificate. Independent external audit has not been performed.
