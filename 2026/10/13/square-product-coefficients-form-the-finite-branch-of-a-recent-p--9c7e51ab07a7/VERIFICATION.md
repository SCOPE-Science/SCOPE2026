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
The exact reduction was replayed with the standalone verifier. For every integer \(N\) from \(1\) through \(500\), it compares the signed-divisor parametrization of \(w^2-v^2=N\) with exhaustive direct search and obtains equality. It also compares the full square-product classification with direct substitution in 96 small cases and checks the witness \(a=b=1,c=3,n=1,x=5,y=4\).

The proof does not depend on these finite checks: the key steps are the rational-square integrality lemma and the exact factorization \((x^n-z)(x^n+z)=c^{2n}\). The computation is a replay aid and does not certify the nonsquare \(t>1\) branch.
