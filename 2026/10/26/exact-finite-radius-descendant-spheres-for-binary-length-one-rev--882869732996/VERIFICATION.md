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

The frozen asymptotic proof (RESULT.md line 33) undercounts both leading powers by a factor of two; the displayed density itself is correct. The replacement proves the exact complementary tails: for m=n+t and t>=1 the two low sums are 2^(m-1) minus the upper-complement tail of degrees 0..n-2 and 2^(m-r-1) minus the tail of degrees 0..n-r-1. These polynomial tails give the stated limit, including n=r=1. Rechecked the complete argument: embed every position of the first run and right-justify matches in later runs; deleting the unmatched first letter of the rightmost unmatched run is legal, and a singleton second-run merger joins entirely matched positions forming an initial seed block. Greedy subsequence counting after a forced prefix gives both sums, with empty target allowed and t=0 handled separately; Pascal gives a strictly positive increment when r increases and t>=2. Independently checked the complementary-tail identity using exact integers at representative n,r and t up to 64. Inspected frozen VERIFICATION.md and verify.py; did not execute uploaded code.

## originality

PASS

PASS for the all-radius exact distinct count and initial-run reduction, not for determining the unbounded reachable language. The strongest inspected exact indexed overlaps are for t=2 and t=3 or just extrema, not all t. The proof's power-of-two correction does not change this comparison.

## value

PASS

The number of distinct outputs of a natural insertion channel at a fixed radius is intrinsically useful and differs from the number of histories. This exact answer for every seed and radius gives a non-obvious one-run invariant, sharp extremizers, and a limiting density without enumeration. Its contribution is not an already-indexed fixed radius or a claim about optimal codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
