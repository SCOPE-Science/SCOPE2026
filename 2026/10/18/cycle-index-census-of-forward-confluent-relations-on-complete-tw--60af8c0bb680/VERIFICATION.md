---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On the ordinal sum of two antichains the only distinct comparable source pairs run from bottom to top. A bottom-source top target is maximal and must be repeated verbatim in every top row; a bottom target can be witnessed by any top target, or else only itself. This proves necessity and sufficiency of the U,T conditions. At fixed supports each hit bottom-source column has 2^p-1 nonzero choices. When T is empty each top row independently either has a top target or is forced on U; when T is nonempty only the columns in T are forced in top rows. These give exactly the two labelled terms. Under a pair of level permutations, an incidence block for cycles (d,e) has gcd(d,e) orbits. Hit target sets consist of whole cycles. With T nonempty there is one forced top-source pattern on each active top target cycle, with independently free top-to-bottom incidence, and subtracting the empty T term gives H1. With T empty, the top-row alternative is constant along each source cycle and forcing U removes exactly the incidence blocks to its active cycles, giving H0. Burnside class weights are 1/(z_lambda z_mu), since automorphisms cannot exchange levels. Direct exhaustive 2-by-2 validation over all 65536 relations tested the original quantified axiom and the normal form relation by relation. Fixed counts for identity, bottom swap, top swap and simultaneous swap are 11401, 355, 409, 103, averaging to 3067; formula arithmetic also reproduced every larger table row without claiming exhaustive enumeration there. Replay: /workspace/branches/814cdce7-110d-4a08-9590-ee0896a2ffc8/record2_oracle.py. The supplied verify.py was inspected, not run. The general counting argument, not the finite checks, establishes the formula for all positive level sizes.

## originality

PASS

The supported claim is the exact labelled and isomorphism census for arbitrary forward-confluent relations with both layers nontrivial, especially the full fixed-count formula. Prior coverage on chains and labelled rooted forks concerns boundary carriers; the two-sided two-level comparison imposes an additional axiom.

## value

PASS

Complete two-level orders are a natural homogeneous family with incomparable worlds on both levels and a nontrivial automorphism group. The formula gives exact benchmarks for admissible relations and their isomorphism classes without enumerating every incidence matrix; the zero-versus-positive top-target distinction explains the constraint structurally and translates it into actual fixed counts, not just an invocation of Burnside. The orbit counts are useful for producing nonredundant finite-frame test collections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
