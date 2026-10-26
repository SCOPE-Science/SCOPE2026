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

The package contains `verification/crown_power_domination_check.py`, an executable Python 3 source file requiring no external dependencies. From the extracted package root, run `python3 verification/crown_power_domination_check.py`.

The verifier constructs adjacency bitmasks for each crown graph, starts from the closed neighborhood of a candidate vertex subset and iterates the unique-unobserved-neighbor rule. It exhaustively tests every subset of every graph with \(4\le n\le8\), compares eligibility with the proposed characterization and compares both the complete bivariate count table and the inclusion-minimal count table with the formulas. Inclusion-minimality is determined from previously computed results for all proper one-element deletions, not assumed from the proposed structural theorem.

Observed output:

```
PASS n=4 subsets=256 all=247 minimal=28
PASS n=5 subsets=1024 all=993 minimal=45
PASS n=6 subsets=4096 all=4013 minimal=66
PASS n=7 subsets=16384 all=16187 minimal=91
PASS n=8 subsets=65536 all=65099 minimal=120
ALL_CHECKS_PASSED
```

The five orders comprise exactly \(87,296\) distinct initial subsets. The verifier also checks the exact total \(4^n-2^{n+1}+n^2+n+3\) separately for each order. Finite exhaustive experiments do not prove the infinite-family claim; its proof is the four-step argument in `RESULT.md`. The claimed originality is subject to the literature access risks stated there. Independent audit has not been performed.
