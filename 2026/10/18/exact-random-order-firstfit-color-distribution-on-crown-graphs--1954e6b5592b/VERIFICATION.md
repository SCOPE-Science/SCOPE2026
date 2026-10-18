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

The exact calculation derives the law from three exhaustive and mutually exclusive arrival events, not from numerical fitting. Every remaining vertex excludes the paired first color, and the \(0\)- or \(1\)-intervening-vertex cases reduce to a uniformly ordered smaller crown graph after a color shift. A separate finite verifier checks the recurrence against complete permutation counting by memoized dynamic programming for \(n=2,\ldots,7\), plus literal permutations for \(n=2,3,4\).

Run `python3 verification/verify.py`. The accompanying `verification/expected_output.txt` contains the exact output of the packaged program. The checker uses integer factorial counts and Python rational numbers. The output at \(n=7\) represents an exhaustive state-summed count of all \(14!\) permutations, not an explicit loop over all \(14!\) permutations. Finite checks are corroborative; the mathematical induction in `RESULT.md` proves the full infinite family.

External independent audit has not been performed. The only published-source originality uncertainty is equivalent unindexed work; the specific motivating primary full text was checked in HTML. No assertion about non-crown graphs is made.
