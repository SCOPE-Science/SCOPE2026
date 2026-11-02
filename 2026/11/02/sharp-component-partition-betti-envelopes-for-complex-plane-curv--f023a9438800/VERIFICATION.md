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

The proof reconstructs the normalization Euler characteristic, uses arithmetic genus and local Milnor number \(\mu=2\delta-b+1\) and Bézout's local intersection sum, and derives the exact local error formula. It then verifies strict nonnegativity and all equality conditions. The algebraic fixed-component optimizer is the unique concentrated partition; the fixed-degree optimizer among component counts is controlled by convexity.

A standalone finite checker (`checks/betti_envelope.py`) evaluates the partition formula in two independent forms and checks unique maxima for all integer degree partitions through degree \(12\). Running it from the embedded package gives `VERIFY_OK`. This is a test of algebraic consistency, not a proof for all degrees or an independent audit.

The main theorem is proved for complex plane curves and rational singular homology of their underlying analytic spaces. Arithmetic genus and delta/Milnor conventions are those of reduced plane analytic germs. An equivalent previously published finite-degree result remains a historical-priority risk. No independent audit has been performed.
