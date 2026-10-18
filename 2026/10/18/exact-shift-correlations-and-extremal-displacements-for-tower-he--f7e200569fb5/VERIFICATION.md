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

Run `python3 verify.py` from this directory. No third-party packages or remote services are required.

The code computes tower heights directly from prime factorizations for the finite tested range, checks three minimum forbidden-exponent benchmarks, enumerates \(24\) prime-power residue models and compares their exact rational forbidden-overlap frequencies with the case-split formula, and compares \(14\) empirical shift densities to finite Euler products (with loose margins acknowledging cutoff and sampling error). It prints `VERIFY_OK` after all tests.

The prime-product theorem for all \(k\ge2\) and arbitrary nonzero \(t\) is established by the CRT and prime-power tail proof in RESULT.md, not by these finite tests. Neither maximal-shift attainment nor exact global novelty can be inferred from the numerical checks. There is no independent mathematical audit.
