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

# Reproducibility

From this directory, run `python3 verify_singleton_peaks.py --verify-certificate census.csv`. Python 3.9 or newer and its standard library suffice. The verifier was executed with this command; it returned PASS and reproduced the full 66-partition table and the exact witness. A second run in certificate-generation mode may be used to regenerate the table in another location before byte comparison.

The mathematical scope is the finite census through \(N=8\), with structural all-size contrasts for equal abundances and census abundances at most two. The program establishes finite combinatorial identities by exhaustive exact arithmetic; the all-size contrasts are proved symbolically in the accompanying result. A finite census does not prove anything about larger population sizes or stochastic sample paths. No separate external scientific audit has been performed.
