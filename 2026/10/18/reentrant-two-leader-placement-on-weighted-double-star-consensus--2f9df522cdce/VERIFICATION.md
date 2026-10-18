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

# Reproduction and limits

Run `python verification/verify.py` with Python 3.10+ and SymPy from the package root. The program constructs the five exact leader-position objective functions, checks four crucial symbolic difference identities and the switching-root equation, proves the chosen six-vertex test signs by exact rational arithmetic, and for each of \(m=2,3,4,5\) builds the full weighted graph Laplacian at four sets of positive rational resistance/feedback parameters. It exhausts every unordered pair of distinct leaders, compares the exact inverse-trace against the formula for its orbit, and checks the minimum independently. It additionally checks positivity of the three comparison numerators at exact test values. Recorded outcome: PASS, 681 assertions.

The exhaustive finite checks do not prove any statement for infinitely many sizes or all real parameters. Those claims rely on the positive-factor comparisons, quadratic-root analysis, and series/parallel derivation in `RESULT.md`. No external or independent audit has been conducted. Library and unindexed-literature coverage is not certified complete.
