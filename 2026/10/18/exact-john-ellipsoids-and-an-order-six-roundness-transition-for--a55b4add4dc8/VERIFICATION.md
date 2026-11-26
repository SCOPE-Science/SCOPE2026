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

In the intrinsic edge-sum hyperplane the incidence identity BBᵀ=(n−2)I+11ᵀ gives the two stated orthogonal components. Coordinate normals have projected energies 2/n and (n−3)/(n−1), and subset normals have U-energy ||Bv−mean(Bv)1||²/(n−2); subtracting from ||v−mean(v)1||² gives the W-energy. Subset slacks are (s−1)(n−s)/n. For the round candidate the squared distances to these hyperplanes are minimized at s=2 or n−1 because their logarithmic derivative strictly decreases; the co-singleton endpoint is the smaller of the two. Its distance exceeds the coordinate radius exactly for integers n≥6 in scope. For n=4,5 the co-singleton cap binds together with the coordinate bound; substituting gives precisely the listed tangencies. The coordinate and subset inequalities in the stated contact list are genuine facets: the coordinate face is the base polytope for K_n with an edge deleted, which has connected cycle matroid for n≥4; a tight subset face factors into base polytopes of the restriction to K_s and the contraction, which has s parallel spokes for each remaining vertex plus its edges to the other remaining vertices. Both factors are matroid-connected (including the one-element restriction), so their dimensions add to m−2. Centered coordinate normals have zero sum and frame operator I; co-singleton normals are the negatives of centered incidence rows, with zero sum and frame operator (n−2)Π_U. After the shape transform and slack normalization, the listed weights give moments 0 and I, including the n=4 certificate using a subset of all contacts; this proves global, not merely symmetric, optimality. Volume follows from the multiplicities, and the n=3 regular triangle has squared inradius 1/6. An independently written rational check (`python3 -B /workspace/branches/bounded_review_checks.py 3`) evaluated actual labeled subset inequalities and matrix moments for n=4 through 10. Neither that finite check nor the supplied, inspected but unexecuted verifier is the all-order proof.

## originality

PASS

Best of inspected evidence for the explicit complete-graph classification including both exceptional anisotropic spectra and the full contact data. The identified results concern facets, reconstruction, a universal optimality criterion, and the ellipsoid of a different body. A sharp inball theorem may help yield the round range via comparison with the containing coordinate simplex, but an inball alone does not determine the anisotropic spectra or their certificate. No specific prior statement covering the full classification was identified.

## value

PASS

The precise intrinsic John geometry of a canonical graphic matroid body is useful beyond a radius calculation. A sharp change occurs at order six, and the full-dimensional certificate explains why exponentially many other facet inequalities do not control the round optimum. For the exceptional orders it certifies unequal principal directions and their exact scales, information an inball cannot provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
