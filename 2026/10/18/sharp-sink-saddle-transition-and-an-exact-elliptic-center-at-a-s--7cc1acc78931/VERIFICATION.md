---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Let P swap x and z and let F=P∘T be extended affinely from Q₄. The branch return is F², since the Q₂ branch is the swap-conjugate of the Q₄ branch. Direct determinant expansion gives the linear part K of F the polynomial r³+a²r−2ab; det(I−K²)=(1+a²−2ab)(1+a²+2ab)>0 for 0<b<1. The fixed point of F is therefore the only possible fixed point of the formal return, even if it falls outside the itinerary. Its sum and difference coordinates satisfy y=b(x+z), x−z=(2b−a)(x+z), x+z=a(x−z)+2, giving exactly the stated points and strict condition a<2b−1. For a≠0 the real root s has the sign of a and 0<|s|<1. Polynomial division gives the remaining roots −s/2±i sqrt(a²+3s²/4), whose squares are the nonreal return pair and have modulus a²+s². For a²<1 compare the increasing function t³+a²t at t=|s| and at t=sqrt(1−a²), where it equals t; this gives the claimed crossing at a²(1+4b²)=1. If a²≥1 the pair is expanding; at a=0 the return linear part is nilpotent and the existing cycle is a sink. At equality, s=2ab≠0 and K restricted to the center plane in basis (v,Kv) acts by (ξ,η)↦(−η,ξ−sη). Substitution preserves H=ξ²−sξη+η², which is positive definite since |s|<1. The invariant ellipses are exact for the affine return, not an approximation. The two strict quadrant visits hold on a neighborhood of U; small invariant neighborhoods for the return are obtained from sublevels of H plus a squared stable coordinate, which contracts by s². The first iterate stays near V on its affine branch and maps the center ellipses to nondegenerate companion ellipses because det K=2ab≠0 there. This gives Lyapunov stability and excludes attraction. Above the boundary the expanding real subspace is two-dimensional, with one transverse stable dimension.

## originality

PASS

The map, symmetry, cycle equations and example positions are prior work, and specializing the formal orbit coordinates is routine. The supported distinction is the sharp local Floquet trichotomy for the strict symmetric cycle and the resulting exact invariant ellipses with local stability at neutral parameters.

## value

PASS

The stability of a previously identified cycle is a natural dynamical invariant. The exact parameter criterion distinguishes a two-dimensional unstable saddle from a sink, and resolves the neutral case with actual invariant ellipses rather than treating unit multipliers as inconclusive. This supplies a local dynamical statement beyond recomputing the orbit or fitting numerical bifurcation examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
