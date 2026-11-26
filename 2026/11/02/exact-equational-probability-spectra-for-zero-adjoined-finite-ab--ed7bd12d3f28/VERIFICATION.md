---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For specified nonempty supports, the event both outputs are absorbing has mass 1−s^i−s^j+s^u. Otherwise equality requires every union variable to land in G; the uniform fibers of the linear difference map then give mass s^u/|dG|. Its image is dG by Bézout with the group exponent. Each support triple can be selected independently of the conditional probability: give every supported variable exponent m on each side where it occurs, and change one exponent by d on one side. To minimize, both lower bounds c≥1/q and s^u≥s^(i+j) must be equalities, and the resulting lower bound 1−s^i−s^j+s^(i+j−1) exceeds 1−s exactly when both supports exceed one. Thus the full equality criterion follows. For limits of distinct values, at least one support size diverges on a subsequence (there are only finitely many c), and the other can be fixed or made to diverge; these give the only possible limits. They are all realized by the disjoint-support families in RESULT.md lines 69–70; alternatively take i=j=u increasing with c=1/q to approach 1. The stated second and third derivatives follow since 1−s^h is strictly increasing to 1. For the Klein four separation an independent shorter exclusion suffices: writing the purported 3/5 probability as equation (*) in the record, its left side 2·5^(u−1) is 2 mod 4, but all terms on the right are divisible by 4 when u≥2 for c=1 or 1/4. The remaining u=1 probabilities are 1 and 2/5. Direct evaluation gives 3/5 for the C₄ witness. `cd /workspace && python checks/independent_replay.py 4` passed 2,700 exact short-word comparisons and minimum-equality tests, supplementing the two frozen bounded checkers and stored outputs; none is relied on for unbounded nonmembership or derived sets.

## originality

PASS

The conditional set of group probabilities was already known in exactly the multiplication-only language on G. The supported distinct result is the full zero-adjoined classification, not the conditional set; in particular it includes the sharp equation-level extremizers, full accumulation hierarchy and separation of two zero-adjoined monoids by an explicit value. The inspected literature does not establish coverage of this remainder; historical priority is bounded by the sources examined.

## value

PASS

The spectrum is a natural invariant of a closely studied multiplication-only language. Incorporating the absorber changes the admissible values substantially; the resulting exact formula, all equality cases and nontrivial topological hierarchy address an entire class and do not follow from enumerating small semigroups. The 3/5 witness is useful because it distinguishes the zero-adjoined structures where merely distinguishing the underlying groups would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
