---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. At equilibrium on an N-cycle, Kirchhoff balance forces identical sine currents J on every edge. A positive definite reduced Jacobian cannot have two nonpositive edges, and a single negative ordinary-unit edge is excluded by comparing its magnitude c with the (m−1)/c positive path resistance; consequently all m ordinary increments are the same acute α. The weak w<=wc=sin(3π/(2m)) bound excludes winding |q|>=2 and excludes an acute weak increment in the open range. For q=1, β∈(π/2,π), α=(2π−β)/m, w=f_m(β)=sinα/sinβ. Positive definiteness of reduced cycle Hessian is exactly cosα+m w cosβ>0, equivalent to f_m′(β)<0. The second derivative of log f_m is strictly positive on (π/2,π), its derivative changes sign exactly once, so there is one fold w_m< w_c; synchrony is the only stable equilibrium for w<=w_m and two reflected stable winding states join for w_m<w<=w_c. At equality wc the ordinary positive edges alone span a path, hence stability persists; the fold has an additional zero mode. The asymptotic tan t*=π+t*, m w_m=sec t*+O(m^-2) follows uniformly at its interior nondegenerate optimum. Independently reconstructed one-weak-link Hessians across N=5..30 corroborate. No unrestricted w>wc classification is claimed.

## originality

PASS

PASS best-of-knowledge for the identical-frequency one-weak-bond complete strictly stable equilibrium count, sharp fold and limiting threshold, not the known existence of one-obtuse-edge stable states or the signed-Laplacian/effective-resistance test. Bronski–DeVille–Ferguson 2015 full accessible primary paper develops signed-cycle stability and a different nonuniform-frequency long-link setting; Delabays–Coletta–Jacquod 2015 studies winding on a single cycle, with homogeneous capacities and nonhomogeneous injections. Their inspected exact statements do not directly imply the present special complete classification and parameter w_m. Mathematical reduction to a more general result not located remains a risk.

## value

PASS

PASS. A natural one-defect oscillator ring has a nontrivial exact saddle-node threshold and a complete count of strictly stable states over its entire weak-bond range, with an unexpected finite-size scaling constant. These are meaningful stability/bifurcation invariants not supplied by generic effective-resistance machinery alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
