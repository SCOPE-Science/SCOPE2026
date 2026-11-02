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

The symbolic proof in `RESULT.md` is the basis for the infinite-domain assertion; finite experiments are supplementary. Execute `python3 checker.py` with Python 3.9 or later. The code independently enumerates set partitions of ordered finite proxies with two representatives from every gap, checks invariance under independent swaps, and obtains the counts `2, 10, 114, 2066` for support sizes zero through three. The code additionally verifies essentiality by independently attempting to forget each named point; the resulting proxy essential-support counts are `2, 8, 96, 1752`. It separately evaluates the Bell convolution and least-support inclusion–exclusion formulas and verifies numerical union-bound consistency. The recorded execution completed with `ALL_CHECKS_OK`.

These tests do not exhaust equivalence relations on the infinite ordered rationals. The gap dichotomy is proved by independent transitivity of rational-order automorphisms, while the essential-support count invokes the least-support property of the total-order symmetry (a cited existing result). The asymptotic estimate invokes known Bell-number ratio asymptotics. Historical priority and independent external mathematical verification remain unperformed.
