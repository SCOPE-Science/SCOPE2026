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
The exact replay is supplied in `verify.py`.

It reconstructs
\[
F_7(c)=\sum_{i=0}^{7}\binom{7}{i}\binom{c+i}{i},
\]
checks the degree-\(7\) factorization at enough integer points to certify the polynomial identity, verifies \(G(-8)=-147456=-2^{14}3^2\), and confirms \(4^7>5040\).

After the symbolic proof reduces all possible solutions to \(1\le c\le5032\), the script checks every value in that interval with exact integer arithmetic and finds no seventh power.
