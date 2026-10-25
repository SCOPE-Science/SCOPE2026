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

# Verification

The general argument uses exact rational neighbor fractions \(1/3,1/2,2/3,1\) and strict comparisons \(0<p(1/3)=p(2/3)<p(1/2)=1\). Its boundary check includes the three-vertex cycle with one agent of each color. The sharp constructions use only the condition \(r\ge b\ge1\).

Run `python3 verify_cycle_enum.py` with a standard Python 3 interpreter. The checker exhausts each choice of vacant vertex and all choices of blue vertices in every case \(1\le b\le r\le9\), \(r+b\le15\), testing every occupied agent's one possible jump. Exact `fractions.Fraction` arithmetic is used with \(p(f)=2\min\{f,1-f\}\). It compares the observed best unrestricted integration and worst equilibrium integration to the theorem formulas. No randomness or external data are used.

This finite check cannot establish the formulas for all sizes. The unlimited-size correctness rests on the equilibrium-vacancy criterion, maximal blue-run length at most two, distinct bordering red agents, and constructive saturation of the upper and lower bounds.
