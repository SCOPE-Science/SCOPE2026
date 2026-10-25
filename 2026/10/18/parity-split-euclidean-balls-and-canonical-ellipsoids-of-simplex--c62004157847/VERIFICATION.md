---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Reconstructed the oriented top-boundary Gram matrix B^T B=mI-ss^T, rank m-1 and unique relation sum s_i v_i=0. Even m=2k yields the orthogonal free sum of two centered regular (k-1)-simplices, dimension m-2; facets indexed by A x B, each normal has squared norm (m-2)/(2m), giving unique inradius sqrt(2m/(m-2)) and circumradius sqrt(m(m-2)). Symmetry and irreducibility yield spherical John and Loewner shapes. Odd m=2k+1: s-sum epsilon is nonzero, so simplex dimension m-1; barycentric normal g_i=(e_i-epsilon*s_i*1)/m has lengths sqrt(m-1)/m (majority) and sqrt(m+3)/m (minority). Summed facet inequalities give unique inradius 2m/[(m+1)sqrt(m-1)+(m-1)sqrt(m+3)]. Averaging the majority vertices proves the unique enclosing sphere radius m*sqrt((m-1)/(m+1)), with strict minority squared clearance 4m/(m+1). Restricted linear map L on 1-perp has singular values 1 and m (multiplicities 1,m-2), giving displayed anisotropic John/Loewner semiaxes and common center c_J. Independently reconstructed L, affine ranks, SVD singular axes, odd screen clearance, and even circumradius numerically m=3..15 in local standalone check; not an infinite proof. Source tree, RESULT.md, METADATA.json, AUDIT.json inspected by exact Git blobs.

## originality

PASS

Best-of-knowledge, statement-and-implication comparison: inspected same-object primary results and relevant published records; literature access limits documented. Claim is a metric refinement, not a renaming of the published parity combinatorial classification; background linear map is explicitly credited.

## value

PASS

Natural top-dimensional Laplacian polytope of the simplex boundary has a parity-dependent affine dimension and contact geometry. Complete Euclidean extremal ball and canonical ellipsoid data in the unaltered ambient metric give useful sharp baseline invariants invisible under combinatorial/unimodular equivalence. Particularly odd minority vertex screening and distinct insphere/circumsphere/John centers are nonroutine geometric facts, beyond mere finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
