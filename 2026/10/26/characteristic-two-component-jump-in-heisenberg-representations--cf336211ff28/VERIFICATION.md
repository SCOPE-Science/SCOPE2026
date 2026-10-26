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

The included Python 3 program constructs the actual four-by-four matrix commutators and checks each of the two Heisenberg identities across every first-superdiagonal pair over the fields of cardinalities 2, 3, 4 and 5. It checks the count predicted from the algebraic proof: base counts 46, 249, 1396 and 2185, with six further free matrix entries contributing a factor equal to the sixth power of the field size. The source uses only the Python standard library; run `python3 verify_heisenberg_n4.py`. These finite experiments check selected field orders and cannot certify infinitely many fields or geometric irreducibility, which are addressed by the proof in RESULT.md. No independent external audit has been performed.
