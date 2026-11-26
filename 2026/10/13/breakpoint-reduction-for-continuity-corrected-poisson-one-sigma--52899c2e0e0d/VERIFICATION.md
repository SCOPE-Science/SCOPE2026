---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a fixed nonempty integer interval [l,u], J'=p_{l-1}-p_u; if l=0 this is negative, otherwise the ratio of the two terms is a positive multiple of lambda^{-(u-l+1)}. There can only be a strict interior maximum. At a finite breakpoint the interval at the point is exactly the intersection of the two adjacent effective intervals: floor selects the higher lower bound and ceiling selects the lower upper bound; clipping the lower endpoint at zero preserves this statement. Thus the value at a breakpoint is no larger than either one-sided branch limit, a detail implicit in the frozen reduction. The raw lower endpoint has no negative integer crossing since lambda-sqrt(lambda)>=-1/4; A_0 changes the raw but not the clipped lower endpoint, and it coincides with B_2. At zero the limit is 1; at infinity the two standardized endpoints converge to -1 and 1 with rounding errors of at most 1/sqrt(lambda), so the CLT gives the stated limit. At s^2 for s>=2 the left and right branches have the additional atoms s^2-s-1 and s^2+s+1, respectively, both with positive mass, proving strict local minimality. Independent replay: python3 /workspace/review_replay.py 2, 45-digit checks of rounded cells through parameter 50 and the exact side-interval indices at squares 4 through 10000. These diagnostics are not the proof. The frozen checker was inspected, not executed; the scientific claim does not rely on it. No proof of the exact-normal lower bound for finite parameters is claimed.

## originality

PASS

The exact event is already stated in Sun–Hu–Sun, and interval-probability endpoint methods are prior tools. The supported distinct result is the outward-rounded localization with the correct side-value comparison and simultaneous-breakpoint minima, not the definition, the differentiation identity, the CLT, or a solution of the remaining finite-parameter normal comparison.

## value

PASS

The motivation is a published corrected Poisson comparison against the normal law. Reducing the continuous problem to two explicit candidate sequences and showing an infinite family of strict local minima gives concrete structure useful to anyone attempting the sharp bound, including why global smoothness/monotonicity is unavailable. It also distinguishes the exact benchmark from a rounded decimal; the elementary derivative or CLT alone would not justify credit. The difficult sign comparison at finite breakpoints remains open in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
