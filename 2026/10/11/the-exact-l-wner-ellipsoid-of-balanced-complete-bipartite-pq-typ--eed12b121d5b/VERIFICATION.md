---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The PQ vertices are (e_i,e_j) with i=j or an oriented cross-edge, all lying in affine coordinate-sum one. Assign diagonal contact weights t/n and each oriented cross-edge (1-t)/(nm); they are positive and sum to one. The centered covariance blocks are H/n and [tH+(1-t)(A/m-J/n)]/n. Diagonalizing via the K_{m,m} sign line and its orthogonal complement in U=(x+y-2c)/sqrt2,V=(x-y)/sqrt2 yields positive eigenvalues 2t/n,(1+t)/n,2(1-t)/n,(1-t)/n with sign-line multiplicities one. The two vertex-orbit quadratic norms are q_diag=(1/t+2(n-2)/(1+t))/n and q_edge=((n-2)/(1+t)+(n-1)/(1-t))/n. Independently factored q_diag-q_edge=(2(n-1)t^2+t-1)/[n*t*(t^2-1)], hence unique positive root 1-t-2(n-1)t^2=0, exactly the asserted t. Weighted trace gives every norm d=2(n-1), and positive definite covariance gives no nonvertex boundary contacts. Averaging any enclosing ellipsoid over this positive isotropic contact distribution and AGM forces det S>=d^d det C with equality only at the proposed center and S=dC, proving uniqueness without symmetric competitor hypothesis. Multiplying spectral eigenvalues gives volume. The inspected SymPy checker reconstructs exact m=2,3,4,5 covariance and contacts; those samples do not substitute for the all-m proof.

## originality

PASS

Best-of-knowledge originality: targeted Resultary comparisons, exact primary theorem/parameter inspection and implication tests do not reveal prior coverage of the specifically identified surviving result. A self-indexed copy of the assigned finding is not prior coverage; risks are documented.

## value

PASS

This determines a full four-eigenspace minimum-volume ellipsoid, every contact point, an explicit algebraic orbit-weight parameter and an exact Euclidean volume for a standard combinatorial PQ adjacency polytope across all balanced K_{m,m}. The geometric metric is not captured by prior Ehrhart/lattice volume computations, so the exact result is independently meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
