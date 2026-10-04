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
The claim was checked from the defining inequalities for \(K\)-frames and ordinary frames.

For a nonzero closed-range \(K\), \(R(K)=N(K^*)^\perp\), and \(K^*\) is bounded below on \(R(K)\). Hence every subfamily that is still a \(K\)-frame projects to a frame on \(R(K)\). This establishes \(E_K(\Phi)\le E(P_{R(K)}\Phi)\) without using the disputed identity.

If \(\Phi\) is near \(K\)-Riesz, deleting its finite exceptional set leaves a \(K\)-Riesz basis, whose projection is a Riesz basis of \(R(K)\); the projected excess and the \(K\)-excess therefore both equal the size of that exceptional set. If every atom already belongs to \(R(K)\), the coefficient identity \(\langle f,\varphi_i\rangle=\langle P_{R(K)}f,\varphi_i\rangle\) gives the converse deletion implication, so the excesses again agree.

For each \(N\ge2\), an orthogonal matrix can be chosen with first row \(N^{-1/2}(1,\ldots,1)\). Its columns form an orthonormal basis \((u_j)\) with \(|\langle e_1,u_j\rangle|^2=1/N\). With \(K\) the projection onto \(\operatorname{span}\{e_1\}\), deleting \(u_j\) and testing on \(u_j\) shows immediately that the remaining family is not a \(K\)-frame. Thus \(E_K=0\). Projection sends every \(u_j\) to \(N^{-1/2}e_1\), so the projected one-dimensional frame has excess \(N-1\).

The smallest case \(N=2\) was also checked explicitly with \(u_1=2^{-1/2}(1,1)\) and \(u_2=2^{-1/2}(1,-1)\). No finite enumeration is used to justify the arbitrary-dimensional statement.

The journal full text was inspected at Theorem 5.9 and equation (5.1). The source's near \(K\)-Riesz assertion is compatible with the corrected result; the contradiction concerns the unrestricted equality asserted for a \(K\)-frame. The review does not assess downstream statements and makes no claim for non-closed-range \(K\).
