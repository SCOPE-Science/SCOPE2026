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

# Verification of the three-digit repunit digit-sum theorem

The precise universal assertion is proved symbolically in `RESULT.md`, using a reversible three-class congruence representation and a sharp small-sum exclusion. The proof applies to every integer base \(b\ge2\) and every positive multiplier; it does **not** infer an infinite assertion from an experiment.

The independently implemented script `verify.py` constructs a finite automaton whose states record used base-\(b\) digit sum, residue modulo \(b^2+b+1\), and the residue class modulo three of the next digit position. Every allowed next digit is traversed, including zeros; reachable states are visited at most once. For each prescribed finite sum bound, this models representations of *arbitrary finite length*. A separate additive-semigroup dynamic program predicts the claimed digit sums. The script compares all sums through \(4b+21\) for bases \(2\) through \(16\), plus \(18\), \(20\), and \(23\).

Actual check result: `PASS: 18 bases; 1162 digit-sum membership comparisons; 551625 finite-state visits.` The verifier additionally checks the asserted genus, Frobenius boundary, and the exceptional congruence-one branch within those ranges.

To reproduce, save the companion file `verify.py` in the same folder and execute `python3 verify.py` with Python 3 and its standard library. This provides an independent finite-range test of all stated branches, not an independent mathematical proof or a check of all infinite parameters.
