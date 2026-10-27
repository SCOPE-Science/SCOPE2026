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

The argument is analytical for all integers \(r\ge1\), \(N\ge4r\). It proves the Neumann-resolvent bound, an exact first-truncation total-variation identity, and the two endpoint-norm estimates. The minimum-codegree conclusion is obtained by comparing integer-separated main terms with their explicit error intervals, not by extrapolation from finite cases.

For optional exact-rational finite checks, install dependencies from `requirements.txt` and execute `python3 CHECKER.py`. One completed execution returned:

`DENSE_COMPLEMENT_EXACT_OK graphs=11 columns=606 examples=[(8, 2, 20), (10, 2, 35), (12, 2, 54), (14, 2, 77), (12, 3, 48), (14, 3, 70), (16, 4, 88), (12, 3, 48), (16, 4, 88), (8, 1, 24), (12, 2, 54)]`

The checker independently grounds and inverts each complement Laplacian over the rational numbers, computes all electrical-current columns, and checks both claimed inequalities and the exact truncated-variation identity. Tested deleted graphs include cycles, random regular graphs, disjoint cliques, a perfect matching, and a four-dimensional hypercube. A finite sample does not establish statements for untested parameters; the proof supplies that coverage.

The columnwise inequalities, edge-codegree minimum criterion, and projection normalization were separately checked against the exact definitions. No independent external mathematical review was conducted.
