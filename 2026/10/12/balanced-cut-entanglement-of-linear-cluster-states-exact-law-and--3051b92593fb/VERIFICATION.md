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

# Reproduction and verification

Run `python3 verify.py` using an ordinary Python 3.9+ interpreter. The program uses only Python's standard library and prints `VERIFY_OK` when its assertions pass.

The checker constructs all \(2^n\) membership strings for \(2\le n\le14\), forms their binary cut-adjacency matrices for the open path, and computes rank by exact bitwise Gaussian elimination. It independently constructs the four-state matching automaton law and compares the entire unconditioned count table, not merely its balanced slice. It verifies the balanced endpoint counts for all tested even sizes and the full six-entry probability numerator histogram for \(n=12\). It also tests the exact transfer characteristic-polynomial formula on an integer interpolation grid. The determinant is a polynomial of degree at most four separately in its three indeterminates, so its equality at five distinct values of each is an exact certificate of that polynomial identity. Finally it evaluates the rational logarithmic Hessian from the characteristic cubic's implicit derivatives.

The central limit theorem and all-size endpoint formula are obtained by the analytic and combinatorial proof in `RESULT.md`. Checking fourteen sites is not an infinite proof and is not presented as one. No external or independent audit has been carried out.
