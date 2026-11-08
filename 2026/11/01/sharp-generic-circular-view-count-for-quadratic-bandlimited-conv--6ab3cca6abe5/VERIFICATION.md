---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Disk projections require vanishing of the two tracefree compression coordinates of Q on each plane. The diagonalize-A separation lemma is sound: dependence with a nontrivial eigenvector e forces e to be a B-eigenvector; variation within a repeated eigenspace forces B scalar on that eigenspace; three noncollinear (a_i,b_i) then yield a plane with two independent measurements, contradiction. Inductively reduce the tracefree symmetric kernel by two dimensions until zero; the nonzero analytic rank minor gives open dense full-measure tuples on connected Gr(2,n)^m. For fewer planes, dimension counting gives nonzero Q in the kernel, and 1+epsilon u^T Q u has positive spherical curvature for small epsilon, hence smooth nonball counterexamples. Independently derived measurement constraints and modular full-rank instances n=3,4,5,6,7 with D=5,9,14,20,27 and m=3,5,7,10,14. Finite ranks corroborate, not prove all n.

## originality

PASS

The exact finite minimal measurement count for quadratic-support convex bodies does not follow from all-plane rotational symmetry rigidity or averaged projection operators; separation and rank induction are distinct mathematical conclusions. Best-of-knowledge originality only.

## value

PASS

The sharp number and generic rank classification of circular shadows is a natural, motivated finite tomography invariant in every dimension. It establishes both attainable reconstruction and a universal obstruction below threshold, beyond a computational table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
