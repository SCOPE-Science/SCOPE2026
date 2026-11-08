---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For C6 dihedral orbit distribution with six explicitly listed total weights polynomial in t, independent exact symbolic computation gives unique sextic root in rational interval (0.597345,0.597346) by sign and monotone derivative, all six weights strictly positive there, and total weight 1. Six orbits support 32 labeled edge configurations, each with <=4 open edges hence disconnected. Independently checked all 36 vertex-disjoint nonempty edge-family moment factorization identities in Q[t]/(F(t)), giving full 1-independence by inclusion-exclusion, not merely pairwise edge independence. All marginals equal p*. Independent thinning extends zero connectivity to 0<=p<=p*. No upper-bound optimality asserted.

## originality

PASS

Day-Falgas-Ravry-Hancock 2019/2020 already numerically suggested C6 threshold around .59733 and offered nonlinear finite-configuration programs; this is not a new decimal discovery or full threshold solution. In materially inspected full primary paper, the exact sextic positive orbit mass witness and rigorous improvement were not found in the relevant C6 sections. No equivalent matching exact certificate from inspected Resultary or primary literature. Priority of unindexed algebraic witnesses remains uncertain.

## value

PASS

C6 is the first cycle beyond already solved small instances in a natural 1-independent percolation connectivity problem. This concise exact algebraic probability law turns a previously numerical suggested scale ~0.59733 into a rigorous nontrivial lower bound p_zero(C6)>=0.597345547..., strictly beyond 1/sqrt(3). Exact six-orbit certificate can aid future sharp threshold work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
