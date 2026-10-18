---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Leaf-permutation averaging preserves feasible convex sets and objective. A two-parameter Gram matrix has Schur complement eigenvalues 1-b and 1+(n-1)b-na^2; its maximum q is 2n*p(1-p)/(n-1), attained by a regular-simplex leaf residue, yielding R0. All metric triangles reduce to q<=2p and, when n>=3, q<=2/3, giving the exact transition at p=1/n and n=3 cap. A cut mixture is a random flipped-leaf subset with mean size <=n*epsilon and clique weight K(n-K); concave piecewise-linear interpolation and a uniform-size mixture give C sharply. The interpolation defect is alpha(1-alpha). Independently checked 198 rational (n,epsilon) pairs for n=2..12 with PSD Schur complement, triangles, cut chord and gap, including endpoints.

## originality

PASS

The exact positive-tolerance star-margin support values, triangle-strengthened additive gap and fractional-cardinality interpolation do not follow from the inspected spanning-tree integral-correlation theorem or general volume/ratio comparisons; the result is a parameterized slice of the elliptope/metric/cut hierarchy.

## value

PASS

An exact full-parameter gap between elliptope, metric triangle strengthening, and cut-polytope feasible moments on a natural rooted star plus clique is a useful structural benchmark. It identifies the first positive-gap graph size (five vertices) and a sharp universal 1/4 additive defect within this family; neither correctness nor reproducibility alone is used as the value argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
