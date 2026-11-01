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

`verify.py` uses exact finite-field arithmetic, builds the complete structure matrix, independently checks its invertibility and the proposed rotation automorphism, exhaustively enumerates all monomial automorphisms in the indicated small cases, and checks the invariant-factor prediction by the complete element-order distribution. For these smaller cases it separately counts graph automorphisms of the support digraph. The recorded `verify_output.txt` has thirteen `CASE_OK` lines and ends with `VERIFY_OK`.

The exhaustive range is explicit in `verify.py`; three larger parameter cases check the claimed constructed rotations and full-rank conditions but not all automorphisms. The universal theorem, the graph-automorphism exhaustion, the universal simplicity statement, and splitting for every field are proven symbolically in `RESULT.md`, not by the finite checker. No independent external mathematical audit was conducted.

`verify_char2.py` independently implements arithmetic in the quadratic extension \(\mathbb F_4\), exhaustively checks all coefficient assignments and their orders for \(m=3,h=2,r=1\), and returns `VERIFY_OK` with automorphism group \(C_9\). Its output is `verify_char2_output.txt`.
