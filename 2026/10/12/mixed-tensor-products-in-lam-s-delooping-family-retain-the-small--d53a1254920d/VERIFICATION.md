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

The symbolic proof checks the following chain.

1. Lam’s endpoint simple \(T_r\) has \(\operatorname{Ext}_{A_r}^i(T_r,A_r)\cong k\) only for \(i=1\) and \(i=r\).
2. Künneth therefore places the mixed Ext groups only in degrees \(2\), \(m+1\), \(n+1\), and \(m+n\), so degrees \(3\) through \(q=\min\{m,n\}\) vanish.
3. That vanishing makes the successive syzygy inclusions left projective approximations and reduces \(\Sigma^{q+1}\Omega^qS\) to the local module \(\Sigma^3\Omega^2S\).
4. The local projectives used in Lam’s three-step calculation have the same Loewy structure with unequal parameters, so the resulting module is supported on \(\{(1,1),(1,2),(2,1),(2,2)\}\).
5. The corresponding rectangular set \(\{(i,j):i\le m+1,\ j\le n+1\}\) is successor-closed, while the minimal total tensor resolution puts \((m+2,q+1)\) in \(\operatorname{supp}(\Omega^qS)\). This prevents the stable retract required for delooping level at most \(q\).

`verify_mixed_delooping.py` independently checks the Ext-degree convolution, successor closure, local projective supports, and uniqueness of the outside-support carrier for every \(2\le m,n\le12\). Its recorded output is `CHECK_OK pairs=121 range=2..12`.

The program does not certify the infinite theorem and is not used as a substitute for the symbolic argument. The theorem does not determine the exact delooping level of the tensor product.
