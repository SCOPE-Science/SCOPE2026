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

The frozen mathematics is correct. Cyclic query edges admit a cyclic orientation. A loop or simple directed cycle in the contraction can be lifted using disjoint paths in the component trees; conversely any directed cycle under a query orientation must project to a quotient cycle. A height-h chain forces at least h components, and longest-chain-ending rank layers supply equality. At equality the chain traverses every component and fixes its entire topological order, proving uniqueness of the strict surjection. Conversely each such surjection and its fiberwise trees gives a maximum support. The exact sum follows by Cayley, including singleton fibers and a chain's empty support. The repaired RESULT retains this proof and domain. Fresh enumeration via transitively closed suborders of a chain and relabeling independently matched literal extension traces to the forest-with-ordered-fibers criterion and the maximum-support count in every order 1–5 (4,231 posets and 4,332,544 support candidates at order 5). Replay: python3 /workspace/audit_checks/03_poset_comparisons.py. The frozen verifier and reported output were inspected, not executed; these are finite checks only.

## originality

PASS

For the repaired extremizer identification and counting identity only. The frozen bundled contribution cannot all be credited as distinct: a different public Resultary record gives the identical forest/contraction criterion and n minus h dimension, with slightly broader scope (includes the empty poset). This comparison does not settle priority. The distinct claim is the unique correspondence with all h-layer strict surjections and the resulting Cayley-weighted exact count. This uses a chain-rigidity argument at equality and a bijection, not just the exhibited canonical rank-layer construction. No inspected source supplies that census or an equivalent exact identity.

## value

PASS

The equality-case bijection makes a natural extremal family inspectable via canonical fibers and yields an exact counting identity for labeled query sets. It distinguishes supports obtainable from different strict h-layer maps from a single rank construction, without claiming efficient evaluation for all posets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
