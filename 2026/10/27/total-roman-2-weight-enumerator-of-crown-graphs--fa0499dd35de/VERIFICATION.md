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

At the paired opposite vertex a singleton positive support supplies neither a positive neighbor nor any defensive weight. Thus both side supports have at least two positives, which also suffices for totality. Defense at a zero a_i uses exactly W_B-B_i. The only nonautomatic cases with this support size are two ones (force both paired opposite positions positive) and an ordered 2,1 pair (force only the position paired with the 2). Subtracting these cases and the support sizes 0,1 from the unrestricted product gives R; fixing one or two positive coordinates gives the stated F1 and F2 after the same exclusions. Combining side types gives R squared and the two mixed robust terms, with both orientations; two weight-2 sides must have identical support, a weight-2 and weight-3 side must also have identical support, and for two weight-3 sides the second ordered pair either has the same 2-index and arbitrary different 1-index or reverses the first pair. These give exactly the three low-regime coefficients. In degree 5 the extra robust mixed term is n(n-1)(n-2), adding to 2n(n-1); in degree 4 only matching two-one supports contribute. Substituting z=1 yields the stated total and dividing by 9^n gives the quoted asymptotic. Boundary n=3 is included. `python3 /workspace/reviews/replay_finite.py 4` independently exhausts labeled pairs via the original neighborhood tests for n=3–7 and agrees in every coefficient (totals 328, 4422, 48974, 488266, 4609770). The frozen verification code and recorded output were inspected, not executed.

## originality

PASS

Pass applies to the full enumerator and additional counts, not to the already stated minimum 4 or its full minimum-function classification and binomial multiplicity. The closest exact prior catalogue finding covers these minimum claims only. Other full-polynomial hits either count the same constraint on a different graph or impose a different zero constraint on the crown. No inspected finding or primary result covers the full target polynomial.

## value

PASS

The full weight law on a natural deleted-matching graph is informative beyond the already known minimum and its minimizers: it identifies how missing matched neighbors couple opposite label supports, gives exact next-weight multiplicities and quantifies the exponentially rare excluded assignments. It can serve as an exact comparison with the complete bipartite and neighboring-2 variants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
