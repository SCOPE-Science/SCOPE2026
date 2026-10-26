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

Run `python verify.py` with Python 3, NumPy, SciPy. The checker builds the combinatorial Laplacian for every \(2\le n\le22\), samples seven times including \(t=0\), computes each kernel from a matrix exponential, and solves the associated Wasserstein transport LP. Its observed result was `PASS: 147 graph/time instances, 3 edge types where defined; independent LP and matrix exponentials`.

The all-dimension, all-time proof is analytic: the signed heat-kernel eigenmode identities, the convex-exponential inequality controlling ordinary-vertex signs, exact graph-distance transport, and elementary maximization. The finite checks do not certify those universal quantifiers by enumeration. Independent scientific audit: not performed.
