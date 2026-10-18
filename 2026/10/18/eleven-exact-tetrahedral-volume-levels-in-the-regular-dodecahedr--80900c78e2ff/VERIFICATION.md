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

# Verification instructions and scope

Run `python3 verify.py` in the directory containing `verify.py` and `spectrum.csv`. The checker uses only the Python standard library, generates exactly twenty distinct dodecahedral vertices, and enumerates all \(\binom{20}{4}=4845\) unordered quadruples. It tests the frequency of all eleven exact determinant values, the fixed-vertex incidence table, individual Gram-determinant identities, and the exact squared-volume moment.

The coefficient pair \((a,b)\) denotes \(a+b\varphi\), where \(\varphi^2=\varphi+1\); each tetrahedral volume is its absolute determinant divided by six. The computation is exhaustive for vertex quadruples; it is not an unrestricted-inscription optimization and does not certify historical priority. The proof's second-moment cross-check is \(\sum\Delta^2=20^4=160000\). An independent external audit has not been performed.
