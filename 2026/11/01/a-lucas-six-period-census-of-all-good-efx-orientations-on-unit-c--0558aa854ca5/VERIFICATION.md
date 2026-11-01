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
# Verification and limitations

Run `python3 verify.py` using Python 3 standard library. It exhaustively constructs the \(2^n\) labeled edge orientations for each \(n=3,\ldots,14\), evaluates the original all-good EFX inequalities for every ordered pair of agents and every edge held by the second agent, and independently checks the prohibited cyclic-triple rule, the Lucas–six-period count, and each even change-count layer.

The final line observed when the standalone program was run is `VERIFY_OK n=3..14`. The total satisfying counts are \(2,6,12,20,30,46,74,122,200,324,522,842\) for \(n=3,\ldots,14\). The proof in `RESULT.md`, not the finite check, establishes the theorem for all \(n\ge3\).

No claims are made for heterogeneous valuations, multigraphs, the relevant-good-only EFX variant, or independent external certification. Literature-coverage uncertainty remains possible.
