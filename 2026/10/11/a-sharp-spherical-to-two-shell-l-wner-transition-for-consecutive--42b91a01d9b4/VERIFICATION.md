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
# Verification and evidence

The algebraic verification program `verify_loewner_slab.py` was executed from its actual extracted package input before packaging. It reported `PASS 27719 integer parameter triples (n=2..54), boundary/contact/semiaxis checks`. The independent SciPy/Numpy D-optimal weight-layer optimizer `independent_optimizer.py` was executed against the same formula and reported `VERIFIED 559 slab parameter triples; worst opt gap 9.947598300641403e-13`. It compared against independently optimized mixtures on every allowed cardinality layer, with three starting distributions per triple.

For mathematical verification, see Steps 1–4 of `RESULT.md`. Especially, the critical inequality \(q(k)-n=\eta(k-a)(k-b)\) is justified by the exact stationarity equation and the sign proof for \(\eta\); the numerical checks are not being used to prove it. The covariance matrix is strictly positive for all stated integer parameters because \(a<b\) and the allowed binary polytope has full affine dimension. All input and output quantities are stated in the standard coordinate Euclidean metric.

Independent auditing and validation have not been performed. An equivalent earlier result under optimal experimental-design terminology remains a literature risk.
