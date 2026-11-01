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

# Reproducible finite verification

Run `python3 verify_q4_equivariant.py` with Python 3.10+ and no third-party packages. The output of the execution performed for this result is embedded in `verification_output.txt`, ending with `VERIFY_OK`.

The program enumerates all \(2^{16}\) vertex masks to test every face; checks the complete pivot matching on \(742\) nonempty faces and all \(2816\) cover relations; verifies that its reversed Hasse graph is acyclic; and independently computes unreduced mod-two boundary ranks. It enumerates every one of \(24\cdot16=384\) signed coordinate automorphisms and compares two independent signed Lefschetz procedures with the claimed character formula. It also counts the twenty signed cycle types and computes exact translation Fourier multiplicities.

The complete face scan and group enumeration prove only statements in the explicitly finite domain. The group module identification additionally uses the general semisimplicity theorem for finite rational representations. The matching theorem is the standard discrete Morse equivalence. These are mathematical arguments, not independent validation or an external certificate.
