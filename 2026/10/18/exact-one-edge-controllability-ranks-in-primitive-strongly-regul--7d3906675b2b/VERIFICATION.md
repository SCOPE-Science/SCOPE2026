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

# Verification

Run `python3 verify_srg.py` from the directory containing this document; only the Python standard library is required. It constructs eight strongly regular graphs (cycle five, Petersen, rook graphs of orders three and four, triangular graphs of orders five and six, Paley thirteen and Shrikhande). For each graph, every edge is perturbed by conductance 1/2, 1, 3/2, or 2, and exact-rational Gaussian elimination determines the span of the first seven Krylov columns at every vertex. The program independently determines graph parameters and verifies the precise rank classes and total count.

Observed result: `VERIFY_OK 14846 exact finite checks across 8 strongly regular graph examples`.

The finite experiments cannot prove the universal theorem; the full mathematical argument is in `RESULT.md`. Positive conductance values outside the finite test set are covered by proof, not experiment. Independent audit has not been performed.
