---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Re-audited repaired RESULT.md: size-two neighborhoods N(b_2) and N(a_(n-1)) separate the respective same-shore pair of colors, and the four cross-edges force all four core colors distinct. It follows for a four-color optimum that the last two B colors are unavailable on the first n-1 A vertices. The allowed binary prefixes start with two different colors, and the third fixes the repeated symbol. Repeating the singleton after that would leave no singleton, so the entire interior A block must repeat the third color. The final A vertex may instead use c_2, which is absent from the first n-1 A vertices. The reverse suffix argument on B excludes c_0 throughout and c_1 except at b_1 and forces the claimed symmetric pattern. Only pendant endpoints can use colors from the other shore, and these choices are proper because each has its single neighbor in a different color. All prefix and suffix singleton conditions hold, including at the full blocks and degrees one and two. For n>=4 both interior blocks are nonempty, so the four binary choices are individually recoverable and no assignments duplicate. Naming the core multiplies 16 by 4!. The n=3 boundary in the repair is verified separately: each pendant endpoint has three permissible choices, and a triple beginning with two distinct colors always has a singleton, giving 9 normalized or 216 named colorings.

## originality

PASS

For the frozen version the scalar contribution is covered: a pre-existing chain-graph theorem gives exactly four and its proof already constructs one optimal pattern. That is a concrete prior-coverage fail for any novelty claim on the scalar, not a mathematical defect. The corrected result explicitly attributes the scalar and the construction, and asserts novelty only for the full optimal family and census. Those remain distinct on the inspected evidence. In particular the prior construction uses disjoint colors on the shores and supplies one normalized form, while the repaired theorem gives every normalized form including those with cross-shore endpoint reuse and proves there are exactly sixteen.

## value

PASS

The repaired result determines the complete minimum-coloring space on the canonical nested bipartite family. It explains why the 16 color-permutation classes persist as the graph grows and identifies exactly where cross-shore palette sharing can occur. This is a natural optimizer classification not supplied by the known scalar or by a single chain-graph optimum construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
