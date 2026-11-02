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

The 1,344 Latin squares with normalized first row expand uniquely by 120 symbol relabelings to 161,280 fully labeled squares. Two explicit representatives B and cyclic C have autotopism stabilizers of orders 12 and 100, verified independently from all 120² row/column permutation pairs; orbit-stabilizer yields 144,000 noncyclic and 17,280 cyclic squares. The cyclic class has no intercalates. The four switches from B lie in its even-isotopy orbit, whose size is 60³/12=18,000. An independent full neighbor BFS from B reached all 18,000 and exact shells (1,4,12,36,108,252,612,1284,2256,3624,4812,3828,1112,59), so graph transitivity yields diameter/radius 13. The eight cosets of A5³ give eight components, each 4-regular with 36,000 edges. The four classical parity triples split two per component by relabeling parity and preservation of all triples. The finite complete enumeration is legitimate finite proof, not sampling or infinite extrapolation.

## originality

PASS

Wanless 2004 directly studies intercalate switching on isotopy/main classes, not all fully labeled squares. Its order-five quotient has two isolated class vertices, collapsing 144,000 noncyclic states to a single vertex and losing the eight individual connected sectors and diameter. The earlier parity obstruction alone yields four signatures, not their twofold splitting. Cavenagh–Stones 2011 is about near-automorphisms; Jacobson–Matthews uses a broader move system through improper squares. No inspected primary result implies the labeled census.

## value

PASS

A canonical finite reconfiguration graph for a historically studied combinatorial design problem. The exact eight components refine classical parity constraints and show an obstruction that the two-state isotopy quotient completely hides; uniform 13-step diameter provides a natural exact reachability invariant needed for intercalate-only local-move studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
