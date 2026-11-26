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

For a (2,1,1) allocation every comparison to another singleton is automatic after removal. A singleton agent facing the pair must value her own good at least as much as the lesser of the two paired goods. Thus actual EF1 depends only on strict orders when no ties occur, and any allocation surviving a strict tie refinement also satisfies the original weak inequalities. Relabeling the goods to fix the first order is unique and preserves the labeled allocation count; the other five orders run independently over all 24 possibilities. An independent exact program built the 36 candidate allocations by surjective assignments, used literal cardinal EF1 on utilities 4,3,2,1 in the respective orders, and accumulated the histogram by profile chunks. All 7,962,624 profiles and every reported cell matched, with minimum two, maximum eighteen, minimum proportion 1/1152, and first moment 64/9. The latter also follows by counting the four independent singleton-agent tests of probability 2/3 for each allocation. Direct cardinal checks gave exactly the two displayed balanced allocations for the sharpness witness, and zero among the 243 complete allocations of the prior five-good example. With at most three goods each occupied group can have a singleton. This proves four-good universal multiplicity and the smallest complete EF1 nonexistence size of five.

## originality

PASS

The three-couple obstruction with five goods is prior work, not credited as new. The inspected same-model theorem supplies that obstruction but not sharp four-good positive multiplicity or the exact profile law. Known two-group, double-fairness, online single-agent and variable-size complexity results differ in the model or quantifiers. The best-of-knowledge pass concerns the sharp balanced four-good universal minimum and strict census, including the new positive side needed for the cutoff.

## value

PASS

Four goods is the last open size immediately before the known five-good failure and the first size for which singleton-only allocation cannot solve EF1. The sharp positive multiplicity shows unavoidable choice among balanced labels even in the tight case, and the full strict census quantifies how often that case and all other multiplicities occur. This is a natural small-instance frontier, useful as an exact benchmark, not an arbitrarily sized enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
