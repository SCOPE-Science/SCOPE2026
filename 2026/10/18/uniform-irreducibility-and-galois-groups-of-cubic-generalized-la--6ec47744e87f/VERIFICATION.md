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

The proof relies on monicity, the exact identity \(y^3=(a+3)(3y+2)\), and the elementary divisibility \(\gcd(y,3y+2)=\gcd(y,2)\). The only integral candidates arising in the odd and even cases lead to \(a+3\in\{0,1,2\}\), outside the asserted domain. Thus the infinite irreducibility assertion is proved rather than inferred from experiments.

The exact discriminant is \(108(a+2)(a+3)^2\). For an irreducible cubic, the square-discriminant criterion distinguishes the cyclic and symmetric Galois groups.

Run `python3 verify.py` with SymPy available to repeat the symbolic normalization, translation and discriminant checks, independent irreducibility checks for 513 specializations, and 60 further square-discriminant specializations. Recorded output is in `verification_output.txt`. Those checks do not exhaust the infinite range and are not a substitute for the proof.

The discriminant locus was identified in the 2013 paper cited in RESULT.md. The previously unavailable unrestricted irreducibility assertion is the focus of this result. Possible unindexed equivalent literature remains a residual originality risk.
