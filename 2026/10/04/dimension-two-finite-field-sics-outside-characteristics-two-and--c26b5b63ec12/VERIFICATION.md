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

The universal statement is verified analytically rather than by finite enumeration.

1. For four vectors in dimension two, trace gives \(4a=2c\), while the ETF parameter identity gives \(a(c-a)=3b\). In characteristic different from two and three this yields \(c=2a\) and \(b=a^2/3\).
2. If \(a=0\), then \(b=0\). A spanning family with all self- and cross-inner products zero would make the nondegenerate Hermitian form vanish on the full space, which is impossible. Therefore \(a\ne0\).
3. Surjectivity of \(z\mapsto z^{q+1}\) onto \(\mathbb F_q^{\times}\) permits global normalization to \((a,b,c)=(1,1/3,2)\).
4. With one vector sent to \((1,0)\), the other three have coordinate norms \(1/3\) and \(2/3\). Unimodular rescaling makes their first coordinates equal, leaving norm-one phases \(u_j\).
5. For a phase ratio \(t=u_i^{-1}u_j\), the cross-inner-product condition is
\[
N((1+2t)/3)=1/3,
\]
which is equivalent to \(t^2+t+1=0\). Since the characteristic is not three, this means \(t\) has order three.
6. The norm-one torus is cyclic of order \(q+1\), so such \(t\) exists exactly when \(3\mid(q+1)\), equivalently \(q\equiv2\pmod3\).
7. Conversely, choosing an order-three \(\omega\) and elements \(\mu,\rho\) of norms \(1/3\) and \(2/3\) gives the four explicit vectors. Direct multiplication checks common norm one, cross norm product \(1/3\), and frame operator \(2I\).

No finite experiment is used to extend these identities beyond their proved domain. Characteristics two and three remain outside the claim.
