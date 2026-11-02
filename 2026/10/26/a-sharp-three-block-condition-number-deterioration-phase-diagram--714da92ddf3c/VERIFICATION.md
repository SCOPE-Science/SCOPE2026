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

SPD A=I+vv^T, exact block-Jacobi P=blockdiag(I+v_j v_j^T); S=P^-1/2 A P^-1/2. Active block spike directions reduce S to H with H_ii=1 and H_ij=sqrt(q_i q_j/[(1+q_i)(1+q_j)]); all perpendicular eigenvalues are 1, so extreme eigenvalues come from H for positive active blocks. Two blocks have eigenvalues 1±sqrt(xy/[(1+x)(1+y)]) and κ(S)<=1+x+y, equality x=y. In (s,s,t) three-active-block family the antisymmetric eigenvalue is 1/(1+s), other eigenvalues (2+3s±sqrt(Delta))/(2(1+s)), Delta=s²+8st(1+s)/(1+t). Delta−9s²=8s(t−s)/(1+t) selects min eigenvalue. Symbolic exact factorizations of Delta−(s+2t)² and Delta(K+1)²−(2+3s)²(K−1)² prove deterioration iff t<s or s<t<s(4s+3)/(s+1), with equality at t=s and second threshold. Independent exact symbolic positive-sum certificate proves ratio strictly below 3/2 and asymptotic s=L²,t=L approaches 3/2. Direct generalized eigenproblem confirms witness κ=7+2sqrt6>10. No claim beyond (s,s,t) for the 3/2 constant or all SPD matrices.

## originality

PASS

Qualified original addition is exact deterioration versus improvement regions in the rank-one (s,s,t) block-Jacobi model and sharp 3/2 sup, not the known block 2×2 eigenvalue pairing or generic condition-number scaling theory.

## value

PASS

An exact SPD preconditioner can strictly worsen the spectral condition number, with the first possible failure already at three active blocks. The complete deterioration/equality/improvement phase diagram and sharp 3/2 ceiling are natural diagnostic invariants for selecting a baseline preconditioner; they offer more actionable structure than a single counterexample or generic near-optimality bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
