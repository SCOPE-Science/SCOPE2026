---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Each candidate variable occurs in at most two resident constraints and each resident tests the sum of at most two binary variables within an integer interval. Combining duplicate pair constraints reduces the dependency graph to disjoint paths/cycles; two-state dynamic programming gives feasible minimum L and maximum H in linear time. For any two feasible endpoint assignments, each forbidden mixed switch at opposite-sign changing sites becomes a directed implication; strongly connected components lie on sign-alternating paths or even cycles and change cardinality by at most one. Activating components in reverse condensation topological order preserves every local interval and sweeps all cardinalities between L and H. The 7-vertex three-arm exact-one construction yields feasible counts {1,3}, certifying a degree-three boundary. Independent exhaustive enumeration of 10843 path/cycle systems checked exact spectra; finite enumeration alone does not prove the SCC theorem.

## originality

PASS

Knop–Schierreich previously solved degree-two housing with arbitrary approval sets in polynomial time. Schierreich previously gave a linear-time algorithm only for upper-bound approvals, where deletion closure makes gap freedom trivial. Exact interval [ell,u] with positive lower bounds, a complete cardinality spectrum and a linear-time arbitrary-k constructive witness are stronger and not supplied by the inspected predecessor statements.

## value

PASS

The theorem upgrades a realistic local constraint class from decision solvability to complete feasible-size spectrum and linear-time construction at any size, with a sharp degree-three obstruction. It gives a reusable path/cycle binary-CSP exchange principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
