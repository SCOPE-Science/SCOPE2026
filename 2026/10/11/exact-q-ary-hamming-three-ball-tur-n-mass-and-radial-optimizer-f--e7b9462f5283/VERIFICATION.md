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

The proof is based on a binomial interpolation identity, not on a numerical search. Run `python checker.py` with Python's standard library to reproduce the exact finite checks; no network, external datasets, or third-party packages are required. The checker validates 297 parameter pairs for 9 alphabet sizes and dimensions 3 through 35, all quadrature weights and moments of orders zero through three, and the Krawtchouk support boundary for selected smaller orders. The checker does not certify the universal quantifiers or originality; those are addressed by the mathematical argument and bibliographic comparison, respectively. All independent validation remains unperformed.
