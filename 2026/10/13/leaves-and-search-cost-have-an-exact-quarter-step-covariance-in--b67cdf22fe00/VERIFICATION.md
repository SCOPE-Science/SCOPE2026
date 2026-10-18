---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For independent uniform-parent growth, L_{n+1}=L_n+1-J_n and P_{n+1}=P_n+D_n+1. Conditioning gives E(D|T_n)=P_n/n, E(J|T_n)=L_n/n, E(JD|T_n)=Q_n/n; mixed old-tree contributions cancel, so c_{n+1}=c_n-q_n/n+ell_n p_n/n². The leaf-depth update Q_{n+1}=Q_n+(1-J)D+1 yields q_{n+1}=(1−1/n)q_n+H_n and q_n=n H_{n-1}/2−(n−2)/4. With ell_n=n/2 and p_n=nH_{n-1}−(n−1), covariance decrement is exactly −1/4, from c_2=0. Classical Var(L_n)=n/12 for n>=3 gives the regression slope and asymptotic Var(P_n) coefficient gives n^-1/2 correlation. Fresh exhaustive rational enumeration of all (n−1)! recursive trees for every n=2..10, total 409113, verified covariance, q_n and marginal moments.

## originality

PASS

The closest primary literature and published-result searches were compared for statement implication and actual mathematical object, not just titles. Marginal expectations and variances for leaves and P_n do not determine Cov(L_n,P_n). Lundblad–Wagner’s comparison of total and external path lengths also does not imply this mixed moment without an extra identity linking count and leaf depths, which the submitted growth recurrence supplies. Looked for terminal vertices/leaves against internal path length/search cost, and for mixed moments/recursive-tree covariance. The source “external path length” is Q_n, the sum of leaf depths, mathematically different from L_n. Residual risks are retained; inaccessible full text alone is not equated to scientific failure.

## value

PASS

Determines an exact mixed second moment between leaf count and total search cost in a canonical random tree, together with a constant-per-step covariance mechanism, regression coefficient and asymptotic decorrelation. The relationship cannot be recovered from the known marginal laws alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
