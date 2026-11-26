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

RESULT.md lines 5–44 and 46–61: the finite relation language and ultrahomogeneity identify the realized positive distance vectors with complete types over the named points; finite many quantifier-free orbits also imply quantifier elimination and all such types are realized. Every admissible positive vector has arbitrarily many copies mutually at distance 1, by the triangle inequalities and finite extension, so these types are nonalgebraic. The pairwise triangle inequalities reduce to a width condition and a lower bound on the sum of the two smallest entries. A minimum m≥a=ceil(s/2) contributes U_m^n−(U_m−1)^n, while m<a must occur once and gives n B_m^(n−1) with other entries freely in [s−m,min(D,s+m)]. The formula gives D at n=1. The upper sum in fact equals h w^n−(h−1)(w−1)^n: the maximum width occurs h times and smaller widths decrease by one to 1. The maximum short base is strictly less than w for even s with a nonempty short range; for odd s=2k+1≥3 it is min(D−k,2k+1) versus w=min(D−k,2k+2), equal precisely at s≤D≤3k+1. This proves both growth regimes and concentration, including the endpoints, with empty short sums for s=1,2 and the exact constant case D=s=1. The packaged checker mentioned in the record is not present; its reported results are not independently credited. A fresh exhaustive triangle-inequality enumeration across the claimed 210 finite census cases passed; replay: python3 /workspace/branches/independent_discrete_checks.py. The limits were checked algebraically, not extrapolated.

## originality

PASS

Best of current knowledge for the full labelled all-(D,s) formula, inclusive odd-distance diameter boundary and concentration law, not for Katětov realizability or isolated diameter-three/four counts. Resultary and primary-source comparisons found real exact overlaps at restricted parameters but no theorem giving this general census or the competing-base transition.

## value

PASS

Equilateral labelled parameter sets are a natural highly symmetric slice of finite metric type counting. A single exact formula with an inclusive parity/diameter threshold shows that a polynomial prefactor in type growth is tied to a change in geometric behavior: almost every extension in one regime has exactly one short coordinate of the specified distance, while almost none in the other do. This resolves more than a small table or a direct realization criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
