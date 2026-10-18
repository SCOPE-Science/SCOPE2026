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

The proof is self-contained subject to the standard finite concept-lattice fact that every concept is a join of object concepts, which is reproved in RESULT.md. The critical independent checks are the four-cycle error estimate, the exact trivariate row-category probability and the row/column Efron–Stein bounded-change calculation.

To reproduce the finite check, run `python3 verify.py`. The implementation independently generates all Galois-closed extents and checks lower covers rather than applying the local irreducibility characterization as an oracle. It verifies 74,384 complete finite contexts, 22,882 of them containing no four-cycle, checks the dual lattice statements, eight exact rational mean identities, and 1,500 additional larger contexts. The observed output is `VERIFY_OK 74384 exhaustive contexts; 22882 square-free contexts; 8 exact expectation identities; 1500 additional random contexts; both lattice-dual proxies`.

These computations do not establish asymptotic convergence or originality. Mathematical originality has been compared against identified primary sources and research records, with remaining search limitations stated in REVIEW.md. No independent audit was performed.
