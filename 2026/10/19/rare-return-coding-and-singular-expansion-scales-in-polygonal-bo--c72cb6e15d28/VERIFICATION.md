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

The analytic proof of the directed four-excursion graph and the source's parameter equation establishes the statement for every sufficiently large admissible index. The `verify.py` checker builds the graph directly for dimensions \(n+4\), confirms the characteristic polynomial \(t^2(t^{n+2}-2t-2)\) and symbolic zeta denominator \(1-2z^{n+1}-2z^{n+2}\) using exact arithmetic for several finite indices, and evaluates high-precision asymptotic normalizations at large indices. Running `python verify.py` returned `VERIFY_OK` with the supplied dependencies `sympy` and `mpmath`.

The numerical scaling checks do not establish an asymptotic theorem. The proof uses a Taylor expansion of the exact scalar parameter equation and of the Perron equation. The source guarantees the polygonal Markov partition for sufficiently large indices; the code does not certify any smaller-index geometric parameter range. Physical periodic points may have nonunique boundary codes, so only symbolic objects are asserted.
