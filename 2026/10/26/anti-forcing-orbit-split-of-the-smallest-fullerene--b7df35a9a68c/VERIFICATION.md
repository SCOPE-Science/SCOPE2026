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

Execute both scripts in this directory:

```sh
python3 verify_gp.py
python3 verify_lcf.py
```

No third-party Python packages are required. The supplied `verify_gp.out` and `verify_lcf.out` record the actual outputs. Both runs completed and printed `all_verified: true`. The first program globally enumerates all \(\binom{30}{k}\) edge deletions for \(0\le k\le5\), rather than sampling; the second uses an LCF graph with an explicit tested isomorphism and enumerates candidate nonmatching-edge deletion sets separately for each matching. Key checks are 36 perfect matchings, complementary two-factor histograms \((20):30\) and \((5,5,10):6\), minimum anti-forcing numbers four and five, and eight or 22 minimum witnesses per matching, respectively.

The computation is finite. No claim is made about all fullerenes, graph families of growing order, or independent external certification. Source priority is limited by accessible literature.
