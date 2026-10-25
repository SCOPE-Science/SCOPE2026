---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For p,q>=3, one exceptional K_pq edge conductance c>=0 with all others 1, the weighted symmetric Laplacian decomposes into four orbit-constant coordinates and zero-sum spaces E_A (eigenvalue q, dim p-2) and E_B (eigenvalue p, dim q-2). PBH injectivity on E_A/E_B necessitates p-2 and q-2 regular leaders. When p!=q and c!=1, quotient determinant at lambda=p,q is respectively p(c-1)(p-q)(q-1), -q(c-1)(p-1)(p-q), so remaining quotient eigenvectors observed by at least one regular leader in each orbit are nonzero. When p=q=n and c!=1, the collision at eigenvalue n gives complete eigenspace dim 2n-3 with endpoint coordinates tied to negative regular-part sums, forcing one additional leader and yielding exact criterion |S|>=2n-3. At c=1, homogeneous zero-sum eigenspaces on the entire bipartitions force all but at most one coordinate in each part. Counting all subsets under these if-and-only-if tests gives the piecewise polynomial z^(N-4)(z+p-1)(z+q-1)(1+z)^2 (unbalanced defect), z^(2n-4)[(z+n-1)^2(1+z)^2-(n-1)^2] (balanced defect), z^(N-2)(z+p)(z+q) (homogeneous). Independently constructed exact rational Laplacians and full Kalman controllability ranks for all 384 leader subsets across four small (p,q,c) cases agreed. Finite ranks corroborate, not replace, the all-parameter spectral-PBH proof.

## originality

PASS

Best-of-knowledge PASS only for the all-placement, three-regime counting polynomial of a single weighted edge defect. Yuan et al. general controllability maximum geometric multiplicity and PBH theorem is prior methodology, not the coordinate input subset distribution. Monshizadeh-Zhang-Camlibel zero forcing refers to controllability for every matrix in a qualitative class and cannot rule out fewer leaders for one specified weighted Laplacian. Klee-Stamps spectra and whole-perfect-matching deletion concern a different perturbation and do not enumerate independently driven actuator placements. Resultary hits on complete-bipartite symmetric edge polytope Laplacians refer to unrelated derived graphs. Unindexed graph-specific classifications are the remaining risk.

## value

PASS

One link defect produces a sharp symmetry-breaking shift in exact leader controllability even without changing graph support when c>0. Minimum independent drivers drop by two for unequal part sizes or one for equal sizes versus c=1 and the zero-forcing sufficiency bound, with the polynomial counting every feasible placement at every size. This is a natural family-wide structural and enumerative result, while appropriately not asserting robust controllability or energy as c approaches 1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
