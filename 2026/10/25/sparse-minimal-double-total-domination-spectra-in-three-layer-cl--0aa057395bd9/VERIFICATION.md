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

Set A,B,C as selected column subsets in the outer/middle/outer K_n layers and a,b,c sizes. Direct neighborhood counts yield outer conditions a,c≥2 and required B coverage if an outer count equals two, plus separate middle conditions b=0,1,2,≥3. The proof divides minimal solutions into b=0,1,2,3,4 and excludes b≥5 because a middle vertex becomes redundant; in each case outer minimality and deletion of B vertices force a finite size profile. The resulting counts are the six terms using q=C(n−2,2), r=2q+C(n−2,3), h=C(n−3,3), j=C(n−3,2); n=6,7 coincident exponents are summed. Independently exhaustively checked all 2^18=262144 layer selections at n=6 by checking 3n neighbor inequalities and every one-vertex deletion; obtained 116290 feasible sets and minimal cardinality counts {6:15,7:600,8:1290,9:920,12:1}, matching the polynomial. The all-n proof rests on complete b-case arguments, not extrapolation from n=6.

## originality

PASS

Kazemi–Pahlavsay–Stones classify and bound scalar k-tuple total domination on Cartesian products of complete graphs, giving the scalar lower bound 6 but no inclusion-minimal spectrum for clique × path. Kazemi's 2017 upper k-tuple total-domination work covers rook graphs and general extremal bounds, not the target G_n. Path × path double total domination and Roman/paired variants concern different graphs or parameters. The exact complete inclusion-minimal polynomial and unique 2n maximum are not implied by the inspected sources.

## value

PASS

A complete cardinality polynomial for inclusion-minimal double total domination on the natural width-three clique strip exposes a striking sparse spectrum with a unique maximum and potentially unbounded gap, information not captured by the known scalar minimum. The three-layer transition makes this more than a routine complete-graph substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
