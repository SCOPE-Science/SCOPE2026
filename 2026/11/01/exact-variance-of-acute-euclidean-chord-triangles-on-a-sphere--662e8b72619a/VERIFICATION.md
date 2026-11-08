---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Read RESULT.md and standard-library verifier. With fixed unit A,B at central angle theta, the acute-angle inequalities are |u·C|<sin(theta/2) and v·C<cos(theta/2) for orthonormal midpoint/chord coordinates. Since the excluded cap is contained in the belt, conditional probability q(theta)=sin(theta/2)-(1-cos(theta/2))/2. Uniform A·B on [-1,1] yields E q=1/2 and E q²=(pi-1)/8. Different third points are conditionally independent given shared endpoints, hence covariance (pi-3)/8 for shared pairs. For one shared point, rotation invariance makes conditional mean exactly 1/2; otherwise independent. Unordered overlap-two pairs count C(n,2)C(n-2,2), so Var=C(n,3)/4 +(pi-3)C(n,2)C(n-2,2)/4, with n=4 variance (3pi-7)/2. Independently numerically integrated conditional q and q² obtaining 0.5000000000 and 0.2676990816 vs (pi-1)/8=0.2676990817; geometric and combinatorial proofs establish all n.

## originality

PASS

Akopyan et al. establish the one-triangle marginal 1/2; the inspected tetrahedral all-four-acute question addresses a four-way intersection. Neither determines the two-triple shared-edge joint probability or the full U-statistic variance coefficient.

## value

PASS

The count of acute Euclidean triangles among random points is a natural geometric U-statistic, and exact variance identifies the positive shared-edge dependence generating n^4 rather than naive independent n^3 fluctuations. The explicit pi coefficient resolves a nontrivial second moment not implied by the known one-triangle probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
