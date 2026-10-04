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

`verify_f25_index4.py` uses only exact integer arithmetic. It realizes \(\mathbb{F}_{25}=\mathbb{F}_5[a]/(a^2-2)\), checks that \(g=1+2a\) has order \(24\), forms \(H=\langle g^4\rangle\), and computes compressed Fourier entries in \(\mathbb{Z}[z]/(\Phi_{30}(z))\).

For character exponents \(j=0,1,2,3,4,5\), the exact zero-minor counts are respectively \(0,0,10,34,10,0\). The order-three cases have ten vanishing \(2\times2\) minors each. The order-two case has eight vanishing entries, eighteen vanishing \(2\times2\) minors, and eight vanishing \(3\times3\) minors. The trivial and order-six cases have none.

The replay performed before packaging ended with `VERIFY_OK`. This verifies the finite determinant computation only; it does not independently establish literature novelty.
