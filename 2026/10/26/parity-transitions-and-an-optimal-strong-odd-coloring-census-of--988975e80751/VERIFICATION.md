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

PASS: Vertex w_i of degree two forces neighboring rim colors different. At v_i, neighborhood {hub,b_{i−1},b_i} has all nonzero color multiplicities odd exactly when both b are hub color or both are distinct nonhub; propagation around cycle gives two modes. Hub forces each used rim color class to appear an odd number of times. Cycle independence bound and parity show lower bounds on palette: 2 rim colors only for n≡2 mod4, 3 rim colors possible odd n except 5, and 4 rim colors for 4|n; case n5 three-color rim class (3,1,1) violates α(C5)=2. Explicit seed words and length+4 extension attain bounds. For odd n≠5, signed 3×3 cycle trace characteristic polynomial λ³+λ+2 gives N=2^n−2−3S_n+24[3|n]; mode B cyclic square colorings require 3|n. At n5 inclusion-exclusion gives exactly 68 nonhub subdivisions per 5! rim word and 6 choices of hub, N5=49680. For 4|n, transition matrices A4 and B4 over squarefree parity group algebra give complete exact counts. Independent integer closed-walk parity DP for n3..12 matched counts 48,360,49680,6,168,37920,552,6,1848,10670760 and minimum palettes; finite evidence supplements all-order proof.

## originality

PASS

PASS qualified: Kwon–Park define strong odd coloring and sparse bounds, Caro–Petruševski–Škrekovski–Tuza address broad graph classes, and Manattu–Vinay–Lakshmanan prove ordinary wheel values with distance-two rim constraints. Subdivided gear graph has a different neighborhood, forced two-mode decomposition and optimum census. Named-colour count and n5 exception are not implied by cited wheel theorem. Unindexed gear/Jahangir parity results remain risk.

## value

PASS

PASS: A canonical bipartite wheel family and a recently defined natural vertex-coloring invariant exhibit sharp mod-four phase transitions, isolated n5 six-color anomaly and complete exact counts of every optimal named coloring. The complete structural mode classification plus fixed-size transfer count is a useful natural classification, not a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
