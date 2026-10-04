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
The proof is symbolic and applies to every finite field of characteristic different from \(2\) and \(3\).

The bundled `artifacts/verify.py` uses only the Python standard library. For the prime fields
\[
\mathbb F_p,\qquad p\in\{5,7,11,13,17,19,23,29,31,37,41\},
\]
it exhausts all ordered pairs and verifies that every nonzero-sum \((a+b,a^3+b^3)\) fiber is exactly one unordered pair, whereas the zero-sum fiber is precisely all \((a,-a)\). It then checks the proposed extremizer and sharp constant using exact rational arithmetic.

Expected output: `VERIFY_OK primes=11 max_prime=41`

These finite checks do not prove the extension to non-prime finite fields; that extension follows from the field-algebra proof in `RESULT.md`.
