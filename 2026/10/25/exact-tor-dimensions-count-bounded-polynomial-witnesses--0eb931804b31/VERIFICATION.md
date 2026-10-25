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

# Mathematical verification and limits

1. Induction gives \(f^n(t,x_1,\ldots,x_m,y_1,\ldots,y_m)=(t+n,x_1,\ldots,x_m,y_1F_{1,n},\ldots,y_mF_{m,n})\).
2. Pullback of \((y_1,\ldots,y_m,P(x,t))\) is the stated ideal \(I_n\).
3. The regular-sequence hypothesis makes the Koszul complex a free resolution of \(R/I_n\); tensoring with \(R/J\) computes the required Tor group.
4. Under \(R/J\cong k[x_1,\ldots,x_m]\), the first \(m\) equations are \(H_n(x_i)=\prod_{j=0}^n(x_i-j)\). Characteristic zero makes each polynomial square-free, and the Chinese remainder theorem identifies their quotient with one copy of \(k\) per grid point.
5. First Koszul homology is the kernel of multiplication by \(P(x,n)\) on that product algebra. The kernel has dimension one at each zero coordinate and zero at every nonzero coordinate, proving the count identity.

Limits: the theorem is not asserted when the displayed generators fail to be a regular sequence. No independent audit or independent validation is claimed.
