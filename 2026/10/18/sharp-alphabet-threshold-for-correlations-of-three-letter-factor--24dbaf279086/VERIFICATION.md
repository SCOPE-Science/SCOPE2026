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
Run `python3 verify.py` in this directory (Python 3 standard library only). The stdout should match `verification_output.txt`.

The checker generates every bijection from incoming to outgoing edges independently at each vertex of the complete directed graph with loops for \(q=3\) and \(q=4\). It retains exactly the matchings that induce one cyclic tour and checks every ordered pair of prescribed nonloop triples with common center against the probability formula. It separately contracts the four edges into two shortcut edges, computes the full rooted Laplacian, applies integer Bareiss elimination, and compares the resulting fraction against the reduced \(2\times2\) formula for all admissible motif pairs at \(q=3,4,5,6\). It verifies the four covariance sign regimes with exact rational arithmetic.

Successful finite tests cannot establish the theorem for all alphabet sizes. The proof in `RESULT.md`, including the BEST theorem, Matrix-Tree theorem, reversible contractions and case analysis, supplies the infinite argument. No independent audit has been performed.
