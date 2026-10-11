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
The theorem is proved symbolically in `RESULT.md`; finite checking is corroborative only.

Critical checks:
- The cycle has exactly \(n\) proper tubes of each cardinality \(1,\ldots,n-1\) and one full tube.
- The simplex-sum affine total is therefore \(n(n-1)+1\).
- A proper tube of size \(k\) contains exactly \(k(k+1)/2\) tubes.
- Its projected intrinsic normal has squared norm \(k(n-k)/n\).
- The displayed factorization of \(d_{n,k}^2-d_{n,1}^2\) is strictly positive for \(k>1\).
- Summing the singleton-facet ball constraints gives the same radius as a universal upper bound and forces the unique center.

`verify.py` checks these identities with exact rational arithmetic for \(3\le n\le200\). It does not establish novelty and is not used as the infinite proof.
