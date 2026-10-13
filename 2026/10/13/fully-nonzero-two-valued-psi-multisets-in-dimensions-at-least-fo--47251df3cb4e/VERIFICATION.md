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

For \(n\ge5\), after choosing the minority multiplicity \(m\le\lfloor n^2/2\rfloor\), the inequality
\[
m-3\le n(n-3)
\]
follows from
\[
n(n-3)+3-\frac{n^2}{2}=\frac{(n-3)^2-3}{2}>0.
\]
Thus every extra deviation after the three-cycle can be placed in columns \(4,\ldots,n\), where it annihilates \(v=(1,\omega,\omega^2,0,\ldots,0)^{\mathsf T}\). Exact multiplication gives \(J_nv=0\) and \(C_0v=\omega v\), so the arranged matrix has nonreal eigenvalue \((s-r)\omega\).

For \(n=4\), the same construction covers minority multiplicities \(3\) through \(7\). At multiplicity \(8\), the displayed zero-one matrix has exactly eight ones and sends \((0,\omega^2,\omega,1)^{\mathsf T}\) to \(\omega^2(0,\omega^2,\omega,1)^{\mathsf T}\), while the coordinate sum is zero. Hence the corresponding entry arrangement has nonreal eigenvalue \((s-r)\omega^2\).

The source theorem for one exceptional entry and source obstruction for two equal exceptional entries were checked directly in arXiv:2609.36524v1. `check_binary_psi.py` independently verifies the two cube-root eigenvector identities and finite-range instances of the packing inequality, ending with `CHECK_OK`.

The checker is a consistency test only. The proof above is symbolic and uniform in \(n\) and in the two distinct nonzero integer values.
