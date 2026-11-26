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

For a nonempty witness set in one part, the complement of its diamond is exactly that part. Successive Boolean exclusion of earlier peeled parts makes such witnesses definable. On the core, every used color has representatives in at least two core parts, so every successor color can be matched while avoiding the current part. Matching peeled successors in the same peeled part proves bisimulation; the definable parts and color tests distinguish all proposed classes. Hence the atom and cardinality formulas hold. Injectivity within each part is also required for full generation: the all-subfamilies private-color test in the Finding is read as an equivalence for empty core, as its proof specifies. A sequential peeling order forbids its first i-1 distinct witness colors in part i. Exchanging any ascending pair of sizes minimizes the maximum n_i+i-1 in descending order; suffix palettes containing their designated witness attain the bound. This handles k=1 and zero generators. Depth is bounded by one new diamond per round, using complementation for a final singleton part. In the chain example each still-unsplit repeated color is visible from every part; only the part with a private current type is detected in the next refinement, splitting just the next chain color. This yields exactly k-1 strict steps, including the final two-part step.

## originality

PASS

The supported distinct result is the specialization to a single ordinary diamond on loopless complete multipartite frames: exact color-class quotient, optimal palette size, and worst-case depth with a matching family. Generic bisimulation and private elements are credited, not claimed as inventions.

## value

PASS

The quotient gives modal observability for every valuation, not only valuations attaining the generator minimum. It replaces generic partition refinement by an explicit support calculation and yields both a tight resource threshold and a sharp depth bound even when parts are tiny. Those answer natural classification and optimization questions about this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
