---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At a concentric radius interval [a,b], Gaussian Fock monomials diagonalize T and lambda_j=1/j! integral_a^b t^j exp(-t) dt. The recurrence lambda_j-lambda_{j-1}=(a^j exp(-a)-b^j exp(-b))/j! changes sign exactly at j=k because b^k exp(-b)=a^k exp(-a). Hence only k-1,k share the strictly maximal eigenvalue; a nonzero gap separates them. The trace-class coherent-state integral is smooth under these small two-center domain perturbations, allowing a Riesz/spectral-projection reduction. Radial variation contributes diag(alpha*tau,0); an independent outer-boundary shape derivative contributes off-diagonal gamma*delta and its conjugate. The two eigenvalues of that Hermitian 2x2 matrix give exactly the displayed square root; the spectral gap controls the remaining terms to quadratic order. The outer radius shift keeps area pi*w exactly; Weyl covariance makes common translation irrelevant. Independent polar quadrature checks k=1,2,3 verify the double top eigenvalue, gamma boundary derivative, and second-order error scaling. No global optimization or uniform-in-k remainder is established.

## originality

PASS

Qualified best-of-knowledge original contribution: A conical eigenvalue crossing for eccentric Gaussian localization annuli. Closest prior work and limits are compared by implication, not title; priority risk retained.

## value

PASS

Gaussian time-frequency localization annuli and Hermite-level ties are canonical, and the optimal captured-energy norm is the natural quantity. The result identifies a precise nonsmooth conical instability under physically meaningful relative center displacement while fixing area, with explicit coefficients for every tie and an independent rigid-motion invariance. Neither the radial spectrum nor general disk optimality quantifies this structural instability; the local law is a motivated sharp mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
