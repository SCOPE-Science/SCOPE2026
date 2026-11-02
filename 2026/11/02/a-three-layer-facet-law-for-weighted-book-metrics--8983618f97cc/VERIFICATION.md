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
# Verification of the weighted book metric facet law

The formal domain is every integer \(n\ge2\) and real \(0<t\le2\). The dual unit ball inequalities follow from all pairwise metric distances: \(|s|\le t\), \(|x_i|\le1\), and \(|x_i-s|\le1\); leaf-leaf inequalities are redundant. For nonnegative hub value the allowed leaf interval is \([s-1,1]\), and for nonpositive hub value it is \([-1,s+1]\). A fiber-interior coordinate is not extreme. A simultaneous affine perturbation of hub and endpoint leaf coordinates excludes all interior hub levels. At the three remaining hub levels each coordinate is pinned by a facet equality, and the zero layer is pinned by its simultaneous hub-leaf constraints. The resulting vertex count is exact and polarity yields the primal facet count.

Run `python check_theta_facets.py`. The standalone file enumerates all independent tight spanning trees over rational distances and their signs, reconstructs feasible normalized potentials, and checks equality with the classified complete sets for \(n=2,3,4\) and \(t=1/4,1/2,1,3/2,7/4,2\). It returns `EXACT_FINITE_CASES_PASS: 18`. Only the analytical argument proves the infinite parameter claim.

Previously published unweighted \(t=1\) and bipartite \(t=2\) facet counts are explicitly excluded from the claimed novel contribution. Full external mathematical verification was not performed. Residual bibliographic risk: a weighted book metric enumeration might exist under another name.
