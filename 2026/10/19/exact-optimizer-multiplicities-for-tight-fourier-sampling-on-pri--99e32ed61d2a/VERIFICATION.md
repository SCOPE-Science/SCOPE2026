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

Run `python3 verify.py` in the directory containing this file. The exact-integer enumerator loops through all nonempty frequency subsets for moduli \(2,4,8,3,9,5\), all required-level profiles, verifies the cyclotomic equal-child test, and compares the counted minimum-size masks with the predicted exponent. It also tests each minimizing frequency set's translation stabilizer and orbit count. The unbounded case is established by the proof, not the finite tests. The independent audit remains unperformed.
