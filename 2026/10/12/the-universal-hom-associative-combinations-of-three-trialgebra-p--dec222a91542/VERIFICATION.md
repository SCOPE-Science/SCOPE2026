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
The packaged checker `artifacts/verify.py` performs exact symbolic verification.

It encodes the source's \(TH_2^7\) table and checks all eleven Hom-associative trialgebra identities on every basis triple.

It then computes the general linear-combination associator and verifies
\[
\mathcal A_*(e_2,e_2,e_1)=\lambda(\mu+\nu)e_1,
\]
\[
\mathcal A_*(e_1,e_2,e_2)=-\mu(\lambda+\nu)e_1,
\]
and
\[
\mathcal A_*(e_1,e_2,e_1)=\nu(\lambda-\mu)e_1.
\]

The all-plus specialization is checked to fail with value
\[
-2e_1,
\]
while the signed specialization \((1,1,-1)\) is checked on every basis triple.

Finally, the checker independently expands the formal universal associator modulo the eleven defining relations and confirms that its only normal-form coefficients are
\[
-\lambda(\mu+\nu),\qquad
\mu(\lambda+\nu),\qquad
\nu(\lambda-\mu).
\]

It returns `VERIFY_OK`.
