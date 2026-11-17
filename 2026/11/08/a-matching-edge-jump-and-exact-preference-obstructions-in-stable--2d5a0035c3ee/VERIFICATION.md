---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

In G_{m,r}, where the two hubs are nonadjacent and the opposite part is a matching plus isolates, orient each matching edge once and join edges toward hubs for n≥3 to obtain maximum reachable set size four (three without matched edges); reverse joins for n≤2. Koana–Oh–Yoneda acyclic reachability implies stable-colour upper bounds. An explicit ranking profile on G_{1,1} blocks all 12 proper named three-colour assignments via a mutual-envy pair; subgraph monotonicity extends the 4 lower bound. The ordinary triangle/K_{2,n} cases give other lower bounds; a neighbor-colour counting proof shows Grundy=3 on the matched n≥3 family. Independently enumerated 6^5=7776 ranking profiles against all 12 assignments and classified exactly 624 with no acyclic envy graph: 576 unavoidable 2-cycles plus 48 with longer cycles only. This is exhaustive for labelled G_{1,1} with exactly three colors, not for all graph sizes.

## originality

PASS

A motivated five-vertex explicit preference obstruction yields a stable-chromatic jump beyond the Grundy bound and an exact full-profile obstruction census; inspected known stable-colouring families do not imply the new lower bound or census.

## value

PASS

A single matching-edge perturbation forces preference stability from three to four colors while the Grundy number remains three, an exact small obstruction to a natural lower-bound mechanism. Exhaustive 624/576/48 structure distinguishes unavoidable mutual envy from intrinsically longer blocking cycles; such fine enumeration of the minimal witness has intrinsic combinatorial value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
