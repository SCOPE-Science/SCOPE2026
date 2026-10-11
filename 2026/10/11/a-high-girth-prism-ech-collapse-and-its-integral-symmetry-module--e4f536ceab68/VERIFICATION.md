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

# Reproducibility and limits

Run `python3 verify_prism.py` with the Python standard library. Expected last line: `VERIFY_OK: 41 connected girth>=5 instances, exact free-face collapses and independent mod-2 ranks`.

The verifier independently reconstructs each neighborhood generator, enumerates all nonempty simplices and every coface in the proposed descending-cardinality elementary collapse, checks the exact tetrahedral-boundary residue and compares mod-two boundary ranks with the theorem. It includes paths of orders 2–7, cycles of lengths 5–10, stars with 2–7 leaves, a three-path theta graph, the Petersen and Heawood graphs, and twenty reproducible sparse high-girth graphs. It checks the short-cycle exclusions separately. Its use of finite examples cannot establish an infinite-family claim; the unrestricted proof is in RESULT.md. The integral and equivariant conclusions follow from that explicit proof, not from the mod-two computation.

Scientific limits: no after-scale-two persistence deaths; no triangle/four-cycle base extension; novelty assessment may miss unindexed literature. Same-model review has passed. No independent audit has been performed.
