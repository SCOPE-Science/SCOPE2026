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
The universal complete-bipartite proof is analytic: the four Laplacian spectral projectors reduce every entry orbit to explicit scalar combinations of \(\varphi(ph)\), \(\varphi(qh)\), and \(\varphi((p+q)h)\), and those combinations factor into positive rational functions for \(h>0\).

For \(P_4\), direct exact inversion produces one potentially sign-changing entry orbit. Its numerator is \(-3h\) times \(h^4-6h^3-60h^2-108h-72\); Descartes' rule gives one positive root, and all other entry numerators are nonnegative for \(h\ge0\). The packaged checker independently reconstructs the exact \(h=12\) matrix, verifies row sums, and compares complete-bipartite projector formulas against exact rational inversions on a finite regression suite.

The finite regression suite is not used as proof of the universal statement. Weighted graphs, internal Runge--Kutta stages, floating-point arithmetic, higher Padé orders, and a full classification of all larger graphs remain outside scope.
