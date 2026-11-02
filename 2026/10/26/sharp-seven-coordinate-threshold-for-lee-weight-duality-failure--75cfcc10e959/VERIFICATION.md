---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The Lee weight on F5 respects column sign reversal. Each generator column of F5^2 therefore has exactly 13 sign-orbit types including zero, so the exact number of spanning rank-two normalized multisets at length n is binomial(n+12,12)-6*binomial(n+2,2)+5. Its n=2..6 values are 60,400,1735,6067,18401. An independently written full C++17 census enumerated every such multiset, evaluated each of 25 primal combinations and the full dual Lee enumerator using the exact character factors F0=1+2z+2z², F1=1+αz+(-1-α)z², F2=1+(-1-α)z+αz², α²=1-α. Each primal spectrum uniquely determined its dual for n<=6, across 1,5,18,49,129 primal spectrum signatures respectively, with all irrational components canceled and integer divisibility checked. A separate direct 5^7-vector dual enumeration (not using Fourier) confirmed equal primal Lee spectra for the two 7-column generators and distinct dual Lee-weight-4 counts 56 and 60. This is an exact finite exhaustive proof within fixed dimension two; it does not extrapolate to other dimensions.

## originality

PASS

PASS, qualified: broad Lee-weight MacWilliams nonduality and rank-two constructions are old, but the first exact two-dimensional quinary failure length 7 requires complete shorter-length exclusion not supplied by Wood (2026) in the inspected full text. Abdelghany–Wood (2020), a particularly plausible older source, was available only at abstract level; institutional full-text access was blocked, and this is a real residual historical-priority risk.

## value

PASS

The first block length at which Lee weight fails to determine its dual for fixed information dimension is a natural sharp invariant of weight enumerator duality. The complete exact exclusion n<=6 and explicit witness n=7 resolve a genuine finite rigidity boundary beyond general MacWilliams failure existence; it is not a tiny arbitrary slice, because n=7 is the minimum length and two is the first nontrivial linear rank for the studied construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
