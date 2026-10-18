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

# Reproducibility and mathematical checks

Execute `python verify_paperfolding_binomial.py` in a directory containing the accompanying file. No network connection, optional dependency, or other artifact is required. A successful replay prints `VERIFY_OK` after checking exact base profiles, exact parity-profile recursion through exponent 12, two independent paperfolding bit generators over more than 65,000 entries, full factor-profile agreement against direct sliding-window scans through exponent 10, and binary scattered-subsequence coefficient identities on short factors.

The bit-prefix scans serve as an independent finite witness comparison; they do not prove that a finite prefix contains every factor. The equality of the parity-profile recursion with all factors of the infinite word follows separately from the index identities \(2i\) and \(2i+1\), which exhaust the nonnegative integers. The proof's parity-disjointness induction, not the replay's sample depth, yields the infinite formula.

The theorem was checked internally for its stated scope. Independent scientific auditing remains not performed.
