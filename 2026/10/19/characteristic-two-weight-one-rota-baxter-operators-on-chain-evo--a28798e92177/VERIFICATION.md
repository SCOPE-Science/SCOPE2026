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
# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 installation; no third-party dependencies are required. The program constructs the finite fields of orders \(2,4,8,16\) using the irreducible polynomials `0b11`, `0b111`, `0b1011`, and `0b10011`, respectively. For each tested dimension, it exhaustively enumerates all \(q^n\) first-column vectors, reconstructs the forced operator from its first column, tests all \(n(n+1)/2\) basis pairs in the weight-one Rota–Baxter identity, computes actual operator ranks by Gaussian elimination in the finite field, and compares the accepted vectors with a separately generated parametric classification.

The checker succeeds in 19 configurations: \(n=2,\ldots,8\) for \(q=2\); \(n=2,\ldots,6\) for \(q=4\); \(n=2,\ldots,5\) for \(q=8\); and \(n=2,3,4\) for \(q=16\). In particular, it finds exactly \(28\) operators when \((q,n)=(2,8)\), \(112\) when \((q,n)=(4,6)\), \(400\) when \((q,n)=(8,5)\), and \(1216\) when \((q,n)=(16,4)\).

This is finite exhaustive validation of those cases only. Arbitrary fields and arbitrary dimensions are handled by the proof in RESULT.md, not by extrapolation. No external review or certification has been performed.
