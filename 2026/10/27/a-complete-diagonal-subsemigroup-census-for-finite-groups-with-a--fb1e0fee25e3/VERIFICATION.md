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

# Reproduction and scientific limits

Run `python verify.py` using Python 3 without additional dependencies. The program constructs multiplication tables and enumerates all reflexive relations directly for \(C_1,C_2,C_3,C_4\), and \(C_2\times C_2\); none of the brute-force closure checks assumes the normal form. Predicted values are independently obtained by enumerating subgroups and normal subgroups. For \(S_3\), all theoretically parametrized relations are constructed and checked for closure, uniqueness, symmetry and congruence, but not all arbitrary binary relations are enumerated (the latter search space is too large for this check).

Observed counts \((D,T,C)\): \(C_1:(4,2,2)\), \(C_2:(13,5,4)\), \(C_3:(13,5,4)\), \(C_4:(29,9,6)\), \(C_2\times C_2:(67,17,10)\), \(S_3:(62,12,6)\). The terminal success marker is `VERIFY_OK`.

The mathematical proof in `RESULT.md` treats arbitrary finite groups. The finite checks cannot establish general uniqueness or asymptotics. Independent mathematical audit has not been performed.
