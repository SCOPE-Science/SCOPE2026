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

# Verification and reproducibility

The accompanying `verify.py` is a standalone Python 3 script requiring only the standard library. Run it with `python3 verify.py` from the directory containing the file.

Observed output on the supplied script:

```text
VERIFY_OK exact_prefix_subsets=255 viable_subsets=30 rectangle_parameter_cases=475 literal_template_words=1260 literal_clique_cases=24 n_range=6..30
```

The script verifies the exact four nested compatible suffix neighborhoods, exhaustively enumerates all 255 nonempty prefix subsets, checks that every feasible prefix/suffix pair collection is contained in an allowed boundary template (including complemented templates), and independently compares exact binomial counts over 475 parameter pairs. It also constructs literal words, checks every pair and self-overlap in sample template families, and compares the theorem to a literal-word maximum-clique exhaustive search in 24 short cases.

**Proof basis.** The all-length claim is proved using the four neighborhoods and their nesting, not from the finite check. The limiting weight-density phase boundaries follow from elementary binomial ratios and exact comparisons of four explicit continuous functions.

**Limitations.** Finite executions cover only their stated ranges. The verifier does not establish novelty, and independent external scientific audit has not been performed.
