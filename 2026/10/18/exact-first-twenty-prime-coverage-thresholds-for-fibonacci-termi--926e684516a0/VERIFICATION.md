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

Using the canonical F_1=F_2=1 encoding with a_1=0 and infinite zero padding, parsing zero followed by one as D and other zeros as S is unique and records only complete-block boundaries. The admissible word counts satisfy w_0=w_1=1 and w_m=w_{m-1}+w_{m-2}. An independently written exact checker enumerated the complete prime interval and additionally generated the admissible word sets to test equality, not only the sizes. It reproduced all twenty counts, thresholds and last words. In particular 135,340 primes through 1,803,947 fill exactly 10,946 length-20 classes; DSSDSSSSDSDSSSSS first occurs at that prime. The maximum of the exact first-hit primes proves coverage at the stated bound and failure at all lower bounds. Chang–Verwee Theorems 1.5–1.6 also justify existence for general fixed lengths in this convention.

## originality

PASS

The distinct claim supported here is the exact twenty-length finite coverage frontier, including the sharp first-hit witnesses, not eventual coverage of fixed classes. The inspected primary source supplies an asymptotic for each fixed word but not these finite maxima. No equivalent table was established by the bounded catalogue and literal-witness searches.

## value

PASS

A sharp coverage frontier and its last-hit witnesses are useful finite benchmarks for algorithms and quantitative predictions near the growing-word problem. The cutoff includes a complete family of 10,946 terminal classes, with both the sharp upper bound and a certified obstruction below it, rather than selected prime examples or approximate frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
