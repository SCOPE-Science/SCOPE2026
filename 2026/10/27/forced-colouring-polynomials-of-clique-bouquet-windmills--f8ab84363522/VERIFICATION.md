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
# Reproducibility and verification

The finite verifier `verify.py` uses Python's standard library and no external data. From a directory containing both program and record, run `python verify.py` and compare its output to `verify_output.txt`.

It creates each clique-bouquet adjacency structure from its definition, enumerates proper total \(m\)-colourings, and for every restriction tests both the stated structural criterion and an iterative implementation of the exact local forcing rule. It checks every coefficient of the polynomial for the seven parameter pairs \((m,k)=(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(5,1)\). In addition, on \((3,1),(3,2),(3,3),(4,1),(4,2)\), it iterates through every possible partial assignment of the \(m\) named colours or the uncoloured symbol, testing success without reference to a known full colouring. The recorded execution ends `VERIFY_OK`.

These are finite checks. Correctness for all \(k\ge2,m\ge3\) rests on the step-by-step structural proof in `RESULT.md`. The singleton-petal checks are boundary consistency tests and do not represent a new claim about complete graphs.

There is no external independent audit or independent-validation certificate for this result.
