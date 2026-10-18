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
# Reproduction

Run `python3 check_density.py` in a directory containing that standalone file. It uses only Python's standard library (`fractions` and `collections`) and no network access. The program recalculates nine named exact densities, 405 exhaustive finite-ring counts, and nesting inequalities for all \(n\in[-40,40]\) and moduli \(3^k\) with \(1\le k\le5\). The original passing terminal output is in `certificate.txt`.

The finite experiment only checks congruence approximations. Its tolerance and finite range do not establish the infinite identities, which instead follow from the explicit Haar partition, Hensel lifting, equal-valuation analysis, and the two exact recurrences in `RESULT.md`. The probability is for *admitting* a square root, not a root-count weighted density.
