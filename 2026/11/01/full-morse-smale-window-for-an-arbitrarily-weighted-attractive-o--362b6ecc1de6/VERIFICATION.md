---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The quotient gradient is −M∇V with M=[[2,1],[1,2]], by orthogonal reduction of the full zero-rotation gradient. The weighted Laplacian has nonzero eigenvalues 3 and 1+2w on the equal-side and antisymmetric directions, and bounds the full Hessian in both signs. Descent is strict for h<2/Λ even for a candidate wrapped fixed point (the potential is periodic), so fixed points are exactly the critical classes. Adding the two stationary equations gives y=−x or y=x+π; the first branch yields sin x(1+2w cos x)=0, and the second yields sin x=0. The binary mixed saddles have Hessian determinant −1; the antipodal class has eigenvalues −1, 2w−1; the extra pair has eigenvalues −1/(2w), (1−4w²)/(2w); the weighted Hessian has the same inertia. The full lift for h<1/Λ has uniformly positive definite Jacobian, is strongly monotone and proper, and descends equivariantly to a diffeomorphism. At equality its synchronous Jacobian is singular; for every larger h, the largest symmetric weighted Hessian eigenvalue varies continuously from Λ at synchrony to a negative value at a source, hence crosses 1/h. Summable descent forces gradients and step sizes to zero; a finite critical set and vanishing steps imply convergence to one class. A neighborhood of any noncritical point is wandering by a uniform first-step potential drop. The forward/backward invariant diagonal and antidiagonal contain respectively the unstable and stable curves of (π,π) when it is a saddle; neither mixed saddle lies on either. The two mixed saddles have the same potential, excluding connections by strict descent, which also excludes homoclinics. All other intersections are transverse (own stable/unstable eigenlines here are complementary; source and sink have the relevant full-dimensional manifolds). In the long-step interval, a nonsynchronous stable multiplier may be zero, so local invertibility there need not be assumed. In a small convex eigen-coordinate chart at each saddle or source, differences in the unstable cone |Δu|≥|Δs| stay in that cone and expand: the linear unstable minimum exceeds 1, the stable maximum is less than 1, and the derivative perturbation can be chosen smaller than both gaps. Thus the local forever-staying set projects injectively, with Lipschitz graph bounds, onto the lower-dimensional stable space and is null. The Jacobian determinant is analytic and nonzero at any source, so its zero set is null; elsewhere local smooth inverses preserve the null-preimage property, which iterates. This yields Haar-a.e. synchrony. Its exact strict Schur threshold follows from the two real multipliers; maximality of a.e. convergence is not asserted.

## originality

PASS

The global attractive Euler-map Morse–Smale/no-connection theorem over all stated positive closing-edge weights and the precise step-window classification are supported as distinct. The continuous equilibrium census, Lyapunov descent, weak-link Morse–Smale precedent and large-step strict-saddle avoidance machinery are not independent novelty claims.

## value

PASS

The complete weighted triangle is the first cycle where extra coupling changes equilibrium types and invariant geometry. The exact global Morse–Smale window with a clean invariant-circle obstruction, and synchronization beyond that window, distinguish genuinely different dynamical properties. The result is not just a weighted-Laplacian calculation or a continuous equilibrium census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
