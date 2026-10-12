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

The classical optimum is established analytically for arbitrary measurable binary response functions. Shared randomness is handled by convexity, so deterministic strategies suffice. For fixed first response, the second response is optimized pointwise, reducing the problem to an \(L^1\) bound for the hemisphere transform.

The critical analytic chain is: spherical-lune geometry gives Lipschitz constant \(2/\pi\); oddness plus Lévy spherical isoperimetry gives the exact superlevel estimate; layer-cake integration gives classical bias at most \(1-2/\pi\); the hemispherical response attains equality. The singlet value follows from the exact fact that the dot product of two independent uniform directions on \(\mathbb S^2\) is uniform on \([-1,1]\).

`verify.py` was executed from the packaged path and returned `VERIFY_OK`. It checks the displayed algebra, quadratures the hemispherical transform at high resolution, and performs fixed-seed Monte Carlo stress tests of the displayed classical and quantum strategies. Those finite checks are not used as evidence for the infinite-dimensional optimality theorem.

The verification does not establish that \(3/4\) is the globally optimal quantum value.
