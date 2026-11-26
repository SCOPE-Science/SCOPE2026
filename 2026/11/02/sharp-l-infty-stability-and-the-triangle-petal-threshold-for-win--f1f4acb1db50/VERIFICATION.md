---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integrating the two unit-edge hats gives the stated nodal Gram matrix. Eliminating the petal blocks gives the positive hub Schur complement and all five inverse entries with the indicated signs. The L-infinity evaluation norm is the kernel's L1 norm, attained by its sign, and independent edge counting gives the six-term outer formula. Interior evaluation is strictly below the maximum: adjacent endpoint kernels have opposite signs on an interval next to one endpoint (positive diagonal and negative adjacent inverse entry), so the integrated triangle inequality is strict for a proper convex combination. I symbolically verified both shifted polynomial certificates, their positivity, the triangle formula and derivative, and the strict inequalities at k=8 and 9. The k=1 row equality follows by complete-graph symmetry. In the s>=3 certificate some terms vanish at k=1, but the constant term stays positive. The limit 458/225 is the nonattained supremum of this family only.

## originality

PASS

The supported distinction is the all-parameter windmill norm and its norming vertices, strict triangle-petal cutoff at nine, and family supremum. The general metric-graph mass-matrix/kernel identity and the possibility of amplification above two without leaves are not credited as new. The general identity computes each instance, but by itself does not perform the symbolic block reduction and certify the hub/outer comparison and threshold uniformly in both parameters. The nearest exact family results have different topologies.

## value

PASS

The knot-free unit-edge windmill is a natural leafless test of whether vertex branching and connections within a petal cause amplification above two. The exact answer isolates the triangular case and the first bouquet size that crosses two, with extremizing vertex locations and a limit across petal counts. These are useful quantitative benchmarks beyond exhibiting another graph above two or numerically recomputing a known instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
