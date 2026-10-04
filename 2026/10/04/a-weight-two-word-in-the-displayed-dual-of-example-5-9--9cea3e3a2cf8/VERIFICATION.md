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
`artifacts/verify.py` uses only the Python standard library.

It reconstructs the displayed original and dual over \(\mathbb F_2\), using cyclic shifts modulo \(31\) and \(9\) and the source binary Gray ordering. It obtains ranks \(29\) and \(20\), verifies every cross inner product is zero, and confirms combined rank \(48\), hence hull dimension \(1\).

It verifies membership of the explicit word
\[
(0\mid\xi_2(1+x)),
\]
whose Gray weight is \(2\), and checks that none of the \(49\) binary unit vectors belongs to the dual. Finally it exhausts all \(2^{20}\) dual words and finds exactly \(36\) words of weight \(2\). Successful replay prints `VERIFY_OK`.
