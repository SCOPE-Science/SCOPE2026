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
# Verification

The proof is symbolic and applies to every integer \(n\ge3\). The accompanying `verify.py` is a finite consistency checker, not a substitute for that proof.

The checker uses only the Python standard library. For each \(3\le n\le8\), it builds the adjacency action directly from the condition that distinct \((i,j)\) and \((k,\ell)\) are adjacent exactly when \(j\ne k\) and \(\ell\ne i\). With exact rational arithmetic it verifies:

- the \(I,J\) block identities;
- the \(D_u,P_u,Q_u\) identities for a basis of \(\mathbf 1^\perp\);
- an explicit basis of the skew row-sum-zero space has dimension \((n-1)(n-2)/2\) and eigenvalue \(-2\);
- an exact nullspace basis of symmetric zero-diagonal row-sum-zero matrices has dimension \(n(n-3)/2\) and eigenvalue \(0\);
- all listed vectors together have exact rank \(n^2\).

A successful replay prints one summary line for each tested value and ends with `VERIFY_OK`.

Unproved limits: the checker does not enumerate all \(n\), and it does not establish literature originality. Those tasks are handled respectively by the symbolic proof and the documented source comparison.
