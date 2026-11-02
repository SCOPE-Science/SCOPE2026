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

# Exact verification

The proof in `RESULT.md` is an all-parameter argument. The separately executable `verify.py` uses the Python standard library and is an independent finite check, not a replacement for any infinite step.

Run `python3 verify.py` in the directory containing that file. It reconstructs the graph and an exact integer directed Laplacian, evaluates rooted cofactors by a fraction-free elimination algorithm for every alphabet size from \(2\) to \(8\), constructs and checks all prescribed length-three windows of one valid universal cycle for each alphabet size from \(2\) to \(25\), and exhaustively enumerates Euler tours with the fixed initial edge `001` for alphabet sizes \(2\), \(3\), and \(4\). The resulting exact counts are \(2\), \(36\), and \(55296\), all agreeing with the closed formula. The verifier also checks the occurrence count of every letter.

The exact determinant reduction, the bijection to Euler tours modulo rotation, and the BEST theorem normalization are justified in `RESULT.md`; only finitely many parameter cases are executed by code. No finite test certifies originality, and independent external review has not occurred.
