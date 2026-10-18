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

Run `python3 verify.py` from the directory containing this file and the verifier. The script requires only the Python standard library, constructs all local transitions rather than importing a cached certificate, checks the unique 147-state cyclic component, and reconstructs exact integer min-plus powers. It verifies \(D_{16}=D_9+6\) for every entry, so associativity gives the infinite periodic recurrence. It also computes all base traces, independently enumerates every code for prism orders three through eight, checks the local/global equivalence for all masks in orders seven and eight, and reconstructs explicit valid minimum witnesses. Expected final output line: `VERIFY_OK`. The full captured output is in `verification_output.txt`.

The exhaustive finite checks alone do not establish all orders; the infinite step is the verified finite matrix identity combined with min-plus associativity. Source overlap outside the inspected literature cannot be excluded. Independent audit: not performed.
