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
The structural proof is exact and symbolic.

For necessity, if \(X=ARB\) and \(AB=0\), then \(\operatorname{im}(B)\subseteq\ker(A)\). Rank-nullity over a division ring gives \(\operatorname{rank}(A)+\operatorname{rank}(B)\le n\), while \(\operatorname{rank}(ARB)\le\min\{\operatorname{rank}(A),\operatorname{rank}(B)\}\). Hence \(\operatorname{rank}(X)\le\lfloor n/2\rfloor\).

For sufficiency, after row and column reduction a rank-\(r\) matrix is \(U J_r V\). With \(2r\le n\), the matrices
\[
A_r=\sum_{i=1}^rE_{i,r+i},\qquad
R_r=\sum_{i=1}^rE_{r+i,i},\qquad
B_r=J_r
\]
satisfy \(A_rB_r=0\) and \(A_rR_rB_r=J_r\). Thus \(U J_rV=(UA_r)R_r(B_rV)\) with \((UA_r)(B_rV)=0\).

The finite-field enumeration is not used to prove the structural theorem. It is obtained afterward by summing the standard rank-\(r\) matrix count over the proved range \(0\le r\le\lfloor n/2\rfloor\).

The proof does not address coefficient rings that are not division rings, and it does not infer an infinite theorem from finite experiments.
