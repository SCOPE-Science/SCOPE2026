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

The proof in RESULT.md is a whole-parameter polynomial identity, not an inference from sampled parameters. The accompanying `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` in the same folder as the files. It separately enumerates all \(2^7=128\) binary assignments to four headwater signals and three local storm signals; each assignment contributes an exact bivariate polynomial weight. It then matches the outlet and internal-count differences against the stated factorized polynomials coefficient by coefficient, and performs 68 rational-value and probability-bound assertions. Expected output:

```text
PASS: 128/128 configurations, two exact bivariate polynomial identities, 68 rational checks
```

The interval signs and the claim that four leaves are minimal follow analytically from positivity and full-binary-tree shape classification, respectively. Checks on this discrete idealization do not test conservation of water, temporal routing, field data, or the novelty of all possible earlier results. Independent verification has not been performed.
