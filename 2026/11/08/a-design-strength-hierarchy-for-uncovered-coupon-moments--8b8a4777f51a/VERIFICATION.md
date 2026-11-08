---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification evidence

The accompanying `verify.py` uses only Python's standard library (`fractions`, `itertools`, `math`). Run `python verify.py` from the directory containing the supplied files. Expected final output: `PASS: 702 exact rational checks; finite sizes only`.

The checks cover fixed-size subset laws for sets of sizes four through seven, including uniform, degenerate, cyclic, and explicitly biased distributions; the Jensen inequality and equality cases for admissible moment ranks; and an independent two-round outcome enumeration for selected ranks. They also construct \(\mathrm{PG}(2,q)\) over the prime fields \(q=2,3,5\), reconstruct the collinear fraction and explicit rational gaps, and independently enumerate all line-draw sequences of lengths two and three for orders two and three.

The general statement is established by the analytical double-counting, strict convexity, and complement-incidence arguments in `RESULT.md`, not by finite computation. The non-Desarguesian extension uses only the projective-plane incidence axioms. The verified statements do not address stochastic ordering of completion times or prove existence of projective planes at unsupported orders. Independent external mathematical audit has not been performed.
