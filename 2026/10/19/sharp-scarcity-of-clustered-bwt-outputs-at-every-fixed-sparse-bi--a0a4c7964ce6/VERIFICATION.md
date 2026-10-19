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

# Reproducible checks

Run `python3 verify.py` with standard Python 3. The program constructs all indexed binary words at every weight from four through six and at every length from weight plus one through twenty, independently sorts complete cyclic rotations, and checks the elementary properties needed by the proof. Its successful output is `ALL_CHECKS_PASS strings= 190890 weights=4..6 lengths=k+1..20`.

The independent finite implementation does not attempt to prove an asymptotic statement from experiments. The proof establishes the bound by counting the integer solutions of fixed linear relations among gap coordinates, and a matching lower bound via a positive-volume family with two largest equal gaps. Other BWT conventions (including terminal markers) were not verified. No external independent audit has been conducted.
