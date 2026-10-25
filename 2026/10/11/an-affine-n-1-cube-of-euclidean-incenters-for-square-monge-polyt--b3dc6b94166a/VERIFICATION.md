---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The claim is correct for all integers n>=2 with the intrinsic metric on sum(C)=1. Projected coordinate normals have Frobenius length alpha=sqrt(1−n^−2), and adjacent Monge normals length 2. The ball inequalities reduce to a nonnegative D=(C−alpha*r*1)/(2r) with each adjacent Monge slack >=1. The quadratic D0_ij=(j−i)(j−i−1)/2 has unit slacks and mass T=n²(n²−1)/12. E=D−D0 is Monge; identity minimizes its permutation assignment cost. Averaging all assignments yields sum(E)/n>=sum(diag E)=sum(diag D)>=0. If sum(D)=T, every diagonal entry vanishes and every assignment ties; swapping arbitrary row-pair columns forces every two-by-two mixed difference of E to vanish. Thus E_ij=u_i−u_j, and D>=0 is equivalent to each adjacent delta_i=u_i−u_(i+1) lying in [0,1]. Conversely these bounds guarantee all entries nonnegative, unit slacks and mass T. Therefore rho=1/(n²*alpha+2*T), and all optimal centers are exactly C_ij=rho*(alpha+(j−i)(j−i−1)+2(u_i−u_j)). Independent deltas parametrize an (n−1)-cube, and the zero diagonal and adjacent pairs give exactly (n−1)²+n+number_of_endpoint_deltas tangent facets.

## originality

PASS

Best-of-knowledge PASS: the exact Monge-polytope facet/volume literature and the accessible 2026 same-family primary text do not give the claimed Euclidean inradius, universal equality rigidity or full center cube. The proof adds the nontrivial all-n minimum-mass Monge assignment equality classification. Three published-results semantic queries found only the assigned record as exact self-match; other inball sources use distinct polytope families. The 2026 same-family full paper was not fully accessible; no whole-document noncoverage is asserted, and possible unindexed or stronger coverage remains residual.

## value

PASS

The sum-one nonsymmetric Monge polytope is a natural family of transportation-cost polyhedra. Its intrinsic Euclidean inradius is an exact perturbation-robustness margin; the full affine (n−1)-cube of optimal centers and the contact counts distinguish flat optimal faces from generic unique incenter geometry. Those natural all-size structural invariants and the sharp n^−4 scale are mathematically motivated and not a table recomputation or substitution into known facet counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
