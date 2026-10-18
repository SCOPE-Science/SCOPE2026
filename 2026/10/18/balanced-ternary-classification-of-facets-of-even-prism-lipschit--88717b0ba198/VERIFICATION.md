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
# Reproducibility and proof limits

Run `python3 verify.py` with Python 3 and only the standard library. Expected output begins `PASS: 25 independent exact theorem-level consistency checks` and prints six even-prism counts.

The program independently counts signed integer \(2\)-flows in each bipyramid at orders \(n=4,6,8,10\), counts integral potential vertices by full bounded-walk enumeration plus connected tight-edge graphs on primal prisms for \(n=4,6\), and computes the Laurent-transfer constant coefficient for \(2\le n\le20\). It checks equality with twice the central trinomial coefficient. Signed flow and primal tight-potential enumerations use different representations. No floating-point arithmetic is required by the certificate.

The enumeration is deliberately finite and does not prove the statement for all even orders. The full proof is the stated bijective conservation argument plus classical planar facet/flow duality and the Gaussian asymptotic estimate. There has been no independent scientific audit.
