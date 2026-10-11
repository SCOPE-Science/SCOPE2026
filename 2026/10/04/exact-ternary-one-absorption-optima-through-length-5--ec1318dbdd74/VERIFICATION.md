---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For each length, a one-absorption-correcting code is exactly a family of source words whose distinct output balls are pairwise disjoint. The package constructs every absorption ball directly from saturated adjacent addition together with the terminal-missing event, then solves both the output set-packing integer program and the equivalent conflict-graph maximum independent-set integer program. Both formulations report zero MIP gap and optima \(3,6,13,29\) for lengths two through five; the supplied witnesses are checked directly. An independent reconstruction of the set-packing matrix reproduced all four optima with exact integrality and zero solver gap. The claim is a finite exhaustive optimization, so an exact integer-program optimum is an appropriate complete certificate of the upper bounds.

## originality

PASS

Ye and Elishco define the same absorption channel and correction criterion, but their complete primary paper focuses on constructions, redundancy, and asymptotic behavior rather than the four small ternary optima. A 2024 nonbinary follow-up advertises improved ternary/general constructions and redundancy bounds; accessible abstract and metadata did not expose a finite optimum table, and no full text was available through the open routes inspected in this run. Current Resultary searches for the exact parameter tuple returned no equivalent finite classification.

## value

PASS

The absorption channel is a recent coding model and the ternary alphabet is the first genuinely nonbinary case. Exact optima through length five provide a sharp baseline for testing general constructions and finite-length bounds, with a complete witness set rather than a single isolated computation. This is a motivated finite cutoff on a natural new model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
