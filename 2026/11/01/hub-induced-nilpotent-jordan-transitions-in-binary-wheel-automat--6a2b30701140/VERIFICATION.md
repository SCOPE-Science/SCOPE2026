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

# Reproducibility checks

Run `python verify_wheel_xor.py` using Python 3 standard library. The standalone implementation builds the undirected wheel's adjacency masks and computes binary matrix powers without using the polynomial decomposition as an input to its matrix routine. It also iterates the vertexwise neighbor-XOR rule on the complete functional graph, marking actual periodic cycles before assigning transient distances.

Recorded successful output in `verification_output.txt`: `WHEEL_XOR_VERIFY_OK`. The finite matrix checks cover \(3\le n\le128\) with 585 power-rank comparisons. The functional-graph checks exhaust \(262128\) configurations across \(3\le n\le16\), including all first-entry shells, not merely sampled orbits. Concrete checked counts include \(n=4\): \((1,7,8,16)\), \(n=6\): \((16,16,32,64)\), \(n=8\): \((1,7,24,96,384)\), and \(n=12\): \((256,1792,2048,4096)\).

These tests are finite corroboration only. The infinite assertion is proved symbolically through a CRT factorization, exact power-rank calculations on the primary factor, nilpotent Jordan reconstruction, and Fitting decomposition. No separate external or independent audit is represented by these checks.
