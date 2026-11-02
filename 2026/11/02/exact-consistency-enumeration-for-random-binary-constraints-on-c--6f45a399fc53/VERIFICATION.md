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

# Verification details

Run `python3 verify.py` with Python 3. The program recomputes the orbits of every one of the \(16\) Boolean \(2\times2\) matrices, checks the provided \(7\times7\) integer transition matrix, and checks its right-annihilator polynomial. It validates the closed recurrence against transfer counts for \(1\le n\le60\), and independently counts every edge-relation choice on the three- and four-cycles by direct checking of all assignments. An independent inclusion-exclusion calculation over nonempty families of vertex assignments gives the same two counts. Expected output:

`VERIFY_OK exhaustive_random_systems=69632 cycle_lengths=3,4 transfer_lengths=1..60 inclusion_exclusion_n=3,4 matrix_orbits=7 annihilator_exact=true`

These computations corroborate the proof but are not an independent audit and do not establish the infinite theorem by themselves. The proof in `RESULT.md` establishes the all-\(n\) claim from integer relations, the annihilator identity, exact base values, and recurrence uniqueness.
