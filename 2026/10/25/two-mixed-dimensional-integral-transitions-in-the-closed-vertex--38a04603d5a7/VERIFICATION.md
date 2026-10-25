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

# Exact finite verification

The standalone Python 3 program `verify.py` uses no third-party packages. It reconstructs the Folkman graph as the subdivided double of \(K_5\), computes all twenty shortest-path distance rows with breadth-first search, and explicitly derives maximal vertex balls at radii one and two. It enumerates **every** nonempty simplex of the finite nerves. Each of 130 and 39,641 deleted face pairs is required to satisfy the unique-immediate-coface condition at the time of deletion; this is exactly the simplicial free-face condition. It checks that the remaining faces form a subcomplex, then constructs the signed integral simplicial boundary matrices. Only unimodular integer operations with pivots \(\pm1\) are permitted; all residual entries must vanish. This verifies both integral ranks and the absence of torsion, not just rational or finite-field Betti numbers.

An independent mod-two Gaussian elimination computes each boundary rank from its simplex incidence data. This duplicate arithmetic corroborates the signed integer calculation. The output is reproduced in `verification_output.txt`, and the script ends with `VERIFY_OK`. The calculation is exhaustive for a **single finite graph**; it does not imply uncomputed homotopy types or any infinite graph-family theorem.

The combinatorial nerve of finite vertex balls at radius \(k\) equals the **even-scale** \(2k\) vertex-centered graph-geometric Čech complex. The program makes no assertions about the intervening odd conventional scales, independent certification, or additional homotopy equivalences.
