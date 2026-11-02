---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For all n>=3 and strictly positive weights, every isometric embedding of the full 2^n weighted Hamming cube in the complex rectangular Schatten-1 class is classified. Equality in the top-to-bottom trace-norm triangle forces each vertex to lie in the positive cone U H_epsilon for the SAME polar partial isometry U, 0<=H_epsilon<=|A|. Singleton P_i=H_{e_i} have trace w_i and ||P_i-P_j||_1=w_i+w_j; the sign-duality equality condition forces mutually orthogonal supports. For each vertex epsilon and each active i, ||H_epsilon-P_i||_1=Tr(H_epsilon-P_i) yields H_epsilon>=P_i. Saturation of total trace over the mutually orthogonal supports leaves no off-support or off-diagonal mass; hence H_epsilon=sum_{i active}P_i. These disjoint positive blocks yield complex-linear extension L(z)=U sum z_i P_i with trace norm sum w_i|z_i|. Nonzero disjoint supports force rank(top-bottom)>=n and min(p,q)>=n, realized by diagonal constructions; at p=q=n all blocks rank one, giving the two-unitary normal form. Inspected `checker.py` generates higher-rank complex rectangular witnesses and exact diagonal metrics. Its 104261 reported diagnostics are not used to prove the universal rigidity.

## originality

PASS

Best-of-knowledge PASS after comparison of theorem statements, hypotheses, reductions and implications. The inspected sources do not establish the complete final claim for this record; known components are acknowledged. Metric-to-complex-linear rigidity of weighted cubes in finite trace-class matrix spaces retains explicit residual priority risks. An inaccessible plausible source alone is not treated as failure or as a whole-document NOT_COVERING finding.

## value

PASS

This is an exact classification of every nonlinear isometric realization of a natural finite weighted ℓ1 cube inside the noncommutative trace norm, forcing a complex-linear extension and characterizing all equality configurations. Its all-weight and rectangular scope gives substantive information beyond the known unweighted dimension obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
