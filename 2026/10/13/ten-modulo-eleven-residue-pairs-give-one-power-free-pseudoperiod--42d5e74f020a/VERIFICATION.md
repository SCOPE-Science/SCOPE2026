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

Run `python3 verify.py` beside `certificate.json`.

The checker reconstructs the fixed/variable \(11\)-residue template from the two morphism images. It examines all \(121\) ordered pairs of shift residues and, whenever a source or target lands on the variable residue, enumerates every independent bit assignment. Exactly twenty ordered classes survive.

For the \(3^+\)-power argument, the checker verifies a fixed opposite-bit residue for each nonzero shift modulo \(11\). It independently generates the six length-\(3\) Thue--Morse factors and exhausts every possible local factor required for periods \(1,2,3,4\). The remaining infinite cases are the explicit arguments in `RESULT.md`: a fixed residue mismatch when the period is not divisible by \(11\), and a forbidden Thue--Morse cube when it is.

A separate long-prefix stress test checks all certified parameter pairs with second shift at most \(300\). That stress test is not used as an infinite proof.

Independent audit has not been performed.
