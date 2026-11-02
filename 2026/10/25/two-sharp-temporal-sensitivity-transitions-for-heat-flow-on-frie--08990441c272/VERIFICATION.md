---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For unnormalized Laplacian of k triangles sharing one vertex, constants and eigenvalue-1 pair-balanced leaf differences, eigenvalue-3 pair antisymmetry, and eigenvalue-(2k+1) hub-leaf radial mode give complete orthogonal decomposition (multiplicities 1,k-1,k,1). Summing projector kernels, the hub absolute row sum is 4ku, while leaf row sum is the max of 3e^-3t+(k-1)e^-t/k+u/k and 2(k-1)e^-t/k+2u/k. The partner entry sign changes at unique monotone root eta; strict convexity of f(x)=(4k²-1)x^k-3kx-(k-1) gives a unique earlier hub-to-leaf crossing xi. Their transversality yields exactly two corners, with asymptotics tau=(log k)/(2k)+O(log k/k²) and sigma=.5 log3+1/(2k)+O(k^-2). Independently constructed the exact rational projectors from graph Laplacian geometry and checked row norms at z=e^-t=1/2 for k=2,3,4, obtaining 41/64, 91/128, 769/1024 as predicted. Finite checks only corroborate the all-k proof.

## originality

PASS

Best-of-knowledge original surviving claim: Knowledge of the spectrum alone does not determine l∞ matrix norm without eigenspace projectors and sign control. The submitted derivation adds both. Prior work and access risks as in structured comparisons.

## value

PASS

The entire sharp time-derivative operator norm of heat flow on the natural friendship family is classified, including a hub-to-leaf maximizer transition and an independently scaled local sign transition. The exact graph-specific sensitivity law is not a textbook eigenvalue list alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
