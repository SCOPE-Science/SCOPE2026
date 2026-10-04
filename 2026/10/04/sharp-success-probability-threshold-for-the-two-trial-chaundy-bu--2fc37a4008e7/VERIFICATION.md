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

The proof was checked by reconstructing the conditioning identity for an independent \(\operatorname{Bin}(2,p)\) increment and the adjacent binomial-mass ratio. Their substitution yields the exact sign factor whose unique interior zero is \(p=(k+m+1)/(2k+m+1)\).

`verify.py` uses only the Python standard library. It computes the two tail probabilities exactly as rational numbers for \(1\le k\le8\), \(0\le m\le5\), verifies the closed factorization, equality at the threshold, strict signs on either side, and the formula for the threshold's excess over \(1/2\). Running the file returns `VERIFY_OK`.

The computation is a stress test only. No finite enumeration is used to justify the theorem for unbounded \(k\) or \(m\). The literature check establishes only the inspected-source comparison described in the accompanying review and does not certify historical uniqueness.
