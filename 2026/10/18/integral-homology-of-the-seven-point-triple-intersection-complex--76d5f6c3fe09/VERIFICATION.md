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

# Computational verification

Compile/run the independently supplied C++17 and Python 3 sources with `python3 verify.py` while all four reproducibility files reside in the same directory. The program enumerates each of the \(1,278,686\) augmented simplices once by an increasing-index recursion on thirty-five vertices; it builds complete face-to-index tables and deterministically matches each face at most once.

For each of the two vertex-toggle orders it exhaustively checks every matched lower face and every possible alternate matched lower facet of the corresponding upper face, and verifies that all matching-gradient nodes admit a topological order. It then recursively constructs the signed critical-to-critical Morse differential matrices. Their exact integer entries must byte-for-byte equal `matrices_forward.txt` and `matrices_reverse.txt`.

The exact standalone integer verifier checks the boundary compositions vanish, performs only unimodular integer row and column operations with unit pivots, and rejects a nonzero residual block. This independently verifies the nonzero Smith invariant factors are all units. No floating-point arithmetic or probabilistic prime sampling is used for the integral conclusion.

Expected final stdout marker: `INTEGRAL_HOMOLOGY_VERIFIED`.

Forward certificate: \(639,293\) pairs, \(501,581\) gradient arrows, Morse differential ranks \((16,11,5)\) on chain ranks \((45,27,16,12)\); reverse certificate: \(639,283\) pairs, \(540,642\) arrows, ranks \((31,10,1)\) on chain ranks \((60,41,11,8)\). Both yield integral reduced homology \(\mathbb Z^{29}\) in degree six, \(\mathbb Z^7\) in degree nine, and zero elsewhere.

The computed matrices are necessary mathematical evidence; a program exit message alone is not a proof. Their combination with exhaustive enumeration, acyclicity, and unimodular reductions certifies this finite example but not other Kneser parameters and not a homotopy wedge decomposition. Independent audit: not performed.
