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
# Verification and limitations

The mathematical proof in `RESULT.md` gives an exact operator-norm block reduction, explicit same-part equality cases, an explicit rank-two cross-part extremizer, and a nuclear-norm dual certificate attaining the same value. The determinant-based nuclear formula remains valid at \(p=q=2\), where the determinant vanishes. These derivations hold for every integer \(p,q\ge2\).

The packaged standalone `verify.py` requires Python 3 with NumPy and can be run as `python3 verify.py`. It tests all \(196\) ordered size pairs \(2\le p,q\le15\), checks sharp primal/dual equalities and includes \(1568\) randomized operator/nuclear dual inequalities. The tests are diagnostic only; no finite sample establishes the general theorem. No independent audit or external certification has been performed. Literature search cannot logically exclude every unknown equivalent formulation.
