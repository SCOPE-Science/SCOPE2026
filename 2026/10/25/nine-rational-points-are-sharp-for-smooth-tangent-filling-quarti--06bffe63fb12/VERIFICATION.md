---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The set of distinct rational tangent lines must cover PG(2,5), equivalently a dual blocking set. A COMPLETE independently rerun g++ integer enumeration of all binom(31,8)=7,888,725 eight-line subsets found 9,300 covering sets, all containing a full 6-line pencil. The classical nontrivial blocking-set lower bound of 9 applies to fewer-line covers; no 8-line non-pencil cover exists. Any putative smooth quartic with <=8 rational points has six pencil tangencies. Normalize their center to [0:0:1]; all 34,375 patterns (5^6+6*5^5) of chosen contact points lead to explicit 12×15 linear F5 quartic coefficient systems. Read and reran complete verify_pencil_lower.cpp: ranks {9:25,11:750,12:33600}, 912,000 rationally nonsingular solutions encountered, minimum rational point count 9. Rational nonsingularity is a weaker filter than geometric smoothness, so this excludes all smooth counterexamples without assuming exhaustive geometric-point tests. Separately used exact finite-field rational tangent checks and SymPy Groebner Jacobian unit ideals on each projective chart for both provided quartics: each has 9 rational points, 9 distinct tangents covering all 31 plane points, and the claimed pencil distinction. This is a complete bounded exact search, not an extrapolation.

## originality

PASS

Asgarli–Ghioca introduce tangent-filling curves and dual blocking criteria, and their degree-(q−1) family explicitly fails at q=5; they do not give the assessed exact nine-point smooth F5 quartic minimum in the inspected full primary paper. Blokhuis gives nontrivial dual blocking-set lower bound 9 but not exclusion of all full-pencil smooth quartics or attaining smooth witnesses. Complete finite certificates make this a distinct sharp conjunction of geometry, incidence, and arithmetic rather than a known genus-three point-count table. O PASS subject to unindexed finite-plane enumerations.

## value

PASS

The sharp minimum number of rational points for a geometrically smooth tangent-filling quartic over the smallest field q=5 at degree q−1 is a natural extremal question left open by broader construction bounds; the curve condition prevents generic blocking-set estimates from settling it. The two explicit smooth extremizers realize combinatorially distinct dual covering modes, making this a substantive complete finite classification of a sharp invariant rather than a random table entry. The full lower bound requires nontrivial exhaustive linear-algebra certificates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
