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

# Verification scope

The embedded `verify_path_maximal.py` uses only Python 3 standard-library integers and fractions. It constructs all legal radius tuples of centered balls and proves strict spectral separation by exact fraction-free Sylvester tests. It checks algebraic characteristic polynomials by integer determinant evaluations, rational Rayleigh witnesses and root brackets, and interval-certified strict radius choices. Its executable checks cover exactly \(18+1200+176400=177618\) selections on the specified three path orders.

Command: `python3 verify_path_maximal.py`.

Observed final line: `ALL_EXACT_CERTIFICATES_OK`.

The accompanying proof derives the nonlinear-to-spectral identity and all equality cases. No infinite-family assertion or independent audit is represented by these finite certificates.
