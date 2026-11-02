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

# Verification

`CHECKER.py` uses only Python's standard library. Run `python CHECKER.py`; the expected final line is:

`PEIRCE_POTTS_COMMUTING_IDEMPOTENTS_OK 31`

The program enumerates all elements of the selected truncated path algebras, computes their products from actual path concatenation, filters all idempotents, and tests commutativity for ordered pairs and triples. The independent prediction evaluates both label-coloring sums and the Fortuin–Kasteleyn spanning-subgraph expansion; equality of these two predictions is separately asserted. There are 31 exhaustive small cases over \(\mathbb F_2\), \(\mathbb F_3\), and the genuine extension \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), including parallel arrows, opposite arrows, a loop, a directed cycle truncated before length three, and triangular algebras with nonzero radical square and cube. The exact run output is embedded in `VERIFY_OUTPUT.txt`.

The general algebraic proof is independent of the program. Step 3 of `RESULT.md` is the critical nonstandard scheme-level inverse: the unit \(w=1+h+n\) uniquely factors as \((1+n(1+h)^{-1})(1+h)\), polynomially over arbitrary base rings. This proves the fiber is an actual affine scheme, not just a rational-point bijection. Direct finite enumeration cannot verify the theorem for all algebras, fields or arities.
