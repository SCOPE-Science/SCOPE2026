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

# Verification and limits

The attached `verify.py` uses Python's standard library only. Run `python3 verify.py` from the directory containing this file; the expected final line starts with `VERIFY_OK`.

It independently counts ordered, properly coloured nontrivial factorization words with all \(m\) colours present, compares them to the Stirling-weighted proper-factorization formula for \(2\le m\le4\) and \(n\le112\), and compares truncated Dirichlet convolution coefficients under valuation restrictions at \(2\) and \(3\). All polynomial/Dirichlet-coefficient operations use integer arithmetic.

For unbounded \(n\), correctness rests on the exact rational generating-function identity, the explicit leading Laurent coefficient, the strict nonperiodicity argument on \(\Re s=\rho\), and the cited Delange Tauberian theorem. The verifier is deliberately finite, proves no asymptotic by enumeration, and supplies no claim of independent audit.
