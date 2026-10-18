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

# Reproducibility and verified limits

The packages `verify_singletons.py` and `verify_independent.py` are standalone Python 3 programs using only the standard library. Run them independently from the same directory:

```
python3 verify_singletons.py
python3 verify_independent.py
```

The first verifier classifies every positive integer partition through census size 17, groups them by number of species, tests all ordered distinct strict-majorization comparable pairs, and evaluates every sample size exactly. Across census sizes 2 through 17 it tests 10,354 comparable pairs; the unique pair with at least two strict sign reversals is \((9,4,3,1)\succ(7,6,2,2)\), with three. The script independently counts singletons on all \(2^{17}\) labeled subsets of each witness community (262,144 total examined subsets). It also verifies local transfer polynomial identities, coefficient endpoints and exactly one sign change in 1,378 eligible test configurations (these tests supplement, not replace, the analytical unrestricted proof).

The second program reconstructs all partitions by enumerating all integer-composition breakpoints rather than using the first program's partition recurrence. It repeats all 10,354 comparable-pair calculations and finds precisely the same unique witness. Both verification programs were executed successfully before assembly of this report.

The all-size single-transfer statement is proved symbolically in `RESULT.md`, using the one-switch coefficient structure of \(Q(z)\) and an elementary adjacent-sums induction. The finite 17-individual minimum and uniqueness depend on complete exhaustiveness of the partition enumeration; they do not extend without a further theorem to larger censuses, different-richness profiles, or arbitrary continuous abundance distributions.
