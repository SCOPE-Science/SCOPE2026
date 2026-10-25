---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The Minkowski sum of connected induced coordinate simplices has normal fan indexed by recursive maximum-coordinate search trees, and in a biclique these are an ordered elimination handle ending in r unordered same-color leaves. Among n! strict Gaussian coordinate permutations, each labeled broom has precisely r! orderings of its terminal leaves; hence mass r!/n!. Counting the last exhausted-color vertex and unordered remaining leaves yields N_{p,q}(r)=(n−r−1)![p C(q,r)1_{r≤q}+q C(p,r)1_{r≤p}], including r1. Independently enumerated all connected tubes, all n! coordinate orders, and directly computed Minkowski-maximizing vertex vectors and grouping by brooms for p,q=(1,1),(1,2),(2,2),(2,3),(2,4),(3,3),(3,4), with exact rational masses. For (3,4) obtained exactly 3702 vertices and C=11/22050, matching equations (1),(2). For m=m derive N_m(r)=2m*C(m,r)*(2m−r−1)!, fixed-r Gaussian leaf mass→2^-r and vertex count/(2m)!→e^{1/2}−1 by dominated convergence. Write collision C as 2(m!)³/((2m)!)² Σ_{k=0}^{m−1} a_m(k), a_m(k)=(m+k−1)!(m−k)!/((m−1)!m!k!), ratio=(m+k)/((m−k)(k+1)); for k≤m/2 bound a_m(k)≤3^k/k!, later terms nonincreasing up to k=m−2 and total tail ≤m·3^floor(m/2)/floor(m/2)!→0. Hence sum→e and conditioned deficit→Pois(1), analytically—not inferred from finite census. At p=q=1 and n2 degenerate brooms still correct.

## originality

PASS

Established graph-associahedron theory already provides the connected-tube simplex sum, nested fan, search-tree bijection and biclique broom shapes. Related K4,4 graph-associahedron eccentricity data count brooms but study flip distance rather than isotropic Gaussian normal cones. The all-(p,q) exact solid-angle masses and three balanced sampling/collision limits are not implied by that distance table or cited diameter estimates as stated. Best-of-knowledge O PASS, with explicit equivalence risk to known random search-tree/linear-extension theory.

## value

PASS

Different sampling measures of the same natural polytopal vertex set lead to genuinely different limiting laws—geometric typical Gaussian, conditioned Poisson under vertex-uniform, and opposite-end Poisson under rare collisions. The exact normal-cone collision localizes exponentially atypical configurations and is a meaningful asymptotic invariant of standard biclique graph associahedra, not an arbitrary numerical slice or generic shape classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
