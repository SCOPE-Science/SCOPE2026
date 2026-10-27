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

The proof itself establishes the result for every \(0<q\le1\) and \(0\le\beta<1\). Run `python verify_qberezin_radius.py` with a standard Python 3 installation to reproduce 41,412 sampled and algebraic consistency checks. Tests include the normalized-kernel overlap, direct geometric-series matrix element, unique-root maximization against an explicit radial grid, explicit radical witness at \(q=\beta=1/2\), and asymptotic coefficient tests near the parameter endpoints. The script is a reproducibility aid; randomized and finite computations do not certify the universal assertions. Independent audit status remains not performed.
