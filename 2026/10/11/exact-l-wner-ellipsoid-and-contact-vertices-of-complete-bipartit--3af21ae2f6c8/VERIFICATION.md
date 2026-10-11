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
# Reproducibility and limits

Run `python3 verify.py` using the Python 3 standard library. The checker reconstructs signed edge-incidence endpoints independently, computes the quadratic ellipsoid gauge through the Laplacian eigenspaces, and checks all sign patterns on eleven bipartite graphs. It also constructs the proposed three-family contact-point probability measure and verifies its full covariance matrix using exact rational arithmetic for 64 pairs of part sizes. Expected output contains `PASS: 64 exact all-coordinate covariance checks;  11 exhaustive sign-cube contact/containment checks`.

The finite cases are supporting consistency checks only. The infinite theorem follows from the symbolic projection inequality, exact equality classification for sign matrices, explicit positive contact weights, and the trace/determinant comparison proved in `RESULT.md`. No independent audit or external proof certification has been performed.
