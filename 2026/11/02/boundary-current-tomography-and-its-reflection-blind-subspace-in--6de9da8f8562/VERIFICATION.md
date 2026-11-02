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

# Verification record

The result is an analytical statement about stationary membrane transport and ideal data. The Green-function endpoint calculation, interface correction, signed-current transform, analytic identity theorem, odd-polynomial measure argument, Jordan-decomposition characterization of nonnegative compatible sources, nonparametric finite-sampling counterexample and reflection symmetry are demonstrated explicitly in `RESULT.md`.

`check_current.py` is an independent computational cross-check. Execute with Python 3 and NumPy 2 or later using `python3 check_current.py`; its observed output was `PASS 428 deterministic checks including probability-law fiber`. The code exercises 54 parameter sets in an explicit point-source Green solution, two distinct reset laws with identical odd parts, an asymmetric single-rate zero-current example, the small-reset-rate slope, and a second finite-volume solver with membrane resistance included between cell centers. All tested finite-volume errors decrease with mesh refinement. No simulation or finite grid check is used as an infinite-dimensional proof.

The checks establish correctness of the written formulas to the extent of the displayed analytical proof and deterministic cross-tests. They do not establish noise-stable inverse recovery, identify an otherwise free symmetric source component, resolve priority against all prior literature, or constitute an independent audit.
