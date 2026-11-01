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

# Reproducibility

Run `python verify_cut_cycle.py` using Python 3 without third-party packages. A complete recorded run is supplied as `verification_output.txt`. The script independently computes period-two states using the specified update, applies the exact phase-cut polynomial, and checks every coefficient. It exhausts every labelled connected simple graph on two to four vertices (8,900 state trials); complete graph size six alone contributes 1,000,000 chip-vector trials; every path and cycle of sizes three through eight is also tested. The final printed success marker is `GRAPH_CUT_TWO_CYCLE_VERIFY_OK`. Its three large finite-size asymptotic diagnostics are numerical observations only and are not an infinite proof.

The proof's noncomputational steps are the Laplacian complementary-phase lemma, the converse interval construction, generating-function summation, reciprocity, Stirling/Laplace concentration and the uniform conditional triangular-array Gaussian argument. Testing does not establish mathematical originality. Independent external audit has not been performed.
