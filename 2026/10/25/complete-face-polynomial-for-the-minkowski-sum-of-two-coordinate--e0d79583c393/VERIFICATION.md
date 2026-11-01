---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For nonempty A,B and positive real a,b, exposing aC_A+bC_B by u produces an intrinsic pair of summand faces. The proof separates both-positive disjoint maxima (counted by inclusion-exclusion), shared maximizing indices (one joint signed-support family), one zero maximum (full summand times simplex) and u=0. Each class has derived face dimensions, and summing gives the stated U_p,U_q,U_r generating polynomial and f0=4(pq+pr+qr)+2r. Polar support inequalities yield facets of exclusive P,exclusive S, and shared R classes, 2^p 1_{p>0}+2^q 1_{q>0}+2^n 1_{r>0}; zero-cardinality p/q/r and n=1 are handled. Independently recomputed every valid support triple through n=4 (26 cases) by exposing both signed coordinate summands to all normals from a five-value integer grid, matching total polynomial face count and vertex coefficient. No finite test is treated as an all-n proof; all-n follows from the exhaustive normal-pattern classification. A separate independent affine-rank computation recovered EVERY f-vector coefficient for all 26 valid parameter triples through dimension four; its checker enumerated exposed summand face pairs and exact rational direction ranks.

## originality

PASS

Directly relevant 2026 primary paper Wang et al. counts lattice points for general Minkowski sums of cross-polytopes and explicitly asks in Section 5 Problem 5.4 for their faces and f-vectors. Neither Ehrhart nor general type-B generalized permutohedral machinery, nor the Minkowski-sums-of-simplices flag polynomial, states the overlap-dependent two-summand complete face polynomial. Priority qualified against older normal-fan literature.

## value

PASS

The result fully enumerates all nonempty faces in a natural, structurally important two-support subfamily of an explicit open question on cross-polytope Minkowski sums. It gives a coefficient-independent face lattice, exact facets and all dimensions, not just numerical tests or restatement of standard Minkowski addition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
