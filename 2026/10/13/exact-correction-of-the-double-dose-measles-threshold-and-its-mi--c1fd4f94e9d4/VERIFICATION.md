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

Exact algebra from the printed ODEs gives \(N^*=\Lambda/\mu\), \(S^*=\Lambda k_3/D\), and \(\mathcal R_{\mathrm{tot}}=\beta\phi\mu k_3/(k_1k_2D)\). The 2026 displayed quantity equals the 2024 displayed quantity divided by \(k_3\), so it has time units and rescales inversely when all rate numerals are rescaled by a time-unit factor. The 2024 expression equals the next-generation result with \(R^*\) omitted from the incidence normalizer; the resulting gap to \(\mathcal R_{\mathrm{tot}}\) is the positive formula in the finding.

The bundled `verify.py` checks these identities, the time-rescaling law, and the exact witness \(93/100<1<31/30\). The checker verifies finite symbolic algebra only; local stability also uses the displayed Jacobian block argument. No independent audit has been performed.
