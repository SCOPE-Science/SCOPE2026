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

# Reproduction of the algebraic certificate

Run `python3 verify.py` with no arguments. It requires only the Python standard library. `verify_output.txt` contains the actual result of this command.

The checker reconstructs ladder graph adjacency and exhaustively compares graph-based membership against transfer-counted polynomials for \(1\le n\le9\). It compares minimum-set subsets with the two (odd-order) or four (even-order) configurations, verifies the first five coefficients of the rational numerator, and checks the recurrence at order six. The decisive universal certificate consists of the sixteen exact formal polynomial identities \(u^{\mathsf T}T^jR(T;z)v=0\) for \(0\le j\le15\), encoded as residual polynomials at orders seven through twenty-two. Because the transfer matrix has exactly sixteen states, Cayley--Hamilton proves all later residuals vanish. All arithmetic uses integer coefficients and exact dictionary operations.

The direct enumeration is finite corroboration, not an exhaustive check of infinitely many graphs. The algebraic certificate, combined with the written transfer-model proof and Cayley--Hamilton, supplies the all-order inference. These checks are not independent mathematical validation.
