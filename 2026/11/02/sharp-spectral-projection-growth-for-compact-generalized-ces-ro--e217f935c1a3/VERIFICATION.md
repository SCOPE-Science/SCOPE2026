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
# Verification of the stated operator identity

Run `python3 check.py` with Python 3 standard library. The script performs fraction-exact finite-section checks of the known eigenvectors and their rank-one spectral projections: \(N=1,\ldots,8\); \(m=0,\ldots,N-1\); \(t\in\{0,1/5,1/2,2/3,9/10\}\), totaling 180 cases. It checks the two endpoint operator norms on each finite section and reports selected asymptotic ratios. Exact finite sections do not verify the infinite-dimensional asymptotic theorem: the proof uses compactness, spectral semisimplicity, rank-one duality, and Gaussian local limits.

Independent audit has not been performed. No formal proof certification is claimed.
