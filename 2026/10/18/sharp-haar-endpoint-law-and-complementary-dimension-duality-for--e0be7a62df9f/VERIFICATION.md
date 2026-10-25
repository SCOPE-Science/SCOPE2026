---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The final theorem is correct for fixed real n>=2 and 1<=k<n. In graph coordinates T around any maximizing coordinate plane, rows of T are inside the l1 unit ball, giving the EXACT local shadow ratio det(I+T^T T)^(-1/2). Ivanov’s sharp equality characterization and Grassmannian compactness localize all sufficiently high-volume events to disjoint such charts. The Gaussian/Stiefel block determinant is a product of independent Beta((k-i+1)/2,(n-k)/2) variables in square; moment determinacy on [0,1] supplies equality of laws. The normalized matrix-t graph density, uniform polar expansion, Wick trace-four moment E tr[(W^TW)^2]=(n+1)/(k(n-k)+2), and sphere integration yield the stated gamma constant and correction k(n-k)(k-2)(n-k-2)/(4(k(n-k)+2)). Complementation sends T to -T^T, and Sylvester’s determinant identity proves the EXACT near-endpoint event identity after choosing a common small neighborhood. Independent calculations checked the gamma symmetry, low-dimensional moment identities and linear correction for 55 dimension pairs. Finite tests do not independently prove Ivanov’s global maximizing-set theorem, which is a cited input. ε0 is existential and the asymptotic is not dimension uniform.

## originality

PASS

Best-of-knowledge originality of the actual final claim, with explicit antecedent coverage and residual risk. The new tail law is a consequence of several known ingredients plus a nontrivial local geometric transfer. It is not stated or automatically implied by the maximal-value inequalities alone. The beta determinant distribution is not independently novel.

## value

PASS

A sharp exact Haar endpoint germ and explicit first correction for the natural random shadow of B_1^n in every fixed dimension are nontrivial probabilistic convex geometry. The (k=2 or n-k=2) cancellation and exact complementary-dimension event identity provide interpretable structure. This is not merely a reparameterized beta-moment formula because identifying the shadow event with coordinate-minor determinants uses the locally active convex-hull facets and globally isolated maximizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
