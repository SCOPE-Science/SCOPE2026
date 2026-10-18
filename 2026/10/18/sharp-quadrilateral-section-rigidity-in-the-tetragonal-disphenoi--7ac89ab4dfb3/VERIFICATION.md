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

# Verification of the displayed theorem

The proof uses invariant affine-plane measure rather than uniform orientation followed by a uniform conditional hitting offset. The distinction is essential: integration first over all offsets produces the length-weighted Crofton edge-crossing identity, and averaging over normals gives the classical exterior-angle mean-width denominator.

The six edge lengths, outward facet normals, two exterior angle values, exact derivative cancellations, endpoint limits, and the Taylor coefficient are explicitly shown in `RESULT.md`. The derivative sign yields the full positive-parameter inequality, independently of numerical sampling. The exact lower value occurs only at \(t=1\).

The delivered `checker.py` uses only Python standard-library functions. Run `python3 checker.py`. It independently forms and sorts projected vertex heights at 180,001 deterministic near-uniform spherical directions for each of seven shape parameters, checking the Crofton ratio, the mean-width identity, and the expected polygon-vertex count. It also numerically checks the one-parameter monotonicity profile and local quadratic coefficient. The program prints `VERIFY_OK`; finite checks are sanity tests, not an infinite proof or an independent scientific audit.

The historical-priority search is bounded. Mathematical claims are restricted to three-dimensional nondegenerate tetrahedra and, for the shape-rigidity statement, the tetragonal disphenoids \(T_t\) with \(t>0\). No assertion of rigidity in the complete two-parameter family of equifacial tetrahedra is made.
