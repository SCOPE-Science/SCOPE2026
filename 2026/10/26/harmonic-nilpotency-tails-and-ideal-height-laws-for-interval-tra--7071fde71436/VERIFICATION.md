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
# Reproduction and checks
Run `python3 verify.py` with only the Python standard library. The script reconstructs the integer monoid's triples and product (not an asserted index histogram), computes successive powers, compares each observed least-zero-power count against the finite formula for every \(1\le N\le18\), and verifies rational antiderivatives on both sides of the ideal-volume transition across multiple rational height cuts and integer exponents. The observed result from the packaged program was `VERIFY_OK: 13367 exact structural, finite enumeration, and rational-integration checks`.

## What is and is not verified
The direct product checks are exhaustive only for the finite parameter range stated, not for all integers. Rational antiderivative checks are exact at tested points but do not alone establish the polynomial identity over every real parameter. The mathematical proof in RESULT.md establishes the required infinite and continuous statements using elementary summation and integration. No external or independent audit was performed.
