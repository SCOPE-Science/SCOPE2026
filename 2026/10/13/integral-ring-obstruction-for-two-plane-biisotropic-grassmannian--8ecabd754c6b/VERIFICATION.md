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

## Reproducibility and scope

The standalone `verify.py` requires only Python 3. Execute `python3 verify.py`; the expected terminal line begins `VERIFY_OK`. It implements independent ballot-path enumeration for Grassmannian degrees, and enumerates the \(k=2\) cell dimensions from the fixed-point formula in the cited paper. A finite test does not establish the infinitely quantified theorem; the proof rests on smooth Plücker linear-section geometry, weak Lefschetz, Pieri's rule, and the integral top-power invariant.

The source's posted version, arXiv:2610.03309v1, states the integral cohomology group equality and explicitly leaves multiplicative questions separate. This package proves a negative comparison for the full family with \(k=2\), not a presentation of its rings or a claim about rational coefficient ring isomorphism. Other parameters have not been assessed.
