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

Run `python3 verify.py` in the directory containing `verify.py` and `certificate.json`. The verifier reconstructs the Heawood graph as the Fano-plane incidence graph, enumerates the complete ordered two-particle Abrams model, constructs both cellular boundaries over \(\mathbb F_2\), checks the chain identity on every two-cell, and recomputes ranks by exact bit-vector elimination.

Expected exact data are cell counts \((182,504,336)\), boundary ranks \((181,307)\), ordinary Betti vector \((1,16,29)\), and Euler characteristic \(14\). The computation is finite and exhaustive. It does not verify any integral-homology or homotopy-type assertion because none is claimed.
