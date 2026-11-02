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

# Verification notes

The proof is the basis for the all-graph claim. `verify.py` is a standalone Python 3.10+ script requiring only the standard library.

It exhaustively enumerated connected labeled graphs of orders two to six and checked exact equivalence between a mixed sign coloring with a same-sign neighbor everywhere and a matching of size at least two. The resulting counts were (1,0), (4,0), (38,34), (728,723) and (26704,26698), where each pair is total connected graphs followed by qualifying graphs. It additionally iterated the four-path fixed-point map with \(K=2\), \(\delta=1/250\), \(\beta=4\), measured residual below \(10^{-12}\), and checked the analytic Lipschitz-bound expression gives a value below 1/4 on a radius-\(10^{-4}\) sup-norm neighborhood. All executable assertions passed.

The computed numbers use ordinary floating point and do not substitute for interval proofs. Unbounded graph size, the strict finite-parameter local stability guarantee, and the matching characterization follow analytically from the complete argument in RESULT.md. The independent audit remains unperformed.
