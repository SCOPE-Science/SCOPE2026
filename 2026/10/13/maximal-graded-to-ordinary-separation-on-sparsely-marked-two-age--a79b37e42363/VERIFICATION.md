---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The n×n S5 frame has reflexive named row and column equivalences, with atom p(i,j) iff j=i or j=i−1 and n≥3. At zero depth p has two types. Ordinary bisimulation never splits them because every row and column meets both colors. For graded depth t, a cell signature is exactly (p,previous row-type histogram,previous column-type histogram). The marked-edge graph is the alternating Hamilton path r0–c0–r1–…–r(n−1)–c(n−1), whose degree/histogram recursion peels one row and one column alternately. At depth 1≤t≤n−2, there are (t+1)² Cartesian histogram blocks and precisely three mixed-color blocks; hence K_t=(t+1)²+3, with K_{n−1}=n², and n−1 is minimal. Any nonconstant one-bit valuation has ≥2 ordinary classes, bounding G/B≤n²/2; the construction attains it. Independently written exact count-histogram refinement over every 3≤n≤17 reproduced the full spectrum, including n=5: 2,7,12,19,25; not used as infinite proof. The induction, not the finite experiment, supports the unrestricted quantifiers.

## originality

PASS

The claim is the exact grid-specific maximum G/B=n²/2 and full graded-depth spectrum, not generic expressiveness of graded modalities. The p-marking is a path on row/column classes, hence this is distinct from Latin-square proper-cover constructions. Best-of-knowledge originality follows from actual semantic published-record searches and the specifically inspected primary theorem material; unsuccessful searching alone is not proof of novelty.

## value

PASS

The exact contrast between ordinary and graded definability is a natural finite-model-theory separation problem. A sparse explicit path marking both attains the universal n²/2 ratio and determines the exact depth at which all grid worlds become distinguishable. The depth census and sharp endpoint are independently useful for counting refinement and model checking, not a mere renaming of general modal equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
