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

Run `python verify_protected_leaves.py` under Python 3, with no third-party packages. The script independently builds all recursive trees on \(n=2,\ldots,9\) by choosing every earlier parent for each arriving vertex and calculates exact integer statistics, then exact rational expectations and covariances. It enumerates 46,233 trees in total and verifies the partition, \(\operatorname{Cov}(L_n,P_n)=-n/12\) and \(\operatorname{Cov}(L_n,Q_n)=0\) for \(n\ge3\), the leaf variance, and the singleton cases. An independently implemented formal-series recurrence checks coefficient identities through degree \(120\) (118 sizes from \(3\) through \(120\)); it also checks a nonindependence witness.

The standalone code was executed against its actual supplied path, and completed successfully. These are finite computations. The unrestricted integer theorem is proved by the formal-power-series argument in RESULT.md and the leaf growth recurrence; no exhaustive finite experiment is asserted to certify every size. No independent audit has been performed.
