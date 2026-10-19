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

Execute `python3 verify.py`. The self-contained program uses no nonstandard Python modules or external network resources. It builds finite abelian groups as products of cyclic groups, computes doubling cycles directly, and compares them with the prime-local classification for all 150 odd-order abelian groups of order at most 240 (193 pairs of equal order). It uses finite-field pointwise spectral identities to check the Fourier product formula for seven cyclic moduli; counts monomial automorphisms over splitting fields for two cycle types; and checks primality, order, valuation and cyclic-permutation counts for the 1093 witness. A successful execution ends with `VERIFY_OK` and the counts.

All integer and field calculations are exact. The general theorems are proved in RESULT.md and do not rest on experimentally checked bounds. This code is a reproducibility aid, not an independent mathematical audit or a claim about unsearched papers.
