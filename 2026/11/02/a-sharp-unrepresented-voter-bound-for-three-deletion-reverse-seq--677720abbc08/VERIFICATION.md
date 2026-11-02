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

# Reproducibility and limits

Run `python verify.py` in the same extracted directory as `RESULT.md`, using a standard Python 3 runtime; no external packages are needed. The verifier uses exact rational arithmetic and independently recomputes individual ballot gaps, complete symmetric extremal-profile marginal losses, and the strict 252-voter example.

The finite verification output is:

```text
VERIFY_OK exact_dual_ballot_cases= 79632 sharp_family_population_cases= 59 strict_252_voter_deletion_scores= [(0, Fraction(62, 3), Fraction(127, 6)), (1, Fraction(31, 1), Fraction(63, 2)), (2, Fraction(33, 1), Fraction(100, 3))]
```

The pointwise residual formulas in `RESULT.md` can additionally be checked by symbolic substitution and rational simplification for each of eight candidate-approval masks, separately for zero and positive winner-approval counts; all sixteen identities were so checked. The resulting closed rational identities, together with the stated nonnegative coefficients and aggregate deletion inequalities, constitute the proof for unbounded integer seat counts. Testing finite ranges is neither an exhaustive proof of an infinite claim nor independent scientific certification.

The original full scientific source was inspected for its definitions, the two-deletion and three-deletion results, and its approximate-EJR theorem. Literature-search nonappearance is not proof of originality in all possible sources.
