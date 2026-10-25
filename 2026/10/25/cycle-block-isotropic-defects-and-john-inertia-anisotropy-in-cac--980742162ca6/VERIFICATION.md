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
# Verification evidence and limits

Run `python verify.py` using Python 3's standard library in the extracted package directory. Its observed completion marker was `VERIFY_OK exact_cycles=10 graphs= 7 monte_carlo=4`.

Exact rational checks reconstruct the centered uniform-sum density spline and integrate its polynomial pieces for cycle lengths 3 through 12. In particular they reproduce \(f_3(0)=3/8\), \(v_3=5/18\), \(\Theta_3=25/27\), \(f_4(0)=1/3\), \(v_4=3/10\), and \(\Theta_4=243/250\). Seven cacti with different cycle counts and bridge placements validate exact graph-count identities through Laplacian cofactor determinants; a seeded numerical independent rejection experiment checks the conditional second moments for cycle lengths 3 to 6.

These experiments do not establish the infinite-family result. The analytic proof in `RESULT.md` proves the edge-coordinate decomposition, Euclidean Jacobian, coarea volume identity, uniform covariance blocks, John contact conditions, and isotropic-defect factorization. The scientific limitations and residual bibliographic risk are stated in `RESULT.md` and `REVIEW.md`. No independent mathematical audit was performed.
