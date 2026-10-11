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

Both embedded programs have been executed directly from their packaged paths using a standard Python interpreter and only its standard library.

Run `python verify_translation.py` and `python verify_local.py` in the unpacked directory. The first enumerates all simplices, signed invariant-face traces, character multiplicities and mod-two simplicial boundary ranks for \(n=3,5,7\), with additional exact dimension summations for \(n=9,11,13,15\). The second independently checks neighborhood overlap cardinalities, translated orbit incidence and weight-multiplicity identities for \(n=3,5,7\).

Results: reduced mod-two Betti ranks in degree two only are \(1,31,351\) for the three enumerated dimensions. The respective representation multiplicities by even Hamming weight are \( (1,0)\), \( (6,1,3)\) and \( (15,6,4,10)\). Mod-two computations cannot alone prove an integral or infinite theorem; the mathematical proof in RESULT.md supplies dimensional concentration, simple connectivity and exact rational character formulas for every odd dimension at least three. No independent audit or external certification has occurred.
