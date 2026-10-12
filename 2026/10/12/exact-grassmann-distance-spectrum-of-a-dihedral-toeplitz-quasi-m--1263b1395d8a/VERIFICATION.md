---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The symbolic proof identifies each row space with \(f\mathbb F_q[x]_{<m}\) inside \(\mathbb F_q[x]_{<n}\). Its critical step is cancellation of \(\gcd(f,g)\) in an exact polynomial intersection equation, followed by degree counting. The pair count is derived separately from unique monic gcd decomposition.

`artifacts/verify.py` reconstructs \(M_f\) directly from coefficients, performs finite-field Gaussian elimination, computes polynomial gcds, and exhausts all ordered projective pairs for \((q,m,n)=(3,2,4),(3,3,5),(5,3,6),(9,2,4)\). The \(q=9\) case uses an explicit model of \(\mathbb F_9\). It verifies full row rank, the intersection formula, subspace distances, every \(N_t\), and \(\sum_tN_t=L(L-1)\). Successful replay ends with `VERIFY_OK`.

The finite replay is supplementary and does not prove arbitrary field size or parameters. Those quantifiers are discharged by the symbolic argument in `RESULT.md`. No Grassmannian optimality is claimed.
