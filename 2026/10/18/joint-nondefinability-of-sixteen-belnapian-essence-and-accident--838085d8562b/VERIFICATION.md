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

# Reproducible checks and mathematical limits

Execute `python3 verify.py` from the directory containing that script. This requires only the Python standard library. It checks exactly the modal truth/falsity clauses reproduced from Petrukhin's Definition 2.6 on crisp inputs; no downloaded paper or other data file is required.

Observed output begins:

```
VERIFY_OK
eight_modal_collapse_checks 2064
two_world_target_separations 16
sampled_reduct_term_comparisons 12000
```

The checker enumerates all \(2^n\) crisp valuations for \(1\le n\le5\) and tests each of eight source modalities at every world. For each of the 16 targets, it checks the full truth/falsity value at the common root of one- and two-world S5 models. It then tests 12,000 sampled nested source formulas using both negations, implication, conjunction/disjunction, all eight b/n operators and arbitrary crisp assignments on one, two and three worlds.

These calculations are tests, not a proof of unrestricted formula nondefinability. The analytic proof in `RESULT.md` uses a structural induction for arbitrarily nested formulas and a pair of symbolic model evaluations for each target. No machine proof or independent mathematical validation is claimed.
