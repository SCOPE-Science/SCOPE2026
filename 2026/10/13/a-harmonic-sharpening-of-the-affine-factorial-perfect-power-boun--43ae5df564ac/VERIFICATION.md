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

The proof is symbolic. The computational check is limited to replaying the finite parameter arithmetic for representative prime powers; it is not used to infer the theorem for all \(m\).

`verify.py` computes \(R=\lceil e^{m-\gamma}\rceil\), the exact prime count \(\pi(R)\), \(K=1+(m-1)(R+\pi(R))\), the Davenport threshold \(D=1+(m-1)(K+R+\pi(R))\), and the exact floor sum
\[
M_0=\sum_{\ell=1}^R\left(\left\lfloor\frac K\ell\right\rfloor+1\right).
\]
For each tested prime power it checks \(D=mK\), \(M_0>D\), and \(D<2m(m-1)\lceil e^m\rceil\).

The replay output is:

`VERIFY_OK samples=9 max_m=13`

The largest sample is \(m=13\), where \(R=248398\), \(\pi(R)=21911\), \(D=42168217\), and \(M_0=42293605\).

Scientific limits: the numerical use of a high-precision decimal for \(\gamma\) is only to choose sample values of \(R\). The proof of the infinite claim uses the exact definition of Euler's constant and the strict inequality \(H_R>\log R+\gamma\), so numerical rounding is not a premise of the theorem.
