---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS. The channel duplicates a consecutive pair ab as ab complement(b) complement(a), with no symbol fixed by the complement involution. Equating outputs at two starts reduces by cancellation to xz=zy; the length-one overlap and longer period-two word equations force the intervening original factor to alternate in complementary pairs, and conversely give equality. Consequently equivalence classes of start positions are maximal alternating runs, so B(w)=n-1-C(w), with C the count of length-three complementary alternating factors. The two suffix states (complementary pair or not) carry transitions [[q-1,1],[q-1,z]], yielding the asserted rational generating function with initial vector q(q-1),q. Indicator expectations 1/q² and adjacent joint 1/q³, while distance-two indicators are independent, give the stated variance. The n=2 boundary and all even q are handled; independent direct daughter-set and histogram enumeration confirmed small q,n without extrapolation.

## originality

PASS

PASS, LIMITED TO THE COMPLETE ALL-q FORWARD ONE-ERROR SIZE DISTRIBUTION AND MOMENTS, NOT THE INDIVIDUAL-SPHERE COLLISION LAW. Critical newly inspected source: Lenz–Wachter-Zeh–Yaakobi (2018 Lemma 3 / 2019 Lemma 12) already proves the exact per-word PAL2 one-error sphere and same-run collisions; Zabokritskiy (2026) proves the even-length PAL/RC conjugacy, so the RC2 per-word collision and size law are already implied by prior work and have no independent priority. Their inspected full texts did not report the submitted all-q bivariate degree enumerator, moment formulas and exact histogram. This surviving natural quantitative distribution requires additional all-words enumeration, even though it follows by applying a two-state transfer count to the known local law. Thus the main complete spectrum is assessed as an original quantitative refinement; the original source's relationship-to-prior-work section materially undercredits this coverage and must be corrected BEFORE any public use. If the original item were claimed only as a sphere law it would be rejected as covered.

## value

PASS

PASS for the complete q-ary one-step channel degree distribution, a natural spectrum of forward branching multiplicities and a quantitative input to finite-error sphere/packing analysis. An exact rational two-parameter enumerator, mean, variance and extremal multiplicities add information beyond the individual per-source size criterion. The credited collision identity alone is not novel or sufficient to establish value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
