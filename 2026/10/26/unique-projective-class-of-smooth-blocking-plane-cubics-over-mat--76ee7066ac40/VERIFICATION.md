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

All 3^10−1=59048 nonzero ternary cubic coefficient vectors were treated via exact projective incidence on 13 points and 13 lines; 9880 blocking forms. Independent code divided 4940 projective blocking equations into ten exact PGL3(F3) orbits via elementary generators; one orbit of size 936 alone was geometrically smooth, established using affine-patch Groebner unit-ideal tests on one representative of every projective orbit. This gives 1872 smooth blocking forms, one orbit, stabilizer 5616/936=6 and six rational points. Pair/line incidences give t1,t2,t3=(6,3,4). Unlike finite samples, the coefficient/orbit enumeration is exhaustive and geometric smoothness is checked algebraically, avoiding unsupported extension cutoffs. Proof limited to embedded plane cubics over F3.

## originality

PASS

Asgarli, Ghioca and Yip already establish existence of the characteristic-three blocking cubic and give the same explicit equation in Example 3.5; neither the existence nor representative alone is original. The distinct surviving theorem is exhaustive classification of *every* smooth blocking ternary cubic into one PGL3(F3) orbit, plus orbit and incidence census. Published blocking-point-set catalogues do not automatically classify cubic equations or their projective stabilizers; small-elliptic finite geometry tables may encode the orbit and remain a risk.

## value

PASS

A sharp and motivated exceptional case is completely closed: known existence and q>=5 nonexistence do not determine projective uniqueness, number of equations or stabilizer. The exhaustive orbit classification and line-incidence refinement provide reusable exact finite-geometric data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
