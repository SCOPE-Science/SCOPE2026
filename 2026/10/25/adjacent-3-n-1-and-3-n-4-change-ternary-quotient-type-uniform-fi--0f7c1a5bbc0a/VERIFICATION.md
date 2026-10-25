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

Execute `python3 verify.py` using Python 3 standard library. The self-contained program reconstructs support sets, verifies their cardinalities and exponents, multiplies the defining polynomials as coefficient dictionaries, and checks the integer identity for every \(5\le n\le204\). It also checks the evaluation-at-one obstruction to polynomial divisibility. Expected final message: `VERIFIED: 200 exact support, carry, integer-identity, and localness checks`.

The complete proof is the symbolic coefficient identity valid for every \(n\ge5\), the evaluation at \(3\), and the nonintegrality of \(P_n(1)/Q_n(1)=9/5\). All numerical tests are finite diagnostics only; they do not certify exhaustive behavior at unbounded exponents. No external mathematical audit has been conducted.
