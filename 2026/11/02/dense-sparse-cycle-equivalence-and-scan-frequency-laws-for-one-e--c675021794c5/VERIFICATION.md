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

# Reproducible verification

Run `python3 verify.py` with standard Python 3; no third-party dependencies are needed. Compare output to `verification_output.txt`. Matrix calculations use rows encoded as binary integers and exact Gaussian elimination over \(\mathbb F_2\); polynomial calculations use separate exact binary polynomial arithmetic and Euclidean gcds.

For both the one-edge-deleted complete graph and the ordinary cycle, all \(n!\) sweeps for \(3\le n\le7\) were constructed independently and all \(2^n\) states per sweep iterated to classify cycles, amounting to 5,910 scan maps and 695,472 scan–state pairs in *each* graph family. The cycle test computes its cyclic-ascent index directly and tests the same gcd formula without using the dense graph matrix. For larger dimensions up to 24, canonical scan matrices, ranks of iterates, the predicted fixed-point formula, invariant factors and order claims were checked across 15,438 exact cases. The verifier checks uniform scan-gap multiplicities separately.

The proof of the general theorem is algebraic in `RESULT.md`. Computer checks of finite dimensions cannot establish the arbitrary-size statement or prove literature novelty. No independent audit has been undertaken.
