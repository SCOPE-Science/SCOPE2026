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

The theorem is proved from a reflected-gap counting inequality and equality analysis; no unbounded assertion rests on finite enumeration. Run `python3 verify.py` with standard Python 3. The checker represents every possible numerical semigroup of Frobenius number \(F\) by a subset of its permitted integers below \(F\), tests addition and isolated gaps directly, and checks that no case beats the claimed bound. It checks complete classifications for \(3\le F\le20\), then validates every explicitly constructed family through \(F=300\).

The exhaustive check is finite, the code is ordinary reproducibility support, and no independent audit or external formal certification is asserted. The proof is meant to be checked separately, especially the disjointness of reflected intervals and their endpoint equalities in the even three-block case.
