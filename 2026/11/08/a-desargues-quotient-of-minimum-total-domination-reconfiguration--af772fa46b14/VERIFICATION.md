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

# Reproduction and boundaries

Run both embedded commands with Python 3 (standard library only):

```sh
python3 check_gp.py
python3 check_lcf.py
```

The exact expected output lines appear in `check_gp.out` and `check_lcf.out`. Both scripts executed successfully against the package's own bytes. `check_gp.py` enumerates each size \(0\) through \(8\) subset, checks all swaps, derives components, and verifies an explicit edge-image certificate to the Desargues graph. `check_lcf.py` uses a different LCF graph model, scans all \(2^{20}\) masks and checks candidates of size at most eight, reconstructs swaps by unordered pairs of configurations, and finds the quotient isomorphism by backtracking. Both check all 150 nontrivial-component eccentricities.

The result is finite and exact for the dodecahedral graph; the code does not assert a theorem for arbitrary generalized Petersen graphs. Existence of the 190 configurations is not in itself an originality assertion, because graph-data systems can return minimum total dominating sets. Historical priority is provisional and independent audit has not been performed.
