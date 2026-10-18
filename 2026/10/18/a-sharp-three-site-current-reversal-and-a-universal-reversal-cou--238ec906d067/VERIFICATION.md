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

Execute `python VERIFY.py` in the extracted directory with the dependency specified in `requirements.txt`. The code constructs each finite generator directly from positive site weights and edge conductances, verifies individual landscape detailed balance, solves the normalized stationary equations, and checks edge fluxes. For the explicit three-site witness it verifies the exact rational-current identity and its unique positive zero and reversal. For other samples it independently computes the \(n-1\)-dimensional inverse-restriction expression and compares its current with the exact full \(2n\)-state stationary calculation.

The recorded package-path run passed 187 exact rational/symbolic assertions: the witness identity, positivity and sign samples, normalization and environment marginals, 108 detailed-balance identities, and 72 independent full-versus-reduced comparisons and normalization checks for 12 positive-landscape pairs on rings of sizes 3 through 6 at two rates. Assertions are exact identities at their stated arguments, not an exhaustive search over all landscapes or all rates. The general theorem is proved in `RESULT.md` using a full symbolic operator argument; the finite checks are corroborative.
