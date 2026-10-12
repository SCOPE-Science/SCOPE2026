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

The exact checker `verify.py` works over rational numbers and verifies the Néron--Severi identities used in the proof: \(F^2=2\), \(B_i^2=-2\), pairwise disjointness of the \(B_i\), \(F=A_i+B_i\), and all relevant intersections. It also checks the arithmetic threshold behind the Cauchy--Schwarz contradiction and the \(1/4\) coefficient obstruction in the only possible fixed-part case.

The checker is auxiliary. Nefness is proved for all roots symbolically in `RESULT.md`; finite computation is not used as evidence for an infinite assertion. Base-point freeness uses the standard K3 linear-system criterion, and the covering-involution conclusion uses the degree-two morphism defined by a primitive nef square-two divisor.

No independent audit has been performed.
