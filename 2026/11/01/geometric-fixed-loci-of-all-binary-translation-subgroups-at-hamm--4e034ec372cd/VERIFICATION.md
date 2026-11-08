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

The barycentric orbit-realization lemma identifies fixed geometric points with admissible coset barycenters, with all positive support coefficients orbit-constant. For H of rank k, coordinate functional double counting yields s 2^(k-1)=sum_h wt(h)<=2(2^k-1), so s<=3; k=3 forces the full 3-cube and a weight-three codeword, contradiction, ruling out all k>=3. Rank-two distinct cosets would span a forbidden rank-three space if compatible, hence the orbit complex is discrete of the stated size. Rank-one weight-one cosets give the (n-1)-cube; weight-two cosets indexed by (p,y) give opposite parity adjacency at d(y,z)<=1 and the parity relabeling (p,y)->(p+sum y,y) gives exactly Q_(n-1), with no triangles/higher faces. Independent enumeration generated all binary subspaces for n=3..5 and verified each eligible orbit graph against the cube or isolated points (rank-one cases 6,10,15; rank-two cases 4,10,20). This corroborates but is not the infinite proof. Boundaries n=3 and empty fixed complexes addressed.

## originality

PASS

Best-of-knowledge PL fixed-locus claim is not the same invariant as ambient homotopy or an equivariant homology representation. Uniform subgroup-rank/weight classification with actual PL types is not deduced from the checked sources. Full paper arXiv:2606.20784 remains inaccessible; there is an explicit possible implicit-coverage priority risk, not automatic rejection.

## value

PASS

For the natural full lattice of pure translation symmetries of binary cubes, one uniform theorem determines *actual* geometric fixed spaces rather than homology traces, with a sharp code-weight/rank phase boundary and exponentially large cube-graph cycle rank. A researcher studying equivariant Rips geometry needs these exact subspace types; it is not a cosmetic change to the ambient homotopy theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
