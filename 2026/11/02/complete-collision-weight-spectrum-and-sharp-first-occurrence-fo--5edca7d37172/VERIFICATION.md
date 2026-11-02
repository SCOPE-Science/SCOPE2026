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

# Verification record

The analytical proof is in `RESULT.md`; the runnable exact checker is `verify.py`. It uses only the Python 3 standard library and recreates all matrices and graphs from the stated Rule 30 local update. Invoke `python3 verify.py` in the extracted package directory. Successful completion prints `VERIFY_OK`.

The program checks the full characteristic polynomials of the four-state and sixteen-state weighted transfer matrices at each of seventeen distinct integer values of the output-weight variable. Every coefficient's weight-variable degree is at most sixteen, so this finite exact-arithmetic check certifies the factorized identities over the integer polynomial ring. This is a polynomial-identity certificate, not a numerical approximation. The program also enumerates every simple cycle of the twelve-vertex off-diagonal graph and verifies its ten-cycle weighted census; that finite census plus decomposition of arbitrary closed walks and shared-vertex constructive cycles proves the support and first-circumference results for unbounded ring size.

As an additional independent check, all binary inputs at ring lengths one through fourteen are propagated directly by the local update. Their equal-output ordered-pair collision counts are grouped by output Hamming weight and compared with the derived formal-series coefficients. A separate graph walk dynamic program validates first circumferences through weight forty-five. These bounded enumerations are corroboration and do not replace the graph/proof argument.

Limitations: no multistep dynamics or cryptographic-security claim, and no independent scientific audit. Historical source comparisons were partial for some long-form older works, which remains a priority risk.
