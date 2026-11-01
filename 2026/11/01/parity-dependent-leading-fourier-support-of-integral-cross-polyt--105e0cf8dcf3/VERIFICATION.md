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

The analytic proof uses an explicitly stated Fourier normalization, exact Laplace transform and residue parity argument. Its dependence on integer frequencies is essential: \(e^{2\pi i a}=1\) for every integer pole \(a\).

Reproduction: run `python CHECK.py` with Python 3; no third-party packages are needed. This produces `EXACT_RESIDUE_TESTS_OK 1095`. The exact tests compare independently computed Laurent series to the closed formulas, and test all vectors in \(\{0,1,2\}^d\) for dimensions three through six. Finite computation is not a proof of the infinite-dimensional family. The mathematical proof and cited source comparison supply the asserted scope. Independent audit and validation have not been performed.
