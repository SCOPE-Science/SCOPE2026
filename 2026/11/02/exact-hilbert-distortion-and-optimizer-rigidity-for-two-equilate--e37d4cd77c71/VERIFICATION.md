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

# Verification of the mathematical claim

The paper `RESULT.md` gives a dimension-independent analytic proof. In particular, apply the exact centroid identity to all within-block and cross-block pairs, and conclude \(D^2v^2\ge\Sigma\). The positive-semidefinite construction uses two orthogonal centered equilateral-simplex Gram matrices and a nonnegative rank-one centroid-separation matrix. It realizes the lower bound for all admissible parameters, including the transition \(\Sigma=v^2\).

The equality proof requires no assumption that a competing embedding respects the finite metric's permutation symmetry. Exact equality in the centroid identity and individual squared-distance constraints forces the optimizer's three pair-orbit distances, shared or separated centroids, and the stated affine dimension. The graph specialization sets \((u,w,v)=(1,2,1)\).

`checker.py` can be replayed with `python3 checker.py` using only the Python standard library. During the self-review it returned:

`CHECK_OK rational_matrix_cases= 2448 identity_cases= 448 validated_relations= 244464 branches= <,=,>`

The checker uses exact rational arithmetic to test the constructed Gram matrices, rank conditions, triangle constraints, distortion formula, and independent centroid identities. It is a finite numerical certificate for sampled rational inputs, **not** an exhaustive proof over all real metric parameters and Hilbert spaces. Originality remains qualified by Robertson's earlier equal-intrablock case and possible other historical equivalent formulations. No independent mathematical audit has been performed.
