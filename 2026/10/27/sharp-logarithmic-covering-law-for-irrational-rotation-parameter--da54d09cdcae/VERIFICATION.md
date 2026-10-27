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
# Reproducibility and verified scope

Run `python verify.py` with Python 3 and SymPy from the directory containing `verify.py`. The actual standalone program passed 7,139 finite exact-rational and symbolic assertions. It checks Möbius differentiation, rational plateau widths, periodic geometric-series truncation, constancy of finite Sturmian sums between bounded-denominator thresholds, and the expanding right-branch example.

The analytic proof, not this finite program, establishes universal quantifiers. The nonstandard inputs from primary literature are Gaivão–Laurent–Nogueira (arXiv:2212.10944v1), Definition 5.1, Theorem 5.2 and Proposition 7.1; the complementary comparison with Janson–Öberg (arXiv:1709.06398v1), Section 7, concerns the known single-slope gauge-Hausdorff upper covering mechanism. No formal proof assistant verification or independent audit has been performed. The uniform covering constants are not asserted at either endpoint of the full rotation interval.
