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

The exact equations are copied from the cited Shimada--Veniani models after substituting \(\alpha=15/16\) in type I and \(\alpha=63\) in type II, moving all terms to one side, and clearing the denominator \(8\) in type I.

The accompanying `verify.py` checks, with exact SymPy arithmetic:

1. every displayed generator preserves the appropriate sextic polynomial exactly;
2. projective closure of the type-I generators has \(8\) elements;
3. its element-order distribution is \(1^1,2^5,4^2\), identifying \(D_8\);
4. projective closure of the type-II generators has \(24\) elements;
5. its element-order distribution is \(1^1,2^9,3^8,4^6\), identifying \(S_4\).

The finite computation does not by itself prove that no other projective automorphisms exist. Exhaustion instead uses the independent mathematical upper bound from Shimada--Veniani: the smooth Enriques surfaces represented by these sextics have full automorphism-group orders \(8\) and \(24\). Any projective stabilizer element lifts injectively to an automorphism of the smooth minimal Enriques model. Hence the explicit subgroups, already of the full allowed orders, are the complete projective stabilizers.

No independent audit has been performed.
