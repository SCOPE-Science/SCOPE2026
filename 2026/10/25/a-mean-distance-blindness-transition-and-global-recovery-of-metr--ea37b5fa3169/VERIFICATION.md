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

The proof is given by conditional integration over six disjoint ordered-edge pair classes and a strictly monotone inversion at the unique mean-blind ratio. It does not rely on computational enumeration.

Run the embedded `checker.py` with `python3 checker.py`. The code uses only Python's standard library. It checks 80 exact rational three-parameter identities, integrates the piecewise-linear distance density exactly for moments of orders zero through two, checks 25 critical-ratio identities and the explicit nonidentifiability witness, and compares four independent deterministic point-pair grids with the moment formulas.

All tests passed in the recorded run. The deterministic grids do not establish uniform error bounds, and the finite rational tests do not replace the infinite-parameter analytic proof. The theorem assumes strictly positive lengths on a known two-loop/one-bridge topology. Historical-priority review is not exhaustive; no independent scientific audit has been performed.
