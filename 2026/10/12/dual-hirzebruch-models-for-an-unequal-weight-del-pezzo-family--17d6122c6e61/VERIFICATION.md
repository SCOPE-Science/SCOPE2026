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
The proof uses two inputs from the cited Kim--Won family: the exact weighted equation and quotient types, and the published intersection calculation for the curves through one quotient point. The second local calculation is obtained by the literal symmetry of the equation after interchanging the two weighted coordinates and their weights.

The local fiber check is exact: at a simple root, write \(f=s u(s)\) with \(u(0)\ne0\); then \(zt+s u(s)=0\) is smooth and its central fiber is the transverse union \(zt=0\). No finite enumeration is used to infer the number or type of fibers.

`verify.py` is an ancillary exact bookkeeping check. It verifies symbolically that \(d=a+b\), that the two sequences of elementary transformations change the section squares to \(+b,-b\) and \(+a,-a\), and that the blow-up formulas give \(\rho=d+2\) and \(K^2=8-d\). The global ruled-surface identification is established in the written proof, not delegated to the script.

Limits: the result assumes square-free \(f\) and \(1\le n<m\). The case \(n=0\) and collisions among the roots of \(f\) are not verified or claimed.
